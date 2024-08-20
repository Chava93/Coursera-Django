from django.http import HttpResponse


# Create your views here.
def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    r = "<p>view count="+str(num_visits)+"</p> <p>da4064fd</p>"
    resp = HttpResponse(r)
    resp.set_cookie('dj4e_cookie', 'da4064fd', max_age=1000)
    return resp