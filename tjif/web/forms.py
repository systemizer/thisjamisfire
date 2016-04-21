from django.forms import ModelForm
from web.models import Jam

class JamForm(ModelForm):
    class Meta:
        model = Jam
        fields = ["track_url"]
