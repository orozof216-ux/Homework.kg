from django.shortcuts import render
from .models import TourCompany
from django.db.models import Avg


def company_list(request):
    companies = TourCompany.objects.all().annotate(avg_rating=Avg('reviews__rating'))

    return render(request, 'horse_list.html', {
        'companies': companies
    })