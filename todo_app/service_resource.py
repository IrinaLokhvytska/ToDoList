from sanic.response import json, html, text

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('static', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True
)


async def render(tpl, **kwargs):
    template = env.get_template(tpl)
    content = await template.render_async(kwargs)
    return html(content)


async def home(request):
    test = {'pip': 'pop', 'foo': 'bar'}
    content = await render('home.html', title='Sanic', data='blob', test=test)
    return content
