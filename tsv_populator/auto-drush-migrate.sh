#!/bin/bash
declare -A aliastitle=( ['p15140coll31']='Judge John Minor Wisdom Collection' ['p16313coll86']='Ex Parte Plessy (Plessy v. Ferguson)' ['p120701coll13']='Louisiana Hurricane Resources' ['p16313coll72']='Orleans Parish School Board Meeting Minutes -- Indexes' ['p15140coll42']='Marcus Christian Collection' ['p15140coll51']='Veterans of Southeast Louisiana')
namespace=''
alias=''
title='' 
#best way to associate alias with title?
#for <alias> in xml; key:value  alias:title
for line in $(cat input);do
#always strip off last 8 characters, ie -cpd.zip or -jp2.zip
  namespace=$(echo "${line:0:${#line}-8}")
  alias=$(echo ${namespace} | sed 's/^[^-]*//' | sed 's/\-//')
  echo 'alias=' ${alias}
  echo 'namespace=' ${namespace}
  echo 'drush --user=admin cicfc --input=/vagrant/'"$namespace"'.tsv  --namespace='"$namespace"' --parent=islandora:root' >> drush-coll-migrate
  echo "${aliastitle[$alias]}"
  echo -e $namespace "\t"  "${aliastitle[$alias]}" "\t"  > ${namespace}.tsv
done;


