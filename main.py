import os
import django

# Init
os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="django_orm.settings")
django.setup()

from app.models import User

# User(
#     name="Kiril",
#     bio="",
#     email='kirilkuda008',
#     birthday="2009-01-26"
# ).save()

user = User.objects.filter(id=1).first()
# print(user.c)
user.name = "sanya"
user.save()