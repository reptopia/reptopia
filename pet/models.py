from django.db import models
from django.conf import settings
from dict.models import Dictionary, AnimalDictionary
from django.utils import timezone
from datetime import date
from django.urls import reverse
import reptopia

class Pet(models.Model):
    species = models.ForeignKey(AnimalDictionary, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    gender = models.ForeignKey(
        Dictionary,
        related_name='gender',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        limit_choices_to={'category': reptopia._GENDER_},
    )
    bod = models.DateField()
    image = models.ImageField(upload_to='pet/%Y/%m/%d', blank=True, null=True)
    desc = models.TextField(blank=True)
    # design = 모프 기능 추가 후 구현 예정
    is_public = models.BooleanField(default=True)
    is_keeping  = models.BooleanField(default=True)

    def __str__(self):
        return '[' + self.species.common_name_kor + ']' + self.name;

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'userid': self.owner.pk, 'pk': self.pk})

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Pet, self).delete(*args, **kwargs)

class Care(models.Model):
    date = models.DateField(default=timezone.now, blank=False)
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    type = models.ForeignKey(
        Dictionary,
        related_name='care_type',
        on_delete=models.CASCADE,
        limit_choices_to={'category': reptopia._CARE_},
    )
    image = models.ImageField(upload_to='care/%Y/%m/%d', blank=True, null=True)
    desc = models.TextField(blank=True)
    created_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pet.name + " : " + localize(self.date) + " : " + self.type.item

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Care, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'userid': self.pet.owner.pk, 'pk': self.pet.pk})

