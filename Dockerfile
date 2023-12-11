FROM python:3
RUN pip install poetry
WORKDIR /tmp
COPY /* .
RUN poetry install
CMD ["main.py"]


