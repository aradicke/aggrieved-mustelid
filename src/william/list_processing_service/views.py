from django.http import JsonResponse
from django.views import View


class list_processing_view(View):
    generic_response_dictionary = {"working": "you betcha", "swimming": "more or less"}

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.generic_response_dictionary)
