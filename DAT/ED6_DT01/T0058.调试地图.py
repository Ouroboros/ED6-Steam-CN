from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0058   ._SN',
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
        '11000待机',                            # 9
        '11001移动',                            # 10
        '11002攻击',                            # 11
        '11003挨打',                            # 12
        '11004倒下',                            # 13
        '11010待机',                            # 14
        '11011移动',                            # 15
        '11012攻击',                            # 16
        '11013挨打',                            # 17
        '11014倒下',                            # 18
        '11020待机',                            # 19
        '11021移动',                            # 20
        '11022攻击',                            # 21
        '11023挨打',                            # 22
        '11024倒下',                            # 23
        '11030待机',                            # 24
        '11031移动',                            # 25
        '11032攻击',                            # 26
        '11033挨打',                            # 27
        '11034倒下',                            # 28
        '11040待机',                            # 29
        '11041移动',                            # 30
        '11042攻击',                            # 31
        '11043挨打',                            # 32
        '11044倒下',                            # 33
        '11050待机',                            # 34
        '11051移动',                            # 35
        '11052攻击',                            # 36
        '11053挨打',                            # 37
        '11054倒下',                            # 38
        '11060待机',                            # 39
        '11061移动',                            # 40
        '11062攻击',                            # 41
        '11063挨打',                            # 42
        '11064倒下',                            # 43
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
        'ED6_DT09/CH11000 ._CH',             # 00
        'ED6_DT09/CH11001 ._CH',             # 01
        'ED6_DT09/CH11002 ._CH',             # 02
        'ED6_DT09/CH11003 ._CH',             # 03
        'ED6_DT09/CH11004 ._CH',             # 04
        'ED6_DT09/CH11010 ._CH',             # 05
        'ED6_DT09/CH11011 ._CH',             # 06
        'ED6_DT09/CH11012 ._CH',             # 07
        'ED6_DT09/CH11013 ._CH',             # 08
        'ED6_DT09/CH11014 ._CH',             # 09
        'ED6_DT09/CH11020 ._CH',             # 0A
        'ED6_DT09/CH11021 ._CH',             # 0B
        'ED6_DT09/CH11022 ._CH',             # 0C
        'ED6_DT09/CH11023 ._CH',             # 0D
        'ED6_DT09/CH11024 ._CH',             # 0E
        'ED6_DT09/CH11030 ._CH',             # 0F
        'ED6_DT09/CH11031 ._CH',             # 10
        'ED6_DT09/CH11032 ._CH',             # 11
        'ED6_DT09/CH11033 ._CH',             # 12
        'ED6_DT09/CH11034 ._CH',             # 13
        'ED6_DT09/CH11040 ._CH',             # 14
        'ED6_DT09/CH11041 ._CH',             # 15
        'ED6_DT09/CH11042 ._CH',             # 16
        'ED6_DT09/CH11043 ._CH',             # 17
        'ED6_DT09/CH11044 ._CH',             # 18
        'ED6_DT09/CH11050 ._CH',             # 19
        'ED6_DT09/CH11051 ._CH',             # 1A
        'ED6_DT09/CH11052 ._CH',             # 1B
        'ED6_DT09/CH11053 ._CH',             # 1C
        'ED6_DT09/CH11054 ._CH',             # 1D
        'ED6_DT09/CH11060 ._CH',             # 1E
        'ED6_DT09/CH11061 ._CH',             # 1F
        'ED6_DT09/CH11062 ._CH',             # 20
        'ED6_DT09/CH11063 ._CH',             # 21
        'ED6_DT09/CH11064 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT09/CH11000P._CP',             # 00
        'ED6_DT09/CH11001P._CP',             # 01
        'ED6_DT09/CH11002P._CP',             # 02
        'ED6_DT09/CH11003P._CP',             # 03
        'ED6_DT09/CH11004P._CP',             # 04
        'ED6_DT09/CH11010P._CP',             # 05
        'ED6_DT09/CH11011P._CP',             # 06
        'ED6_DT09/CH11012P._CP',             # 07
        'ED6_DT09/CH11013P._CP',             # 08
        'ED6_DT09/CH11014P._CP',             # 09
        'ED6_DT09/CH11020P._CP',             # 0A
        'ED6_DT09/CH11021P._CP',             # 0B
        'ED6_DT09/CH11022P._CP',             # 0C
        'ED6_DT09/CH11023P._CP',             # 0D
        'ED6_DT09/CH11024P._CP',             # 0E
        'ED6_DT09/CH11030P._CP',             # 0F
        'ED6_DT09/CH11031P._CP',             # 10
        'ED6_DT09/CH11032P._CP',             # 11
        'ED6_DT09/CH11033P._CP',             # 12
        'ED6_DT09/CH11034P._CP',             # 13
        'ED6_DT09/CH11040P._CP',             # 14
        'ED6_DT09/CH11041P._CP',             # 15
        'ED6_DT09/CH11042P._CP',             # 16
        'ED6_DT09/CH11043P._CP',             # 17
        'ED6_DT09/CH11044P._CP',             # 18
        'ED6_DT09/CH11050P._CP',             # 19
        'ED6_DT09/CH11051P._CP',             # 1A
        'ED6_DT09/CH11052P._CP',             # 1B
        'ED6_DT09/CH11053P._CP',             # 1C
        'ED6_DT09/CH11054P._CP',             # 1D
        'ED6_DT09/CH11060P._CP',             # 1E
        'ED6_DT09/CH11061P._CP',             # 1F
        'ED6_DT09/CH11062P._CP',             # 20
        'ED6_DT09/CH11063P._CP',             # 21
        'ED6_DT09/CH11064P._CP',             # 22
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


    ScpFunction(
        "Function_0_622",          # 00, 0
        "Function_1_623",          # 01, 1
        "Function_2_624",          # 02, 2
        "Function_3_63A",          # 03, 3
        "Function_4_650",          # 04, 4
        "Function_5_674",          # 05, 5
    )


    def Function_0_622(): pass

    label("Function_0_622")

    Return()

    # Function_0_622 end

    def Function_1_623(): pass

    label("Function_1_623")

    Return()

    # Function_1_623 end

    def Function_2_624(): pass

    label("Function_2_624")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_639")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_624")

    label("loc_639")

    Return()

    # Function_2_624 end

    def Function_3_63A(): pass

    label("Function_3_63A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64F")
    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("Function_3_63A")

    label("loc_64F")

    Return()

    # Function_3_63A end

    def Function_4_650(): pass

    label("Function_4_650")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_673")
    OP_8D(0xFE, 4000, 20000, 24000, 30000, 1500)
    Jump("Function_4_650")

    label("loc_673")

    Return()

    # Function_4_650 end

    def Function_5_674(): pass

    label("Function_5_674")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "喝～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_674 end

    SaveToFile()

Try(main)
