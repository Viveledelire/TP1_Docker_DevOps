FROM python:3.11-alpine
LABEL maintainer="antonin.le-meur@supdevinci-edu.fr"
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["src/flask_app.py"]
