#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -sL -H "X-HolbertonSchool-User-Id: 98" "$1"
