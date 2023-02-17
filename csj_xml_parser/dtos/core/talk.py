"""_summary_

Returns:
    _type_: _description_
"""

from .ipu import DtoIpu
from .talk_comment import DtoTalkComment


class DtoTalk:
    """_summary_
    ipuタグの要素
    """

    def __init__(
        self,
        speaker_birth_generation: str,
        speaker_birth_place: str,
        speaker_id: int,
        speaker_sex: str,
        talk_id: str,
        talk_comment: DtoTalkComment,
        ipus: list[DtoIpu],
    ):
        self.speaker_birth_generation: str = speaker_birth_generation
        self.speaker_birth_place: str = speaker_birth_place
        self.speaker_id: int = speaker_id
        self.speaker_sex: str = speaker_sex
        self.talk_id: str = talk_id
        self.talk_comment: DtoTalkComment = talk_comment
        self.ipus: list[DtoIpu] = ipus

    def to_list(self):
        """_summary_
            listにして表示する
        Returns:
            _type_: _description_
        """
        return [
            self.speaker_birth_generation,
            self.speaker_birth_place,
            self.speaker_id,
            self.speaker_sex,
            self.talk_id,
            self.talk_comment,
            [ipu.to_list() for ipu in self.ipus],
        ]

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
