-- Delivery Delay Analysis - Task 2

USE delivery_delay_analysis;

-- S2a - Total delay_days by service type
SELECT
    r.service_type,
    SUM(GREATEST(d.actual_days - d.promised_days, 0)) AS total_delay_days
FROM deliveries d
JOIN routes r ON d.route_id = r.route_id
GROUP BY r.service_type
ORDER BY total_delay_days DESC;

-- S2b - Routes with significant delay
SELECT
    d.route_id,
    r.route,
    SUM(GREATEST(d.actual_days - d.promised_days, 0)) AS total_delay_days
FROM deliveries d
JOIN routes r ON d.route_id = r.route_id
GROUP BY d.route_id, r.route
HAVING SUM(GREATEST(d.actual_days - d.promised_days, 0)) > 8
ORDER BY total_delay_days DESC;

-- S2c - Top two hubs by delay
SELECT
    d.hub,
    SUM(GREATEST(d.actual_days - d.promised_days, 0)) AS total_delay_days
FROM deliveries d
GROUP BY d.hub
ORDER BY total_delay_days DESC, d.hub ASC
LIMIT 2;

-- Diagnostic query - unmatched route keys
SELECT d.route_id
FROM deliveries d
LEFT JOIN routes r ON d.route_id = r.route_id
WHERE r.route_id IS NULL;
