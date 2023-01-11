-- количество исполнителей в каждом жанре

select musician_id, count(*) 
from styles_musicians sm 
group by musician_id 
order by musician_id 

-- количество треков, вошедших в альбомы 2019-2020 годов

select count(*)
from tracks as t
inner join albums a on t.album_id = a.album_id 
where a.year_of_release
between '2019 years' and '2020 years'

-- средняя продолжительность треков по каждому альбому

select album_id, avg(duration)
from tracks t 
group by album_id 
order by album_id 

-- все исполнители, которые не выпустили альбомы в 2020 году

select distinct m."name", a.year_of_release
from musician m 
left join albums_of_musicians aom on m.musician_id = aom.musician_id
left join albums a on aom.album_id = a.album_id 
where a.year_of_release <> '2020 years'
order by a.year_of_release 

-- названия сборников, в которых присутствует конкретный исполнитель (выберите сами)

select distinct c."name" 
from collections c 
inner join tracks_in_collection tic on c.collection_id = tic.collection_id 
inner join tracks t on tic.track_id = t.track_id
inner join albums a on t.album_id = a.album_id
inner join albums_of_musicians aom on a.album_id = aom.album_id 
inner join musician m on aom.musician_id = m.musician_id 
where m."name" = 'Gorillaz'


-- название альбомов, в которых присутствуют исполнители более 1 жанра

select a."name", count(sm.genre_id)
from albums a 
inner join albums_of_musicians aom on a.album_id = aom.album_id 
inner join styles_musicians sm on aom.musician_id = sm.musician_id 
group by a."name"
having count(sm.genre_id) > 1

-- наименование треков, которые не входят в сборники

select t."name"
from tracks t
where t.track_id 
not in(select track_id from tracks_in_collection tic)

-- исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)

select distinct m."name"
from musician m 
inner join albums_of_musicians aom on m.musician_id = aom.musician_id 
inner join tracks t on aom.album_id = t.album_id 
where t.duration in (select min(t.duration) from tracks t)
group by m."name" 

-- название альбомов, содержащих наименьшее количество треков

select a."name" , count(t."name") 
from albums a 
full join tracks t on t.album_id = a.album_id
group by a.album_id 
having count(t."name") <= (
select count(t."name") 
from albums a 
full join tracks t on t.album_id = a.album_id
group by a.album_id
order by count(t."name") asc
limit 1)
order by count(t."name")
