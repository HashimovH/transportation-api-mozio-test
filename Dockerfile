FROM python:3.10-alpine

LABEL name="transportation-booking-py" maintainer="Hashim Hashimov"

COPY requirements.txt ./

RUN pip install -U setuptools pip wheel \\
    && pip install -r requirements.txt

USER app
COPY --chown=app:app . /app
WORKDIR /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]