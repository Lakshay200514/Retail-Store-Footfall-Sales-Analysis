
-- ==========================================
-- RETAIL STORE FOOTFALL VS SALES ANALYSIS
-- Analytical SQL Queries
-- ==========================================

-- 1. Total Sales and Footfall
SELECT
    SUM(total_sales) AS total_sales,
    SUM(total_footfall) AS total_footfall
FROM Store_Performance;


-- 2. Store-wise Sales Performance
SELECT
    store_id,
    SUM(total_sales) AS total_sales,
    SUM(total_footfall) AS total_footfall,
    AVG(conversion_rate) AS avg_conversion_rate
FROM Store_Performance
GROUP BY store_id
ORDER BY total_sales DESC;


-- 3. Hourly Sales Analysis
SELECT
    hour,
    SUM(total_sales) AS hourly_sales
FROM Store_Performance
GROUP BY hour
ORDER BY hour;


-- 4. Hourly Footfall Analysis
SELECT
    hour,
    SUM(total_footfall) AS hourly_footfall
FROM Store_Performance
GROUP BY hour
ORDER BY hour;


-- 5. Top 5 Performing Stores
SELECT TOP 5
    store_id,
    SUM(total_sales) AS total_sales
FROM Store_Performance
GROUP BY store_id
ORDER BY total_sales DESC;


-- 6. Daily Sales and Footfall
SELECT
    analysis_date,
    SUM(total_sales) AS daily_sales,
    SUM(total_footfall) AS daily_footfall
FROM Store_Performance
GROUP BY analysis_date
ORDER BY analysis_date;


-- 7. Average Conversion Rate
SELECT
    store_id,
    AVG(conversion_rate) AS avg_conversion_rate
FROM Store_Performance
GROUP BY store_id
ORDER BY avg_conversion_rate DESC;
