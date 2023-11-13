from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from .forms import BookingRoomForm
from .services.views_services import (
    create_soft_booking,
    get_booking_records_context,
    get_room_detail_context,
    get_room_list_context,
    pay_for_booking,
)


class RoomListView(View):
    template_name = "booking/room_list.html"

    def get(self, request):
        context = get_room_list_context(request)
        return render(request, self.template_name, context)


class RoomDetailView(View):
    template_name = "booking/booking_detail.html"

    def get(self, request, room_id):
        context = get_room_detail_context(request, room_id)
        return render(request, self.template_name, context)

    def post(self, request, room_id):
        form = BookingRoomForm(request.POST)

        if form.is_valid():
            create_soft_booking(request, room_id, form)

        room_detail_url = reverse("booking:room_detail", args=[room_id])
        return redirect(room_detail_url)


class BookingRecordsView(View):
    template_name = "booking/booking_records.html"

    def get(self, request):
        context = get_booking_records_context(request)
        return render(request, self.template_name, context)

    def post(self, request):
        pay_for_booking(request)
        return redirect("booking:booking_records")
