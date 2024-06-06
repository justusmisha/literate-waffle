CREATE TABLE IF NOT EXISTS forms (
    id SERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    datetime TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    instagram TEXT NOT NULL
);