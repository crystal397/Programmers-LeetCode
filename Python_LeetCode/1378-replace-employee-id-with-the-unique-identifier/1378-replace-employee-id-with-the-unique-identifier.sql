-- Write your PostgreSQL query statement below
SELECT B.unique_id, A.name
FROM Employees A
LEFT JOIN EmployeeUNI B
ON A.id = b.id 