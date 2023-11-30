#!/bin/bash
# This gets the comtent-lenght of a given ip address
curl -sI "$1" | awk '/Content-Length/{print $2}'
