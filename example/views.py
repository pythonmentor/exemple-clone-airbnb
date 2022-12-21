from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Availability, Reservation


def success(request):
    ids = request.session.get("availabilities", [])
    availabilities = Availability.objects.filter(id__in=ids)
    reservation_id = request.session.get("reservation")
    return render(
        request,
        "example/success.html",
        {
            "availabilities": availabilities,
            "reservation": Reservation.objects.get(id=reservation_id),
        },
    )


@login_required
def book(request):
    if request.method == "POST":
        ids = [int(i) for i in request.POST.getlist("availabilities")]
        availabilities = Availability.objects.filter(id__in=ids)
        for availability in availabilities:
            availability.reservation = Reservation.objects.create(
                ordered_by=request.user
            )
            availability.save()
        request.session["reservation"] = availability.reservation.id
        request.session["availabilities"] = ids
        return redirect("success")
    return redirect("home")


def search(request):
    startdate_str = request.GET.get("startdate")
    if startdate_str:
        startdate = datetime.strptime(startdate_str, "%Y-%m-%d")
    enddate_str = request.GET.get("enddate")
    if enddate_str:
        enddate = datetime.strptime(enddate_str, "%Y-%m-%d")
    availabilities = Availability.objects.filter(
        date__range=[startdate_str, enddate_str]
    )
    return render(
        request,
        "example/results.html",
        {
            "availabilities": availabilities,
        },
    )


def home(request):
    return render(request, "example/home.html")
