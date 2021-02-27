-- DROP SCHEMA story;

CREATE SCHEMA story AUTHORIZATION postgres;

-- story.chapter definition

-- Drop table

-- DROP TABLE story.chapter;

CREATE TABLE story.chapter (
	"name" varchar NOT NULL,
	id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	available bool NULL,
	story_id int8 NOT NULL
);

-- story."character" definition

-- Drop table

-- DROP TABLE story."character";

CREATE TABLE story."character" (
	id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	"content" varchar NULL,
	story_id int8 NULL
);

-- story.game definition

-- Drop table

-- DROP TABLE story.game;

CREATE TABLE story.game (
	id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	"name" varchar NOT NULL
);

-- story.scene definition

-- Drop table

-- DROP TABLE story.scene;

CREATE TABLE story.scene (
	id int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	chapter_id int8 NULL,
	"content" varchar NULL,
	speech_id int8 NULL,
	"type" varchar NULL
);

