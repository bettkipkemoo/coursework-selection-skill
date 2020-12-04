from mycroft.skills.context import adds_context, removes_context

class Courseworkselection(MycroftSkill):
    @intent_handler(IntentBuilder('CourseIntent').require("CourseKeyword"))
    @adds_context('SpringContext')
    def handle_course_intent(self, message):
        self.spring = False
        self.speak('Yes, 32 courses are offered in spring semester?',
                   expect_response=True)

    @intent_handler(IntentBuilder('NoSpringIntent').require("NoKeyword").
                                  require('SpringContext').build())
    @removes_context('SpringContext')
    @adds_context('RegisterContext')
    def handle_no_spring_intent(self, message):
        self.speak('You can register online or visit campus admin for assistance', expect_response=True)

    @intent_handler(IntentBuilder('YesSpringIntent').require("YesKeyword").
                                  require('SpringContext').build())
    @removes_context('SpringContext')
    @adds_context('RegisterContext')
    def handle_yes_spring_intent(self, message):
        self.spring = True
        self.speak('August', expect_response=True)

    @intent_handler(IntentBuilder('NoRegisterIntent').require("NoKeyword").
                                  require('RegisterContext').build())
    @removes_context('RegisterContext')
    def handle_no_register_intent(self, message):
        if self.spring:
            self.speak('Science and art courses are offered')
        else:
            self.speak('A pass in Maths, and/or Physics')

    @intent_handler(IntentBuilder('YesRegisterIntent').require("YesKeyword").
                                require('RegisterContext').build())
    @removes_context('RegisterContext')
    def handle_yes_register_intent(self, message):
        if self.spring:
            self.speak('Yes, computer programming is offered in spring, you can register')
        else:
            self.speak('Come along with a PC and an iPad')
