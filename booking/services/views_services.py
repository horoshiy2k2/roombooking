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


def get_booking_records_context(request):
    soft_booking_records = BookingRecord.objects.filter(
        booking_type=BookingRecord.SOFT
    )  # can add user filter here
    hard_booking_records = BookingRecord.objects.filter(
        booking_type=BookingRecord.HARD
    )  # can add user filter here

    context = {}
    context["soft_booking_records"] = soft_booking_records
    context["hard_booking_records"] = hard_booking_records
    return context


def create_soft_booking(request, room_id, form):
    booking_from = form.cleaned_data["booking_from"]
    booking_until = form.cleaned_data["booking_until"]
    isAvailable = validate_booking_period(booking_from, booking_until, room_id)
    print("Available: " + str(isAvailable))  # delete later
    if isAvailable:
        duration = get_duration(booking_from, booking_until)
        cost = calculate_cost(duration)

        booking_record, created = BookingRecord.objects.get_or_create(
            booking_user=request.user,
            room_id=room_id,
            booking_type=BookingRecord.SOFT,
            booking_from=booking_from,
            booking_until=booking_until,
            duration=duration,
            cost=cost,
        )


def validate_booking_period(start_dt, end_dt, room_id):
    min_period_duration_in_seconds = 5 * 60
    period_duration = get_duration(start_dt, end_dt)
    if end_dt < start_dt:
        return False
    if period_duration.seconds < min_period_duration_in_seconds:
        return False
    print(
        "isInClosedTime(start_dt, end_dt, room_id) = ",
        isInClosedTime(start_dt, end_dt, room_id),
    )
    if isInClosedTime(start_dt, end_dt, room_id):
        return False

    print(
        "isInBookedTime(start_dt, end_dt, room_id)",
        isInBookedTime(start_dt, end_dt, room_id),
    )
    if isInBookedTime(start_dt, end_dt, room_id):
        return False
    # if (not isInClosedDays(start_dt, end_dt, room_id)): return False
    # if (isOneDay())
    # check days

    # if ()
    # get_available_periods_list(day)

    return True


def isInBookedTime(start_dt, end_dt, room_id):
    room = Room.objects.get(id=room_id)
    booking_start_day = start_dt.date().day  # for one month available booking
    print("start_booking_day: ", booking_start_day)
    booking_records_in_the_same_day = BookingRecord.objects.filter(
        room_id=room_id,
        booking_from__day=booking_start_day,
        booking_type=BookingRecord.HARD,
    )

    print("booking_records_in_the_same_day", booking_records_in_the_same_day)

    # can put this into filter using gte and lte...
    for booking_recrod in booking_records_in_the_same_day:
        booking_from = booking_recrod.booking_from
        booking_until = booking_recrod.booking_until
        # check negative options. Only for the same day? no.
        if booking_from < start_dt < booking_until:
            return True
        if end_dt > booking_from and end_dt < booking_until:
            return True

    return False


def isInClosedTime(start_dt, end_dt, room_id):  # add check for days here? weekdays
    room = Room.objects.get(id=room_id)
    closed_from_time = room.closed_from
    closed_until_time = (
        room.closed_until
    )  # should validate from and until (not here) like f<u

    # reverse. start < end always already
    if start_dt.time() < closed_until_time or end_dt.time() > closed_from_time:
        return True

    return False


def get_duration(start_date_time, end_date_time):
    return end_date_time - start_date_time


def calculate_cost(duration):
    # implement
    return 5


def pay_for_booking(request):
    name_pay_button = "create payment record"
    if name_pay_button in request.POST:
        booking_record_id = request.POST.get("booking_record_id")
        booking_record = BookingRecord.objects.get(id=booking_record_id)
        PaymentRecord.objects.create(
            booking_record=booking_record, amount=booking_record.cost
        )
        booking_record.booking_type = (
            booking_record.HARD
        )  # can separate logic to other service
        booking_record.save()
