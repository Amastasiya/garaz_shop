from django.shortcuts import render
from django.http import HttpResponse

import json


def index(requeest):

    return render(
        requeest,
        'mainpage/index.html',

    )