from sanic.response import html
from db.todo_lists import ToDoLists

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('static', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True
)

to_do_class = ToDoLists()


async def render(tpl, **kwargs):
    template = env.get_template(tpl)
    content = await template.render_async(kwargs)
    return html(content)


async def home(request):
    to_do_list = await to_do_class.find_all_lists()
    content = await render('home.html', title='Sanic', to_do_list=to_do_list)
    return content
