"""[summary]
Returns:
    [type]: [description]
"""


import re
import xml.etree.ElementTree as ET

from ...dtos.noncore.suw import DtoSuwNonCore


class DaoIPUNonCore:
    """[summary]
    CSJのIPU単位を扱うクラス
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

    def parse(self, file_path: str) -> list[DtoSuwNonCore]:
        """[summary]
        Args:
            file ([type]): [description]
        Returns:
            [type]: [description]
        """
        suw_list: list[DtoSuwNonCore] = []
        xml_data: str = self.load_xml(file_path=file_path)
        root = ET.fromstring(xml_data)

        for index, ipu in enumerate(root.iter("IPU")):
            if index > 0 and len(suw_list) > 0:
                suw_list[-1].ipu_pause = "pause"

            # 転記単位の時間については
            # file:///home/shimamorieiki/Downloads/kkrep_124.pdf P35(pdfの枚数的には53枚目)
            # あたりから記述がありそれに従う。
            for suw in ipu.iter("SUW"):
                dto_suw: DtoSuwNonCore = DtoSuwNonCore()
                dto_suw.suw_id = suw.get("SUWID", "")
                dto_suw.column_id = suw.get("ColumnID", "")
                dto_suw.dictionary_form = suw.get("SUWDictionaryForm", "")
                dto_suw.lemma = suw.get("SUWLemma", "")
                dto_suw.pos = suw.get("SUWPOS", "")
                dto_suw.conjugate_type = suw.get("ConjugateType", "")
                dto_suw.conjugate_type2 = suw.get("ConjugateType2", "")
                dto_suw.conjugate_form = suw.get("ConjugateForm", "")
                dto_suw.conjugate_form2 = suw.get("ConjugateForm2", "")
                dto_suw.misc_pos_info1 = suw.get("SUWMiscPOSInfo1", "")
                dto_suw.misc_pos_info2 = suw.get("SUWMiscPOSInfo2", "")
                dto_suw.misc_pos_info3 = suw.get("SUWMiscPOSInfo3", "")
                dto_suw.plain_orthographic_transcription = suw.get(
                    "PlainOrthographicTranscription", ""
                )
                dto_suw.orthographic_transcription = suw.get(
                    "OrthographicTranscription", ""
                )
                dto_suw.phonetic_transcription = suw.get("PhoneticTranscription", "")
                dto_suw.clause_unit_id = suw.get("ClauseUnitID", "")
                dto_suw.clause_boundary_label = suw.get("ClauseBoundaryLabel", "")
                dto_suw.cu_operation_sign = suw.get("CU_OperationSign", "")
                dto_suw.cu_pre_bracket = suw.get("CU_PreBracket", "")
                dto_suw.cu_post_bracket = suw.get("CU_PostBracket", "")
                dto_suw.cu_obligate_comment = suw.get("CU_ObligateComment", "")
                dto_suw.dep_bunsetu_unit_id = suw.get("Dep_BunsetsuUnitID", "")
                dto_suw.dep_modifiee_bunsetu_unit_id = suw.get(
                    "Dep_ModifieeBunsetsuUnitID", ""
                )
                dto_suw.dep_obligate_comment = suw.get("Dep_obligateComment", "")
                dto_suw.dep_label = suw.get("Dep_Label", "")
                dto_suw.ipu_pause = ""

                suw_list.append(dto_suw)
        return suw_list

    @staticmethod
    def return_sentence_directly(dto_suws: list[DtoSuwNonCore]) -> list[str]:
        """[summary]
        Args:
            suw_list ([type]): [description]
        Returns:
            [type]: [description]
        """

        def format_label(sentence: str):
            return re.sub(r"&lt;|&gt;|<|>|\[|\]", "/", sentence)

        sentence: str = ""
        sentences: list[str] = []

        for index, _ in enumerate(dto_suws):
            clause_label: str = str(dto_suws[index].clause_boundary_label)
            pause_label: str = str(dto_suws[index].ipu_pause)

            morph = str(dto_suws[index].orthographic_transcription)
            if morph == "<FV>":
                continue

            if clause_label == "[文末]":
                sentence += format_label(morph + clause_label)
                sentences.append(sentence)
                sentence = ""
            elif clause_label != "":
                sentence += format_label(morph + clause_label)
            else:
                sentence += format_label(morph)

            if pause_label == "pause":
                sentence += "/pause/"
        sentences.append(sentence)
        return sentences
