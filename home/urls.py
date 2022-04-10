from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<url>/', views.getPost, name='blog-post'),
    # path('category/<url>/', views.getCategory, name='blog-category'),
    path('about/', views.aboutPage, name='blog-about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
