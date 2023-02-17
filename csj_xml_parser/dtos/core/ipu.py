"""_summary_

Returns:
    _type_: _description_
"""

from .luw import DtoLuw


class DtoIpu:
    """_summary_
    ipuタグの要素
    """

    def __init__(
        self,
        channel: str,
        ipu_end_time: float,
        ipu_id: int,
        ipu_start_time: float,
        luws: list[DtoLuw],
    ):
        self.channel: str = channel
        self.ipu_end_time: float = ipu_end_time
        self.ipu_id: int = ipu_id
        self.ipu_start_time: float = ipu_start_time
        self.luws: list[DtoLuw] = luws

    def to_list(self):
        """_summary_
            listにして表示する
        Returns:
            _type_: _description_
        """
        return [
            self.channel,
            self.ipu_end_time,
            self.ipu_id,
            self.ipu_start_time,
            [luw.to_list() for luw in self.luws],
        ]

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
