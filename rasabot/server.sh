#!/bin/sh

rasa run -m models --enable-api --cors "*"  --debug -vv -p 8080

