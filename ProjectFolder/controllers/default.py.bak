def mobileindex():
    return locals()
@auth.requires_login()
def index():
    if request.user_agent().is_mobile:
        response.view='default/mobileindex.html'
    useract=db(db.auth_user.id == auth.user_id).select().first()
    point=0
    if db(db.profile.user_id == auth.user_id).select():
        point= db(db.profile.user_id == auth.user_id).select().first()
    else:
        response.flash="Please Update your profile."
    levels=5
    return locals()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    if request.args[0]=='profile':
        redirect(URL('profile','index'))
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
