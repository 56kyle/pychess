from chess.notation import Notation


class FIDE(Notation):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _get_notation_string(self):
        pass

