from django.contrib import admin
from .models import Offer, OfferGalleryImage, OfferImage


admin.site.register(OfferImage)


class OfferImageInline(admin.TabularInline):
    model = OfferImage
    extra = 3


class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferImageInline, ]


admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferGalleryImage)
