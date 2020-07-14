
from django.db import models


class InjertoManager(models.Manager):

    def activo(self):
        return self.filter(activo=True)


class SolicitanteManager(models.Manager):

    def activo(self):
        return self.filter(user=self.user)        