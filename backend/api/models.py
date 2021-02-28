from django.db import models
from django.utils.translation import gettext_lazy as _


# Payment model
class Payment(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Payment"


# Usage model
class Usage(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Usage"


# Currency model
class Currency(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Currency"


# Bill detail model
class Bill(models.Model):
    class BillType(models.TextChoices):
        INCOME = 'IN', _('Income')
        EXPENSE = 'EX', _('Expense')

    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    usage = models.ForeignKey(Usage, on_delete=models.CASCADE)
    bill_type = models.CharField(
        max_length=2,
        choices=BillType.choices,
        default=BillType.EXPENSE,
    )
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    note = models.TextField(null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Payment: {self.payment.name}, price: {str(self.price)}'

    class Meta:
        verbose_name = "Bill"