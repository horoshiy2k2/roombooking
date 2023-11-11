from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost_per_hour = models.FloatField(default=1)
    # closed hours # + new logic to set avaible times every day/week/month

    def __str__(self):
        return self.name


class BookingRecord(models.Model):
    SOFT = "S"
    HARD = "H"

    BOOKING_TYPE_CHOICES = [
        (SOFT, "Soft"),
        (HARD, "Hard"),
    ]

    booking_type = models.CharField(max_length=1, choices=BOOKING_TYPE_CHOICES)
    booking_user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_from = models.DateTimeField()
    booking_until = models.DateTimeField()
    duration = models.DurationField()  # auto calculate? where?
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    cost = models.FloatField()  # auto calculate
    # name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.room} - {self.booking_type} id={self.id}"


class PaymentRecord(models.Model):
    booking_record = models.ForeignKey(BookingRecord, on_delete=models.CASCADE)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment: {self.booking_record} - {self.amount}$ id={self.id}"
