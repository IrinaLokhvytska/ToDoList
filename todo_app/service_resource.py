from sanic.response import html
from db.todo_lists import ToDoList

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
