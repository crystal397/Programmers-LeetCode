-- Write your PostgreSQL query statement below
SELECT A.user_id, COALESCE(B.confirmation_rate, 0) AS confirmation_rate
FROM Signups A
LEFT JOIN (
    SELECT user_id, ROUND(SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) * 1.0 / COUNT(user_id), 2) AS confirmation_rate
    FROM Confirmations
    GROUP BY user_id) B
ON A.user_id = B.user_id
