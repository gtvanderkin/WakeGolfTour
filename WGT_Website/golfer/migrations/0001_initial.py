# Generated by Django 3.1.6 on 2021-03-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Golfer',
            fields=[
                ('golfer_id', models.AutoField(primary_key=True, serialize=False)),
                ('golfer_name', models.TextField()),
                ('golfer_birthdate', models.DateField()),
            ],
            options={
                'verbose_name': 'Tournament Golfer',
                'verbose_name_plural': 'Tournament Golfers',
                'db_table': 'Golfer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GolferRoundScores',
            fields=[
                ('grs_id', models.AutoField(primary_key=True, serialize=False)),
                ('grs_total_score', models.IntegerField()),
                ('grs_hole1_score', models.IntegerField()),
                ('grs_hole2_score', models.IntegerField()),
                ('grs_hole3_score', models.IntegerField()),
                ('grs_hole4_score', models.IntegerField()),
                ('grs_hole5_score', models.IntegerField()),
                ('grs_hole6_score', models.IntegerField()),
                ('grs_hole7_score', models.IntegerField()),
                ('grs_hole8_score', models.IntegerField()),
                ('grs_hole9_score', models.IntegerField()),
                ('grs_hole10_score', models.IntegerField()),
                ('grs_hole11_score', models.IntegerField()),
                ('grs_hole12_score', models.IntegerField()),
                ('grs_hole13_score', models.IntegerField()),
                ('grs_hole14_score', models.IntegerField()),
                ('grs_hole15_score', models.IntegerField()),
                ('grs_hole16_score', models.IntegerField()),
                ('grs_hole17_score', models.IntegerField()),
                ('grs_hole18_score', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Golfer Round Scores',
                'verbose_name_plural': 'Golfers Round Scores',
                'db_table': 'GolferRoundScores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TournGolfer',
            fields=[
                ('tg_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'TournGolfer',
                'managed': False,
            },
        ),
    ]
