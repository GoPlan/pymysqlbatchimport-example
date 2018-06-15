DROP TABLE IF EXISTS data_import;
CREATE TABLE data_import (
	id 					INT PRIMARY KEY,
	item_code 			VARCHAR(255) UNIQUE,
	item_cost 			DOUBLE,
	qty					DOUBLE,
	total				DOUBLE,
	created_ts			DATETIME,
	modified_ts			DATETIME,
	created_ts_varchar 	VARCHAR(255),
	modified_ts_varchar VARCHAR(255),
	INDEX IcreatedTs	(created_ts),
	INDEX ImodifiedTs	(modified_ts)
)
