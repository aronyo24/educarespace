from django.contrib import admin
from django.urls import include, path
from .views import blog, classes, contact, gallery, home, about, team


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('classes/', classes, name='classes'),
    path('gallery/', gallery, name='gallery'),
    path('team/', team, name='team'),
    path('blog/', blog, name='blog'),
]
