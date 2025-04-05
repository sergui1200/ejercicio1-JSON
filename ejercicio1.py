import json

data = json.load(open("datos.json"))
print(f"El señor {data["nombre"]}")
print(f"de edad {data["edad"]}")
print(f"con dni {data["Dni"]}")
print(f"es acusado de {len(data["Delitos"])} delitos,")
print(f"delitos provocados el {data["Tiempo_de_los_delitos"][0]["Dia2"]}, {data["Tiempo_de_los_delitos"][1]["Dia25"]}")
print(f",{data["Tiempo_de_los_delitos"][2]["Dia26"]} y el {data["Tiempo_de_los_delitos"][3]["Dia27"]}.")
print(f"Los delitos a mencionar seran los siguientes: {data["Delitos"][0]["Estafa"]}, {data["Delitos"][1]["Robo a mano armada"]}, {data["Delitos"][3]["Asesinato"]}")
print(f"ademas de los delitos ya mencionados anteriormente se le acusa de {data["Delitos"][2]["Allanamiento de morada"]}")
print(f"Los delitos dichos anteriormente tendran las siguientes consecuencias: ")
for consecuencia in data["Posibles_consecuencias"]:
    print(f"- {consecuencia}")
