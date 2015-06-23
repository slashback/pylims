from django import template
from journal.models import Division

register = template.Library()


@register.inclusion_tag('journal/tags/division_list.html')
def division_list():
    divisions = Division.objects.all()
    return {'divisions': divisions}
