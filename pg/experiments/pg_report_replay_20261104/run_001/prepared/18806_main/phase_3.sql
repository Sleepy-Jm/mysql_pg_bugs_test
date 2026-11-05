create table orders_p1 partition of orders for values with (
modulus 32, remainder 0);
