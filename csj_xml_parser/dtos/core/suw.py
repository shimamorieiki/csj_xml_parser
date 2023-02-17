"""_summary_"""

from .trans_suw import DtoTransSuw


class DtoSuwCore:
    """_summary_
    suwタグの要素
    """

    def __init__(
        self,
        suw_id: int | None,
        column_id: int | None,
        dictionary_form: str | None,
        lemma: str | None,
        pos: str | None,
        conjugate_type: str | None,
        conjugate_type2: str | None,
        conjugate_form: str | None,
        conjugate_form2: str | None,
        misc_pos_info1: str | None,
        misc_pos_info2: str | None,
        misc_pos_info3: str | None,
        plain_orthographic_transcription: str | None,
        orthographic_transcription: str | None,
        phonetic_transcription: str | None,
        clause_unit_id: int | None,
        clause_boundary_label: str | None,
        cu_operation_sign: str | None,
        cu_pre_bracket: str | None,
        cu_post_bracket: str | None,
        cu_obligate_comment: str | None,
        dep_bunsetu_unit_id: int | None,
        dep_modifiee_bunsetu_unit_id: int | None,
        dep_obligate_comment: str | None,
        dep_label: str | None,
        trans_suw: DtoTransSuw,
    ):
        self.suw_id: int | None = suw_id
        self.column_id: int | None = column_id
        self.dictionary_form: str | None = dictionary_form
        self.lemma: str | None = lemma
        self.pos: str | None = pos
        self.conjugate_type: str | None = conjugate_type
        self.conjugate_type2: str | None = conjugate_type2
        self.conjugate_form: str | None = conjugate_form
        self.conjugate_form2: str | None = conjugate_form2
        self.misc_pos_info1: str | None = misc_pos_info1
        self.misc_pos_info2: str | None = misc_pos_info2
        self.misc_pos_info3: str | None = misc_pos_info3
        self.plain_orthographic_transcription: str | None = (
            plain_orthographic_transcription
        )
        self.orthographic_transcription: str | None = orthographic_transcription
        self.phonetic_transcription: str | None = phonetic_transcription
        self.clause_unit_id: int | None = clause_unit_id
        self.clause_boundary_label: str | None = clause_boundary_label
        self.cu_operation_sign: str | None = cu_operation_sign
        self.cu_pre_bracket: str | None = cu_pre_bracket
        self.cu_post_bracket: str | None = cu_post_bracket
        self.cu_obligate_comment: str | None = cu_obligate_comment
        self.dep_bunsetu_unit_id: int | None = dep_bunsetu_unit_id
        self.dep_modifiee_bunsetu_unit_id: int | None = dep_modifiee_bunsetu_unit_id
        self.dep_obligate_comment: str | None = dep_obligate_comment
        self.dep_label: str | None = dep_label
        self.trans_suw: DtoTransSuw = trans_suw

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
            self.trans_suw.to_list(),
        ]

    def __str__(self):
        return ", ".join([str(i) for i in self.to_list()])
