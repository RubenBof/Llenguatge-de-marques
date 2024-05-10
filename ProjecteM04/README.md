# 1. Instruccions per desplegar l'aplictiu.
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
[Documentació adicional de Flask](https://flask.palletsprojects.com/en/3.0.x/)
