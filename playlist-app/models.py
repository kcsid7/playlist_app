"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)

    songs = db.relationship("PlaylistSong", backref="playlists")

    all_songs = db.relationship("Song", secondary="playlists_songs", backref="all_playlists")

    def __repr__(self):
        return f"<Playlist {self.id} - {self.name}>"


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    artist = db.Column(db.Text, nullable=True)

    playlists = db.relationship("PlaylistSong", backref="songs")

    
    def __repr__(self):
        return f"<Song {self.id} - {self.title} - {self.artist}>"




class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id", ondelete="cascade"), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id", ondelete="cascade"), primary_key=True)



# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
