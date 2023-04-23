from random import randint
from objects import (
    answer_btn,
    result_l,
    question_le
)
from constants import probability


def reset():
    result_l.hide()


def start():
    if len(question_le.text()) > 0:
        alpha: int = base_generator()
        if alpha < probability:
            yes()
        else:
            no()
        result_l.show()


def yes():
    result_l.setText('YES')


def no():
    result_l.setText('NO')


def base_generator() -> int:
    return randint(0, probability * 2)


answer_btn.clicked.connect(start)
question_le.textChanged.connect(reset)
