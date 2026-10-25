"""Database models."""

from django.db import models


class WellWish(models.Model):
    """One well-wish message, live as soon as it is saved."""

    name = models.CharField(
        max_length=60,
        help_text="Who the wish is from, as it should appear on the card (e.g. Grace.",
    )
    relationship = models.CharField(
        max_length=40,
        blank=True,
        help_text="Optional. How you know them, shown beside your name (e.g. Mum, Auntie, Cousin).",
    )
    message = models.CharField(
        max_length=300,
        help_text="Write something kind...",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        help_text="When the wish was sent. Set automatically.",
    )

    class Meta:
        ordering = ("-created",)
        verbose_name_plural = "Well wishes"

    def __str__(self):
        """Label used in the admin: the name, then the start of the message.

        Examples::

            str(WellWish(name="Grace", message="You got this!"))  # "Grace: You got this!"
        """
        return f"{self.name}: {self.message[:40]}"
