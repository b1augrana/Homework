SELECT name, released_at FROM album 
WHERE released_at >= '2018-01-01' AND released_at < '2019-01-01';

SELECT name, duration FROM track
ORDER BY duration DESC 
LIMIT 1;

SELECT name FROM track
WHERE duration >= 210
ORDER BY duration DESC;

SELECT name FROM collection
WHERE released_at BETWEEN  '2018-01-01' AND '2020-12-31';

SELECT name FROM artist
WHERE NOT name LIKE '% %';

SELECT name FROM track
WHERE LOWER(name) LIKE '%my%';