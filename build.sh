#!/usr/bin/env bash

watchmedo shell-command --patterns="*.py" --recursive --command="inv build" .
