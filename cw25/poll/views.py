from django.shortcuts import render
from poll.models import Poll, Choice
import datetime

def show_question(request):
    if request.method == 'POST':
        pass
    else:
        today = datetime.datetime.today().date()
        poll = Poll.objects.get(publish_date=today)
        choices = Choice.objects.filter(question=poll)
        context = {'poll': poll, 'choices': choices}
        return render(
            request,
            'poll.html',
            context
        )