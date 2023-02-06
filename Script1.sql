CREATE TABLE IF NOT EXISTS Genre ( 
genre_id SERIAL PRIMARY KEY,
name VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Artist ( 
artist_id SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL,
genre_id INTEGER REFERENCES Genre(genre_id)
);

CREATE TABLE IF NOT EXISTS Genre_Artist ( 
id SERIAL PRIMARY KEY,
artist_id INTEGER REFERENCES Artist(artist_id),
genre_id INTEGER REFERENCES Genre(genre_id) 
);

CREATE TABLE IF NOT EXISTS Album ( 
album_id SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL,
artist_id INTEGER REFERENCES Artist(artist_id), 
released_at DATE NOT null CHECK (released_at > 1900)
);

CREATE TABLE IF NOT EXISTS Artist_Album ( 
id SERIAL PRIMARY KEY,
album_id INTEGER REFERENCES Album(album_id),
artist_id INTEGER REFERENCES Artist(artist_id)
);

CREATE TABLE IF NOT EXISTS Track ( 
track_id SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL,
album_id INTEGER REFERENCES Album(album_id), 
duration INTEGER NOT NULL CHECK (duration > 0)
);


CREATE TABLE IF NOT EXISTS Collection ( 
collection_id SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL,
released_at DATE NOT NULL CHECK (released_at > 1900)
);

CREATE TABLE IF NOT EXISTS Collection_Track ( 
id SERIAL PRIMARY KEY,
track_id INTEGER REFERENCES Track(track_id),
collection_id INTEGER REFERENCES Collection(collection_id)
);
