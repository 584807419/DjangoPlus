from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver


# Create your models here.

class DateTimeBase(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class ParaentConmany(DateTimeBase):
#     name = models.CharField(name='name', verbose_name='公司名称', null=True, max_length=128, help_text='公司名称')
#     status = models.BooleanField(default=False)


class Company(DateTimeBase):
    name = models.CharField(name='name', verbose_name='公司名称', null=True, max_length=128, help_text='公司名称')
    address = models.CharField(name='address', verbose_name='公司所在国家和城市', null=True, max_length=128)  # 字符串
    #
    # # 数字相关字段
    # temp1 = models.BigIntegerField()  # 范围是 -9223372036854775808 到9223372036854775807之间
    # temp1 = models.SmallIntegerField()  # 对于django来讲，该字段值在 -32768 至 32767这个范围内对所有可支持的数据库都是安全的。
    # temp1 = models.IntegerField()  # 从 -2147483648 到 2147483647 范围内的值是合法的
    # temp1 = models.PositiveIntegerField()  # 正数或者零(0). 从0到2147483647的值
    # temp1 = models.PositiveSmallIntegerField()  # 只允许小于某一特定值（依据数据库类型而定）。从0 到 32767 这个区间，对于Django所支持的所有数据库而言都是安全的。
    # temp1 = models.CommaSeparatedIntegerField(max_length=None)  # 一个逗号分隔的整数字段
    # temp1 = models.DecimalField(max_digits=19, decimal_place=10)  # 要存储那些将近10亿，并且要求达到小数点后十位精度的数字
    #
    # # 布尔值
    # temp1 = models.BinaryField()  # 存储原始二进制码,尽管你可能想使用数据库来存储你的文件，但是99%的情况下这都是不好的设计
    # temp1 = models.BooleanField()  # BooleanField 的默认值是 None。
    # temp1 = models.NullBooleanField()  # 如果你需要设置null 值，则使用NullBooleanField 来代替BooleanField。
    #
    # # 时间日期
    # temp1 = models.DateField(auto_now=False, auto_now_add=False)  # 使用Python的datetime.date实例表示的日期
    # temp1 = models.TimeField(auto_now=False, auto_now_add=False)  # 使用Python的datetime.time实例表示的时间
    # temp1 = models.DateTimeField(auto_now=False, auto_now_add=False)  # 使用Python的datetime.datetime实例表示的日期
    #
    # # 专用
    # import uuid
    #
    # temp1 = models.EmailField()
    # temp1 = models.TextField()  # 大文本字段
    # temp1 = models.URLField(max_length=200)  # 一个CharField 类型的URL
    # temp1 = models.GenericIPAddressField(protocol='both')  # 一个 IPv4 或 IPv6 地址, 字符串格式
    # temp1 = models.SlugField(max_length=100)  # 一个slug只能包含字母、数字、下划线或者是连字符，通常用来作为短标签。通常它们是用来放在URL里的。
    # temp1 = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                          editable=False)  # 一个用来存储UUID的字段。使用Python的UUID类。 当使用PostgreSQL数据库时，该字段类型对应的数据库中的数据类型是uuid，使用其他数据库时，数据库对应的是char(32)类型。使用UUID类型相对于使用具有primary_key参数的AutoField类型是一个更好的解决方案
    #
    # # 文件
    # temp1 = models.FileField(upload_to='pic/%Y/%m/%d')  # db_obj.temp1.url db_obj.temp1.name  db_obj.temp1.size
    # temp1 = models.ImageField(upload_to='pic/%Y/%m/%d')
    # temp1 = models.FilePathField(path="/home/images", match="foo.*",
    #                              recursive=True)  # 一个 CharField ，内容只限于文件系统内特定目录下的文件名
    # temp1 = models.FloatField()  # 用Python的一个float 实例来表示一个浮点数
    # temp1 = models.ImageField(height_field=200, width_field=200)
    #
    # # 关系字段
    # paraent = models.ForeignKey(ParaentConmany, limit_choices_to={'status': True}, db_index=False)

    # class Meta:
    #     db_table = 'company_info'

    def __str__(self):
        return f'{self.name,self.address}'


@receiver(pre_save, sender=Company)
def test(sender, **kwargs):
    print("it worked")
