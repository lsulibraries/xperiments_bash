
This branch assumes you need to test for existing collections on the production server.

change to a local-test branch to ignore checking for preexisting collections
######


move your zipfiles to a directory. I like /tmp/python (which i just made up with mkdir)
####

from this directory `ls /tmp/python >> input`
writes a list your sipfiles to the input file, which is used to feed arguments to the script.

`python3 auto_drush_migrate.py`

check the contents of migrate_coll file
