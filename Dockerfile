FROM python:3.9.10-slim@sha256:2d8048d453fbac5076f571a1a7dd837148aecfb45df0c1d454abd075384ca783
RUN apt-get update

RUN groupadd -g 4937 python && useradd -r -u 4937 -g python python

RUN mkdir /usr/app && chown python:python /usr/app

USER 4937
WORKDIR /usr/app

RUN /usr/local/bin/python -m venv /usr/app/venv

COPY --chown=python:python pythonmqtt.py /usr/app/
COPY --chown=python:python pythonmqtt.ini /usr/app/
COPY --chown=python:python requirements.txt /usr/app/

RUN /usr/app/venv/bin/pip install --no-cache-dir --requirement /usr/app/requirements.txt

ENV PATH="/usr/app/venv/bin:$PATH"

CMD [ "python", "pythonmqtt.py" ]

