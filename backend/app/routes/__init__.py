from .v1 import v1_api


def all_routes(app):
    app.include_router(v1_api)