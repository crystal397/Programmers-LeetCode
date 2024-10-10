# Write your MySQL query statement below
SELECT A.product_id, 
    COALESCE(ROUND(SUM(CASE 
        WHEN (B.purchase_date BETWEEN A.start_date AND A.end_date) THEN A.price * B.units
        ELSE 0
        END) / NULLIF(SUM(CASE 
        WHEN (B.purchase_date BETWEEN A.start_date AND A.end_date) THEN B.units
        ELSE 0
        END), 0), 2), 0) AS average_price
FROM Prices A
LEFT JOIN UnitsSold B
ON A.product_id = B.product_id
GROUP BY A.product_id