from django.shortcuts import render

def home_feed(request):
  return render(request, 'home_feed.html')