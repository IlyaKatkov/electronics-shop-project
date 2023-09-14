class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = "Ôאיכ ןמגנוזה¸ם"
