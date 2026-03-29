
from django.contrib.auth.models import User
u = User.objects.get(username='your_username')
u.is_staff = True
u.is_superuser = True
u.save()

