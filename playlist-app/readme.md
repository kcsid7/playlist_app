## Playlist-app

To get this application running, make sure you do the following in the Terminal:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `createdb playlist-app`
5. `flask run`





INSERT INTO playlists_songs (playlist_id, song_id) VALUES (1, 1), (1, 2), (1, 4), (1, 6), (2, 3), (2, 7), (1, 5), (3, 8);

INSERT INTO songs (artist, title) VALUES ('Rihanna', 'Umbrella'), ('50 Cent', 'In Da Club'), ('Akon', 'Mr Lonely'), ('Lady Gaga', 'Romance'), ('Killers', 'Mr Brightside'), ('Journey', 'Dont stop believing'), ('Killers', 'When We Were Young'), ('Bieber', 'Bach'), ('David Bowie', 'Starman'), ('Bach', 'Symphony 99');

INSERT INTO playlists (name, description) VALUES ('Party', 'Party Playlist'), ('Road Trip', 'Tripping in the road'), ('Study', 'Focus');
