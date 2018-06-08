from django.db import models
from django_mysql.models import JSONField

# table containing the pair of values survey/key needed to access a questionnaire from the homepage

class surveyauth(models.Model):
    key = models.CharField(max_length = 20, primary_key = True)
    survey = models.CharField(max_length = 255)

# table containing list of survey submissions

class surveysubmission(models.Model):
    surveyJSON = JSONField()