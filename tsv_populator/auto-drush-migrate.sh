#!/bin/bash
declare -A ali_title

#for line in $(cat 'alias-names'); do
while read -r ali title;do
  echo $ali ' => ' $title
  ali_title+=( [$ali]=$title )
done < alias-names

echo $ali_title

namespace=''
alias=''
title='' 
for line in $(cat input);do
#always strip off last 8 characters, ie -cpd.zip or -jp2.zip
  namespace=$(echo "${line:0:${#line}-8}")
  alias=$(echo ${namespace} | sed 's/^[^-]*//' | sed 's/\-//')
  echo 'alias=' ${alias}
  echo 'namespace=' ${namespace}
  echo 'drush --user=admin cicfc --input=/vagrant/'"$namespace"'.tsv  --namespace='"$namespace"':collection --parent=islandora:root' >> drush-coll-migrate
  echo "${aliastitle[$alias]}"
  echo -e $namespace "\t"  "${ali_title[$alias]}" "\t"  > ${namespace}.tsv
done;


