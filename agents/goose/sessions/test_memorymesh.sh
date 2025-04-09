#!/bin/bash

echo "Testing connection to memorymesh server..."

REQUEST='{
  "jsonrpc": "2.0",
  "method": "add_npc",
  "params": {
    "npc": {
      "abilities": ["Musical Talent", "Combat Training"],
      "background": "Military veteran who became a rockerboy",
      "currentLocation": ["Night City"],
      "description": "Legendary anti-corporate revolutionary",
      "name": "Johnny Silverhand",
      "role": "Rockerboy",
      "status": "Digital Construct"
    }
  },
  "id": 1
}'

echo $REQUEST | node /home/skogix/.local/src/memorymesh/dist/index.js

echo "Test complete."
