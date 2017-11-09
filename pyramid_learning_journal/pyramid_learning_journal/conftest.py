"""Fixture module to be used in testing."""
import pytest
from pyramid import testing
from pyramid_learning_journal.models.meta import Base
from pyramid_learning_journal.models.entries import Entry
from pyramid_learning_journal.data.journal_entries import entries
import transaction
from pyramid_learning_journal.models import get_tm_session
import pdb


@pytest.fixture(scope="session")
def configuration(request):
    """."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://postgres:potato@localhost:5432/test_entries'
    })
    config.include("pyramid_learning_journal.models")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture
def db_session(configuration, request):
    """."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture
def dummy_request(db_session):
    """."""
    return testing.DummyRequest(dbsession=db_session)


all_entries = []
for entry in entries:
    new_entry = Entry(
        title=entry["title"],
        body=entry["body"],
        creation_date=entry["creation_date"]
    )
    all_entries.append(new_entry)


@pytest.fixture
def add_models(dummy_request):
    """Add enties to the test database."""
    dummy_request.dbsession.add_all(all_entries)


@pytest.fixture(scope="session")
def testapp(request):
    """Create a test app for functional testing."""
    from webtest import TestApp
    from pyramid_learning_journal import Configurator

    def main():
        settings = {
            'sqlalchemy.url': 'postgres://postgres:potato@localhost:5432/test_entries'
        }
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('pyramid_learning_journal.routes')
        config.include('pyramid_learning_journal.models')
        config.include('pyramid_learning_journal.security')
        config.scan()
        return config.make_wsgi_app()

    app = main()

    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)  # builds the tables

    def tearDown():
        Base.metadata.drop_all(bind=engine)  # when tests are done, kill tables in DB

    request.addfinalizer(tearDown)

    return TestApp(app)


@pytest.fixture
def fill_the_db(testapp):
    """Fill test app with entry data."""
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        # pdb.set_trace()
        dbsession.add_all(all_entries)

    return dbsession