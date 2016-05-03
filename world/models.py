# _*_ coding: utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import Sum
import datetime
import pytz


class Branch(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name=u"Наименование")
    address = models.CharField(max_length=50, verbose_name=u"Адрес")

    class Meta:
        verbose_name = u'Филиал'
        verbose_name_plural = u'Филиалы'

    def __str__(self):
        return self.name


class MyUserManager(BaseUserManager):
    def create_user(self, email, branch, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            branch=branch
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, branch, password):
        user = self.create_user(email,
                                password=password,
                                branch=Branch.objects.get(pk=branch)
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=u"Email адрес",
        max_length=255,
        unique=True,
    )
    branch = models.ForeignKey(Branch, null=True, blank=True, verbose_name=u"Филиал")
    is_active = models.BooleanField(default=True, verbose_name=u"Активный")
    is_admin = models.BooleanField(default=False, verbose_name=u"Администратор")
    is_staff = models.BooleanField(default=True, verbose_name=u"Персонал")

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['branch']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'


class SuitType(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name=u"Наименование")

    class Meta:
        verbose_name = u'Отдел'
        verbose_name_plural = u'Отделы'

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name=u"ФИО")
    passport_data = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"Паспортные данные")
    address = models.CharField(max_length=100, verbose_name=u"Адрес проживания")
    phone = models.CharField(max_length=50, verbose_name=u"Телефон")

    class Meta:
        verbose_name = u'Наниматель'
        verbose_name_plural = u'База нанимателей'

    def __str__(self):
        return self.name


class Suit(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name=u"Наименование")
    picture = models.ImageField(upload_to='images', null=True, blank=True, verbose_name=u"Картинка")
    vendor_code = models.CharField(max_length=10, verbose_name=u"Артикул")
    year_issue = models.IntegerField(verbose_name=u"Год производства")
    details = models.TextField(max_length=100, verbose_name=u"Детализация")
    colour = models.CharField(max_length=50, verbose_name=u"Цвет")
    rent_price = models.IntegerField(verbose_name=u"Арендная плата")
    item_price = models.IntegerField(verbose_name=u"Сумма имущества")
    note = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"Примечание")
    branch = models.ForeignKey(Branch, verbose_name=u"Филиал")
    type = models.ForeignKey(SuitType, verbose_name=u"Отдел")

    def admin_image(self):
        if not self.picture:
            return '<img src="%s" width="100" height="100"/>'
        else:
            return '<img src="%s" width="100" height="100"/>' % self.picture.url

    admin_image.allow_tags = True
    admin_image.short_description = u"Картинка"

    class Meta:
        verbose_name = u'Инвентарь'
        verbose_name_plural = u'Инвентаризация'

    def __str__(self):
        return self.name

class Agreement(models.Model):
    protocol_num = models.CharField(max_length=20, verbose_name=u"Номер договора")
    start_date = models.DateField(default=timezone.now, verbose_name=u"Дата начала проката")
    end_date = models.DateField(default=timezone.now, verbose_name=u"Дата конца проката")
    people = models.ForeignKey(People, verbose_name=u"Наниматель")
    reserve_sum = models.IntegerField(verbose_name=u"Сумма при брони")
    total_price = models.IntegerField(verbose_name=u"Общая сумма")
    user = models.ForeignKey(MyUser, verbose_name=u"Наймодатель")
    published_date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата записи")
    is_returned = models.NullBooleanField(null=True, blank=True, verbose_name=u"Возвращено?")

    def item_status_return(self):
        utc = pytz.UTC
        enddate = utc.localize(datetime.datetime.strptime(self.end_date.__str__(), '%Y-%m-%d'))
        return enddate > timezone.now() or self.is_returned

    item_status_return.admin_order_field = 'published_date'
    item_status_return.boolean = True
    item_status_return.short_description = u'Статус'

    def __str__(self):
        return self.protocol_num

    class Meta:
        verbose_name = u'Договор'
        verbose_name_plural = u'База договоров'

class SuitToSize(models.Model):
    suit = models.ForeignKey(Suit, verbose_name=u"Инвентарь")
    size = models.IntegerField(verbose_name=u"Размер")
    count = models.IntegerField(verbose_name=u"Количество")
    created_date = models.DateField(default=timezone.now(), verbose_name=u"Дата добавления")

    @property
    def in_stock(self):
        if not SuitToRent.objects.filter(suit_to_size__pk=self.pk).filter(agreement__is_returned=False).aggregate(total=Sum('count'))['total']:
            return self.count
        else:
            return self.count - SuitToRent.objects.filter(suit_to_size__pk=self.pk).filter(agreement__is_returned=False).aggregate(total=Sum('count'))['total']

    class Meta:
        verbose_name = u'Размер'
        verbose_name_plural = u'Размеры инвентарей'
        unique_together = ('suit', 'size',)

    def __str__(self):
        return self.suit.name + u", размер: " + str(self.size) + u", в наличии: " + str(self.in_stock)


class SuitToRent(models.Model):
    agreement = models.ForeignKey(Agreement, verbose_name=u"Номер договора")
    suit_to_size = models.ForeignKey(SuitToSize, verbose_name=u"Инвентарь")
    count = models.IntegerField(verbose_name=u"Количество")

    class Meta:
        verbose_name = u'Инвентарь'
        verbose_name_plural = u'Комплект'
        unique_together = ('agreement', 'suit_to_size',)

    def __str__(self):
        return self.suit_to_size.suit.name

class SystemErrorLog(models.Model):
    level = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField('Дата и время', null=True, blank=True)
