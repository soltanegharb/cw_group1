from django.db import models


class Poll(models.Model):
    question = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class Choice(models.Model):
    poll = models.ForeignKey(to=Poll, on_delete=models.CASCADE)
    choice_text = models.TextField()
    vote_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text}"
