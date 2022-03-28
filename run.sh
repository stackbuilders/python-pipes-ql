#!/bin/sh
# Helper to watch the changes and run the code
ls $@ | entr -cr python $@
