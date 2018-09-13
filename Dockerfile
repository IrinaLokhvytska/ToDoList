FROM python:3.6

COPY . /todo_app
WORKDIR /todo_app
RUN pip install pipenv
RUN pipenv install --system --deploy

CMD [ "python", "main.py" ]