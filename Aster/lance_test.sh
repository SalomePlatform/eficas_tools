unalias do
for file in `ls /local/noyret/Install_Eficas/lescomm/*`
do
	filepath=$file
	grep "VISU_EFICAS='NON'" $filepath > /dev/null 2>/dev/null
	rc=$?
	if [ "$rc" != "0" ]
	then
	    grep INCLUDE $filepath | grep -v "#" | grep -v INCLUDE_MATERIAU > /dev/null 2>/dev/null
	    rc=$?
	    if  [ "$rc" != "0" ]
	    then
                echo $file
 	    	./test_eficas.py $filepath 
	    fi
	fi
#        read a; if [ "$a" == "b" ]  
#	then  
#	   exit  
#	fi 
done
