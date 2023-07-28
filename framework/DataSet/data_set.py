class DataSet:

    def __init__(self):
        self.user_types_dict = {'admin': 'Admin AutoUser',
                                'user': 'User User',
                                }

    @property
    def admin_name(self):
        return self.user_types_dict['admin']

    @property
    def user_name(self):
        return self.user_types_dict['user']
