CREATE TABLE IF NOT EXISTS style (
	genre_id INTEGER SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS musician (
	musician_id INTEGER SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS styles_musicians (
	styles_musicians_id INTEGER SERIAL PRIMARY KEY,
	genre_id INTEGER REFERENCES style(genre_id),
	musician_id INTEGER REFERENCES musician(musician_id)
);

CREATE TABLE IF NOT EXISTS albums (
	album_id INTEGER SERIAL PRIMARY KEY,
	name TEXT NOT NULL
	year_of_release DATE NOT NULL,
	
);

CREATE TABLE IF NOT EXISTS albums_of_musicians (
	albums_of_musicians_id INTEGER SERIAL PRIMARY KEY,
	musician_id INTEGER REFERENCES musician(musician_id),
	album_id INTEGER REFERENCES albums(album_id)
);

CREATE TABLE IF NOT EXISTS tracks (
	track_id INTEGER SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	duration FLOAT NOT NULL,
	album_id INTEGER REFERENCES albums(album_id)
);

CREATE TABLE IF NOT EXISTS collections (
	collection_id INTEGER SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	year_of_release DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS tracks_in_collection (
	tracks_in_collection_id INTEGER SERIAL PRIMARY KEY,
	collection_id INTEGER REFERENCES collections(collection_id),
	track_id INTEGER REFERENCES tracks(track_id)
);
