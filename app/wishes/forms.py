"""Wishes Forms."""

from typing import ClassVar

from django import forms

from .models import WellWish


class WellWishForm(forms.ModelForm):
    """Form for leaving a well-wish."""

    class Meta:
        model = WellWish
        fields = ("name", "relationship", "message")
        labels: ClassVar[dict[str, str]] = {
            "name": "Your name",
            "relationship": "How do you know them? (optional)",
            "message": "Your message",
        }
        widgets: ClassVar[dict[str, forms.Widget]] = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. Grace"}
            ),
            "relationship": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Mum, Auntie, Cousin",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Write something kind...",
                }
            ),
        }
