__author__ = 'luis'

# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for

from OCR import app

#from OCR.movies.models import Movie


mod_OCR = Blueprint('OCR', __name__, url_prefix='/')
mod_upload = Blueprint('upload', __name__, url_prefix='/upload/')


@mod_OCR.route('/', methods=['GET'])
def ocr():
    """Render page to display current movies in the database
    :return index.html:
    """

    return render_template('movies/index.html', movies_list=_movies.movies_list)

@mod_upload.route('/upload', methods=['GET'])
def upload():
    """Render page to display current movies in the database
    :return index.html:
    """

    return render_template('movies/index.html', movies_list=_movies.movies_list)




"""
@mod_movie.route('', methods=['GET', 'POST'])
def movie():
    """Render page to display current movies in the database
    :return index.html:
    """
    _movies = Movies()

    if request.method == 'GET':
        return render_template('movies/new_movie.html', name="John Doe")
    else:
        _movie = Movie()
        _movie.title, _movie.year, _movie.genre, _movie.director, _movie.main_cast, _movie.mpaa_rating, _movie.my_rating \
            = request.form["title"], \
              request.form["year"], \
              request.form["genre"], \
              request.form["director"], \
              request.form["main_cast"], \
              request.form["mpaa_rating"], \
              request.form["my_rating"]

        result = _movie.insert()

        if app.VALIDATION_FAIL == result:
            flash('Validation Fail with fields: ')
            flash(request.form["title"] + " " +  " " + str(request.form["year"]) + " " + request.form["genre"] + " " +
                  request.form["director"] + " " + request.form["main_cast"] + " " + request.form["mpaa_rating"] + " " +
                  str(request.form["my_rating"]))
            return render_template('movies/index.html', movies_list=_movies.movies_list)
        elif app.INSERTION_FAIL == result:
            flash('Insertion Fail')
            return render_template('movies/index.html', movies_list=_movies.movies_list)
        else:
            flash('Success')
            return render_template('movies/index.html', movies_list=_movies.movies_list)
""

# Register missing page handler
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404