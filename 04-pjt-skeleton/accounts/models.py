<<<<<<< HEAD
import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class StockInterest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name = 'stock_interests')
    stock = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'stock'], name='unique_user_stock')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.stock}"
=======
from django.db import models

# Create your models here.
>>>>>>> dahye2-dev
