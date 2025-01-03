def user_listing_path(instance, filename):
    return f'listings/{instance.seller.user.id}/{filename}'