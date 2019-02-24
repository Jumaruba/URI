# How to start your SQL data base

All the work here will be done by using the file data.csv.

### How to import CSV data to SQL


First, create a table with the same columns of the file, for example:

```
  CREATE TABLE "data" (Time int, Geo varchar(100), Indic_ed varchar(100), Value float(5), Flag varchar(100));
```

Then type:

```
  COPY data from 'directoy' DELIMITER ',' CSV HEADER
```

For example:

```
  COPY data from '/home/maruba/Desktop/Data.csv' DELIMITER ',' csv header;
```

### How to clean data

You can substitue some values by doing

```
UPDATE 
   table_name
SET 
   column_name = REPLACE(column,old_text,new_text)
WHERE 
   condition
 ```
 
 For example: 
 
 ```
 UPDATE data
set Value = REPLACE(Value, ':', NULL)
where value = ':';
```

### About window function


PostgreSQL’s documentation does an excellent job of introducing the concept of Window Functions: a window function performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result.

Through introducing window functions, we have also introduced two statements that you may not be familiar with: OVER and PARTITION BY. These are key to window functions. Not every window function uses PARTITION BY; we can also use ORDER BY or no statement at all depending on the query we want to run.
