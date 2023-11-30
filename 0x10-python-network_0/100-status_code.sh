#!/bin/bash
# Script sends a request to a URL passed as an argument displaying only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
