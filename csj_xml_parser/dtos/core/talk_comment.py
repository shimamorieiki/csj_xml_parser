"""_summary_

Returns:
    _type_: _description_
"""
from .comment import DtoComment


class DtoTalkComment:
    """_summary_
    ipuタグの要素
    """

    def __init__(self, comment: DtoComment):
        self.comment: DtoComment = comment

    def to_list(self):
        """_summary_
            listにして表示する
        Returns:
            _type_: _description_
        """
        return [self.comment]

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
