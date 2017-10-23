# -*- coding: utf-8 -*-
db.define_table('profile',
                Field('user_id', default=auth.user_id,writable=False, readable=False),
                Field('age'),
                Field('dp', 'upload', label='Profile Pic', requires=IS_IMAGE())
)
