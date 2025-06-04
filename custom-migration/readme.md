Writing a custom migration in Django allows you to execute arbitrary Python code during the migration process—ideal when you need to:

- Backfill or transform data.

- Execute non-schema-changing database commands.

- Use custom logic that isn't supported by standard migration operations.


--------------------

Step-by-Step Guide

1. Modify Your Model
Add a new field in your model:


<pre>
# app/models.py
class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, blank=True, null=True)  # new field
</pre>


2. Create Initial Migration

<pre>
python manage.py makemigrations your_app
</pre>


3. Create a Custom Data Migration

Now generate an empty migration where you’ll add custom code:

<pre>
python manage.py makemigrations your_app --empty --name populate_full_name
</pre>

4. Edit the Migration File

Open the migration file and add logic:

<pre>
from django.db import migrations

def populate_full_name(apps, schema_editor):
    UserProfile = apps.get_model('your_app', 'UserProfile')
    for profile in UserProfile.objects.all():
        profile.full_name = f"{profile.first_name} {profile.last_name}"
        profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('your_app', '0001_initial'),  # depends on the migration that added full_name
    ]

    operations = [
        migrations.RunPython(populate_full_name),
    ]
</pre>


5. Apply the Migration

<pre>
python manage.py migrate your_app
</pre>