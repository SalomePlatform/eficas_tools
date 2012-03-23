#!/bin/sh
here=$(dirname $0)
EFICAS_ROOT=$here/../../..
export PYTHONPATH=$EFICAS_ROOT/Aster:$EFICAS_ROOT:$PYTHONPATH

python $here/usecase.py
