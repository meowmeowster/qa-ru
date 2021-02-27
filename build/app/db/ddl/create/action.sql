-- DROP SCHEMA "action";

CREATE SCHEMA "action" AUTHORIZATION postgres;

-- "action".russian definition

-- Drop table

-- DROP TABLE "action".russian;

CREATE TABLE "action".russian (
	id int8 NOT NULL,
	speech_id int8 NULL,
	story_id int8 NULL,
	"content" varchar NOT NULL,
	"cost" int8 NULL,
	ad_friendly bool NULL,
	requirement varchar NULL,
	"result" varchar NULL
);

