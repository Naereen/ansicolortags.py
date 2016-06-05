#!/bin/bash
#
# Author:   Lilian Besson
# Email:    lilian DOT besson AT ens-cachan D O T org
# Version:  1.3
# Date:     20/03/2013
#
# A simple script to automatize the generation of the zip archive to send to pythonhosted.org.
#

echo -e "${red}TODO : use twine${white}"
echo -e "twine upload dist/*"

if [ -f doc_ansicolortags.zip ]; then
    echo -e "The doc was already there, I'm moving it to /tmp/ ..."
    mv -fv doc_ansicolortags.zip /tmp/
fi

cd .build/html
zip -r -9 -T -v -u ../../doc_ansicolortags.zip ./
cd ../..

echo -e ""

echo -e "Now, go to ${u}https://pypi.python.org/pypi?:action=pkg_edit&name=ansicolortags${U}, and upload (manually) this file doc_ansicolortags.zip..."
