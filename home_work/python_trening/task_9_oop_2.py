class Page:
    def __int__(self, url):
        self.url = url
    def __get__(self):
        print(self.url)




home = Page ("https://demoga.com/")
home.get()
