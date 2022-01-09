import chardet, re
from flask import Flask, render_template, flash, request
from app.basic import runDetermine
from app.forms import InputForm


app = Flask(__name__)
app.secret_key = 'secretKey'


def allowed_file(fileType):
    allowedList = ['application/octet-stream', 'text/plain']
    return True if fileType in allowedList else False


def languageDetect(text):
    return bool(re.search('[а-яА-Я]', text))


@app.route('/determine', methods=["GET", "POST"])
def determine():
    try:
        form = InputForm()
        if request.method == 'POST':
            submit = form.validate_on_submit()
            if submit and request.form["message"] != "":
                message = request.form["message"]
                form.message.data = ""
                if not message.isdigit():
                    if not languageDetect(message):
                        result = runDetermine(message)
                        flash(result)
                    else:
                        exit(1)

            elif submit and form.file.data.filename != "":
                if allowed_file(form.file.data.content_type):
                    filestream = form.file.data
                    filestream.seek(0)
                    # Read from FileStorage
                    content = filestream.read()
                    message = content.decode(chardet.detect(content)['encoding'])
                    form.message.data = ""

                    if not message.isdigit():
                        if not languageDetect(message):
                            result = runDetermine(message)
                            flash(result)
                        else:
                            exit(1)
                else:
                    exit(1)
    except:
        result = "Найдены ошибки при обработке данных. " \
                 "Файл имеет не корректную кодировку/введены символы не английского алфавита."
        flash(result)
        form.message.data = ""
    finally:
        return render_template('determine.html', form=form)


if __name__ == "__main__":
    from waitress import serve
    #serve(app, host='0.0.0.0', port=3000)
    app.run(host='0.0.0.0',port=3000)
