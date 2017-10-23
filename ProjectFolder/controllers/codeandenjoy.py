# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    levels=5
    useract=db(db.auth_user.id == auth.user_id).select().first()
    point=0
    if db(db.profile.user_id == auth.user_id).select():
        point= db(db.profile.user_id == auth.user_id).select().first()
    return locals()

def levelsuccess():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if int(request.args[0])> int(at.playing3):
        session.flash="LEVEL INCREASED on INTRODUCTION TO DATA STRUCTURES"
        db(db.auth_user.id == auth.user_id).update(playing3= int(request.args[0]))
    redirect(URL('codeandenjoy','index'), client_side=True)

@auth.requires_login()
def level1():
    return locals()

@auth.requires_login()
def level2():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing3 < 1:
        raise HTTP(502,"Bad Gateway.")
    return locals()

@auth.requires_login()
def level3():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing3 < 2:
        raise HTTP(502,"Bad Gateway.")
    return locals()

@auth.requires_login()
def level4():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing3 < 3:
        raise HTTP(502,"Bad Gateway.")
    return locals()

@auth.requires_login()
def level5():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing3 < 4:
        raise HTTP(502,"Bad Gateway.")
    return locals()

@auth.requires_login()
def level6():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing3 < 5:
        raise HTTP(502,"Bad Gateway.")
    return locals()
