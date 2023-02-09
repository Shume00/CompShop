# Generated by Django 4.1.6 on 2023-02-09 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CompShop', '0003_alter_admins_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admins',
            options={'managed': True, 'verbose_name_plural': 'Admins'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': True, 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='deliveryagent',
            options={'managed': True, 'verbose_name_plural': 'Delivery Agents'},
        ),
        migrations.AlterModelOptions(
            name='deliveryfirm',
            options={'managed': True, 'verbose_name_plural': 'Delivery Firms'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'managed': True, 'verbose_name_plural': 'Manufacturers'},
        ),
        migrations.AlterModelOptions(
            name='orderhasproduct',
            options={'managed': True, 'verbose_name_plural': 'Ordershaveproducts'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': True, 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'managed': True, 'verbose_name_plural': 'Prices'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': True, 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productimages',
            options={'managed': True, 'verbose_name_plural': 'Product Images'},
        ),
        migrations.AlterModelOptions(
            name='productisinsc',
            options={'managed': True, 'verbose_name_plural': 'Productsareinsc'},
        ),
        migrations.AlterModelOptions(
            name='productisinsideso',
            options={'managed': True, 'verbose_name_plural': 'Productsareinsideso'},
        ),
        migrations.AlterModelOptions(
            name='productisofcategory',
            options={'managed': True, 'verbose_name_plural': 'Productsareofcategories'},
        ),
        migrations.AlterModelOptions(
            name='promotion',
            options={'managed': True, 'verbose_name_plural': 'Promotions'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'managed': True, 'verbose_name_plural': 'Shopping Carts'},
        ),
        migrations.AlterModelOptions(
            name='stockorder',
            options={'managed': True, 'verbose_name_plural': 'Stock Orders'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'managed': True, 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='category',
            name='subcategoryof',
            field=models.ForeignKey(blank=True, db_column='subcategoryof', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='CompShop.category'),
        ),
        migrations.AlterField(
            model_name='productisofcategory',
            name='categoryid',
            field=models.OneToOneField(db_column='categoryid', on_delete=django.db.models.deletion.DO_NOTHING, to='CompShop.category'),
        ),
        migrations.AlterField(
            model_name='productisofcategory',
            name='productid',
            field=models.ForeignKey(db_column='productid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='CompShop.product'),
        ),
    ]
