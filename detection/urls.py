from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload'),
    path('webcam/', views.webcam_view, name='webcam'),
    path('analyze_frame/', views.analyze_frame, name='analyze_frame'),
]
