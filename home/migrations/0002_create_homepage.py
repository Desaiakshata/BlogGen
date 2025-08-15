from django.db import migrations

def create_homepage(apps, scheme_editor):
    HomePage = apps.get_model("home.HomePage")

    HomePage.objects.create(
        title="Home-Page"
    )

def remove_homepage(apps, scheme_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_homepage, remove_homepage)
    ]
