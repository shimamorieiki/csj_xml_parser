"""_summary_"""

from .mora import DtoMora


class DtoTransSuw:
    """_summary_
    suwタグの要素
    """

    def __init__(
        self,
        tag_filler_end: int | None,
        tag_filler_start: int | None,
        tag_mask_midst: int | None,
        trans_suw_id: int,
        moras: list[DtoMora],
    ):
        self.tag_filler_end: int | None = tag_filler_end
        self.tag_filler_start: int | None = tag_filler_start
        self.tag_mask_midst: int | None = tag_mask_midst
        self.trans_suw_id: int = trans_suw_id
        self.moras: list[DtoMora] = moras

    def to_list(self):
        """_summary_
            listにして表示する
        Returns:
            _type_: _description_
        """
        return [
            self.tag_filler_end,
            self.tag_filler_start,
            self.tag_mask_midst,
            self.trans_suw_id,
            [mora.to_list() for mora in self.moras]
        ]

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
