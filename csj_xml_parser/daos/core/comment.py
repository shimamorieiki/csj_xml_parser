"""[summary]
Returns:
    [type]: [description]
"""

from xml.etree.ElementTree import Element

from ...dtos.core.comment import DtoComment
from .base import DaoBase


class DaoComment(DaoBase):
    """[summary]
    CSJのIPU単位を扱うクラス
    """

    def parse(self, comment_element: Element) -> DtoComment:
        """[summary]
        .xmlファイルからsuwのリストを取得する
        Args:
            file (str): xmlファイルのパス
        Returns:
            suw_list (list[str]): suwのリスト
        """
        comment_strings: str | None = comment_element.get("CommentStrings")

        if comment_strings is None:
            raise ValueError("can't find Comment")

        return DtoComment(comment_strings=comment_strings)
