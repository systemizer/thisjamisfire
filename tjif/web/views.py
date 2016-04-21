from django.shortcuts import render_to_response
from django.template import RequestContext

from web.forms import JamForm
from web.models import Jam

def index(request):
    form = JamForm()
    if request.method == "POST":
        form = JamForm(request.POST)
        if form.is_valid():
            jam = form.save(commit=False)
            jam.user = request.user
            jam.save()
            

    jams = Jam.objects.all()

    return render_to_response("index.html", {'jams': jams, 'form': form }, RequestContext(request))
