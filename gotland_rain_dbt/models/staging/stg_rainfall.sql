SELECT
    date,
    value AS rainfall_mm,
    quality,
    station_id,
    station_name,
    parameter,
    unit
FROM GOTLAND_RAIN.RAW.RAINFALL_RAW