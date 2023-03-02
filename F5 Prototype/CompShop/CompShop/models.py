# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib import admin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Admins(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userid', primary_key=True)
    typeofadmin = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'admins'
        verbose_name_plural = 'Admins'

    def __str__(self):
        return self.userid.username

admin.site.register(Admins)

class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    nameofcategory = models.CharField(max_length=50)
    subcategoryof = models.ForeignKey('self', models.DO_NOTHING, db_column='subcategoryof', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nameofcategory

admin.site.register(Category)

class Customer(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userid', primary_key=True)
    phonenumber = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.userid.username

admin.site.register(Customer)

class DeliveryAgent(models.Model):
    deliveryagentid = models.AutoField(primary_key=True)
    nameofdeliveryagent = models.CharField(max_length=100, blank=True, null=True)
    deliveryfirmid = models.ForeignKey('DeliveryFirm', models.DO_NOTHING, db_column='deliveryfirmid')

    class Meta:
        managed = True
        db_table = 'delivery_agent'
        verbose_name_plural = 'Delivery Agents'

    def __str__(self):
        return self.nameofdeliveryagent

admin.site.register(DeliveryAgent)

class DeliveryFirm(models.Model):
    deliveryfirmid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nameofdeliveryfirm = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'delivery_firm'
        verbose_name_plural = 'Delivery Firms'

    def __str__(self):
        return self.nameofdeliveryfirm

admin.site.register(DeliveryFirm)

class Manufacturer(models.Model):
    manufacturerid = models.AutoField(primary_key=True)
    nameofmanufacturer = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.nameofmanufacturer

admin.site.register(Manufacturer)

class Orderhasproduct(models.Model):
    id = models.AutoField(primary_key=True)
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='orderid')
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productid')
    quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'orderhasproduct'
        unique_together = (('orderid', 'productid'),)
        verbose_name_plural = 'Ordershaveproducts'

    def __str__(self):
        return '{} - {}'.format(self.orderid,self.productid.nameofproduct)

admin.site.register(Orderhasproduct)

class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    dateoforder = models.DateTimeField()
    totalprice = models.IntegerField()
    adminid = models.ForeignKey(Admins, models.DO_NOTHING, db_column='adminid', blank=True, null=True)
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customerid')
    scid = models.ForeignKey('ShoppingCart', models.DO_NOTHING, db_column='scid')
    deliveryfirmid = models.ForeignKey(DeliveryFirm, models.DO_NOTHING, db_column='deliveryfirmid', blank=True, null=True)
    code = models.ForeignKey('Promotion', models.DO_NOTHING, db_column='code', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orders'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.orderid)

admin.site.register(Orders)

class Price(models.Model):
    productid = models.OneToOneField('Product', models.DO_NOTHING, db_column='productid', primary_key=True)
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    value = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'price'
        unique_together = (('productid', 'startdate'),)
        verbose_name_plural = 'Prices'

    def __str__(self):
        return "Price for: " + self.productid.nameofproduct

admin.site.register(Price)

class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    nameofproduct = models.CharField(max_length=100)
    adminid = models.ForeignKey(Admins, models.DO_NOTHING, db_column='adminid')
    manufacturerid = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='manufacturerid')

    class Meta:
        managed = True
        db_table = 'product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.nameofproduct

admin.site.register(Product)

class ProductImages(models.Model):
    productid = models.OneToOneField(Product, models.DO_NOTHING, db_column='productid', primary_key=True)
    images = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'product_images'
        unique_together = (('productid', 'images'),)
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return "Image for: " + self.productid.nameofproduct

admin.site.register(ProductImages)

class Productisinsc(models.Model):
    id = models.AutoField(primary_key = True)
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productid')
    scid = models.ForeignKey('ShoppingCart', models.DO_NOTHING, db_column='scid')
    quantity = models.IntegerField(blank=True, null=True)
    @property
    def get_total(self):
        total = self.productid.price.value * self.quantity
        return total
    class Meta:
        managed = True
        db_table = 'productisinsc'
        unique_together = (('productid', 'scid'),)
        verbose_name_plural = 'Productsareinsc'

    def __str__(self):
        return '{} - {}'.format(self.scid, self.productid.nameofproduct)

admin.site.register(Productisinsc)

class Productisinsideso(models.Model):
    id = models.AutoField(primary_key=True)
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productid')
    stockorderid = models.ForeignKey('StockOrder', models.DO_NOTHING, db_column='stockorderid')
    quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'productisinsideso'
        unique_together = (('productid', 'stockorderid'),)
        verbose_name_plural = 'Productsareinsideso'

    def __str__(self):
        return '{} - {}'.format(self.stockorderid,self.productid.nameofproduct)


admin.site.register(Productisinsideso)

class Productisofcategory(models.Model):
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productid', primary_key=True)
    categoryid = models.OneToOneField(Category, models.DO_NOTHING, db_column='categoryid')

    class Meta:
        managed = True
        db_table = 'productisofcategory'
        unique_together = (('categoryid', 'productid'),)
        verbose_name_plural = 'Productsareofcategories'

    def __str__(self):
        return '{} - {}'.format(self.productid.nameofproduct, self.categoryid.nameofcategory)

admin.site.register(Productisofcategory)

class Promotion(models.Model):
    code = models.CharField(primary_key=True, max_length=16)
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    percentage = models.IntegerField()
    adminid = models.ForeignKey(Admins, models.DO_NOTHING, db_column='adminid')

    class Meta:
        managed = True
        db_table = 'promotion'
        verbose_name_plural = 'Promotions'

    def __str__(self):
        return str(self.code)

admin.site.register(Promotion)

class ShoppingCart(models.Model):
    scid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customerid')

    @property
    def get_cart_total(self):
        cartitems = self.productisinsc_set.all()
        total = sum([item.get_total for item in cartitems])
        return total

    @property
    def get_cart_items(self):
        cartitems = self.productisinsc_set.all()
        total = sum([item.quantity for item in cartitems])
        return total

    class Meta:
        managed = True
        db_table = 'shopping_cart'
        verbose_name_plural = 'Shopping Carts'

    def __str__(self):
        return str(self.scid)

admin.site.register(ShoppingCart)

class StockOrder(models.Model):
    stockorderid = models.AutoField(primary_key=True)
    orderdate = models.DateField()
    adminid = models.ForeignKey(Admins, models.DO_NOTHING, db_column='adminid')
    manufacturerid = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='manufacturerid')

    class Meta:
        managed = True
        db_table = 'stock_order'
        verbose_name_plural = 'Stock Orders'

    def __str__(self):
        return str(self.stockorderid)

admin.site.register(StockOrder)

class MyUserManager(BaseUserManager):
    def create_user(self, username, nameofuser, password=None):
        if not username:
            raise ValueError("Username is required")
        if not nameofuser:
            raise ValueError("Name of the user is required")

        user = self.model(
            username=username,
            nameofuser=nameofuser
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nameofuser, password=None, **kwargs):
        user = self.create_user(
            username=username,
            nameofuser=nameofuser,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    userid = models.AutoField(primary_key=True)
    username = models.TextField(unique=True, max_length=255, blank=False, null=False)
    password = models.TextField(max_length=255, blank=False, null=False)
    nameofuser = models.TextField(max_length=255, blank=False, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['nameofuser']

    objects = MyUserManager()

    class Meta:
        managed = True
        db_table = 'users'
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

admin.site.register(Users)