from django import template

register = template.Library()

@register.filter(name="minutes")
def minutes(timedelta_obj):
    secs = timedelta_obj.total_seconds()
    minutes = int(secs // 60)
    return minutes
