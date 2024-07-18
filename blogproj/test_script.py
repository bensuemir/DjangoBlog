import os
import django

# Django ayarlarını yapılandırın
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogproj.settings')
django.setup()

# PostSerializer'ı import edin
from blog.api.serializers import PostSerializer

# Test verisi
data = {
    'title': 'Test Post',
    'content': 'This is a test post.'
}

# Serializer'ı kullanın
serializer = PostSerializer(data=data)
if serializer.is_valid():
    print(serializer.data)
else:
    print(serializer.errors)
