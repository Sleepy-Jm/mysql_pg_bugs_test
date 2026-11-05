Then, I update log_hostname to 'yes' in postgresql.conf, and send SIGHUP
signal to reload configuration files.


I saw the logs showing the parameter was updated:
2022-07-03 10:50:54.477 UTC [5955] LOG:  received SIGHUP, reloading
configuration files
2022-07-03 10:50:54.478 UTC [5955] LOG:  parameter "log_hostname" changed to
"yes"


After I disconnected to Postgres, connection log messages kept showing the
IP address (127.0.0.1), which expected to show the host name (localhost).
This means updating log_hostname did not take effect.;
