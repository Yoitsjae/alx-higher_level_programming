-- 13-count_shows_by_genre.sql

-- Use the database
USE hbtn_0d_tvshows;

-- List genres and count of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;
