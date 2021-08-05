# Generated by Django 3.2 on 2021-08-05 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210805_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='StructureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='Images')),
                ('Verified', models.BooleanField(blank=True, null=True)),
                ('projectName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.structure')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='Images')),
                ('Verified', models.BooleanField(blank=True, null=True)),
                ('projectName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='Images')),
                ('Verified', models.BooleanField(blank=True, null=True)),
                ('projectName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.material')),
            ],
        ),
        migrations.CreateModel(
            name='FlatImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='Images')),
                ('Verified', models.BooleanField(blank=True, null=True)),
                ('projectName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.flat')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='Images')),
                ('Verified', models.BooleanField(blank=True, null=True)),
                ('projectName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipment')),
            ],
        ),
    ]