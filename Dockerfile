FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR ${APP_HOME}/site

ENV PORT 8080
EXPOSE 8080
CMD uvicorn main:app --host 0.0.0.0 --port 8080