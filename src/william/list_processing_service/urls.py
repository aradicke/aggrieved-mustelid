from django.urls import path
from list_processing_service.views import list_processing_view

urlpatterns = [
    path("process", list_processing_view.as_view(), name="list_processing_view"),
]
