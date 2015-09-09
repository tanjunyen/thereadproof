# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doc_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='file',
            field=models.FileField(default=datetime.datetime(2015, 9, 9, 20, 39, 16, 195755, tzinfo=utc), upload_to=b'files_to_proofread'),
            preserve_default=False,
        ),
    ]
