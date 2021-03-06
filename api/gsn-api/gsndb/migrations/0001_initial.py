# Generated by Django 2.1.3 on 2018-11-09 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_data_entry_time', models.DateTimeField(auto_now_add=True)),
                ('attendance_total_unexcused_absences', models.IntegerField()),
                ('attendance_total_excused_absences', models.IntegerField()),
                ('attendance_total_tardies', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Behavior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behavior_incident_date_time', models.DateTimeField()),
                ('behavior_context', models.TextField(max_length=500)),
                ('behavior_result', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_subject', models.CharField(choices=[('MTH', 'Math'), ('SNC', 'Science'), ('HST', 'History'), ('SCS', 'Social Studies'), ('CMP', 'Computer Education'), ('STD', 'Study Hall'), ('SPL', 'Special Education'), ('ENG', 'English'), ('ESL', 'English As a Second Language'), ('SPA', 'Spanish'), ('CHN', 'Chinese'), ('FRH', 'French'), ('GRM', 'German'), ('JPN', 'Japanese'), ('LTN', 'Latin'), ('SNL', 'Subject Not Listed')], default='SNL', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_state', models.CharField(max_length=2)),
                ('district_city', models.CharField(max_length=50)),
                ('district_number', models.SmallIntegerField()),
                ('district_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_data_entry_time', models.DateTimeField(auto_now_add=True)),
                ('grade_metric', models.DecimalField(decimal_places=2, max_digits=3)),
                ('grade_scale', models.SmallIntegerField(choices=[(4, 'Four Point Scale'), (7, 'Seven Point Scale')], default=4)),
                ('grade_is_final', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.Course')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.TextField(max_length=150)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.District')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(max_length=35)),
                ('student_last_name', models.CharField(max_length=35)),
                ('student_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'NonBinary')], default='NB', max_length=2)),
                ('student_birth_date', models.DateField()),
                ('student_state_id', models.IntegerField()),
                ('school', models.ManyToManyField(to='gsndb.School')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSnap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_grade_placement', models.SmallIntegerField(choices=[(0, 'Kindergarten'), (1, 'First Grade'), (2, 'Second Grade'), (3, 'Third Grade'), (4, 'Fourth Grade'), (5, 'Fifth Grade'), (6, 'Sixth Grade'), (7, 'Seventh Grade'), (8, 'Eighth Grade'), (9, 'Ninth Grade'), (10, 'Tenth Grade'), (11, 'Eleventh Grade'), (12, 'Twelfth Grade')], default=0)),
                ('student_attendance_term', models.CharField(choices=[('SPR', 'Spring'), ('SMR', 'Summer'), ('FLL', 'Fall'), ('WNT', 'Winter'), ('SPC', 'Special Term'), ('NSP', 'No Term Specified')], default='NSP', max_length=3)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.School')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.Student')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='student_snap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.StudentSnap'),
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.School'),
        ),
        migrations.AddField(
            model_name='behavior',
            name='student_snap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.StudentSnap'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_snap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsndb.StudentSnap'),
        ),
    ]
