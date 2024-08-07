-- ranks country origins of bands ordered by number of fans
-- Column names origin and nb_fans

SELECT origin, fans AS nb_fans FROM metal_bands ORDER BY fans DESC;
