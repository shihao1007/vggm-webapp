FROM continuumio/miniconda3

RUN conda install -y bokeh numpy pandas nltk

VOLUME '/app'

EXPOSE 5006

#ENTRYPOINT ["bokeh", "serve", "/app/bokehapp/map.py", "--allow-websocket-origin=18.222.239.0:5006", "--address=0.0.0.0"]

CMD bokeh serve --address=0.0.0.0 --port 5006 --allow-websocket-origin=* /app/bokehapp/map.py