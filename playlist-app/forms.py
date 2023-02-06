"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, FloatField


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    playlist_name = StringField("Playlist Name")
    playlist_desc = StringField("Playlist Description")


class SongForm(FlaskForm):
    """Form for adding songs."""
    song_title = StringField("Song Title")
    song_artist = StringField("Song Artist")

    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
