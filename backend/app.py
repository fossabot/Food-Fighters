import flask
import sqlite3

api = flask.Flask(__name__)

@api.route("/")
def hello_world():
    return "<h1>Homepage</h1>"

@api.route("/addrecipe")
def addrecipe():
    return flask.render_template("/recipes.html")

@api.route("/submitrecipe", methods = ['POST'])
def submitrecipe():
    conn = sqlite3.connect('data/recipes.db')
    c = conn.cursor()

    recipe_name = flask.request.form['recipe_name']
    ingredients = flask.request.form['ingredients']
    steps = flask.request.form['steps']

    c.execute(f'''INSERT INTO recipes (recipe_name, ingredients, steps, poster_id) \
                  VALUES("{recipe_name}", "{ingredients}", "{steps}", {-1})''')
    conn.commit()
    conn.close()

    return flask.redirect("/")

@api.route("/display")
def display():
  """ 
  Test display function. Grabs recipe name from database
  and send to React for display on UI.
  """
  conn = sqlite3.connect('data\recipes.db')
  cursor = conn.cursor()

  recipe_id = 3   # Hardcoded to select eggnog recipe
  cursor.execute(f'''SELECT * from recipes WHERE recipe_id = {recipe_id}''')

  name = cursor.fetchall()[0][1]
  
  conn.close()
  return {"recipe_name": name}