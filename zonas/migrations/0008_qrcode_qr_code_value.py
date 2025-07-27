import uuid
from django.db import migrations, models

def generate_uuid_for_qrcode(apps, schema_editor):
    QRCode = apps.get_model('zonas', 'QRCode')
    for qrcode in QRCode.objects.all():
        if not qrcode.qr_code_value:
            qrcode.qr_code_value = uuid.uuid4()
            qrcode.save()

class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0007_placa_max_pessoas_catamara_placa_max_pessoas_miudas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='qr_code_value',
            field=models.UUIDField(
                blank=True,
                editable=False,
                help_text='Valor único para o QR Code físico.',
                null=True
            ),
        ),
        migrations.RunPython(generate_uuid_for_qrcode, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='qrcode',
            name='qr_code_value',
            field=models.UUIDField(
                default=uuid.uuid4,
                unique=True,
                editable=False,
                help_text='Valor único para o QR Code físico.'
            ),
        ),
    ]
