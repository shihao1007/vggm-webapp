FROM continuumio/miniconda3

RUN conda install -y bokeh numpy pandas nltk

VOLUME '/app'

EXPOSE 5006

CMD bokeh serve --allow-websocket-origin=* /app/bokehapp/map.py