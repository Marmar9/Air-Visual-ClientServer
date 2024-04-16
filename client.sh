#!/bin/bash
source .env

body=$(curl "http://api.airvisual.com/v2/city?country=Poland&state=Mazovia&city=Warsaw&key=$APIKEY")

echo "$body"

curl -X POST -H "Content-Type: application/json" -d "$body" "http://127.0.0.1:8000/data"
