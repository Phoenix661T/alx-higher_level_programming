#!/bin/bash
# Sents a POST request
curl -s $1 -X POST --data-urlencode email=test@gmail.com -d subject="I will always be here for PLD"
