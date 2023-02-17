"""[summary]
Returns:
    [type]: [description]
"""
from xml.etree.ElementTree import Element

from ...dtos.core.mora import DtoMora
from .base import DaoBase


class DaoMora(DaoBase):
    """[summary]
    CSJのMora単位を扱うクラス
    """

    def parse(self, mora_element: Element) -> DtoMora:
        """[summary]
        .xmlファイルからsuwのリストを取得する
        Args:
            file (str): xmlファイルのパス
        Returns:
            suw_list (list[str]): suwのリスト
        """
        mora_entity: str | None = mora_element.get("MoraEntity")
        mora_id: str | None = mora_element.get("MoraID")

        if mora_entity is None or mora_id is None:
            raise ValueError("mora value can't be None")

        return DtoMora(
            mora_entity=mora_entity,
            mora_id=int(mora_id),
        )
