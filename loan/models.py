from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.conf import settings
# Create your models here.


class Loan(models.Model):
    effectivity = models.DateTimeField(
        _("Effectivity"), auto_now=False, auto_now_add=False)
    years_to_pay = models.IntegerField(_("Years to pay"))
    base_amount = models.DecimalField(
        _("Base Amount"), max_digits=8, decimal_places=2)
    interest_rate = models.FloatField(_("Interest Rate"))
    total_amount = models.DecimalField(
        _("Total Amount"), max_digits=8, decimal_places=2)
    monthly = models.DecimalField(
        _("Monthly"), max_digits=8, decimal_places=2)
    member = models.ForeignKey("loan.Member", verbose_name=_(
        "Member"), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("loan")
        verbose_name_plural = _("loans")

    def __str__(self):
        return f"{self.effectivity}-{self.member}"

    def get_absolute_url(self):
        return reverse("loan_detail", kwargs={"pk": self.pk})


class Member(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name=_("User"), on_delete=models.CASCADE)
    unit = models.CharField(_("Unit"), max_length=200)

    class Meta:
        verbose_name = _("member")
        verbose_name_plural = _("members")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"pk": self.pk})


class Payment(models.Model):

    loan = models.ForeignKey("loan.Loan", verbose_name=_("Loan"),
                             on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(_("Amount"), max_digits=8, decimal_places=2)
    paydate = models.DateTimeField(
        _("Payment Date"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("payment")
        verbose_name_plural = _("payments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("payment_detail", kwargs={"pk": self.pk})
