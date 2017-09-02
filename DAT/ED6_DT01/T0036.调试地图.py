from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0036   ._SN',
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
        '00450迪恩待机',                        # 9
        '00451迪恩移动',                        # 10
        '00452迪恩攻击',                        # 11
        '00453迪恩挨打',                        # 12
        '00454迪恩倒下',                        # 13
        '00460雷斯待机',                        # 14
        '00461雷斯移动',                        # 15
        '00462雷斯攻击',                        # 16
        '00463雷斯挨打',                        # 17
        '00464雷斯倒下',                        # 18
        '00470洛克待机',                        # 19
        '00471洛克移动',                        # 20
        '00472洛克攻击',                        # 21
        '00473洛克挨打',                        # 22
        '00474洛克倒下',                        # 23
        '00410男游击士２待机',                  # 24
        '00411男游击士２移动',                  # 25
        '00412男游击士２攻击',                  # 26
        '00413男游击士２挨打',                  # 27
        '00414男游击士２倒下',                  # 28
        '00415男游击士２魔法咏唱',              # 29
        '00418男游击士２魔法发动',              # 30
        '00420女游击士２待机',                  # 31
        '00421女游击士２移动',                  # 32
        '00422女游击士２攻击',                  # 33
        '00423女游击士２挨打',                  # 34
        '00424女游击士２倒下',                  # 35
        '00425女游击士２魔法咏唱',              # 36
        '00428女游击士２魔法发动',              # 37
        '00480洛伦斯待机',                      # 38
        '00481洛伦斯移动',                      # 39
        '00482洛伦斯攻击',                      # 40
        '00483洛伦斯挨打',                      # 41
        '00484洛伦斯倒下',                      # 42
        '00485洛伦斯魔法咏唱',                  # 43
        '00488洛伦斯魔法发动',                  # 44
        '00490男游击士４待机',                  # 45
        '00491男游击士４移动',                  # 46
        '00492男游击士４攻击',                  # 47
        '00493男游击士４挨打',                  # 48
        '00494男游击士４倒下',                  # 49
        '00495男游击士４魔法咏唱',              # 50
        '00498男游击士４魔法发动',              # 51
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
        'ED6_DT07/CH00450 ._CH',             # 00
        'ED6_DT07/CH00451 ._CH',             # 01
        'ED6_DT07/CH00452 ._CH',             # 02
        'ED6_DT07/CH00453 ._CH',             # 03
        'ED6_DT07/CH00454 ._CH',             # 04
        'ED6_DT07/CH00460 ._CH',             # 05
        'ED6_DT07/CH00461 ._CH',             # 06
        'ED6_DT07/CH00462 ._CH',             # 07
        'ED6_DT07/CH00463 ._CH',             # 08
        'ED6_DT07/CH00464 ._CH',             # 09
        'ED6_DT07/CH00470 ._CH',             # 0A
        'ED6_DT07/CH00471 ._CH',             # 0B
        'ED6_DT07/CH00472 ._CH',             # 0C
        'ED6_DT07/CH00473 ._CH',             # 0D
        'ED6_DT07/CH00474 ._CH',             # 0E
        'ED6_DT07/CH00410 ._CH',             # 0F
        'ED6_DT07/CH00411 ._CH',             # 10
        'ED6_DT07/CH00412 ._CH',             # 11
        'ED6_DT07/CH00413 ._CH',             # 12
        'ED6_DT07/CH00414 ._CH',             # 13
        'ED6_DT07/CH00415 ._CH',             # 14
        'ED6_DT07/CH00416 ._CH',             # 15
        'ED6_DT07/CH00420 ._CH',             # 16
        'ED6_DT07/CH00421 ._CH',             # 17
        'ED6_DT07/CH00422 ._CH',             # 18
        'ED6_DT07/CH00423 ._CH',             # 19
        'ED6_DT07/CH00424 ._CH',             # 1A
        'ED6_DT07/CH00425 ._CH',             # 1B
        'ED6_DT07/CH00426 ._CH',             # 1C
        'ED6_DT07/CH00480 ._CH',             # 1D
        'ED6_DT07/CH00481 ._CH',             # 1E
        'ED6_DT07/CH00482 ._CH',             # 1F
        'ED6_DT07/CH00483 ._CH',             # 20
        'ED6_DT07/CH00484 ._CH',             # 21
        'ED6_DT07/CH00485 ._CH',             # 22
        'ED6_DT07/CH00486 ._CH',             # 23
        'ED6_DT07/CH00490 ._CH',             # 24
        'ED6_DT07/CH00491 ._CH',             # 25
        'ED6_DT07/CH00492 ._CH',             # 26
        'ED6_DT07/CH00493 ._CH',             # 27
        'ED6_DT07/CH00494 ._CH',             # 28
        'ED6_DT07/CH00495 ._CH',             # 29
        'ED6_DT07/CH00496 ._CH',             # 2A
    )

    AddCharChipPat(
        'ED6_DT07/CH00450P._CP',             # 00
        'ED6_DT07/CH00451P._CP',             # 01
        'ED6_DT07/CH00452P._CP',             # 02
        'ED6_DT07/CH00453P._CP',             # 03
        'ED6_DT07/CH00454P._CP',             # 04
        'ED6_DT07/CH00460P._CP',             # 05
        'ED6_DT07/CH00461P._CP',             # 06
        'ED6_DT07/CH00462P._CP',             # 07
        'ED6_DT07/CH00463P._CP',             # 08
        'ED6_DT07/CH00464P._CP',             # 09
        'ED6_DT07/CH00470P._CP',             # 0A
        'ED6_DT07/CH00471P._CP',             # 0B
        'ED6_DT07/CH00472P._CP',             # 0C
        'ED6_DT07/CH00473P._CP',             # 0D
        'ED6_DT07/CH00474P._CP',             # 0E
        'ED6_DT07/CH00410P._CP',             # 0F
        'ED6_DT07/CH00411P._CP',             # 10
        'ED6_DT07/CH00412P._CP',             # 11
        'ED6_DT07/CH00413P._CP',             # 12
        'ED6_DT07/CH00414P._CP',             # 13
        'ED6_DT07/CH00415P._CP',             # 14
        'ED6_DT07/CH00416P._CP',             # 15
        'ED6_DT07/CH00420P._CP',             # 16
        'ED6_DT07/CH00421P._CP',             # 17
        'ED6_DT07/CH00422P._CP',             # 18
        'ED6_DT07/CH00423P._CP',             # 19
        'ED6_DT07/CH00424P._CP',             # 1A
        'ED6_DT07/CH00425P._CP',             # 1B
        'ED6_DT07/CH00426P._CP',             # 1C
        'ED6_DT07/CH00480P._CP',             # 1D
        'ED6_DT07/CH00481P._CP',             # 1E
        'ED6_DT07/CH00482P._CP',             # 1F
        'ED6_DT07/CH00483P._CP',             # 20
        'ED6_DT07/CH00484P._CP',             # 21
        'ED6_DT07/CH00485P._CP',             # 22
        'ED6_DT07/CH00486P._CP',             # 23
        'ED6_DT07/CH00490P._CP',             # 24
        'ED6_DT07/CH00491P._CP',             # 25
        'ED6_DT07/CH00492P._CP',             # 26
        'ED6_DT07/CH00493P._CP',             # 27
        'ED6_DT07/CH00494P._CP',             # 28
        'ED6_DT07/CH00495P._CP',             # 29
        'ED6_DT07/CH00496P._CP',             # 2A
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    ScpFunction(
        "Function_0_762",          # 00, 0
        "Function_1_763",          # 01, 1
        "Function_2_764",          # 02, 2
        "Function_3_77A",          # 03, 3
        "Function_4_790",          # 04, 4
        "Function_5_7AB",          # 05, 5
        "Function_6_7C6",          # 06, 6
        "Function_7_7E1",          # 07, 7
        "Function_8_7FC",          # 08, 8
        "Function_9_812",          # 09, 9
        "Function_10_849",         # 0A, 10
        "Function_11_85F",         # 0B, 11
        "Function_12_896",         # 0C, 12
        "Function_13_8AC",         # 0D, 13
        "Function_14_8E3",         # 0E, 14
        "Function_15_8F9",         # 0F, 15
        "Function_16_930",         # 10, 16
    )


    def Function_0_762(): pass

    label("Function_0_762")

    Return()

    # Function_0_762 end

    def Function_1_763(): pass

    label("Function_1_763")

    Return()

    # Function_1_763 end

    def Function_2_764(): pass

    label("Function_2_764")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_779")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_764")

    label("loc_779")

    Return()

    # Function_2_764 end

    def Function_3_77A(): pass

    label("Function_3_77A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_78F")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_3_77A")

    label("loc_78F")

    Return()

    # Function_3_77A end

    def Function_4_790(): pass

    label("Function_4_790")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AA")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Sleep(500)
    Jump("Function_4_790")

    label("loc_7AA")

    Return()

    # Function_4_790 end

    def Function_5_7AB(): pass

    label("Function_5_7AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C5")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Sleep(500)
    Jump("Function_5_7AB")

    label("loc_7C5")

    Return()

    # Function_5_7AB end

    def Function_6_7C6(): pass

    label("Function_6_7C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E0")
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Sleep(500)
    Jump("Function_6_7C6")

    label("loc_7E0")

    Return()

    # Function_6_7C6 end

    def Function_7_7E1(): pass

    label("Function_7_7E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FB")
    OP_99(0xFE, 0x0, 0xB, 0x960)
    Sleep(500)
    Jump("Function_7_7E1")

    label("loc_7FB")

    Return()

    # Function_7_7E1 end

    def Function_8_7FC(): pass

    label("Function_8_7FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_811")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_8_7FC")

    label("loc_811")

    Return()

    # Function_8_7FC end

    def Function_9_812(): pass

    label("Function_9_812")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_848")
    SetChrChipByIndex(0xFE, 20)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 21)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_9_812")

    label("loc_848")

    Return()

    # Function_9_812 end

    def Function_10_849(): pass

    label("Function_10_849")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85E")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_10_849")

    label("loc_85E")

    Return()

    # Function_10_849 end

    def Function_11_85F(): pass

    label("Function_11_85F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_895")
    SetChrChipByIndex(0xFE, 27)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 28)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_11_85F")

    label("loc_895")

    Return()

    # Function_11_85F end

    def Function_12_896(): pass

    label("Function_12_896")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8AB")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_12_896")

    label("loc_8AB")

    Return()

    # Function_12_896 end

    def Function_13_8AC(): pass

    label("Function_13_8AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E2")
    SetChrChipByIndex(0xFE, 34)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 35)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_13_8AC")

    label("loc_8E2")

    Return()

    # Function_13_8AC end

    def Function_14_8E3(): pass

    label("Function_14_8E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F8")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Jump("Function_14_8E3")

    label("loc_8F8")

    Return()

    # Function_14_8E3 end

    def Function_15_8F9(): pass

    label("Function_15_8F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92F")
    SetChrChipByIndex(0xFE, 41)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    SetChrChipByIndex(0xFE, 42)
    OP_99(0xFE, 0x0, 0x1, 0x3E8)
    Sleep(1000)
    Jump("Function_15_8F9")

    label("loc_92F")

    Return()

    # Function_15_8F9 end

    def Function_16_930(): pass

    label("Function_16_930")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "喝～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_930 end

    SaveToFile()

Try(main)
