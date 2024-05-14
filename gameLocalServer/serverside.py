import os
from fpdf import FPDF
from flask import Flask, request, jsonify

app = Flask(__name__)

OUTPUT_PATH = r"/home/kemon/Game"  # Specify the output directory

def generate_receipt(player_name, player_score, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Name: " + str(player_name), ln=True, align='C')
    pdf.cell(200, 10, txt="Points: " + str(player_score), ln=True, align='C')
    file_path = os.path.join(OUTPUT_PATH, filename)
    pdf.output(file_path, "F")
    return file_path

@app.route("/print-score", methods=["POST"])
def print_score():
    score = request.json.get('score')  # Getting score from JSON data
    filename = request.args.get('filename')  # Getting filename from request parameters

    split_data = score.split(",")
    player_name, player_score = split_data[0], split_data[1]

    if not score:
        return jsonify({"error": "Missing score."}), 400

    if not filename:
        return jsonify({"error": "Missing filename."}), 400

    try:
        generated_filename = generate_receipt(player_name, player_score, filename)
        return jsonify({"message": "Score sent successfully!", "filename": generated_filename}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
