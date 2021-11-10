from django.shortcuts import render
from .models import Examination
from math import ceil


def index(request):
    allProds = []
    catprods = Examination.objects.values('roll_number', 'id')
    cats = {item['roll_number'] for item in catprods}
    for cat in cats:
        prod = Examination.objects.filter(roll_number=11911076)

        allProds.append([prod, range(1, 10)])
    params = {'allProds':allProds}
    return render(request, 'exams/index.html',params)

