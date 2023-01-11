# Generated by Django 3.2 on 2023-01-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_station_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='disabled',
            field=models.BooleanField(default=False, verbose_name='Disabled'),
        ),
        migrations.AlterField(
            model_name='station',
            name='api_key',
            field=models.CharField(help_text='<a onclick="genRand()">Generate new random key</a><script>function genRand() {var result = "INSECURE-";for (var i = 1; i < 21; i++) {result += "abcdefghijklmnopqrstuvwxyz0123456789!@#$%&".charAt(Math.floor(Math.random() * 42));if (i % 5 == 0 && i != 20) result += "-"}document.getElementById("id_api_key").value = result;}if (!document.getElementById("id_api_key").value) genRand()</script>', max_length=32, unique=True, verbose_name='API Key'),
        ),
    ]