from django.urls import path
from . import views

urlpatterns = [
    path('entry/', views.entry_form_view, name='entry_form'),
    path('success/', views.success_view, name='success'),  # Define a success view if needed
]

