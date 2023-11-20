-- Lists record of table with both score and name
-- Task 11
SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;