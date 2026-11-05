Currently, PostgreSQL defaults to listen on 'localhost', which translates to
single-stack IPv4 loopback address 127.0.0.1. However, IPv6 is more and more
prevalent, not everything support happy eyeballs. Therefor, when no
listen_addresses are specified and/or if localhost is specified, this should
not default to 127.0.0.1, but instead to '127.0.0.1, ::1' to make PostreSQL
listen both on IPv4 and IPv6 loopback interfaces.


This especially fixes issues with the latest NodeJS v17.;
