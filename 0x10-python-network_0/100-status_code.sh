#!/bin/bash
# Sents a POST request
curl -l -o -I -s -w "%{http_code}" $1
