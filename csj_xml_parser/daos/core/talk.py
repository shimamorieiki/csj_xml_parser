"""[summary]
Returns:
    [type]: [description]
"""

from xml.etree.ElementTree import Element

from ...dtos.core.ipu import DtoIpu
from ...dtos.core.talk import DtoTalk
from ...dtos.core.talk_comment import DtoTalkComment
from .base import DaoBase
from .ipu import DaoIpu
from .talk_comment import DaoTalkComment


class DaoTalk(DaoBase):
    """[summary]
    CSJのIPU単位を扱うクラス
    """

    def parse(self, talk_element: Element) -> DtoTalk:
        """[summary]
        .xmlファイルからsuwのリストを取得する
        Args:
            file (str): xmlファイルのパス
        Returns:
            suw_list (list[str]): suwのリスト
        """

        speaker_birth_generation: str | None = talk_element.get(
            "SpeakerBirthGeneration"
        )
        speaker_birth_place: str | None = talk_element.get("SpeakerBirthPlace")
        speaker_id_str: str | None = talk_element.get("SpeakerID")
        speaker_sex: str | None = talk_element.get("SpeakerSex")
        talk_id: str | None = talk_element.get("TalkID")

        if (
            speaker_birth_generation is None
            or speaker_birth_place is None
            or speaker_id_str is None
            or speaker_sex is None
            or talk_id is None
        ):
            raise ValueError("can't find talk")

        dao_ipu: DaoIpu = DaoIpu()

        ipus: list[DtoIpu] = [
            dao_ipu.parse(ipu_element=ipu_element)
            for ipu_element in talk_element.iter("IPU")
        ]

        dao_talk_comment: DaoTalkComment = DaoTalkComment()
        talk_comment_elements: list[Element] = list(talk_element.iter("TalkComment"))
        if len(talk_comment_elements) != 1:
            raise ValueError("can't find TalkComment")

        talk_comment: DtoTalkComment = dao_talk_comment.parse(
            talk_comment_element=talk_comment_elements[0]
        )

        return DtoTalk(
            speaker_birth_generation=speaker_birth_generation,
            speaker_birth_place=speaker_birth_place,
            speaker_id=int(speaker_id_str, base=10),
            speaker_sex=speaker_sex,
            talk_id=talk_id,
            talk_comment=talk_comment,
            ipus=ipus,
        )
