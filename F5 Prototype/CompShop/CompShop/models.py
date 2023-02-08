# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admins(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userid', primary_key=True)
    typeofadmin = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'admins'


class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    nameofcategory = models.CharField(max_length=50)
    subcategoryof = models.ForeignKey('self', models.DO_NOTHING, db_column='subcategoryof', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category'


class Customer(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userid', primary_key=True)
    phonenumber = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'customer'


class DeliveryAgent(models.Model):
    deliveryagentid = models.AutoField(primary_key=True)
    nameofdeliveryagent = models.CharField(max_length=100, blank=True, null=True)
    deliveryfirmid = models.ForeignKey('DeliveryFirm', models.DO_NOTHING, db_column='deliveryfirmid')

    class Meta:
        managed = True
        db_table = 'delivery_agent'


class DeliveryFirm(models.Model):
    deliveryfirmid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nameofdeliveryfirm = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'delivery_firm'


class Manufacturer(models.Model):
    manufacturerid = models.AutoField(primary_key=True)
    nameofmanufacturer = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'manufacturer'


class Orderhasproduct(models.Model):
    quantity = models.IntegerField()
    orderid = models.OneToOneField('Orders', models.DO_NOTHING, db_column='orderid', primary_key=True)
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='productid')

    class Meta:
        managed = True
        db_table = 'orderhasproduct'
        unique_together = (('orderid', 'productid'),)


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


class Price(models.Model):
    productid = models.OneToOneField('Product', models.DO_NOTHING, db_column='productid', primary_key=True)
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    value = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'price'
        unique_together = (('productid', 'startdate'),)


class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    nameofproduct = models.CharField(max_length=100)
    adminid = models.ForeignKey(Admins, models.DO_NOTHING, db_column='adminid')
    manufacturerid = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='manufacturerid')

    class Meta:
        managed = True
        db_table = 'product'


class ProductImages(models.Model):
    productid = models.OneToOneField(Product, models.DO_NOTHING, db_column='productid', primary_key=True)
    images = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'product_images'
        unique_together = (('productid', 'images'),)


class Productisinsc(models.Model):
    quantity = models.IntegerField()
    productid = models.OneToOneField(Product, models.DO_NOTHING, db_column='productid', primary_key=True)
    scid = models.ForeignKey('ShoppingCart', models.DO_NOTHING, db_column='scid')

    class Meta:
        managed = True
        db_table = 'productisinsc'
        unique_together = (('productid', 'scid'),)


class Productisinsideso(models.Model):
    quantity = models.IntegerField()
    productid = models.OneToOneField(Product, models.DO_NOTHING, db_column='productid', primary_key=True)
    stockorderid = models.ForeignKey('StockOrder', models.DO_NOTHING, db_column='stockorderid')

    class Meta:
        managed = True
        db_table = 'productisinsideso'
        unique_together = (('productid', 'stockorderid'),)


class Productisofcategory(models.Model):
    categoryid = models.OneToOneField(Category, models.DO_NOTHING, db_column='categoryid', primary_key=True)
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productid')

    class Meta:
        managed = True
        db_table = 'productisofcategory'
        unique_together = (('categoryid', 'productid'),)


class Promotion(models.Model):
    code = models.CharField(primary_key=True, max_length=16)
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    percentage = models.IntegerField()
    adminid = models.ForeignKey(Admins, models.DO_NOTHING, db_column='adminid')

    class Meta:
        managed = True
        db_table = 'promotion'


class ShoppingCart(models.Model):
    scid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customerid')

    class Meta:
        managed = True
        db_table = 'shopping_cart'


class StockOrder(models.Model):
    stockorderid = models.AutoField(primary_key=True)
    orderdate = models.DateField()
    adminid = models.ForeignKey(Admins, models.DO_NOTHING, db_column='adminid')
    manufacturerid = models.ForeignKey(Manufacturer, models.DO_NOTHING, db_column='manufacturerid')

    class Meta:
        managed = True
        db_table = 'stock_order'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50, blank=True, null=True)
    userpass = models.CharField(max_length=50)
    nameofuser = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'users'
