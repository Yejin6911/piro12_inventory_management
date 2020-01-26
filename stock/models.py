from django.db import models
from django.urls import reverse

from mysite.utils import uuid_upload_to


class Account(models.Model):
    name = models.CharField(max_length=200, verbose_name='이름')
    phone = models.CharField(max_length=100, verbose_name='전화번호')
    address = models.TextField(verbose_name='주소')

    def __str__(self):
        return f'{self.name}'



class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='제품명')
    photo = models.ImageField(upload_to=uuid_upload_to, verbose_name='제품 사진')
    content = models.TextField(verbose_name='제품 설명')
    price = models.PositiveIntegerField(verbose_name='가격')
    left = models.PositiveIntegerField(verbose_name='남은 수량')

    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='거래처',related_name='products')

    def __str__(self):
        return f'<{self.pk}> {self.name}'

#    def get_absolute_url(self):
#        return reverse('stock:product_detail', kwargs={'pk': self.pk})
