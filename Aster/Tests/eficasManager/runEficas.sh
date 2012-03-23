#!/bin/sh
# This run the test with the good environment (no previous extention is required)
# (gboulant - 23/03/2012)
here=$(dirname $0)
EFICAS_ROOT=$here/../../..
export PYTHONPATH=$EFICAS_ROOT/Aster:$EFICAS_ROOT:$PYTHONPATH
python $here/usecase.py
