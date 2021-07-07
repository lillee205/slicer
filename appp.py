from flask import Flask, request, jsonify
import traceback
from flask.templating import render_template
from pythonFunc import compressArr, checkEvenlySpaced
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/selectIndex')
def selectIndex():
    return render_template("selectIndex.html")

@app.route('/typeIndex')
def typeIndex():
    return render_template("typeIndex.html")

@app.route('/bg_process_getSplice')
def bg_process_getSplice():
    pythonSliceStr = ""

    indexes = eval(request.args.to_dict()["indexes"])
    if len(indexes) > 1:
        diffFlag = checkEvenlySpaced(indexes)
        if diffFlag != False:
            pythonSliceStr += "item[{}:{}{}]".format(indexes[0] if indexes[0] != 0 else "", indexes[-1] + 1, ":" + str(diffFlag) if diffFlag != 1 else "")
            return jsonify(pythonSliceStr)
    compressedArr = compressArr(indexes)

    for range in compressedArr:
        if type(range) == tuple:
            pythonSliceStr += "item[{}:{}]".format(range[0], range[1] + 1)
        else:
            pythonSliceStr += "[item[{}]]".format(range)
        
        pythonSliceStr += " + "
    pythonSliceStr = pythonSliceStr[:-3]
    return jsonify(pythonSliceStr)

@app.route('/bg_process_typeSplice')
def bg_process_typeSplice():
    item = eval(request.args.to_dict()["item"])
    splice = request.args.to_dict()["splice"]
    try:
        x = eval(splice)
        selectedIndexes=[]
        arrOfSpliced = splice.split("+")
        for spliced in arrOfSpliced:
            spliced = spliced.strip()
            spliced = spliced if spliced[0] != "[" else spliced[1:-1]
            sect = spliced[spliced.index("[") + 1:spliced.index("]")].split(":")
            sectNum = [eval(x) for x in sect]
            selectedIndexes.append(list(range(*sectNum)) if len(sect) > 1 else ([sectNum[0]]))
        print(selectedIndexes)
        print("\n\n\n")
        return jsonify(result = selectedIndexes)
    except Exception as e:
        traceback.print_exc()
        return jsonify(result = "Error: " + str(e))
        

if __name__ == "__main__":
    app.run(debug=True)
