from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing property listings.
    Supports CRUD operations.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing bookings.
    Supports CRUD operations.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
