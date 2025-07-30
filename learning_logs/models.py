from django.db import models
#Aula vinculo
from django.contrib.auth.models import User

#Aula 01
class Topic(models.Model):
    """
        Assunto que o usuário está aprendendo
    """

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    #Aula vinculo
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
            Develve uma representação em string do modelo
        """
        return self.text
    
#Aula 02
class Entry(models.Model):
    """Algo aprendido sobre o assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Develve uma representação em string do modelo"""
        return self.text[:50] + '...'