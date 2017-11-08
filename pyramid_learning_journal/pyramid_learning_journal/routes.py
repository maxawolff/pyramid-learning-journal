"""Routes."""


def includeme(config):
    """The routes to be included."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('list', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new-entry')
    config.add_route('update', '/journal/edit-entry/{id:\d+}')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
