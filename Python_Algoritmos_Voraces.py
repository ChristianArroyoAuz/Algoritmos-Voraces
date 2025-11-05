from IPython.display import clear_output
import matplotlib.pyplot as plt
from colorama import Fore
import pandas as pd
from math import pi
import sys

def base():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t ALGRITMOS VORACES \t\t\t')
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Calendarización.')
    print('\t 2. Ingrese "2" para Cobertura de Habilidades.')
    print('\t 3. Ingrese "0" para Salir.')
    opcion_voraz = input("\t  " + "¿Cual es tu opción?: ")
    if opcion_voraz.isdigit() & len(opcion_voraz) != 0:
        clear_output(wait=True)
        tipo_seleccion(int(opcion_voraz))
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        base()

def calendario():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t CALENDARIACIÓN USANDO ALGORITMOS VORACES \t\t\t' + Fore.BLACK)
    print("                                   ")
    print(Fore.GREEN + "\t\t\t CALENDARIO A SER ANALIZADO \t\t\t" + Fore.BLACK)
    fig, gnt = plt.subplots()
    gnt.set_ylim(11, 0)
    gnt.set_xlim(0, 14)
    gnt.set_xlabel("Tiempos")
    gnt.set_ylabel("Materias")
    gnt.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    gnt.set_yticklabels(["1", "2", "3","4", "5", "6", "7", "8", "9", "10", "11"])
    gnt.grid(True)
    gnt.broken_barh([(1, 3)], (0, 1), facecolors = ("tab:olive"))
    gnt.broken_barh([(3, 2)], (1, 1), facecolors = ("tab:red"))
    gnt.broken_barh([(0, 6)], (2, 1), facecolors = ("tab:cyan"))
    gnt.broken_barh([(5, 2)], (3, 1), facecolors = ("tab:pink"))
    gnt.broken_barh([(3, 5)], (4, 1), facecolors = ("tab:blue"))
    gnt.broken_barh([(5, 4)], (5, 1), facecolors = ("tab:gray"))
    gnt.broken_barh([(6, 4)], (6, 1), facecolors = ("tab:cyan"))
    gnt.broken_barh([(8, 3)], (7, 1), facecolors = ("tab:purple"))
    gnt.broken_barh([(8, 4)], (8, 1), facecolors = ("tab:red"))
    gnt.broken_barh([(2, 11)], (9, 1), facecolors = ("tab:olive"))
    gnt.broken_barh([(12, 2)], (10, 1), facecolors = ("tab:blue"))
    plt.show()
    print("                                                                                       ")
    print(Fore.GREEN + "\t\t\t RESULTADOS DESPUES DE APLICAR EL ALGORITMO GREEDY \t\t\t" + Fore.BLACK)
    intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    intervals.sort(key = lambda x: x[1])
    count = 0
    end = 0
    answer = []
    for interval in intervals:
        if(end <= interval[0]):
            end = interval[1]
            count += 1
            answer.append(interval)
    print(Fore.GREEN + "Número máximo de materias que se puede tomar: " + str(count)  + Fore.BLACK)
    print(Fore.GREEN + "Los horarios de materias son: " + str(answer) + Fore.BLACK)
    print("                                                                                       ")
    x = -1
    fig, gnt = plt.subplots()
    gnt.set_ylim(4, 0)
    gnt.set_xlim(0, 14)
    gnt.set_xlabel("Tiempos")
    gnt.set_ylabel("Materias")
    gnt.set_yticks([1, 2, 3, 4])
    gnt.set_yticklabels(["1", "2", "3","4"])
    gnt.grid(True)
    for var in answer:
        x = x + 1
        gnt.broken_barh([(var[0], var[1] - var[0])], (x, 1), facecolors =('tab:olive'))
    plt.show()
    salir()

