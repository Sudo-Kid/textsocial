from __future__ import unicode_literals

import uuid

from django.db import models


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    locality = models.CharField()

    modified_date = models.DateTime(auto_now=True)
    creation_date = models.DateTime(auto_now_add=True)


class StreetTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField()


class Street(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street_type = models.ForignKey('StreetType')

    directional_prefix = models.CharField(blank=True, default='')
    name = models.CharField()
    directional_suffix = models.CharField(blank=True, default='')

    modified_date = models.DateTime(auto_now=True)
    creation_date = models.DateTime(auto_now_add=True)


class StreetNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    prefix = models.CharField(blank=True, default='')
    number = models.CharField()
    suffix = models.CharField(blank=True, default='')


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    locality = models.ForeignKey('City')
    street_name = models.ForeignKey('Street')
    street_number = models.ForeignKey('StreetNumber')

    civic_id = models.CharField(blank=True, default='')
    latitude = models.DecimalField(max_digits=16, decimal_places=13)
    longitude = models.DecimalField(max_digits=16, decimal_places=13)

    modified_date = models.DateTime(auto_now=True)
    creation_date = models.DateTime(auto_now_add=True)
