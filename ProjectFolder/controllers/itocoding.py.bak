# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
    if request.user_agent().is_mobile:
        response.view='itocoding/mobileindex.html'
    levels=2
    useract=db(db.auth_user.id == auth.user_id).select().first()
    point=0
    if db(db.profile.user_id == auth.user_id).select():
        point= db(db.profile.user_id == auth.user_id).select().first()
    return locals()

@auth.requires_login()
def mobileindex():
    levels=5
    useract=db(db.auth_user.id == auth.user_id).select().first()
    point=0
    if db(db.profile.user_id == auth.user_id).select():
        point= db(db.profile.user_id == auth.user_id).select().first()
    return locals()

@auth.requires_login()
def level1():
    return locals()

@auth.requires_login()
def levelsuccess():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if int(request.args[0])> int(at.playing2):
        session.flash="LEVEL INCREASED on INTRODUCTION TO CODING"
        db(db.auth_user.id == auth.user_id).update(playing2= int(request.args[0]))
    redirect(URL('itocoding','index'), client_side=True)

@auth.requires_login()
def level2():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing2 < 1:
        raise HTTP(502,"Bad Gateway.")
    return locals()
'''
@auth.requires_login()
def level3():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing2 < 2:
        raise HTTP(502,"Bad Gateway.")
    return locals()

@auth.requires_login()
def level4():
    at=db(db.auth_user.id == auth.user_id).select().first()
    if at.playing2 < 3:
        raise HTTP(502,"Bad Gateway.")
    return locals()
'''
