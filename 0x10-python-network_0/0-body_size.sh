#!/bin/bash
# Display size of body response
curl -Is $1 | awk '/Content-Length: / {print $2}'
