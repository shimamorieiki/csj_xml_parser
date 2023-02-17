"""_summary_"""

from .suw import DtoSuwCore


class DtoLuw:
    """_summary_
    suwタグの要素
    """

    def __init__(
        self,
        is_new_line: int | None,
        luw_dictionary_form: str | None,
        luw_id: int | None,
        luw_lemma: str | None,
        luw_misc_pos_info_1: str | None,
        luw_pos: str | None,
        line_id: str | None,
        suws: list[DtoSuwCore],
    ):
        self.is_new_line: int | None = is_new_line
        self.luw_dictionary_form: str | None = luw_dictionary_form
        self.luw_id: int | None = luw_id
        self.luw_lemma: str | None = luw_lemma
        self.luw_misc_pos_info_1: str | None = luw_misc_pos_info_1
        self.luw_pos: str | None = luw_pos
        self.line_id: str | None = line_id
        self.suws: list[DtoSuwCore] = suws

    def to_list(self):
        """_summary_
            listにして表示する
        Returns:
            _type_: _description_
        """
        return [
            self.is_new_line,
            self.luw_dictionary_form,
            self.luw_id,
            self.luw_lemma,
            self.luw_misc_pos_info_1,
            self.luw_pos,
            self.line_id,
            [suw.to_list() for suw in self.suws],
        ]

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
