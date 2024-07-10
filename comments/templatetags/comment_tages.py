from django import template

register = template.Library()


@register.filter
def only_active_comments(comments):
    return comments.filter(active=True)


@register.filter
def number_active_comments(comments):
    return len(comments.filter(active=True))


@register.filter
def star_rating(star):
    number_char = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
    }
    return number_char[star]
