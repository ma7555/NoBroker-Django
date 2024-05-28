from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # Database Model for User Details
    """We can't remove the username completely with using Abstract User,
    so instead we leave it blank."""
    username = models.CharField(blank=True, null=True, max_length=128)
    mobile_no = models.CharField(max_length=10, unique=True)

    USERNAME_FIELD = "mobile_no"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.mobile_no

    """password_hash = db.Column(db.String(128))
	user_properties = db.relationship('Properties', backref = 'user_property', lazy='dynamic')
	user_enquiries = db.relationship('Enquiries', backref='user_enquiry', lazy='dynamic')"""


class Properties(models.Model):
    property_name = models.CharField(max_length=20)
    lease_type = models.CharField(max_length=5)
    furnished = models.CharField(max_length=1)
    address = models.CharField(max_length=20)
    rent = models.CharField(max_length=100)
    rooms = models.CharField(max_length=1)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
    # enquiry = models.ForeignKey(Enquiries,on_delete=models.CASCADE)

    def __str__(self):
        return self.property_name

    """enquiries = db.relationship('Enquiries', backref='property_enquiries', lazy='dynamic')"""


class Enquiries(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    enquirer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.property
