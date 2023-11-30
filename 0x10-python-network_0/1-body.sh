#!/bin/bash
# This takes a URL,sends a GET request to the URL,then displays body of the response
curl -Lsf "$1"
