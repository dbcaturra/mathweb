# Generated by Django 2.0.13 on 2019-02-14 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CriticalPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criticalpoint', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Dba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dba', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Learning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning', models.CharField(max_length=400)),
                ('dba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Dba')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=400)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thought', models.CharField(max_length=200)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='standard',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Subject'),
        ),
        migrations.AddField(
            model_name='standard',
            name='thought',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Thought'),
        ),
        migrations.AddField(
            model_name='process',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Subject'),
        ),
        migrations.AddField(
            model_name='learning',
            name='process',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='math_area.Process'),
        ),
        migrations.AddField(
            model_name='learning',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Standard'),
        ),
        migrations.AddField(
            model_name='learning',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Subject'),
        ),
        migrations.AddField(
            model_name='learning',
            name='thought',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Thought'),
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ManyToManyField(to='math_area.Subject'),
        ),
        migrations.AddField(
            model_name='dba',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Grade'),
        ),
        migrations.AddField(
            model_name='dba',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Standard'),
        ),
        migrations.AddField(
            model_name='dba',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Subject'),
        ),
        migrations.AddField(
            model_name='dba',
            name='thought',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Thought'),
        ),
        migrations.AddField(
            model_name='criticalpoint',
            name='dba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Dba'),
        ),
        migrations.AddField(
            model_name='criticalpoint',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Grade'),
        ),
        migrations.AddField(
            model_name='criticalpoint',
            name='process',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='math_area.Process'),
        ),
        migrations.AddField(
            model_name='criticalpoint',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Standard'),
        ),
        migrations.AddField(
            model_name='criticalpoint',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Subject'),
        ),
        migrations.AddField(
            model_name='criticalpoint',
            name='thought',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_area.Thought'),
        ),
    ]
