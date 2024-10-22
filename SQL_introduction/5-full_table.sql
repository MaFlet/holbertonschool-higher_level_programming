-- Prints following description of the table first_table fromt the database hbtn_0c_0 in MySQL server
SELECT COLUMN_NAME, COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'first_table'
ORDER BY ORDINAL_POSITION;
