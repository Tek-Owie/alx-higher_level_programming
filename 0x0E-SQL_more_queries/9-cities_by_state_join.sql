-- lists all cities contained in the database hbtn_0d_usa.
SELECT id, name, name
FROM cities
INNER JOIN states
    ON cities.state_id = states.id
WHERE state_id = 1
ORDER BY cities.id ASC;
