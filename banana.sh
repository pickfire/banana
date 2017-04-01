#!/bin/sh
# Simple hosts file client

run=1
tld='zkey'

hosts() grep -v '^#' hosts
ret() echo ${cmd%E}ED $id $*

echo INIT 1 0
trap run=0 TERM

while [ $run -eq 1 ]
do
	read cmd id name
	# TODO: Timeout exceeded
	case $cmd in
		RESOLVE)
			[ ${name#*.} = $tld ] || { ret '2 "'$tld' not recognized tld"'; continue; }
			addr=$(hosts | awk "/\<$name\>/ { print \$1; exit }")

			[ -n "$addr" ] && ret "0 $addr" || ret '3 "'$name' not registered"'
			;;
	esac
done
