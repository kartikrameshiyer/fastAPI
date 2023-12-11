FROM python:3
RUN pip install poetry
WORKDIR /tmp
COPY ./pyproject.toml ./poetry.lock /temp/ 
RUN poetry install
