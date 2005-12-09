#unalias do
#set -x
version=NEW82
passe=2
rm -rf ./Batch/${version}/ok_${passe}
rm -rf ./Batch/${version}/bad_${passe} 
rm -rf ./Batch/${version}/badfile_${passe}
rm -rf ./Batch/${version}/nt_${passe}
for file in `cat ./Batch/${version}/aTester`
do
        #echo $file
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
		  echo $file >> ./Batch/${version}/bad_${passe}
		else
		  nomfeuille=`basename $file`
		  boncr="DEBUT CR validation : "${nomfeuille}" FIN CR validation :"${nomfeuille}
		  cr=`echo $cr`
		  if [ "${cr}" != "$boncr" ]
		  then
			echo $file >> ./Batch/${version}/bad_${passe}
			echo $cr >>./Batch/${version}/bad_${passe}
			echo $file >>./Batch/${version}/badfile_${passe}
		  else
			echo $file >> ./Batch/${version}/ok_${passe}
		  fi
		fi
	    else
	      echo $file >> ./Batch/${version}/nt_${passe}
	    fi
	else
	   echo $file >> ./Batch/${version}/nt_${passe}
	fi 
done
