#!/bin/bash
#
# Generate a set of .bdf files from a source .ttf or .otf file
#
if [ $# -ne 1 ]; then
    echo "usage: $0 source_file.(ttf|otf)"
    exit 1
fi

cmd="otf2bdf"
if ! hash $cmd ; then
    echo "$0: error: font converter tool ($cmd) not found in path."
    exit 1
fi

input=$1
if [ ! -f $input ]; then
    echo "$0: error: source file \"$input\" not found."
    exit 1
fi

output=`basename -- "$input" ".${input##*.}"`
mkdir -p $output

sizes="6 7 8 9 10 11 12 14 16 18 20 24 28 32 36 42 48 56 64"

echo "Generating .bdf files for source '$input' to folder '$output' with the following px sizes: $sizes"

# Do the actual conversion..
for size in $sizes; do
    printf -v padsize "%02d" $size
    thiscommand="$cmd -p $size -o $output/$output-$padsize.bdf $input"
    echo "Running: $thiscommand"
    $thiscommand
done
