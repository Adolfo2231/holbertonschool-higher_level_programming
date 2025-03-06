-- This command groups the scores in the second_table and counts the number of occurrences of each score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY
    score
ORDER BY number DESC;