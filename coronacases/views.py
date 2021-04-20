from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
import requests
def cases(request):
    data=requests.get("https://api.covid19api.com/summary")
    item=data.json()
    items={
        'item':item['Countries'],
        'x':datetime.datetime.now()

    }
    return render(request,'index.htm',items)
