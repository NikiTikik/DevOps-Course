#!/bin/bash

#Checking the number of arguments
if [[ "$#" -ne 2 ]]; then
	echo -ne "Illegal number of parameters!\nPlease enter names of two files!\n"
	exit
fi

#Calculating and output
res1=`cat $1 | bc`
res2=`cat $2 | bc`
echo "Result of the $1 is $res1"
echo "Result of the $2 is $res2"

#Definition of a large number
if [[ $res1 -gt $res2 ]]; then
	echo "$res1 is larger"
   else
	   echo "$res2 is larger"
fi
