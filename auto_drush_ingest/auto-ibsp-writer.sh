#!/bin/bash
declare -A cmodels
cmodels=( ['pdf']='sp_pdf' ['jp2']='sp_large_image_cmodel' ['mp4']='sp_videoCModel' ['mp3']='sp-audoCmodel')
#echo "${!cmodels[@]}"
#echo "${cmodels[@]}"
namespace=''
name_ext=''
ext=''

for line in $(cat input);do
	if [[ ${line} =~ .*cpd.* ]]; then
		namespace=$(echo ${line} |  sed 's/-cpd\.[^.]*$//' )
		echo 'drush -u 1 icbp --target=/tmp/'"$namespace"'-cpd --namespace='"$namespace"' --parent='"$namespace"':collection' >> drush-commands
	fi
	if [[ ${line} != *cpd* ]]; then
		namespace=$(echo ${line} |  sed 's/\.[^.]*$//' )
		name_ext=$(echo "${line:0:${#line}-4}")
		ext=${name_ext: -3}
                echo 'drush -u 1 ibsp --type=zip --scan_target=/tmp/'"$line"' --content_model='"${cmodels[$ext]}"' -namespace='"$namespace"' --parent='"$namespace"':collection' >> drush-commands
        fi

done;
