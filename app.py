from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/generate')
def generate():
    # Shallotを呼び出し、出力を取得する
    output = subprocess.check_output(["./Shallot/shallot", "^sumi"])
    # 出力を解析してpublic_keyとprivate_keyを取得する
    # （ここでは省略。実際には適切に解析する必要があります）
    public_key = ""
    private_key = ""
    return jsonify({"public_key": public_key, "private_key": private_key})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
