#!/bin/bash
# Sents a POST request with a JSON file
curl -s -H "Content-Type: application/json" -X POST -d @$2 $1
