-- Report #111097; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
create table `cs_rec_cardactivelog` (
  `formnum` varchar(32)
);
insert into `cs_rec_cardactivelog` values ('20014403205816');
insert into `cs_rec_cardactivelog` values ('20021356099700');

create table `om_wl_log` (
  `worklogid` decimal(14,0) not null,
  `workid` decimal(14,0) not null
);

insert into `om_wl_log` values (20021356105936,20021356099700);
