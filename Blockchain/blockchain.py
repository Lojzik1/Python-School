from flask import Flask, request, jsonify
import hashlib
import json

app = Flask(__name__)

muj_blockchain = []
cekajici_transakce = []

def vytvor_hash(blok):
    text_bloku = json.dumps(blok, sort_keys=True).encode()
    return hashlib.sha256(text_bloku).hexdigest()

prvni_blok = {
    "index": 1,
    "transakce": [],
    "predchozi_hash": "00000000000000000000"
}
muj_blockchain.append(prvni_blok)


@app.route('/pridat_transakci', methods=['POST'])
def pridej_transakci():
    data = request.get_json()
    
    nova_transakce = {
        "kdo_posila": data["kdo_posila"],
        "komu_posila": data["komu_posila"],
        "kolik": data["kolik"]
    }
    
    cekajici_transakce.append(nova_transakce)
    
    return "Transakce byla úspěšně přidána na hromádku!", 200


@app.route('/vytvor_blok', methods=['GET'])
def vytvor_blok():
    global cekajici_transakce 
    
    posledni_blok = muj_blockchain[-1]
    
    novy_blok = {
        "index": len(muj_blockchain) + 1,
        "transakce": cekajici_transakce,
        "predchozi_hash": vytvor_hash(posledni_blok) 
    }
    
    muj_blockchain.append(novy_blok)
    
    cekajici_transakce = []
    
    return "Nový blok byl vytvořen a přidán do blockchainu!", 200


@app.route('/ukaz_blockchain', methods=['GET'])
def ukaz():
    return jsonify(muj_blockchain), 200

if __name__ == '__main__':
    app.run(port=5000)