import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class CardSet(models.Model):
    set_title = models.CharField(max_length=50, default='Untitled Set')
    pub_date = models.DateTimeField('date set created', default=timezone.now)
    active = models.BooleanField('is the set active?', default=True)
    
    def __str__(self) -> str:
        return self.set_title


class Card(models.Model):
    question_text = models.CharField(default='', null=False, max_length=200)
    answer_text = models.CharField(default='', max_length=300)
    created_date = models.DateTimeField('date card created', default=timezone.now)
    rel_cardset = models.ForeignKey(CardSet, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.question_text