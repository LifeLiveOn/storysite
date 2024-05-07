from django.urls import path
from . import views
from .views import SignUpView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # default login /login
    path('logout/', views.logout_view, name='logout'),
    path('stories/login/', auth_views.LoginView.as_view(template_name="registration/login.html",
                                                        authentication_form=LoginForm)
         , name='login'),
    path('story/<int:story_id>/', views.story_detail, name='story_detail'),
    path('create/', views.StoryCreateView.as_view(), name='create')
]
