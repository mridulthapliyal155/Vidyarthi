from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    RATING_CHOICES = (
        ('Bad','Bad'),
        ('Average','Average'),
        ('Excellent','Excellent'),
    )
    RECOMMEND = (
        ('Yes','Yes'),
        ('No','No')
    )
    rating              = models.CharField(max_length=100,choices=RATING_CHOICES,verbose_name='How much do you want to rate our website',default=None)
    know_us             = models.CharField(max_length=100,verbose_name='How do you know about this website?',default=None,blank=True,null=True)
    recommend           = models.CharField(max_length=10,choices=RECOMMEND,verbose_name='Do you recommend this website to your friends',default=None,blank=True,null=True)
    suggestion          = models.TextField(max_length=1000,verbose_name='Give your suggestions about how we can make this website even more good',default=None)
    reviewer            = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return('{} reviewer'.format(self.reviewer))


class Seconday_model(models.Model):
    BOOLEAN = (
        ('Yes','Yes'),
        ('No','No')
    )
    interest            = models.CharField(max_length=100,verbose_name='What is your subject of interest?')
    college             = models.CharField(max_length=100,verbose_name='What is your dream college?',null=True,blank=True)
    interest_college    = models.CharField(max_length=100,choices=BOOLEAN,verbose_name='Are you going to your subject of interest type of college?')
    if_college          = models.CharField(max_length=100,choices=BOOLEAN,verbose_name='Did you go to your dream college?',null=True,blank=True)
    reason              = models.TextField(max_length=1000,verbose_name="Can you give any reason why you didn't get your dream college or subject of type of interest college.",default=None)
    student             = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return('{} student review'.format(self.student))

