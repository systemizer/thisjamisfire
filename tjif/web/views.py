from django.shortcuts import render_to_response
from django.template import RequestContext

from web.forms import JamForm
from web.models import Jam

def index(request):
    return render_to_response("index.html", RequestContext(request))

def add_jam(request):
    form = JamForm()
    if request.method == "POST":
        form = JamForm(request.POST)
        if form.is_valid():
            jam = form.save(commit=False)
            jam.user = request.user
            jam.save()
        return render_to_response("add-jam-finish.html", {'jam': jam}, RequestContext(request))
            

    jams = Jam.objects.all()
    
    return render_to_response("add-jam.html", {'jams': jams, 'form': form }, RequestContext(request))

def discover(request):
    return render_to_response("discover.html", RequestContext(request))

def profile(request):
    return render_to_response("profile.html", RequestContext(request))
