from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Avg, F
from django.urls import reverse_lazy

from .models import TourCompany, Booking
from .forms import BookingForm


class CompanyListView(ListView):
    model = TourCompany
    template_name = 'horse_tour/horse_list.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_queryset(self):
        search = self.request.GET.get('q', '')

        companies = TourCompany.objects.all().annotate(
            avg_rating=Avg('reviews__rating')
        )

        if search:
            companies = companies.filter(name__icontains=search)

        return companies


class TourDetailView(DetailView):
    model = TourCompany
    template_name = 'horse_tour/tour_detail.html'
    context_object_name = 'tour'

    def get_object(self):
        obj = super().get_object()

        # 🔥 views +1 как у тебя было
        TourCompany.objects.filter(pk=obj.pk).update(views=F('views') + 1)

        return obj


class BookingListView(ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_list')


class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('booking_list')


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking/booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')