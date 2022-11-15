from django.urls import path
from edge_face.views import main_external_view

urlpatterns = [
    path("", main_external_view.as_view(), name="main_external_view"),
]
