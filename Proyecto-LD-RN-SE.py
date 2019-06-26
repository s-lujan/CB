import numpy as np

import skfuzzy as fuzz

from skfuzzy import control as ctrl

#import time

#Rango de valores

array_dia = np.arange(1,8,1)

array_carretera = np.arange (0,101,1)

array_mes = np.arange (1,13,1)

array_lluvia = np.arange(0,101,1)

array_velocidad = np.arange(0,81,1)



dia = ctrl.Antecedent (array_dia, 'dia')

carretera = ctrl.Antecedent (array_carretera, 'carretera')

mes = ctrl.Antecedent (array_mes, 'mes')

lluvia = ctrl.Antecedent (array_lluvia, 'lluvia')

velocidad = ctrl.Consequent (array_acc, 'velocidad')



dia['laboral'] = fuzz.trapmf(array_dia, [0,1,1.5,5])

dia['finde'] = fuzz.trapmf(array_dia, [2,5,6,7])



mes['invierno'] = fuzz.trapmf(array_mes, [0,1,1.5, 3])

mes ['primavera'] = fuzz.trapmf(array_mes, [2,3,4,6])

mes ['verano'] = fuzz.trapmf(array_mes, [4,6,7,9])

mes ['otono'] = fuzz.trapmf(array_mes, [6,9,10, 12])



carretera ['mal'] = fuzz.trapmf(array_carretera, [0,0,0.5, 33])

carretera ['normal'] = fuzz.trapmf(array_carretera, [1,30,34, 66])

carretera ['buena'] = fuzz.trapmf(array_carretera, [31,66,67,100])



lluvia ['no'] = fuzz.trapmf (array_lluvia, [0, 0, 0.5, 25] )

lluvia ['leve']= fuzz.trapmf (array_lluvia, [1, 20, 26, 50] )

lluvia  ['normal']= fuzz.trapmf (array_lluvia, [21, 50, 51, 75] )

lluvia ['fuerte']= fuzz.trapmf (array_lluvia, [51, 75, 76, 100] )



velocidad ['poca']= fuzz.trapmf (array_velocidad, [0, 0, 0.5, 20] )

velocidad ['leve'] = fuzz.trapmf (array_velocidad, [1, 15, 21, 40] )

velocidad ['moderada']= fuzz.trapmf (array_velocidad, [16, 30, 41, 60] )

velocidad ['rapida']= fuzz.trapmf (array_velocidad, [31, 60, 61, 80] )







rule1 = ctrl.Rule(mes['invierno'] or carretera['mal'] or lluvia['fuerte'], velocidad['poca'])

rule2 = ctrl.Rule((mes['verano'] & carretera['buena']) & dia['finde'], velocidad['rapida'] )

rule3 = ctrl.Rule((mes['primavera'] & carretera['buena']) & dia['laboral'], velocidad['moderada'] )

rule4 = ctrl.Rule((mes['verano'] & carretera['buena']) & dia['laboral'], velocidad['moderada'] )

rule5 = ctrl.Rule((mes['otono'] & carretera['normal'] ) & dia['finde'], velocidad['moderada'])

rule6 = ctrl.Rule((mes['otono'] & carretera['normal']) & dia['laboral'], velocidad['moderada'] )

rule7 = ctrl.Rule((mes['otono'] & carretera['normal']) & dia['laboral'], dia['leve'] )

rule8 = ctrl.Rule((mes['verano'] & carretera['buena'])| (mes['otono'] & carretera['normal'])| (mes['verano'] & carretera['normal'])| (mes['otono'] & carretera['buena']), lluvia['no'] )

rule9 = ctrl.Rule((mes['invierno'] or carretera['mal'] or mes['otono'] or carretera['normal'] or carretera['mal'] or mes['invierno']), velocidad['poca'])

rule10 = ctrl.Rule((mes['invierno'] | carretera['mal'] | carretera['mal'] | mes['invierno'])& (dia['laboral']), velocidad['poca'])

rule11 = ctrl.Rule((mes['invierno'] | carretera['mal'])& dia['laboral'], velocidad['moderada'])

rule12 = ctrl.Rule((mes['invierno'] | carretera['mal'])& dia['finde'], velocidad['poca'])

rule13 = ctrl.Rule((mes['otono'] | carretera['normal'] | carretera['mal'] | mes['invierno'])&(dia['laboral']), velocidad['poca'])

rule15 = ctrl.Rule((mes['otono'] | carretera['normal'])& (dia['finde']), velocidad['poca'])

rule18 = ctrl.Rule((mes['verano'] & carretera['buena'])| (mes['otono'] & carretera['normal'])| (mes['verano'] & carretera['normal'])| (mes['otono'] & carretera['buena']), velocidad['rapida'] )



velocidad_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule15, rule18])

prueba = ctrl.ControlSystemSimulation(velocidad_ctrl)



prueba.input['dia'] = 3

prueba.input['carretera'] = 9

prueba.input['mes'] = 2

prueba.input['lluvia'] = 80

prueba.compute()

print("La velocidad debe ser de: " + str(prueba.output['velocidad']))

'''

for i in range (0,121):

	for j in range (0,11):

		for y in range (0,11):

			prueba.input['dia'] = i

			prueba.input['Cercania estacion'] = j

			prueba.input['Cercania curva'] = y



			prueba.compute()

			print("La velocidad debe ser de: " + str(prueba.output['velocidad']) + "---- " + str (i)+ "---- " + str (j)+ "---- "+ str (y))

#lluvia.view(sim=prueba)

'''



#rule2.view()

#carretera['buena'].view()

#time.sleep(60)
