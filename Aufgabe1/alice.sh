#!/bin/bash
gaptext=`cat $1`;
cat $2 | grep -iEo "${gaptext//_/"\w+"}"
