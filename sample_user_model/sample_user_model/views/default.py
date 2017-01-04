from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from pyramid.httpexceptions import HTTPFound
from ..models import MyModel, User


@view_config(route_name='home', renderer='../templates/home.jinja2')
def home_view(request):
    entries = request.dbsession.query(User).order_by(User.id).all()
    entry_list = []
    for entry in entries:
        entry_list.append(entry)
    return {'entries': entry_list}



@view_config(route_name='register', renderer='../templates/register.jinja2')
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        favoritefood = request.POST['favoritefood']
        entry = User(username=username,
                     firstname=firstname,
                     lastname=lastname,
                     email=email,
                     password=password,
                     favoritefood=favoritefood)
        request.dbsession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    if request.method == "GET":
        return {}




db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_sample_user_model_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
