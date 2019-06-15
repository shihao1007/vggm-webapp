FROM continuumio/miniconda3

RUN conda install -y bokeh flask pandas nltk

VOLUME '/app'

EXPOSE 80

ENTRYPOINT ["python", "/app/webapp/app.py"]
