from flask import Flask
from flask import request
from flask import jsonify
from flask import send_from_directory
from tools.memory_answer import answer_memory
from tools.knowledge_gate import ask
from tools.core_identity import answer_identity


app = Flask(__name__)

@app.route("/memory")
def memory():

    query = request.args.get(
        "q",
        ""
    )

    answer = ask(query)

    return jsonify({
        "query": query,
        "answer": answer
    })
# ====================================
# IDENTITY
# ====================================

@app.route("/identity")
def identity():

    query = request.args.get(
        "q",
        ""
    )

    answer = answer_identity(
        query
    )

    if answer is None:

        answer = ""

    return jsonify({

        "query": query,

        "answer": answer

        
    @app.route("/favicon.ico")
        def favicon():
        return send_from_directory(
            app.static_folder,
            "favicon.ico",
            mimetype="image/vnd.microsoft.icon"
        )
    })
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5005,
        debug=False
    )