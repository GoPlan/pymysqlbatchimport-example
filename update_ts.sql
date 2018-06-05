UPDATE data_import
SET
createdTs = str_to_date(createdTsVarChar, '%d/%m/%Y'),
modifiedTs = str_to_date(modifiedTsVarChar, '%d/%m/%Y')
WHERE
createdTs IS NULL OR modifiedTs IS NULL
