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
