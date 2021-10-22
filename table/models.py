from django.db import models


class ResPool(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=200, null=True)
    respool = models.ForeignKey(ResPool, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Item(models.Model):
    MEMORY = (
        ('8 Gb', '8 Gb'),
        ('16 Gb', '16 Gb'),
        ('32 Gb', '32 Gb'),
        ('64 Gb', '64 Gb'),
    )

    vCPU = (
        ('8 core', '8 core'),
        ('16 core', '16 core'),
        ('32 core', '32 core'),
        ('64 core', '64 core'),
    )
    HDD = (
        ('512 Gb', '512 Gb'),
        ('1 Tb', '1 Tb'),
        ('5 Tb', '5 Tb'),
        ('10 Tb', '10 Tb'),
    )

    respool = models.ForeignKey(ResPool, null=True, on_delete=models.SET_NULL)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
    name = models.CharField('Name', max_length=100)
    memory = models.CharField(max_length=200, null=True, choices=MEMORY)
    vcpu = models.CharField(max_length=200, null=True, choices=vCPU)
    hdd = models.CharField(max_length=200, null=True, choices=HDD)

    def __str__(self):
        return self.name
