from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django User model.

    Adds additional boolean fields to control module access permissions:
    - can_access_contact: Whether the user can access contact information.
    - can_access_sales: Whether the user can access sales data.
    - can_access_purchase: Whether the user can access purchase data.
    - can_access_account: Whether the user can access account data.
    """
    can_access_contact = models.BooleanField(default=False)
    can_access_sales = models.BooleanField(default=False)
    can_access_purchase = models.BooleanField(default=False)
    can_access_account = models.BooleanField(default=False)

    # Add unique `related_name` values to avoid conflicts with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    def __str__(self):
        """Return the string representation of the user, typically the id."""
        return self.username

