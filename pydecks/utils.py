import uuid
from typing import Union


class Sequence:
    def __init__(self, card_sequence: Union[str, int]):
        self.letters = "123456789acefghijkoqrsuvwxyz"
        self.start_val = 28 * 29 - 1
        self.implicit_zero = True
        self.letter_to_index = {
            letter: index for index, letter in enumerate(self.letters)
        }
        self.length = len(self.letters)

        if isinstance(card_sequence, str):
            self.string = self.id = card_sequence
            self.int = self.sequence = self._seq_to_int(card_sequence)
        elif isinstance(card_sequence, int):
            self.int = self.sequence = card_sequence
            self.string = self.id = self._int_to_seq(card_sequence)

    def _int_to_seq(self, int_val):
        seq = []
        q = int_val + self.start_val
        if self.implicit_zero:
            q += 1

        while q:
            if self.implicit_zero:
                q -= 1
            r = q % self.length
            q = q // self.length
            seq.insert(0, self.letters[r])

        return "".join(seq)

    def _seq_to_int(self, seq):
        int_val = self.letter_to_index.get(seq[0], 0)
        for char in seq[1:]:
            if self.implicit_zero:
                int_val += 1
            int_val = int_val * self.length + self.letter_to_index[char]
        return int_val - self.start_val

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"Sequence(accountSeq: {self.int} id: '${self.string}')"


def generate_url(
    subdomain: str, card_title: str, account_seq: Union[Sequence, str, int]
) -> str:
    if isinstance(account_seq, (str, int)):
        account_seq = Sequence(account_seq)
    return f"https://{subdomain}.codecks.io/card/{account_seq}-{card_title.replace(' ', '-')}"


def pascalize(string: str) -> str:
    return string[0].upper() + string[1:]


def is_valid_uuid(s: str) -> bool:
    try:
        uuid.UUID(s)
    except ValueError:
        return False
    return True
