from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from poll.models import Poll, Choice
import datetime
from poll.forms import PostForm

def show_question(request):

    today = datetime.datetime.today().date()
    print(today)
    voted = request.session.get('voted')
    if voted == today:
        return redirect('already_vote')
    
    if request.method == 'POST':
        fo
        request.session['voted'] = today
        poll = Poll.objects.get(publish_date=today)
        poll_question = poll.question
        choices = Choice.objects.filter(poll=poll)
        
        context = {'poll': poll_question, 'choices': choices}
        return render(
            request,
            'poll.html',
            context
        )


        # return redirect(reverse('poll:show_question'))
    else:
        poll = Poll.objects.get(publish_date=today)
        poll_text = poll.question
        choices = Choice.objects.filter(poll=poll)
        
        context = {'poll': poll_text, 'choices': choices}
        return render(
            request,
            'poll.html',
            context
        )
    

def already_vote(request):
    return HttpResponse('you have already voted tody. please comeback tomorrow!')
