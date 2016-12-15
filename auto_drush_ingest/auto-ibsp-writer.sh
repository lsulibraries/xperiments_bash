#!/bin/bash
declare -A cmodels
cmodels=( ['pdf']='sp_pdf' ['jp2']='sp_large_image_cmodel' ['mp4']='sp_videoCModel' ['mp3']='sp-audoCmodel')
echo "${!cmodels[@]}"
echo "${cmodels[@]}"

for line in $(cat input);do
	echo $line
done;
