from sanic import Blueprint
from todo_app.service_resource import home, registration

bp = Blueprint(__name__)

bp.add_route(home, '/', methods=['GET'])
bp.add_route(registration, '/registration')
