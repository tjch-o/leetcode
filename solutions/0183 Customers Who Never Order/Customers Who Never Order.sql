select name as Customers
from Customers
    left join Orders on Customers.id = Orders.customerid
where Orders.customerid is null;