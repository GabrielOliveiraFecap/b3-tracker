import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template
from banco import listar_tickers, adicionar_ticker, remover_ticker

load_dotenv()

token= os.getenv("TOKEN")

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get(
        "https://brapi.dev/api/v2/stocks/quote",
        headers={"Authorization": f"Bearer {token}"},
        params={"symbols": ",".join(listar_tickers())},
    )
    response.raise_for_status()
    data = response.json()

    acoes = []
    for item in data["results"]:
        quote = item["data"]
        acoes.append({
            "ticker": item["symbol"],
            "preco": quote["regularMarketPrice"],
            "variacao": quote["regularMarketChangePercent"],
        })

    return render_template("index.html", titulo="B3 Tracker", acoes=acoes)



if __name__ == "__main__":
    app.run(debug=True)