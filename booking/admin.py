from django.contrib import admin

from .models import BookingRecord, PaymentRecord, Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "cost_per_hour"]


@admin.register(BookingRecord)
class BookingRecordAdmin(admin.ModelAdmin):
    list_display = [
        "room",
        "booking_from",
        "booking_until",
        "duration",
        "booking_type",
        "cost",
        "booking_user",
    ]


@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = ["booking_record", "amount", "created_at"]
