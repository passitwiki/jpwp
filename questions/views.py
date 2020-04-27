from datetime import datetime
from typing import List

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Answer, Question


def questions(request):

    return HttpResponse("")
