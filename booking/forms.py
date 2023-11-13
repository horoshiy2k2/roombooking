from django import forms

from booking.models import BookingRecord, PaymentRecord, Room


class BookingRoomForm(forms.Form):
    # room_id = forms.IntegerField()
    booking_from = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )
    booking_until = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = BookingRecord
        fields = (
            "title",
            "description",
            "creator",
            "start_date",
            "end_date",
        )  # no need?
