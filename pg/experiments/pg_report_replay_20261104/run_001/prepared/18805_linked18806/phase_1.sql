create table orders(order_id int, name char(10)) partition by hash
(order_id);
