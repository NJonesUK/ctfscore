from django.shortcuts import *
from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from challenges.models import Challenge, ChallengeEntry

def index(request):
    return render_to_response("index.html")

@login_required
def profile(request):
    render_dict = {}
    render_dict['challenges'] = Challenge.objects.exclude(id__in = ChallengeEntry.objects.filter(user=request.user).values_list('id', flat=True))
    render_dict['completed_challenges'] = ChallengeEntry.objects.filter(user=request.user)
    render_dict['total_score'] = 0

    for entry in render_dict['completed_challenges']:
        render_dict['total_score'] += entry.challenge.points

    print render_dict
    return render_to_response("profile.html", render_dict)