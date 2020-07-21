FROM node:12-slim

EXPOSE 8080

RUN npm i npm@latest -g

RUN mkdir /opt/node_app && chown node:node /opt/node_app
WORKDIR /opt/node_app

RUN npm install --no-optional \
&& npm install -g http-server \
&& npm install -g sass \
&& npm cache clean --force

HEALTHCHECK --interval=30s CMD node healthcheck.js

WORKDIR /opt/node_app/app
COPY . .

RUN ["sass ./CSS basics/variables.scss:./CSS basics/variables.css"]

CMD [ "node", "./bin/www", "http-server" ]
