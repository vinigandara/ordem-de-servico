from django.db import models
from django.utils import timezone
    
class Equipamentos(models.Model):
    nome_do_equipamento = models.Textfield()
    marca = models.Textfield()
    modelo = models.Textfield()
    n_de_serie = models.Textfield()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome_do_equipamento
