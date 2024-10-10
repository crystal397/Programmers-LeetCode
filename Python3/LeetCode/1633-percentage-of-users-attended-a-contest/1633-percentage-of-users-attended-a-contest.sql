-- Write your PostgreSQL query statement below
SELECT B.contest_id, ROUND((COUNT(DISTINCT B.user_id)*100.0/(SELECT COUNT(*) FROM Users)),2) AS percentage
FROM Users A
LEFT JOIN Register B
ON A.user_id = B.user_id
where b.contest_id is not null
GROUP BY B.contest_id
ORDER BY percentage DESC, B.contest_id ASC