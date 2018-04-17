#!/usr/bin/env bash
# Makes python output more acme friendly

python $@ 3>&1 1>&2 2>&3 3>&- | sed -e 's/", line /:/g'
