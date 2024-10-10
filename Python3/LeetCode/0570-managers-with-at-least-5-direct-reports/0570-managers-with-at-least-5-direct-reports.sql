-- Write your PostgreSQL query statement below
SELECT B.name
FROM (
    SELECT managerId, COUNT(managerId) AS counts
    FROM Employee
    GROUP BY managerId
    HAVING managerId IS NOT NULL AND COUNT(managerId) >= 5) A
INNER JOIN Employee B
ON A.managerId = B.id