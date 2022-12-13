from django.db import models


class ObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()


def image_folder(instance, filename):
    return 'images/{}.webp'.format(instance.name)


class Product(models.Model):

    HAVE = 'HV'
    ORDER = 'OR'
    EXPECTED = 'EX'
    OUT_OF_STOCK = 'OOS'
    NOT_PRODUCED = 'NP'
    STATUS_CHOICES = (
        (HAVE, 'В наличии'),
        (ORDER, 'Под заказ'),
        (EXPECTED, 'Ожидается поступление'),
        (OUT_OF_STOCK, 'Нет в наличии'),
        (NOT_PRODUCED, 'Не производится'),
    )
    objects = ObjectsManager()
    name = models.CharField(max_length=64)
    article = models.IntegerField()  # сделать уникальным увелить стоимость
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to=image_folder)
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='статус', max_length=3, default=HAVE)

    # images = models.ImageField()
    def __str__(self):
        return f'Название товара - {self.name}'



