-- Lists all records of second table without listing rows without a name value
-- Task 16
SELECT score, name FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;