#!/bin/bash
declare -A cmodels
cmodels=( ['pdf']='sp_pdf' ['jp2']='sp_large_image_cmodel' ['mp4']='sp_videoCModel' ['mp3']='sp-audoCmodel')
#echo "${!cmodels[@]}"
#echo "${cmodels[@]}"
namespace=''
name_ext=''
ext=''

for line in $(cat zips);do
	if [[ ${line} =~ .*cpd.* ]]; then
		namespace=$(echo ${line} |  sed 's/-cpd\.[^.]*$//' )
		echo 'has cpd namespace:' ${namespace}
		echo 'drush -u 1 icbp --target=/tmp/'"$namespace"'-cpd --namespace='"$namespace"' --parent='"$namespace"':collection' >> drush-commands
	fi
	if [[ ${line} != *cpd* && ${line} == *.zip  ]]; then
		name_ext=$(echo ${line} |  sed 's/\.[^.]*$//' )
		namespace=$(echo "${name_ext:0:${#name_ext}-4}")
		echo 'simple collection, namespace:'
		echo  ${namespace}
		echo 'simple collection, name_ext'
		echo  ${name_ext}
		ext=${name_ext: -3}
		echo 'simple collection, extension'
		echo ${ext}
                echo 'drush -u 1 ibsp --type=zip --scan_target=/tmp/'"$line"' --content_models=islandora:'"${cmodels[$ext]}"' --namespace='"$namespace"' --parent='"$namespace"':collection' >> drush-commands
        fi
	if [[ ${line} != *.zip  ]]; then
		namespace=$(echo "${line:0:${#line}-4}")
		echo 'gig dir,  namespace:' ${namespace}
                ext=${line: -3}
                echo 'drush -u 1 ibsp --type=directory --scan_target=/tmp/'"$line"' --content_models=islandora:'"${cmodels[$ext]}"' --namespace='"$namespace"' --parent='"$namespace"':collection' >> drush-commands
	fi
done;
