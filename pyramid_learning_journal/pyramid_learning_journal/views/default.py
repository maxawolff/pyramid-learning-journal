"""Docstring yo."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid_learning_journal.models.entries import Entry
from datetime import datetime
import pdb


@view_config(route_name='list',
             renderer="pyramid_learning_journal:templates/index.jinja2")
def home(request):
    """."""
    entries = request.dbsession.query(Entry).all()
    return {
        "entries": entries
    }
    # rev_entries = reversed(entries)
    # return {
    #     'entries': rev_entries
    # }


@view_config(route_name="detail",
             renderer="pyramid_learning_journal:templates/detail-entry.jinja2")
def detail(request):
    """."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(entry_id)
    if entry:
        return_val = {
            'title': entry.title,
            'date': entry.creation_date,
            'body': entry.body,
            'number': entry.id
        }
        return return_val
    else:
        raise HTTPNotFound


@view_config(route_name='update',
             renderer="pyramid_learning_journal:templates/edit-entry.jinja2")
def edit_entry(request):
    """View to handle updating an existing entry."""
    entry_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(entry_id)
    if not entry:
        raise HTTPNotFound
    if request.method == "GET":
        return {
            'title': entry.title,
            'date': entry.creation_date,
            'body': entry.body,
            'number': entry_id
        }
    if request.method == "POST" and request.POST:
        entry.title = request.POST['title']
        entry.creation_date = datetime.strptime(request.POST['date'], '%Y-%m-%d')
        entry.body = request.POST['body']
        request.dbsession.flush()
        return HTTPFound(request.route_url('detail', id=entry.id))
    # # pdb.set_trace()
    # """."""
    # entry_id = int(request.matchdict['id'])
    # # pdb.set_trace()
    # if entry_id < 0 or entry_id > len(entries) + 1:
    #     raise HTTPNotFound
    # entry = list(filter(lambda entry: entry['id'] == entry_id, entries))[0]
    # # pdb.set_trace()
    # return {
    #     'title': entry['title'],
    #     'date': entry['creation_date'],
    #     'body': entry['body'],
    #     'number': entry['id']
    # }


@view_config(route_name='create',
             renderer="pyramid_learning_journal:templates/new-entry.jinja2")
def new_entry(request):
    """Creating a new learning journal entry."""
    if request.method == "POST":
        form_data = request.POST
        new_entry = Entry(
            title=form_data['title'],
            body=form_data['body'],
            creation_date=datetime.now().strftime("%m/%d/%Y")
        )
        request.dbsession.add(new_entry)
        return HTTPFound(request.route_url('list'))
    return {}
