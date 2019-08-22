from django.db import migrations
from .. import ACL_CACHE
from ...cache.operations import StartCacheVersioning


class Migration(migrations.Migration):
    dependencies = [
    ]

    # operations = [StartCacheVersioning(ACL_CACHE)]