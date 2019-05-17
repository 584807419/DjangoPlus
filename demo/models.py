from django.db import models


# Create your models here.

class DateTimeBase(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(DateTimeBase):
    name = models.CharField(name='name', verbose_name='公司名称', null=True, max_length=128, help_text='公司名称')
    address = models.CharField(name='address', verbose_name='公司所在国家和城市', null=True, max_length=128)

    def __str__(self):
        return f'{self.name,self.address}'
