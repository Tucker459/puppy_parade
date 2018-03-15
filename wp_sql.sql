/* Analyzing tables for better query and execution plans.
 Creating Indexes on various columns to improve speed and efficiency of queries used.
 psql -U christiantucker -d puppy_parade -a -f wp_sql.sql */

ANALYZE route_stop;

ANALYZE dog_info;

ANALYZE route_stop_time;

CREATE INDEX indx1_route_stop on route_stop (dog_info_id);

CREATE INDEX indx2_route_stop on route_stop (dog_walker_id);

CREATE INDEX indx1_route_stop_time on route_stop_time (route_stop_id);

CREATE INDEX indx1_dog_info on dog_info (id);
