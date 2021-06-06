FROM rasa/rasa:latest

COPY app /app
COPY server.sh /app/server.sh

USER root
RUN pip3 install rasa[spacy]
RUN python -m spacy download es_core_news_md && python3 -m spacy validate
RUN chmod -R 777 /app
USER 1001

RUN rasa train nlu

ENTRYPOINT ["/app/server.sh"]
