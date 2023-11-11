from django import forms

from booking.models import BookingRecord, PaymentRecord, Room


class BookingRoomForm(forms.Form):
    # room_id = forms.IntegerField()
    booking_from = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    booking_until = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))


# class CourseCreationForm(forms.ModelForm):
#     modules = forms.ModelMultipleChoiceField(
#         queryset=Module.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False,
#     )

#     title = forms.CharField(max_length=100)
#     description = forms.CharField(widget=forms.Textarea, max_length=200)

#     start_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
#     end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

#     class Meta:
#         model = Course
#         fields = ("title", "description", "creator", "start_date", "end_date")
