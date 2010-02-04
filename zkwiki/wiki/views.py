"""
Views for the 'wiki' Django application.
"""
from django.shortcuts import render_to_response


def home(request):
    """
    Default home page for the wiki app.
    """
    return render_to_response(
        'wiki/home.djhtml',
    )
