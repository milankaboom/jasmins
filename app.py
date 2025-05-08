# from flask import Flask, render_template
# import sqlite3
# from pathlib import Path
# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)

# def get_db_connection():
#     """
#     Izveido un atgriež savienojumu ar SQLite datubāzi.
#     """

#     db = Path(__file__).parent / "edienkarte.db"
# # Izveido savienojumu ar SQLite datubāzi
#     conn = sqlite3.connect(db)
# # Nodrošina, ka rezultāti būs pieejami kā vārdnīcas (piemēram: product["name"])
#     conn.row_factory = sqlite3.Row
#     return conn

# def get_product_description(product_id):
#     conn = sqlite3.connect('edienkarte.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT description FROM products WHERE id = ?", (product_id,))
#     result = cursor.fetchone()
#     conn.close()
#     return result[0] if result else None

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/produkti")
# def products():
#     conn = get_db_connection() # Pieslēdzas datubāzei
# # Izpilda SQL vaicājumu, kas atlasa visus produktus
#     products = conn.execute("SELECT * FROM menu_items").fetchall()
#     conn.close() # Aizver savienojumu ar datubāzi
# # Atgriežam HTML veidni "products.html", padodot produktus veidnei
#     return render_template("products.html", products=products)

# @app.route("/produkti/<int:product_id>")
# def products_show(product_id):
#     conn = get_db_connection()
#     product = conn.execute(
#         "SELECT * FROM menu_items WHERE id = ?",
#         (product_id,)
#     ).fetchone()
    

#     if product is None:
#         return "<h1>Produkts nav atrasts!</h1>", 404

#     return render_template("products_show.html", product=product)


# @app.route("/par-mums")
# def about():
#     return render_template("about.html")
# if __name__ == "__main__":
#     app.run(debug=True)



# @app.route('/comment')
# def show_comment():
#     conn = get_db_connection()
#     menu_item_with_comment = conn.execute("SELECT id, name, review FROM movies WHERE review IS NOT NULL AND review != ''").fetchall()
#     return render_template("comment.html", comment=menu_item_with_comment)

# @app.route('/comment/new', methods=['GET', 'POST'])
# def new_review():
#     conn = get_db_connection()
#     if request.method == 'POST':
#         itemsid = request.form['itemsid']
#         comment = request.form['comment']
#         conn.execute("UPDATE movies SET review = ? WHERE id = ?", (comment, itemsid))
#         conn.commit()
#         return redirect('/reviews')
#     menu_items = conn.execute("SELECT id, name FROM menu_items").fetchall()
#     return render_template("new_comment.html", menu_item=menu_items)

# @app.route('/comment/edit/<int:id>', methods=['GET', 'POST'])
# def edit_review(id):
#     conn = get_db_connection()
#     if request.method == 'POST':
#         comment = request.form['comment']
#         conn.execute("UPDATE menu_items SET comment = ? WHERE id = ?", (comment, id))
#         conn.commit()
#         return redirect('/reviews')
#     menu_items = conn.execute("SELECT id, name, comment FROM menu_items WHERE id = ?", (id,)).fetchone()
#     return render_template("comment_edit.html", name=menu_items)

# @app.route('/comment/delete/<int:id>', methods=['POST'])
# def delete_comment(id):
#     conn = get_db_connection()
#     conn.execute("UPDATE menu_items SET comment = NULL WHERE id = ?", (id,))
#     conn.commit()
#     return redirect('/comment')




# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, render_template, request, redirect
import sqlite3
from pathlib import Path

app = Flask(__name__)

def get_db_connection():
    db = Path(__file__).parent / "edienkarte.db"
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produkti")
def products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM menu_items").fetchall()
    conn.close()
    return render_template("products.html", products=products)

@app.route("/produkti/<int:product_id>")
def products_show(product_id):
    conn = get_db_connection()
    product = conn.execute("SELECT * FROM menu_items WHERE id = ?", (product_id,)).fetchone()
    conn.close()
    if product is None:
        return "<h1>Produkts nav atrasts!</h1>", 404
    return render_template("products_show.html", product=product)

@app.route("/par-mums")
def about():
    return render_template("about.html")

# ======== KOMENTĀRI (CRUD) ========

@app.route('/comment')
def show_comment():
    conn = get_db_connection()
    comments = conn.execute("""
        SELECT id, name, comment 
        FROM menu_items 
        WHERE comment IS NOT NULL AND comment != ''
    """).fetchall()
    conn.close()
    return render_template("comments.html", comments=comments)

@app.route('/comment/new', methods=['GET', 'POST'])
def new_comment():
    conn = get_db_connection()
    if request.method == 'POST':
        itemsid = request.form['itemsid']
        comment = request.form['comment']
        conn.execute("UPDATE menu_items SET comment = ? WHERE id = ?", (comment, itemsid))
        conn.commit()
        conn.close()
        return redirect('/comment')
    menu_items = conn.execute("SELECT id, name FROM menu_items").fetchall()
    conn.close()
    return render_template("new_comment.html", menu_items=menu_items)

@app.route('/comment/edit/<int:id>', methods=['GET', 'POST'])
def edit_comment(id):
    conn = get_db_connection()
    if request.method == 'POST':
        comment = request.form['comment']
        conn.execute("UPDATE menu_items SET comment = ? WHERE id = ?", (comment, id))
        conn.commit()
        conn.close()
        return redirect('/comment')
    menu_item = conn.execute("SELECT id, name, comment FROM menu_items WHERE id = ?", (id,)).fetchone()
    conn.close()
    return render_template("comment_edit.html", menu_item=menu_item)

@app.route('/comment/delete/<int:id>', methods=['POST'])
def delete_comment(id):
    conn = get_db_connection()
    conn.execute("UPDATE menu_items SET comment = NULL WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/comment')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
