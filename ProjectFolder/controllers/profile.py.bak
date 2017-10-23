# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
    authdetails=SQLFORM(db.auth_user, auth.user_id, fields=['first_name', 'last_name', 'email', 'password'], showid=False, submit_button="Update").process(next=URL('profile','index'))
    point=0
    if db(db.profile.user_id == auth.user_id).select():
        point= db(db.profile.user_id == auth.user_id).select().first()
        moredetails=SQLFORM(db.profile ,point.id, showid=False, submit_button="Update" ).process()
    else:
        moredetails=SQLFORM(db.profile).process()
    return locals()
