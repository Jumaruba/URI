In a quiz question in the previous Basic SQL lesson, you saw this question:

Create a column that divides the standard_amt_usd by the standard_qty to find the unit price for standard paper for each order. 
Limit the results to the first 10 orders, and include the id and account_id fields. NOTE - you will be thrown an error with 
the correct solution to this question. This is for a division by zero. You will learn how to get a solution without an error 
to this query when you learn about CASE statements in a later section.

Let's see how we can use the CASE statement to get around this error.

SELECT id, account_id, standard_amt_usd/standard_qty AS unit_price
FROM orders
LIMIT 10;


Now, let's use a CASE statement. 
This way any time the standard_qty is zero, we will return 0, and otherwise we will return the unit_price.


SELECT account_id, CASE WHEN standard_qty = 0 OR standard_qty IS NULL THEN 0
                        ELSE standard_amt_usd/standard_qty END AS unit_price
FROM orders
LIMIT 10;
