from django.db import models
from django.db.models import IntegerField
from django.utils import timezone
import datetime




class Item(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    icon = models.FileField(upload_to="Item/")

    def __str__(self):
        return self.name


class AuctionItemPrice(models.Model):
    item = models.ForeignKey('Item', on_delete=models.PROTECT, related_name="+")
    price = models.PositiveIntegerField()
    amount = models.IntegerField(db_index=True)
    sold_at = models.DateTimeField(default=timezone.now)



class AuctionItemOrder(models.Model):
    item = models.ForeignKey('Item', on_delete=models.PROTECT, related_name="+")
    price = models.PositiveIntegerField()
    amount = models.IntegerField(db_index=True)
    sold_at = models.DateTimeField(default=timezone.now)






