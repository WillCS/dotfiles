#!/usr/bin/env bash

# Kill any running bars
killall -q polybar

echo "---" | tee -a /tmp/polybar.log
polybar bar 2>&1 | tee -a /tmp/polybar.log & disown

echo "Launched Polybar"

