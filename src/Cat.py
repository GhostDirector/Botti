from random import choice


class Cat:
    def __init__(self):
        self.links = ["https://www.catgifpage.com/",
                      "http://bit.ly/2yO593Z",
                      "https://youtu.be/PGpQk2cW494/",
                      "https://youtu.be/9EYZnSXEla0/",
                      "http://random.cat/"]
        self.keys = ["gif", "doge", "wizard", "meow", "random"]

    def get_cat(self, command):
        if command == "help":
            return self.commands()

        for i, key in enumerate(self.keys):
            if key == command:
                return self.links[i]

        return choice(self.links)

    def commands(self):
        return "gif\ndoge\nwizard\nmeow\nrandom"
