# Generated by Django 5.0.3 on 2024-03-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_category_cart_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Taraba', 'Taraba'), ('Plateau', 'Plateau'), ('Ondo', 'Ondo'), ('Oyo', 'Oyo'), ('Edo', 'Edo'), ('Gombe', 'Gombe'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Zamfara', 'Zamfara'), ('Cross River', 'Cross River'), ('Bauchi', 'Bauchi'), ('Ogun', 'Ogun'), ('Rivers', 'Rivers'), ('Katsina', 'Katsina'), ('Akwa Ibom', 'Akwa Ibom'), ('Kano', 'Kano'), ('Bayelsa', 'Bayelsa'), ('Delta', 'Delta'), ('Sokoto', 'Sokoto'), ('Nasarawa', 'Nasarawa'), ('Enugu', 'Enugu'), ('Kogi', 'Kogi'), ('Lagos', 'Lagos'), ('Ebonyi', 'Ebonyi'), ('Kwara', 'Kwara'), ('Jigawa', 'Jigawa'), ('Anambra', 'Anambra'), ('Ekiti', 'Ekiti'), ('Kebbi', 'Kebbi'), ('Adamawa', 'Adamawa'), ('Imo', 'Imo'), ('Abia', 'Abia'), ('Kaduna', 'Kaduna'), ('Yobe', 'Yobe'), ('Osun', 'Osun'), ('Niger', 'Niger'), ('FCT', 'FCT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PH', 'Phone'), ('SH', 'shoes'), ('WT', 'Watch'), ('LT', 'Laptop'), ('TL', 'Tele'), ('RD', 'Radio'), ('FT', 'Fruit')], max_length=2),
        ),
    ]
