from .models import Offer, OfferImage
from django import forms

class CreateOfferForm(forms.ModelForm):
    
    class Meta:
        model = Offer
        fields = ['title', 'description', 'price',
                  'negotiable']


class CreateOfferImageForm(forms.ModelForm):
    class Meta:
        model = OfferImage
        fields = ['image', ]
        widgets = {'image': forms.ClearableFileInput(
                            attrs={'multiple': True})}


class UpdateOfferImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget = forms.ClearableFileInput()
        self.fields['image'].widget.clear_checkbox_label = 'Usuń zdjęcie'
        self.fields['image'].widget.attrs['hidden'] = True
        self.fields['image'].widget.attrs['multiple'] = True

    class Meta:
        model = OfferImage
        fields = ['image', ]
        # widgets = {'image': forms.ClearableFileInput()}
