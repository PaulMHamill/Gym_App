DROP TABLE booking;
DROP TABLE member;
DROP TABLE session;

CREATE TABLE member (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  age VARCHAR(255),
  address VARCHAR(255)
);

CREATE TABLE session (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  date DATE,
  time TIME
);

CREATE TABLE booking (
  id SERIAL PRIMARY KEY,
  member_id INT REFERENCES member(id) ON DELETE CASCADE,
  session_id INT NOT NULL REFERENCES session(id) ON DELETE CASCADE
);
