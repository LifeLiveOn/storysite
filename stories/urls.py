from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('logout/',views.logout_view, name='logout'),
    path('story:id',views.story, name='story'),

]