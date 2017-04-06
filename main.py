
from flask import Flask, render_template, request

from google.appengine.api import memcache
from google.appengine.api import users
from google.appengine.api import mail

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def counter():
    if 'reset' in request.args:
      memcache.flush_all()

 
  
      
       
    # set up names if it doesn't exist
    memcache.add('names','')
    memcache.add('sexes','')
    memcache.add('memes','')
    memcache.add('langs','')
    
    name = ""
    sex = ""
    meme=""
    lang=""
    confirm=""
    results=""
    
    if request.method == 'GET' and 'email' in request.args:
      name = request.args['email']
     
      # Check to see if that name is in names
      names = memcache.get('names')
      if name in names.split('/'):
      	# that person is already there
      	memcache.incr(name)
      else:
        memcache.set('names', names + '/' + name)
        memcache.set(name,1)
    names = memcache.get('names').split('/')
    counts = []
    for n in names:
      counts.append( (n, memcache.get(n) ) )

    
    if request.method == 'GET' and 'sex' in request.args:
      sex = request.args['sex']
      
      sexes = memcache.get('sexes')
      if sex in sexes.split('/'):
	memcache.incr(sex)
      else:
	memcache.set('sexes', sexes + '/' + sex)
        memcache.set(sex,1)
    sexes = memcache.get('sexes').split('/')
    
    for n in sexes:
      counts.append( (n, memcache.get(n) ) )


    if request.method == 'GET' and 'meme' in request.args:
      meme = request.args['meme']
      
      memes = memcache.get('memes')
      if meme in memes.split('/'):
	memcache.incr(meme)
      else:
	memcache.set('memes', memes + '/' + meme)
        memcache.set(meme,1)
    memes = memcache.get('memes').split('/')
    
    for n in memes:
      counts.append( (n, memcache.get(n) ) )

    if request.method == 'GET' and 'lang' in request.args:
      lang = request.args['lang']
      
      langs = memcache.get('langs')
      if lang in langs.split('/'):
	memcache.incr(lang)
      else:
	memcache.set('langs', langs + '/' + lang)
        memcache.set(lang,1)
    langs = memcache.get('langs').split('/')
    
    for n in langs:
      counts.append( (n, memcache.get(n) ) )

    for resp in counts:
	a,b = resp
	results = results + a + ', ' +str(b) + '\n'
    
   

    
      

    user = users.get_current_user()
    if user:
      #return str(dir(user))
      curr_users = memcache.get('curr_users')
      if curr_users:
        if user.nickname() not in curr_users:
          curr_users.append(user.nickname())
          memcache.set('curr_users',curr_users)
      else:
        memcache.set('curr_users',[user.nickname()])
      #logout_url = users.create_logout_url('/')
      curr_users = memcache.get('curr_users') 
      return render_template('survey.html', counts=counts, name=name)  
    else:
      login_url = users.create_login_url('/')
      return render_template('logout.html', login_url=login_url)

    
    

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
    
    
    
    
    
    
    
    

