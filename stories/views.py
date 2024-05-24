import base64

from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView

from .forms import CustomUserCreationForm, EventForm
from .models import Story, Event

User = get_user_model()

# Create your views here.
class HomePageView(ListView):
    model = Story
    ordering = ['-id']
    context_object_name = 'stories'
    template_name = 'stories/home.html'


def story_detail(res, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(res, 'stories/detail.html', {'story': story})


def about(res):
    return render(res, 'stories/about.html')


def contact(res):
    return render(res, 'stories/contact.html')


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

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Handle cartoon image if available
        cartoon_image_data = self.request.POST.get('cartoon_image')
        if cartoon_image_data:
            format, imgstr = cartoon_image_data.split(';base64,')
            ext = format.split('/')[-1]
            image = ContentFile(base64.b64decode(imgstr), name='cartoon_image.' + ext)
            form.instance.story_image = image

        return super().form_valid(form)


class EventCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'stories/add.html'

    def test_func(self):
        story_id = self.kwargs['story_id']
        self.story = get_object_or_404(Story, id=story_id)
        return self.story.user == self.request.user

    def handle_no_permission(self):
        raise PermissionDenied("You do not have the permission to access this page")

    def form_valid(self, form):
        form.instance.story = self.story
        return super().form_valid(form)

    def get_success_url(self):
        story_id = self.kwargs.get('story_id')
        return reverse('story_detail', args=[story_id])


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'description', 'date', 'image']
    template_name = 'stories/add.html'

    def test_func(self):
        event_id = self.kwargs['pk']
        self.event = get_object_or_404(Event, id=event_id)
        return self.event.story.user == self.request.user

    def handle_no_permission(self):
        raise PermissionDenied("You do not have the permission to access this page")

    def form_valid(self, form):
        messages.success(self.request, 'This has been updated!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('story_detail', args=[self.event.story.id])
