from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()

from src.sow.crew import Sow
import warnings
from datetime import datetime
import os

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = Flask(__name__)

@app.route("/generate-sow", methods=["POST"])
def generate_sow():
    data = request.json or {}

    inputs = {
        'Client': data.get('Client', 'Default Client'),
        'Contractor': data.get('Contractor', 'Default Contractor'),
        'raw_description': data.get('raw_description', ''),
        'current_year': str(datetime.now().year)
    }

    try:
        Sow().crew().kickoff(inputs=inputs)

        # Read the generated scope_of_work.md file
        output_file = "scope_of_work.md"
        if not os.path.exists(output_file):
            return jsonify({
                "status": "error",
                "message": "SOW generated, but scope_of_work.md was not found."
            }), 500

        with open(output_file, "r", encoding="utf-8") as f:
            sow_content = f.read()

        return jsonify({
            "status": "success",
            "message": "SOW generated successfully.",
            "sow_content": sow_content
        }), 200


    except Exception as e:
        import traceback
        return jsonify({
            "status": "error",
            "message": str(e),
            "trace": traceback.format_exc()
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
