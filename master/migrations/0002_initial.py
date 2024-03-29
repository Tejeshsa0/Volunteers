# Generated by Django 5.0.1 on 2024-02-04 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        ('user', '0002_alter_otpverificationdata_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterblogdata',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.userdata'),
        ),
        migrations.AddField(
            model_name='mastercourseblogimagedata',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.masterblogdata'),
        ),
        migrations.AddField(
            model_name='mastercourseblogvideodata',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.masterblogdata'),
        ),
        migrations.AddField(
            model_name='mastercoursedata',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.userdata'),
        ),
        migrations.AddField(
            model_name='mastercourseblogvideodata',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.mastercoursedata'),
        ),
        migrations.AddField(
            model_name='mastercourseblogimagedata',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.mastercoursedata'),
        ),
        migrations.AddField(
            model_name='masterblockdata',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='master.masterdistrictdata'),
        ),
    ]
