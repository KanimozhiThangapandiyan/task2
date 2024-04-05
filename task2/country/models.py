from django.db import models
import uuid
from django.core.validators import RegexValidator

class Country(models.Model):
    country_uuid = models.UUIDField(default=uuid.uuid4, editable=False)  
    country_name = models.CharField(max_length=50, unique=True, validators=[
        RegexValidator(r'^[a-zA-Z]+$', 'Only alphabetic characters are allowed.')
    ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.country_name

# class Country(models.Model):
#     country_uuid = models.UUIDField(default=uuid.uuid4, editable=False)  
#     country_name = models.CharField(max_length=50,unique=True,validators=[
#         RegexValidator(r'^[a-zA-Z]+$', 'Only alphabetic characters are allowed.')
#     ])
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.country_name


class State(models.Model):
    state_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50,unique=True,validators=[
        RegexValidator(r'^[a-zA-Z]+$', 'Only alphabetic characters are allowed.')
    ])
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.state_name

class City(models.Model):
    city_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50,unique=True,validators=[
        RegexValidator(r'^[a-zA-Z]+$', 'Only alphabetic characters are allowed.')
    ])
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.city_name

    
