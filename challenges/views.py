from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from challenges.models import Challenge, ChallengeEntry
from challenges.forms import AnswerForm

@login_required
def leaderboard(request):
    render_dict = {}
    render_dict['user_scores'] = {}
    render_dict['users'] = User.objects.all()

    for user in render_dict['users'] :
        render_dict['user_scores'][user] = 0
        completed = ChallengeEntry.objects.filter(user=user)
        for challenge in completed:
            render_dict['user_scores'][user] += challenge.challenge.points

    print render_dict
    return render_to_response("leaderboard.html", render_dict)

@login_required
def challenge(request, challenge_id):
    challenge = Challenge.objects.get(pk=challenge_id)
    incorrect = False
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer'] == challenge.answer:
                print "correct answer!"
                ce = ChallengeEntry(challenge=challenge, user=request.user)
                ce.save()
                return HttpResponseRedirect('/accounts/profile') # Redirect after POST
            else:
                incorrect = True
    else:
        form = AnswerForm() # An unbound form

    render_dict = {'challenge': challenge, 'form': AnswerForm}
    render_dict['incorrect'] = incorrect

    return render_to_response("challenge.html", render_dict, context_instance=RequestContext(request))