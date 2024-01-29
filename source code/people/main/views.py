from django import http
from django import shortcuts


def home(request):
    return http.HttpResponse('Welcome, it works')


def hello(request, visitor_id):
    return http.HttpResponse(f'Hello, visitor with id of {visitor_id}')


def fully_formed_webpage(request, visitor_name):
    return shortcuts.render(
        request,
        'main/fully_formed_webpage.html',
        context={
            'visitor_name':visitor_name
        }
    )


def people_list(request):
    people = [
        ('Fred', 'Bristol'),
        ('Saskia', 'Barcelona'),
        ('Ahmed', 'Brazil'),
        ('Nadine', 'Breda')
    ]

    return shortcuts.render(
        request,
        template_name='main/people_list.html',
        context={
            'people':people
        }
    )


def tags_and_filters(request):
    # Name, age, is_family, comment
    people = [
        ('Fred', 15, False, ''),
        ('Saskia', 25, True, '<b>Very</b> helpful'),
        ('Ahmed', 1, True, 'Just finding his voice'),
        ('Nadine', 37, False, ''),
    ]

    return shortcuts.render(
        request,
        template_name='main/tags_and_filters.html',
        context=dict(
            people=people,
        )
    )
