FROM python:3.11.8-slim

RUN addgroup --system app && adduser --system --group app

ENV HOME=/home/app
ENV APP_HOME=${HOME}/src

RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

COPY . ${APP_HOME}
RUN chown -R app:app ${HOME}

RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

USER app

