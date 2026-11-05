log detail:
2025-02-13 11:45:28.563 CST    [4015389]LOG:  00000: received SIGHUP,
reloading configuration files
2025-02-13 11:45:28.563 CST    [4015389]LOCATION: 
process_pm_reload_request, postmaster.c:2104
2025-02-13 11:45:28.564 CST    [4015389]LOG:  22023: invalid value for
parameter "synchronized_standby_slots": "slave"
2025-02-13 11:45:28.564 CST    [4015389]DETAIL:  replication slot "slave"
does not exist
2025-02-13 11:45:28.564 CST    [4015389]LOCATION:  call_string_check_hook,
guc.c:6927
2025-02-13 11:45:28.564 CST    [4015389]LOG:  F0000: configuration file
"/data/pgdata/pg5433/data/postgresql.conf" contains errors; unaffected
changes were applied
2025-02-13 11:45:28.564 CST    [4015389]LOCATION: 
ProcessConfigFileInternal, guc.c:616
2025-02-13 11:45:28.687 CST    [4015389]LOG:  00000: system logger process
(PID 1511029) was terminated by signal 11: Segmentation fault
2025-02-13 11:45:28.687 CST    [4015389]LOCATION:  LogChildExit,
postmaster.c:3097;
