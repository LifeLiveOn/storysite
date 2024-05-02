from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import CustomUserCreationForm
from .models import Story

User = get_user_model()


# Create your views here.
class HomePageView(ListView):
    # paginate_by = 5
    # descending order
    model = Story
    ordering = ['-id']

    context_object_name = 'stories'
    template_name = 'stories/home.html'


class StoryDetailView(DetailView):
    model = Story
    template_name = 'stories/detail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # No need to fetch events here as it can be accessed directly in the template using 'story.events.all'
        return context


def about(request):
    return None


def contact(request):
    return None


def login(request):
    return None


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("home"))


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['story_name', 'story_description', 'is_valid', 'story_image']
    template_name = 'stories/create.html'
    success_url = reverse_lazy('home')

    # use current login user as the default user when creating stories
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
