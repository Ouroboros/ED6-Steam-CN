from ED6ScenarioHelper import *

def main():
    # 调试地图

    CreateScenaFile(
        FileName            = 'T0061   ._SN',
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
        '11120待机',                            # 9
        '11121移动',                            # 10
        '11122攻击',                            # 11
        '11123挨打',                            # 12
        '11124倒下',                            # 13
        '11130待机',                            # 14
        '11131移动',                            # 15
        '11132攻击',                            # 16
        '11133挨打',                            # 17
        '11134倒下',                            # 18
        '11140待机',                            # 19
        '11141移动',                            # 20
        '11142攻击',                            # 21
        '11143挨打',                            # 22
        '11144倒下',                            # 23
        '11150移动',                            # 24
        '11151待机',                            # 25
        '11152攻击',                            # 26
        '11153挨打',                            # 27
        '11154倒下',                            # 28
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
        'ED6_DT09/CH11120 ._CH',             # 00
        'ED6_DT09/CH11121 ._CH',             # 01
        'ED6_DT09/CH11122 ._CH',             # 02
        'ED6_DT09/CH11123 ._CH',             # 03
        'ED6_DT09/CH11124 ._CH',             # 04
        'ED6_DT09/CH11130 ._CH',             # 05
        'ED6_DT09/CH11131 ._CH',             # 06
        'ED6_DT09/CH11132 ._CH',             # 07
        'ED6_DT09/CH11133 ._CH',             # 08
        'ED6_DT09/CH11134 ._CH',             # 09
        'ED6_DT09/CH11140 ._CH',             # 0A
        'ED6_DT09/CH11141 ._CH',             # 0B
        'ED6_DT09/CH11142 ._CH',             # 0C
        'ED6_DT09/CH11143 ._CH',             # 0D
        'ED6_DT09/CH11144 ._CH',             # 0E
        'ED6_DT09/CH11150 ._CH',             # 0F
        'ED6_DT09/CH11151 ._CH',             # 10
        'ED6_DT09/CH11152 ._CH',             # 11
        'ED6_DT09/CH11153 ._CH',             # 12
        'ED6_DT09/CH11154 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT09/CH11120P._CP',             # 00
        'ED6_DT09/CH11121P._CP',             # 01
        'ED6_DT09/CH11122P._CP',             # 02
        'ED6_DT09/CH11123P._CP',             # 03
        'ED6_DT09/CH11124P._CP',             # 04
        'ED6_DT09/CH11130P._CP',             # 05
        'ED6_DT09/CH11131P._CP',             # 06
        'ED6_DT09/CH11132P._CP',             # 07
        'ED6_DT09/CH11133P._CP',             # 08
        'ED6_DT09/CH11134P._CP',             # 09
        'ED6_DT09/CH11140P._CP',             # 0A
        'ED6_DT09/CH11141P._CP',             # 0B
        'ED6_DT09/CH11142P._CP',             # 0C
        'ED6_DT09/CH11143P._CP',             # 0D
        'ED6_DT09/CH11144P._CP',             # 0E
        'ED6_DT09/CH11150P._CP',             # 0F
        'ED6_DT09/CH11151P._CP',             # 10
        'ED6_DT09/CH11152P._CP',             # 11
        'ED6_DT09/CH11153P._CP',             # 12
        'ED6_DT09/CH11154P._CP',             # 13
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


    ScpFunction(
        "Function_0_3CA",          # 00, 0
        "Function_1_3CB",          # 01, 1
        "Function_2_3CC",          # 02, 2
        "Function_3_3E2",          # 03, 3
        "Function_4_3F8",          # 04, 4
        "Function_5_41C",          # 05, 5
    )


    def Function_0_3CA(): pass

    label("Function_0_3CA")

    Return()

    # Function_0_3CA end

    def Function_1_3CB(): pass

    label("Function_1_3CB")

    Return()

    # Function_1_3CB end

    def Function_2_3CC(): pass

    label("Function_2_3CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3CC")

    label("loc_3E1")

    Return()

    # Function_2_3CC end

    def Function_3_3E2(): pass

    label("Function_3_3E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F7")
    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("Function_3_3E2")

    label("loc_3F7")

    Return()

    # Function_3_3E2 end

    def Function_4_3F8(): pass

    label("Function_4_3F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41B")
    OP_8D(0xFE, 4000, 20000, 24000, 30000, 1500)
    Jump("Function_4_3F8")

    label("loc_41B")

    Return()

    # Function_4_3F8 end

    def Function_5_41C(): pass

    label("Function_5_41C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "喝～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_41C end

    SaveToFile()

Try(main)
