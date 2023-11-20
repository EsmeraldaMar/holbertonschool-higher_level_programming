-- lists number of records with the same score
-- Task 15
SELECT score, COUNT(score) AS number FROM second_table
    GROUP BY score
    ORDER BY number DESC;