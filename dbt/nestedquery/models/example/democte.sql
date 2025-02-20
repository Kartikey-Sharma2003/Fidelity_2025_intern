WITH rename_columns AS (
    SELECT 
        customerNumber AS customer_id,
        customerName AS name,
        phone,
        country
    FROM fidelity.customers
)
SELECT * FROM rename_columns
