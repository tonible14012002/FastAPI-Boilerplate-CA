FROM python:3.12-alpine as requirements-stage
# --------- requirements ---------

WORKDIR /tmp

RUN pip install poetry poetry-plugin-export

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


# --------- final image build ---------
FROM python:3.12-alpine

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code

# -------- replace with comment to run with gunicorn --------
CMD ["uvicorn", "cmd.server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
