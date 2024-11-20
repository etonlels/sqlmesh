MODEL (
  name example.model
);

SELECT
  NULL AS a
FROM other.model
CROSS JOIN UNNEST(JSON_QUERY_ARRAY(json, '$')) AS label