from django.db import models
from datetime import date




class Spent(models.Model):
    CURRENT_MONTH = date.today().month
    MONTHS = (
        (1, 'Janvier'),
        (2, 'Février'),
        (3, 'Mars'),
        (4, 'Avril'),
        (5, 'Mai'),
        (6, 'Juin'),
        (7, 'Juillet'),
        (8, 'Août'),
        (9, 'Septembre'),
        (10, 'Octobre'),
        (11, 'Novembre'),
        (12, 'Décembre'),

    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    done_at = models.DateField()
    amount = models.FloatField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='spents')
    month = models.IntegerField(choices=MONTHS)


    def __str__(self):
        return f'{self.title}'


    def get_month(self):
        return self.MONTHS[self.month][1]

    def get_month_with_id(self):
        return f'{self.MONTHS[self.month][0]} - {self.MONTHS[self.month][1]}'

    def get_simple_title(self):
        if len(self.title) > 20:
            return f'{self.title[:20]}...'
        return self.title

    def get_amout(self):
        return f'{self.amount} €'

    def get_abs_amout(self):
        return str(self.amount).replace(',', '.')

    def get_user(self):
        return f'{self.user}'

    def get_current_month(self):
        return self.CURRENT_MONTH

