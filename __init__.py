from mycroft import MycroftSkill, intent_file_handler


class CourseworkSelection(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('selection.coursework.intent')
    def handle_selection_coursework(self, message):
        self.speak_dialog('selection.coursework')


def create_skill():
    return CourseworkSelection()

