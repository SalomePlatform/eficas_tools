unalias do
for file in `ls /local/noyret/Install_Eficas/lescomm/z*`
do
        echo $file
	filepath=$file
	#filepath=/local/noyret/Install_Eficas/lescomm/$file
	grep "VISU_EFICAS='NON'" $filepath > /dev/null 2>/dev/null
	rc=$?
	if [ "$rc" != "0" ]
	then
	    grep INCLUDE $filepath | grep -v "#" | grep -v INCLUDE_MATERIAU > /dev/null 2>/dev/null
	    rc=$?
	    if  [ "$rc" != "0" ]
	    then
 	    	./test_eficas.py $filepath  | grep -v mx.TextTools | grep -v Aster | grep -v relire| grep -v mxExtensions | grep -v DEBUT | grep -v FIN 
	    fi
	fi
#        read a; if [ "$a" == "b" ]  
#	then  
#	   exit  
#	fi 
done
