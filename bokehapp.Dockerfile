FROM continuumio/miniconda3

RUN conda install -y bokeh numpy pandas nltk

VOLUME '/app'

EXPOSE 5006

ENTRYPOINT ["bokeh", "serve", "/app/bokehapp/map.py", "--allow-websocket-origin=127.0.0.1:5000", "--allow-websocket-origin=0.0.0.1:5000", "--allow-websocket-origin=localhost:5006"]