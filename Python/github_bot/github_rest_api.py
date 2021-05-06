import  requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "Your token"

    def getUser(self,username):
        cevap = requests.get(self.api_url + '/users/'+ username)
        return cevap.json()

    def getRepos(self,username):
        cevap = requests.get(self.api_url+'/users/'+username+'/repos')
        return cevap.json()

    def createRepo(self,name):
        cevap = requests.post(self.api_url+'/user/repos?acces_token='+self.token,json={
            "id": 210581998,
            "node_id": "MDEwOlJlcG9zaXRvcnkyMTA1ODE5OTg=",
            "name": "python-dersleri",
            "full_name": "mahmut/python-dersleri",
            "private": False,
            "owner": {
              "login": "mahmut",
              "id": 19492591,
              "node_id": "MDQ6VXNlcjE5NDkyNTkx",
              "avatar_url": "url",
              "gravatar_id": "",
              "url": "url",
              "html_url": "url",
              "followers_url": "url",
              "following_url": "url",
              "gists_url": "url",
              "starred_url": "url",
              "subscriptions_url": "url",
              "organizations_url": "url",
              "repos_url": "url",
              "events_url": "url",
              "received_events_url": "url",
              "type": "User",
              "site_admin": False
            }})
        return cevap.json()

git = Github()

while True:
    secim = input("1- Find User\n2- Get repositories\n3- Create repository\n4- EXIT\nSeçiminiz: ")
    if secim == '4':
        break
    else:
        if secim == '1':
            username = input("Enter username: ")
            result = git.getUser(username=username)
            print(f"Name: {result['name']} | Location: {result['location']} | Repos: {result['public_repos']} | Followers: {result['followers']}")
        elif secim == '2':
            username = input("Enter username: ")
            result = git.getRepos(username=username)
            for i in result:
                print(i['name'])
        elif secim =='3':
            name = input("Enter repo name: ")
            result = git.createRepo(name)
            print(result)
        else:
            print("Hatalı seçim")