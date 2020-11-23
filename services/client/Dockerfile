# base image
FROM node:11.12.0-alpine

# estableciendo una carpeta de trabajo
WORKDIR /usr/src/app

# agregando `/usr/src/app/node_modules/.bin` a $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# instalando dependencias y app caché 
COPY package.json /usr/src/app/package.json
COPY package-lock.json /usr/src/app/package-lock.json
RUN npm ci
RUN npm install react-scripts@2.1.8 -g --silent

# iniciando app
CMD ["npm", "start"]
