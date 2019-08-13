from flask import Flask, session, redirect  # Import Flask to allow us to create our app
app = Flask(__name__) 

app.secret_key = 'abc'

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
  if 'count' in session:
    session['count'] += 1
    print (' in session','-'*30, session['count'])
  else:
    session['count'] = 0
  return str(session['count'])


@app.route('/destroy_session')
def howmany ():
  session['count'] = 0
  return redirect('/')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    