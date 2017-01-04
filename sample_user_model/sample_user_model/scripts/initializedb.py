import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import User

ENTRIES = [

    {
        "id": 0,
        "username": "jordan",
        "password": "password0",
        "firstname": "jordan",
        "lastname": "schatzman",
        "email": "j.schatzman@outlook.com",
        "favoritefood": "sushi"
    },

    {
        "id": 1,
        "username": "bob",
        "password": "password1",
        "firstname": "bob",
        "lastname": "steve",
        "email": "bobsteve@gmail.com",
        "favoritefood": "pizza"
    },

    {
        "id": 2,
        "username": "ed",
        "password": "password2",
        "firstname": "mike",
        "lastname": "johnson",
        "email": "mike@outlook.com",
        "favoritefood": "burgers"
    },

]

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
   # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session_factory = get_session_factory(engine)
    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        for entry in ENTRIES:
            model = User(username=entry['username'],
                         password=entry['password'],
                         firstname=entry['firstname'],
                         lastname=entry['lastname'],
                         email=entry['email'],
                         favoritefood=entry['favoritefood'])
            dbsession.add(model)
