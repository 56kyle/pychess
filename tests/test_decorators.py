
from chess.decorators import callback


def test_callback_with_no_before_and_no_after():
    @callback
    def example():
        pass
    example()


def test_callback_with_before_and_no_after():
    before_ran = False

    def before_example():
        before_ran = True

    @callback(before=before_example)
    def example(foo: int):
        assert before_ran



