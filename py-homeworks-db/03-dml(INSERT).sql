-- добавляем стили


INSERT INTO style(name)
VALUES('rock');

INSERT INTO style(name)
VALUES('hip-hop');

INSERT INTO style(name)
VALUES('Indie');

INSERT INTO style(name)
VALUES('jazz');

INSERT INTO style(name)
VALUES('electro');

INSERT INTO style(name)
VALUES('electronic rock');

INSERT INTO style(name)
VALUES('funk');

INSERT INTO style(name)
VALUES('pop-rock');

INSERT INTO style(name)
VALUES('rock `n` roll');

INSERT INTO style(name)
VALUES('pop');


-- добавляем музыкантов


INSERT INTO musician(name)
VALUES('Nirvana');

INSERT INTO musician(name)
VALUES('Gorillaz');

INSERT INTO musician(name)
VALUES('Kanye West');

INSERT INTO musician(name)
VALUES('The Killers');

INSERT INTO musician(name)
VALUES('Coldplay');

INSERT INTO musician(name)
VALUES('Louis Armstrong');

INSERT INTO musician(name)
VALUES('Blank & Jones');

INSERT INTO musician(name)
VALUES('The Prodigy');

INSERT INTO musician(name)
VALUES('Michael Jackson');

INSERT INTO musician(name)
VALUES('The Beatles');

INSERT INTO musician(name)
VALUES('Elvis Aaron Presley');

INSERT INTO musician(name)
VALUES('Mariah Carey');


--добавляем альбомы


INSERT INTO albums(name, year_of_release)
VALUES('Nevermind', '1992');

INSERT INTO albums(name, year_of_release)
VALUES('Demon Days', '2005');

INSERT INTO albums(name, year_of_release)
VALUES('Incesticide', '1988');

INSERT INTO albums(name, year_of_release)
VALUES('Gorillaz', '2001');

INSERT INTO albums(name, year_of_release)
VALUES('Graduation', '2007');

INSERT INTO albums(name, year_of_release)
VALUES('Hot Fuss', '2003');

INSERT INTO albums(name, year_of_release)
VALUES('Parachutes', '2000');

INSERT INTO albums(name, year_of_release)
VALUES('What a Wonderful World', '1967');

INSERT INTO albums(name, year_of_release)
VALUES('Relax Edition 14', '2022');

INSERT INTO albums(name, year_of_release)
VALUES('Experience', '1992');

INSERT INTO albums(name, year_of_release)
VALUES('Thriller', '1983');

INSERT INTO albums(name, year_of_release)
VALUES('Anthology 3', '1968');

INSERT INTO albums(name, year_of_release)
VALUES('The King and Eye', '1956');

INSERT INTO albums(name, year_of_release)
VALUES('Daydream', '1955');


-- добавляем треки


INSERT INTO tracks(name, duration, album_id)
VALUES('Smells Like Teen Spirit', 280, 1);

INSERT INTO tracks(name, duration, album_id)
VALUES('Feel Good Inc.', 207, 2);

INSERT INTO tracks(name, duration, album_id)
VALUES('All Alone', 210, 2);

INSERT INTO tracks(name, duration, album_id)
VALUES('Downer', 103, 3);

INSERT INTO tracks(name, duration, album_id)
VALUES('Clint Eastwood', 349, 4);

INSERT INTO tracks(name, duration, album_id)
VALUES('Flashing Lights', 237, 5);

INSERT INTO tracks(name, duration, album_id)
VALUES('Mr. Brightside', 222, 6);

INSERT INTO tracks(name, duration, album_id)
VALUES('Yellow', 269, 7);

INSERT INTO tracks(name, duration, album_id)
VALUES('What A Wonderful World', 141, 8);

INSERT INTO tracks(name, duration, album_id)
VALUES('Nothing`s Happening By The Sea', 250, 9);

INSERT INTO tracks(name, duration, album_id)
VALUES('Hyperspeed', 316, 10);

INSERT INTO tracks(name, duration, album_id)
VALUES('Billie Jean', 294, 11);

INSERT INTO tracks(name, duration, album_id)
VALUES('Hey Jude', 428, 12);

INSERT INTO tracks(name, duration, album_id)
VALUES('Don`t Be Cruel', 124, 13);

INSERT INTO tracks(name, duration, album_id)
VALUES('One Sweet Day', 283, 14);


-- добавляем сборники

INSERT INTO collections(name, year_of_release)
VALUES('With the Lights Out', '1992');

INSERT INTO collections(name, year_of_release)
VALUES('Official World Top 100 Airplay Songs', '2005');

INSERT INTO collections(name, year_of_release)
VALUES('Canadian Billboard Albums', '2001');

INSERT INTO collections(name, year_of_release)
VALUES('UK CD single', '2007');

INSERT INTO collections(name, year_of_release)
VALUES('UK Singles Chart', '2000');

INSERT INTO collections(name, year_of_release)
VALUES('Rock on the Net - ARC Weekly Top 40', '1967');

INSERT INTO collections(name, year_of_release)
VALUES('Brit Awards', '1992');

INSERT INTO collections(name, year_of_release)
VALUES('Billboard Hot 100', '1995');


-- добавляем жанры в которых исполняют музыканты

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(1, 1);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(1, 2);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(2, 2);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(2, 3);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(3, 4);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(3, 5);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(4, 6);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(5, 7);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(6, 8);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(7, 9);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(8, 10);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(9, 11);

INSERT INTO styles_musicians(genre_id, musician_id)
VALUES(10, 12);


--добавляем альбомы музыкантов

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(1, 1);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(1, 3);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(2, 2);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(2, 4);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(3, 5);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(4, 6);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(5, 7);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(6, 8);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(7, 9);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(8, 10);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(9, 11);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(10, 12);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(11, 13);

INSERT INTO albums_of_musicians(musician_id, album_id)
VALUES(12, 14);


--добавляем треки в коллекции

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(1, 1);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(1, 4);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(2, 2);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(2, 3);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(2, 7);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(3, 5);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(4, 6);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(4, 10);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(5, 8);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(6, 9);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(7, 11);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(8, 12);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(8, 13);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(8, 14);

INSERT INTO tracks_in_collection(collection_id, track_id)
VALUES(8, 15);
