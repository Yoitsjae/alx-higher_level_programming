-- 100-not_my_genres.sql

-- Use the database
USE hbtn_0d_tvshows;

-- Get the genre IDs linked to Dexter
SELECT genre_id FROM tv_show_genres
WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter');

-- List all genres not linked to Dexter
SELECT name FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id FROM tv_show_genres
    WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
)
ORDER BY name ASC;
