import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repository.settings')
django.setup()

from library.models import LibraryUser

username = 'admin'
password = '12345'
email = 'admin@example.com'

u = LibraryUser.objects.filter(username=username).first()
if not u:
    LibraryUser.objects.create_user(
        email=email,
        username=username,
        password=password,
        first_name='Admin',
        last_name='User',
        phone_number='0000000000',
        is_faculty=False,
        is_admin=True,
        is_allowed=True,
    )
    print('created')
else:
    u.set_password(password)
    u.is_admin = True
    u.is_allowed = True
    u.save()
    print('updated')
