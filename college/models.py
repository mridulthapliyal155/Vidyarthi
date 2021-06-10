from django.db import models

class College(models.Model):
    college = models.CharField(max_length=100,default=None)
    college_pic = models.URLField(null=True)
    def __str__(self):
        return(self.college)

class Detail_college(models.Model):
    placement = models.IntegerField(default=None)
    year      = models.IntegerField(default=None)
    name      = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return('{} {}'.format(self.name,self.placement))

class Line_Chart(models.Model):
    Branch = models.CharField(max_length=100)
    placed = models.IntegerField()
    name = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return('{}'.format(self.name))

CITIES = [
    ('Kanpur','Kanpur'),
    ('Lucknow','Lucknow'),
    ('Varanasi','Varanasi'),
    ('Allahbad','Allahbad'),
    ('Greater Noida','Greater Noida'),
    ('Noida','Noida'),
    ('Ghaziabad','Ghaziabad'),
    ('Sultanpur','Sultanpur'),
    ('Gorakhpur','Gorakhpur'),
    ('Agra','Agra'),
    ('Jhansi','Jhansi'),
    ('Sadabad Jakhaiva','Sadabad Jakhaiva'),
    ('Raebareli','Raebareli'),
    ('Bareilly','Bareilly'),
    ('Muradanagar','Muradanagar'),
    ('Jaunpur','Jaunpur'),
    ('Amethi','Amethi'),
    ('Mathura','Mathura'),
    ('New Delhi','New Delhi'),
]


STATE = [
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Delhi','Delhi')
]

class College_Info(models.Model):
    rank = models.CharField(max_length=100)
    college_email = models.EmailField(max_length=100)
    max_placements = models.CharField(max_length=100)
    college_fees = models.CharField(max_length=100)
    name = models.ForeignKey(College,on_delete=models.CASCADE)
    description = models.TextField(max_length=1000,null=True,default=None)
    city       = models.CharField(choices=CITIES,max_length=100,null=True,default=None)
    state      = models.CharField(choices=STATE,null=True,default=None,max_length=100)

    def __str__(self):
        return ('{} rank is {}'.format(self.name,self.rank))

class College_Courses(models.Model):
    course = models.CharField(max_length=100)
    name   = models.ForeignKey(College,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

