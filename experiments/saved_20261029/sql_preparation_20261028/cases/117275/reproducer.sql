-- MySQL report #117275; source anchors: cmain, c550210
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
set sql_mode='';
drop table  if exists t;
 CREATE TABLE `t` (
 `ID` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PACKAGE_NAME` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '??????????????profile?????',
  `STATE` tinyint NOT NULL COMMENT '???0?????3?????1????????2????????8?????9?????',
  PRIMARY KEY (`ID` DESC) USING BTREE,
  KEY `IDX_PROFILE_TASK_PKGNAME` (`PACKAGE_NAME`) USING BTREE,
  KEY `IDX_PROFILE_TASK_STATE` (`STATE`) USING BTREE
) ENGINE=InnoDB;

insert into t values
(" f7e806c69d2c489cb5e338ab2bfb1151", "com.example.install_faile_yyx               ",   9  ),
(" f7e806c69d2c489cb5e338ab2bfb252", "com.a01tech.massagercn                      ", 2  ),
(" f7e806c69d2c489cb5e338ab2bfb3653", "com.ctrip.harmonynext                       ",    9 ),
(" f7e806c69d2c489cb5e338ab2bf4864", "AR000JOGJD_011                              ",  3 ),
(" f7e806c69d2c489cb5e338ab2bfb5655", "com.xiachufang.recipe                       ",  9 ),
(" f7e806c69d2c489cb5e338ab2bfb6656", "com.example.install_faile_yyx               ", 2  ),
(" f7e806c69d2c489cb5e338ab2bfb7657", "                                            ", 2  ),
(" f7e806c69d2c489cb5e338ab2bfb8658", "NULL                                        ",  2  ),
(" f7e806c69d2c489cb5e338ab2bfb9659", "com.example.install_faile_yyx               ",  2  ),
( " f7e806c69d2c489cb5e338ab2bfb11f", "com.atomicservice.5765880207845661477       ", 3 ),
(" f7e806c69d2c489cb5e338ab2bfb825f", "com.example.install_faile_yyx               ", 2 ),
(" f7e806c69d2c489cb5e338ab2bfb835f",  "com.example.install_faile_yyx               ", 3 );

SELECT /*+ set_var(optimizer_switch='index_merge=off') */  PACKAGE_NAME,STATE FROM `t`  WHERE PACKAGE_NAME='com.example.install_faile_yyx' AND STATE=3;
SELECT /*+ set_var(optimizer_switch='index_merge=on') */  PACKAGE_NAME,STATE FROM `t`  WHERE PACKAGE_NAME='com.example.install_faile_yyx' AND STATE=3;
