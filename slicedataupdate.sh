#!/bin/bash
svn up;

for size in 10 100 1000 10000;
do
    rsync -Ccavq -e ssh gpcu.dyndns.org:/home/pricegd/ddrevslice_$size/ raw_data/ddrevslice_$size/ 
    svn add raw_data/ddrevslice_$size/*$size 2>/dev/null;

    output="#Benchmark,Intersect,ITE"
    for j in raw_data/ddrevslice_$size/*$size.dat;
    do 
	bm="4"`echo $j | cut -f"2-" -d"4" | cut -f"-2" -d"_";`
	num=`echo $bm | cut -c"-3"`;
	name=`echo $bm | cut -f"-1" -d"_" | cut -c"4-"`;
	test=`echo $bm | cut -f"2-" -d"_"`;
	bm="$num.$name.$test"
	
	output="$output $bm"

	for slice in "Intersect Slice" "ITE Slice"
	do
	    sum=0;
	    count=0;
	    for i in `cat $j | grep "$slice" | cut -f3 -d","`;
	    do 
		sum=`echo $sum+$i | bc -q 2>/dev/null`;
		let count+=1;
	    done;
	    ave=`echo "scale=10;$sum/$count" | bc -q 2>/dev/null`;
	    if [ -n "$ave" ]
	    then
		output="$output,$ave"
	    else
		output="$output,0"
	    fi
	done;
    done;

    rm data/slice$size.dat 2>/dev/null;
    for line in $output;
    do
	echo $line >> data/slice$size.dat;
    done;
    svn add data/slice$size.dat 2>/dev/null;
done;
svn commit -m"Automated data translation and addition";