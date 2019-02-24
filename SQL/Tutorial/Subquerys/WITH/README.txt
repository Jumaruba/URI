QUESTION: You need to find the average number of events for each channel per day.

SOLUTION:

SELECT channel, AVG(events) AS average_events
FROM (SELECT DATE_TRUNC('day',occurred_at) AS day,
             channel, COUNT(*) as events
      FROM web_events 
      GROUP BY 1,2) sub
GROUP BY channel
ORDER BY 2 DESC;


Let's try this again using a WITH statement.


Notice, you can pull the inner query:


SELECT DATE_TRUNC('day',occurred_at) AS day, 
       channel, COUNT(*) as events
FROM web_events 
GROUP BY 1,2


This is the part we put in the WITH statement. Notice, we are aliasing the table as events below:

WITH events AS (
          SELECT DATE_TRUNC('day',occurred_at) AS day, 
                        channel, COUNT(*) as events
          FROM web_events 
          GROUP BY 1,2)


Now, we can use this newly created events table as if it is any other table in our database:


WITH events AS (
          SELECT DATE_TRUNC('day',occurred_at) AS day, 
                        channel, COUNT(*) as events
          FROM web_events 
          GROUP BY 1,2)

SELECT channel, AVG(events) AS average_events
FROM events
GROUP BY channel
ORDER BY 2 DESC;


For the above example, we don't need anymore than the one additional table, but imagine we needed to create a second table to pull from.
We can create an additional table to pull from in the following way:



WITH table1 AS (
          SELECT *
          FROM web_events),

     table2 AS (
          SELECT *
          FROM accounts)


SELECT *
FROM table1
JOIN table2
ON table1.account_id = table2.id;


You can add more and more tables using the WITH statement in the same way. 
The quiz at the bottom will assure you are catching all of the necessary components of these new queries.