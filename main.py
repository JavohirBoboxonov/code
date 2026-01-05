# first=# select p.product_name, od.quantity, o.order_id, o.employee_id, c.contact_name from products as p
# first-# inner join order_details as od on p.product_id = od.product_id
# first-# inner join orders as o on o.order_id = od.order_id
# first-# inner join customers as c on c.customer_id = o.customer_id
# first-# where o.required_date > o.shipped_date and od.quantity > 5
# first-# limit 5;


# first=# select p.product_name, p.unit_price, s.contact_name, od.order_id, c.contact_name from products as p
# first-# inner join order_details as od on od.product_id = p.product_id
# first-# inner join orders as o on od.order_id = o.order_id
# first-# inner join customers as c on c.customer_id = o.customer_id
# first-# inner join suppliers as s on p.supplier_id = s.supplier_id
# first-# where od.quantity > 10
# first-# limit 50;


# first=# SELECT country, COUNT(*) as customer_count 
# FROM customers 
# GROUP BY country 
# HAVING COUNT(*) > 5
# ORDER BY customer_count DESC;

# first=# select p.product_name, od.quantity, o.order_id, o.employee_id, e.first_name, e.last_name, e.country, e.city from products as p
# first-# inner join order_details as od on od.product_id = p.product_id
# first-# inner join orders as o on o.order_id = od.order_id
# first-# inner join employees as e on o.employee_id = e.employee_id
# first-# group by p.product_name, od.quantity, o.order_id, o.employee_id, e.first_name, e.last_name, e.country, e.city
# first-# order by od.quantity desc
# first-# limit 5;
