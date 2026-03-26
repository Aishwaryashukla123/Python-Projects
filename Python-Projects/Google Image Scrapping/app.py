from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import logging
import os

logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/review', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            query = request.form['content'].replace(" ", "")
            save_directory = "static/"

            if not os.path.exists(save_directory):
                os.makedirs(save_directory)

            headers = {
                "User-Agent": "Mozilla/5.0"
            }

            url = f"https://www.google.com/search?tbm=isch&q={query}"
            response = requests.get(url, headers=headers)

            soup = BeautifulSoup(response.content, "html.parser")
            image_tags = soup.find_all("img")

            img_data = []

            for i, image_tag in enumerate(image_tags[1:]):
                image_url = image_tag.get('src')

                #if not image_url:
                if not image_url or not image_url.startswith("http"):
                    continue

                try:
                    image_data = requests.get(image_url).content
                    file_name = f"{query}_{i}.jpg"

                    with open(os.path.join(save_directory, file_name), "wb") as f:
                        f.write(image_data)

                    img_data.append(file_name)

                except Exception as e:
                    logging.info(e)

            #return f"{len(img_data)} images downloaded successfully!"
            return render_template("result.html",images= img_data)

        except Exception as e:
            logging.info(e)
            return "Something went wrong!"

    else:
        return(
render_template("index.html"))


if __name__=="__main__":
    app.run(debug=True)
