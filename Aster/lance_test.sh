#unalias do
#set -x
version=V8
passe=1
rm -rf ./Tests_Batch/${version}/ok_${passe}
rm -rf ./Tests_Batch/${version}/bad_${passe}
rm -rf ./Tests_Batch/${version}/nt_${passe}
for file in `cat ./Tests_Batch/${version}/aTester`
do
        echo $file
	grep "VISU_EFICAS='NON'" $file > /dev/null 2>/dev/null
	rc=$?
	if [ "$rc" != "0" ]
	then
	    grep INCLUDE $file | grep -v "#" | grep -v INCLUDE_MATERIAU > /dev/null 2>/dev/null
	    rc=$?
	    if  [ "$rc" != "0" ]
	    then
 	    	cr=`./test_eficas.py $file` 
		if [ "${cr}" == "" ]
		then
		  echo $file >> ./Tests_Batch/${version}/bad_${passe}
		else
		  nomfeuille=`basename $file`
		  boncr="DEBUT CR validation : "${nomfeuille}" FIN CR validation :"${nomfeuille}
		  cr=`echo $cr`
		  if [ "${cr}" != "$boncr" ]
		  then
			echo $file >> ./Tests_Batch/${version}/bad_${passe}
		  else
			echo $file >> ./Tests_Batch/${version}/ok_${passe}
		  fi
		fi
	    else
	      echo $file >> ./Tests_Batch/${version}/nt_${passe}
	    fi
	else
	   echo $file >> ./Tests_Batch/${version}/nt_${passe}
	fi 
done
