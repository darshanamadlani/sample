# from datetime import date, datetime,time
from flask import Flask, render_template, request
import test


app = Flask(__name__)


@app.route("/display")
def main():
    return render_template('page1.html')

@app.route("/", methods=['GET','POST'])
def display():
        if request.form.get('sid'):
            sid =  str(request.form.get('sid'))
            test.cursor.execute("""SELECT grants.GrantTitle, grants.Type, grants.AccountNo
                                    FROM gra,grants
                                    WHERE gra.Funding = grants.AccountNo and StudentId = %s""",[sid])
            data = test.cursor.fetchall()
            print(data)
            return render_template('display_GRA.html',data=data)
        else:
            Error_text = "Please enter Data"
        return render_template('display_GRA.html',Error_text=Error_text)
    

if __name__ == "__main__":
    app.run()