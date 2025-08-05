from django.db import models
import uuid

from users.models import Profile, Location
from .utils import user_listing_path


class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    name = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, db_index=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='user_listings/', null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.name} by {self.seller.user.username}"
    
class LikedList(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.listing.name} listing liked by {self.profile.user.username}'