"""Docstring yo."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from jounal_entries import entries


@view_config(route_name='home',
             renderer="pyramid_learning_journal:templates/index.jinja2")
def home(request):
    """."""
    return {
        'entries': entries
    }


@view_config(route_name="api_detail",
             renderer="pyramid_learning_journal:templates/detail-entry.jinja2")
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


@view_config(route_name='update',
             renderer="pyramid_learning_journal:templates/edit-entry.jinja2")
def edit_entry(request):
    """."""


@view_config(route_name='home',
             renderer="pyramid_learning_journal:templates/new-entry.jinja2")
def new_entry(request):
    """."""
