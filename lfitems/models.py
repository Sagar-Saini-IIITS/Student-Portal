from django.utils import timezone
from django.db import models

# Create your models here.
class LF(models.Model):
    item_id=models.AutoField
    item_name=models.CharField(max_length=50, default="")
    item_category= models.CharField(max_length=50, default="")
    item_desc=models.CharField(max_length=300, default="")
    item_image= models.ImageField(upload_to="lfitems/lostfound",null=True, blank = True)
    pub_date = models.DateTimeField()
    item_document= models.FileField(upload_to="lfitems/lostfound",null=True, blank = True)

    def __str__(self):
        return self.item_name
