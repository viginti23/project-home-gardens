from django.contrib import admin
from .models import MaintenanceCategory, SizeCategory, Offer, OfferGalleryImage, OfferImage


admin.site.register(OfferImage)


class OfferImageInline(admin.TabularInline):
    model = OfferImage
    extra = 3


class OfferAdmin(admin.ModelAdmin):
    inlines = [OfferImageInline, ]


admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferGalleryImage)
admin.site.register(SizeCategory)
admin.site.register(MaintenanceCategory)
