from django.urls import path

from . import views


urlpatterns = [
    path('<slug:file_name>/', views.get_content)
]
