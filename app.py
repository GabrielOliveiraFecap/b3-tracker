from flask import Flask, render_template
import requests

token = ""
response = requests.get(
    "https://brapi.dev/api/v2/stocks/quote",
    headers={"Authorization": f"Bearer {token}"},
    params={"symbols": "PETR4,VALE3,MGLU3,ITUB4"},
)
response.raise_for_status()
data = response.json()
for item in data["results"]:
    quote = item["data"]
    print(item["symbol"], quote["regularMarketPrice"])

'''apiKey = ""
urlBase = "https://brapi.dev/api/v2/stocks/quote?symbols=PETR4,VALE3,ITUB4,MGLU3"
parametros = {
    'key': apiKey,
}
reposta = requests.get(urlBase, params=parametros)

print(reposta.content)'''

#app = Flask(__name__)

#@app.route("/")
#def home():
 #   return render_template("index.html", titulo="B3 Tracker")

#if __name__ == "__main__":
 #   app.run(debug=True)