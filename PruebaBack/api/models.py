from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class States (models.Model):
    slug = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Slug',
        unique = True
    )

    def __str__(self):
        return self.slug

class Cities (models.Model):
    slug = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Slug'
    )
    zip = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Zip'
    )
    state = models.ForeignKey(
        States,
        on_delete=models.CASCADE,
        verbose_name = 'States'
    )

    def __str__(self):
        return self.slug

class Categories (models.Model):
    slug = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Slug'
    )

    def __str__(self):
        return self.slug

class PropertyTypes (models.Model):
    slug = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Slug'
    )

    def __str__(self):
        return self.slug

class Transactions (models.Model):
    slug = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Slug'
    )
    propertyTypes = models.ManyToManyField(
        PropertyTypes,
        verbose_name = 'Property Types'
    )

    def __str__(self):
        return self.slug


class Properties(models.Model):
    title = models.CharField (
        max_length = 20,
        null = False,
        verbose_name = 'Title'
    )
    image = models.CharField (
        max_length = 500,
        null = False,
        verbose_name = 'Image'
    )
    price = models.PositiveIntegerField (
        null = False,
        verbose_name = 'Price'
    )
    city = models.ForeignKey (
        Cities,
        on_delete = models.CASCADE,
        verbose_name = 'City'
    )
    baths = models.PositiveIntegerField (
        null = False,
        verbose_name = 'Baths'
    )
    beds = models.PositiveIntegerField (
        null = False,
        verbose_name = 'Beds'
    )
    sqft = models.PositiveIntegerField (
        null = False,
        verbose_name = 'Square feet'
    )
    category = models.ForeignKey (
        Categories,
        on_delete = models.CASCADE,
        verbose_name = 'Category'
    )
    propertyType = models.ForeignKey(
        PropertyTypes,
        on_delete = models.CASCADE,
        verbose_name = 'Property Type'
    )

class Reviews (models.Model):
    feedback = models.CharField (
        max_length = 500,
        null = False,
        verbose_name = 'Feedback'
    )
    rating = models.IntegerField (
        null = False,
        verbose_name = 'Rating',
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    avatar = models.CharField (
        max_length = 500,
        null = False,
        verbose_name = 'Avatar'
    )
    property = models.ForeignKey (
        Properties,
        on_delete = models.CASCADE,
        verbose_name = 'Property'
    )
