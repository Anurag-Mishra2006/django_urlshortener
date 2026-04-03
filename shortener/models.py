import string
import random
from django.db import models

def generate_short_code():
    length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class URL(models.Model):
    original_url = models.URLField(max_length=10000)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"