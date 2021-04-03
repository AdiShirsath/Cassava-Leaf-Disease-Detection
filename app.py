from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow_hub as hub
from tensorflow.keras.preprocessing import image
import os
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
model = load_model('cropnet_1.h5', custom_objects={'KerasLayer': hub.KerasLayer})
disease_names = ['Cassava Bacterial Blight', 'Cassava Brown Streak Disease', 'Cassava Green Mottle', 'Cassava Mosaic Disease', 'Healthy']
uploaded_folder="static/images/uploaded"


# function to process image and predict results
def process_predict(image_path, model):
    # read image
    img = image.load_img(image_path, target_size=(224, 224))
    # preprocess image
    img = image.img_to_array(img)
    # now divide image and expand dims
    img = np.expand_dims(img, axis=0) / 255
    # Make prediction
    pred_probs = model.predict(img)
    # Get name from prediction
    pred = disease_names[np.argmax(pred_probs)]
    pred_probs = round(np.max(pred_probs)*100, 2)
    return pred, pred_probs


run_with_ngrok(app)
@app.route('/', methods=['GET', 'POST'])
def home_page():
  if request.method == 'POST':
        # name inside files and in html input should match
        image_file = request.files['file']
        if image_file:
                filename = image_file.filename
                file_path = os.path.join( uploaded_folder, filename)
                image_file.save(file_path)
                # prediction
                pred, pred_proba = process_predict(file_path, model)
                if pred_proba > 45:
                  return render_template('prediction.html', prediction=pred, prediction_probability=pred_proba)
                else:
                    return render_template('false_pred.html')  
  return render_template("index.html")


@app.route('/Categories')
def categories_page():
    return render_template('categories.html')

@app.route('/About')
def about_page():
    return render_template("about.html")


app.get('/app/:id', checkUserAuth, findApp, renderView, sendJSON);

function checkUserAuth(req, res, next) {
  if (req.session.user) return next();
  return next(new NotAuthorizedError());
}

if __name__ == '__main__':
    app.run()
