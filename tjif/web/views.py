from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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
            

    myjams = Jam.objects.filter(user=request.user)
    
    return render_to_response("add-jam.html", {'myjams': myjams, 'form': form }, RequestContext(request))

def follow(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404

    following = user in request.user.profile.following.all()
    if following:
        request.user.profile.following.remove(user)
    else:
        request.user.profile.following.add(user)        
        
    return HttpResponseRedirect(reverse("web:profile", kwargs={"username": user.username}))
    

def discover(request):
    profile = request.user.profile
    myjams = Jam.objects.filter(user=request.user)[:10]
    followingjams = Jam.objects.filter(user__in=profile.following.all())[:10]
    recentjams = Jam.objects.all().order_by("-created")[:10]
    return render_to_response("discover.html",
                              {'myjams': myjams,
                               'recentjams': recentjams,
                               'followingjams': followingjams},
                              RequestContext(request))

def profile(request, username=None):
    if not username:
        user = request.user
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    jams = Jam.objects.filter(user=user)[:20]
    following = user in request.user.profile.following.all()
    return render_to_response("profile.html", {'user': user, 'jams': jams, 'following': following }, RequestContext(request))

def jam(request, jam_id):
    try:
        jam = Jam.objects.get(id=jam_id)
    except:
        raise Http404

    return render_to_response("jam.html",{'jam':jam}, RequestContext(request))
