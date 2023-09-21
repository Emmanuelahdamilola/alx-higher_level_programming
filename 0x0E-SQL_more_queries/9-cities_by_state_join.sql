-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.

SELECT c.`id`, c.`name`, s.`name` FROM `cities` AS c INNER JOIN `states` AS s ON c.`state_id` = s.`id` ORDER BY c.`id`;
