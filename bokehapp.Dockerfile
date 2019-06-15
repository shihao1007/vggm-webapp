FROM continuumio/miniconda3

RUN conda install -y bokeh numpy pandas nltk

VOLUME '/app'

EXPOSE 5006

#ENTRYPOINT ["bokeh", "serve", "/app/bokehapp/map.py", "--allow-websocket-origin=3.16.213.22:5006", "--address=0.0.0.0"]

CMD bokeh serve --address=0.0.0.0 /app/bokehapp/map.py 
