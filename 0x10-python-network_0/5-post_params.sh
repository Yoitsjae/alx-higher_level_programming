#!/bin/bash
# A script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response . a variable email must be sent with the value hr@holbertonschool.com . a variable subject must be sent with the value I will always be here for PLD
 curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
