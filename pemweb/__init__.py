from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession, Base

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_tm')
    config.add_static_view(name='static', path='static')
    config.scan()
    return config.make_wsgi_app()
