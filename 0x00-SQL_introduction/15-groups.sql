-- Sleects number of records eth samecscore value
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
