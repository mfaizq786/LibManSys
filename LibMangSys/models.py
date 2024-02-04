from django.db import models
from django.db.models.deletion import CASCADE
from datetime import date
# Create your models here.

class StudentRegistration(models.Model):
    fname = models.CharField('first name',max_length=30)
    lname = models.CharField('last name',max_length=30)
    enrollno = models.CharField('enrollmentno',max_length=30)
    branch = models.CharField('branch',max_length=10)
    image = models.ImageField(upload_to='images')
    username = models.CharField('username',max_length=30)
    password = models.CharField('password',max_length=20)
    def __str__(self):
        return self.username

class Book(models.Model):
    bookname = models.CharField('book name',max_length=30)
    authorname = models.CharField('author name',max_length=30)
    bookno = models.CharField('bookno',max_length=30)
    category = models.CharField('catogory',max_length=10)   
    quantity = models.IntegerField('quantity')
    def __str__(self):
        return self.bookname

class Issuedbook(models.Model):
    x = date.today()
    day = int(x.strftime('%d'))
    month = int(x.strftime('%m'))
    year = int(x.strftime('%Y'))
    sum = day + 2
    if sum > 30:
        month += 1
        day = sum - 30
    else:
        day = sum    
    y = date(year,month-1,day)

    studid = models.ForeignKey(StudentRegistration,on_delete=CASCADE)
    bookid = models.ForeignKey(Book,on_delete=CASCADE)
    enrollmentno = models.CharField(max_length=50)
    bookno = models.CharField(max_length=30)
    issuedate = models.DateField(default=x)
    returndate = models.DateField(default=y)
    fine = models.IntegerField(default=0)
    latedays = models.IntegerField(default=0)
    def __str__(self):
        return self.enrollmentno


