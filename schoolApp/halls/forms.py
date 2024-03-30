from .models import Video
from django import forms


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["url"]
        labels = {
            "url": "Video URL",
            "youtube_id": "Youtube ID",
            "title": "Video Title",
        }


class SearchVideoForm(forms.Form):
    query = forms.CharField(label="Search for a video", max_length=255)
