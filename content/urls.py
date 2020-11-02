from django.urls import path

from content.views import ProfileView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
]
