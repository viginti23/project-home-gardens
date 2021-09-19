from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import OfferGalleryImage, OfferImage
from PIL import Image

#
# @receiver(post_save, sender=OfferImage)
# def create_offer_gallery_image(sender, instance, created, **kwargs):
#     if created:
#         ins = OfferGalleryImage.objects.create(
#             offer_image=instance, gallery_image=instance.image, offer=instance.offer)
#         ins.save()
# #
#
# @receiver(post_save, sender=OfferImage)
# def save_offer_gallery_image(sender, instance, **kwargs):
#     new_pic = Image.open(instance.offergalleryimage.path)
#     if new_pic.width > 500 or new_pic.height > 250:
#         output_size = (500, 250)
#         new_pic.thumbnail(output_size)
#         new_pic.save(instance.offergalleryimage.gallery_image.path)
#
#     instance.offergalleryimage.save()
