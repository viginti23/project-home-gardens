from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView
from .models import Offer, OfferGalleryImage, OfferImage
from django.contrib.auth.decorators import login_required
from .forms import CreateOfferForm, CreateOfferImageForm, UpdateOfferImageForm
from django.contrib import messages
from django.views.generic import ListView, DeleteView, TemplateView
from PIL import Image, UnidentifiedImageError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import OfferFilter
from django.template.response import TemplateResponse


class AboutView(TemplateView):
    template_name = 'home/about.html'

class BlogView(TemplateView):
    template_name = 'home/blog.html'


@login_required(login_url='login')
def offer_form_view(request):
    if request.method == 'POST':
        offer_form = CreateOfferForm(request.POST)
        image_form = CreateOfferImageForm(request.POST, request.FILES)
        pics = request.FILES.getlist('image')

        if offer_form.is_valid() and image_form.is_valid():
            offer_instance = offer_form.instance
            offer_instance.seller_id = request.user.id
            offer_instance.save()
            for pic in pics:
                try:
                    img_instance = OfferImage.objects.create(offer=offer_instance, image=pic)
                    # img_instance = OfferImage(image=pic, offer=offer_instance)
                    # img_instance.save()
                    # SIGNALS
                    gallery_img_instance = OfferGalleryImage(
                        gallery_image=pic, offer=offer_instance, offer_image=img_instance)
                    gallery_img_instance.save()

                    # RESIZING IMAGES
                    new_pic = Image.open(gallery_img_instance.gallery_image.path)
                    if new_pic.width > 500 or new_pic.height > 250:
                        output_size = (500, 250)
                        new_pic.thumbnail(output_size)
                        new_pic.save(gallery_img_instance.gallery_image.path)
                except UnidentifiedImageError:
                    messages.warning(
                        request, 'Nie wszystkie zdjęcia zostały dodane!')
            messages.success(request, 'Ogłoszenie zostało pomyślnie dodane!')
            return redirect('offerdetail', pk=offer_instance.id)
    offer_form = CreateOfferForm()
    image_form = CreateOfferImageForm()
    context = {'offer_form': offer_form, 'image_form': image_form}
    template = 'home/offer_form_view.html'
    return TemplateResponse(request, template, context)


def offer_detail_view(request, pk, *args, **kwargs):
    if request.method == 'GET':
        template = 'home/offer_detail_view.html'
        context = {}
        obj = Offer.objects.get(id=pk)
        context['object'] = obj
        context['full_images'] = OfferImage.objects.filter(offer=obj)
        # print(context['offer_filter'])
        return TemplateResponse(request, template, context)


class OfferListView(ListView):
    model = Offer
    template_name = 'home/offer_list_view.html'
    context_object_name = 'offers'
    ordering = ['-date_posted']
    paginate_by = 10
    response_class = TemplateResponse

    def get_queryset(self):
        queryset = super().get_queryset()
        titlesearch = self.request.GET.get('titlesearch') or ''
        queryset = queryset.filter(title__icontains=titlesearch)
        offer_filter = OfferFilter(self.request.GET, queryset=queryset)
        queryset = offer_filter.qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # context['offer_filter'] = OfferFilter(self.request.GET, queryset=self.get_queryset())
        return context


class OfferUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    fields = ['title', 'description', 'negotiable', 'price']
    model = Offer
    template_name = 'home/offer_update_view.html'
    response_class = TemplateResponse

    def get(self, pk, **kwargs):
        offer = Offer.objects.get(id=pk)
        offer_form = CreateOfferForm(instance=offer)

        current_imgs_forms = []
        current_imgs = []
        current_imgs_urls = []

        for offer_image in offer.offerimage_set.all():
            image_form = UpdateOfferImageForm(self.request.POST, self.request.FILES, instance=offer_image)
            current_imgs_forms.append(image_form)
            current_imgs.append(offer_image.offergalleryimage)
            current_imgs_urls.append(offer_image.offergalleryimage.gallery_image.url)

        new_image_form = CreateOfferImageForm()

        template = self.template_name
        context = {'offer_form': offer_form, 'current_imgs_urls': current_imgs_urls, 'current_imgs': current_imgs,
                   'current_imgs_forms': current_imgs_forms, 'new_image_form': new_image_form}
        return render(self.request, template, context)

    def post(self, pk, **kwargs):
        if self.request.method == 'POST':
            offer_instance = None
            offer = Offer.objects.get(id=pk)
            offer_form = CreateOfferForm(self.request.POST, instance=offer)
            if offer_form.is_valid():
                offer_instance = offer_form.save(commit=False)
                offer_instance.seller_id = self.request.user.id
                offer_instance.save()
                self.get(pk)

            ############## DELETE SELECTED IMAGES ##################
            images_IDs_to_delete = self.request.POST.getlist('delete')
            for ID in images_IDs_to_delete:
                offerimage_obj = OfferImage.objects.get(id=int(ID))
                offerimage_obj.delete()
            ########################################################

            pics = self.request.FILES.getlist('image')
            for pic in pics:
                try:
                    img_instance = OfferImage(image=pic, offer=offer_instance)
                    img_instance.save()

                    #### SIGNALS ######
                    gallery_img_instance = OfferGalleryImage(
                        gallery_image=pic, offer=offer_instance, offer_image=img_instance)
                    gallery_img_instance.save()

                    ############### RESIZING IMAGES ###############
                    new_pic = Image.open(gallery_img_instance.gallery_image.path)
                    if new_pic.width > 500 or new_pic.height > 250:
                        output_size = (500, 250)
                        new_pic.thumbnail(output_size)
                        new_pic.save(
                            gallery_img_instance.gallery_image.path)
                    ###############################################

                except UnidentifiedImageError:
                    messages.warning(self.request, 'Nie wszystkie zdjęcia zostały dodane!')
                    continue
            messages.success(self.request, 'Ogłoszenie zostało pomyślnie uaktualnione!')
            return redirect('offerdetail', pk=offer_instance.id)
        self.get(pk)

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
    response_class = TemplateResponse
    template_name = 'home/offer_confirm_delete.html'

    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.seller:
            return True
        return False
