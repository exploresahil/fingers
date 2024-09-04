from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
import cv2
import fingerprint_enhancer

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'dib', 'bmp'}

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        folder_name = request.form.get('folder_name', 'default_folder').strip()
        processed_folder = os.path.join(
            app.config['PROCESSED_FOLDER'], folder_name)
        os.makedirs(processed_folder, exist_ok=True)

        files = request.files.getlist('files')
        for file in files:
            if file and allowed_file(file.filename):
                # Create the full path for the file in the upload folder
                file_path = os.path.join(
                    app.config['UPLOAD_FOLDER'], file.filename)

                # Ensure the directory exists before saving the file
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                file.save(file_path)

                # Process the file
                img = cv2.imread(file_path, 0)
                if img is not None:
                    out = fingerprint_enhancer.enhance_Fingerprint(img)
                    output_filename = file.filename.rsplit(
                        '.', 1)[0] + '_enhanced.jpeg'
                    output_path = os.path.join(
                        processed_folder, output_filename)
                    cv2.imwrite(output_path, out)

        return redirect(url_for('uploaded_files', folder=folder_name))

    return render_template('upload.html')


@app.route('/processed/<folder>/<filename>')
def processed_file(folder, filename):
    return send_from_directory(os.path.join(app.config['PROCESSED_FOLDER'], folder), filename)


@app.route('/uploaded_files')
def uploaded_files():
    folder = request.args.get('folder', 'default_folder')
    processed_folder = os.path.join(app.config['PROCESSED_FOLDER'], folder)
    files = os.listdir(processed_folder)
    return render_template('files.html', files=files, folder=folder)


if __name__ == '__main__':
    app.run(debug=True)
