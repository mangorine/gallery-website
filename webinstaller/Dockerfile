FROM node:17-alpine as node_base

RUN mkdir /app && chown node /app && chmod 700 /app \
    && mkdir /var/node_modules && chown node /var/node_modules \
    && mkdir /react && chown node /react && chmod 700 /react

WORKDIR /app

# ======================== DEV ENVIRONMENT =========================

FROM node_base as development

COPY install-frontend-dev.sh /usr/local/bin/
RUN sed -i 's/\r$//g' /usr/local/bin/install-frontend-dev.sh \
    && chmod +x /usr/local/bin/install-frontend-dev.sh
RUN npm config set unsafe-perm true

USER node

CMD ["/usr/local/bin/install-frontend-dev.sh"]

# ======================== PROD ENVIRONMENT ========================

FROM node_base as production

COPY ./react/src /app/src
COPY ./react/.babelrc ./react/package-lock.json ./react/package.json ./react/webpack.config.js ./react/tsconfig.json /app/
RUN chown node .babelrc package-lock.json package.json webpack.config.js tsconfig.json

COPY ./webinstaller/install-frontend-prod.sh /usr/local/bin/
RUN sed -i 's/\r$//g' /usr/local/bin/install-frontend-prod.sh \
    && chmod +x /usr/local/bin/install-frontend-prod.sh

USER node

CMD ["/usr/local/bin/install-frontend-prod.sh"]