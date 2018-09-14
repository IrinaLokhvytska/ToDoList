from sanic import Sanic
from todo_app.api import bp


app = Sanic(__name__)

app.static('/static', './static')
app.static('/bootstrap/dist/css/bootstrap.css', '/bootstrap/dist/css/bootstrap.css', name='bootstrap_css')
app.static('/bootstrap/dist/js/bootstrap.js', '/bootstrap/dist/js/bootstrap.js', name='bootstrap_js')

app.blueprint(bp)

app.run(host='0.0.0.0', port=5000, debug=True)
