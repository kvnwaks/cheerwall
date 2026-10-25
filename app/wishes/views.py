"""Views."""

from django.conf import settings
from django.shortcuts import redirect, render

from .forms import WellWishForm
from .models import WellWish


def carousel(request):
    """Show every wish in a carousel, newest first.

    Examples::

        GET /kpsea-wishes/  # carousel.html with all wishes
    """
    context = {"wishes": WellWish.objects.all(), "student": settings.STUDENT_NAME}
    return render(request, "wishes/carousel.html", context)


def add(request):
    """Show the form, and save the wish on a valid POST.

    Examples::

        GET /kpsea-wishes/add/   # empty form
        POST /kpsea-wishes/add/  # saves the wish, redirects to /kpsea-wishes/thanks/
    """
    form = WellWishForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("thanks")
    context = {"form": form, "student": settings.STUDENT_NAME}
    return render(request, "wishes/add.html", context)


def thanks(request):
    """Thank the sender and link back to the carousel.

    Examples::

        GET /kpsea-wishes/thanks/  # thanks.html
    """
    return render(request, "wishes/thanks.html", {"student": settings.STUDENT_NAME})
