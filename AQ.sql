SELECT g.name, count(a.name) FROM genre g 
LEFT JOIN genre_artist ga USING(genre_id) 
LEFT JOIN artist a USING(artist_id)
GROUP BY g.name 
ORDER BY count(artist_id) DESC;  

SELECT a.name, a.released_at, count(track_id) FROM album a 
LEFT JOIN track t USING(album_id)
WHERE a.released_at BETWEEN '2019-01-01' AND '2020-12-31'
GROUP BY a.name, a.released_at;

SELECT a.name, avg(t.duration) FROM album a 
LEFT JOIN track t USING(album_id) 
GROUP BY a.name 
ORDER BY avg(t.duration); 

SELECT DISTINCT a.name FROM artist a 
WHERE a.name NOT IN (
	SELECT DISTINCT a.name FROM artist a
	LEFT JOIN artist_album aa USING(artist_id)
	LEFT JOIN album a2 USING(album_id)
	WHERE a2.released_at BETWEEN '2020-01-01' AND '2020-12-31'
)
ORDER BY a.name;

SELECT DISTINCT c.name FROM collection c 
LEFT JOIN collection_track ct USING(collection_id) 
LEFT JOIN track t USING(track_id)
LEFT JOIN album a USING(album_id)
LEFT JOIN artist_album aa USING(album_id) 
LEFT JOIN artist a2 USING(artist_id) 
WHERE a2.name LIKE '%Post Malone%'
ORDER BY c.name;

SELECT a.name FROM album a 
LEFT JOIN artist_album aa USING(album_id)
LEFT JOIN artist a2 USING(artist_id) 
LEFT JOIN genre_artist ga USING(artist_id) 
LEFT JOIN genre g USING(genre_id) 
GROUP BY a.name 
HAVING count(genre_id) > 1
ORDER BY a.name;

SELECT t.name FROM track t 
LEFT JOIN collection_track ct USING(track_id) 
WHERE ct.track_id IS NULL; 

SELECT a.name, t.duration FROM artist a 
LEFT JOIN artist_album aa USING(artist_id) 
LEFT JOIN album a2 USING(album_id) 
LEFT JOIN track t USING(album_id) 
where t.duration = (SELECT min(duration) FROM track)
ORDER BY a.name;

SELECT DISTINCT a.name FROM album a 
LEFT JOIN track t USING(album_id) 
WHERE t.album_id IN (
	SELECT album_id FROM track
	GROUP BY album_id 
	HAVING count(track_id) = (
		SELECT count(track_id) FROM track
		GROUP BY album_id 
		ORDER BY count(track_id) 
		LIMIT 1
		)
	)
ORDER BY a.name;	

