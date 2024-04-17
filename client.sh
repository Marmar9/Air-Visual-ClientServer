#!/bin/bash
regex='^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}Z$'
source .env

if [ "$1" == "push" ]; then
     
    body=$(curl "http://api.airvisual.com/v2/city?country=Poland&state=Mazovia&city=Warsaw&key=$APIKEY")
     
    curl --silent -X POST -H "Content-Type: application/json" -d "$body" "http://$HOST:$PORT/data" > /dev/null

    echo "Data in app updated"

elif [ "$1" == "pull" ]; then
    if [[ "$2" =~ $regex ]]; then
        curl --silent -X GET "http://$HOST:$PORT/data?date=$2" | jq
    else
        echo 'Provide date after 'pull' in format: "YYYY-MM-DDTHH:MM:SS.sssZ"'
    fi
else
    echo "Invalid argument. Please provide 'push' or 'pull'."
fi

