FROM python:3.11-alpine
LABEL maintainer="antonin.le-meur@supdevinci-edu.fr"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["src/app.py"]
