When we JOIN tables together, it is nice to give each table an alias. Frequently an alias is just the first letter of the table name. You actually saw something similar for column names in the Arithmetic Operators concept.

Example:

FROM tablename AS t1
JOIN tablename2 AS t2
Before, you saw something like:


SELECT col1 + col2 AS total, col3


Frequently, you might also see these statements without the AS statement. 
Each of the above could be written in the following way instead, and they would still produce the exact same results:



FROM tablename t1
JOIN tablename2 t2

and...

SELECT col1 + col2 total, col3