def habilidades():
    print("                                                                                       ")
    print(Fore.BLUE + '\t\t\t COVERTURA DE HABILIDADES \t\t\t' + Fore.BLACK)
    print("                                   ")
    print(Fore.GREEN + '\t\t\t JUGADORES A SER ANALIZADOS \t\t\t' + Fore.BLACK)
    print("                                   ")
    df = pd.DataFrame({
    'jugadores'   : ['0',  '1',  '2',  '3',  '4',  '5',  '6',  '7',  '8',  '9'],
    'Aceleracion' : [ 50,   50,   50,    0,    0,    0,   50,    0,    0,  50],
    'Agilidad'    : [ 50,    0,    0,    0,   50,    0,    0,    0,   50,   0],
    'Fuerza'      : [  0,    0,    0,   50,    0,   50,    0,    0,    0,   0],
    'Inteligencia': [  0,   50,    0,    0,    0,    0,    0,   50,    0,   0],
    'Presicion'   : [ 50,    0,   50,    0,    0,   50,    0,   50,    0,   0],
    'Reaccion'    : [  0,   50,    0,    0,   50,    0,    0,    0,   50,   0],
    'Resistencia' : [ 50,    0,   50,   50,    0,    0,    0,    0,    0,   0],
    'Sprint'      : [  0,   50,    0,    0,   50,    0,    0,    0,    0,   0],
    'Velocidad'   : [  0,    0,    0,   50,    0,   50,   50,    0,    0,   0],
    'Vitalidad'   : [  0,    0,    0,    0,    0,    0,    0,    0,    0,  50]
    })
    categories=list(df)[1:]
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(90)
    plt.yticks([0, 10, 20, 30, 40, 50], ["0", "10", "20", "30", "40", "50"], color = "black", size = 10)
    plt.ylim(0, 50)
    for x in range(0, 10):
        values=df.loc[x].drop('jugadores').values.flatten().tolist()
        values += values[:1]
        ax.fill(angles, values, "blue", alpha = 0.1)
        ax.plot(angles, values, linewidth=1, linestyle='solid', label = "Jugador " + str(x))
        plt.legend(loc = 'upper right', bbox_to_anchor = (0, 0))
    plt.show()
    habilidades_necesarias = set(["Aceleracion", "Agilidad", "Fuerza", "Inteligencia", "Presicion",  "Reaccion", "Resistencia", 
                                  "Sprint", "Velocidad", "Vitalidad"])
    jugadores_disponibles = {}
    jugadores_disponibles["Jugador_0"] = set(["Aceleracion", "Agilidad", "Presicion", "Resistencia"])
    jugadores_disponibles["Jugador_1"] = set(["Agilidad", "Inteligencia", "Reaccion", "Sprint"])
    jugadores_disponibles["Jugador_2"] = set(["Aceleracion", "Presicion", "Resistencia"])
    jugadores_disponibles["Jugador_3"] = set(["Fuerza", "Resistencia", "Velocidad"])
    jugadores_disponibles["Jugador_4"] = set(["Agilidad", "Reaccion", "Sprint"])
    jugadores_disponibles["Jugador_5"] = set(["Fuerza", "Presicion", "Velocidad"])
    jugadores_disponibles["Jugador_6"] = set(["Aceleracion", "Velocidad"])
    jugadores_disponibles["Jugador_7"] = set(["Inteligencia", "Presicion"])
    jugadores_disponibles["Jugador_8"] = set(["Agilidad", "Reaccion"])
    jugadores_disponibles["Jugador_9"] = set(["Aceleracion", "Vitalidad"])
    jugadores_seleccionados = set()
    print("Habilidades Necesarias: " + str(habilidades_necesarias))
    print("                                                                                       ")
    print(Fore.GREEN + "\t\t\t RESULTADOS DESPUES DE APLICAR EL ALGORITMO GREEDY \t\t\t" + Fore.BLACK)
    print("Jugadores que cubre las habilidades necesarias")
    while habilidades_necesarias:
        mejores_jugadores= None
        jugadores_revisados = set()
        for jugador, habilidades in jugadores_disponibles.items():
            jugador_revisado = habilidades_necesarias & habilidades
            if len(jugador_revisado) > len(jugadores_revisados):
                mejores_jugadores = jugador
                jugadores_revisados = jugador_revisado
        print("\t Jugador escogido: " + str(mejores_jugadores) + ". Con un número de habilidades de: " + str(len(jugadores_revisados)))
        print("\t\t Sus Habilidades son: " + str(jugadores_revisados))
        habilidades_necesarias -= jugadores_revisados
        jugadores_seleccionados.add(mejores_jugadores)
    print("Lista de jugadores escogidos: " + str(jugadores_seleccionados))
    df = pd.DataFrame({
    'jugadores'   : ['0',  '1',  '2',  '3',  '4',  '5',  '6',  '7',  '8',  '9'],
    'Aceleracion' : [ 50,   50,   50,    0,    0,    0,   50,    0,    0,  50],
    'Agilidad'    : [ 50,    0,    0,    0,   50,    0,    0,    0,   50,   0],
    'Fuerza'      : [  0,    0,    0,   50,    0,   50,    0,    0,    0,   0],
    'Inteligencia': [  0,   50,    0,    0,    0,    0,    0,   50,    0,   0],
    'Presicion'   : [ 50,    0,   50,    0,    0,   50,    0,   50,    0,   0],
    'Reaccion'    : [  0,   50,    0,    0,   50,    0,    0,    0,   50,   0],
    'Resistencia' : [ 50,    0,   50,   50,    0,    0,    0,    0,    0,   0],
    'Sprint'      : [  0,   50,    0,    0,   50,    0,    0,    0,    0,   0],
    'Velocidad'   : [  0,    0,    0,   50,    0,   50,   50,    0,    0,   0],
    'Vitalidad'   : [  0,    0,    0,    0,    0,    0,    0,    0,    0,  50]
    })
    categories=list(df)[1:]
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(90)
    plt.yticks([0, 10, 20, 30, 40, 50], ["0", "10", "20", "30", "40", "50"], color = "black", size = 10)
    plt.ylim(0, 50)
    values=df.loc[0].drop('jugadores').values.flatten().tolist()
    values += values[:1]
    ax.fill(angles, values, "blue", alpha = 0.1)
    ax.plot(angles, values, linewidth=1, linestyle='solid', label = "Jugador " + str(0))
    plt.legend(loc = 'upper right', bbox_to_anchor = (0, 0))
    values=df.loc[1].drop('jugadores').values.flatten().tolist()
    values += values[:1]
    ax.fill(angles, values, "red", alpha = 0.1)
    ax.plot(angles, values, linewidth=1, linestyle='solid', label = "Jugador " + str(1))
    plt.legend(loc = 'upper right', bbox_to_anchor = (0, 0))
    values=df.loc[3].drop('jugadores').values.flatten().tolist()
    values += values[:1]
    ax.fill(angles, values, "green", alpha = 0.1)
    ax.plot(angles, values, linewidth=1, linestyle='solid', label = "Jugador " + str(3))
    plt.legend(loc = 'upper right', bbox_to_anchor = (0, 0))
    values=df.loc[9].drop('jugadores').values.flatten().tolist()
    values += values[:1]
    ax.fill(angles, values, "purple", alpha = 0.1)
    ax.plot(angles, values, linewidth=1, linestyle='solid', label = "Jugador " + str(9))
    plt.legend(loc = 'upper right', bbox_to_anchor = (0, 0))
    plt.show()
    salir()
    
def default_1():
    clear_output(wait = True)
    print(Fore.RED + "                                                                    ")
    print(Fore.RED + "\t  Opción Erronea - Ingrese una de las opciones establecidas.  \t\n")
    base()

def tipo_seleccion(numero_0):
    return opciones_calendario_habilidades.get(numero_0, default_1)()

def salir():
    print("                                                     ")
    print(Fore.BLUE + '\t\t\t ADIÓS HASTA LA PRÓXIMA \t\t\t' + Fore.BLACK)
    sys.exit()

opciones_calendario_habilidades = {
    1: calendario,
    2: habilidades,
    0: salir
    }

base()