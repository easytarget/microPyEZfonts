#!/bin/bash
#
# Insert the contents of file arg 1 as 'COMMENT' lines
# in the header of all .bdf files in current folder.
#
if [ $# -ne 1 ]; then
    echo "usage: $0 comment file"
    exit 1
fi

include=$1
if [ ! -f $include ]; then
    echo "$0: error: source file \"$include\" not found."
    exit 1
fi

comments=$1.temp
sed "s/^/COMMENT /" $include > $comments

for file in `ls *.bdf`; do
    ls -l $file
    head --lines 1 $file > $file.tmp
    cat $comments >> $file.tmp
    tail --lines +2 $file >> $file.tmp
    mv $file.tmp $file
done

rm $comments
