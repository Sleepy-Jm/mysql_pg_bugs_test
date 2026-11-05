explain select * from test t join orders o on
t.order_id =o.order_id where t.order_id in (select order_id from orders);
