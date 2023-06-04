
FROM node:16-alpine 
WORKDIR /opt/app
COPY shipments_front /opt/app
# RUN npm ci 
RUN pwd
RUN npm install
RUN npm run build && npm install axios && npm install react-router-dom 

ENV NODE_ENV production
EXPOSE 3000
CMD [ "npm", "start" ]