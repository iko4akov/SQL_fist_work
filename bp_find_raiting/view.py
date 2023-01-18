from bp_find_raiting.dao.utils import find_rating
from flask import Blueprint


children_blueprint = Blueprint('children_blueprint', __name__)
family_blueprint = Blueprint('family_blueprint', __name__)
adult_blueprint = Blueprint('adult_blueprint', __name__)


@children_blueprint.get('/children')
def page_find_children():
    result = find_rating("G")
    return result


@family_blueprint.get('/family')
def page_find_family():
    result = find_rating(["G", "PG", "PG-13"])
    return result

@adult_blueprint.get('/adult')
def page_find_adult():
    result = find_rating(["R", "NC-17"])
    return result

