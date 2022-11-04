#!/bin/bash
if [ $# = 2 ] ; then
	gaptext=`cat $2`;
	cat $1 | grep -iEo "${gaptext//_/"\w+"}"
else
	echo "Syntax: ./alice.sh stoerung lueckentext"
fi
