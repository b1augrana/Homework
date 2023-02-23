INSERT INTO Genre(name) 
VALUES ('Indie'), ('Rap'), ('Pop'), ('Rock'), ('Hard rock'), ('House');

INSERT INTO Artist(name) 
VALUES('Dolphin'), ('Post Malone'), ('Arctic Monkeys'), ('twenty one pilots'), ('Nazareth'), ('Placebo'), ('Ed Sheeran'), ('Avicii');

INSERT INTO Album(name, released_at) 
VALUES('442', '2018-01-01'), ('beerbongs & bentleys', '2018-01-01'), ('Tranquility Base Hotel & Casino', '2018-01-01'), ('Trench', '2018-01-01'), ('Tattoed on My Brain', '2018-01-01'), ('Never Let Me Go', '2022-01-01'), ('=', '2021-01-01'), ('TIM', '2019-01-01');

INSERT INTO Track(name, album_id, duration) 
VALUES ('520', 1, 273), ('744', 1, 300), ('Paranoid', 2, 221), ('rockstar', 2, 218), ('Bathphone', 3, 271), ('Science Fiction', 3, 185), ('My Blood', 4, 229), ('Morph', 4, 258), ('Tattoed on My Brain', 5, 169), ('Push', 5, 228), ('Hugz', 6, 231), ('Chemtrails', 6, 271), ('Shivers', 7, 207), ('Bad Habits', 7, 230), ('Heaven', 8, 277), ('Freak', 8, 179);

INSERT INTO Collection(name, released_at) 
VALUES('Rap hits', '2020-01-01'), ('Club Dance', '2020-01-01'), ('Best of indie', '2019-01-01'), ('Best of pop', '2021-01-01'), ('Rock hits', '2019-01-01'), ('Best of 2018', '2018-01-01'), ('All time hits', '2021-01-01'), ('Best of 2022', '2022-12-01');

INSERT INTO genre_artist(genre_id, artist_id) 
VALUES (1, 1), (1, 3), (1, 4), (2, 1), (2, 2), (3, 7), (4, 6), (5, 5), (6, 8);

INSERT INTO artist_album(artist_id, album_id) 
VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8);

INSERT INTO collection_track(collection_id, track_id)
VALUES (1, 3), (1, 4), (2, 15), (2, 16), (3, 6), (3, 8), (4, 13), (4, 14), (5, 9), (5, 12), (6, 4), (6, 7), (7, 4), (7, 13), (8, 11), (8, 12);