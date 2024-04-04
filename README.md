# Documentacio amb Markdown.
## XML:
L'XML es un llenguatge de marques estandard que utilitza etiquetes per representar informació. Els documents XML sempre tenen una etiqueta pare y altres etiquetes filles. L'objectiu principal del xml es aconseguir un document ben format que pugi ser llegit per ordinadors y persones. Aquestos documents requereixen una validesa, que es pot comprovar al navegador. L'xml es poden crear y editar en qualsevol editor de text.
Podem trobar mes informacio de xml en el seguent enllaç: 
"Insertar enlace"

Aqui tenem un exemple de un xml ben format.
"xml bien formado"

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








