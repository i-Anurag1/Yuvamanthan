from flask import *
from process_video import detective
from keras.models import load_model

model = load_model('model.h5') #Load in the model 

app = Flask(__name__, static_url_path='/static')   #Initialise the app and mark /static/ as the directory for CSS and Images

@app.route('/')  
def upload():  #Upload function for index.html
	return render_template("upload.html") 

@app.route('/result', methods = ['POST'])  
def result():  
	if request.method == 'POST':  
		f = request.files['file'] #Request the files
		f.save(f.filename) #Save the file
		pred = detective(f.filename, model) #Run our function on the video and save the output in pred
		return render_template("classify.html", name = f.filename, pred = pred)

if __name__ == '__main__':
	app.run(debug = True)  
