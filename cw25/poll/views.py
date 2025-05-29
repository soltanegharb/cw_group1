from django.shortcuts import render, redirect, HttpResponse
from poll.models import Poll, Choice
import datetime

def show_question(request):

    today = datetime.datetime.today().date()
    voted = request.session.get('voted')
    if voted == today:
        return redirect('already_vote')
    
    if request.method == 'POST':
        
        request.session['voted'] = today
    else:
        poll = Poll.objects.get(publish_date=today)
        choices = Choice.objects.filter(question=poll)
        
        context = {'poll': poll, 'choices': choices}
        return render(
            request,
            'poll.html',
            context
        )
    

def already_vote(rquest):
    return HttpResponse('you have already voted tody. please comeback tomorrow!')