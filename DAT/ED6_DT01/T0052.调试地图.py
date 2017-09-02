from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0052   ._SN',
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
        '10700待机',                            # 9
        '10701移动',                            # 10
        '10702攻击',                            # 11
        '10703挨打',                            # 12
        '10704倒下',                            # 13
        '10710待机',                            # 14
        '10711移动',                            # 15
        '10712攻击',                            # 16
        '10713挨打',                            # 17
        '10714倒下',                            # 18
        '10720待机',                            # 19
        '10721移动',                            # 20
        '10722攻击',                            # 21
        '10723挨打',                            # 22
        '10724倒下',                            # 23
        '10730待机',                            # 24
        '10731移动',                            # 25
        '10732攻击',                            # 26
        '10733挨打',                            # 27
        '10734倒下',                            # 28
        '10740待机',                            # 29
        '10741移动',                            # 30
        '10742攻击',                            # 31
        '10743挨打',                            # 32
        '10744倒下',                            # 33
        '10750待机',                            # 34
        '10751移动',                            # 35
        '10752攻击',                            # 36
        '10753挨打',                            # 37
        '10754倒下',                            # 38
        '10760待机',                            # 39
        '10761移动',                            # 40
        '10762攻击',                            # 41
        '10763挨打',                            # 42
        '10764倒下',                            # 43
        '10770移动',                            # 44
        '10771待机',                            # 45
        '10772攻击',                            # 46
        '10773挨打',                            # 47
        '10774倒下',                            # 48
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
        'ED6_DT09/CH10700 ._CH',             # 00
        'ED6_DT09/CH10701 ._CH',             # 01
        'ED6_DT09/CH10702 ._CH',             # 02
        'ED6_DT09/CH10703 ._CH',             # 03
        'ED6_DT09/CH10704 ._CH',             # 04
        'ED6_DT09/CH10710 ._CH',             # 05
        'ED6_DT09/CH10711 ._CH',             # 06
        'ED6_DT09/CH10712 ._CH',             # 07
        'ED6_DT09/CH10713 ._CH',             # 08
        'ED6_DT09/CH10714 ._CH',             # 09
        'ED6_DT09/CH10720 ._CH',             # 0A
        'ED6_DT09/CH10721 ._CH',             # 0B
        'ED6_DT09/CH10722 ._CH',             # 0C
        'ED6_DT09/CH10723 ._CH',             # 0D
        'ED6_DT09/CH10724 ._CH',             # 0E
        'ED6_DT09/CH10730 ._CH',             # 0F
        'ED6_DT09/CH10731 ._CH',             # 10
        'ED6_DT09/CH10732 ._CH',             # 11
        'ED6_DT09/CH10733 ._CH',             # 12
        'ED6_DT09/CH10734 ._CH',             # 13
        'ED6_DT09/CH10740 ._CH',             # 14
        'ED6_DT09/CH10741 ._CH',             # 15
        'ED6_DT09/CH10742 ._CH',             # 16
        'ED6_DT09/CH10743 ._CH',             # 17
        'ED6_DT09/CH10744 ._CH',             # 18
        'ED6_DT09/CH10750 ._CH',             # 19
        'ED6_DT09/CH10751 ._CH',             # 1A
        'ED6_DT09/CH10752 ._CH',             # 1B
        'ED6_DT09/CH10753 ._CH',             # 1C
        'ED6_DT09/CH10754 ._CH',             # 1D
        'ED6_DT09/CH10760 ._CH',             # 1E
        'ED6_DT09/CH10761 ._CH',             # 1F
        'ED6_DT09/CH10762 ._CH',             # 20
        'ED6_DT09/CH10763 ._CH',             # 21
        'ED6_DT09/CH10764 ._CH',             # 22
        'ED6_DT09/CH10770 ._CH',             # 23
        'ED6_DT09/CH10771 ._CH',             # 24
        'ED6_DT09/CH10772 ._CH',             # 25
        'ED6_DT09/CH10773 ._CH',             # 26
        'ED6_DT09/CH10774 ._CH',             # 27
    )

    AddCharChipPat(
        'ED6_DT09/CH10700P._CP',             # 00
        'ED6_DT09/CH10701P._CP',             # 01
        'ED6_DT09/CH10702P._CP',             # 02
        'ED6_DT09/CH10703P._CP',             # 03
        'ED6_DT09/CH10704P._CP',             # 04
        'ED6_DT09/CH10710P._CP',             # 05
        'ED6_DT09/CH10711P._CP',             # 06
        'ED6_DT09/CH10712P._CP',             # 07
        'ED6_DT09/CH10713P._CP',             # 08
        'ED6_DT09/CH10714P._CP',             # 09
        'ED6_DT09/CH10720P._CP',             # 0A
        'ED6_DT09/CH10721P._CP',             # 0B
        'ED6_DT09/CH10722P._CP',             # 0C
        'ED6_DT09/CH10723P._CP',             # 0D
        'ED6_DT09/CH10724P._CP',             # 0E
        'ED6_DT09/CH10730P._CP',             # 0F
        'ED6_DT09/CH10731P._CP',             # 10
        'ED6_DT09/CH10732P._CP',             # 11
        'ED6_DT09/CH10733P._CP',             # 12
        'ED6_DT09/CH10734P._CP',             # 13
        'ED6_DT09/CH10740P._CP',             # 14
        'ED6_DT09/CH10741P._CP',             # 15
        'ED6_DT09/CH10742P._CP',             # 16
        'ED6_DT09/CH10743P._CP',             # 17
        'ED6_DT09/CH10744P._CP',             # 18
        'ED6_DT09/CH10750P._CP',             # 19
        'ED6_DT09/CH10751P._CP',             # 1A
        'ED6_DT09/CH10752P._CP',             # 1B
        'ED6_DT09/CH10753P._CP',             # 1C
        'ED6_DT09/CH10754P._CP',             # 1D
        'ED6_DT09/CH10760P._CP',             # 1E
        'ED6_DT09/CH10761P._CP',             # 1F
        'ED6_DT09/CH10762P._CP',             # 20
        'ED6_DT09/CH10763P._CP',             # 21
        'ED6_DT09/CH10764P._CP',             # 22
        'ED6_DT09/CH10770P._CP',             # 23
        'ED6_DT09/CH10771P._CP',             # 24
        'ED6_DT09/CH10772P._CP',             # 25
        'ED6_DT09/CH10773P._CP',             # 26
        'ED6_DT09/CH10774P._CP',             # 27
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
        TalkScenaIndex      = 5,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 5,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 5,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 18000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_6EA",          # 00, 0
        "Function_1_6EB",          # 01, 1
        "Function_2_6EC",          # 02, 2
        "Function_3_702",          # 03, 3
        "Function_4_718",          # 04, 4
        "Function_5_73C",          # 05, 5
    )


    def Function_0_6EA(): pass

    label("Function_0_6EA")

    Return()

    # Function_0_6EA end

    def Function_1_6EB(): pass

    label("Function_1_6EB")

    Return()

    # Function_1_6EB end

    def Function_2_6EC(): pass

    label("Function_2_6EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_701")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6EC")

    label("loc_701")

    Return()

    # Function_2_6EC end

    def Function_3_702(): pass

    label("Function_3_702")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_717")
    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("Function_3_702")

    label("loc_717")

    Return()

    # Function_3_702 end

    def Function_4_718(): pass

    label("Function_4_718")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_73B")
    OP_8D(0xFE, 4000, 20000, 24000, 30000, 1500)
    Jump("Function_4_718")

    label("loc_73B")

    Return()

    # Function_4_718 end

    def Function_5_73C(): pass

    label("Function_5_73C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "喝～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_73C end

    SaveToFile()

Try(main)
