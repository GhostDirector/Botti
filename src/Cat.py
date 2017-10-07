class Cat:
    def get_cat(self, command):
        if command == "gif":
            return "https://www.catgifpage.com/"
        if command == "doge":
            return "http://bit.ly/2yO593Z"
        if command == "wizard":
            return "https://youtu.be/PGpQk2cW494/"
        if command == "meow":
            return "https://youtu.be/9EYZnSXEla0/"
        if command == "help":
            return self.commands()
        if command == "random":
            return "http://random.cat/"
        else:
            return "http://random.cat/"

    def commands(self):
        return "gif\ndoge\nwizard\nmeow\nrandom"

    def random_cat(self):
