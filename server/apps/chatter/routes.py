from apps.chatter.views import IndexView


def setup_routes(app):
    app.router.add_route('GET', '/', IndexView, name='index')