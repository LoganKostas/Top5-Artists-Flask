from flask import Flask, render_template

# creating an instance of our flask
app = Flask(__name__)

# creating our routes
@app.route('/')
def home():
    artists = ['Young Thug','Young Nudy','Shoreline Mafia','Gunna','Future' ]
    return render_template('home.html',names = artists)
    

@app.route('/Young Thug')
def youngthug():
    songs = ['Take it To Trial','Bad Bad Bad','Digits','The London','Hot']
    return render_template('youngthug.html', music = songs)


@app.route('/Young Nudy')
def youngnudy():
    songs = ['EA','Nun To Do','Zone 6','Loaded Baked Potato','Impala']
    return render_template('youngnudy.html', music = songs)


@app.route('/Shoreline Mafia')
def shorelinemafia():
    songs = ['Musty','C Notes','Hoe Shit',"Pour Two 4's",'All the Time']
    return render_template('shorelinemafia.html', music = songs)


@app.route('/Gunna')
def gunna():
    songs = ['ONE WATCH','Fox 5','SKYBOX','Spending Addiction','BLINDFOLD']
    return render_template('gunna.html', music = songs)


@app.route('/Future')
def future():
    songs = ['Codeine Crazy','March Madness','PUFFIN ON ZOOTIEZ','X','Relationship']
    return render_template('future.html', music = songs)


