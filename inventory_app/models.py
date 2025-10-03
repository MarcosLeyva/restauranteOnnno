from django.db import models

class Bebida(models.Model):
    SABORES = [
        ('horchata', 'Horchata'),
        ('cardamomo', 'Cardamomo'),
        ('lavanda', 'Lavanda'),
        ('coldbrew', 'Coldbrew'),
        ('matcha', 'Matcha'),
        ('maple', 'Maple'),
    ]

    sabor = models.CharField(max_length=20, choices=SABORES)
    volumen_ml = models.PositiveIntegerField(default=295)
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        # Asigna el precio automáticamente según el sabor
        if self.sabor == 'matcha':
            self.precio = 90
        else:
            self.precio = 80
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_sabor_display()} ({self.volumen_ml} ml) - ${self.precio}"
