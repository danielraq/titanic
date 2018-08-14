FROM python:3.6.6-alpine3.7
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt \
    rm requirements.txt
EXPOSE 5002
ENTRYPOINT ["python", "start.py"]