from django.db import models

class News(models.Model): 
    headline = models.CharField(max_length=200) 
    body = models.TextField() 
    date = models.DateField()

    # This code shows the headline as the item name in the admin module
    def __str__(self):
       return self.headline


