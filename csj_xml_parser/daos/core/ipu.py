"""[summary]
Returns:
    [type]: [description]
"""

from xml.etree.ElementTree import Element

from ...dtos.core.ipu import DtoIpu
from ...dtos.core.luw import DtoLuw
from .base import DaoBase
from .luw import DaoLuw


class DaoIpu(DaoBase):
    """[summary]
    CSJのIPU単位を扱うクラス
    """

    def parse(self, ipu_element: Element) -> DtoIpu:
        """[summary]
        .xmlファイルからsuwのリストを取得する
        Args:
            file (str): xmlファイルのパス
        Returns:
            suw_list (list[str]): suwのリスト
        """

        channel: str | None = ipu_element.get("Channel")
        ipu_end_time_str: str | None = ipu_element.get("IPUEndTime")
        ipu_id_str: str | None = ipu_element.get("IPUID")
        ipu_start_time_str: str | None = ipu_element.get("IPUStartTime")

        if (
            channel is None
            or ipu_end_time_str is None
            or ipu_id_str is None
            or ipu_start_time_str is None
        ):
            raise ValueError("can't find ipu")

        dao_luw_core: DaoLuw = DaoLuw()

        luws: list[DtoLuw] = [
            dao_luw_core.parse(luw_element=luw_element)
            for luw_element in ipu_element.iter("LUW")
        ]

        return DtoIpu(
            channel=channel,
            ipu_end_time=float(ipu_end_time_str),
            ipu_id=int(ipu_id_str),
            ipu_start_time=float(ipu_start_time_str),
            luws=luws,
        )
