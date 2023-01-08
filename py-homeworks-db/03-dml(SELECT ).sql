-- название и год выхода альбомов, вышедших в 2018 году

SELECT name, year_of_release 
FROM albums 
WHERE year_of_release = '2018 years'

-- название и продолжительность самого длительного трека

SELECT name, duration 
FROM tracks 
ORDER BY duration desc
LIMIT 1

-- название треков, продолжительность которых не менее 3,5 минуты

SELECT name 
FROM tracks 
WHERE duration >= 210

-- названия сборников, вышедших в период с 2018 по 2020 год включительно

SELECT name 
FROM collections 
WHERE year_of_release 
BETWEEN '2018 years' and '2020 years'

-- исполнители, чье имя состоит из 1 слова

SELECT name 
FROM musician 
WHERE (LENGTH(name) - LENGTH(replace(name, ' ', ''))) < 1

-- название треков, которые содержат слово "мой"/"my"

SELECT name 
FROM tracks 
WHERE name 
LIKE '%мой%';

SELECT name 
FROM tracks 
WHERE name 
LIKE '%my%'
