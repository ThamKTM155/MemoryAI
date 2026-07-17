from flask import Flask
from flask import request
from flask import jsonify

from memory_answer import answer_memory

app = Flask(__name__)

@app.route("/memory")
def memory():

    query = request.args.get(
        "q",
        ""
    )

    answer = answer_memory(
        query
    )

    return jsonify({
        "query": query,
        "answer": answer
    })

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5005,
        debug=False
    )