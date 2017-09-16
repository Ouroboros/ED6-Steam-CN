from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1510   ._SN',
        MapName             = 'Bose',
        Location            = 'T1510.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '雷纳德',                               # 9
        '索菲娜',                               # 10
        '罗伊德',                               # 11
        '艾露凯',                               # 12
        '阿妮特',                               # 13
        '斯丁克',                               # 14
        '亚妮拉丝',                             # 15
        '雪拉扎德',                             # 16
        '奥利维尔',                             # 17
        '器皿',                                 # 18
        '器皿',                                 # 19
        '器皿',                                 # 20
        '咖啡',                                 # 21
        '咖啡',                                 # 22
        '咖啡',                                 # 23
        '咖啡',                                 # 24
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
        Unknown_30              = 225,
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01183 ._CH',             # 03
        'ED6_DT07/CH01213 ._CH',             # 04
        'ED6_DT07/CH01623 ._CH',             # 05
        'ED6_DT07/CH01630 ._CH',             # 06
        'ED6_DT07/CH00023 ._CH',             # 07
        'ED6_DT07/CH00033 ._CH',             # 08
        'ED6_DT06/CH20020 ._CH',             # 09
        'ED6_DT06/CH20021 ._CH',             # 0A
        'ED6_DT06/CH20049 ._CH',             # 0B
        'ED6_DT07/CH01180 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01183P._CP',             # 03
        'ED6_DT07/CH01213P._CP',             # 04
        'ED6_DT07/CH01623P._CP',             # 05
        'ED6_DT07/CH01630P._CP',             # 06
        'ED6_DT07/CH00023P._CP',             # 07
        'ED6_DT07/CH00033P._CP',             # 08
        'ED6_DT06/CH20020P._CP',             # 09
        'ED6_DT06/CH20021P._CP',             # 0A
        'ED6_DT06/CH20049P._CP',             # 0B
        'ED6_DT07/CH01180P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
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
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 13000,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 13700,
        Z                   = 150,
        Y                   = 6400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 15930,
        Z                   = 250,
        Y                   = 6290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 23980,
        Z                   = 300,
        Y                   = 9640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 17080,
        Z                   = 0,
        Y                   = 13470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 16100,
        Z                   = 200,
        Y                   = 6240,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 13450,
        Z                   = 200,
        Y                   = 6320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 15250,
        Z                   = 700,
        Y                   = 6400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327690,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14160,
        Z                   = 700,
        Y                   = 6050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327690,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14790,
        Z                   = 800,
        Y                   = 6500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14450,
        Z                   = 800,
        Y                   = 6650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15000,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14600,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14200,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835017,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 23100,
        TriggerZ            = 0,
        TriggerY            = 6000,
        TriggerRange        = 700,
        ActorX              = 24500,
        ActorZ              = 1500,
        ActorY              = 6100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 80610,
        TriggerZ            = 0,
        TriggerY            = 9100,
        TriggerRange        = 1400,
        ActorX              = 80610,
        ActorZ              = 1500,
        ActorY              = 9100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_362",          # 00, 0
        "Function_1_58D",          # 01, 1
        "Function_2_5AF",          # 02, 2
        "Function_3_5C5",          # 03, 3
        "Function_4_5C6",          # 04, 4
        "Function_5_5EA",          # 05, 5
        "Function_6_12A9",         # 06, 6
        "Function_7_12AE",         # 07, 7
        "Function_8_251D",         # 08, 8
        "Function_9_25B6",         # 09, 9
        "Function_10_2B81",        # 0A, 10
        "Function_11_3053",        # 0B, 11
        "Function_12_3632",        # 0C, 12
        "Function_13_39EC",        # 0D, 13
        "Function_14_449A",        # 0E, 14
        "Function_15_4F97",        # 0F, 15
        "Function_16_67A8",        # 10, 16
        "Function_17_6832",        # 11, 17
        "Function_18_6F68",        # 12, 18
        "Function_19_6FC2",        # 13, 19
        "Function_20_7017",        # 14, 20
    )


    def Function_0_362(): pass

    label("Function_0_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_380")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_4B4")

    label("loc_380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_END)), "loc_38A")
    Jump("loc_4B4")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_3E2")
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 13)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xB, 54800, 0, 3410, 180)
    SetChrPos(0xC, 51130, 0, 5960, 270)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x4)
    Jump("loc_4B4")

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_43A")
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 13)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xB, 54800, 0, 3410, 180)
    SetChrPos(0xC, 51130, 0, 5960, 270)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x4)
    Jump("loc_4B4")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_444")
    Jump("loc_4B4")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_44E")
    Jump("loc_4B4")

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_46C")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4B4")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_476")
    Jump("loc_4B4")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_494")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_4B4")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4B4")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0xE, 0x80)

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_567")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_517")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x10, 13450, 200, 6240, 0)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 11)
    SetChrSubChip(0x12, 1)
    Jump("loc_567")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_END)), "loc_535")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_567")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_558")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrSubChip(0x12, 1)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_567")

    label("loc_558")

    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_575")
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_58C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 16)

    label("loc_58C")

    Return()

    # Function_0_362 end

    def Function_1_58D(): pass

    label("Function_1_58D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A5")
    OP_B1("t1510_y")
    Jump("loc_5AE")

    label("loc_5A5")

    OP_B1("t1510_n")

    label("loc_5AE")

    Return()

    # Function_1_58D end

    def Function_2_5AF(): pass

    label("Function_2_5AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5AF")

    label("loc_5C4")

    Return()

    # Function_2_5AF end

    def Function_3_5C5(): pass

    label("Function_3_5C5")

    Return()

    # Function_3_5C5 end

    def Function_4_5C6(): pass

    label("Function_4_5C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E9")
    OP_8D(0xFE, 50200, 5000, 54800, 6300, 2000)
    Jump("Function_4_5C6")

    label("loc_5E9")

    Return()

    # Function_4_5C6 end

    def Function_5_5EA(): pass

    label("Function_5_5EA")

    TalkBegin(0x8)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64A")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x15)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_64A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_664")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_664")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6D4")

    ChrTalk(
        0x8,
        "噢，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "客人又来钓鱼吗？\x01",
            "请在这里好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_764")

    ChrTalk(
        0x8,
        (
            "那边的两个人，\x01",
            "喝得真是不少啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我必须要去拉文努村\x01",
            "多订购一些果实酒才行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_7EA")

    ChrTalk(
        0x8,
        "哟，鱼钓得怎么样啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果钓到什么好东西的话，\x01",
            "不妨让我们帮你做成菜哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_84D")

    ChrTalk(
        0x8,
        "唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "今天又进了很新鲜的鱼。\x01",
            "敬请期待我们的料理吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_8FF")

    ChrTalk(
        0x8,
        "来找罗伊德大叔的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果你们不介意的话，\x01",
            "一定要留在这里住一晚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "刚才正好有一个房间\x01",
            "因为取消预定空出来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCB")
    OP_A2(0x33C)
    OP_28(0x38, 0x1, 0x2)
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    SetChrSubChip(0x8, 0)

    ChrTalk(
        0x8,
        (
            "欢迎来到川蝉亭。\x01",
            "请问几位客人是来留宿的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯……也算是吧。\x01",
            "其实我们不单是来留宿的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们还要找一个人。\x02\x03",
            "请问在这里留宿的客人当中，\x01",
            "有没有钓鱼爱好者呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，说到钓鱼，\x01",
            "这里的大部分客人都非常喜欢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F听说昨天来留宿的老伯\x01",
            "认识这里的一位钓友。\x02\x03",
            "不知道你是否认识那位钓友呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊啊，你说罗伊德大叔吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们一说钓友，\x01",
            "我就知道是罗伊德大叔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F罗伊德？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，一位从王都来的客人，\x01",
            "自称是专业的前卫钓鱼者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "听说他也是王都的\x01",
            "『钓公师团』的成员之一。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCC")

    ChrTalk(
        0x101,
        (
            "#506F听、听起来好像很厉害啊。\x02\x03",
            "#000F那么他现在在哪呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈哈，这个时间他应该\x01",
            "正在悠然自得地垂钓吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "到里面的栈桥就可以找到他了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_DC6")

    label("loc_CCC")


    ChrTalk(
        0x101,
        (
            "#506F听、听起来好像很厉害啊。\x02\x03",
            "#000F想问一下他是不是\x01",
            "在外面钓鱼的那个大叔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊啊，我想就是他。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们大声叫他就行了，\x01",
            "如果太小声的话他可能听不见。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC6")

    EventEnd(0x1)
    Jump("loc_E59")

    label("loc_DCB")


    ChrTalk(
        0x8,
        (
            "罗依德先生现在应该\x01",
            "正在悠然自得地垂钓吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "到里面的栈桥就可以找到他了。\x02",
    )

    CloseMessageWindow()

    label("loc_E59")

    Jump("loc_12A5")

    label("loc_E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5E")
    OP_A2(0x2)

    ChrTalk(
        0x8,
        "说起来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "王国军也曾经到这里\x01",
            "打听失踪的定期船的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过，\x01",
            "这里平时可是平静得不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "别说可疑的人物，\x01",
            "就连定期船也不会在这里出现。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE0")

    label("loc_F5E")


    ChrTalk(
        0x8,
        (
            "王国军也曾经到这里\x01",
            "打听失踪的定期船的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过，\x01",
            "这里平时可是平静得不得了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE0")

    Jump("loc_12A5")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B6")
    OP_A2(0x2)

    ChrTalk(
        0x8,
        "说起来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "从这里向西北方向望去，\x01",
            "能看到一座很古老的塔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个建筑物好像\x01",
            "被称为『琥珀之塔』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那座塔究竟是\x01",
            "为了什么而建造出来的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_113D")

    label("loc_10B6")


    ChrTalk(
        0x8,
        (
            "从这里向西北方向望去，\x01",
            "能看到一座被称为\x01",
            "『琥珀之塔』的很古老的塔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那座塔究竟是\x01",
            "为了什么而建造出来的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113D")

    Jump("loc_12A5")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_12A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120D")
    OP_A2(0x2)

    ChrTalk(
        0x8,
        "噢，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这里是我们兄妹俩经营的\x01",
            "瓦雷利亚湖北岸旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，如果没什么急事，\x01",
            "请在这里好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A5")

    label("loc_120D")


    ChrTalk(
        0x8,
        (
            "这里是我们兄妹俩经营的\x01",
            "瓦雷利亚湖北岸旅馆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，如果没什么急事，\x01",
            "请在这里好好放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A5")

    TalkEnd(0x8)
    Return()

    # Function_5_5EA end

    def Function_6_12A9(): pass

    label("Function_6_12A9")

    Call(0, 7)
    Return()

    # Function_6_12A9 end

    def Function_7_12AE(): pass

    label("Function_7_12AE")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130E")
    OP_0D()
    OP_A9(0x14)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_130E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_131F")
    TalkEnd(0x9)
    Return()

    label("loc_131F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1393")

    ChrTalk(
        0x9,
        "今天真是好天气啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呵呵，\x01",
            "被子都应该晒干了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_145A")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "这绝对不是我在自夸，\x01",
            "我哥烧的鱼可是非常好吃的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "请你们一定要尝一下啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_1537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F7")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "本店的料理\x01",
            "都是用从渔夫那里\x01",
            "直接购进的鲜鱼制成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "所以说呢，来本店的客人\x01",
            "都能品尝到最新鲜的料理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1534")

    label("loc_14F7")


    ChrTalk(
        0x9,
        "你在找同伴的那个男孩子吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不好意思，\x01",
            "他好像没有到这边来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1534")

    Jump("loc_2519")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_19CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D5")

    ChrTalk(
        0x9,
        (
            "各位，\x01",
            "来到这里可不要错过钓鱼的乐趣啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我们也准备了租借用的钓竿，\x01",
            "请随意使用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C8")

    label("loc_15D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178D")
    EventBegin(0x0)
    OP_69(0x9, 0x3E8)
    OP_A2(0x344)

    ChrTalk(
        0x101,
        (
            "#000F那个……\x02\x03",
            "请问你们这里有钓鱼竿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "嗯，有啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "您是想钓鱼吧。\x01",
            "来留宿的客人不用付租金。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊，真的吗？\x01",
            "太幸运了㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x332, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "钓鱼竿\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#501F嗯，虽说是租借用的钓鱼竿，\x01",
            "不过质量还挺不错的嘛。\x02\x03",
            "那我就不客气地拿去用了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呵呵……\x01",
            "请好好享受钓鱼的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_19C8")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190B")
    OP_A2(0x1)

    ChrTalk(
        0x101,
        (
            "#501F想问问，\x01",
            "你们这里有什么好的钓鱼场所呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "让我想想……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "说到好的钓鱼场所，\x01",
            "肯定是湖上的小岛上……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过我觉得还是\x01",
            "栈桥周围的环境最好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "水底的地形比较复杂，\x01",
            "所以那里的鱼也会有比较多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C8")

    label("loc_190B")


    ChrTalk(
        0x9,
        (
            "我觉得还是\x01",
            "栈桥周围的环境最好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "水底的地形比较复杂，\x01",
            "所以那里的鱼也会有比较多。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C8")

    Jump("loc_2519")

    label("loc_19CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_208B")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 22480, 0, 5710, 90)
    SetChrPos(0x102, 22370, 0, 6610, 90)
    SetChrPos(0x103, 21380, 0, 5470, 90)
    SetChrPos(0x104, 22060, 0, 4510, 45)
    TurnDirection(0x9, 0x101, 0)
    OP_69(0x9, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6C")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        "哎呀，客人是要留宿的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯，有这个打算……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，等一下。\x02\x03",
            "如果有什么事情还没做的话，\x01",
            "还是趁这个时间去完成比较好。\x02\x03",
            "要是我们租了房间，\x01",
            "那就不能再回柏斯了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，的确是啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Jump("loc_1B94")

    label("loc_1B6C")


    ChrTalk(
        0x9,
        "啊，你们要租房间吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1B94")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【暂时不租】\x01",      # 0
            "【租房间】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C01"),
        (1, "loc_1C7D"),
        (SWITCH_DEFAULT, "loc_2088"),
    )


    label("loc_1C01")


    ChrTalk(
        0x9,
        "我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "你们可以先预约，\x01",
            "等办完事情再来。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0x9, 255)
    Jump("loc_2088")

    label("loc_1C7D")


    ChrTalk(
        0x9,
        "我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "各位请这边走。\x01",
            "我带你们到房间去。\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    OP_A2(0x33E)
    OP_28(0x38, 0x1, 0x40)
    OP_28(0x16, 0x4, 0x40)
    OP_28(0x18, 0x4, 0x40)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x9, 104400, 0, 13140, 180)
    SetChrPos(0x101, 106160, 0, 11480, 180)
    SetChrPos(0x102, 105150, 0, 10900, 180)
    SetChrPos(0x104, 104580, 0, 11870, 180)
    SetChrPos(0x103, 105850, 0, 12550, 180)
    OP_6D(107290, 0, 4690, 0)
    OP_6B(2800, 0)
    Sleep(1000)
    FadeToBright(1500, 0)
    OP_6D(107690, 0, 12420, 3000)
    OP_0D()

    ChrTalk(
        0x9,
        "这里就是客人你们的房间。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么，在享用晚饭之前，\x01",
            "大家就先在这里好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x4)
    OP_8C(0x9, 225, 300)
    OP_8E(0x9, 0x19604, 0x0, 0x3282, 0x7D0, 0x0)

    def lambda_1E16():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E16)
    OP_8E(0x9, 0x18F7E, 0x0, 0x3282, 0x7D0, 0x0)
    SetChrFlags(0x9, 0x80)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F的确是一间好房子啊。\x01",
            "和城市的酒店相比，真的别有一番风味。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F#2P嗯，感觉真好。\x02\x03",
            "而且租金又不是很贵。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 225, 400)

    ChrTalk(
        0x103,
        (
            "#020F#1P呵呵，好了……\x02\x03",
            "在今夜行动之前，\x01",
            "我们就先好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(
        0x104,
        "#031F呵呵，不错的提议。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        (
            "#004F#2P啊，虽然放松一下也不错……\x01",
            "可是这么悠然自得地休息可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F#1P休息的时候就该好好休息。\x01",
            "这也是游击士的工作啊。\x02\x03",
            "吃零食也好，到外面散步也好，\x01",
            "总之现在可以自由活动哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2088")

    Jump("loc_2519")

    label("loc_208B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_20EC")

    ChrTalk(
        0x9,
        (
            "各位客人您好。\x01",
            "欢迎来到川蝉亭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果想留宿的话，\x01",
            "请先到我这里来登记。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_20EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_21AD")

    ChrTalk(
        0x9,
        (
            "王国军好像到\x01",
            "琥珀之塔周边进行了调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而且他们好像\x01",
            "发现了一个可疑人物。\x01",
            "听说还是一位考古学者。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_21AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_22F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226E")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "这里是原本是\x01",
            "雷纳德哥哥经营的旅馆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我来这里玩的时候\x01",
            "被这里的气氛所深深吸引。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "所以我就干脆\x01",
            "来帮哥哥打理这里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F2")

    label("loc_226E")


    ChrTalk(
        0x9,
        (
            "我来这里玩的时候\x01",
            "被这里的气氛所深深吸引……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "所以我就干脆\x01",
            "来帮哥哥打理这里了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F2")

    Jump("loc_2519")

    label("loc_22F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2451")
    OP_A2(0x1)

    ChrTalk(
        0x9,
        (
            "欢迎来到川蝉亭。\x01",
            "请问客人是来留宿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F嗯……这个嘛，\x01",
            "其实不是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哦，真是遗憾呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这里湖边景色十分漂亮，\x01",
            "而且全天都吹着清爽自然的风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "在这里休闲度假是最适合不过了。\x01",
            "以后有机会一定要来这里休息一下哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_2451")


    ChrTalk(
        0x9,
        (
            "这里湖边景色十分漂亮，\x01",
            "而且全天都吹着清爽自然的风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "在这里休闲度假是最适合不过了。\x01",
            "以后有机会一定要来这里休息一下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2519")

    TalkEnd(0x9)
    Return()

    # Function_7_12AE end

    def Function_8_251D(): pass

    label("Function_8_251D")

    TalkBegin(0xA)

    ChrTalk(
        0xFE,
        (
            "今天又让那家伙\x01",
            "逃过了我一次的追捕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来要选择一个更好的位置才行，\x01",
            "再努力一下试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_8_251D end

    def Function_9_25B6(): pass

    label("Function_9_25B6")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_261F")

    ChrTalk(
        0xFE,
        (
            "一到傍晚，\x01",
            "这附近就被夕阳染成橘黄色，\x01",
            "非常漂亮呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_261F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_27C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2718")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "啊啊，\x01",
            "又这样悠悠闲闲地过了一天啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "工作累了的话，\x01",
            "适当放松一下也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说回去还有很多工作要做，\x01",
            "不过休息的时候还是要好好休息。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C2")

    label("loc_2718")


    ChrTalk(
        0xFE,
        (
            "工作累了的话，\x01",
            "适当放松一下也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说回去还有很多工作要做，\x01",
            "不过休息的时候还是要好好休息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C2")

    Jump("loc_2B7D")

    label("loc_27C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_2822")

    ChrTalk(
        0xFE,
        (
            "啊呀，\x01",
            "你们也是来这里投宿的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请多关照哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_29C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2925")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "明年我要和老公一起\x01",
            "来这里度假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每年他只有看家的份，\x01",
            "也真是挺可怜的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，和女儿两个人来，\x01",
            "这种感觉也蛮不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C3")

    label("loc_2925")


    ChrTalk(
        0xFE,
        (
            "明年我要和老公一起\x01",
            "来这里度假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每年他只有看家的份，\x01",
            "也真是挺可怜的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C3")

    Jump("loc_2B7D")

    label("loc_29C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2A30")

    ChrTalk(
        0xFE,
        (
            "柏斯的这间川蝉亭\x01",
            "和蔡斯的红叶亭，\x01",
            "我都非常喜欢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2AC5")

    ChrTalk(
        0xFE,
        (
            "虽然顺着那些旅游胜地\x01",
            "一路游览下来也很不错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我还是喜欢像这样\x01",
            "悠然自得的旅行生活啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2B76")

    ChrTalk(
        0xFE,
        "今天天气真是好呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我决定下午\x01",
            "在湖边好好看书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，不过看书之余，\x01",
            "也想试试钓鱼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7D")

    label("loc_2B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2B7D")

    label("loc_2B7D")

    TalkEnd(0xB)
    Return()

    # Function_9_25B6 end

    def Function_10_2B81(): pass

    label("Function_10_2B81")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_END)), "loc_2C0F")

    ChrTalk(
        0xFE,
        (
            "差不多到吃饭的时间了。\x01",
            "今天的菜会是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这里的菜还是可以期待一下的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_2CF0")

    ChrTalk(
        0xFE,
        (
            "本店的大部分客人\x01",
            "都是为了钓鱼而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之前从柏斯来了一个老爷爷，\x01",
            "他为了在这里钓鱼连家也不回，\x01",
            "一钓就是一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也想试试\x01",
            "钓一天的鱼是什么感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 6)), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(
        0xFE,
        "今天的晚饭是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我现在就开始期待了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 5)), scpexpr(EXPR_END)), "loc_2E3C")

    ChrTalk(
        0xFE,
        (
            "从王都来的那个叫罗伊德的人\x01",
            "好像挺古怪的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他钓鱼的时候，无论你怎么叫他，\x01",
            "他也好像完全没有反应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在食堂和他聊天的时候，\x01",
            "他给人的感觉却是很随和很健谈的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2E3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2FB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F44")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "每年的这个时候，\x01",
            "我和母亲\x01",
            "都会到这里来旅游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这里呆上几天\x01",
            "是我们母女的例行公事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "母亲她每年\x01",
            "都很期待这个旅游哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "每次都是我和母亲两个人来，\x01",
            "而把父亲自己丢在家里。\x01",
            "总觉得他有点可怜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB1")

    label("loc_2F44")


    ChrTalk(
        0xFE,
        (
            "每年的这个时候，\x01",
            "我和母亲\x01",
            "都会到这里来旅游。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在这里呆上几天\x01",
            "是我们母女的例行公事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB1")

    Jump("loc_304F")

    label("loc_2FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_304F")

    ChrTalk(
        0xFE,
        (
            "可以品尝美味的料理，\x01",
            "又可以悠闲地度假……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然这是超级的享受，\x01",
            "不过也要注意是否会发胖啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304F")

    TalkEnd(0xC)
    Return()

    # Function_10_2B81 end

    def Function_11_3053(): pass

    label("Function_11_3053")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DD")
    OP_A2(0x35F)
    OP_A2(0x5)

    ChrTalk(
        0x101,
        (
            "#006F（咦……\x01",
            "　这个人莫非是……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯，\x01",
            "　好像和我们一样都是游击士呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F喂，打扰一下？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F蜂蜜苏打水……\x02\x03",
            "#020F好久不见了呢，斯丁克。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "你是……\x01",
            "以前的那个见习游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F没错呢。\x02\x03",
            "托你的福，\x01",
            "现在我已经是正游击士啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼……看起来的确成熟了不少。\x01",
            "在柏斯支部有工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F嗯，现在就正在工作呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近发生了很多事情，\x01",
            "游击士的人手远远不够呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……那就靠你们了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)

    ChrTalk(
        0x101,
        (
            "#002F（是雪拉姐的熟人吧。\x01",
            "　感觉有点恐怖的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（但是那走路的动作……\x01",
            "　看起来应该很厉害吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362E")

    label("loc_33DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F6")
    OP_A2(0x5)

    ChrTalk(
        0x101,
        (
            "#000F啊，您是……\x01",
            "是斯丁克先生吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您会在这里，\x01",
            "难道是发生了什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……我是来消灭通缉魔兽的。\x01",
            "不是什么大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "说起来，你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我从卢格兰老爷子那里听说了，\x01",
            "你们真的是卡西乌斯先生的孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F您认识父亲吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是啊……\x01",
            "以前曾经受过他的照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F唔……\x02\x03",
            "老爸在柏斯地区\x01",
            "熟人也相当多呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯，是呀。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)
    Jump("loc_362E")

    label("loc_35F6")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "……如果能早点得知\x01",
            "卡西乌斯先生的消息就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 0)

    label("loc_362E")

    TalkEnd(0xD)
    Return()

    # Function_11_3053 end

    def Function_12_3632(): pass

    label("Function_12_3632")

    TalkBegin(0xE)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3967")
    OP_A2(0x360)

    ChrTalk(
        0xFE,
        (
            "#814F啊，难道……\x01",
            "这不是雪拉扎德前辈吗？\x02\x03",
            "#850F很久不见了～\x01",
            "自从您去修行之后就再没见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F啊呀，这不是亚妮拉丝嘛。\x01",
            "你在这里做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810嗯～\x01",
            "协会委托我来这边消灭通缉魔兽。\x02\x03",
            "就在刚才，\x01",
            "我终于把工作解决掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是这样啊……\x02\x03",
            "对了，\x01",
            "你已经找到所谓的剑之道了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#819F呵呵，请别问了。\x01",
            "我还处在修行阶段呢。\x02\x03",
            "#810F说起来，\x01",
            "前辈您也是在执行协会的任务吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F是啊，不过我和你的任务性质不同。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F是这样啊……\x02\x03",
            "这个地区最近发生的\x01",
            "不寻常的事情还真多啊。\x02\x03",
            "您路上一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39E8")

    label("loc_3967")


    ChrTalk(
        0xFE,
        (
            "#810F雪拉扎德前辈，\x01",
            "这个地区最近发生了很多不寻常的事情呢。\x02\x03",
            "您路上一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E8")

    TalkEnd(0xE)
    Return()

    # Function_12_3632 end

    def Function_13_39EC(): pass

    label("Function_13_39EC")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A05")
    TalkEnd(0x10)
    Call(0, 17)
    Jump("loc_4496")

    label("loc_3A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_3FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8C")
    EventBegin(0x0)
    OP_A2(0x34A)
    OP_6D(14850, 0, 6330, 1000)

    ChrTalk(
        0xF,
        (
            "#028F唔～\x01",
            "你的酒量也不错嘛。\x02\x03",
            "哦呵呵……正合我意啊㈱\x02\x03",
            "好啦好啦，赶快给我喝！\x01",
            "（咕噜咕噜咕噜……）\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x12, 5)
    OP_0D()
    OP_62(0x10, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#037F等、等一下。\x01",
            "你喝得有点太猛了吧？\x02\x03",
            "这样的话晚上的工作不就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#029F……你说什么……\x02",
    )

    CloseMessageWindow()
    OP_7C(0x0, 0xC8, 0x7D0, 0xC8)

    ChrTalk(
        0xF,
        (
            "#029F哼哼，赖皮演奏家！\x01",
            "难道你不愿意喝我敬你的酒吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#038F哇哇哇……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C47")
    SetChrSubChip(0x10, 1)
    Jump("loc_3C78")

    label("loc_3C47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C5D")
    SetChrSubChip(0x10, 0)
    Jump("loc_3C78")

    label("loc_3C5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C73")
    SetChrSubChip(0x10, 2)
    Jump("loc_3C78")

    label("loc_3C73")

    SetChrSubChip(0x10, 1)

    label("loc_3C78")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#038F艾丝蒂尔君……\x01",
            "你们怎么不帮我说几句啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不好意思啊～\x01",
            "变成这样的话我也阻止不住了。\x02\x03",
            "#006F别担心，\x01",
            "雪拉姐就算喝多少瓶都不会醉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#037F我是说……你们不担心我吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    EventEnd(0x0)
    Jump("loc_3FD7")

    label("loc_3D8C")

    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DAE")
    SetChrSubChip(0x10, 1)
    Jump("loc_3DC9")

    label("loc_3DAE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DC4")
    SetChrSubChip(0x10, 1)
    Jump("loc_3DC9")

    label("loc_3DC4")

    SetChrSubChip(0x10, 2)

    label("loc_3DC9")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F43")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        "#037F她、她真的这么能喝吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F雪拉姐不单是一级的游击士，\x01",
            "而且还是一级的酒场好手呢。\x02\x03",
            "就连我家的老爸也喝不过她。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#037F这、这么厉害啊……\x02\x03",
            "这样说我倒是想看看她喝醉的样子。\x01",
            "不过我还是有点怕怕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FD2")

    label("loc_3F43")


    ChrTalk(
        0x10,
        (
            "#037F虽说想看她有什么大胆的表演，\x01",
            "不过在那之前我可能已经醉了……\x02\x03",
            "唔……这是重大的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD2")

    SetChrSubChip(0x10, 0)

    label("loc_3FD7")

    Jump("loc_4496")

    label("loc_3FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E2")
    EventBegin(0x0)
    OP_A2(0x343)
    OP_6D(14850, 0, 6330, 1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雪拉扎德和奥利维尔\x01",
            "以沁凉的果实酒交杯换盏。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x101, 0xF, 400)

    ChrTalk(
        0x101,
        (
            "#000F雪拉姐呀……\x01",
            "现在还是白天你就喝这么多了。\x02\x03",
            "就算是再清淡的酒也有个限度啊，\x01",
            "喝多了不怕搞坏身体吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_412D")
    SetChrSubChip(0xF, 2)
    Jump("loc_415E")

    label("loc_412D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4143")
    SetChrSubChip(0xF, 1)
    Jump("loc_415E")

    label("loc_4143")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4159")
    SetChrSubChip(0xF, 0)
    Jump("loc_415E")

    label("loc_4159")

    SetChrSubChip(0xF, 2)

    label("loc_415E")

    OP_8C(0xF, 270, 0)
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#021F没问题，没问题。\x01",
            "酒这种东西其实和水差不多嘛。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41C2")
    SetChrSubChip(0x10, 1)
    Jump("loc_41F3")

    label("loc_41C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41D8")
    SetChrSubChip(0x10, 0)
    Jump("loc_41F3")

    label("loc_41D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_41EE")
    SetChrSubChip(0x10, 2)
    Jump("loc_41F3")

    label("loc_41EE")

    SetChrSubChip(0x10, 1)

    label("loc_41F3")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)

    ChrTalk(
        0x10,
        (
            "#035F呵呵，艾丝蒂尔君。\x01",
            "有时候也要适当放松一下自己嘛。\x02\x03",
            "我知道怎么服侍雪拉君，\x01",
            "你们就放心把她交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#007F不，令人担心的倒不是雪拉姐……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#033F？？？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0xF, 0)
    EventEnd(0x0)
    Jump("loc_4496")

    label("loc_42E2")

    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4304")
    SetChrSubChip(0x10, 1)
    Jump("loc_431F")

    label("loc_4304")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_431A")
    SetChrSubChip(0x10, 1)
    Jump("loc_431F")

    label("loc_431A")

    SetChrSubChip(0x10, 2)

    label("loc_431F")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4400")
    OP_A2(0x7)

    ChrTalk(
        0x10,
        (
            "#035F我只是问她要不要喝一杯，\x01",
            "她就很轻易地说ＯＫ没问题。\x02\x03",
            "呵呵，雪拉君也终于开始\x01",
            "注意到我无人能敌的魅力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（过分的自信怕是会弄出人命的……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4491")

    label("loc_4400")


    ChrTalk(
        0x10,
        (
            "#031F呵呵……\x02\x03",
            "如果她醉倒的话，\x01",
            "我会温柔地让她投入我的怀里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F（我为你的无知有点担心……）\x02",
    )

    CloseMessageWindow()

    label("loc_4491")

    SetChrSubChip(0x10, 0)

    label("loc_4496")

    TalkEnd(0x10)
    Return()

    # Function_13_39EC end

    def Function_14_449A(): pass

    label("Function_14_449A")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44B3")
    TalkEnd(0xF)
    Call(0, 17)
    Jump("loc_4F93")

    label("loc_44B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_END)), "loc_49FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4841")
    EventBegin(0x0)
    OP_A2(0x34A)
    OP_6D(14850, 0, 6330, 1000)

    ChrTalk(
        0xF,
        (
            "#028F唔～\x01",
            "你的酒量也不错嘛。\x02\x03",
            "哦呵呵……正合我意啊㈱\x02\x03",
            "好啦好啦，赶快给我喝！\x01",
            "（咕噜咕噜咕噜……）\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x12, 5)
    OP_0D()
    OP_62(0x10, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#037F等、等一下。\x01",
            "你喝得有点太猛了吧？\x02\x03",
            "这样的话晚上的工作不就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#029F……你说什么……\x02",
    )

    CloseMessageWindow()
    OP_7C(0x0, 0xC8, 0x7D0, 0xC8)

    ChrTalk(
        0xF,
        (
            "#029F哼哼，赖皮演奏家！\x01",
            "难道你不愿意喝我敬你的酒吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#038F哇哇哇……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_46F5")
    SetChrSubChip(0x10, 1)
    Jump("loc_4726")

    label("loc_46F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_470B")
    SetChrSubChip(0x10, 0)
    Jump("loc_4726")

    label("loc_470B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4721")
    SetChrSubChip(0x10, 2)
    Jump("loc_4726")

    label("loc_4721")

    SetChrSubChip(0x10, 1)

    label("loc_4726")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#038F艾丝蒂尔君……\x01",
            "你们怎么不帮我说几句啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#007F不好意思啊～\x01",
            "变成这样的话我也阻止不住了。\x02\x03",
            "#006F别担心，\x01",
            "雪拉姐就算喝多少瓶都不会醉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#037F我是说……你们不担心我吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0)
    EventEnd(0x0)
    Jump("loc_49F8")

    label("loc_4841")

    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4863")
    SetChrSubChip(0xF, 2)
    Jump("loc_487E")

    label("loc_4863")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4879")
    SetChrSubChip(0xF, 2)
    Jump("loc_487E")

    label("loc_4879")

    SetChrSubChip(0xF, 1)

    label("loc_487E")

    OP_8C(0xF, 270, 0)
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4955")
    OP_A2(0x6)

    ChrTalk(
        0xF,
        (
            "#028F唔……好热啊～\x02\x03",
            "干脆通通脱光算了，\x01",
            "穿着衣服喝酒好麻烦啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F你、你喝醉啦。\x01",
            "这里有很多客人在吃饭啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49F3")

    label("loc_4955")

    OP_62(0xF, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#028F艾丝蒂尔～你这个小丫头\x01",
            "真的是越看越可爱呢～\x02\x03",
            "来，陪姐姐喝一杯好不好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F我不喝！ \x02",
    )

    CloseMessageWindow()

    label("loc_49F3")

    SetChrSubChip(0xF, 0)

    label("loc_49F8")

    Jump("loc_4F93")

    label("loc_49FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CFC")
    EventBegin(0x0)
    OP_A2(0x343)
    OP_6D(14850, 0, 6330, 1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雪拉扎德和奥利维尔\x01",
            "以沁凉的果实酒交杯换盏。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        (
            "#000F雪拉姐呀……\x01",
            "现在还是白天你就喝这么多了。\x02\x03",
            "就算是再清淡的酒也有个限度啊，\x01",
            "喝多了不怕搞坏身体吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B47")
    SetChrSubChip(0xF, 2)
    Jump("loc_4B78")

    label("loc_4B47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B5D")
    SetChrSubChip(0xF, 1)
    Jump("loc_4B78")

    label("loc_4B5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B73")
    SetChrSubChip(0xF, 0)
    Jump("loc_4B78")

    label("loc_4B73")

    SetChrSubChip(0xF, 2)

    label("loc_4B78")

    OP_8C(0xF, 270, 0)
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#021F没问题，没问题。\x01",
            "酒这种东西其实和水差不多嘛。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4BDC")
    SetChrSubChip(0x10, 1)
    Jump("loc_4C0D")

    label("loc_4BDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4BF2")
    SetChrSubChip(0x10, 0)
    Jump("loc_4C0D")

    label("loc_4BF2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C08")
    SetChrSubChip(0x10, 2)
    Jump("loc_4C0D")

    label("loc_4C08")

    SetChrSubChip(0x10, 1)

    label("loc_4C0D")

    OP_8C(0x10, 90, 0)
    SetChrFlags(0x10, 0x10)

    ChrTalk(
        0x10,
        (
            "#035F呵呵，艾丝蒂尔君。\x01",
            "有时候也要适当放松一下自己嘛。\x02\x03",
            "我知道怎么服侍雪拉君，\x01",
            "你们就放心把她交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#007F不，令人担心的倒不是雪拉姐……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#033F？？？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    EventEnd(0x0)
    Jump("loc_4F93")

    label("loc_4CFC")

    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D1E")
    SetChrSubChip(0xF, 2)
    Jump("loc_4D39")

    label("loc_4D1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D34")
    SetChrSubChip(0xF, 2)
    Jump("loc_4D39")

    label("loc_4D34")

    SetChrSubChip(0xF, 1)

    label("loc_4D39")

    OP_8C(0xF, 270, 0)
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EBD")
    OP_A2(0x6)

    ChrTalk(
        0xF,
        (
            "#020F说起来，艾丝蒂尔。\x01",
            "约修亚他干什么去了？\x02\x03",
            "难道是你被甩了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F嗯……就是这样。\x02",
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#023F真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F我本来约他去钓鱼，\x01",
            "但是他说要读书，就不管我了。\x02\x03",
            "真是的，难道不觉得态度过于冷淡了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#025F什么呀，差点让我误会了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F8E")

    label("loc_4EBD")


    ChrTalk(
        0xF,
        (
            "#020F我知道你从小就很喜欢钓鱼。\x01",
            "　\x02\x03",
            "不过这可是男孩子的兴趣哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F嘿嘿，没关系啦。\x01",
            "本来钓鱼就是非常有趣的事情嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F8E")

    SetChrSubChip(0xF, 0)

    label("loc_4F93")

    TalkEnd(0xF)
    Return()

    # Function_14_449A end

    def Function_15_4F97(): pass

    label("Function_15_4F97")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(17490, 0, 11000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0xA, 17247, 0, 11528, 180)
    SetChrPos(0x101, 18088, 0, 10277, 270)
    SetChrPos(0x102, 18100, 0, 9000, 270)
    SetChrPos(0x103, 15700, 0, 10682, 90)
    SetChrPos(0x104, 15500, 0, 9000, 90)

    ChrTalk(
        0xA,
        (
            "是这样啊……\x01",
            "你们是从库瓦诺那儿听说我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊啊，我的确是看到了。\x01",
            "就在前天夜晚，几个奇怪的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F果然是……\x02\x03",
            "可以把那天看到的事情\x01",
            "详细地告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……在此之前我想问一句。\x01",
            "你们是不是游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "我说的话是不是牵涉到什么案件？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F现在还不能断定。\x01",
            "不过，相关联的可能性还是有的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我知道了……\x01",
            "既然是这样，我一定会协助你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "前天晚上……\x01",
            "也就是我在小艇上夜钓的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "因为和努西苦战了一整天，\x01",
            "累得不行了所以想回旅馆休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "天色也已经晚了，\x01",
            "住宿的客人也都休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F请等一下。\x01",
            "……你说的『努西』是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "你可要认真听好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "所谓的努西，\x01",
            "是生活在这个瓦雷利亚湖的\x01",
            "一种十分巨大的鱼精。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "十年来，努西一直都是\x01",
            "我们这些钓鱼爱好者最热衷的话题，\x01",
            "但它同时也是一种让人难以捉摸的鱼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#023F（不妙……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（不小心让他兴致高昂起来了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F有、有这么厉害的鱼吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对啊，要知道这五年来，\x01",
            "我一直在追踪那家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过，那家伙的脾性反复无常，\x01",
            "一时游到这来一时游到那去，\x01",
            "一时吃这种鱼饵一时吃那种鱼饵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "最近，我听说那家伙在这附近出现，\x01",
            "就急忙从王都追了过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F呵呵，多么狂热的激情啊。\x01",
            "对于你的心情我非常地理解。\x02\x03",
            "若是看到了中意的东西，\x01",
            "我也一定会想尽办法得到它。\x02\x03",
            "譬如说『格兰·夏利拿』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F那样也叫得到吗？\x01",
            "应该是不问自取偷偷喝完才对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F咳咳……回到正题吧。\x02\x03",
            "那么罗伊德先生，\x01",
            "你夜钓回来之后又怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "啊，好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "之后，我就把小艇放好，\x01",
            "接着正要走回旅馆睡觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "就在那时，我看到了奇怪的二人组合。\x01",
            "他们从旅馆出来，走到外面的街道上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F走到街道上……\x01",
            "而且是在深夜的时候？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "啊啊，我不会看错的。\x01",
            "就是走到安塞尔新街那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我本来以为他们\x01",
            "是外出游玩晚归的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "不过深更半夜才回来也太奇怪了吧。\x01",
            "所以第二天，我向旅馆的人打听了一下，\x01",
            "不过大家都说不认识这些家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "当时我以为自己看到了幽灵，\x01",
            "不禁感觉背后发寒。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F幽、幽灵……\x02\x03",
            "会、会出现吗？在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哈哈，我看到的是两人一起，\x01",
            "而且还是一男一女的年轻组合呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "或许那两人是一对得不到\x01",
            "身边人的承认而徇情的恋人……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#003F啊～～～别、别再说了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F哎呀哎呀。\x01",
            "你还是怕听到幽灵这类的话题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F就是越害怕才越想听嘛，\x01",
            "怪谭之类的，还有不可思议的故事之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#031F呵呵，看艾丝蒂尔君\x01",
            "害怕得尖叫起来的样子，\x01",
            "真是越看越可爱，越看越动人。\x02\x03",
            "简直就像在寒风中战栗的小猫㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#009F哼！再说这种话就小心你的门牙！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "哈哈哈……\x01",
            "幽灵什么的只是开玩笑而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "当时我还不敢肯定，\x01",
            "不过那对男女应该不是情侣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "因为我看到那个女子穿着很怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F穿着很怪……这怎么说呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我只是看到背影，\x01",
            "也不敢肯定有没有看错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "不过看样子她穿的就是校服。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_62(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#004F校服？难道说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F杰尼丝王立学院的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "呵呵，你们知道得很清楚嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我的外甥女也在那学校念书，\x01",
            "所以我看得出那就是王立学院的校服。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F原来如此……\x01",
            "终于知道所谓的奇怪家伙是谁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F怪不得被人叫做奇怪的家伙！\x01",
            "肯定是那个嚣张的男人婆！\x02\x03",
            "总算抓到你的尾巴了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "怎么了……\x01",
            "难道你们认识他们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "我觉得那两个人选择在\x01",
            "深夜出现可能是出于什么目的吧，\x01",
            "这一点你们也最好注意一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对了，我还听他们说过\x01",
            "今天半夜会再来这里一次的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F啊？真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "对对，那个年轻男子亲口说过，\x01",
            "两天后还会再来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "他的口气十分认真，让我印象很深。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F原来如此……\x02\x03",
            "这是很重要的线索啊。\x01",
            "感谢你的合作，之后就交给我们吧。\x02\x03",
            "我们绝对会好好利用这些线索的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "呼，太好了……\x01",
            "你能这么说我很高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "突然感觉如释重负啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……这下可安心了。\x01",
            "我又可以安安稳稳地钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "这次不会让你逃掉的！\x01",
            "各位朋友，我这就先失陪了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xA, 0x5F17, 0x0, 0x37A7, 0x3A98, 0x0)
    SetChrFlags(0xA, 0x80)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F好一个钓鱼迷呢……\x01",
            "这样的集中力我们还真是比不上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那个所谓的『钓公师团』，\x01",
            "不知道是一个什么样的组织呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F听到现在，\x01",
            "我连那对男女是什么来头也还没搞清楚。\x02\x03",
            "究竟你们在调查什么事情，\x01",
            "可以向我详细地解释一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F也对。\x01",
            "事情大致是这样的……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "雪拉扎德向奥利维尔讲解了关于\x01",
            "在洛连特出现的空贼团少女乔丝特的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x104,
        (
            "#033F原来如此……还真是\x01",
            "踏破铁鞋无觅处，得来全不费功夫。 \x02\x03",
            "这么说，今天晚上有好戏看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是啊……\x02\x03",
            "为了慎重起见，\x01",
            "我们也要租一间房间落脚比较好。\x02\x03",
            "而且必须等到今天半夜才能行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯。\x01",
            "我们回柜台那里去吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    Fade(1000)
    SetChrPos(0x0, 17154, 0, 12588, 0)
    SetChrPos(0x1, 17154, 0, 12588, 0)
    SetChrPos(0x2, 17154, 0, 12588, 0)
    SetChrPos(0x3, 17154, 0, 12588, 0)
    EventEnd(0x0)
    Return()

    # Function_15_4F97 end

    def Function_16_67A8(): pass

    label("Function_16_67A8")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(23550, 0, 12290, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrSubChip(0xF, 2)
    SetChrSubChip(0x10, 1)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    OP_8C(0x9, 0, 0)
    OP_6D(17310, 0, 5790, 6000)
    OP_A2(0x3FB)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_67A8 end

    def Function_17_6832(): pass

    label("Function_17_6832")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(15740, 0, 7650, 0)
    SetChrPos(0x101, 15500, 0, 7820, 225)
    SetChrPos(0x102, 16400, 0, 7540, 225)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#038F你们……快来救救我啊……\x02\x03",
            "再、再喝下去会出……人命的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F呜哇～好厉害哦。\x01",
            "看来要对你另眼相看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F确实是啊，陪雪拉姐姐喝酒，\x01",
            "能像你这样还有意识的可没几个哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 2)
    Sleep(300)
    OP_62(0xF, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#028F呵呵……\x01",
            "你们来得真巧啊⊙\x02\x03",
            "来来来～陪姐姐一起喝酒㈱\x02\x03",
            "好不好，好不好，来～嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        (
            "#009F我、我们现在要去吃晚饭，\x01",
            "所以就不陪你们耍酒疯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#029F不行不行～\x01",
            "通通留下来陪我喝酒～\x02\x03",
            "你们不陪，我可要大发雷霆哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F雪拉姐已经进入疯狂状态了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F雪拉姐姐、奥利维尔，\x01",
            "看来你们相处得还不错嘛。\x02\x03",
            "说实话，其实你们俩挺相配的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0)
    Sleep(300)
    OP_8C(0x101, 225, 0)

    ChrTalk(
        0xF,
        (
            "#028F#2P…………………………（盯着看）\x02\x03",
            "#021F什么呀～这家伙还差的远啦㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#036F哎哟……\x02\x03",
            "约、约修亚君，\x01",
            "你就别这样和人家开玩笑嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F好、好可怜的样子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F有这回事吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#035F不过你们两个小坏蛋也……\x01",
            "挺有情趣的……我最喜欢了……\x02\x03",
            "…………呼呼………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F看来白担心了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F呵呵，说得也是。\x01",
            "那我们到去柜台那边吧。\x02\x03",
            "不要破坏他们的二人世界了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x12)
    OP_43(0x102, 0x1, 0x0, 0x13)
    Sleep(1000)
    OP_6D(14770, 0, 6250, 2000)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#036F雪拉君……求求你了……\x01",
            "不要再灌我了好不好……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x12, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x10,
        "#038F………啊啊啊啊啊啊………\x02",
    )

    CloseMessageWindow()
    OP_3F(0x332, 1)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1501   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_6832 end

    def Function_18_6F68(): pass

    label("Function_18_6F68")

    Sleep(700)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x4808, 0x0, 0x1D4C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4CAE, 0x0, 0x2206, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6176, 0x0, 0x224C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_18_6F68 end

    def Function_19_6FC2(): pass

    label("Function_19_6FC2")

    OP_8C(0xFE, 90, 400)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x4808, 0x0, 0x1D4C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4CAE, 0x0, 0x2206, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6176, 0x0, 0x224C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_19_6FC2 end

    def Function_20_7017(): pass

    label("Function_20_7017")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "钓鱼工具并排摆在架子上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_20_7017 end

    SaveToFile()

Try(main)
