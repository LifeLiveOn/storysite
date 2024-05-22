from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm
from .views import SignUpView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup/', SignUpView.as_view(), name='signup'),
    # default login /login
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html",
                                                authentication_form=LoginForm), name='login'),
    path('story/<int:story_id>/', views.story_detail, name='story_detail'),
    path('create/', views.StoryCreateView.as_view(), name='create'),
    path('add/<int:story_id>', views.EventCreateView.as_view(), name='add_event'),
    path('edit_event/<int:pk>', views.EventUpdateView.as_view(), name='edit_event'),
]
