from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def current_datetime(request):
    now = timezone.now()
    html = f"<html><body>Current date and time: {now}</body></html>"
    return HttpResponse(html)
