SELECT
    station_name,
    DATE(date) AS rainfall_date,
    SUM(rainfall_mm) AS total_rainfall_mm
FROM {{ ref('stg_rainfall') }}
GROUP BY 1,2
ORDER BY rainfall_date DESC