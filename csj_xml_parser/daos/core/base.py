"""[summary]
Returns:
    [type]: [description]
"""


class DaoBase:
    """[summary]
    CSJのMora単位を扱うクラス
    """

    def read(self, file_path: str) -> list[str]:
        """[summary]
            ファイルパスのテキストをリストとして取得する
        Args:
            file_path ([type]): [description]
        Returns:
            [type]: [description]
        """ """
        file_path -> list[文]
        """

        with open(file_path, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
        return [line.replace("\n", "") for line in lines if line != "\n"]

    def load_xml(self, file_path: str):
        """_summary_

        Args:
            file_path (str): _description_

        Returns:
            _type_: _description_
        """
        return "".join(self.read(file_path=file_path))
