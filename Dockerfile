FROM alpine:latest

RUN apk update \
    && apk add python3 py3-pip

RUN python3 -m pip install Flask

COPY ./ /app/

# RUN python3 -m pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["python3", "/app/app.py"]
