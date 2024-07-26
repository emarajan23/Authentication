from django.db import models

class Device(models.Model):
    
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    release_year = models.PositiveIntegerField()
    os = models.CharField(max_length=50)
    display_size = models.FloatField()  
    ram = models.PositiveIntegerField()  
    storage = models.PositiveIntegerField()  
    battery_capacity = models.PositiveIntegerField()  
    main_camera = models.PositiveIntegerField()  
    front_camera = models.PositiveIntegerField()  
    current_price = models.IntegerField()
    previous_price = models.IntegerField()
    image = models.ImageField(upload_to='device_images/', blank=True, null=True)
