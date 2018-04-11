import raw.atmo2 as mdm

my_Wind_Speed=mdm.T_Wind_Speed(0)
my_Value=mdm.T_Value(0)
my_Unit=mdm.T_Unit(0)
my_Mesure=mdm.T_Mesure(my_Value,my_Unit)
# my_B_enter_mesure=mdm.T_B_enter_mesure(my_Wind_Speed,my_Mesure)

my_Wind_Speed1=mdm.T_Wind_Speed1(1)
my_Value1=mdm.T_Value1(1)
my_Unit1=mdm.T_Unit1(1)
my_Mesure1=mdm.T_Mesure1(my_Value1,my_Unit1)

# my_Wind=mdm.T_Wind(my_Wind_Speed1,my_Mesure1)
# my_Wind.append(my_Wind_Speed)
# my_Wind.append(my_Mesure)
# ou
# my_Wind.extend([my_Wind_Speed,my_Mesure])
# ou
my_Wind=mdm.T_Wind(my_Wind_Speed1,my_Mesure1,my_Wind_Speed,my_Mesure)


my_Atmos=mdm.Atmos(my_Wind)
xmls=my_Atmos.toxml()
xmls=my_Atmos.toDOM().toprettyxml()

open('modele_atmo_test2.xml', 'w').write(xmls)
