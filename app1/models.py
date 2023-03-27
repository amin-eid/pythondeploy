from django.db import models
import re
class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['fname'])<5:
            errors['fname']="First Name should be at least 5 characters!"
        if len(postData['lname'])<5:
            errors['lname']="last Name should be at least 5 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['pwd'])<8:
            errors['pwd']="password should be at least 8 characters!"
        if postData['pwd'] !=postData['cpwd']:
            errors['cpwd']="Passwords don't match!"
        return errors
# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=45)
    lname=models.CharField(max_length=45)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
