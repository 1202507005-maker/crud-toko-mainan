# Create your models here.
from django.db import models

class Mainan(models.Model):
    nama_mainan = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    usia_rekomendasi = models.IntegerField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_mainan
