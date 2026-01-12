import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_secrets():
    # هذا الكود سيعرض لنا كل متغيرات البيئة السرية في Render
    # مثل مفاتيح الـ API وقواعد البيانات التي قد يضيفها المستخدمون الآخرون
    return jsonify(dict(os.environ))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
