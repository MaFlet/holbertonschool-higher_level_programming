-- Computes score average of all records in the table second_table of the database hbtn_0c_0 in mySQL server.
SELECT ROUND(AVG(score), 4) AS average
FROM second_table;