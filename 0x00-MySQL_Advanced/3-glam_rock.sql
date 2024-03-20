-- "glam rock" bands
SELECT
    band_name,
    IFNULL(split - formed, YEAR(2022) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
