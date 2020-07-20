from dateutil.parser import parse
from sqlalchemy import orm, create_engine
from config import SQLALCHEMY_DATABASE_URI
from app import Artist, Show, Venue
from migrations.data._396f7a7f3f7b.venue_data import venue_data
from migrations.data._396f7a7f3f7b.artist_data import artist_data
from migrations.data._396f7a7f3f7b.show_data import show_data

engine = create_engine(SQLALCHEMY_DATABASE_URI)

with engine.connect() as connection:
    connection.execute('DELETE FROM "Show"')
    connection.execute('DELETE FROM "Venue"')
    connection.execute('DELETE FROM "Artist"')
    session = orm.Session(bind=connection)
    for data in venue_data:
        venue = Venue(**data)
        session.add(venue)

    for data in artist_data:
        artist = Artist(**data)
        session.add(artist)

    for data in show_data:
        start_time = parse(data['start_time'])
        data['start_time'] = start_time
        show = Show(**data)
        session.add(show)

    session.commit()
