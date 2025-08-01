# Write your MySQL query statement below
SELECT s.name
FROM SalesPerson as s
WHERE s.sales_id NOT IN (
    SELECT DISTINCT o.sales_id 
    FROM Orders AS o 
    LEFT JOIN Company as c
    ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)