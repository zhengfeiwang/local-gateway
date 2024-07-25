FROM python:3.12-slim

COPY start.sh /start.sh

RUN pip install promptflow==1.13.0 \
    && chmod +x /start.sh

CMD ["/start.sh"]
