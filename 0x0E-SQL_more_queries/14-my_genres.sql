-- uses hbtn_0d_tvshows database to lists genres of the show Dexter
-- uses databse to lists rows in table corresponding to rows in another
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;