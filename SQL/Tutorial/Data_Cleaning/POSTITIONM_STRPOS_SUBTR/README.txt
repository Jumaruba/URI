SELECT first_name,
	last_name,
	city_state,
	POSITION(',' IN city_state) AS comma_position,
	STRPOS(city_state,',') AS substr_comma_position,
	LOWER(city_state) AS lowercase,
	UPPER(city_state) AS uppercase,
	LEFT(city_state, POSITION(',' IN city_state) -1) AS city)
FROM demo.customer_data
	

LENGTH(city_state)