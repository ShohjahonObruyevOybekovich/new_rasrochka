from datetime import date

from dateutil.relativedelta import relativedelta
from django.db import models


class User(models.Model):
    chat_id = models.BigIntegerField()
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Installment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="installments")
    product = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    starter_payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_months = models.IntegerField()  # Total number of installment months
    additional_fee_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Fee in percentage
    start_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('ACTIVE', 'Active'), ('COMPLETED', 'Completed')], default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product} ({self.user.full_name})"

    def calculate_overall_price(self):
        """
        Calculate the total price with the additional fee.
        """
        remaining_balance = self.price - self.starter_payment
        additional_fee = (remaining_balance * self.additional_fee_percentage) / 100
        return remaining_balance + additional_fee

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment amount.
        """
        overall_price = self.calculate_overall_price()
        return overall_price / self.payment_months

    def next_payment_date(self):
        """
        Calculate the next payment date based on the start date.
        """
        payments_made = self.payments.count()
        return self.start_date + relativedelta(months=payments_made + 1)

    def is_payment_overdue(self):
        """
        Check if a payment is overdue.
        """
        next_payment = self.next_payment_date()
        return date.today() > next_payment and self.status == "ACTIVE"

    def payment_history(self):
        """
        Returns a summary of the payment history for this installment.
        """
        payments = self.payments.all()
        total_paid = sum(payment.amount for payment in payments)
        remaining_balance = self.calculate_overall_price() - total_paid
        history = {
            "total_paid": total_paid,
            "paid_months": payments.count(),
            "remaining_balance": remaining_balance,
            "payments": [{"amount": payment.amount, "date": payment.payment_date} for payment in payments]
        }
        return history


class Payment(models.Model):
    installment = models.ForeignKey('Installment', on_delete=models.CASCADE, related_name="payments", null=True)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} for {self.installment.product} on {self.payment_date}"


