dicoEnum = { 'Type_Of_Advection' : { '1' : "'characteristics'",        '2' : "'SUPG'", '3' : "'Conservative N-scheme'" ,\
                                     '4' : "'Conservative N-scheme'" , '5' : "'Conservative PSI-scheme'" ,    \
                                     '6' : "'Non conservative PSI scheme'" , '7' : "'Implicit non conservative N scheme'" ,\
                                     '13': "' Edge-based N-scheme'", '14': "'Edge-based N-scheme'"},
             'Solver' :{ '1': "'conjugate gradient'", '2': "'conjugate residual'", '3': "'conjugate gradient on a normal equation'",\
                         '4': "'minimum error'", '5' :"'conjugate gradient squared (not implemented)'",\
                         '6': "'cgstab'", '7': "'gmres'" , '8': "'direct'" } ,
             'Discretisations_In_Space' : {  "11;11":"linear for velocity and depth", \
                 "12;11" : "quasi-bubble-velocity and linear depth", \
                 "13;11 ": "quadratic velocity and linear depth" },
            }
