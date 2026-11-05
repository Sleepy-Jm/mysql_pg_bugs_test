USE `replay_a9c9c8ae55f0c7c34aaa963b`;
SET time_zone="+00:00";
SET NAMES utf8mb4;
CREATE TABLE `employee` (
  `id` INT UNSIGNED AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(255) DEFAULT NULL,
  `surname` VARCHAR(255) DEFAULT NULL,
  `retired` TINYINT(1) DEFAULT NULL,
  PRIMARY KEY(`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB;

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (1, 'Oliver', 'Smith', 0);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (2, 'Jack', 'Williams', 1);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (3, 'Harry', 'Taylor', 1);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (4, 'Charlie', 'Lee', 0);

select
  *
from
  (
    select
      'žlutý_😀' `❤`
  ) `🚀`
where
  `❤` = 'žlutý_😀'
group by
  `🚀`.`❤`
having
  (`❤` = 'žlutý_😀');
