SELECT *, 
	COALESCE(primary_poc, 'no POC') AS primary_poc-modified
FROM demo.accounts
WHERE primary_poc IS NULL