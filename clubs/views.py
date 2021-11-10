from django.shortcuts import render
from .models import Group, Groupnotices, Groupresults
from math import ceil


def clubs(request):
    allProds = []
    catprods = Group.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Group.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides)])
    params = {'allProds':allProds}
    return render(request, 'clubs/clubs.html',params)

def clubnotices(request):
    allProds = []
    catprods = Groupnotices.objects.values('notice_category', 'id')
    cats = {item['notice_category'] for item in catprods}
    for cat in cats:
        prod = Groupnotices.objects.filter(notice_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'clubs/clubnotices.html', params)

def clubdesc(request, myid):

    # Fetch the product using the id
    group = Group.objects.filter(id=myid)
    return render(request, 'clubs/clubsdesc.html', {'group':group[0]})

def clubresults(request):
    allProds = []
    catprods = Groupresults.objects.values('result_category', 'id')
    cats = {item['result_category'] for item in catprods}
    for cat in cats:
        prod = Groupresults.objects.filter(result_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'clubs/clubresults.html', params)


