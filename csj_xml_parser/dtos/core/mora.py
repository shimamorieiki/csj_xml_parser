"""_summary_"""


class DtoMora:
    """_summary_
    moraタグの要素
    """

    def __init__(self, mora_entity: str, mora_id: int):
        self.mora_entity: str = mora_entity
        self.mora_id: int = mora_id

    def to_list(self):
        """_summary_
            listにして表示する
        Returns:
            _type_: _description_
        """
        return [
            self.mora_entity,
            self.mora_id,
        ]

    def set_dummy_data(self):
        """_summary_
        適当なデータをセットする
        """
        self.mora_entity = ""
        self.mora_id = -1

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
