from flask import Flask, render_template

app = Flask (__name__)


@app.route('/play')
def index():
    return render_template( "index.html", color='lightblue', num=3)

@app.route('/play/<int:times>')
def indextimes(times):
    return render_template( "index.html", color='skyblue', num=times)

@app.route('/play/<int:times>/<color>')
def indexntimescolor(times,color):
    return render_template( "index.html", color=color, num=times)

if __name__=="__main__":
    app.run(debug=True)