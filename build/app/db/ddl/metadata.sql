-- DROP SCHEMA metadata;

CREATE SCHEMA metadata AUTHORIZATION postgres;

-- metadata.russian definition

-- Drop table

-- DROP TABLE metadata.russian;

CREATE TABLE metadata.russian (
	id int8 NOT NULL,
	"table" varchar NULL,
	"content" varchar NULL,
	outer_id int8 NULL
);

-- metadata."user" definition

-- Drop table

-- DROP TABLE metadata."user";

CREATE TABLE metadata."user" (
	id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	"name" varchar NOT NULL,
	"language" varchar NOT NULL,
	balance int8 NULL
);

-- metadata.client definition

-- Drop table

-- DROP TABLE metadata.client;

CREATE TABLE metadata.client (
	app_build varchar NULL,
	is_production bool NULL,
	debug_mode bool NULL
);

