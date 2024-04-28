# Generated by Django 5.0.2 on 2024-04-25 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssessmentAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='customer',
        ),
        migrations.AlterField(
            model_name='assessment',
            name='alignment_engineer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessment_template',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='customer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='alignment_engineer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vcio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='proposedproject',
            name='customer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='assessment',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='customer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recommendationproposedproject',
            name='proposed_project',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recommendationproposedproject',
            name='recommendation',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='technologyinventory',
            name='customer',
            field=models.IntegerField(),
        ),
    ]
