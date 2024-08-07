-- lists all bands with Glam rock as their main style
-- ranked by their longevity

SELECT band_name, (split - formed) AS lifespan FROM metal_bands
WHERE split IS NOT NULL AND formed IS NOT NULL AND style="black"
ORDER BY lifespan DESC;
