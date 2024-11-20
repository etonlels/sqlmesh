MODEL (
  name example.model
);

SELECT
  JSON_VALUE(value, '$') AS value
FROM other.table