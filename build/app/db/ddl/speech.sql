-- DROP SCHEMA speech;

CREATE SCHEMA speech AUTHORIZATION postgres;

-- speech.russian definition

-- Drop table

-- DROP TABLE speech.russian;

CREATE TABLE speech.russian (
	id int8 NOT NULL,
	story_id int8 NULL,
	chapter_id int8 NULL,
	"content" varchar NOT NULL,
	character_id int8 NULL,
	callable bool NULL,
	"next" int8 NULL
);

