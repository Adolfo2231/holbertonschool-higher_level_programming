-- This command selects the score and name from the second_table where the name is not NULL and orders them by score in descending order
SELECT score, name
FROM second_table
WHERE
    name IS NOT NULL
ORDER BY score DESC;