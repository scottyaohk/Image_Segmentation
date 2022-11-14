from flask import Flask, render_template, request, jsonify, redirect, url_for
import time
import Compression as C

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

images_directory = "static/images_source/"
images_target = "static/images_result/"
suffix = '.jpg'
def get_file_path():
    filename=str(int(time.time()))
    return f"{images_directory}{filename}{suffix}", f"{images_target}{filename}{suffix}"

@app.route('/transform',methods=["POST","GET"])
def identify():
    file = request.files['file']
    if file.filename == "":
        return render_template("index.html", ALERT="A JPG file is required. You can use the download link in the instruction part above.")
    try:
        k=int(request.values.get("k"))
    except:
        return render_template("index.html", ALERT="Please type in an integer in the range of [1,11] (Because of the capacity of my server, the number can't be too large)")
    if k<1 or k>11:
        return render_template("index.html", ALERT="Please type in an integer in the range of [1,11] (Because of the capacity of my server, the number can't be too large)")
    file_name, file_dest = get_file_path()
    file.save(file_name)
    C.Compress(file_name, file_dest,k)
    return render_template("index.html", img_dir_ori=file_name, img_dir_res=file_dest)


if __name__ == '__main__':
    app.run('127.0.0.1', 8000)
