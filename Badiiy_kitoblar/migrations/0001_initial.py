# Generated by Django 4.0.4 on 2022-04-28 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('sahifa', models.PositiveSmallIntegerField()),
                ('janr', models.CharField(choices=[('Badiiy', 'Badiiy'), ('Ilmiy', 'Ilmiy'), ('Hujjatli', 'Hujjatli'), ('Detektiv', 'Detektiv')], max_length=12)),
                ('sana', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('tirik', models.BooleanField()),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('guruh', models.CharField(max_length=10)),
                ('guvohnoma', models.CharField(blank=True, max_length=10)),
                ('kitob_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField()),
                ('qaytardi', models.CharField(choices=[('Ha', 'Ha'), ("Yo'q", "Yo'q")], max_length=5)),
                ('qaytarish_sana', models.DateField()),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Badiiy_kitoblar.kitob')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Badiiy_kitoblar.student')),
            ],
        ),
    ]
