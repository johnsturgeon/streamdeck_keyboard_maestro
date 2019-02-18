class KMButtonInstance():
    def __init__(self, context):
        self.context = context
        self.settings = {}

    def macroUUID(self):
        return self.settings['macroUUID']
