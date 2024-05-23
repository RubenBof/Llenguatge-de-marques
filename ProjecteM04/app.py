from flask import Flask, request, render_template, redirect, url_for, flash
from flask import request
import feedparser

app = Flask(__name__)
app.secret_key = '¡3248 97320983 bkjxdlrkfj k2 r9p874989387 98p78oiyylkhçç'

#
# Exemple de formulari amb post
#
@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == 'GET':
        return render_template("exemples/insert/insert_form.html")
    else:
        # POST
        producte = request.form.get('producte', type = str)
        quantitat = request.form.get('quantitat', type = int)

        # Aquí hauríem de fer alguna cosa amb producte i quantitat
        # com per exemple un insert a la base de dades

        # https://www.seobility.net/es/wiki/Post/Redirect/Get
        flash(f"El producte {producte} amb quantitat {quantitat} s'ha inserit correctament")
        return redirect(url_for('insert'))

@app.route('/')
def index():
    deportes = feedparser.parse("https://www.lavanguardia.com/rss/deportes.xml")
    politica = feedparser.parse("https://www.lavanguardia.com/rss/politica.xml")
    vida = feedparser.parse("https://www.lavanguardia.com/rss/vida.xml")
    series = feedparser.parse("https://www.lavanguardia.com/rss/series.xml")
    tecnologia = feedparser.parse("https://www.lavanguardia.com/rss/tecnologia.xml")
    return render_template("index.html", deportes = deportes, vida = vida, politica = politica, series = series, tecnologia = tecnologia)



@app.route('/lavanguardia/<seccio>')
def lavanguardia(seccio):
    rss = get_rss_lavanguardia(seccio)
    return render_template("lavanguardia.html", rss = rss)

def get_rss_lavanguardia(seccio):
    # MODE REMOT: versió on descarrega l'XML de la web
    xml = f"https://www.lavanguardia.com/rss/{seccio}.xml"    
    rss = feedparser.parse(xml)
    return rss
