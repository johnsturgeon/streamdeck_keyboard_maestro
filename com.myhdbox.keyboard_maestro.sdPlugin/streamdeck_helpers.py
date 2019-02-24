class KMButtonInstance():
    def __init__(self, context):
        self.context = context
        self.settings = {}

    def macroUUID(self):
        if 'macroUUID' in self.settings:
            return self.settings['macroUUID']
        else:
            return None
