from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Avg, F

from .models import TourCompany, Booking
from .forms import BookingForm


def company_list(request):
    search = request.GET.get('q', '')

    companies = TourCompany.objects.all().annotate(
        avg_rating=Avg('reviews__rating')
    )

    if search:
        companies = companies.filter(name__icontains=search)

    paginator = Paginator(companies, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'horse_tour/horse_list.html', {
        'page_obj': page_obj,
        'search': search
    })


def tour_detail(request, pk):
    TourCompany.objects.filter(pk=pk).update(views=F('views') + 1)

    tour = get_object_or_404(TourCompany, pk=pk)

    return render(request, 'horse_tour/tour_detail.html', {
        'tour': tour
    })


def booking_list(request):
    bookings = Booking.objects.all()

    return render(request, 'booking/booking_list.html', {
        'bookings': bookings
    })


def booking_create(request):
    form = BookingForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('booking_list')

    return render(request, 'booking/booking_form.html', {
        'form': form
    })


def booking_update(request, id):
    booking = get_object_or_404(Booking, id=id)

    form = BookingForm(request.POST or None, instance=booking)

    if form.is_valid():
        form.save()
        return redirect('booking_list')

    return render(request, 'booking/booking_form.html', {
        'form': form
    })


def booking_delete(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()

    return redirect('booking_list')