-- 11-genre_id_all_shows.sql

-- Use the database
USE hbtn_0d_tvshows;

-- Select all shows with corresponding genre IDs
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
