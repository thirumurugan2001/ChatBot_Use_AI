CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    passKey TEXT NOT NULL,
    is_active BOOLEAN DEFAULT true
);
CREATE TABLE usersChat (
    id SERIAL PRIMARY KEY,
    userschat TEXT NOT NULL DEFAULT '[]', 
    userId INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT fk_user FOREIGN KEY (userId) REFERENCES users(id) ON DELETE CASCADE
);

SELECT email FROM users
select * from users
select * from usersChat
