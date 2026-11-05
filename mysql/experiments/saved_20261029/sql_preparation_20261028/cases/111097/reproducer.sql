-- Report #111097; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
select * from cs_rec_cardactivelog c, om_wl_log l where l.worklogid = (select case when exists (select 1 from om_wl_log where workid = c.formnum) then (select worklogid from om_wl_log) end max_worklogid from dual);
SELECT * FROM cs_rec_cardactivelog c JOIN om_wl_log l ON c.formnum=l.workid;
