# Generated by Django 5.1.5 on 2025-02-03 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraison', '0003_remove_livraison_signature_livraison_nom_employe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livraison',
            old_name='nom_transporteur',
            new_name='nom_chauffeur',
        ),
        migrations.RenameField(
            model_name='livraison',
            old_name='signature_transporteur',
            new_name='signature_chauffeur',
        ),
    ]
