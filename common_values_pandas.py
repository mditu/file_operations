import pandas as pd
import numpy as np
from pandas import DataFrame
from typing import List, Dict

file_llama = pd.read_csv("/home/mariacristina_ditu_liveramp_com/Kantar/check/PEL_CID_AE_CID_PEL_LiveRamp_FR_NE_Audience_Element_Partie_Link_20210821_NO_EXPANSION_620_20210922.psv", delimiter = "|")
file_redbull = pd.read_csv("/home/mariacristina_ditu_liveramp_com/Kantar/check/model_superb_sansevieria_de0e7760f3088c9bfad102881b3ba28f_audience_meaty_oystercatcher_948e9c386109c7b5fd449ee7978b866a_011. csv")


common = file_llama.merge(file_redbull, on="Customer_Link", how="inner")

common.to_csv("/home/mariacristina_ditu_liveramp_com/Kantar/check/join_pukka_merge.csv", index=False)
