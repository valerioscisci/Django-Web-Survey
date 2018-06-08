from django.shortcuts import render
from django.views.generic import TemplateView
from websurvey.models import surveyauth, surveysubmission
from django.http import QueryDict, HttpResponse
import json

# View for the Homepage

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'Home.html', context=None)

# View for the Cross Border Survey

class CrossBorderView(TemplateView):
    obj = surveyauth.objects.get_or_create(key='crossborder2018', survey='Cross Border')
    template_name = "crossborder.html"

# Method used to check if the key inserted by the user to access a survey is correct

def check_key(request):

    response_data = {}

    try:
        AccessCode = surveyauth.objects.get(key=QueryDict(request.body).get('key'), survey=QueryDict(request.body).get('survey'))
    except surveyauth.DoesNotExist:
        AccessCode = "fail"

    if AccessCode == "fail":
        response_data['msg'] = 'Not Found'
    else:
        response_data['msg'] = 'Found'

    return HttpResponse (
        json.dumps(response_data),
        content_type='application/json'
    )

# Method used to save a survey json result in the DB

def save(request):

    response_data = {}

    s = surveysubmission(surveyJSON = QueryDict(request.body).get('survey'))
    s.save()
    response_data['msg'] = 'Saved'

    return HttpResponse (
        json.dumps(response_data),
        content_type='application/json'
    )