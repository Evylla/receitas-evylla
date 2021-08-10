from django.db import models

# Create your models here.
class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instruções = models.TextField()
    postado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome