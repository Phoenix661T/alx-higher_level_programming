#!/bin/bash
# Sents a DELETE request
curl -sI $1 | grep Allow | cut -b 8-
