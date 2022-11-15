from django.http import JsonResponse, HttpResponse
from django.views import View
import requests


class main_external_view(View):
    def get(self, request, *args, **kwargs):

        go_get_data = requests.get("http://internal-apis:8000/lps/process")

        if go_get_data.status_code != 200:
            return HttpResponse(
                f"<p>There was a problem of the {go_get_data.status_code} variety</p>"
            )
        else:
            return HttpResponse(go_get_data)
