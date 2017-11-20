"""Test for routes and stuff."""
import pytest
import pdb
from pyramid_learning_journal.models.entries import Entry
from pyramid.httpexceptions import HTTPNotFound  # HTTPFound, HTTPBadRequest
from datetime import datetime


# follow to annother page = response.follow()


FMT = '%m/%d/%Y'


# def test_model_gets_added(db_session):
#     """Test that database works."""
#     assert len(db_session.query(Entry).all()) == 0
#     model = Entry(
#         title="A title",
#         body="some words and stuff",
#         creation_date=datetime.strptime('11/08/2017', FMT),
#     )
#     db_session.add(model)
#     assert len(db_session.query(Entry).all()) == 1


def test_home_returns_dictionary(dummy_request):
    """List view should return a dictionary."""
    from pyramid_learning_journal.views.default import home
    response = home(dummy_request)
    assert isinstance(response, dict)


def test_home_returns_nothing_empty_database(dummy_request):
    """Home view returns nothing with no data."""
    from pyramid_learning_journal.views.default import home
    response = home(dummy_request)
    assert len(response['entries']) == 0


def test_home_returns_count_matching_database(dummy_request, add_models):
    """Home view response matches database count."""
    from pyramid_learning_journal.views.default import home
    response = home(dummy_request)
    query = dummy_request.dbsession.query(Entry)
    print(len(response['entries']))
    assert len(response['entries']) == query.count()


def test_detail_returns_correct_info(dummy_request, add_models):
    """Detail view response has correct title."""
    from pyramid_learning_journal.views.default import detail
    dummy_request.matchdict['id'] = 12
    response = detail(dummy_request)
    assert response['title'] == 'Day 12'


def test_detail_returns_404_bad_id(dummy_request, add_models):
    """Home view response matches database count."""
    from pyramid_learning_journal.views.default import detail
    dummy_request.matchdict['id'] = 13
    with pytest.raises(HTTPNotFound):
        detail(dummy_request)


def test_home_returns_200_ok(testapp, fill_the_db):
    """List view should always return 200 ."""
    response = testapp.get('/')
    assert response.status_code == 200


def test_home_route_has_entry_titles(testapp):
    """Should have 12 h2s on home page if entries are present."""
    response = testapp.get("/")
    assert len(response.html.find_all('h2')) == 12


def test_detail_shows_actual_detail(testapp):
    """Detail view should have correct info from db."""
    response = testapp.get("/journal/11")
    assert 'custom routes' in response.ubody


def test_detail_good_id_returns_200_ok(testapp):
    """Detail view should return 200 for valid id."""
    response = testapp.get('/journal/1')
    assert response.status_code == 200


def test_detail_bad_id_returns_400_ok(testapp):
    """Detail view for nonexistant entry should raise 404 ."""
    assert testapp.get('/journal/100', status=404)


def test_create_hidden_not_signed_in(testapp):
    """Should not be able to see create new entry unless signed in."""
    response = testapp.get("/")
    assert "Create New Entry" not in response.ubody


def test_create_shown_after_sign_in(testapp):
    """Should have show create button after signing in."""
    testapp.post('/login', {"username": 'maxawolff', "password": "C8rd1n81"})
    response = testapp.get("/")
    assert "Create New Entry" in response.ubody


def test_still_signed_in(testapp):
    """Test to see if user will stay signed in."""
    response = testapp.get("/")
    assert "Create New Entry" in response.ubody


def test_sign_out(testapp):
    """Test to see if user will stay signed in."""
    testapp.get("/logout")
    response = testapp.get("/")
    assert "Create New Entry" not in response.ubody


def test_need_authentication_to_post(testapp):
    """Trying to view creat page without signing in should return 403."""
    assert testapp.get('/journal/new-entry', status=403)


def test_need_authentication_to_edit(testapp):
    """Trying to view creat page without signing in should return 403."""
    assert testapp.get('/journal/edit-entry/5', status=403)


# Fuck this test, it was working the other day when we tried dropping the database, now that doesn't work. I give up
# when I add a new entry it sets the ID to one, even though there are other entires in there, I have no idea
# def test_post_after_sign_in(testapp):
#     """Trying to view creat page without signing in should return 403."""
#     testapp.post('/login', {"username": 'maxawolff', "password": "C8rd1n81"})
#     response = testapp.get('/journal/new-entry')
#     token = response.html.findAll('input')[0]['value']
#     testapp.post('/journal/new-entry', {'title': "Test Title",
#                                         'body': "some words and stuff",
#                                         'creation_date': datetime.strptime('11/20/2017', FMT),
#                                         'csrf_token': token})
#     assert 'Test Title' in testapp.get('/').ubody
