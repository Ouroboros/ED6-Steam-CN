from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3170   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3170.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3170   ._SN',
            'ED6_DT01/T3170_1 ._SN',
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
        '多杰',                                 # 9
        '贝恩',                                 # 10
        '乌尔斯',                               # 11
        '兰达老人',                             # 12
        '科奇莫爷爷',                           # 13
        '伊格尔',                               # 14
        '雷曼',                                 # 15
        '康丝坦茨',                             # 16
        '雷伊',                                 # 17
        '蒂亚利',                               # 18
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
        'ED6_DT07/CH01143 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01000 ._CH',             # 03
        'ED6_DT07/CH01100 ._CH',             # 04
        'ED6_DT07/CH01250 ._CH',             # 05
        'ED6_DT07/CH01450 ._CH',             # 06
        'ED6_DT07/CH01230 ._CH',             # 07
        'ED6_DT07/CH01220 ._CH',             # 08
        'ED6_DT07/CH01663 ._CH',             # 09
        'ED6_DT07/CH01223 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01143P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01000P._CP',             # 03
        'ED6_DT07/CH01100P._CP',             # 04
        'ED6_DT07/CH01250P._CP',             # 05
        'ED6_DT07/CH01450P._CP',             # 06
        'ED6_DT07/CH01230P._CP',             # 07
        'ED6_DT07/CH01220P._CP',             # 08
        'ED6_DT07/CH01663P._CP',             # 09
        'ED6_DT07/CH01223P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -530,
        TriggerZ            = -1000,
        TriggerY            = 4660,
        TriggerRange        = 400,
        ActorX              = -2470,
        ActorZ              = 500,
        ActorY              = 4710,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_63E",          # 01, 1
        "Function_2_6B2",          # 02, 2
        "Function_3_6C8",          # 03, 3
        "Function_4_6EC",          # 04, 4
        "Function_5_710",          # 05, 5
        "Function_6_734",          # 06, 6
        "Function_7_963",          # 07, 7
        "Function_8_DE0",          # 08, 8
        "Function_9_1099",         # 09, 9
        "Function_10_13D4",        # 0A, 10
        "Function_11_154A",        # 0B, 11
        "Function_12_154B",        # 0C, 12
        "Function_13_1550",        # 0D, 13
        "Function_14_28C0",        # 0E, 14
        "Function_15_33E6",        # 0F, 15
        "Function_16_3C38",        # 10, 16
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 790, -1000, 6110, 1)
    Jump("loc_63D")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_34A")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_419")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 1800, 4000, 7110, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -580, -1000, 8800, 356)
    OP_43(0x9, 0x0, 0x0, 0x3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -260, 4000, 7710, 192)
    OP_43(0xC, 0x0, 0x0, 0x5)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 790, -1000, 6110, 1)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -540, -1000, 4640, 270)
    OP_44(0x10, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 10)
    SetChrPos(0x10, -2630, 4200, 7900, 182)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, -3800, 4200, 6600, 90)
    SetChrFlags(0x11, 0x10)
    Jump("loc_63D")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1200, -1000, 5200, 97)
    OP_43(0xA, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -1000, 2230, 105)
    Jump("loc_63D")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4B8")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_50B")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1200, -1000, 5200, 97)
    OP_43(0xB, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 640, -1000, 6620, 9)
    Jump("loc_63D")

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_557")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3450, -1000, 8500, 185)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_5A3")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63D")

    label("loc_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5EF")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -1000, 2230, 105)
    Jump("loc_63D")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_63D")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -1000, 2230, 105)

    label("loc_63D")

    Return()

    # Function_0_266 end

    def Function_1_63E(): pass

    label("Function_1_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_648")
    Jump("loc_6B1")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_652")
    Jump("loc_6B1")

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_65C")
    Jump("loc_6B1")

    label("loc_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_66A")
    OP_64(0x0, 0x1)
    Jump("loc_6B1")

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_674")
    Jump("loc_6B1")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_67E")
    Jump("loc_6B1")

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_68C")
    OP_64(0x0, 0x1)
    Jump("loc_6B1")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_696")
    Jump("loc_6B1")

    label("loc_696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_6A0")
    Jump("loc_6B1")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_6AA")
    Jump("loc_6B1")

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6B1")

    label("loc_6B1")

    Return()

    # Function_1_63E end

    def Function_2_6B2(): pass

    label("Function_2_6B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6B2")

    label("loc_6C7")

    Return()

    # Function_2_6B2 end

    def Function_3_6C8(): pass

    label("Function_3_6C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EB")
    OP_8D(0xFE, -1880, 8780, 440, 8570, 3000)
    Jump("Function_3_6C8")

    label("loc_6EB")

    Return()

    # Function_3_6C8 end

    def Function_4_6EC(): pass

    label("Function_4_6EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70F")
    OP_8D(0xFE, 400, 5540, 5960, 4780, 3000)
    Jump("Function_4_6EC")

    label("loc_70F")

    Return()

    # Function_4_6EC end

    def Function_5_710(): pass

    label("Function_5_710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733")
    OP_8D(0xFE, -1460, 6310, 0, 9500, 3000)
    Jump("Function_5_710")

    label("loc_733")

    Return()

    # Function_5_710 end

    def Function_6_734(): pass

    label("Function_6_734")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C4")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【对话】\x01",              # 0
            "【报告测试结果】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7BF"),
        (1, "loc_85D"),
        (SWITCH_DEFAULT, "loc_8BD"),
    )


    label("loc_7BF")


    ChrTalk(
        0xFE,
        (
            "前辈的想法，\x01",
            "与其说是积极，\x01",
            "不如说是马马虎虎呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么糟糕的西红柿，\x01",
            "就算取了个好名字，\x01",
            "也是卖不出去的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BD")

    label("loc_85D")


    ChrTalk(
        0xFE,
        (
            "抱歉，\x01",
            "今天工作已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那件事情\x01",
            "等明天再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BD")

    label("loc_8BD")

    TalkEnd(0xFE)
    Return()

    label("loc_8C4")


    ChrTalk(
        0xFE,
        (
            "前辈的想法，\x01",
            "与其说是积极，\x01",
            "不如说是马马虎虎呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么糟糕的西红柿，\x01",
            "就算取了个好名字，\x01",
            "也是卖不出去的吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_734 end

    def Function_7_963(): pass

    label("Function_7_963")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_B57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_A05")

    ChrTalk(
        0xFE,
        (
            "蒂亚利，\x01",
            "我觉得你的积极构想还远远不够。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管跌倒了多少次都要爬起来，\x01",
            "那样的韧劲是必不可少的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54")

    label("loc_A05")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "蒂亚利，\x01",
            "我觉得你的积极构想还远远不够。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就拿那个苦西红柿来说吧。\x01",
            "若是取一个适当的名字，\x01",
            "搞不好会异常畅销。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是啊！比如……\x01",
            "『苦味西红柿』什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，相当不错啊。\x01",
            "那么就叫『苦味西红柿』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B54")

    Jump("loc_DDC")

    label("loc_B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_C52")

    ChrTalk(
        0xFE,
        (
            "适合在研究中吃的饭，\x01",
            "果然还要数蔡斯的传统料理啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "要是蒂亚利也跟过来就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "整天呆在研究室，\x01",
            "头脑中是不会涌现出什么新构想的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDC")

    label("loc_C52")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "呼呼，适合在研究中吃的饭，\x01",
            "果然还要数蔡斯的传统料理啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然经常会被美食家\x01",
            "批评说缺乏细腻……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过在刺激头脑这点上，\x01",
            "没有什么能比得过蔡斯的料理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "身为一名研究员，\x01",
            "很少会有\x01",
            "享受美食的空闲时间的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为不知道\x01",
            "什么时候就会找到\x01",
            "研究的线索。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDC")

    TalkEnd(0xFE)
    Return()

    # Function_7_963 end

    def Function_8_DE0(): pass

    label("Function_8_DE0")

    SetChrFlags(0xF, 0x10)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_E58")

    ChrTalk(
        0xFE,
        (
            "呼呼，\x01",
            "今天可是特别烦累的一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来要喝上一杯，\x01",
            "舒缓一下压力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1095")

    label("loc_E58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EC7")

    ChrTalk(
        0xFE,
        (
            "呼呼，\x01",
            "今天可是特别烦累的一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来要喝上一杯，\x01",
            "舒缓一下压力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_1095")

    label("loc_EC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_F6C")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "难道你们把书拿来了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过正如你们所见，\x01",
            "现在已经下班了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工作的事情，\x01",
            "现在还是不要谈了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_8C(0xFE, 270, 400)
    Jump("loc_1095")

    label("loc_F6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1033")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "难道你们是来谈工作的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过正如你们所见，\x01",
            "现在已经下班了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工作的事情，\x01",
            "现在还是不要谈了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_8C(0xFE, 270, 400)
    Jump("loc_1095")

    label("loc_1033")


    ChrTalk(
        0xFE,
        (
            "呼呼，\x01",
            "今天可是特别烦累的一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来要喝上一杯，\x01",
            "舒缓一下压力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_1095")

    TalkEnd(0xFE)
    Return()

    # Function_8_DE0 end

    def Function_9_1099(): pass

    label("Function_9_1099")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1127")

    ChrTalk(
        0xFE,
        (
            "真是的！\x01",
            "好不容易参加了营救博士的作战……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但却不能向别人夸耀这件事，\x01",
            "真是痛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125F")

    label("loc_1127")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "哟，\x01",
            "你们在要塞那边干得很漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为一名工房船的船员，\x01",
            "我能帮上忙真是感到自豪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过当集装箱被士兵们围住的时候\x01",
            "我紧张得手心都出汗了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……哎呀，因为现在没有事了，\x01",
            "才能这样轻松地谈笑啊。\x01",
            "当时全体船员都是脸色苍白哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125F")

    Jump("loc_13D0")

    label("loc_1262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_13D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_12FD")

    ChrTalk(
        0xFE,
        (
            "明天工房船\x01",
            "似乎又要出动\x01",
            "去雷斯顿要塞执行任务了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "最近来自军方的任务也太多了点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D0")

    label("loc_12FD")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "明天工房船\x01",
            "似乎又要出动\x01",
            "去雷斯顿要塞执行任务了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "现在大家都在做出动的准备吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是在这种时候，\x01",
            "我觉得自己是个驾驶员真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D0")

    TalkEnd(0xFE)
    Return()

    # Function_9_1099 end

    def Function_10_13D4(): pass

    label("Function_10_13D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_147A")

    ChrTalk(
        0xFE,
        (
            "我特地来找兰达那家伙，\x01",
            "谁知他已经回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没办法。\x01",
            "既然难得来一趟，\x01",
            "至少要好好享受一下怀旧的风味吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_147A")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "呼呼，什么呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我特地来找兰达那家伙，\x01",
            "谁知他已经回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是个让人捉摸不透的家伙。\x01",
            "和年轻的时候真是一点都没变。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1546")

    TalkEnd(0xFE)
    Return()

    # Function_10_13D4 end

    def Function_11_154A(): pass

    label("Function_11_154A")

    Return()

    # Function_11_154A end

    def Function_12_154B(): pass

    label("Function_12_154B")

    Call(0, 13)
    Return()

    # Function_12_154B end

    def Function_13_1550(): pass

    label("Function_13_1550")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1607")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "买东西\x01",          # 1
            "让他看食材\x01",      # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DB")
    OP_0D()
    OP_A9(0x41)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_15DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F3")
    Call(1, 2)
    TalkEnd(0x9)
    Return()

    label("loc_15F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1604")
    TalkEnd(0x9)
    Return()

    label("loc_1604")

    Jump("loc_1675")

    label("loc_1607")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1664")
    OP_0D()
    OP_A9(0x41)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_1664")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1675")
    TalkEnd(0x9)
    Return()

    label("loc_1675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_16CD")

    ChrTalk(
        0x9,
        (
            "谢了。\x01",
            "今天多亏你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "敬请期待\x01",
            "本店全新的菜单吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BC")

    label("loc_16CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_18C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F2")

    ChrTalk(
        0x9,
        (
            "刚才从工房来的客人\x01",
            "好像正在谈论\x01",
            "什么珍贵西红柿的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我问了问能否用在这个新菜谱里面，\x01",
            "于是就得到了样品……\x01",
            "这可是非常合适啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "马上去工房打听一下\x01",
            "那个西红柿的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "同时也预定将它\x01",
            "尽快添加到店里的菜单上。\x01",
            "敬请期待哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C1")

    label("loc_17F2")

    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "哦，是你们啊。\x01",
            "之前多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "刚才，\x01",
            "我去了工房和他们商谈\x01",
            "关于那个西红柿的供货问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "离加入店里菜单的日子\x01",
            "已经不远了。\x01",
            "敬请期待哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C1")

    Jump("loc_28BC")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1998")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(
        0x9,
        "哦，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们这边的午餐时间\x01",
            "也正好刚刚结束，\x01",
            "可以休息一下喘口气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哦，对了。\x01",
            "你们想尝尝『苦西红柿三明治』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F还、还是算了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1995")

    label("loc_1950")


    ChrTalk(
        0x9,
        "哦，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们这边的午餐时间\x01",
            "也正好刚刚结束，\x01",
            "可以休息一下喘口气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你们请随便坐吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1995")

    Jump("loc_28BC")

    label("loc_1998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1A3C")

    ChrTalk(
        0x9,
        (
            "我们这里\x01",
            "每天都在开发新的菜谱，\x01",
            "真是非常繁忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "同时也得注意\x01",
            "不要累坏了身子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C44")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1AA4")

    ChrTalk(
        0x9,
        (
            "这里每天\x01",
            "都是那么繁忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "同时也得注意\x01",
            "不要累坏了身子呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C44")

    label("loc_1AA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BA2")
    OP_A2(0xB)

    ChrTalk(
        0x9,
        (
            "嗯，每天这里都\x01",
            "持续着忙碌的日子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为除了平常的工作，\x01",
            "还要开发新的菜谱\x01",
            "来满足客人的需要。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这样拼命地工作，\x01",
            "一定会把身体搞坏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "忙碌的同时也要注意身体。\x01",
            "你们也要注意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C44")

    label("loc_1BA2")

    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "嗯，每天这里都\x01",
            "持续着忙碌的日子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这样拼命地工作，\x01",
            "一定会把身体搞坏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "忙碌的同时也要注意身体。\x01",
            "你们也要注意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C44")

    Jump("loc_28BC")

    label("loc_1C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1D6E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1CFF")

    ChrTalk(
        0x9,
        "唔，该死。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "乌尔斯已经回去了，\x01",
            "兰达也不在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……没办法，工作吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "必须研究一下\x01",
            "那个西红柿该用什么方法烹饪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D6B")

    label("loc_1CFF")


    ChrTalk(
        0x9,
        "唔，该死。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "乌尔斯已经回去了，\x01",
            "兰达也不在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "……没办法，工作吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1D6B")

    Jump("loc_28BC")

    label("loc_1D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1E0E")

    ChrTalk(
        0x9,
        (
            "工房那里\x01",
            "似乎发生了什么骚乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那里聚集了大量的先进技术，\x01",
            "大概小偷是瞄准了这一点，\x01",
            "想盗走什么研究成果吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BC")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2016")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1E69")

    ChrTalk(
        0x9,
        "那么，老爷子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "先帮我尝尝\x01",
            "这个西红柿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2013")

    label("loc_1E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1EA6")

    ChrTalk(
        0x9,
        (
            "那么，老爷子。\x01",
            "今天咱们聊些什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2013")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F63")
    OP_A2(0xB)

    ChrTalk(
        0x9,
        (
            "最近一段时间\x01",
            "在乌尔斯外出的时候\x01",
            "他就在使劲地工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "今天将工作全部交给他了，\x01",
            "我要继续构想我的新菜谱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2013")

    label("loc_1F63")

    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "最近一段时间\x01",
            "在乌尔斯外出的时候\x01",
            "他就在使劲地工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "今天将工作全部交给他了，\x01",
            "我决心一秒都不再工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2013")

    Jump("loc_28BC")

    label("loc_2016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_21BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2041")

    ChrTalk(
        0x9,
        (
            "老爷子！\x01",
            "煎肉来了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_2041")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2105")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "刚刚乌尔斯\x01",
            "那家伙出去了，\x01",
            "只好我自己来掌勺……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "偶尔自己亲自动动手，\x01",
            "觉得其实做饭还是很有乐趣的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "在新菜谱里\x01",
            "使用那个西红柿的构想\x01",
            "也涌现在我脑子里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_2105")

    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "刚刚乌尔斯\x01",
            "那家伙出去了，\x01",
            "只好我自己来掌勺……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "偶尔自己亲自动动手，\x01",
            "觉得其实做饭还是很有乐趣的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "新菜谱的构想\x01",
            "也涌现在我脑子里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BB")

    Jump("loc_28BC")

    label("loc_21BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2282")

    ChrTalk(
        0x9,
        (
            "唔，\x01",
            "不过那可是道很刺激的料理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "传统料理的菜谱\x01",
            "也已经用完了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不快点想出新点子来\x01",
            "就糟糕了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2301")

    label("loc_2282")

    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "每天都吃同样东西的话，\x01",
            "就算再好吃也会感到厌烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "老爷子\x01",
            "是一个任性的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2301")

    Jump("loc_28BC")

    label("loc_2304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2477")

    ChrTalk(
        0x9,
        (
            "昨天整个城市的导力\x01",
            "好像全部停止了，\x01",
            "还引起了大骚动哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "话说回来，\x01",
            "现在的年轻人\x01",
            "根本无法想象没有导力的世界。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "照明啊，采暖啊，\x01",
            "打扫啊，洗涤啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "日常生活和工作\x01",
            "渐渐地都交给了导力器处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这样一想，\x01",
            "普及推广导力器的拉赛尔博士\x01",
            "实在是太伟大了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BC")

    label("loc_2477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_27E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2588")

    ChrTalk(
        0x9,
        (
            "反正搞研究的人身体不好\x01",
            "这种事也不是今天才开始的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "蔡斯的料理\x01",
            "就是为他们设计出来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "做法和吃法都很简单，\x01",
            "作为食品，营养也很丰富……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这也是蔡斯的厨师\x01",
            "所追求的理想料理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DE")

    label("loc_2588")

    OP_A2(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_END)), "loc_2662")

    ChrTalk(
        0x9,
        (
            "蔡斯的料理\x01",
            "多数是为了没什么空闲的技师\x01",
            "而做的快餐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "做法和吃法都很简单，\x01",
            "作为食品，营养也很丰富……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这也是蔡斯的厨师\x01",
            "所追求的理想料理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DE")

    label("loc_2662")

    OP_A2(0x576)

    ChrTalk(
        0x9,
        (
            "哦，真少见，\x01",
            "这不是提妲大小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "怎么样，\x01",
            "拉赛尔博士身体还好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯，是的。\x01",
            "要多棒有多棒呢。\x02\x03",
            "他在研究所里闭门不出，\x01",
            "一～直埋头做实验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "也就是说……\x01",
            "还是每天都过着\x01",
            "没有规律的生活啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呼，真是的。\x01",
            "他以为自己几岁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "有时间还是让博士他\x01",
            "到外面走走散散心比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27DE")

    Jump("loc_28BC")

    label("loc_27E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_285F")

    ChrTalk(
        0x9,
        (
            "我这里还供应\x01",
            "传统的蔡斯料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "『简单又高效』……\x01",
            "这是蔡斯料理的特点哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28BC")

    label("loc_285F")

    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "噢，欢迎光临。\x01",
            "以前没见过你们，是旅行者吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么，\x01",
            "在这里好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28BC")

    TalkEnd(0x9)
    Return()

    # Function_13_1550 end

    def Function_14_28C0(): pass

    label("Function_14_28C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_29C8")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2958")

    ChrTalk(
        0xFE,
        (
            "露依赛她的工作\x01",
            "终于也步入正轨了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之后，只要祈祷老板的新菜谱\x01",
            "像平常一样美味就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C5")

    label("loc_2958")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "不知何时开始\x01",
            "老板又在构思新菜谱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯，既期待又有点不安，\x01",
            "两种感情混杂在一起真是很微妙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C5")

    Jump("loc_33E2")

    label("loc_29C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2A75")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2A11")

    ChrTalk(
        0xFE,
        (
            "呼呼，露依赛她的新工作\x01",
            "要是能进展顺利就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A72")

    label("loc_2A11")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "午饭时间终于结束了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后就是轻松地处理\x01",
            "傍晚之前的准备工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A72")

    Jump("loc_33E2")

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2C05")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2B33")

    ChrTalk(
        0xFE,
        (
            "虽然工作的时候要热心，\x01",
            "不过一点空闲都没有也不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只有工作的人生\x01",
            "不是一点意思都没有吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "话说回来，像我们的老板那样\x01",
            "完全不工作也很让人头痛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C02")

    label("loc_2B33")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "昨天，\x01",
            "我到露依赛家试着做了做\x01",
            "向老板学成的汤……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她好像很忙，\x01",
            "连吃饭的时间都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过她妹妹乌缇\x01",
            "跟我说汤很好喝，\x01",
            "这样看来还是不错的嘛……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C02")

    Jump("loc_33E2")

    label("loc_2C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2D15")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2CB9")

    ChrTalk(
        0xFE,
        (
            "露依赛受到\x01",
            "导力文明的毒害，\x01",
            "运动方面完全不在行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "她是那种一个人玩相扑\x01",
            "也会受重伤的类型。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D12")

    label("loc_2CB9")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "喂喂，听说了吗？\x01",
            "中央工房出事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "露依赛说今天\x01",
            "她也要去上班的。\x01",
            "有点担心她啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D12")

    Jump("loc_33E2")

    label("loc_2D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2E23")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2D78")

    ChrTalk(
        0xFE,
        "可恶，气死了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明没有多少客人来，\x01",
            "却还这么忙，真让人不爽！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E20")

    label("loc_2D78")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "唔～然后是煎肉……\x01",
            "啊、不对，是先做汤吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呜呜，不知什么时候\x01",
            "洗物槽已经被盘子给堆满了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊，老板。\x01",
            "拜托了，帮我分担一些工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E20")

    Jump("loc_33E2")

    label("loc_2E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2FB5")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2EF8")

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "露依赛最近也有点奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "请她来吃饭也不来，\x01",
            "好像都不和妹妹一同出门了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "觉得她一点空闲都没有啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB2")

    label("loc_2EF8")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "……真是的，露依赛那家伙。\x01",
            "只有这种时候才会想到我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说什么自己的工作很忙，\x01",
            "照顾她妹妹的任务\x01",
            "就硬推给我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哼，说起来，\x01",
            "那家伙明明是有时间的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB2")

    Jump("loc_33E2")

    label("loc_2FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3109")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_301F")

    ChrTalk(
        0xFE,
        (
            "仔细想想，\x01",
            "当时我竟然没从楼梯上摔下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼，我真厉害啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3106")

    label("loc_301F")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "唉～\x01",
            "昨天真是糟透了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那时候我正好\x01",
            "在二楼清理桌子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正要下楼梯时，\x01",
            "突然店里一片漆黑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我现在已经想不起来\x01",
            "当时是怎么保护盘子没有摔碎的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3106")

    Jump("loc_33E2")

    label("loc_3109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_326B")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_317E")

    ChrTalk(
        0xFE,
        (
            "不过，如果这个就是菜式的话，\x01",
            "即使是我也可以轻易地做出来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "下次去女朋友家做做看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3268")

    label("loc_317E")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "我还是有点\x01",
            "不敢相信呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尝了一下刚才偷工减料做的汤，\x01",
            "竟然那么有效果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这只不过是把材料投进锅里\x01",
            "用火煮煮就好的汤而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(
        0xFE,
        "我对你要重新评价了，老板。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你啊，\x01",
            "不是个单纯的懒人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3268")

    Jump("loc_33E2")

    label("loc_326B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33E2")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_331F")

    ChrTalk(
        0xFE,
        (
            "这种汤据说有种\x01",
            "提高集中力的效果呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……不过，真的有效吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实，不就是把水、鸡骨头、青菜\x01",
            "还有胡椒放到一起煮吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E2")

    label("loc_331F")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "放入鸡骨头……\x01",
            "接着是青菜、胡椒和水吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后一边等\x01",
            "一边煮一会儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……啊？　\x01",
            "老板的菜谱\x01",
            "到这里就写完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "………………\x01",
            "难道这样就可以了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E2")

    TalkEnd(0xFE)
    Return()

    # Function_14_28C0 end

    def Function_15_33E6(): pass

    label("Function_15_33E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3451")

    ChrTalk(
        0xFE,
        "呵呵，老板。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天你身上运动了的部分\x01",
            "不会只有嘴旁边的肌肉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C34")

    label("loc_3451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_34F4")

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "竟然可以一本正经地说出那样的台词……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "不愧是老板啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C34")

    label("loc_34F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_35F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_355F")

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "当时光顾忙着说话，\x01",
            "完全没有注意到骚动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F3")

    label("loc_355F")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "以前工房也常常会有小偷出现……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过这一回\x01",
            "似乎是相当大的案子呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F3")

    Jump("loc_3C34")

    label("loc_35F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_36D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_365D")

    ChrTalk(
        0xFE,
        (
            "好吧，\x01",
            "我就跟老板你说说\x01",
            "我去卢安的旅行见闻吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D0")

    label("loc_365D")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "年轻人果然就是要劳动才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看着他们麻利工作的身姿，\x01",
            "自己心情也舒畅啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D0")

    Jump("loc_3C34")

    label("loc_36D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_378A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3736")

    ChrTalk(
        0xFE,
        (
            "老板，\x01",
            "煎肉还没好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "客人们都等着呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3787")

    label("loc_3736")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "乌尔斯那孩子\x01",
            "竟然擅自跑出去了。\x01",
            "我也来帮帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，中午这一会儿\x01",
            "应该是忙得团团转的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3787")

    Jump("loc_3C34")

    label("loc_378A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3808")

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "真是感到郁闷啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每天都来这里，\x01",
            "不管什么样的菜都吃腻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～\x01",
            "想吃点刺激的菜呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C34")

    label("loc_3808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_38F3")

    ChrTalk(
        0xFE,
        "真是的，每个人都是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不能使用导力器，\x01",
            "一个个都慌乱得不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又不去试想一下，\x01",
            "没有导力的年代人家是怎么生活的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C34")

    label("loc_38F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3B3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39B6")
    OP_A2(0x577)

    ChrTalk(
        0xFE,
        (
            "呵呵，拉赛尔那家伙\x01",
            "好像还在很努力地工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我曾经也是个钟表工匠，\x01",
            "还和那个家伙一起工作过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "后来我的眼力不好，就退休不干了。\x01",
            "真是羡慕拉赛尔现在还在工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3B")

    label("loc_39B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A36")

    ChrTalk(
        0xFE,
        (
            "话又说回来，\x01",
            "贝恩的料理还是挺简单方便的，\x01",
            "味道方面也算是让人放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也就是说那家伙\x01",
            "有自己的一套做料理的聪明方法吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3B")

    label("loc_3A36")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "要特别注意\x01",
            "这里的老板贝恩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他最擅长给各种料理\x01",
            "加上各种各样的名堂来偷工减料了。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    OP_69(0x9, 0x3E8)

    ChrTalk(
        0x9,
        "够了吧，老爷子！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "别老是跟客人\x01",
            "说些容易误会的话！\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)

    ChrTalk(
        0xFE,
        (
            "呵呵，\x01",
            "我可没有瞎说啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B3B")

    Jump("loc_3C34")

    label("loc_3B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3BA3")

    ChrTalk(
        0xFE,
        (
            "唉呀，\x01",
            "我是刚刚从卢安旅行回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是呆在家里舒服啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C34")

    label("loc_3BA3")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "好不容易才回到家里来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉呀，\x01",
            "我是刚刚从卢安旅行回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "尽管可以尽情的游玩，\x01",
            "不过还是呆在家里舒服啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C34")

    TalkEnd(0xFE)
    Return()

    # Function_15_33E6 end

    def Function_16_3C38(): pass

    label("Function_16_3C38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3D72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3CD7")

    ChrTalk(
        0xFE,
        (
            "虽说多数是些很简单的菜，\x01",
            "不过味道可不差嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不为吃饭花时间， \x01",
            "正好符合技术人员的性格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D72")

    label("loc_3CD7")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "每天呆在酒店里也不是办法，\x01",
            "于是就来这里尝尝看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是符合工房都市的特点，\x01",
            "菜色简单而味道也不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D72")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C38 end

    SaveToFile()

Try(main)
