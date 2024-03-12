from django.shortcuts import render


# Create your views here.
def deeXs(request):
    return render(request, "deeXs/deex_list.html")
