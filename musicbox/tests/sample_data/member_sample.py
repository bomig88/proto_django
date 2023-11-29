from member.models.member import Member

def get_register_sample():
    params = dict()
    params['username'] = 'regit1'
    params['password'] = 'test1234'
    params['birthday'] = '20000101'
    params['gender'] = Member.GenderChoice.F.value
    params['email'] = 'bomig88@gmail.com'
    params['tag'] = Member.TagChoice.BASIC_USER.value
    return params

def get_register_simplicity_user_sample():
    params = dict()
    params['username'] = 'regit1'
    params['password'] = 'test1234'
    params['birthday'] = '20000101'
    params['gender'] = Member.GenderChoice.F.value
    params['email'] = 'bomig88@gmail.com'
    params['tag'] = Member.TagChoice.SIMPLICITY_USER.value
    return params

def get_register_manager_sample():
    params = dict()
    params['username'] = 'regit1'
    params['password'] = 'test1234'
    params['birthday'] = '20000101'
    params['gender'] = Member.GenderChoice.F.value
    params['email'] = 'bomig88@gmail.com'
    params['tag'] = Member.TagChoice.MANAGER.value
    return params

def get_register_super_manager_sample():
    params = dict()
    params['username'] = 'regit1'
    params['password'] = 'test1234'
    params['birthday'] = '20000101'
    params['gender'] = Member.GenderChoice.F.value
    params['email'] = 'bomig88@gmail.com'
    params['tag'] = Member.TagChoice.SUPER_MANAGER.value
    return params
