CREATE TABLE books (
  id INTEGER,
  title TEXT,
  author TEXT
);
-- Do not modify above this line --
-- Alter books table by adding column published year
ALTER TABLE books ADD COLUMN published_year INTEGER;

-- modify id column to be called isb
ALTER TABLE books RENAME COLUMN id TO isbn;

--DROP author column
ALTER TABLE books DROP COLUMN author;

-- Do not modify below this line --
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'books'
ORDER BY column_name;
