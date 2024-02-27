FROM python:3.11-slim

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false --local

RUN poetry install

EXPOSE 8000

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]