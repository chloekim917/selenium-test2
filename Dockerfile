# FROM: 

FROM python:14
COPY . /app
WORKDIR /app
RUN npm install
EXPOSE 8080
CMD node ./app.js