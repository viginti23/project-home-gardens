from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import OfferGalleryImage, OfferImage


# @receiver(post_save, sender=OfferImage)
# def create_offer_gallery_image(sender, instance, created, **kwargs):
#     if created:
#         OfferGalleryImage.objects.create(image=instance)
#
#
# @receiver(post_save, sender=OfferImage)
# def save_offer_gallery_image(sender, instance, **kwargs):
#     instance.account.save()
