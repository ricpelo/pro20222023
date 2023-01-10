import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')
raiz = arbol.getroot()

for socio in raiz.findall('./socios/socio'):
    ident = socio.get('id')
    nombre = socio.find('nombre').text
    print(f'[{ident}] {nombre}')
