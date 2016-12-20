#!/bin/bash

for OUTPUT in  $(ls *.zip);
do
	if [[ ${OUTPUT} =~ .*cpd.* ]]; then
		$(mkdir $(echo ${OUTPUT} | sed 's/\.[^.]*$//' ))
		$(mv ${OUTPUT} $(echo ${OUTPUT} |  sed 's/\.[^.]*$//' ))
	fi

done
