# Documentacio amb Markdown.
## XML:
L'XML es un **llenguatge de marques** estandard que utilitza etiquetes per representar informació. Els documents XML sempre tenen una etiqueta pare y altres etiquetes filles. L'objectiu principal del xml es aconseguir un document ben format que pugi ser llegit per ordinadors y persones. Aquestos documents requereixen una validesa, que es pot comprovar al navegador. L'xml es poden crear y editar en qualsevol editor de text.

Podem trobar mes informacio de XML en el seguent enllaç: 
***[W3Schools XML](https://www.w3schools.com/xml/xml_whatis.asp)***

Aqui tenem un exemple de un xml **ben format**.
```xml
<restaurante>
  <logo>
    <image enlace="https://static.vecteezy.com/system/resources/previews/010/383/996/non_2x/sushi-and-ramen-logo-template-vector.jpg">Logo</image>
  </logo>
  <carta>
    <platos>
      <plato>
        <nombre tipo="plato">Ramen de Cerdo y pollo</nombre>
        <tipo alergenos="Gluten">Ramen</tipo>
        <precios>
          <grande>12€</grande>
          <pequeño>8€</pequeño>
        </precios>
        <ingredientes>Cerdo, contramuslos de pollo, huevos marinados, cebolleta, tallarines chukasoba, cebolla, puerro, jengibre, ajo, kombu, sal.</ingredientes>
      </plato>
      <plato>
        <nombre tipo="plato">Ramen vegano</nombre>
        <tipo alergenos="Gluten">Ramen</tipo>
        <precios>
          <grande>11€</grande>
          <pequeño>7,5€</pequeño>
        </precios>
        <ingredientes>ajo, cebolla, jengibre, seta shiitake, miso, tallarines chukasoba, tofu</ingredientes>
      </plato>
      <plato>
        <nombre tipo="plato">Maki de salmón</nombre>
        <tipo alergenos="pescado">Sushi</tipo>
        <precios>
          <racion unidades="6">4€</racion>
          <unidad>1€</unidad>
        </precios>
        <ingredientes>arroz, salmon, alga nori.</ingredientes>
      </plato>
      <plato>
        <nombre tipo="plato">Onigiri de atun</nombre>
        <tipo alergenos="pescado">Sushi</tipo>
        <precios>
          <racion unidades="4">3€</racion>
          <unidad>1€</unidad>
        </precios>
        <ingredientes>arroz, atun, alga nori.</ingredientes>
      </plato>
      <plato>
        <nombre tipo="postre">Mochi</nombre>
        <sabores>chocolate, vainilla, fresa, mango.</sabores>
        <precios>
          <racion unidades="4">6€</racion>
          <unidad>2€</unidad>
        </precios>
        <ingredientes>harina de arroz, helado.</ingredientes>
      </plato>
      <plato>
        <nombre tipo="postre">Dango</nombre>
        <precios>
          <racion unidades="4">8€</racion>
          <unidad>3€</unidad>
        </precios>
        <ingredientes>harina de arroz, azucar, te en polvo.</ingredientes>
      </plato>
      <plato>
        <nombre tipo="bebida">Coca-cola</nombre>
        <precios>
          <unidad>2€</unidad>
        </precios>
      </plato>
      <plato>
        <nombre tipo="bebida">Fanta</nombre>
        <sabores>limon, naranja.</sabores>
        <precios>
          <unidad>2€</unidad>
        </precios>
      </plato>
    </platos>
  </carta>
</restaurante>
```

## XLST:
XSLT és un llenguatge utilitzat per transformar documents XML en altres formats o estructures com per exemple HTML. Basicament modifica l'estructura del document XML que donem per crear un nou document en el format que volem.

Podem trobar mes informacio de XSLT en aquest enllaç:
***[W3Schools XSLT](https://www.w3schools.com/xml/xsl_intro.asp)***


## XPath:
XPATH s'utilitza per fer consultes sobre nodes especifics d'un XML. 
Hi ha 7 tipus de nodes:
- Node arrel
- Elements
- Atributs
- Text 
- Espai de noms
- Comentaris
- Instuccions de processament

Utilitzan aquestes expresions sobre els nodes podem accedir a dades especifiques:
| Expresio      | Descripció |
|---------------|------------|
| Nom del node  | Indica tots els fills del nom del node |
| /             | Indica l'element arrel del document     |
| //            | Indica tots els elements del document  |
| .             | Indica el node actual                   |
| ..            | Indica el pare del node actual         |
| @             | Indica l'atribut d'un element           |

Exemples de consultes de XPath sobre aquest document XML:
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<botiga>
	<bluray>
		<titol idioma="ca">Avatar</titol>
		<director>J. Cameron</director>
		<preu>21</preu>
		<any>2009</any>
	</bluray>
	<bluray>
		<titol idioma="en">Zombieland</titol>
		<director>R. Fleischer</director>
		<preu>16</preu>
		<any>2009</any>
	</bluray>
	<bluray>
		<titol idioma="es">REC</titol>
		<director>Balaguero, Plaza</director>
		<preu>13</preu>
		<any>2007</any>
	</bluray>
	<bluray>
		<titol idioma="ca">REC2</titol>
		<director>Balaguero, Plaza</director>
		<preu>17</preu>
		<any>2009</any>
	</bluray>
	<bluray>
		<titol idioma="en">La herencia</titol>
		<director>Stephen</director>
		<preu>17</preu>
		<any>2010</any>
	</bluray>
	<bluray>
		<titol idioma="ca">Even the Rain</titol>
		<director>Thomas Edison</director>
		<preu>11</preu>
		<any>2005</any>
	</bluray>
	<bluray>
		<titol idioma="en">Black Bread</titol>
		<director>Vila</director>
		<preu>7</preu>
		<any>2010</any>
	</bluray>
</botiga>
```
Llistat dels títols de totes les pel·lícules de la botiga.

![image](https://github.com/RubenBof/Llenguatge-de-marques/assets/160047252/e41d38b3-652b-4aea-bb8b-64f5674c52ce)


Llistat de tots els preus de les pel·lícules de la botiga.

![image](https://github.com/RubenBof/Llenguatge-de-marques/assets/160047252/fb7b0bda-ddfa-4c3e-8b9e-04fccc940daa)


Preu de les pel·licules dirigides per "J. Cameron"

![image](https://github.com/RubenBof/Llenguatge-de-marques/assets/160047252/3d746735-de65-4d12-866c-80c0cab6b079)



Podem trobar mes informacio de XPath en aquest enllaç:
***[W3Schools XPath](https://www.w3schools.com/xml/xpath_intro.asp)***

## DOM:
Permet accedir, modificar i manipular documents HTML o XML utilitzant Python, per allo necesitem importar la seva llibreria amb aquesta linea: "from xml.dom import minidom". Utilitzant DOM en Python podem crear, llegir, actualitzar i eliminar nodes i contingut dins d'un document XML.

Exemple de un document de Python amb DOM:
```python
#!/usr/bin/env python3
from xml.dom import minidom

doc = minidom.parse("fitxer2.xml")
alumnes = {}
persona = doc.getElementsByTagName("persona")
assignaturas = doc.getElementsByTagName("assignatures")
for etiqueta in persona:
    alumne = {}
    asignaturas = []
    nom = etiqueta.getElementsByTagName("nom")[0].firstChild.data
    cognom = etiqueta.getElementsByTagName("cognoms")[0].firstChild.data
    edat = etiqueta.getElementsByTagName("edat")[0].firstChild.data
    alumne["nom"] = nom
    alumne["cognom"] = cognom
    alumne["edat"] = edat
    asignaturas1 = etiqueta.getElementsByTagName("assignatura")
    for x in asignaturas1:
        asignaturas.append(x.firstChild.data)
    alumne["asignaturas"] = asignaturas
    alumnes[f"{nom} {cognom}"] = alumne

opcio = "0"

while opcio != "3":
    print("""
1. Preguntar asignatura
2. Veure alumnes
3. Sortir
""")
    opcio = input("Quina opcio vols? ")
    if opcio == "1":
        buscar = input("Quina asignatura vols buscar ")
        for nom_dic, dades in alumnes.items():
            for x, y in dades.items():
                if x == "asignaturas":
                    for z in y:
                        if buscar == z:
                            print(f"L'alumne/a {nom_dic} te l'asignatura {buscar}")
                
    elif opcio == "2":
        for nom_dic, dades in alumnes.items():
            for x, y in dades.items():
                if x == "nom":
                    print(f"Nom: {y}")
                elif x == "cognom":
                    print(f"Cognom: {y}")
                elif x == "edat":
                    print(f"Edat: {y}")
                elif x == "asignaturas":
                    print("Asignaturas:")
                    for z in y:
                        print(f"  - {z}")
            print("\n")
        
    elif opcio == "3":
        print("Sortint...")
```

Podem trobar mes informacio de Dom en aquest enllaç:
***[W3Schools DOM](https://www.w3schools.com/xml/dom_intro.asp
)***







