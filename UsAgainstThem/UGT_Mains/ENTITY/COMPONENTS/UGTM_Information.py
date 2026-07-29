from UGT_Utilities.UGTM_GlobalImports import dataclass

# Genders Male, Female, Non-Binary
# M, F, B
# Maybe i should add more in the future!

@dataclass
class cUGT_Information:
    i_FirstName : str = ""
    i_LastName : str = ""
    i_NickName : str = ""
    i_Gender : str = "B"
    
    