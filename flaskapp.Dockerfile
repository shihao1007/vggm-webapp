FROM continuumio/miniconda3

RUN conda install -y bokeh flask pandas nltk

VOLUME '/app'

EXPOSE 5000

ENTRYPOINT ["python", "/app/webapp/app.py"]
