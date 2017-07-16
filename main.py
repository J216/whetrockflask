from flask import Flask, render_template

app = Flask(__name__)
# host='0.0.0.0'
# port='80'
app.debug = True

page_info = {}
page_info['business_name'] = u"Whetrock Quarries"
page_info['desciption'] = u"Supplier of Scalpings, Crusher Run, Screened Rock, Lateral Rock, Ag Lime, Ditch Liner, Rip Rap, and Shot Rock."
page_info['about'] = u"Whetrock Quarry is family owned and operated by the Whetstine family of Troy, KS. Forged in 1985 by Rodger Whetstine Sr., Whetrock Inc. has supplied limestone products to Doniphan County and surrounding area for the last 30 years. Now under the leader ship of Rodger D. Whetstine Jr., Whetrock is growing operations to meet increased demand of limestone products."
page_info['phone'] = u"(785) 985-2791"
page_info['phone_link'] = u"+17859852791"
page_info['address'] = u"1488 Mesquito Creek Rd, Troy, KS"
page_info['email'] = u"whetrockquarry@hotmail.com"
page_info['facebook'] = u"https://www.facebook.com/whetrockquarry/"
page_info['twitter'] = u"https://twitter.com/whetrockquarry"


@app.route("/")
def index():
    return render_template("index.html",page_info=page_info)

@app.route("/contact.html")
def contact():
    return render_template("contact.html", page_info=page_info)

@app.route("/products.html")
def products():
    return render_template("products.html", page_info=page_info)

@app.route("/about.html")
def about():
    return render_template("about.html", page_info=page_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)
