-- Write your PostgreSQL query statement below
SELECT B.id
FROM Weather A
INNER JOIN Weather B
ON B.recordDate - A.recordDate = 1
AND B.temperature - A.temperature > 0
