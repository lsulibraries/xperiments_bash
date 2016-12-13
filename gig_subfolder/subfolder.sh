#!/bin/bash
SIZE=4000
for OUTPUT in $(ls *.zip );do 
#	echo ${OUTPUT}
	if [ $(stat -c '%s' "${OUTPUT}") > $SIZE ]; then
		if [[ ${OUTPUT} != *cpd* ]]; then
#			$(echo ${OUTPUT})
			$(mkdir $(echo ${OUTPUT} | sed 's/\.[^.]*$//' ))
			$(mv ${OUTPUT} $(echo ${OUTPUT} |  sed 's/\.[^.]*$//' ))
		fi
	fi
done
