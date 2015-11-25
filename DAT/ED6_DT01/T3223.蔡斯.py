from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3223   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3223.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '朵洛希',                               # 9
        '麻绪婆婆',                             # 10
        '艾德',                                 # 11
        '拜舍尔',                               # 12
        '林',                                   # 13
        '莉西亚',                               # 14
        '希利尔',                               # 15
        '艾缇',                                 # 16
        '拉克',                                 # 17
        '希玛',                                 # 18
        '库安',                                 # 19
        '西加罗',                               # 20
        '艾德尔',                               # 21
        '艾德',                                 # 22
        '水果牛奶',                             # 23
        '水果牛奶',                             # 24
        '水果牛奶',                             # 25
        '水果牛奶',                             # 26
        '水果牛奶',                             # 27
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02430 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01460 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
        'ED6_DT07/CH01120 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01160 ._CH',             # 08
        'ED6_DT07/CH01020 ._CH',             # 09
        'ED6_DT07/CH01060 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01130 ._CH',             # 0C
        'ED6_DT07/CH01270 ._CH',             # 0D
        'ED6_DT06/CH20021 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02430P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01460P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
        'ED6_DT07/CH01120P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01160P._CP',             # 08
        'ED6_DT07/CH01020P._CP',             # 09
        'ED6_DT07/CH01060P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01130P._CP',             # 0C
        'ED6_DT07/CH01270P._CP',             # 0D
        'ED6_DT06/CH20021P._CP',             # 0E
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 131086,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196622,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 2670,
        TriggerZ            = 250,
        TriggerY            = 3820,
        TriggerRange        = 400,
        ActorX              = 2590,
        ActorZ              = 1750,
        ActorY              = 5360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9940,
        TriggerZ            = 0,
        TriggerY            = 90,
        TriggerRange        = 400,
        ActorX              = 8490,
        ActorZ              = 1500,
        ActorY              = 340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8960,
        TriggerZ            = 250,
        TriggerY            = 13840,
        TriggerRange        = 1000,
        ActorX              = 9100,
        ActorZ              = 1750,
        ActorY              = 13840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3EE",          # 00, 0
        "Function_1_746",          # 01, 1
        "Function_2_747",          # 02, 2
        "Function_3_75D",          # 03, 3
        "Function_4_781",          # 04, 4
        "Function_5_A12",          # 05, 5
        "Function_6_C81",          # 06, 6
        "Function_7_13AD",         # 07, 7
        "Function_8_1735",         # 08, 8
        "Function_9_173C",         # 09, 9
        "Function_10_1743",        # 0A, 10
        "Function_11_1B7A",        # 0B, 11
        "Function_12_1B7F",        # 0C, 12
        "Function_13_20DC",        # 0D, 13
        "Function_14_2162",        # 0E, 14
        "Function_15_2169",        # 0F, 15
        "Function_16_2170",        # 10, 16
        "Function_17_2177",        # 11, 17
        "Function_18_217C",        # 12, 18
        "Function_19_3357",        # 13, 19
        "Function_20_34C5",        # 14, 20
        "Function_21_3765",        # 15, 21
    )


    def Function_0_3EE(): pass

    label("Function_0_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_401")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 19)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_40F")
    OP_A3(0x3FB)
    Event(0, 20)

    label("loc_40F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_445")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    Jump("loc_745")

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4C4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14330, 0, 1850, 182)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -1040, 0, 40770, 2)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -28880, 0, 43500, 9)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -28740, 0, 38750, 93)
    OP_43(0x14, 0x0, 0x0, 0x3)
    Jump("loc_745")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_52D")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14330, 0, 1850, 182)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -28740, 0, 38750, 93)
    OP_43(0x14, 0x0, 0x0, 0x3)
    Jump("loc_745")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_58F")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 11260, 0, 10650, 175)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 11070, 0, 8460, 358)
    Jump("loc_745")

    label("loc_58F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_618")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -2470, 0, 39920, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_615")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, 14070, 0, 2040, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 14600, 750, 1030, 0)

    label("loc_615")

    Jump("loc_745")

    label("loc_618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_690")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -1040, 0, 40770, 2)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 11260, 0, 10650, 175)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 11070, 0, 8460, 358)
    Jump("loc_745")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_6C6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14330, 0, 1850, 182)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 970, 0, -2050, 0)
    Jump("loc_745")

    label("loc_6C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6FC")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14330, 0, 1850, 182)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -2080, 250, 6150, 195)
    Jump("loc_745")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_745")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -30310, -250, 8840, 81)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 8490, 0, 340, 102)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -2080, 250, 6150, 195)

    label("loc_745")

    Return()

    # Function_0_3EE end

    def Function_1_746(): pass

    label("Function_1_746")

    Return()

    # Function_1_746 end

    def Function_2_747(): pass

    label("Function_2_747")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_747")

    label("loc_75C")

    Return()

    # Function_2_747 end

    def Function_3_75D(): pass

    label("Function_3_75D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_780")
    OP_8D(0xFE, -30720, 37410, -25780, 40750, 3000)
    Jump("Function_3_75D")

    label("loc_780")

    Return()

    # Function_3_75D end

    def Function_4_781(): pass

    label("Function_4_781")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_78E")
    Jump("loc_A0E")

    label("loc_78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_827")

    ChrTalk(
        0xFE,
        (
            "呵呵，最后的目标是\x01",
            "趁着女王诞辰庆典\x01",
            "在王都做笔大买卖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在那之前泡泡温泉，\x01",
            "积蓄一些精力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_8E4")

    ChrTalk(
        0xFE,
        (
            "听客房的服务生说，\x01",
            "蔡斯好像出事了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "连这种偏僻地方\x01",
            "都已经听到了传闻，\x01",
            "那边肯定是发生大乱子了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_8E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_94E")

    ChrTalk(
        0xFE,
        (
            "好好泡一下温泉，\x01",
            "缓解旅途的劳累……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了接下来的采购\x01",
            "养足精神吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_958")
    Jump("loc_A0E")

    label("loc_958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_9F3")

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "看到那些可爱的餐具，\x01",
            "想也没想就买下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家特产店里\x01",
            "好像还可以淘到很多宝贝呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0E")

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_9FD")
    Jump("loc_A0E")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_A07")
    Jump("loc_A0E")

    label("loc_A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A0E")

    label("loc_A0E")

    TalkEnd(0xFE)
    Return()

    # Function_4_781 end

    def Function_5_A12(): pass

    label("Function_5_A12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_A1F")
    Jump("loc_C7D")

    label("loc_A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_AC3")

    ChrTalk(
        0xFE,
        (
            "和妻子商量过了，\x01",
            "最近就在这里\x01",
            "好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后预计在女王的\x01",
            "诞辰庆典开始之前\x01",
            "到达最终目的地王都。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7D")

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_ACD")
    Jump("loc_C7D")

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_B0A")

    ChrTalk(
        0xFE,
        (
            "那么～\x01",
            "这就去泡个晨澡吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4C")

    label("loc_B0A")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        "你们要离开这里了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们暂时还会\x01",
            "在这里休息一阵子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4C")

    Jump("loc_C7D")

    label("loc_B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_B59")
    Jump("loc_C7D")

    label("loc_B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BD6")

    ChrTalk(
        0xFE,
        (
            "艾德尔那家伙，\x01",
            "已经去特产店买了好多东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，真是的。\x01",
            "真是不能大意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5F")

    label("loc_BD6")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "就在我没注意的一瞬间，\x01",
            "艾德尔那家伙\x01",
            "已经去特产店买了好多东西了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，真是的。\x01",
            "真是不能大意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5F")

    Jump("loc_C7D")

    label("loc_C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_C6C")
    Jump("loc_C7D")

    label("loc_C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_C76")
    Jump("loc_C7D")

    label("loc_C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C7D")

    label("loc_C7D")

    TalkEnd(0xFE)
    Return()

    # Function_5_A12 end

    def Function_6_C81(): pass

    label("Function_6_C81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D57")

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "好不容易闲下来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "就趁现在赶快准备一下\x01",
            "待会儿的饭菜吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天突然\x01",
            "一下子来了很多客人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E2F")

    label("loc_D57")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "好不容易闲下来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "为什么客人们\x01",
            "都在同一天来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果每个人能把\x01",
            "来的时间错开的话，\x01",
            "就能更舒服地享受温泉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2F")

    Jump("loc_13A9")

    label("loc_E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EAF")

    ChrTalk(
        0xFE,
        "怎么样，调查进展如何了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里和平常一样还是很忙啊。\x01",
            "因为老是只有我一个人干活。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_F72")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "难道你们今天是来调查案件的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里也已经传来消息了。\x01",
            "中央工房的东西被盗走了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当游击士\x01",
            "实在是很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_FCF")

    ChrTalk(
        0xFE,
        "啊，要走了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后有空的话\x01",
            "要再来玩啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_10EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1070")

    ChrTalk(
        0xFE,
        (
            "东方的料理\x01",
            "不仅味道可口，\x01",
            "而且对健康很有好处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然做起来\x01",
            "要花不少时间和精力，\x01",
            "不过却相当值得。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E7")

    label("loc_1070")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "啊，要去泡澡了吗？\x01",
            "慢慢享受吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我就趁这段时间给你们\x01",
            "做好吃的东方料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E7")

    Jump("loc_13A9")

    label("loc_10EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_11FA")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "刚才麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听到客人平安无事，\x01",
            "我也就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "这下可以开始安心地准备晚饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为来了不少新客人，\x01",
            "我这边也变得更忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_128C")

    ChrTalk(
        0xFE,
        (
            "没想到竟然\x01",
            "会有游击士在这里。\x01",
            "这下就放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "这件事就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_128C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1296")
    Jump("loc_13A9")

    label("loc_1296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1319")

    ChrTalk(
        0xFE,
        (
            "偶尔放松一下，\x01",
            "给自己放个假虽然很好……\x01",
            "但是时间久了就会消磨干劲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "人啊，\x01",
            "真是容易懒散下来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A9")

    label("loc_1319")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "啊～今天很闲啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "偶尔放松一下，\x01",
            "给自己放个假虽然很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是时间久了\x01",
            "就会消磨干劲了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A9")

    TalkEnd(0xFE)
    Return()

    # Function_6_C81 end

    def Function_7_13AD(): pass

    label("Function_7_13AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_13BA")
    Jump("loc_1731")

    label("loc_13BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1488")

    ChrTalk(
        0xFE,
        (
            "我觉得只有充分休息\x01",
            "才能让身心都恢复活力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "总觉得有一种\x01",
            "会钓到大型猎物的预感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好，最好抓紧时间。\x01",
            "趁这种感觉还没消失，\x01",
            "快赶到下一个钓场！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1731")

    label("loc_1488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1504")

    ChrTalk(
        0xFE,
        (
            "刚才听到了小道消息，\x01",
            "说是蔡斯出事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "最近的骚动真让人不安啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1731")

    label("loc_1504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_150E")
    Jump("loc_1731")

    label("loc_150E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_15C1")

    ChrTalk(
        0xFE,
        (
            "嘿，\x01",
            "你们也要在这里住宿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "等露天澡堂能用了，\x01",
            "你们就赶快去试试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要体验过一次，\x01",
            "你们就会迷上这个温泉的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1731")

    label("loc_15C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_15CB")
    Jump("loc_1731")

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_172A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16A9")

    ChrTalk(
        0xFE,
        (
            "就算不泡澡，\x01",
            "也还有很多乐趣哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个『红叶亭』的\x01",
            "正宗东方料理味道相当不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，这里确实是个天堂。\x01",
            "我现在就开始期待晚餐了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1727")

    label("loc_16A9")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "抽取温泉水的水泵\x01",
            "好像有一点故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算啦，\x01",
            "这个温泉胜地已经有年头了。\x01",
            "发生这种事情也没什么好奇怪的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1727")

    Jump("loc_1731")

    label("loc_172A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1731")

    label("loc_1731")

    TalkEnd(0xFE)
    Return()

    # Function_7_13AD end

    def Function_8_1735(): pass

    label("Function_8_1735")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_1735 end

    def Function_9_173C(): pass

    label("Function_9_173C")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_173C end

    def Function_10_1743(): pass

    label("Function_10_1743")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1750")
    Jump("loc_1B76")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_17EB")

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "快点抓住那些\x01",
            "袭击中央工房的犯人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "绝对不能让那种\x01",
            "无法无天的家伙逍遥法外。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1876")

    label("loc_17EB")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "啊，是你们。\x01",
            "还是这么忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从艾德那里听说了，\x01",
            "你们是游击士对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请加油。\x01",
            "我支持你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1876")

    Jump("loc_1B76")

    label("loc_1879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1883")
    Jump("loc_1B76")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_188D")
    Jump("loc_1B76")

    label("loc_188D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1897")
    Jump("loc_1B76")

    label("loc_1897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_19C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_18D8")

    ChrTalk(
        0xFE,
        "您好，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『柚子之间』\x01",
            "是这里隔壁的房间哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BD")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1948")

    ChrTalk(
        0xFE,
        (
            "那么，趁现在还早，\x01",
            "赶快收拾一下床铺吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "马上就是晚饭时间了，\x01",
            "客人们都该回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BD")

    label("loc_1948")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "哎呀，太好了。\x01",
            "有人来修理水泵了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们总是受到\x01",
            "中央工房的照顾啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19BD")

    Jump("loc_1B76")

    label("loc_19C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1AC3")

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "今天真难办啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为，\x01",
            "温泉的水泵出了点故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不早点修理好的话\x01",
            "会让客人们失望的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "客人们都是为了温泉\x01",
            "才来这里的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6C")

    label("loc_1AC3")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "欢迎。\x01",
            "这里是温泉旅馆『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个旅馆的客房\x01",
            "都有各自的名字哦。\x01",
            "这里叫做『柚子之间』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起『２０１室』这类的名字\x01",
            "更加有情调吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6C")

    Jump("loc_1B76")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B76")

    label("loc_1B76")

    TalkEnd(0xFE)
    Return()

    # Function_10_1743 end

    def Function_11_1B7A(): pass

    label("Function_11_1B7A")

    Call(0, 12)
    Return()

    # Function_11_1B7A end

    def Function_12_1B7F(): pass

    label("Function_12_1B7F")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                 # 0
            "买东西\x01",                               # 1
            "欢迎品尝「诱惑山菜火锅」700米拉\x01",      # 2
            "离开\x01",                                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFC")
    OP_0D()
    OP_A9(0x46)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_1BFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CD0")
    SubMira(700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "诱惑山菜火锅\x07\x00",
            "品尝过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x4)"), scpexpr(EXPR_END)), "loc_1C91")
    Jump("loc_1CC2")

    label("loc_1C91")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "学会了\x07\x02",
            "诱惑山菜火锅\x07\x00",
            "的做法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC2")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_1CF8")

    label("loc_1CD0")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_1CF8")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xF)
    Return()

    label("loc_1D0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D1B")
    TalkEnd(0xF)
    Return()

    label("loc_1D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1D98")

    ChrTalk(
        0xF,
        (
            "只有这种时候\x01",
            "才适合做扫除啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "一会儿旅馆又会挤满\x01",
            "来这里泡温泉的客人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1D")

    label("loc_1D98")

    OP_A2(0x6)

    ChrTalk(
        0xF,
        (
            "啊，欢迎光临。\x01",
            "这里是『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "因为大家都去王都参加诞辰庆典了，\x01",
            "所以能有客人来我们非常欢迎。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1D")

    Jump("loc_20D8")

    label("loc_1E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1E2A")
    Jump("loc_20D8")

    label("loc_1E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1EDD")

    ChrTalk(
        0xF,
        (
            "今天不管和谁说话，\x01",
            "都是在谈论蔡斯的事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "难得来到这个温泉胜地，\x01",
            "却只顾着谈论这么阴暗的话题……\x01",
            "真是感到有些失落啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_1EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1F3E")

    ChrTalk(
        0xF,
        (
            "啊，已经要回去了吗？\x01",
            "还是那么忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "下次来的时候，\x01",
            "要慢慢好好享受哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_1F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1FC7")

    ChrTalk(
        0xF,
        (
            "泡完澡出来享用东方料理，\x01",
            "会更有一番风味呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "痛痛快快地出汗吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_1FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_203E")

    ChrTalk(
        0xF,
        "啊～欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "你们的房间在二楼。\x01",
            "请从前台旁边的楼梯走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D8")

    label("loc_203E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_2048")
    Jump("loc_20D8")

    label("loc_2048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2052")
    Jump("loc_20D8")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20D8")

    ChrTalk(
        0xF,
        (
            "啊，欢迎光临。\x01",
            "这里是『红叶亭』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "请好好享受\x01",
            "我们的东方料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D8")

    TalkEnd(0xF)
    Return()

    # Function_12_1B7F end

    def Function_13_20DC(): pass

    label("Function_13_20DC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "#151F泡过温泉之后\x01",
            "喝杯水果牛奶真是好舒服啊～\x02\x03",
            "泡得暖暖的身体\x01",
            "都被这清凉和甘甜给感染了～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_20DC end

    def Function_14_2162(): pass

    label("Function_14_2162")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_2162 end

    def Function_15_2169(): pass

    label("Function_15_2169")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_15_2169 end

    def Function_16_2170(): pass

    label("Function_16_2170")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_16_2170 end

    def Function_17_2177(): pass

    label("Function_17_2177")

    Call(0, 18)
    Return()

    # Function_17_2177 end

    def Function_18_217C(): pass

    label("Function_18_217C")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21DC")
    OP_0D()
    OP_A9(0x45)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_21DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21ED")
    TalkEnd(0x9)
    Return()

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2825")
    ClearMapFlags(0x1)
    OP_66(0x0)
    OP_69(0x9, 0x3E8)
    OP_A2(0x525)
    OP_28(0x40, 0x1, 0x800)
    OP_28(0x40, 0x4, 0x10)

    ChrTalk(
        0x9,
        (
            "#680F提妲，谢谢了。\x02\x03",
            "泵好像\x01",
            "已经修好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F呵呵……\x02\x03",
            "经常受你照顾，\x01",
            "这点小事当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F呵呵，\x01",
            "好甜的小嘴呀。\x02\x03",
            "呀，刚才也\x01",
            "真是辛苦你们了。\x02\x03",
            "她好像和你们认识呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F呵呵呵～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F？？？\x02\x03",
            "什么事呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F正好遇上\x01",
            "游击士的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F你们真是\x01",
            "帮了大忙啦。\x02\x03",
            "作为回礼，\x01",
            "你们今天就住在这里休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎，可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，婆婆。\x02\x03",
            "我们没对爷爷说\x01",
            "今天要住在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F呀，不用担心了，\x01",
            "我刚才和拉赛尔连络过了。\x02\x03",
            "他说『这里的作业明天才能完成，\x01",
            "今晚就住在你那里了』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F爷爷吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎！\x01",
            "博士还真机灵呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F还不如说\x01",
            "嘴比较甜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F呀，不要客气呀。\x02\x03",
            "二楼的『柚子之间』的房间\x01",
            "已经给你们准备好了，把行李放下来吧。\x02\x03",
            "离晚饭还要点时间，\x01",
            "你们先去泡温泉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F饭前洗澡？\x02\x03",
            "洗澡一般不是\x01",
            "在睡觉前的嘛？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F在说什么呢，\x01",
            "难得的温泉呀。\x02\x03",
            "从早到晚，\x01",
            "什么时候泡都是很正常的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F呵呵，就算一天\x01",
            "泡三次都是常有的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样呀……\x02\x03",
            "嗯，我虽然很喜欢洗澡，\x01",
            "但这么沉迷……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F到房间放行李的话\x01",
            "还是快去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)
    OP_66(0x1)
    Jump("loc_3353")

    label("loc_2825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2ACE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2890")

    ChrTalk(
        0x9,
        (
            "#680F有空的话\x01",
            "你们可以随时来这里住。\x02\x03",
            "那么，到王都的路上\x01",
            "你们要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACB")

    label("loc_2890")

    OP_A2(0x0)

    ChrTalk(
        0x9,
        (
            "#680F啊，是你们……\x01",
            "犯人的调查已经告一段落了吗？\x02\x03",
            "如果做完的话\x01",
            "就好好歇歇吧。\x02\x03",
            "因为最近客人很多，\x01",
            "露天温泉也都预订满了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～\x01",
            "我们也想这样……\x02\x03",
            "不过，\x01",
            "现在必须得去王都一趟呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "之前真是承蒙照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F哪里，别这么客气嘛。\x01",
            "就算是修水泵的谢礼吧。\x02\x03",
            "提妲还是那样子\x01",
            "又在帮拉赛尔干活吗？\x02\x03",
            "这样太勉强那个孩子了，\x01",
            "你们俩要帮我\x01",
            "和拉赛尔说说才行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊…………\x02\x03",
            "……嗯！\x01",
            "我知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我们会转达的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F那么到王都的路上\x01",
            "你们要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACB")

    Jump("loc_3353")

    label("loc_2ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2B9F")

    ChrTalk(
        0x9,
        (
            "#680F啊，是你们。\x02\x03",
            "总是为了追捕犯人\x01",
            "而东奔西走忙个不停啊。\x02\x03",
            "唉……今天的晚饭又只有\x01",
            "不过在这一带\x01",
            "没有听说什么线索。\x02\x03",
            "呼～\x01",
            "至少能帮上点忙也好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_2B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2C8C")

    ChrTalk(
        0x9,
        (
            "#680F哦，提妲你怎么了？\x02\x03",
            "脸色看起来有点不好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，不。\x01",
            "没什么事啦。\x02\x03",
            "我们有件事\x01",
            "只是有些累了而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F是吗，\x01",
            "可不要太过勉强哦。\x02\x03",
            "你跟拉赛尔那家伙\x01",
            "实在太像了。\x01",
            "可不要学他乱来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3D")

    label("loc_2C8C")

    OP_A2(0x0)

    ChrTalk(
        0x9,
        (
            "#680F啊，是你们。\x01",
            "不过应该没事吧？\x02\x03",
            "听说中央工房\x01",
            "发生了强盗事件，\x01",
            "真是有点担心啊。\x02\x03",
            "但如果是这样的话就没问题了。\x01",
            "呼，终于放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D3D")

    Jump("loc_3353")

    label("loc_2D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2DA0")

    ChrTalk(
        0x9,
        (
            "#680F哦，回来的真快啊。\x02\x03",
            "是不是要去\x01",
            "露天温泉泡澡呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_2DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_2E36")

    ChrTalk(
        0x9,
        (
            "#680F温泉和这里是分开的，\x01",
            "从食堂里面的通道过去吧。\x02\x03",
            "请在我们引以为荣的露天温泉里\x01",
            "慢慢享受一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_2E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_31D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_END)), "loc_2EBC")

    ChrTalk(
        0x9,
        (
            "#680F你们的房间 \x01",
            "是二楼的『柚子房间』哦。\x02\x03",
            "放好行李之后，\x01",
            "在晚饭之前都可以泡温泉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D2")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_2F75")

    ChrTalk(
        0x9,
        (
            "#680F那孩子和拉赛尔一样，\x01",
            "一摸到机械就停不下手。\x02\x03",
            "麻烦你们去\x01",
            "水泵小屋看看情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31D2")

    label("loc_2F75")

    OP_A2(0x58D)

    ChrTalk(
        0x9,
        (
            "#680F哎呀，\x01",
            "真是辛苦你们了呢。\x02\x03",
            "那个客人\x01",
            "是你们的熟人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F呵呵呵～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F看来水泵的修理\x01",
            "也顺利地完成了哦。\x02\x03",
            "外面的水井\x01",
            "也开始有热水湧出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F啊，是吗？\x02\x03",
            "但是提妲\x01",
            "还在小屋那里没回来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，刚才应该先去\x01",
            "小屋看看情况呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是啊，走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F那就拜托你们去看看吧。\x02\x03",
            "那孩子和拉赛尔一样，\x01",
            "一摸到机械就停不下手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哈哈，果然呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那我们就去看看吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F那就拜托了。\x01",
            "再麻烦你们跑一趟。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31D2")

    Jump("loc_3353")

    label("loc_31D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_323E")

    ChrTalk(
        0x9,
        (
            "#680F又给你们添麻烦了，\x01",
            "拜托你们了。\x02\x03",
            "无论如何请帮忙\x01",
            "到平原道找到那个客人，\x01",
            "并把她平安地带回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_323E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_32BE")

    ChrTalk(
        0x9,
        (
            "#680F怎么，忘了\x01",
            "水泵小屋在哪里？\x02\x03",
            "走到村子的广场那里，\x01",
            "从北面的斜坡上去就到了。\x02\x03",
            "那么就拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3353")

    label("loc_32BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3353")

    ChrTalk(
        0x9,
        (
            "#680F嘿～欢迎。\x01",
            "本旅馆有我们引以为豪的天然温泉。\x02\x03",
            "其中东方风格的露天澡堂\x01",
            "特别受客人们欢迎。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3353")

    TalkEnd(0x9)
    Return()

    # Function_18_217C end

    def Function_19_3357(): pass

    label("Function_19_3357")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(10910, 0, 69600, 0)
    SetChrPos(0x101, 11690, 0, 68340, 180)
    SetChrPos(0x102, 11420, 0, 67000, 45)
    SetChrPos(0x107, 12710, 0, 66950, 315)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#502F#2P好了。\x01",
            "行李已经放好了……\x02\x03",
            "#505F对了，温泉在哪呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F#6P啊……\x01",
            "后面不远处就是泡澡专用的温泉。\x02\x03",
            "而且里面还有\x01",
            "一个很大的露天温泉哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P说到露天温泉……\x01",
            "就是在室外建造的澡堂吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P嘿嘿～好像很有趣嘛！\x02\x03",
            "#001F那么，我们出发吧！\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    EventEnd(0x0)
    Return()

    # Function_19_3357 end

    def Function_20_34C5(): pass

    label("Function_20_34C5")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(12630, 0, 1940, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 14070, 0, 2040, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x16, 14600, 750, 1030, 0)
    SetChrPos(0x17, 13500, 700, 950, 0)
    SetChrPos(0x18, 13380, 700, 500, 0)
    SetChrPos(0x19, 13870, 700, 660, 0)
    SetChrPos(0x1A, 13800, 700, 310, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#152F#2P唔，好慢啊～\x01",
            "小艾他们去哪儿了嘛～\x02\x03",
            "呼～还没吃晚饭，\x01",
            "肚子就喝得这么涨了……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "泡完温泉后的艾丝蒂尔他们\x01",
            "先是安慰生气的朵洛希，\x01",
            "接着一起品尝旅馆引以为豪的东方料理。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "晚饭过后四人玩纸牌助兴，\x01",
            "玩了一阵子之后又再去泡温泉……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，\x01",
            "众人在温泉乡度过了轻松有趣的一天。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xD, 0x0, 0x64)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Sleep(5000)
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_34C5 end

    def Function_21_3765(): pass

    label("Function_21_3765")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "露天澡堂在这边  ≡\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_3765 end

    SaveToFile()

Try(main)
