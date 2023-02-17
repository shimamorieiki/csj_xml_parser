"""[summary]
Returns:
    [type]: [description]
"""

from xml.etree.ElementTree import Element

from ...dtos.core.comment import DtoComment
from ...dtos.core.talk_comment import DtoTalkComment
from .base import DaoBase
from .comment import DaoComment


class DaoTalkComment(DaoBase):
    """[summary]
    CSJのIPU単位を扱うクラス
    """

    def parse(self, talk_comment_element: Element) -> DtoTalkComment:
        """[summary]
        .xmlファイルからsuwのリストを取得する
        Args:
            file (str): xmlファイルのパス
        Returns:
            suw_list (list[str]): suwのリスト
        """
        dao_comment: DaoComment = DaoComment()
        comment: DtoComment = [
            dao_comment.parse(comment_element=comment_element)
            for comment_element in talk_comment_element.iter("Comment")
        ][0]

        return DtoTalkComment(comment=comment)
