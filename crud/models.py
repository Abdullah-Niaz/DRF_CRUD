from django.db import models

# Create your models here.


class Transcations(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    transcation_type = models.CharField(max_length=100, choices=(
        ("CREDIT", "CREDIT"), ("DEBIT", "DEBIT")))

    def save(self, *args, **kwargs):
        if self.transcation_type == "DEBIT":
            self.amount = self.amount * -1

        return super().save(*args, **kwargs)
