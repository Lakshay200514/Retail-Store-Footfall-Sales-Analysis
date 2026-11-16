
-- Retail Store Footfall vs Sales Analysis
-- Create Store Performance Table

CREATE TABLE Store_Performance (
    performance_id INT IDENTITY(1,1) PRIMARY KEY,

    store_id INT NOT NULL,

    analysis_date DATE NOT NULL,

    hour INT NOT NULL,

    total_sales DECIMAL(18,2),

    total_footfall INT,

    conversion_rate DECIMAL(10,2),

    created_at DATETIME2 DEFAULT GETDATE()
);

-- View table structure
SELECT *
FROM Store_Performance;
