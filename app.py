from flask import Flask
from flask import url_for
from flask import render_template


app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")    

@app.route("/dashboard2.html")
def dashboard2():
    return render_template("dashboard2.html")

@app.route("/dashboard3.html")
def dashboard3():
    return render_template("dashboard3.html")    

@app.route("/dashboard4.html")
def dashboard4():
    return render_template("dashboard4.html")

@app.route("/facts.html")
def facts():
    return render_template("facts.html")

@app.route("/cpc_a.html")
def cpc_a():
    return render_template("cpc_a.html")

@app.route("/cpc_d.html")
def cpc_d():
    return render_template("cpc_d.html")

@app.route("/cpc_f.html")
def cpc_f():
    return render_template("cpc_f.html")

@app.route("/cpc_n.html")
def cpc_n():
    return render_template("cpc_n.html")

@app.route("/cpc_s.html")
def cpc_s():
    return render_template("cpc_s.html")

@app.route("/cpc_total.html")
def cpc_total():
    return render_template("cpc_total.html")

@app.route("/ppg_b.html")
def ppg_b():
    return render_template("ppg_b.html")

@app.route("/ppg_c.html")
def ppg_c():
    return render_template("ppg_c.html")

@app.route("/ppg_d.html")
def ppg_d():
    return render_template("ppg_d.html")

@app.route("/ppg_h.html")
def ppg_h():
    return render_template("ppg_h.html")

@app.route("/ppg_i.html")
def ppg_i():
    return render_template("ppg_i.html")

@app.route("/ppg_total.html")
def ppg_total():
    return render_template("ppg_total.html")

@app.route("/tp_b.html")
def tp_b():
    return render_template("tp_b.html")

@app.route("/tp_c.html")
def tp_c():
    return render_template("tp_c.html")

@app.route("/tp_e.html")
def tp_e():
    return render_template("tp_e.html")

@app.route("/tp_v.html")
def tp_v():
    return render_template("tp_v.html")

@app.route("/tp_i.html")
def tp_i():
    return render_template("tp_i.html")

@app.route("/tp_total.html")
def tp_total():
    return render_template("tp_total.html")

@app.route("/tc_b.html")
def tc_b():
    return render_template("tc_b.html")

@app.route("/tc_f.html")
def tc_f():
    return render_template("tc_f.html")

@app.route("/tc_g.html")
def tc_g():
    return render_template("tc_g.html")

@app.route("/tc_j.html")
def tc_j():
    return render_template("tc_j.html")

@app.route("/tc_u.html")
def tc_u():
    return render_template("tc_u.html")

@app.route("/tc_total.html")
def tc_total():
    return render_template("tc_total.html")

if __name__=="__main__":
    app.run(debug=True)
