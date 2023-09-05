from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Yellow(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    ADDRESS = models.CharField(max_length=255, null=True, blank=True)
    CFM_ID = models.CharField(max_length=20, null=True, blank=True)
    CITY = models.CharField(max_length=20, null=True, blank=True)
    COMPANY = models.CharField(max_length=100, null=True, blank=True)
    CONTACT_1 = models.CharField(max_length=20, null=True, blank=True)
    CONTACT_2 = models.CharField(max_length=20, null=True, blank=True)
    FAX = models.CharField(max_length=20, null=True, blank=True)
    INDUSTRY = models.CharField(max_length=30, null=True, blank=True)
    PHONE = models.CharField(max_length=30, null=True, blank=True)
    STATE = models.CharField(max_length=20, null=True, blank=True)
    ZIP = models.CharField(max_length=20, null=True, blank=True)
    ACCOUNT_ID = models.CharField(max_length=20, null=255, blank=True)
    CATEGORY = models.CharField(max_length=20, null=True, blank=True)
    PREFERRED = models.CharField(max_length=20, null=True, blank=True)
    EMAIL = models.CharField(max_length=20, null=True, blank=True)
    WEBSITE = models.CharField(max_length=100, null=True, blank=True)
    URL = models.CharField(max_length=255, null=True, blank=True)
    SOURCE = models.CharField(max_length=255, null=True, blank=True)
    SCRAPED_TIME = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'state_data'

