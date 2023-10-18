-- 10-genre_id_by_show.sql

-- Use the database
USE hbtn_0d_tvshows;

-- Select shows with corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
