from mycroft import MycroftSkill, intent_file_handler


class Courseworkselection(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('courseworkselection.intent')
    def handle_courseworkselection(self, message):
        self.speak_dialog('courseworkselection')


def create_skill():
    return Courseworkselection()
