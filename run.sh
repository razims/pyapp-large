#!/usr/bin/env bash

echo "Generating big_file 850M"
mkfile -n 850M big_file

echo "Pushing"
xs push