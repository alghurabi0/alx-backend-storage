-- Createing the table if it doesn't exist
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'users')
BEGIN
    CREATE TABLE users (
        id INT IDENTITY(1,1) PRIMARY KEY,
        email NVARCHAR(255) NOT NULL UNIQUE,
        name NVARCHAR(255)
    );
END;
