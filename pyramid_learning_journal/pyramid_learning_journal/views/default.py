"""Docstring yo."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid_learning_journal.models.entries import Entry
from datetime import datetime
from pyramid.security import remember, forget
from pyramid_learning_journal.security import check_credentials


@view_config(route_name='list',
             renderer="pyramid_learning_journal:templates/index.jinja2")
def home(request):
    """."""
    entries = request.dbsession.query(Entry).all()
    return {
        "entries": entries
    }


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
             renderer="pyramid_learning_journal:templates/edit-entry.jinja2",
             permission='secret')
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


@view_config(route_name='create',
             renderer="pyramid_learning_journal:templates/new-entry.jinja2",
             permission='secret')
def new_entry(request):
    """Creating a new learning journal entry."""
    if request.method == "GET":
        return {}
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


@view_config(route_name='login', renderer='../templates/login.jinja2', require_csrf=False)
def login(request):
    """View for login page."""
    if request.authenticated_userid:
        return HTTPFound(request.route_url('list'))

    if request.method == 'POST':
        username = request.params.get('username', '')
        password = request.params.get('password', '')
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(location=request.route_url('list'), headers=headers)
        else:
            return {'message': 'incorrect login information, please try again'}
    return {}


@view_config(route_name='logout')
def logout(request):
    """When user hits this route, log them out."""
    headers = forget(request)
    return HTTPFound(request.route_url('list'), headers=headers)
