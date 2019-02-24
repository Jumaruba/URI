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


PostgreSQL’s documentation does an excellent job of introducing the concept of Window Functions:https://www.postgresql.org/docs/9.1/tutorial-window.html. 

A window function performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result.

Through introducing window functions, we have also introduced two statements that you may not be familiar with: *OVER* and _PARTITION BY_. These are key to window functions. Not every window function uses _PARTITION BY_; we can also use _ORDER BY_ or no statement at all depending on the query we want to run.

//source: udacity, business analyst course

### Percentiles

You can use window functions to identify what percentile (or quartile, or any other subdivision) a given row falls into. The syntax is NTILE(*# of buckets*). In this case, ORDER BY determines which column to use to determine the quartiles (or whatever number of ‘tiles you specify).
Expert Tip

In cases with relatively few rows in a window, the NTILE function doesn’t calculate exactly as you might expect. For example, If you only had two records and you were measuring percentiles, you’d expect one record to define the 1st percentile, and the other record to define the 100th percentile. Using the NTILE function, what you’d actually see is one record in the 1st percentile, and one in the 2nd percentile.

In other words, when you use a NTILE function but the number of rows in the partition is less than the NTILE(number of groups), then NTILE will divide the rows into as many groups as there are members (rows) in the set but then stop short of the requested number of groups. If you’re working with very small windows, keep this in mind and consider using quartiles or similarly small bands.

You can check out a complete list of window functions in Postgres (the syntax Mode uses) in the Postgres documentation.

//source: udacity, business analyst course
