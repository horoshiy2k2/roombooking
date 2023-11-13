from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("", views.RoomListView.as_view(), name="room_list"),
    path("room/<int:room_id>/", views.RoomDetailView.as_view(), name="room_detail"),
    path(
        "booking_records/", views.BookingRecordsView.as_view(), name="booking_records"
    ),
]
