"""[summary]
Returns:
    [type]: [description]
"""


from xml.etree.ElementTree import Element

from ...dtos.core.luw import DtoLuwCore
from ...dtos.core.suw import DtoSuwCore
from .base import DaoBase
from .suw import DaoSuwCore


class DaoLuw(DaoBase):
    """[summary]
    CSJのIPU単位を扱うクラス
    """

    def parse(self, luw_element: Element) -> DtoLuwCore:
        """[summary]
        .xmlファイルからsuwのリストを取得する
        Args:
            file (str): xmlファイルのパス
        Returns:
            suw_list (list[str]): suwのリスト
        """
        is_new_line_str: str | None = luw_element.get("IsNewLine")
        luw_dictionary_form: str | None = luw_element.get("LUWDictionaryForm")
        luw_id_str: str | None = luw_element.get("LUWID")
        luw_lemma: str | None = luw_element.get("LUWLemma")
        luw_misc_pos_info_1: str | None = luw_element.get("LUWMiscPOSInfo1")
        luw_pos: str | None = luw_element.get("LUWPOS")
        line_id: str | None = luw_element.get("LineID")

        is_new_line: int | None = (
            int(is_new_line_str, base=10) if is_new_line_str is not None else None
        )

        luw_id: int | None = (
            int(luw_id_str, base=10) if luw_id_str is not None else None
        )

        dao_suw_core: DaoSuwCore = DaoSuwCore()

        suws: list[DtoSuwCore] = [
            dao_suw_core.parse(suw_element=suw_element)
            for suw_element in luw_element.iter("SUW")
        ]

        return DtoLuwCore(
            is_new_line=is_new_line,
            luw_dictionary_form=luw_dictionary_form,
            luw_id=luw_id,
            luw_lemma=luw_lemma,
            luw_misc_pos_info_1=luw_misc_pos_info_1,
            luw_pos=luw_pos,
            line_id=line_id,
            suws=suws,
        )
