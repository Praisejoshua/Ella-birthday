from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def birthday_page():
    heartfelt_message = """Hey Inemese :),  

I must have done something wild to have met you and kept you in my life, and honestly, I wouldn't have it any other way.  

I’ll keep this short—Happy Birthday! 🎉 Thank you for everything, for always being there, for the jokes, for the gist, for DLS, for just being "you". I appreciate you more than words can say, and I love you so much.  

Distance may be a thing now, but if I could, I’d trade anything to be by your side today. Happy Birthday, Ella! 😊🤗.

    """
    return render_template('birthday.html', heartfelt_message=heartfelt_message)

if __name__ == "__main__":
    app.run(debug=True)
