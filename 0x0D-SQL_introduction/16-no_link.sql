-- lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Done by @andergcp
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
