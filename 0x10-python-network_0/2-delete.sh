#!/bin/bash
# This sends a delete request to the URL passed as the first argument and displays the body of the response
curl -sX DELETE "$1"
