INSERT INTO route_stop (id, dog_walker_id, dog_info_id, address, is_pickup,
next_id) VALUES
(1, 2, 0, '31 Mediterranean Ave', 'true', 1),
(2, 2, 1, '78 Baltic Ave', 'true', 3),
(3, 2, 2, '12 Oriental Ave', 'true', 4),
(5, 2, 0, '31 Mediterranean Ave', 'false', null),
(5, 2, 1, '78 Baltic Ave', 'false', null),
(5, 2, 2, '12 Oriental Ave', 'false', null);


INSERT INTO dog_info (id, breed, name, weight) VALUES
(3, 'yorkie', 'Henry', 5);
