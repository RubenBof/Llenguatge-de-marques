# Projecte M04
### Rubén Rodríguez Bayón

## Index
* 1 Instruccions per desplegar l'aplictiu.
* 2 Documentació
  * 2.1 Flask
  * 2.2 Jinja
  * 2.3 RSS
  * 2.4 Feedparser
* 3. Com funcionen els modes remot y local.
  * 3.1 Remot
  * 3.2 Local


## 1. Instruccions per desplegar l'aplictiu.
El pirmer que tenim que fer es executar les seguents instruuccions:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Per a Linux.
```batch
python -m venv .venv
.venv\Scripts\activate
```
Per a Windows.

Per sortir de l'entorn farem:
```bash
deactivate
```

Un cop dins de l'entorn tenim que instalar flask i feedparser, ho farem amb les seguents comandes:
```bash
pip install flask
pip install feedparser
```
Despres,dins de l'aplicatiu executarem les seguents comandes per iniciar el servidor Flask:
```bash
flask run --debug
```
Si volem aturar el servidor Flask, tenim que fer "Ctrl + C".

Per a mes informacio revisar [documentació adicional de Flask](https://flask.palletsprojects.com/en/3.0.x/)
