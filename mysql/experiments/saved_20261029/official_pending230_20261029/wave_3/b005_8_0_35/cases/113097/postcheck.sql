-- Read-only postchecks for report 113097; run in the same disposable schema/session.
SELECT createdAt,timezone FROM temp; SELECT CONVERT_TZ('2022-02-15 16:47:12','+00:00','+00:00') AS fixed_offset_control; SELECT @case_optimizer;
