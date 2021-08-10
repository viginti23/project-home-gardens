from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import UpdateView
from .models import Offer, OfferImage
from django.contrib.auth.decorators import login_required
from .forms import CreateOfferForm, CreateOfferImageForm, UpdateOfferImageForm
from django.contrib import messages
from django.views.generic import CreateView, FormView, DetailView, ListView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from PIL import Image, UnidentifiedImageError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required(login_url='login')
def offer_form_view(request):
    if request.method == 'POST':
        offer_form = CreateOfferForm(
            request.POST)
        image_form = CreateOfferImageForm(request.POST, request.FILES)
        pics = request.FILES.getlist('image')

        if offer_form.is_valid() and image_form.is_valid():
            offer_instance = offer_form.save(commit=False)
            offer_instance.seller_id = request.user.id
            offer_instance.save()

            for pic in pics:
                try:
                    img_instance = OfferImage(image=pic, offer=offer_instance)
                    
                    img_instance.save()

                    # new_pic = Image.open(img_instance.image.path)
                    # if new_pic.width > 500 or new_pic.height > 250:
                    #     output_size = (500, 250)
                    #     new_pic.thumbnail(output_size)
                    #     new_pic.save(img_instance.image.path)
                except UnidentifiedImageError:
                    messages.warning(request, 'Nie wszystkie zdjęcia zostały dodane!')
                    pass
            messages.success(request, 'Ogłoszenie zostało pomyślnie dodane!')
            return redirect('offerdetail', pk=offer_instance.id)
    offer_form = CreateOfferForm()
    image_form = CreateOfferImageForm()
    return render(request, 'home/offer_form_view.html', {'offer_form': offer_form, 'image_form': image_form})

def offer_detail_view(request, pk, *args, **kwargs):
    if request.method == 'GET':
        template = 'home/offer_detail_view.html'
        context = {}
        context['object'] = Offer.objects.get(id=pk)
        return render(request, template, context)

class OfferListView(ListView):
    model = Offer
    template_name = 'home/offer_list_view.html'
    context_object_name = 'offers'
    ordering = ['-date_posted']

class OfferUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ['title', 'description', 'negotiable', 'price']
    model = Offer
    template_name = 'home/offer_update_view.html'
    # form_class = CreateOfferForm
    def get(self, request, pk, *args, **kwargs):
        offer = Offer.objects.get(id=pk)
        offer_form = CreateOfferForm(instance=offer)
        
        current_images_forms = []
        current_offer_imgs = []
        curr_offer_imgs_urls = []

        # image below is an OfferImage object
        for offerimage in offer.offerimage_set.all():
            image_form = UpdateOfferImageForm(request.POST, request.FILES, instance=offerimage)
            current_images_forms.append(image_form)
            current_offer_imgs.append(offerimage)
            curr_offer_imgs_urls.append(offerimage.image.url)
            
        new_image_form = CreateOfferImageForm()
        template = 'home/offer_update_view.html'
        context = {}
        context['offer_form'] = offer_form
        context['curr_offer_imgs_urls'] = curr_offer_imgs_urls
        context['current_offer_imgs'] = current_offer_imgs
        context['current_images_forms'] = current_images_forms
        context['new_image_form'] = new_image_form
        return render(request, template, context)
    
    def post(self, request, pk, *args, **kwargs):
        if request.method == 'POST':
            offer_instance = None
            offer = Offer.objects.get(id=pk)
            offer_form = CreateOfferForm(request.POST, instance=offer)
            if offer_form.is_valid():
                    offer_instance = offer_form.save(commit=False)
                    offer_instance.seller_id = request.user.id
                    offer_instance.save()
                    self.get(request, pk)

            ############## DELETE SELECTED IMAGES ##################
            images_IDs_to_delete = request.POST.getlist('delete')
            for ID in images_IDs_to_delete:
                offerimage_obj = OfferImage.objects.get(id=int(ID))
                offerimage_obj.delete()
            ########################################################

            pics = request.FILES.getlist('image')
            for pic in pics:
                try:
                    img_instance = OfferImage(image=pic, offer=offer_instance)
                    img_instance.save()

                    ############### RESIZING IMAGES ###############
                    # new_pic = Image.open(img_instance.image.path)
                    # if new_pic.width > 500 or new_pic.height > 250:
                    #     output_size = (500, 250)
                    #     new_pic.thumbnail(output_size)
                    #     new_pic.save(img_instance.image.path)
                    ###############################################

                except UnidentifiedImageError:
                    messages.warning(request, 'Nie wszystkie zdjęcia zostały dodane!')
                    continue
            messages.success(request, 'Ogłoszenie zostało pomyślnie uaktualnione!')
            return redirect('offerdetail', pk=offer_instance.id)
        self.get(request, pk)


    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        offer = self.get_object()
        if self.request.user == offer.seller:
            return True
        return False



class OfferDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Offer
    success_url = '/'
    
    template_name = 'home/offer_confirm_delete.html'
    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.seller:
            return True
        return False
