from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView

from .forms import CustomUserCreationForm, EventForm
from .models import Story, Event

User = get_user_model()


# Create your views here.
class HomePageView(ListView):
    # paginate_by = 5
    # descending order
    model = Story
    ordering = ['-id']

    context_object_name = 'stories'
    template_name = 'stories/home.html'


def story_detail(res, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(res, 'stories/detail.html', {'story': story})


def about(res):
    return None


def contact(res):
    return None


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"

    success_url = reverse_lazy('login')


@login_required
def logout_view(res):
    logout(res)
    return redirect(reverse_lazy('login'))


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['story_name', 'story_description', 'is_valid', 'story_image']
    template_name = 'stories/create.html'
    success_url = reverse_lazy('home')

    # use current login user as the default user when creating stories
    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'stories/add.html'

    def form_valid(self, form):
        story_id = self.kwargs['story_id']
        form.instance.story = get_object_or_404(Story, id=story_id)
        return super().form_valid(form)

    def get_success_url(self):
        # Assuming 'story_id' is the name of the URL pattern variable
        story_id = self.kwargs.get('story_id')
        return reverse('story_detail', args=[story_id])


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
