DROP TABLE IF EXISTS favorites;

CREATE TABLE favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT,
    release_date TEXT,
    director TEXT,
    writer TEXT,
    actors TEXT,
    poster TEXT
);