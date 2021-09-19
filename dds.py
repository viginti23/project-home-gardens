import json
from home.models import Offer, OfferImage, OfferGalleryImage
from django.utils import timezone


def sd():  # send_data():
    with open('offers.json', encoding='utf-8') as o:
        offers_json = json.load(o)
        for offer in offers_json:
            offer['date_posted'] = timezone.now()
            offer = Offer(
                title=offer['title'],
                description=offer['description'],
                price=offer['price'],
                negotiable=offer['negotiable'],
                date_posted=offer['date_posted'],
                size_category=offer['size_category'],
                maintenance_category=offer['maintenance_category'],
                indoor=offer['indoor'],
                outdoor=offer['outdoor'],
                pet_friendly=offer['pet_friendly'],
                location=offer['location'],
                )
            offer.save()

            offer_image = OfferImage(offer=offer)
            offer_image.save()
            offer_gallery_image = OfferGalleryImage(offer=offer, offer_image=offer_image)
            offer_gallery_image.save()

    print('Data sent!')
    exit()


if __name__ == '__main__':
    sd()
