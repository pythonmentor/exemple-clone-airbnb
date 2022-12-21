from django.db import models
from django.conf import settings


class Reservation(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    ordered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
    )

    def __str__(self):
        return f"Réservation du {self.datetime_created} par {self.ordered_by.username}"


class Accommodation(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="accomodations",
    )
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Availability(models.Model):
    date = models.DateField()
    accommodation = models.ForeignKey(
        "Accommodation",
        on_delete=models.CASCADE,
        related_name="availabilities",
    )
    reservation = models.ForeignKey(
        "Reservation", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "availabilities"

    def __str__(self):
        return f"{self.accommodation.name} ({self.date})"
