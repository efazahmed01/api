from flask import Flask, request, jsonify
from parrot import Parrot

app = Flask(__name__)
parrot = Parrot()

@app.route('/paraphrase', methods=['POST'])
def paraphrase():
    input_text = request.json.get("text", "")
    results = parrot.augment(input_phrase=input_text, use_gpu=False)
    output = [r[0] for r in results] if results else []
    return jsonify({"paraphrases": output})
