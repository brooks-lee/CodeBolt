# -*- coding: utf-8 -*-
# try something like
@auth.requires_login()
def index():
    levels=2
    useract=db(db.auth_user.id == auth.user_id).select().first()
    point=0
    if db(db.profile.user_id == auth.user_id).select():
        point= db(db.profile.user_id == auth.user_id).select().first()
    return locals()

def allaboutcomp():
    return locals()

@auth.requires_login()
def level1():
    return locals()

def levelsuccess():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if int(request.args[0])> int(at.playing1):
        session.flash="LEVEL INCREASED on INTRODUCTION TO COMPUTERS"
        db(db.auth_user.id == auth.user_id).update(playing1= int(request.args[0]))
    redirect(URL('itocomputers','index'), client_side=True)
    
@auth.requires_login()
def level2():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing1 < 1:
        raise HTTP(502,"Bad Gateway.")
    return locals()

@auth.requires_login()
def level3():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing1 < 1:
        raise HTTP(502,"Bad Gateway.")
    return locals()
