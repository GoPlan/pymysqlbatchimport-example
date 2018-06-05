DROP TABLE IF EXISTS data_import;
CREATE TABLE data_import (
	id 					INT PRIMARY KEY,
	item_code 			VARCHAR(255) UNIQUE,
	item_cost 			DOUBLE,
	qty					DOUBLE,
	total				DOUBLE,
	createdTs			DATETIME,
	modifiedTs			DATETIME,
	createdTsVarChar 	VARCHAR(255),
	modifiedTsVarChar 	VARCHAR(255),
	INDEX IcreatedTs	(createdTs),
	INDEX ImodifiedTs	(modifiedTs)
)
