-- Crear base de datos
CREATE DATABASE catalogo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Crear usuario (puedes cambiar 'django_user' y 'Password123!' por lo que prefieras)
CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'Password123!';

-- Asignar permisos completos sobre la base de datos al usuario
GRANT ALL PRIVILEGES ON catalogo_db.* TO 'django_user'@'localhost';

-- Aplicar los cambios de privilegios
FLUSH PRIVILEGES;