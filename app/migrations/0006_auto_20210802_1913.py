# Generated by Django 3.2 on 2021-08-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_flat_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image1Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image2Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image3Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image4Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image5Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image6',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='image6Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='flat',
            name='image1Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='flat',
            name='image2Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='flat',
            name='image3Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='flat',
            name='image4Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='flat',
            name='image5Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='image6',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='flat',
            name='image6Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='image7',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='flat',
            name='image7Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='material',
            name='image1Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='material',
            name='image2Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='material',
            name='image3Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='material',
            name='image4Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='material',
            name='image5Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='image6',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='material',
            name='image6Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='property',
            name='image1Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='property',
            name='image2Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='property',
            name='image3Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='property',
            name='image4Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='property',
            name='image5Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='image6',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='property',
            name='image6Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='image7',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='property',
            name='image7Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='service',
            name='image1Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='service',
            name='image2Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='service',
            name='image3Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='service',
            name='image4Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='service',
            name='image5Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image6',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='service',
            name='image6Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='structure',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='structure',
            name='image1Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='structure',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='structure',
            name='image2Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='structure',
            name='image3',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='structure',
            name='image3Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='structure',
            name='image4',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='structure',
            name='image4Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='structure',
            name='image5',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='structure',
            name='image5Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='structure',
            name='image6',
            field=models.FileField(blank=True, null=True, upload_to='Images'),
        ),
        migrations.AddField(
            model_name='structure',
            name='image6Verify',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]