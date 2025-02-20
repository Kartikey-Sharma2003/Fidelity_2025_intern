SELECT  
    c.customerNumber,
    c.customerName,  
    o.orderNumber,
    o.status,  
    p.productName,
    od.quantityOrdered,  
    od.priceEach,  
    od.orderLineNumber  
FROM  
    fidelity.customers AS c  
JOIN  
    fidelity.orders AS o  
ON  
    c.customerNumber = o.customerNumber  
JOIN  
    fidelity.orderdetails AS od  
ON  
    o.orderNumber = od.orderNumber  
JOIN  
    fidelity.products AS p  
ON  
    od.productCode = p.productCode  
WHERE  
    o.status = 'Pending'  
ORDER BY  
    o.orderDate DESC
