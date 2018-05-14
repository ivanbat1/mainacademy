from django.db import models

# Create your models here.
class Room(models.Model):

    area = models.IntegerField()
    room = models.IntegerField()
    coins = models.IntegerField()
    rent_buy = models.BooleanField()
    day_rent = models.IntegerField(null = True)
    comment = models.CharField(max_length = 200)


    def __str__(self):
        return "{} {} {} {} {} {}".format(self.area, self.room, self.coins, self.rent_buy, self.day_rent, self.comment)


