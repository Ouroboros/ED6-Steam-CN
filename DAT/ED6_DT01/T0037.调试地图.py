from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0037   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '00320王国军士兵待机',                  # 9
        '00321王国军士兵移动',                  # 10
        '00322王国军士兵攻击',                  # 11
        '00323王国军士兵挨打',                  # 12
        '00324王国军士兵倒下',                  # 13
        '00325王国军士兵魔法咏唱',              # 14
        '00328王国军士兵魔法发动',              # 15
        '00330王国军军官待机',                  # 16
        '00331王国军军官移动',                  # 17
        '00332王国军军官攻击',                  # 18
        '00333王国军军官挨打',                  # 19
        '00334王国军军官倒下',                  # 20
        '00335王国军军官魔法咏唱',              # 21
        '00338王国军军官魔法发动',              # 22
        '00340特务兵待机',                      # 23
        '00341特务兵移动',                      # 24
        '00342特务兵攻击',                      # 25
        '00343特务兵挨打',                      # 26
        '00344特务兵倒下',                      # 27
        '00345特务兵魔法咏唱',                  # 28
        '00348特务兵魔法发动',                  # 29
        '00260洛伦斯待机',                      # 30
        '00261洛伦斯移动',                      # 31
        '00262洛伦斯攻击',                      # 32
        '00263洛伦斯挨打',                      # 33
        '00264洛伦斯倒下',                      # 34
        '00265洛伦斯魔法咏唱',                  # 35
        '00268洛伦斯魔法发动',                  # 36
        '00270理查德上校待机',                  # 37
        '00271理查德上校移动',                  # 38
        '00272理查德上校攻击',                  # 39
        '00273理查德上校挨打',                  # 40
        '00274理查德上校倒下',                  # 41
        '00275理查德上校魔法咏唱',              # 42
        '00276理查德上校魔法发动',              # 43
        '00280凯诺娜上尉待机',                  # 44
        '00281凯诺娜上尉移动',                  # 45
        '00282凯诺娜上尉攻击',                  # 46
        '00283凯诺娜上尉挨打',                  # 47
        '00284凯诺娜上尉倒下',                  # 48
        '00285凯诺娜上尉魔法咏唱',              # 49
        '00288凯诺娜上尉魔法发动',              # 50
        '00430王国军军官Ｂ待机',                # 51
        '00431王国军军官Ｂ移动',                # 52
        '00432王国军军官Ｂ攻击',                # 53
        '00433王国军军官Ｂ挨打',                # 54
        '00434王国军军官Ｂ倒下',                # 55
        '00435王国军军官Ｂ魔法咏唱',            # 56
        '00438王国军军官Ｂ魔法发动',            # 57
        '00440特务兵Ｂ待机',                    # 58
        '00441特务兵Ｂ移动',                    # 59
        '00442特务兵Ｂ攻击',                    # 60
        '00443特务兵Ｂ挨打',                    # 61
        '00444特务兵Ｂ倒下',                    # 62
        '00445特务兵Ｂ魔法咏唱',                # 63
        '00448特务兵Ｂ魔法发动',                # 64
        '00500特务兵Ｃ中隊長待机',              # 65
        '00501特务兵Ｃ中隊長移动',              # 66
        '00502特务兵Ｃ中隊長攻击',              # 67
        '00503特务兵Ｃ中隊長挨打',              # 68
        '00504特务兵Ｃ中隊長倒下',              # 69
        '00505特务兵Ｃ中隊長魔法咏唱',          # 70
        '00508特务兵Ｃ中隊長魔法发动',          # 71
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00320 ._CH',             # 00
        'ED6_DT07/CH00321 ._CH',             # 01
        'ED6_DT07/CH00322 ._CH',             # 02
        'ED6_DT07/CH00323 ._CH',             # 03
        'ED6_DT07/CH00324 ._CH',             # 04
        'ED6_DT07/CH00320 ._CH',             # 05
        'ED6_DT07/CH00326 ._CH',             # 06
        'ED6_DT07/CH00330 ._CH',             # 07
        'ED6_DT07/CH00331 ._CH',             # 08
        'ED6_DT07/CH00332 ._CH',             # 09
        'ED6_DT07/CH00333 ._CH',             # 0A
        'ED6_DT07/CH00334 ._CH',             # 0B
        'ED6_DT07/CH00335 ._CH',             # 0C
        'ED6_DT07/CH00336 ._CH',             # 0D
        'ED6_DT07/CH00340 ._CH',             # 0E
        'ED6_DT07/CH00341 ._CH',             # 0F
        'ED6_DT07/CH00342 ._CH',             # 10
        'ED6_DT07/CH00343 ._CH',             # 11
        'ED6_DT07/CH00344 ._CH',             # 12
        'ED6_DT07/CH00345 ._CH',             # 13
        'ED6_DT07/CH00346 ._CH',             # 14
        'ED6_DT07/CH00260 ._CH',             # 15
        'ED6_DT07/CH00261 ._CH',             # 16
        'ED6_DT07/CH00262 ._CH',             # 17
        'ED6_DT07/CH00263 ._CH',             # 18
        'ED6_DT07/CH00264 ._CH',             # 19
        'ED6_DT07/CH00265 ._CH',             # 1A
        'ED6_DT07/CH00266 ._CH',             # 1B
        'ED6_DT07/CH00270 ._CH',             # 1C
        'ED6_DT07/CH00271 ._CH',             # 1D
        'ED6_DT07/CH00272 ._CH',             # 1E
        'ED6_DT07/CH00273 ._CH',             # 1F
        'ED6_DT07/CH00274 ._CH',             # 20
        'ED6_DT07/CH00275 ._CH',             # 21
        'ED6_DT07/CH00276 ._CH',             # 22
        'ED6_DT07/CH00280 ._CH',             # 23
        'ED6_DT07/CH00281 ._CH',             # 24
        'ED6_DT07/CH00282 ._CH',             # 25
        'ED6_DT07/CH00283 ._CH',             # 26
        'ED6_DT07/CH00284 ._CH',             # 27
        'ED6_DT07/CH00285 ._CH',             # 28
        'ED6_DT07/CH00286 ._CH',             # 29
        'ED6_DT07/CH00430 ._CH',             # 2A
        'ED6_DT07/CH00431 ._CH',             # 2B
        'ED6_DT07/CH00432 ._CH',             # 2C
        'ED6_DT07/CH00433 ._CH',             # 2D
        'ED6_DT07/CH00434 ._CH',             # 2E
        'ED6_DT07/CH00435 ._CH',             # 2F
        'ED6_DT07/CH00436 ._CH',             # 30
        'ED6_DT07/CH00440 ._CH',             # 31
        'ED6_DT07/CH00441 ._CH',             # 32
        'ED6_DT07/CH00442 ._CH',             # 33
        'ED6_DT07/CH00443 ._CH',             # 34
        'ED6_DT07/CH00444 ._CH',             # 35
        'ED6_DT07/CH00445 ._CH',             # 36
        'ED6_DT07/CH00446 ._CH',             # 37
        'ED6_DT07/CH00278 ._CH',             # 38
        'ED6_DT07/CH00500 ._CH',             # 39
        'ED6_DT07/CH00501 ._CH',             # 3A
        'ED6_DT07/CH00502 ._CH',             # 3B
        'ED6_DT07/CH00503 ._CH',             # 3C
        'ED6_DT07/CH00504 ._CH',             # 3D
        'ED6_DT07/CH00505 ._CH',             # 3E
        'ED6_DT07/CH00506 ._CH',             # 3F
    )

    AddCharChipPat(
        'ED6_DT07/CH00320P._CP',             # 00
        'ED6_DT07/CH00321P._CP',             # 01
        'ED6_DT07/CH00322P._CP',             # 02
        'ED6_DT07/CH00323P._CP',             # 03
        'ED6_DT07/CH00324P._CP',             # 04
        'ED6_DT07/CH00320P._CP',             # 05
        'ED6_DT07/CH00326P._CP',             # 06
        'ED6_DT07/CH00330P._CP',             # 07
        'ED6_DT07/CH00331P._CP',             # 08
        'ED6_DT07/CH00332P._CP',             # 09
        'ED6_DT07/CH00333P._CP',             # 0A
        'ED6_DT07/CH00334P._CP',             # 0B
        'ED6_DT07/CH00335P._CP',             # 0C
        'ED6_DT07/CH00336P._CP',             # 0D
        'ED6_DT07/CH00340P._CP',             # 0E
        'ED6_DT07/CH00341P._CP',             # 0F
        'ED6_DT07/CH00342P._CP',             # 10
        'ED6_DT07/CH00343P._CP',             # 11
        'ED6_DT07/CH00344P._CP',             # 12
        'ED6_DT07/CH00345P._CP',             # 13
        'ED6_DT07/CH00346P._CP',             # 14
        'ED6_DT07/CH00260P._CP',             # 15
        'ED6_DT07/CH00261P._CP',             # 16
        'ED6_DT07/CH00262P._CP',             # 17
        'ED6_DT07/CH00263P._CP',             # 18
        'ED6_DT07/CH00264P._CP',             # 19
        'ED6_DT07/CH00265P._CP',             # 1A
        'ED6_DT07/CH00266P._CP',             # 1B
        'ED6_DT07/CH00270P._CP',             # 1C
        'ED6_DT07/CH00271P._CP',             # 1D
        'ED6_DT07/CH00272P._CP',             # 1E
        'ED6_DT07/CH00273P._CP',             # 1F
        'ED6_DT07/CH00274P._CP',             # 20
        'ED6_DT07/CH00275P._CP',             # 21
        'ED6_DT07/CH00276P._CP',             # 22
        'ED6_DT07/CH00280P._CP',             # 23
        'ED6_DT07/CH00281P._CP',             # 24
        'ED6_DT07/CH00282P._CP',             # 25
        'ED6_DT07/CH00283P._CP',             # 26
        'ED6_DT07/CH00284P._CP',             # 27
        'ED6_DT07/CH00285P._CP',             # 28
        'ED6_DT07/CH00286P._CP',             # 29
        'ED6_DT07/CH00430P._CP',             # 2A
        'ED6_DT07/CH00431P._CP',             # 2B
        'ED6_DT07/CH00432P._CP',             # 2C
        'ED6_DT07/CH00433P._CP',             # 2D
        'ED6_DT07/CH00434P._CP',             # 2E
        'ED6_DT07/CH00435P._CP',             # 2F
        'ED6_DT07/CH00436P._CP',             # 30
        'ED6_DT07/CH00440P._CP',             # 31
        'ED6_DT07/CH00441P._CP',             # 32
        'ED6_DT07/CH00442P._CP',             # 33
        'ED6_DT07/CH00443P._CP',             # 34
        'ED6_DT07/CH00444P._CP',             # 35
        'ED6_DT07/CH00445P._CP',             # 36
        'ED6_DT07/CH00446P._CP',             # 37
        'ED6_DT07/CH00278P._CP',             # 38
        'ED6_DT07/CH00500P._CP',             # 39
        'ED6_DT07/CH00501P._CP',             # 3A
        'ED6_DT07/CH00502P._CP',             # 3B
        'ED6_DT07/CH00503P._CP',             # 3C
        'ED6_DT07/CH00504P._CP',             # 3D
        'ED6_DT07/CH00505P._CP',             # 3E
        'ED6_DT07/CH00506P._CP',             # 3F
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 16,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 17,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 18,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 20,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 21,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 22,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 23,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 52,
        ChipIndex           = 0x34,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 53,
        ChipIndex           = 0x35,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 54,
        ChipIndex           = 0x36,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 24,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 25,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 57,
        ChipIndex           = 0x39,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 58,
        ChipIndex           = 0x3A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 59,
        ChipIndex           = 0x3B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 60,
        ChipIndex           = 0x3C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 61,
        ChipIndex           = 0x3D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 62,
        ChipIndex           = 0x3E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 26,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 36000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 63,
        ChipIndex           = 0x3F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 27,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )


    ScpFunction(
        "Function_0_A8A",          # 00, 0
        "Function_1_A8B",          # 01, 1
        "Function_2_A8C",          # 02, 2
        "Function_3_AA2",          # 03, 3
        "Function_4_AB8",          # 04, 4
        "Function_5_AD3",          # 05, 5
        "Function_6_AEE",          # 06, 6
        "Function_7_B09",          # 07, 7
        "Function_8_B24",          # 08, 8
        "Function_9_B48",          # 09, 9
        "Function_10_B5E",         # 0A, 10
        "Function_11_B87",         # 0B, 11
        "Function_12_B9D",         # 0C, 12
        "Function_13_BD4",         # 0D, 13
        "Function_14_BEA",         # 0E, 14
        "Function_15_C21",         # 0F, 15
        "Function_16_C37",         # 10, 16
        "Function_17_C6E",         # 11, 17
        "Function_18_C84",         # 12, 18
        "Function_19_CBB",         # 13, 19
        "Function_20_CD1",         # 14, 20
        "Function_21_CE7",         # 15, 21
        "Function_22_D1E",         # 16, 22
        "Function_23_D34",         # 17, 23
        "Function_24_D6B",         # 18, 24
        "Function_25_D81",         # 19, 25
        "Function_26_DB8",         # 1A, 26
        "Function_27_DCE",         # 1B, 27
        "Function_28_E05",         # 1C, 28
    )


    def Function_0_A8A(): pass

    label("Function_0_A8A")

    Return()

    # Function_0_A8A end

    def Function_1_A8B(): pass

    label("Function_1_A8B")

    Return()

    # Function_1_A8B end

    def Function_2_A8C(): pass

    label("Function_2_A8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA1")
    OP_99(0xFE, 0x0, 0x7, 0x9C4)
    Jump("Function_2_A8C")

    label("loc_AA1")

    Return()

    # Function_2_A8C end

    def Function_3_AA2(): pass

    label("Function_3_AA2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB7")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_3_AA2")

    label("loc_AB7")

    Return()

    # Function_3_AA2 end

    def Function_4_AB8(): pass

    label("Function_4_AB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AD2")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Sleep(500)
    Jump("Function_4_AB8")

    label("loc_AD2")

    Return()

    # Function_4_AB8 end

    def Function_5_AD3(): pass

    label("Function_5_AD3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AED")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Sleep(500)
    Jump("Function_5_AD3")

    label("loc_AED")

    Return()

    # Function_5_AD3 end

    def Function_6_AEE(): pass

    label("Function_6_AEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B08")
    OP_99(0xFE, 0x0, 0x7, 0x578)
    Sleep(500)
    Jump("Function_6_AEE")

    label("loc_B08")

    Return()

    # Function_6_AEE end

    def Function_7_B09(): pass

    label("Function_7_B09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B23")
    OP_99(0xFE, 0x0, 0xB, 0x960)
    Sleep(500)
    Jump("Function_7_B09")

    label("loc_B23")

    Return()

    # Function_7_B09 end

    def Function_8_B24(): pass

    label("Function_8_B24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B47")
    OP_8D(0xFE, 4000, 20000, 24000, 28000, 1500)
    Jump("Function_8_B24")

    label("loc_B47")

    Return()

    # Function_8_B24 end

    def Function_9_B48(): pass

    label("Function_9_B48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5D")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_9_B48")

    label("loc_B5D")

    Return()

    # Function_9_B48 end

    def Function_10_B5E(): pass

    label("Function_10_B5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B86")
    SetChrChipByIndex(0xFE, 0)
    OP_99(0xFE, 0x0, 0x7, 0x9C4)
    SetChrChipByIndex(0xFE, 6)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_10_B5E")

    label("loc_B86")

    Return()

    # Function_10_B5E end

    def Function_11_B87(): pass

    label("Function_11_B87")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9C")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_11_B87")

    label("loc_B9C")

    Return()

    # Function_11_B87 end

    def Function_12_B9D(): pass

    label("Function_12_B9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BD3")
    SetChrChipByIndex(0xFE, 12)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 13)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_12_B9D")

    label("loc_BD3")

    Return()

    # Function_12_B9D end

    def Function_13_BD4(): pass

    label("Function_13_BD4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE9")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_13_BD4")

    label("loc_BE9")

    Return()

    # Function_13_BD4 end

    def Function_14_BEA(): pass

    label("Function_14_BEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C20")
    SetChrChipByIndex(0xFE, 19)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 20)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_14_BEA")

    label("loc_C20")

    Return()

    # Function_14_BEA end

    def Function_15_C21(): pass

    label("Function_15_C21")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C36")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_15_C21")

    label("loc_C36")

    Return()

    # Function_15_C21 end

    def Function_16_C37(): pass

    label("Function_16_C37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C6D")
    SetChrChipByIndex(0xFE, 26)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 27)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_16_C37")

    label("loc_C6D")

    Return()

    # Function_16_C37 end

    def Function_17_C6E(): pass

    label("Function_17_C6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C83")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_17_C6E")

    label("loc_C83")

    Return()

    # Function_17_C6E end

    def Function_18_C84(): pass

    label("Function_18_C84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CBA")
    SetChrChipByIndex(0xFE, 33)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 34)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_18_C84")

    label("loc_CBA")

    Return()

    # Function_18_C84 end

    def Function_19_CBB(): pass

    label("Function_19_CBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CD0")
    OP_99(0xFE, 0x0, 0xB, 0x3E8)
    Jump("Function_19_CBB")

    label("loc_CD0")

    Return()

    # Function_19_CBB end

    def Function_20_CD1(): pass

    label("Function_20_CD1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CE6")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_20_CD1")

    label("loc_CE6")

    Return()

    # Function_20_CD1 end

    def Function_21_CE7(): pass

    label("Function_21_CE7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D1D")
    SetChrChipByIndex(0xFE, 40)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 41)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_21_CE7")

    label("loc_D1D")

    Return()

    # Function_21_CE7 end

    def Function_22_D1E(): pass

    label("Function_22_D1E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D33")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_22_D1E")

    label("loc_D33")

    Return()

    # Function_22_D1E end

    def Function_23_D34(): pass

    label("Function_23_D34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D6A")
    SetChrChipByIndex(0xFE, 47)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 48)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_23_D34")

    label("loc_D6A")

    Return()

    # Function_23_D34 end

    def Function_24_D6B(): pass

    label("Function_24_D6B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D80")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_24_D6B")

    label("loc_D80")

    Return()

    # Function_24_D6B end

    def Function_25_D81(): pass

    label("Function_25_D81")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DB7")
    SetChrChipByIndex(0xFE, 54)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 55)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_25_D81")

    label("loc_DB7")

    Return()

    # Function_25_D81 end

    def Function_26_DB8(): pass

    label("Function_26_DB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DCD")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_26_DB8")

    label("loc_DCD")

    Return()

    # Function_26_DB8 end

    def Function_27_DCE(): pass

    label("Function_27_DCE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E04")
    SetChrChipByIndex(0xFE, 62)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 63)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_27_DCE")

    label("loc_E04")

    Return()

    # Function_27_DCE end

    def Function_28_E05(): pass

    label("Function_28_E05")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "喝～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_E05 end

    SaveToFile()

Try(main)
