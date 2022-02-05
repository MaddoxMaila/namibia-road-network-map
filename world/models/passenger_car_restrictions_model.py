from django.contrib.gis.db import models


class PassengerCarRestrictions(models.Model):
    
    is_freeway = models.BooleanField()
    road_type = models.IntegerField()
    speed_limitations = models.IntegerField()
    geom = models.GeometryField()



# ft_ferry_element = models.BooleanField()
# ft_address_element = models.BooleanField()
# country_left = models.CharField(max_length=3)
# country_right = models.CharField(max_length=3)
# centimeters = models.IntegerField()
# positional_accuracy = models.IntegerField(choices=[(1, 'Good'), (2, 'Medium'), (3, 'Bad')])
# ada_compliant = models.BooleanField()