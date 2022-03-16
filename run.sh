#!/bin/sh
ls $@ | entr -cr python $@
