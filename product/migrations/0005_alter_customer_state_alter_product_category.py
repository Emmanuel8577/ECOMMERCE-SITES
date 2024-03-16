# Generated by Django 5.0.3 on 2024-03-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_customer_mobile_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Kwara', 'Kwara'), ('Ekiti', 'Ekiti'), ('Kogi', 'Kogi'), ('FCT', 'FCT'), ('Kebbi', 'Kebbi'), ('Benue', 'Benue'), ('Ebonyi', 'Ebonyi'), ('Zamfara', 'Zamfara'), ('Jigawa', 'Jigawa'), ('Rivers', 'Rivers'), ('Imo', 'Imo'), ('Enugu', 'Enugu'), ('Gombe', 'Gombe'), ('Nasarawa', 'Nasarawa'), ('Yobe', 'Yobe'), ('Ondo', 'Ondo'), ('Delta', 'Delta'), ('Sokoto', 'Sokoto'), ('Akwa Ibom', 'Akwa Ibom'), ('Edo', 'Edo'), ('Oyo', 'Oyo'), ('Ogun', 'Ogun'), ('Kaduna', 'Kaduna'), ('Plateau', 'Plateau'), ('Bauchi', 'Bauchi'), ('Anambra', 'Anambra'), ('Borno', 'Borno'), ('Lagos', 'Lagos'), ('Kano', 'Kano'), ('Niger', 'Niger'), ('Bayelsa', 'Bayelsa'), ('Katsina', 'Katsina'), ('Cross River', 'Cross River'), ('Adamawa', 'Adamawa'), ('Taraba', 'Taraba'), ('Osun', 'Osun'), ('Abia', 'Abia')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FT', 'Fruit'), ('WT', 'Watch'), ('TL', 'Tele'), ('RD', 'Radio'), ('SH', 'shoes'), ('PH', 'Phone'), ('LT', 'Laptop')], max_length=2),
        ),
    ]