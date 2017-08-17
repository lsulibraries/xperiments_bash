 #!/bin/bash
counter=1
p="p"
counterp=${counter}${p}
test='tulane record tulane:jrphil193050'
current=''
for line in $(cat tulane-orig-ns.txt);do
  bod=$(sed -n ${counterp} < tulane_collections.tsv)
  echo $bod | sed "s/$test/'tulane record $line'/" >>tmp.tsv
  counter=$((counter+1))
  counterp=${counter}${p}
done
counter=1
