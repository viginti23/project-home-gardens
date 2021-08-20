from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import OfferGalleryImage, OfferImage
from PIL import Image


@receiver(post_save, sender=OfferImage)
def create_offer_gallery_image(sender, instance, created, **kwargs):
    if created:
        OfferGalleryImage.objects.create(gallery_image=instance.image, offer=instance.offer,
                                         offer_image=instance)
        old = instance.image
        new_gallery_image = Image.open(instance.offergalleryimage.gallery_image.path)
        if new_gallery_image.width > 500 or new_gallery_image.height > 250:
            output_size = (500, 250)
            new_gallery_image.thumbnail(output_size)
            new_gallery_image.save(instance.offergalleryimage.gallery_image.path)
        instance.image = old

@receiver(post_save, sender=OfferImage)
def save_offer_gallery_image(sender, instance, created, **kwargs):
    instance.offergalleryimage.save()
