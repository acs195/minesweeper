FROM python:3.7

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Copy app
ENV APP_DIR /app
RUN mkdir -p ${APP_DIR}
COPY . ${APP_DIR}/

# install dependencies
RUN python -m pip install --upgrade pip
RUN pip install -r ${APP_DIR}/requirements.txt

# Set environment
ENV APP_ENVIRONMENT development
ENV LOG_LEVEL INFO
ENV PORT 5000

# Run app
WORKDIR ${APP_DIR}/app
CMD exec gunicorn main:app \
    --log-level ${LOG_LEVEL} \
    --bind :${PORT} \
    --workers 1 \
    --timeout 120 \
    --graceful-timeout 120 \
    --keep-alive 5 \
    --error-logfile - \
    -k uvicorn.workers.UvicornWorker
