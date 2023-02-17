"""[summary]
Returns:
    [type]: [description]
"""


from xml.etree.ElementTree import Element

from ...dtos.core.suw import DtoSuwCore
from ...dtos.core.trans_suw import DtoTransSuw
from .base import DaoBase
from .trans_suw import DaoTransSuw


class DaoSuwCore(DaoBase):
    """[summary]
    CSJのIPU単位を扱うクラス
    """

    def parse(self, suw_element: Element) -> DtoSuwCore:
        """[summary]
        .xmlファイルからsuwのリストを取得する
        Args:
            file (str): xmlファイルのパス
        Returns:
            suw_list (list[str]): suwのリスト
        """
        suw_id_str: str | None = suw_element.get("SUWID")
        column_id_str: str | None = suw_element.get("ColumnID")
        dictionary_form: str | None = suw_element.get("SUWDictionaryForm")
        lemma: str | None = suw_element.get("SUWLemma")
        pos: str | None = suw_element.get("SUWPOS")
        conjugate_type: str | None = suw_element.get("ConjugateType")
        conjugate_type2: str | None = suw_element.get("ConjugateType2")
        conjugate_form: str | None = suw_element.get("ConjugateForm")
        conjugate_form2: str | None = suw_element.get("ConjugateForm2")
        misc_pos_info1: str | None = suw_element.get("SUWMiscPOSInfo1")
        misc_pos_info2: str | None = suw_element.get("SUWMiscPOSInfo2")
        misc_pos_info3: str | None = suw_element.get("SUWMiscPOSInfo3")
        plain_orthographic_transcription: str | None = suw_element.get(
            "PlainOrthographicTranscription"
        )
        orthographic_transcription: str | None = suw_element.get(
            "OrthographicTranscription"
        )
        phonetic_transcription: str | None = suw_element.get("PhoneticTranscription")
        clause_unit_id_str: str | None = suw_element.get("ClauseUnitID")
        clause_boundary_label: str | None = suw_element.get("ClauseBoundaryLabel")
        cu_operation_sign: str | None = suw_element.get("CU_OperationSign")
        cu_pre_bracket: str | None = suw_element.get("CU_PreBracket")
        cu_post_bracket: str | None = suw_element.get("CU_PostBracket")
        cu_obligate_comment: str | None = suw_element.get("CU_ObligateComment")
        dep_bunsetu_unit_id_str: str | None = suw_element.get("Dep_BunsetsuUnitID")
        dep_modifiee_bunsetu_unit_id_str: str | None = suw_element.get(
            "Dep_ModifieeBunsetsuUnitID"
        )
        dep_obligate_comment: str | None = suw_element.get("Dep_obligateComment")
        dep_label: str | None = suw_element.get("Dep_Label")
        trans_suw_elements: list[Element] = list(suw_element.iter("TransSUW"))

        if len(trans_suw_elements) != 1:
            raise ValueError("can't find Suw")

        trans_suw: DtoTransSuw = DaoTransSuw().parse(
            trans_suw_element=trans_suw_elements[0]
        )

        suw_id: int | None = (
            int(suw_id_str, base=10) if suw_id_str is not None else None
        )

        column_id: int | None = (
            int(column_id_str, base=10) if column_id_str is not None else None
        )

        clause_unit_id: int | None = (
            int(clause_unit_id_str, base=10) if clause_unit_id_str is not None else None
        )

        dep_bunsetu_unit_id: int | None = (
            int(dep_bunsetu_unit_id_str, base=10)
            if dep_bunsetu_unit_id_str is not None
            else None
        )
        dep_modifiee_bunsetu_unit_id: int | None = (
            int(dep_modifiee_bunsetu_unit_id_str, base=10)
            if dep_modifiee_bunsetu_unit_id_str is not None
            else None
        )

        return DtoSuwCore(
            suw_id=suw_id,
            column_id=column_id,
            dictionary_form=dictionary_form,
            lemma=lemma,
            pos=pos,
            conjugate_type=conjugate_type,
            conjugate_type2=conjugate_type2,
            conjugate_form=conjugate_form,
            conjugate_form2=conjugate_form2,
            misc_pos_info1=misc_pos_info1,
            misc_pos_info2=misc_pos_info2,
            misc_pos_info3=misc_pos_info3,
            plain_orthographic_transcription=plain_orthographic_transcription,
            orthographic_transcription=orthographic_transcription,
            phonetic_transcription=phonetic_transcription,
            clause_unit_id=clause_unit_id,
            clause_boundary_label=clause_boundary_label,
            cu_operation_sign=cu_operation_sign,
            cu_pre_bracket=cu_pre_bracket,
            cu_post_bracket=cu_post_bracket,
            cu_obligate_comment=cu_obligate_comment,
            dep_bunsetu_unit_id=dep_bunsetu_unit_id,
            dep_modifiee_bunsetu_unit_id=dep_modifiee_bunsetu_unit_id,
            dep_obligate_comment=dep_obligate_comment,
            dep_label=dep_label,
            trans_suw=trans_suw,
        )
