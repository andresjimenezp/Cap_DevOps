FROM python:3.12-slim

WORKDIR /opt/python-api/

COPY . /opt/python-api/

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app"]

CMD ["--host", "0.0.0.0", "--port", "8000"]