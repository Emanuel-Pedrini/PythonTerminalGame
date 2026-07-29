_StartBreak : int = 87
_Curve : float = 2.443
_CurveMult : float = 0.19
_StepMult : float = 106.5
_InitialStep : int = 300
_LevelBreak : int = 50
_LevelBreakMult : float = 1.047
_LevelUniversalDivisor : float = 9.2

def _Initial(Param_Level : int) -> float:
    return float((Param_Level ** 1.89) / 50) + ((Param_Level ** _Curve) * _CurveMult) - _StartBreak

def _ExperienceNeeded(Param_Level : int) -> int:
    _Exp = int(_Initial(Param_Level) + _StepMult * Param_Level) + _InitialStep
    if Param_Level > _LevelBreak:
        _Exp **= _LevelBreakMult
    return int(_Exp / _LevelUniversalDivisor)

if __name__ == "__main__":
    for i in range(1, 60, 1):
        print(f"Lv {i} :{_ExperienceNeeded(i)}")