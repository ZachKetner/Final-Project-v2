from django.db import models
import re, bcrypt
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use"
        if len(postData['fName']) < 2:
            errors['fNameShort'] = "First Name must be longer than 2 characters"
        if len(postData['lName']) < 2:
            errors['lNameShort'] = "Last Name must be longer than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8:
            errors['passwordShort'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['passwordMatch'] = "Password and Confirm Password do not match"
        return errors
    def login_validator(self, postData):
        print(postData)
        errors = {}
        checkuser = User.objects.filter(email = postData['email'])
        if len(checkuser)<1:
            errors['noUser'] = "Invaild Email and Password combination"
        elif not bcrypt.checkpw(postData['password'].encode(),checkuser[0].password.encode()):
            errors['passwordNoMatch'] = "Invalid Email and Password combination"
        return errors
    def user_edit_validator(self, postData, user):
        errors = {}
        if len(postData['fName']) <1:
            errors['FirstNameEmpty'] = "Must enter a first name."
        if len(postData['lName']) <1:
            errors['LastNameEmpty'] = "Must enter a last name."
        if len(postData['email']) <1:
            errors['EmailEmpty'] = "Must enter an email."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['Email'] = "Invalid email address."
        if len(User.objects.filter(email=postData['email']))>0:
            if user.email != postData['email']:
                errors['EmailExists'] = "There's a user already using this email address."
        return errors

class User(models.Model):
    fName = models.CharField(max_length=32)
    lName = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    skill = models.CharField(max_length=64, default='beginner')
    preferred_ride_distance = models.CharField(max_length=64, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()
