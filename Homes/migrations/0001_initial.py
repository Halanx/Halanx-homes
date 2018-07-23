# Generated by Django 2.0.7 on 2018-07-22 11:45

import Homes.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, choices=[('In-House', 'In-House'), ('Society', 'Society')], max_length=25, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Homes.utils.get_amenity_picture_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_no', models.CharField(blank=True, max_length=10, null=True)),
                ('available', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_no', models.CharField(blank=True, max_length=10, null=True)),
                ('bhk_count', models.PositiveIntegerField(default=1)),
                ('floor', models.PositiveIntegerField(default=1)),
                ('rent', models.CharField(blank=True, max_length=10, null=True)),
                ('deposit', models.CharField(blank=True, max_length=10, null=True)),
                ('available', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rules', models.TextField(blank=True, null=True)),
                ('cover_pic_url', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('available_from', models.DateField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
                ('street_address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('house_type', models.CharField(blank=True, choices=[('Apartment', 'Apartment'), ('Independent', 'Independent'), ('Villa', 'Villa')], max_length=25, null=True)),
                ('furnish_type', models.CharField(blank=True, choices=[('Fully furnished', 'Fully furnished'), ('Semi furnished', 'Semi furnished'), ('Unfurnished', 'Unfurnished')], max_length=25, null=True)),
                ('available_accomodation_types', multiselectfield.db.fields.MultiSelectField(choices=[('shared', 'Shared rooms'), ('private', 'Private rooms'), ('flat', 'Entire house')], max_length=25)),
                ('accomodation_allowed', multiselectfield.db.fields.MultiSelectField(choices=[('Girls', 'Girls'), ('Boys', 'Boys'), ('Family', 'Family')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='HouseAmenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_amenities', to='Homes.Amenity')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='Homes.House')),
            ],
        ),
        migrations.CreateModel(
            name='HouseMonthlyExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accomodation_type', models.CharField(choices=[('shared', 'Shared rooms'), ('private', 'Private rooms'), ('flat', 'Entire house')], default='flat', max_length=25)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HousePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Homes.utils.get_house_picture_upload_path)),
                ('is_cover_pic', models.BooleanField(default=False)),
                ('rank', models.PositiveIntegerField(default=1)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pictures', to='Homes.House')),
            ],
        ),
        migrations.CreateModel(
            name='HouseVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('scheduled_visit_time', models.DateTimeField()),
                ('is_visited', models.BooleanField(default=False)),
                ('actual_visit_time', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='house_visits', to='Homes.Customer')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visits', to='Homes.House')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrivateRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(blank=True, max_length=10, null=True)),
                ('rent', models.FloatField()),
                ('deposit', models.FloatField()),
                ('available', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='private_rooms', to='Homes.House')),
            ],
        ),
        migrations.CreateModel(
            name='SharedRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(blank=True, max_length=10, null=True)),
                ('sharing_limit', models.PositiveIntegerField(default=1)),
                ('rent', models.FloatField()),
                ('deposit', models.FloatField()),
                ('available', models.BooleanField(default=True)),
                ('visible', models.BooleanField(default=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shared_rooms', to='Homes.House')),
            ],
        ),
        migrations.CreateModel(
            name='SubAmenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Homes.utils.get_sub_amenity_picture_upload_path)),
                ('amenity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_amenities', to='Homes.Amenity')),
            ],
        ),
        migrations.AddField(
            model_name='housemonthlyexpense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='house_monthly_expenses', to='Homes.MonthlyExpenseCategory'),
        ),
        migrations.AddField(
            model_name='housemonthlyexpense',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_expenses', to='Homes.House'),
        ),
        migrations.AddField(
            model_name='houseamenity',
            name='sub_amenities',
            field=models.ManyToManyField(related_name='house_sub_amenities', to='Homes.SubAmenity'),
        ),
        migrations.AddField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='houses', to='Homes.HouseOwner'),
        ),
        migrations.AddField(
            model_name='flat',
            name='house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flats', to='Homes.House'),
        ),
        migrations.AddField(
            model_name='bed',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='beds', to='Homes.SharedRoom'),
        ),
    ]
