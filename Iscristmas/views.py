from django.shortcuts import render
import datetime

# Create your views here.
def Christmas(request):
    today = datetime.datetime.now()
    s=str(today.day)+"-"+str(today.month)
    return render(request, r'Christmas/Ch.html', context={'today':s})