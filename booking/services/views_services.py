from django.shortcuts import redirect

from booking.forms import BookingRoomForm
from booking.models import BookingRecord, PaymentRecord, Room


def get_room_list_context(request):
    room_list = Room.objects.all()
    context = {"rooms": room_list}
    return context


def get_room_detail_context(request, room_id):
    room = Room.objects.get(id=room_id)
    form = BookingRoomForm()
    context = {"room": room, "form": form}
    return context


def create_soft_booking(request, room_id, form):
    booking_from = form.cleaned_data["booking_from"]
    booking_until = form.cleaned_data["booking_until"]
    duration = get_duration(booking_from, booking_until)
    cost = calculate_cost(duration)

    booking_record, created = BookingRecord.objects.get_or_create(
        booking_user=request.user,
        room_id=room_id,  # should be object? get object using id
        booking_type=BookingRecord.SOFT,
        booking_from=booking_from,
        booking_until=booking_until,
        duration=duration,  # make function calculate_duration(dt1, dt2) or just duration = booking_until - booking_from
        cost=5,  # calculate
    )


def get_duration(start_date_time, end_date_time):
    return end_date_time - start_date_time


def calculate_cost(duration):
    # implement
    return 5
