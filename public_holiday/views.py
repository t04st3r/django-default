from rest_framework import viewsets
from .models import PublicHoliday
from .serializers import PublicholidaySerializer

class PublicHolidayList(viewsets.ReadOnlyModelViewSet):
    """
    A simple List ViewSet.
    """
    queryset = PublicHoliday.objects.all()
    serializer_class = PublicholidaySerializer