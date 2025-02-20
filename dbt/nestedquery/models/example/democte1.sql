{{ config(materialized='view') }}

SELECT  
    c.customerName,  
    c.phone,  
    CONCAT(c.addressLine1, ' ', COALESCE(c.addressLine2, '')) AS address,  
    o.orderDate,  
    o.status  
FROM  
    fidelity.customers AS c  
JOIN  
    fidelity.orders AS o  
ON  
    c.customerNumber = o.customerNumber