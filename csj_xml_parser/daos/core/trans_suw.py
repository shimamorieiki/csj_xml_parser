"""[summary]
Returns:
    [type]: [description]
"""
from xml.etree.ElementTree import Element

from ...dtos.core.mora import DtoMora
from ...dtos.core.trans_suw import DtoTransSuw
from .base import DaoBase
from .mora import DaoMora


class DaoTransSuw(DaoBase):
    """[summary]
    CSJのMora単位を扱うクラス
    """

    def parse(self, trans_suw_element: Element) -> DtoTransSuw:
        """[summary]
        .xmlファイルからsuwのリストを取得する
        Args:
            file (str): xmlファイルのパス
        Returns:
            suw_list (list[str]): suwのリスト
        """
        tag_filler_end_str: str | None = trans_suw_element.get("TagFillerEnd")
        tag_filler_start_str: str | None = trans_suw_element.get("TagFillerStart")
        tag_mask_midst_str: str | None = trans_suw_element.get("TagMaskMidst")
        trans_suw_id_str: str | None = trans_suw_element.get("TransSUWID")
        moras: list[DtoMora] = []

        dao_mora = DaoMora()
        for mora_element in trans_suw_element.iter("Mora"):
            moras.append(dao_mora.parse(mora_element))

        if trans_suw_id_str is None:
            raise ValueError("transSuw value can't be None")

        tag_filler_end: int | None = (
            int(tag_filler_end_str, base=10) if tag_filler_end_str is not None else None
        )
        tag_filler_start: int | None = (
            int(tag_filler_start_str, base=10)
            if tag_filler_start_str is not None
            else None
        )
        tag_mask_midst: int | None = (
            int(tag_mask_midst_str, base=10) if tag_mask_midst_str is not None else None
        )

        return DtoTransSuw(
            tag_filler_end=tag_filler_end,
            tag_filler_start=tag_filler_start,
            tag_mask_midst=tag_mask_midst,
            trans_suw_id=int(trans_suw_id_str),
            moras=moras,
        )
