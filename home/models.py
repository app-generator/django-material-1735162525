# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Empresa(models.Model):

    #__Empresa_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=255, null=True, blank=True)

    #__Empresa_FIELDS__END

    class Meta:
        verbose_name        = _("Empresa")
        verbose_name_plural = _("Empresa")


class Colaborador(models.Model):

    #__Colaborador_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=255, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    #__Colaborador_FIELDS__END

    class Meta:
        verbose_name        = _("Colaborador")
        verbose_name_plural = _("Colaborador")



#__MODELS__END
