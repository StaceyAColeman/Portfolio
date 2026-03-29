import os
import django  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
django.setup()

# Now your original command will work:
#from django.contrib.auth.models import User
#print(User.objects.all())


from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='stace')
print(user.is_active, user.is_staff)
