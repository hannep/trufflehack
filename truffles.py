from flask import Flask, render_template
import random 


app = Flask(__name__)

@app.route("/")

def doit(): 

	adj = ["The finest", "Exquisite", "Aromatic", "Delectable", "Decadent", "Indulgent", "Distinctive", "Divine", "Gourmet", "Subtle", "Vibrant", "Innovative" ]
	ing = ["maple bourbon", "absinthe", "grand marnier", "orange extract", "orange bitters", "orange spice bitters", "lavender bitters", "celery bitters", "peychaud's bitters", "almond extract", "vanilla extract", "wild orange blossom tea", "thai tea", "earl grey supreme", "lemon tea", "peach oolong", "anise", "cinnamon", "nutmeg", "cardamom", "allspice", "ginger", "smoked salt", "fleur de sel", "smoked paprika", "turkish paprika", "rosemary", "rainbow peppercorns", "honey", "mango puree", "pear puree", "raspberry puree", "pink lemon zest", "orange zest"] 	
	out = ["enrobed in chocolate", "rolled in cocoa"]
	on = ["", "and drizzled with white chocolate.", u"and accented with pearl drag\u00E9es.", "and sprinkled with grated chocolate.", "and festively embellished with sprinkles."]
	return render_template("truffle.html", adjective = random.sample(adj, 1), ingredients = random.sample(ing, 3), outside = random.sample(out, 1), on = random.sample(on, 1))
if __name__ == "__main__":
    app.run(debug=True)

