
from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beachfront Villa", "description": "A lovely villa by the ocean.", "price_per_night": 250.00, "location": "Cape Town"},
            {"title": "City Apartment", "description": "Modern apartment in the city center.", "price_per_night": 120.00, "location": "Johannesburg"},
            {"title": "Safari Lodge", "description": "Stay close to nature with this safari lodge.", "price_per_night": 300.00, "location": "Kruger National Park"},
            {"title": "Cozy Cottage", "description": "A peaceful retreat in the countryside.", "price_per_night": 90.00, "location": "Drakensberg"},
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))
