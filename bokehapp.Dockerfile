FROM continuumio/miniconda3

RUN conda install -y bokeh numpy pandas nltk

VOLUME '/app'

EXPOSE 5006

#ENTRYPOINT ["bokeh", "serve", "/app/bokehapp/map.py", "--allow-websocket-origin=18.222.239.0:5006", "--address=0.0.0.0"]

#CMD bokeh serve --allow-websocket-origin=3.16.26.212:80 --allow-websocket-origin=127.0.0.1:5000 --allow-websocket-origin=0.0.0.0:5000 --allow-websocket-origin=0.0.0.0:80 /app/bokehapp/map.py

CMD bokeh serve /app/bokehapp/map.py