from django.db import models

class Exame(models.Model):
    TIPO_CHOICES = [('Tomografia', 'Tomografia')]
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, default='Tomografia')
    data_hora = models.DateTimeField(auto_now_add=True)
    tecnico = models.CharField(max_length=100)
    laudo = models.TextField()
    imagem_exame = models.FileField(upload_to='imagens_exames/')
    # imagem_exame = models.CharField(max_length=200)
