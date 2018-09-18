from sanic.response import html
from db.todo_lists import ToDoList
from db.user import User

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('static', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True
)


async def render(tpl, **kwargs) -> object:
    """Asynchronous function for rendering templates"""
    template = env.get_template(tpl)
    content = await template.render_async(kwargs)
    return html(content)


async def home(request: object) -> object:
    """Asynchronous function for rendering page with current tasks"""
    to_do_class = ToDoList(request.app.db)
    to_do_list = await to_do_class.find_all_lists()
    content = await render('home.html', title='Sanic', to_do_list=to_do_list)
    return content


async def registration(request: object) -> object:
    """Asynchronous function for registration users"""
    user_class = User(request.app.db)
    data = {
        'login': 'ilokh',
        'firstname': 'Iryna',
        'lastname': 'Lokhvytska'
    }
    await user_class.insert_user(data)
    users = await user_class.find_all_users()
    content = await render('user.html', title='Sanic', users=users)
    return content
