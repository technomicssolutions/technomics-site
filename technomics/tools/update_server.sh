#!/bin/bash

cd $WORKSPACE

hg pull -u
python ./manage.py syncdb --migrate


