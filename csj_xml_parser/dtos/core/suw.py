"""_summary_

Returns:
    _type_: _description_
"""


class DtoSuwCore:
    """_summary_
    suwタグの要素
    """

    def __init__(self):
        self.suw_id: str = None
        self.column_id: int = None
        self.dictionary_form: str = None
        self.lemma: str = None
        self.pos: str = None
        self.conjugate_type: str = None
        self.conjugate_type2: str = None
        self.conjugate_form: str = None
        self.conjugate_form2: str = None
        self.misc_pos_info1: str = None
        self.misc_pos_info2: str = None
        self.misc_pos_info3: str = None
        self.plain_orthographic_transcription: str = None
        self.orthographic_transcription: str = None
        self.phonetic_transcription: str = None
        self.clause_unit_id: int = None
        self.clause_boundary_label: str = None
        self.cu_operation_sign: str = None
        self.cu_pre_bracket: str = None
        self.cu_post_bracket: str = None
        self.cu_obligate_comment: str = None
        self.dep_bunsetu_unit_id: int = None
        self.dep_modifiee_bunsetu_unit_id: int = None
        self.dep_obligate_comment: str = None
        self.dep_label: str = None
        self.ipu_pause: str = None

    def to_list(self):
        """_summary_
            listにして表示する
        Returns:
            _type_: _description_
        """
        return [
            self.suw_id,
            self.column_id,
            self.dictionary_form,
            self.lemma,
            self.pos,
            self.conjugate_type,
            self.conjugate_type2,
            self.conjugate_form,
            self.conjugate_form2,
            self.misc_pos_info1,
            self.misc_pos_info2,
            self.misc_pos_info3,
            self.plain_orthographic_transcription,
            self.orthographic_transcription,
            self.phonetic_transcription,
            self.clause_unit_id,
            self.clause_boundary_label,
            self.cu_operation_sign,
            self.cu_pre_bracket,
            self.cu_post_bracket,
            self.cu_obligate_comment,
            self.dep_bunsetu_unit_id,
            self.dep_modifiee_bunsetu_unit_id,
            self.dep_obligate_comment,
            self.dep_label,
            self.ipu_pause,
        ]

    def set_dummy_data(self):
        """_summary_
        適当なデータをセットする
        """
        self.suw_id = ""
        self.column_id = 0
        self.dictionary_form = ""
        self.lemma = ""
        self.pos = ""
        self.conjugate_type = ""
        self.conjugate_type2 = ""
        self.conjugate_form = ""
        self.conjugate_form2 = ""
        self.misc_pos_info1 = ""
        self.misc_pos_info2 = ""
        self.misc_pos_info3 = ""
        self.plain_orthographic_transcription = ""
        self.orthographic_transcription = ""
        self.phonetic_transcription = ""
        self.clause_unit_id = 0
        self.clause_boundary_label = ""
        self.cu_operation_sign = ""
        self.cu_pre_bracket = ""
        self.cu_post_bracket = ""
        self.cu_obligate_comment = ""
        self.dep_bunsetu_unit_id = 0
        self.dep_modifiee_bunsetu_unit_id = 0
        self.dep_obligate_comment = ""
        self.dep_label = ""
        self.ipu_pause = ""

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
