from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('signup/',SignUpView.as_view(), name='signup'),
    # default login /login
    path('logout/',views.logout_view, name='logout'),
    path('story/<int:pk>/',views.StoryDetailView.as_view(), name='storyDetail'),
    path('create/',views.StoryCreateView.as_view(), name='create')
]