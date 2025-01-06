# Generated by Django 5.1.4 on 2025-01-06 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomrequest',
            options={'ordering': ['-submitted_at'], 'verbose_name': 'Room Request', 'verbose_name_plural': 'Room Requests'},
        ),
        migrations.AlterModelOptions(
            name='universityregistration',
            options={'ordering': ['-submitted_at'], 'verbose_name': 'University Registration', 'verbose_name_plural': 'University Registrations'},
        ),
        migrations.AlterField(
            model_name='roomrequest',
            name='reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_room_requests', to='landlord.landlord'),
        ),
        migrations.AlterField(
            model_name='roomrequest',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_requests', to='student.student'),
        ),
        migrations.AlterField(
            model_name='universityregistration',
            name='reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_university_registrations', to='landlord.landlord'),
        ),
        migrations.AlterField(
            model_name='universityregistration',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_registrations', to='student.student'),
        ),
    ]