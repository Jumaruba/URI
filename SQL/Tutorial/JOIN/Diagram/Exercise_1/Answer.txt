SELECT orders.*
FROM orders
JOIN accounts
ON orders.account_id = accounts.id;