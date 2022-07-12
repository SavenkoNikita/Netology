import Secret_data


class API_VK:
    def __init__(self):
        self.url = 'https://api.vk.com/method/'
        self.method = 'groups.getById'
        self.params = {
            'access_token': Secret_data.VK_token,
            'v': '5.131',
            'group_ids': target_group_ids,
            'fields': 'members_count,activity,description'
        }
