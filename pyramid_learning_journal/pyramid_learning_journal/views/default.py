"""Docstring yo."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
import pdb


entries = [{'id': 1, 'title': 'Day 1', 'creation_date': '10/16/17', 'body': 'some words and some text'},
           {'id': 2, 'title': 'Day 2', 'creation_date': '10/17/17', 'body': 'some words and some text'},
           {'id': 3, 'title': 'Day 3', 'creation_date': '10/18/17', 'body': 'some words and some text'},
           {'id': 4, 'title': 'Day 4', 'creation_date': '10/19/17', 'body': 'some words and some text'},
           {'id': 5, 'title': 'Day 5', 'creation_date': '10/20/17', 'body': 'some words and some text'},
           {'id': 6, 'title': 'Day 6', 'creation_date': '10/23/17', 'body': 'some words and some text'},
           {'id': 7, 'title': 'Day 7', 'creation_date': '10/24/17', 'body': 'some words and some text'},
           {'id': 8, 'title': 'Day 8', 'creation_date': '10/25/17', 'body': 'some words and some text'},
           {'id': 9, 'title': 'Day 9', 'creation_date': '10/26/17', 'body': 'some words and some text'},
           {'id': 10, 'title': 'Day 10', 'creation_date': '10/27/17', 'body': "Some good news and some bad news today. We finished our work for day 3, our server works as expected, sending back the file that we asked for, passing all of our tests. However we had a problem with our gevent server which was giving us an OS error that none of the TA's could figure out, (though they were all awesome and really tried to help!). Anyways I'm feeling pretty good about the class so far, though this was a bit frustrating. The code review session today was very helpful, it emphasized the importance of writing tests."},
           {'id': 11, 'title': 'Day 11', 'creation_date': '10/30/17', 'body': "Today we walked through how to use pyramid to host our own sites. I think this is the proper terminology for this, we can serve up our html files, give them custom routes and even more probably. It doesn't sound like a lot but there is a lot to it and was not easy to do. However it is much easier than trying to write our own servers and handle all possible edge cases. I also worked on deploying a site to heroku again, only this time in python instead of javascript. Always a few issues there but thankfully it went up without too much trouble."},
           {'id': 12, 'title': 'Day 12', 'creation_date': '10/31/17', 'body': "Today was interesting. We spent most of our time working on our binary heap, which was harder than I thought it would be. We tried using nodes at first but eventually we ran into a bunch of problems with this. Once we switched over to using a list it was easier but we still took a while to figure out exactly what should happen, right before we were going to switch to the learning journal though we got our push method working. Working with pyramid has been ... interesting? It doesn't seem too hard, though I haven't quite finished it, but I also don't totally understand it yet. I'm sure I will eventually though."}]


@view_config(route_name='list',
             renderer="pyramid_learning_journal:templates/index.jinja2")
def home(request):
    """."""
    return {
        'entries': entries
    }


@view_config(route_name="detail",
             renderer="pyramid_learning_journal:templates/detail-entry.jinja2")
def detail(request):
    """."""
    entry_id = int(request.matchdict['id'])
    if entry_id < 0 or entry_id > len(entries) + 1:
        raise HTTPNotFound
    entry = list(filter(lambda entry: entry['id'] == entry_id, entries))[0]
    # pdb.set_trace()
    return {
        'title': entry['title'],
        'date': entry['creation_date'],
        'body': entry['body'],
        'number': entry['id']
    }


@view_config(route_name='update',
             renderer="pyramid_learning_journal:templates/edit-entry.jinja2")
def edit_entry(request):
    # pdb.set_trace()
    """."""
    entry_id = int(request.matchdict['id'])
    # pdb.set_trace()
    if entry_id < 0 or entry_id > len(entries) + 1:
        raise HTTPNotFound
    entry = list(filter(lambda entry: entry['id'] == entry_id, entries))[0]
    # pdb.set_trace()
    return {
        'title': entry['title'],
        'date': entry['creation_date'],
        'body': entry['body'],
        'number': entry['id']
    }


@view_config(route_name='create',
             renderer="pyramid_learning_journal:templates/new-entry.jinja2")
def new_entry(request):
    """."""
    return {
        'entry': entries
    }
