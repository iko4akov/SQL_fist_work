from flask import Flask
from utils import find_in_db, find_genre
from bp_find_raiting.view import children_blueprint, family_blueprint, adult_blueprint


app = Flask(__name__)

app.register_blueprint(children_blueprint, url_prefix='/rating')
app.register_blueprint(adult_blueprint, url_prefix='/rating')
app.register_blueprint(family_blueprint, url_prefix='/rating')


@app.get('/movie/<title>')
def title_page(title):
    info_film = [find_in_db(title)]
    return info_film


@app.get('/genre/<genre>')
def genre_page(genre):
    result = find_genre(genre)
    return result


if __name__ == '__main__':
    app.run()
