from django.utils import timezone

def get_current_month():
    return timezone.now().month
