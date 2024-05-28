"""A file for all the extra utilities used in the project"""

from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name="has_group")
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()


"""
Usage:
{% if request.user|has_group:"mygroup" %} 
    <p>User belongs to my group 
{% else %}
    <p>User doesn't belong to mygroup</p>
{% endif %}
"""
