#!/bin/bash
source .env

hypercorn src/main:app --bind "$HOST":"$PORT" --quic-bind localhost:4433 --reload
