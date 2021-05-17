from mycroft import MycroftSkill, intent_file_handler


class AtividadeFisica(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fisica.atividade.intent')
    def handle_fisica_atividade(self, message):
        self.speak_dialog('fisica.atividade')


def create_skill():
    return AtividadeFisica()

