UPDATE data_import
SET
created_ts = str_to_date(created_ts_varchar, '%d/%m/%Y'),
modified_ts = str_to_date(modified_ts_varchar, '%d/%m/%Y')
WHERE
created_ts IS NULL OR modified_ts IS NULL
