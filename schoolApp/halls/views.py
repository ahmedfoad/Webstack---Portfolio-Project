from django.forms import BaseModelForm
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from halls.models import Hall, Video
from .forms import VideoForm, SearchVideoForm
import urllib
from django.forms.utils import ErrorList

YOUTUBE_API_KEY = "AIzaSyCYFRWf0cWb_ze3evzrOMPsl2kqbADchhY"

def home(request):
    return render(request, "halls/home.html")


def dashboard(request):
    return render(request, "halls/dashboard.html")


def add_video(request, pk):
    form = VideoForm()
    search_form = SearchVideoForm()
    # Make sure the Hall exists and get it
    hall = Hall.objects.get(pk=pk)
    if not request.user == hall.user:
        raise Http404

    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = Video()
         
            new_video.url = form.cleaned_data["url"]
            parsed_url = urllib.parse.urlparse(form.cleaned_data["url"])
            new_video.youtube_id = form.cleaned_data["youtube_id"]
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            new_video.title = form.cleaned_data["title"]
            new_video.hall = hall
            

            if video_id:
                new_video.youtube_id = video_id[0]
                new_video.title =
                new_video.save()  # Save the Video instance to the database

            # Redirect or show a success message after saving
            # Replace 'some_success_url' with the name of the URL you want
            # to redirect to
            return redirect("home")
    else:
        form = VideoForm()

    # Render the form page again if GET request or if form is invalid
    return render(
        request,
        "halls/add_video.html",
        {"form": form, "search_form": search_form, "hall": hall, "pk": pk},
    )


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get("username"),
        form.cleaned_data.get(
            "password1"
        )
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class CreateHall(generic.CreateView):
    model = Hall
    fields = ["title"]
    success_url = reverse_lazy("home")
    template_name = "halls/create_hall.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect("home")


class DetailHall(generic.DetailView):
    model = Hall
    template_name = "halls/detail_hall.html"


class UpdateHall(generic.UpdateView):
    model = Hall
    fields = ["title"]
    template_name = "halls/update_hall.html"
    success_url = reverse_lazy("home")


class DeleteHall(generic.DeleteView):
    model = Hall
    template_name = "halls/delete_hall.html"
    success_url = reverse_lazy("home")
