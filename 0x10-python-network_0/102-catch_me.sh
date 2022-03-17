#!/bin/bash
# Sents a POST request with a JSON file
curl -s -X PUT -d user_id=98 -d '{"Allow: OPTIONS, PUT, GET, POST"}' 0.0.0.0:5000/catch_me -L -H "Origin: HolbertonSchool"
