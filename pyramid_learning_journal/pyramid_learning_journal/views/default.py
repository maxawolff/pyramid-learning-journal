"""Docstring yo."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from jounal_entries import entries


@view_config(route_name='home', renderer="pyramid_learning_journal:templates/index.jinja2")
def list_expenses(request):
    """."""
    return {
        'entries': entries
    }


@view_config(route_name="api_detail", renderer="pyramid_learning_journal:templates/detail-entry.jinja2")
def detail(request):
    """."""
    entry_id = int(request.matchdict['id'])
    if entry_id < 0 or entry_id > len(entries) - 1:
        raise HTTPNotFound
    entry = list(filter(lambda entry: entry['id'] == entry_id, entries))[0]
    return {
        'title': entry.title,
        'date': entry.creation_date,
        'body': entry.body
    }


# def list_view(request):
#     with open('pyramid_learning_journal/templates/index.html') as file:
#         return Response(file.read())


# def detail_view(request):
#     with open('pyramid_learning_journal/templates/detail-entry.html') as file:
#         return Response(file.read())


# def create_view(request):
#     with open('pyramid_learning_journal/templates/new-entry.html') as file:
#         return Response(file.read())


# def update_view(request):
#     with open('pyramid_learning_journal/templates/edit-entry.html') as file:
#         return Response(file.read())
