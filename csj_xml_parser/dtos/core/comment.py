"""_summary_

Returns:
    _type_: _description_
"""


class DtoComment:
    """_summary_
    ipuタグの要素
    """

    def __init__(self, comment_strings: str):
        self.comment_strings: str = comment_strings

    def to_list(self):
        """_summary_
            listにして表示する
        Returns:
            _type_: _description_
        """
        return [self.comment_strings]

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
