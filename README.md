# Documentacio amb Markdown.
## XML:
L'XML es un **llenguatge de marques** estandard que utilitza etiquetes per representar informació. Els documents XML sempre tenen una etiqueta pare y altres etiquetes filles. L'objectiu principal del xml es aconseguir un document ben format que pugi ser llegit per ordinadors y persones. Aquestos documents requereixen una validesa, que es pot comprovar al navegador. L'xml es poden crear y editar en qualsevol editor de text.
Podem trobar mes informacio de xml en el seguent enllaç: 
-[W3Schools](https://www.w3schools.com/xml/xml_whatis.asp)-

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

Utilitzan aquestes expresione sobre els nodes podem accedir a dades especifiques:
| Expresio      | Descripció |
|---------------|------------|
| Nom del node  | Indica tots els fills del nom del node |
| /             | Indica l'element arrel del document     |
| //            | Indica tots els elements del document  |
| .             | Indica el node actual                   |
| ..            | Indica el pare del node actual         |
| @             | Indica l'atribut d'un element           |

## DOM:
Permet accedir, modificar i manipular documents HTML o XML utilitzant Python, per allo necesitem importar la seva llibreria amb aquesta linea: "from xml.dom import minidom". Utilitzant DOM en Python podem crear, llegir, actualitzar i eliminar nodes i contingut dins d'un document XML.








