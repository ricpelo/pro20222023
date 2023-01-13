import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')
raiz = arbol.getroot()
lst = []
for socio in raiz.iter('socio'):
    nombre = socio.find('nombre').text
    alta = socio.find('alta').text
    lst.append((alta, nombre))
lst.sort()
for _, nombre in lst:
    print(nombre)
