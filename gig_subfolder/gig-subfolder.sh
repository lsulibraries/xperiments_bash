#!/bin/bash
SIZE=999999999
for OUTPUT in $(ls *.zip );do
	if [[ $(stat -c '%s' "${OUTPUT}") > $SIZE ]]; then
		if [[ ${OUTPUT} != *cpd* ]]; then
			$(mkdir $(echo ${OUTPUT} | sed 's/\.[^.]*$//' ))
			$(mv ${OUTPUT} $(echo ${OUTPUT} |  sed 's/\.[^.]*$//' ))
		fi
	fi
done
