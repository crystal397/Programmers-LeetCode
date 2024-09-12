-- Write your PostgreSQL query statement below
SELECT name
FROM (SELECT id, name
FROM Customer
EXCEPT
SELECT id, name
FROM Customer
WHERE referee_id = 2)