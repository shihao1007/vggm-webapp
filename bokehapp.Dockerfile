FROM continuumio/miniconda3

LABEL maintainer="shihao1007@gmail.com"

RUN conda install -y bokeh numpy pandas nltk

VOLUME '/app'

EXPOSE 5006

CMD bokeh serve --allow-websocket-origin=localhost:80 /app/bokehapp/map.py