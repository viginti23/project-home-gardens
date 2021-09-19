from .filters import OfferFilter


class DetailSearchFilterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.offer_filter = OfferFilter()

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if response.context_data:
            response.context_data['offer_filter'] = self.offer_filter
        return response
