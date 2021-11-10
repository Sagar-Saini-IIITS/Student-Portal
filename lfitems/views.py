from django.shortcuts import render
from .models import LF
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catprods = LF.objects.values('item_category', 'id')
    cats = {item['item_category'] for item in catprods}
    for cat in cats:
        prod = LF.objects.filter(item_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'lfitems/index.html', params)