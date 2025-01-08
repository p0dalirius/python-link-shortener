FROM alpine:latest

RUN apk update \
    && apk add python3 py3-pip

COPY ./ /app/

WORKDIR /app/

RUN python3 -m pip install flask --break-system-packages

EXPOSE 5000

CMD ["sh"]
