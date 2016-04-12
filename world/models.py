# _*_ coding: utf-8
from django.db import models
from django.utils import timezone

class Branch(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Наименование")
    address = models.CharField(max_length=50, verbose_name=u"Адрес")

    class Meta:
        verbose_name = u'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"ФИО")
    passport_data = models.CharField(max_length=50, verbose_name=u"Паспортные данные")
    address = models.CharField(max_length=100, verbose_name=u"Адрес проживания")
    phone = models.CharField(max_length=50, verbose_name=u"Телефон")

    class Meta:
        verbose_name = u'Наниматель'
        verbose_name_plural = 'База нанимателей'

    def __str__(self):
        return self.name

class Suit(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Наименование")
    picture = models.ImageField(upload_to='images', null=True, blank=True, verbose_name=u"Картинка")
    vendor_code = models.CharField(max_length=10, verbose_name=u"Артикул")
    year_issue = models.IntegerField(verbose_name=u"Год производства")
    details = models.TextField(max_length=100, verbose_name=u"Детализация")
    colour = models.CharField(max_length=50, verbose_name=u"Цвет")
    rent_price = models.IntegerField(verbose_name=u"Арендная плата")
    item_price = models.IntegerField(verbose_name=u"Сумма имущества")
    note = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"Примечание")
    branch = models.ForeignKey(Branch, verbose_name=u"Филиал")

    class Meta:
        verbose_name = u'Инвентарь'
        verbose_name_plural = 'Инвентаризация'

    def __str__(self):
        return self.name


class SuitToSize(models.Model):
    suit = models.ForeignKey(Suit, verbose_name=u"Инвентарь")
    size = models.IntegerField(verbose_name=u"Размер")
    count = models.IntegerField(verbose_name=u"Количество")
    created_date = models.DateField(null=True, blank=True, verbose_name=u"Дата добавления")

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = u'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.suit.name + u", размер: " + str(self.size)


class SuitToRent(models.Model):
    protocol_num = models.CharField(max_length=20, null=True, blank=True, verbose_name=u"Номер договора")
    suit_to_size = models.ForeignKey(SuitToSize, verbose_name=u"Инвентарь")
    count = models.IntegerField(verbose_name=u"Количество")
    start_date = models.DateField(default=timezone.now, verbose_name=u"Дата начала проката")
    end_date = models.DateField(default=timezone.now, verbose_name=u"Дата конца проката")
    people = models.ForeignKey(People, verbose_name=u"Наниматель")
    total_price = models.IntegerField(verbose_name=u"Общая сумма")
    user = models.ForeignKey('auth.User', verbose_name=u"Наймодатель")
    published_date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата записи")

    class Meta:
        verbose_name = u'Договор'
        verbose_name_plural = 'База договоров'

    def publish(self):
        self.user = request.user
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.suit_to_size.suit.name


class UserToBranch(models.Model):
    user = models.ForeignKey('auth.User')
    branch = models.ForeignKey(Branch)

    def __str__(self):
        return self.branch.name
