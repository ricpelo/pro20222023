import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')
raiz = arbol.getroot()
socio = raiz.find('./socios/socio[@id="51"]')
padre = raiz.find('socios')
padre.remove(socio)
arbol.write('club.xml', encoding='UTF-8', xml_declaration=True)
