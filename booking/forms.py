from django import forms

from booking.models import BookingRecord, PaymentRecord, Room


class BookingRoomForm(forms.Form):
    # room_id = forms.IntegerField()
    booking_from = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "value": "2023-11-14T18:30"}
        )
    )
    booking_until = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "value": "2023-11-14T22:30"}
        )
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
