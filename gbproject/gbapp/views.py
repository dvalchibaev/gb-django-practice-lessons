import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, World!")


def about(request):
    logger.info('About page accessed')
    return HttpResponse("About us")



