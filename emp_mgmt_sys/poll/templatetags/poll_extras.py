from django import template
from poll.models import Question

register = template.Library()

def change_to_upper(value, n):
    """Converts a string into all uppercase"""
    return value.upper()[0:n]

def change_to_upper_all(value):
    """Converts a string into all uppercase"""
    return value.upper()


register.filter('change_upper', change_to_upper)
register.filter('change_upper_all', change_to_upper_all)




@register.simple_tag
def recent_polls(n=5, **kwargs):
    """Return recent n polls"""
    name = kwargs.get("name", "Argument is not passed")
    print(name)
    questions = Question.objects.all().order_by('-created_at')
    return questions[0:n]



# JUst restart the server after adding the tag if it is not reflecting in ui