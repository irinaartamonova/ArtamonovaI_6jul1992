SELECT DISTINCT name FROM Regions;

SELECT m.name, m.season, m.edible
FROM Mushrooms m
JOIN Categories c ON m.category_id = c.category_id
WHERE c.name = 'Трубчатые';

SELECT c.name, COUNT(m.mushroom_id) AS mushroom_count
FROM Categories c
LEFT JOIN Mushrooms m ON c.category_id = m.category_id
GROUP BY c.name
ORDER BY mushroom_count DESC;

SELECT m.name, m.description
FROM Mushrooms m
JOIN Regions r ON m.primary_region_id = r.region_id
WHERE m.edible = TRUE
AND r.region_id IN (SELECT region_id FROM Regions ORDER BY size DESC LIMIT 5);

SELECT m.name
FROM Mushrooms m
JOIN Categories c ON m.category_id = c.category_id
JOIN Regions r ON m.primary_region_id = r.region_id
WHERE m.season = 'весна'
AND c.name = 'Пластинчатые'
AND r.size < 6000;