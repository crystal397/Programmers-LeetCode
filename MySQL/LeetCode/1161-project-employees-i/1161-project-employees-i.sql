# Write your MySQL query statement below
SELECT A.project_id,
    ROUND((SUM(B.experience_years) / COUNT(*)), 2)
    AS average_years
FROM Project A
LEFT JOIN Employee B
ON A.employee_id = B.employee_id
GROUP BY A.project_id