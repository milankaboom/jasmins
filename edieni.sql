-- SELECT * FROM menu_items
-- -- ✅ Izveido tabulu 'categories'
-- CREATE TABLE IF NOT EXISTS categories (
--     id INTEGER PRIMARY KEY,
--     name TEXT NOT NULL
-- );

-- -- ✅ Ievieto kategorijas
-- INSERT INTO categories (name)
-- VALUES 
--     ('Zupas'),
--     ('Pamatēdieni'),
--     ('Deserti');

-- -- ✅ Pievieno kolonnu 'category_id', ja tās vēl nav (ignorē kļūdu, ja tā jau eksistē)
-- ALTER TABLE menu_items ADD COLUMN category_id INTEGER REFERENCES categories(id);

-- -- ✅ Izveido tabulu 'users'
-- CREATE TABLE IF NOT EXISTS users (
--     id INTEGER PRIMARY KEY,
--     name TEXT NOT NULL
-- );

-- -- ✅ Ievieto lietotājus
-- INSERT INTO users (name)
-- VALUES 
--     ('Anna'),
--     ('Jānis');

-- -- ✅ Izveido tabulu 'comments'
-- CREATE TABLE IF NOT EXISTS comments (
--     id INTEGER PRIMARY KEY,
--     content TEXT NOT NULL,
--     user_id INTEGER,
--     menu_item_id INTEGER,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY(user_id) REFERENCES users(id),
--     FOREIGN KEY(menu_item_id) REFERENCES menu_items(id)
-- );

-- -- ✅ Ievieto ēdienus ar kategorijām (ievēro kļūdaino kolonnas nosaukumu "desciption")
-- INSERT INTO menu_items (name, desciption, price, image, category_id)
-- VALUES
--     ('Tomātu zupa', 'Garšīga tomātu zupa ar baziliku', 4.50, 'zupatomat.jpg', 1),
--     ('Cēzara salāti', 'Salāti ar vistu, krutoniem un Cēzara mērci', 5.50, 'cezarsalati.jpg', 2);

-- -- ✅ Ievieto komentārus
-- INSERT INTO comments (content, user_id, menu_item_id)
-- VALUES
--     ('Ļoti garšīgi!', 1, 1),
--     ('Iesaku pamēģināt!', 2, 2);

-- -- ✅ Papildus: komentāru pārskats ar lietotāja un ēdiena nosaukumu
-- SELECT 
--     c.id AS comment_id,
--     c.content,
--     u.name AS user_name,
--     m.name AS menu_item_name,
--     c.created_at
-- FROM comments c
-- JOIN users u ON c.user_id = u.id
-- JOIN menu_items m ON c.menu_item_id = m.id;
