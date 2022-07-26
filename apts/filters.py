from listings import models
import django_filters

class AptFilter(django_filters.FilterSet):
    class Meta:
        model = models.Listing
        fields=['price','bedrooms','city','is_furnished','allow_pets','park_lot']