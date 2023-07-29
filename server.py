from flask import Flask
app = Flask(__name__)
@app.route("/", methods=["GET"])
def root():
    return "welcome to ITIL exam.............."
@app.route("/modules", methods=["GET"])
def modules():
    return "COSA,ITIAM,FCN,NDC,security-concepts,dev-ops,compliance-audit"
@app.route("/me", methods=["GET"])
def me():
    return "PRN:230344223045,Name: saurabh sawarkar,Phone number: 960415574"
      
  
app.run(host="0.0.0.0",port=4000, debug=True)



