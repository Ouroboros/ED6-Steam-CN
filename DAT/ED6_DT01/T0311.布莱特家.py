from ED6ScenarioHelper import *

def main():
    # 布莱特家

    CreateScenaFile(
        FileName            = 'T0311   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0311.x',
        MapIndex            = 15,
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
        '卡西乌斯',                             # 9
        '约修亚',                               # 10
        '艾丝蒂尔',                             # 11
        '艾丝蒂尔',                             # 12
        '男孩',                                 # 13
        '卡西乌斯',                             # 14
        '器皿',                                 # 15
        '器皿',                                 # 16
        '器皿',                                 # 17
        '咖啡',                                 # 18
        '咖啡',                                 # 19
        '咖啡',                                 # 20
        '法式面包',                             # 21
        '炸面包',                               # 22
        '床',                                   # 23
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 66900,
        Unknown_04              = 800,
        Unknown_08              = 35500,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = -32600,
        Unknown_20              = 0,
        Unknown_24              = -41000,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 66900,
        Unknown_04              = 800,
        Unknown_08              = 35500,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 6000,
        Unknown_18              = -10000,
        Unknown_1C              = -1040,
        Unknown_20              = 0,
        Unknown_24              = -3230,
        Unknown_28              = 3000,
        Unknown_2C              = 280,
        Unknown_30              = 45,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 66900,
        Unknown_04              = 800,
        Unknown_08              = 35500,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 6000,
        Unknown_18              = -10000,
        Unknown_1C              = -1040,
        Unknown_20              = 0,
        Unknown_24              = -3230,
        Unknown_28              = 3000,
        Unknown_2C              = 280,
        Unknown_30              = 45,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 15,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02000 ._CH',             # 00
        'ED6_DT07/CH00010 ._CH',             # 01
        'ED6_DT06/CH20008 ._CH',             # 02
        'ED6_DT06/CH20005 ._CH',             # 03
        'ED6_DT06/CH20006 ._CH',             # 04
        'ED6_DT07/CH02210 ._CH',             # 05
        'ED6_DT07/CH02220 ._CH',             # 06
        'ED6_DT06/CH20011 ._CH',             # 07
        'ED6_DT07/CH00003 ._CH',             # 08
        'ED6_DT07/CH00013 ._CH',             # 09
        'ED6_DT07/CH02003 ._CH',             # 0A
        'ED6_DT07/CH00023 ._CH',             # 0B
        'ED6_DT06/CH20020 ._CH',             # 0C
        'ED6_DT06/CH20021 ._CH',             # 0D
        'ED6_DT06/CH20056 ._CH',             # 0E
        'ED6_DT06/CH20033 ._CH',             # 0F
        'ED6_DT06/CH20133 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02000P._CP',             # 00
        'ED6_DT07/CH00010P._CP',             # 01
        'ED6_DT06/CH20008P._CP',             # 02
        'ED6_DT06/CH20005P._CP',             # 03
        'ED6_DT06/CH20006P._CP',             # 04
        'ED6_DT07/CH02210P._CP',             # 05
        'ED6_DT07/CH02220P._CP',             # 06
        'ED6_DT06/CH20011P._CP',             # 07
        'ED6_DT07/CH00003P._CP',             # 08
        'ED6_DT07/CH00013P._CP',             # 09
        'ED6_DT07/CH02003P._CP',             # 0A
        'ED6_DT07/CH00023P._CP',             # 0B
        'ED6_DT06/CH20020P._CP',             # 0C
        'ED6_DT06/CH20021P._CP',             # 0D
        'ED6_DT06/CH20056P._CP',             # 0E
        'ED6_DT06/CH20033P._CP',             # 0F
        'ED6_DT06/CH20133P._CP',             # 10
    )

    DeclNpc(
        X                   = -1600,
        Z                   = 0,
        Y                   = 3011,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 11500,
        Z                   = 0,
        Y                   = -3400,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 148000,
        Z                   = 520,
        Y                   = 145400,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8230,
        Z                   = 200,
        Y                   = -520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9550,
        Z                   = 200,
        Y                   = -520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8100,
        Z                   = 200,
        Y                   = 2200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 65548,
        ChipIndex           = 0xC,
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
        Unknown3            = 65548,
        ChipIndex           = 0xC,
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
        Unknown3            = 65548,
        ChipIndex           = 0xC,
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
        Unknown3            = 1572876,
        ChipIndex           = 0xC,
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
        Unknown3            = 1572876,
        ChipIndex           = 0xC,
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
        Unknown3            = 1572876,
        ChipIndex           = 0xC,
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
        Unknown3            = 720908,
        ChipIndex           = 0xC,
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
        Unknown3            = 2031628,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8470,
        Z                   = 0,
        Y                   = 67140,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2031628,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 146290,
        TriggerZ            = 0,
        TriggerY            = 144760,
        TriggerRange        = 800,
        ActorX              = 147910,
        ActorZ              = 1500,
        ActorY              = 144780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72010,
        TriggerZ            = 0,
        TriggerY            = 71390,
        TriggerRange        = 800,
        ActorX              = 72570,
        ActorZ              = 1500,
        ActorY              = 72600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_426",          # 00, 0
        "Function_1_81D",          # 01, 1
        "Function_2_81E",          # 02, 2
        "Function_3_834",          # 03, 3
        "Function_4_A73",          # 04, 4
        "Function_5_D07",          # 05, 5
        "Function_6_1D62",         # 06, 6
        "Function_7_1DEB",         # 07, 7
        "Function_8_1E55",         # 08, 8
        "Function_9_296A",         # 09, 9
        "Function_10_2A05",        # 0A, 10
        "Function_11_2A83",        # 0B, 11
        "Function_12_2ABA",        # 0C, 12
        "Function_13_41F0",        # 0D, 13
        "Function_14_429A",        # 0E, 14
        "Function_15_5BB0",        # 0F, 15
        "Function_16_71F3",        # 10, 16
        "Function_17_7490",        # 11, 17
    )


    def Function_0_426(): pass

    label("Function_0_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_435")
    SetChrFlags(0x8, 0x80)
    Jump("loc_52D")

    label("loc_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_455")
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 3554, 0, 71683, 161)
    Jump("loc_52D")

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 2)), scpexpr(EXPR_END)), "loc_519")
    SetChrPos(0x8, -8100, 200, 2200, 180)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -7860, 700, 200, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, -9620, 700, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -9120, 700, 200, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, -8860, 700, 1200, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_52D")

    label("loc_519")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_544")
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_55B")
    OP_A3(0x3FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_55B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_577"),
        (2, "loc_61A"),
        (3, "loc_730"),
        (102, "loc_746"),
        (103, "loc_7B1"),
        (SWITCH_DEFAULT, "loc_81C"),
    )


    label("loc_577")

    ClearMapFlags(0x1)
    OP_6D(-6600, 0, 1400, 0)
    SetChrSubChip(0xE, 10)
    SetChrSubChip(0xF, 10)
    SetChrSubChip(0x10, 1)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xF, -9620, 700, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x15, -640, 800, 2960, 0)
    ClearChrFlags(0x15, 0x80)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_81C")

    label("loc_61A")

    ClearMapFlags(0x1)
    OP_6D(-3500, 0, 1700, 0)
    SetChrPos(0xA, -8230, 200, -520, 0)
    SetChrPos(0x9, -9550, 200, -520, 0)
    SetChrPos(0x8, -8100, 200, 2200, 180)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0x8, 10)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -7860, 700, 200, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, -9620, 700, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -9120, 700, 200, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, -8860, 700, 1200, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    ClearChrFlags(0x14, 0x80)
    FadeToBright(1000, 0)
    Event(0, 5)
    Jump("loc_81C")

    label("loc_730")

    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SoundLoad(125)
    Event(0, 14)
    Jump("loc_81C")

    label("loc_746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_750")
    Jump("loc_7AE")

    label("loc_750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_7AE")
    ClearMapFlags(0x1)
    OP_6D(6187, 0, 71060, 0)
    SetChrPos(0x101, 3012, 0, 67051, 0)
    SetChrPos(0x102, 3891, 0, 66840, 0)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 3060, 200, 71360, 180)
    SetChrChipByIndex(0x8, 10)
    Event(0, 8)

    label("loc_7AE")

    Jump("loc_81C")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_7BB")
    Jump("loc_819")

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_819")
    ClearMapFlags(0x1)
    OP_6D(6187, 0, 71060, 0)
    SetChrPos(0x101, 8324, 0, 71386, 270)
    SetChrPos(0x102, 8138, 0, 70528, 270)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 3060, 200, 71360, 180)
    SetChrChipByIndex(0x8, 10)
    Event(0, 8)

    label("loc_819")

    Jump("loc_81C")

    label("loc_81C")

    Return()

    # Function_0_426 end

    def Function_1_81D(): pass

    label("Function_1_81D")

    Return()

    # Function_1_81D end

    def Function_2_81E(): pass

    label("Function_2_81E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_833")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_81E")

    label("loc_833")

    Return()

    # Function_2_81E end

    def Function_3_834(): pass

    label("Function_3_834")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A07")
    OP_A2(0x3)

    ChrTalk(
        0x101,
        (
            "#000F对了，老爸。\x01",
            "你今天不去游击士协会吗？\x02\x03",
            "#000F这几天你还是抽空去一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F我还有一些堆积的文件要处理。\x02\x03",
            "#080F呵呵，不用为我担心，\x01",
            "等到要被解雇的时候我自然会回去工作的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F（老爸真是一点也不可靠啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6F")

    label("loc_A07")


    ChrTalk(
        0x8,
        (
            "#080F你们还不去协会那里？\x01",
            "雪拉扎德不是在等着你们过去吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6F")

    TalkEnd(0xFE)
    Return()

    # Function_3_834 end

    def Function_4_A73(): pass

    label("Function_4_A73")

    OP_72(0x0, 0x20)
    OP_6F(0x0, 5)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x8)
    OP_6D(-1590, 0, 1830, 4000)
    Sleep(1000)
    OP_0D()
    Fade(1000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x10)
    OP_6D(148000, 540, 145400, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(2000)
    OP_8C(0xA, 45, 0)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    OP_99(0xA, 0xF, 0x10, 0x3E8)
    Sleep(1000)
    OP_61(0x101)

    ChrTalk(
        0xA,
        "#377F……呜～……好刺眼呢……\x02",
    )

    CloseMessageWindow()

    def lambda_B4D():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B4D)
    Sleep(200)
    OP_6F(0x0, 5)
    OP_70(0x0, 0x14)
    Sleep(1500)

    def lambda_B75():
        OP_99(0xFE, 0x8, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B75)

    ChrTalk(
        0xA,
        "#375F呼哇啊啊啊啊啊啊～……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0xA,
        "#440F嗯～～睡得真舒服～～！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_99(0xA, 0x11, 0x12, 0x3E8)
    Sleep(400)

    ChrTalk(
        0xA,
        (
            "#370F……对了………\x01",
            "今天早上轮到老爸做饭。\x02\x03",
            "那么……\x01",
            "也就是说约修亚还在睡觉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x46)
    OP_1F(0x4B, 0xC8)
    Sleep(2000)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_99(0xA, 0x13, 0x15, 0x3E8)

    ChrTalk(
        0xA,
        "#371F啊哈，好像已经起来了呢。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_99(0xA, 0x16, 0x17, 0x3E8)

    ChrTalk(
        0xA,
        (
            "#376F好的……\x01",
            "我也赶快起床吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    EventBegin(0x0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T0300   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_4_A73 end

    def Function_5_D07(): pass

    label("Function_5_D07")

    EventBegin(0x0)
    OP_6D(-3500, 0, 1700, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    AddParty(0x1, 0xFF)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x102, -4460, 0, 230, 0)
    ClearMapFlags(0x1)
    OP_43(0x101, 0x0, 0x0, 0x6)
    OP_43(0x9, 0x0, 0x0, 0x7)
    OP_A2(0x0)
    OP_67(0, 7000, -11000, 3000)
    OP_A5(0x0)

    ChrTalk(
        0xA,
        (
            "#001F我吃饱啦～！\x02\x03",
            "#001F嗯……\x01",
            "肚子已经鼓鼓的了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(
        0x9,
        "#010F#3P一大早你就吃这么多……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#502F不行吗？\x01",
            "能吃能睡的孩子才健康嘛⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F说的也是，\x01",
            "吃饱了才有精神去做事哦。\x02\x03",
            "#080F对了，\x01",
            "你们今天不是要去协会做最后的研修吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#010F#3P嗯。\x01",
            "就是复习至今为止学到的知识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#006F最重要的是，过了研修之后呢，\x01",
            "我们就和老爸一样是『游击士』啦。\x02\x03",
            "以后再也不会被当成小孩子啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F哼哼，你们还太嫩了。\x02\x03",
            "开始的时候也不过是『准游击士』，\x01",
            "也就是见习而已。\x02\x03",
            "要想独当一面的话，\x01",
            "就得早日成为『正游击士』才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#009F呵呵，这正合我意呢。\x02\x03",
            "等着瞧吧～\x01",
            "我一定会做出很多成绩来的，\x01",
            "然后超越老爸！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#081F哈哈哈。\x01",
            "做得到的话就试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#017F#3P这有什么好争的啊……\x02\x03",
            "#010F艾丝蒂尔，绝对不能小看今天的复习。\x02\x03",
            "#010F复习研修之后，\x01",
            "还有一场考试等着我们呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#501F啊？\x02\x03",
            "……………………\x02\x03",
            "考试……有这回事？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#018F#3P难，难道说……\x01",
            "你已经把这件事忘掉了？\x02\x03",
            "那可是考察我们有没有\x01",
            "在研修里学到东西的测验啊。\x02\x03",
            "要是不合格的话就要重新补习，\x01",
            "雪拉姐姐之前不是说过吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#002F糟了～……\x01",
            "忘得一干二净了……\x02\x03",
            "听你这么一说，\x01",
            "我也觉得雪拉姐好像是说过这件事……\x02\x03",
            "#001F不怕不怕，车到山前必有路☆\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#017F#3P唉，你啊……\x01",
            "该说你是天性乐观呢，还是思想单纯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#083F真拿你没办法。\x02\x03",
            "这种乐天的性格，\x01",
            "到底像谁呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#009F真、真讨厌～\x01",
            "比起老爸你来我还算好的呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#017F#3P简直就是一个模子里刻出来的父女。\x02\x03",
            "#010F好了好了。\x01",
            "艾丝蒂尔，差不多该去城里了。\x02\x03",
            "#010F雪拉姐姐还在协会等着呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#006F嗯，知道了。\x01",
            "让雪拉姐等太久可就惨了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)
    Fade(1000)
    OP_A2(0x0)
    OP_A2(0x1)
    Sleep(200)
    OP_6D(-5050, 0, -70, 4000)
    OP_A5(0x0)

    ChrTalk(
        0x101,
        (
            "#501F啊～对了老爸。\x02\x03",
            "今天晚上轮到我做饭哦，\x01",
            "想吃点什么呢？\x02\x03",
            "别客气，想吃什么尽管说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#085F嗯，想吃的东西嘛……\x02\x03",
            "#085F………………………………\x02\x03",
            "#080F我想吃点卢安风味的……\x01",
            "就来个香醋烤鱼怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F那、那是什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#019F对艾丝蒂尔来说，\x01",
            "要做那个也许太难了点吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#081F算了，只是随便说说而已。\x02\x03",
            "和平常一样，\x01",
            "做点炸鱼和煎蛋什么的就行了。\x02\x03",
            "不用太过勉强，\x01",
            "做出来能吃进肚子就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F谁说我不会做的啊……\x01",
            "你、你就不能少说点吗，讨厌……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F对了，还要拜托你一件事情。\x02\x03",
            "到了城里，帮我到杂货铺\x01",
            "买本叫《利贝尔通讯》的杂志。\x02\x03",
            "最新一期今天应该到货了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F知道了。\x01",
            "《利贝尔通讯》对吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B32():
        OP_6D(-5870, 0, 1160, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B32)
    OP_8E(0x101, 0xFFFFE5E8, 0x0, 0x86E, 0x7D0, 0x0)
    TurnDirection(0x101, 0x8, 500)
    SetChrSubChip(0x8, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x04",
            "５００\x07\x00",
            "米拉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    AddMira(500)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x8,
        (
            "#080F剩下的就给你们当零花钱吧。\x02\x03",
            "#080F不过可别乱花哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#001F太好了，谢谢老爸！\x02",
    )

    CloseMessageWindow()

    def lambda_1C75():
        OP_6D(-4460, 0, 230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C75)
    OP_8E(0x101, 0xFFFFEE94, 0x0, 0xE6, 0x7D0, 0x0)
    SetChrSubChip(0x8, 0)
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(
        0x9,
        "#010F那么爸爸，我们走了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F哦，好好干。\x01",
            "代我向雪拉扎德问好。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x10)
    OP_A2(0x202)

    def lambda_1D3C():
        OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D3C)
    EventEnd(0x0)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearMapFlags(0x2000000)
    Return()

    # Function_5_D07 end

    def Function_6_1D62(): pass

    label("Function_6_1D62")

    OP_A6(0x0)
    OP_6D(-8500, 0, 1700, 3000)
    OP_A3(0x0)
    OP_A6(0x0)
    ClearChrFlags(0xFE, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xFE, -8810, 0, -1170, 180)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFDE9A, 0x0, 0xFFFFF768, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEE94, 0x0, 0xE6, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    TurnDirection(0xFE, 0x8, 500)
    OP_A3(0x0)
    Return()

    # Function_6_1D62 end

    def Function_7_1DEB(): pass

    label("Function_7_1DEB")

    OP_A6(0x1)
    SetChrChipByIndex(0xFE, 1)
    SetChrPos(0xFE, -10410, 0, -800, 180)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFD77E, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE3C2, 0x0, 0xFFFFF880, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF222, 0x0, 0xFFFFFC0E, 0x7D0, 0x0)
    Sleep(300)
    TurnDirection(0xFE, 0x8, 500)
    OP_A3(0x1)
    Return()

    # Function_7_1DEB end

    def Function_8_1E55(): pass

    label("Function_8_1E55")

    EventBegin(0x0)
    OP_43(0x101, 0x0, 0x0, 0x9)
    OP_43(0x102, 0x0, 0x0, 0xA)
    OP_43(0x8, 0x0, 0x0, 0xB)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F我们回来了～老爸。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1)
    OP_A5(0x1)
    OP_A5(0x0)

    ChrTalk(
        0x101,
        "#000F工作报告也已经完成了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#080F#2P嗯，辛苦了。\x02\x03",
            "#080F报告内容会在各支部进行评测，\x01",
            "报酬和升级之类的也会受其影响。\x02\x03",
            "#080F这点你们要记住才行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F知道了。\x02\x03",
            "#501F对了老爸。\x01",
            "《利贝尔通讯》买回来了。\x02\x03",
            "#501F而且还有协会要我转交的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A5(0x0)
    OP_8C(0x101, 270, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "交出了\x07\x02",
            "利贝尔通讯\x07\x05",
            "和\x07\x02",
            "致卡西乌斯的信\x07\x05",
            "。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x347, 1)
    OP_3F(0x336, 1)

    ChrTalk(
        0x8,
        "#084F#2P唔，是信啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F好了，\x01",
            "我还要去准备晚饭。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A5(0x0)

    ChrTalk(
        0x101,
        "#501F啊，对了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        (
            "#008F……今天谢谢老爸你了。\x01",
            "在危急的时候救了我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#2P呵呵，今天真是一反常态，这么乖啊。\x02\x03",
            "#080F你终于理解为父的伟大了，\x01",
            "真是件令人高兴的事情。 \x02\x03",
            "#081F来吧女儿，不必客气。\x01",
            "飞扑到爸爸怀里来尽情撒娇吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#009F不要得意忘形！\x02\x03",
            "#009F真是的，\x01",
            "为什么这家里的男人都只会耍嘴皮子啊……\x02",
        )
    )

    CloseMessageWindow()
    SetMapFlags(0x400000)
    OP_A2(0x0)
    OP_A2(0x1)
    Sleep(300)
    SetChrSubChip(0x8, 0)
    OP_A5(0x0)
    OP_A5(0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#080F#2P看起来并没有我想象得那么沮丧嘛……\x01",
            "　\x02\x03",
            "#080F约修亚，是因为你吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#010F其实我也没做什么。\x01",
            "只是稍微鼓励了她一下吧。\x02\x03",
            "#010F她本来就很坚强的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#085F#2P哼，还太嫩了。\x02\x03",
            "#085F做游击士这种工作，\x01",
            "感到迷茫肯定是经常会有的。\x02\x03",
            "#085F要独当一面就得跨过这些门槛才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F呵呵，您就是那么为女儿着想。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "惨了～……\x01",
            "还得再重来一遍啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x101,
        (
            "突然挑战这个菜式，\x01",
            "对我来说真的那么难吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "不对，做料理要靠气势！\x01",
            "无论失败多少次都要继续挑战！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#083F#2P真是的……\x01",
            "我这个沉不住气的女儿。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        (
            "#010F我去帮她一下吧。\x02\x03",
            "#010F这样下去，\x01",
            "都不知道什么时候才能吃饭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A5(0x1)

    ChrTalk(
        0x8,
        (
            "#080F#2P呵呵……\x02\x03",
            "#085F……好吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "卡西乌斯把信封打开。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_20(0xBB8)

    ChrTalk(
        0x8,
        (
            "#080F#2P嗯……\x01",
            "是帝国那边寄来的联络信啊……\x02\x03",
            "#080F………………………………\x02\x03",
            "#082F………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(2000)
    OP_21()

    ChrTalk(
        0x8,
        "#086F#2P……什么……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    Call(0, 12)
    Return()

    # Function_8_1E55 end

    def Function_9_296A(): pass

    label("Function_9_296A")

    OP_A6(0x0)
    OP_8E(0xFE, 0x1592, 0x0, 0x11334, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_8E(0xFE, 0x1082, 0x0, 0x115DC, 0x7D0, 0x0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_8E(0xFE, 0x1592, 0x0, 0x11334, 0x7D0, 0x0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_8E(0xFE, 0xD7B, 0x0, 0x10693, 0xFA0, 0x0)
    OP_8E(0xFE, 0xBE3, 0x0, 0xFC48, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_A3(0x0)
    Return()

    # Function_9_296A end

    def Function_10_2A05(): pass

    label("Function_10_2A05")

    OP_A6(0x1)
    Sleep(500)
    OP_8E(0xFE, 0x1647, 0x0, 0x10E4D, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    OP_A3(0x1)
    OP_A6(0x1)

    label("loc_2A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A40")
    TurnDirection(0xFE, 0x101, 0)
    OP_48()
    Jump("loc_2A2E")

    label("loc_2A40")

    OP_A6(0x1)
    OP_8E(0xFE, 0xD7B, 0x0, 0x10693, 0xBB8, 0x0)
    OP_8E(0xFE, 0xBE3, 0x0, 0xFC48, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x2)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_A3(0x1)
    Return()

    # Function_10_2A05 end

    def Function_11_2A83(): pass

    label("Function_11_2A83")

    OP_A6(0x2)

    label("loc_2A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2A98")
    TurnDirection(0xFE, 0x101, 0)
    OP_48()
    Jump("loc_2A86")

    label("loc_2A98")

    OP_A6(0x2)

    label("loc_2A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2AAD")
    TurnDirection(0xFE, 0x102, 0)
    OP_48()
    Jump("loc_2A9B")

    label("loc_2AAD")

    OP_A6(0x2)
    OP_A3(0x2)
    OP_A6(0x2)
    OP_A3(0x2)
    Return()

    # Function_11_2A83 end

    def Function_12_2ABA(): pass

    label("Function_12_2ABA")

    EventBegin(0x0)
    OP_6D(-2500, 0, 1700, 0)
    SetChrPos(0x101, -7950, 0, -500, 0)
    SetChrPos(0x102, -9310, 0, -300, 0)
    SetChrPos(0xA, -8230, 200, -520, 0)
    SetChrPos(0x9, -9550, 200, -520, 0)
    SetChrPos(0x8, -8100, 200, 2200, 180)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    SetChrChipByIndex(0xA, 8)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xF, 0)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x14, 7)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -7860, 700, 200, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, -9620, 700, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x12, -9120, 700, 200, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, -8860, 700, 1200, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    ClearChrFlags(0x14, 0x80)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_6D(-7500, 0, 1700, 3500)
    OP_0D()

    ChrTalk(
        0x8,
        "#084F#5P哦，真是不可思议啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#508F怎么样，这可是艾丝蒂尔特制的\x01",
            "香滑美味的鸡肉蛋包饭！\x02\x03",
            "请用心品味哦⊙\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#010F#6P嗯。\x01",
            "味道真的很好啊，这个。\x02\x03",
            "#019F做得不错嘛，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#502F哼哼，这就是我的真正实力哦㈱\x02\x03",
            "#006F啊～虽然发生了很多事，\x01",
            "不过今天还真是很棒的一天啊。\x02\x03",
            "得到了游击士的资格，\x01",
            "完成了自己的第一份任务……\x02\x03",
            "#001F蛋包饭也成功了⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#5P嗯……\x01",
            "第一次做的竟然还能入口。\x02\x03",
            "#081F本来已经做好心理准备了，有点意外啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#509F好讨厌啊～\x01",
            "直接说好吃不就行了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#5P嗯，\x01",
            "真没想到能在出发前吃到这么好的东西。\x02\x03",
            "#080F做得很不错，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F嘿嘿……\x02\x03",
            "#506F……………\x02\x03",
            "#501F……出发前？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#014F#6P爸爸，难道您……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#5P嗯。\x02\x03",
            "突然接到了紧急任务。\x01",
            "我又要暂时离家外出了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        (
            "#580F等、等一下！\x02\x03",
            "那……什么时候出发？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#080F#5P明天就走。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F什么～！？\x01",
            "再怎么说这也太急了吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#6P是因为今天那封信吧……\x01",
            "难道出了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#085F没什么……单纯的调查而已。\x02\x03",
            "要到很多地方去看看，\x01",
            "大概要花一个月左右的时间吧。\x02\x03",
            "#080F就是这样，又要拜托你们看家了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F#3S什么『就是这样』啊！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F老爸真是的，\x01",
            "每次都自作主张……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P没办法啊，艾丝蒂尔。\x02\x03",
            "接到任务就要立刻行动，\x01",
            "这就是游击士的本职工作啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F这我知道啊……\x01",
            "可是洛连特支部的工作该怎么办呢？\x02\x03",
            "很多工作……应该也还没做完吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#5P嗯，大概有五、六个吧。\x02\x03",
            "#080F我也考虑过这个……\x02\x03",
            "#080F不然你们代替我，\x01",
            "去试着完成这其中几个任务吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊……\x02\x03",
            "#004F就是说让我们来做\x01",
            "本该由老爸去做的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#5P嗯，\x01",
            "给你们几个新手也可以应付得来的任务。\x02\x03",
            "#080F其余那些难度高点的工作\x01",
            "我就交给雪拉扎德帮忙。\x02\x03",
            "#080F怎么样？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "『我一定会做好的！』\x01",      # 0
            "『虽然想试试看……』\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3738"),
        (1, "loc_3C0B"),
        (SWITCH_DEFAULT, "loc_40E3"),
    )


    label("loc_3738")


    ChrTalk(
        0x101,
        (
            "#001F我一定会做好的！\x01",
            "而且一定会比之前做得更好！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#501F对不对？约修亚。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#019F#6P嗯。\x01",
            "而且我觉得这是难得的锻炼机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#5P就这么定了。\x02\x03",
            "#080F明天出发前，\x01",
            "我会亲自向协会说明一下。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#006F嗯。\x01",
            "我觉得现在充满了干劲呢！\x02\x03",
            "#006F我们可不能让老爸丢脸，\x01",
            "一定全力以赴把几个任务做好！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#084F#5P啊啊，艾丝蒂尔……\x01",
            "你这一番话太让我感动了。\x02\x03",
            "#085F在天国的孩子她妈，你看到了吗？\x02\x03",
            "我们的女儿终于长大了，\x01",
            "是一个又懂事又听话的好孩子呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F我说老爸你年纪也不小了，\x01",
            "怎么老是把我当成小孩子看待啊。\x02\x03",
            "#507F帮助父亲去完成工作是女儿应该做的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#086F#5P我今年才不过是４５而已！\x01",
            "而且还是协会里现役的游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F#6P啊……这对父女又在对唱了。\x02\x03",
            "#010F对了老爸。\x01",
            "你明天要坐哪艘定期船啊？\x02\x03",
            "#010F去王都的？\x01",
            "还是去柏斯的？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E3")

    label("loc_3C0B")


    ChrTalk(
        0x101,
        (
            "#007F虽然想试试看……\x01",
            "不过一想到万一失败的话……\x02\x03",
            "#505F真的是我们这种新人\x01",
            "也可以应付得来的工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#5P相对来说都是比较简单的，\x01",
            "不过其中也会有性命攸关的工作。\x02\x03",
            "#080F我不强求你们。\x01",
            "可以再好好考虑一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F……………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#002F约修亚你觉得怎样？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#010F#6P我赞成。\x01",
            "而且这是一次难得的锻炼机会。\x02\x03",
            "确实我们的能力都有所不足，\x01",
            "不过我想一起行动的话应该没问题的。\x02\x03",
            "两人齐心协力的话，\x01",
            "应该可以取长补短。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F齐心协力取长补短……\x02\x03",
            "#006F嗯，说得对啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#508F老爸！\x01",
            "我也要试试看！\x02\x03",
            "#001F老实说是跃跃欲试啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#5P就这么定了。\x02\x03",
            "明天出发前\x01",
            "我会亲自向协会说明一下。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#010F#6P对了爸爸。\x01",
            "你明天要坐哪艘定期船啊？\x02\x03",
            "#010F去王都的？\x01",
            "还是去柏斯的？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E3")

    label("loc_40E3")


    ChrTalk(
        0x8,
        (
            "#080F#5P去王都的。\x01",
            "明早１０点出发。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F这样啊……\x01",
            "那明天要早点起来才行呢。\x02\x03",
            "#001F我还是先调好闹钟吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    Call(0, 13)
    Return()

    # Function_12_2ABA end

    def Function_13_41F0(): pass

    label("Function_13_41F0")

    OP_1D(0x54)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x80)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x101, 67000, 300, 35500, 225)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 5)
    SetChrPos(0xA, 148000, 520, 145400, 315)
    SetChrChipByIndex(0xA, 2)
    SetChrSubChip(0xA, 0)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    OP_69(0xA, 0x0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0xA, 0xFFFFFE0C, 1200, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(3000)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T0301   ._SN", 2, 0, 0)
    IdleLoop()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    Return()

    # Function_13_41F0 end

    def Function_14_429A(): pass

    label("Function_14_429A")

    OP_77(0x5A, 0x5A, 0x7D, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    AddParty(0x0, 0xFF)
    AddParty(0x1, 0xFF)
    AddParty(0x2, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrPos(0xB, -7995, 0, 2276, 180)
    OP_69(0xB, 0x0)
    OP_6B(3300, 0)
    FadeToBright(2000, 0)
    Sleep(2000)

    def lambda_4310():
        OP_6B(2500, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4310)
    Sleep(2000)
    Fade(5000)
    ClearChrFlags(0xB, 0x80)
    SetChrSubChip(0xE, 3)
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0xF, 7)
    SetChrSubChip(0x14, 11)
    SetChrPos(0xE, -8360, 700, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, -9200, 750, 1000, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x14, -9000, 750, 400, 0)
    ClearChrFlags(0x14, 0x80)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    OP_66(0x0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#295F嗯……\x02\x03",
            "爸爸怎么还没回来……\x02\x03",
            "协会捎来的口信\x01",
            "明明说他今天会回家的……\x02",
        )
    )

    CloseMessageWindow()
    Fade(400)
    Sleep(1000)

    def lambda_442A():
        OP_6D(-7866, 1000, 5490, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_442A)
    OP_8C(0xB, 90, 0)
    OP_95(0xB, 0x3E8, 0x0, 0x0, 0x258, 0x1770)
    Sleep(500)
    OP_8E(0xB, 0xFFFFE629, 0x0, 0xB5E, 0xBB8, 0x0)
    OP_8E(0xB, 0xFFFFE146, 0x0, 0x1572, 0xBB8, 0x0)
    Sleep(1500)

    ChrTalk(
        0xB,
        (
            "#295F#5P雪拉姐也还在\x01",
            "周游王国的修行旅途中……\x02\x03",
            "唉～真无聊。\x01",
            "吃饭前还是再练习一下棒术吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1550, 0, -3450, 0)
    SetChrChipByIndex(0x8, 14)
    Sleep(500)

    NpcTalk(
        0x8,
        "男性的声音",
        "哟，我回来了。\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xB, 180, 800)

    ChrTalk(
        0xB,
        "#291F#5P爸爸！\x02",
    )

    CloseMessageWindow()

    def lambda_45BB():
        OP_6D(-1110, 0, -1690, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_45BB)
    OP_8E(0xB, 0xFFFFF772, 0x0, 0xFFFFFA92, 0x1388, 0x0)
    OP_8C(0xB, 180, 400)

    ChrTalk(
        0x8,
        (
            "#080F#4P我回来了，艾丝蒂尔。\x01",
            "让你等急了吧。\x02\x03",
            "有没有乖乖地看家啊，我的乖女儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#290F#1P哼哼，当然有啦☆\x02\x03",
            "#290F爸爸你也没什么事吧。\x02\x03",
            "和魔兽战斗没受伤吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#4P当然啦，你瞧，我不是精神得很吗？\x02\x03",
            "对了，艾丝蒂尔。\x01",
            "我这次给你带回一样礼物哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#291F#1P啊，真的！？\x02\x03",
            "钓鱼竿？还是运动鞋？\x01",
            "要不然就是棒术用具！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#083F#4P…………………………\x01",
            "唉，我是不是真的教女无方呢。\x02\x03",
            "你啊，一个女孩子家，\x01",
            "难道不想要衣服或者首饰之类的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#290F#1P我当然喜欢漂亮的衣服呀，\x01",
            "不过，再漂亮的衣服一会儿就弄脏了。\x02\x03",
            "首饰也是一样哦，\x01",
            "活动的时候很容易就会坏掉。\x02\x03",
            "对了，爸爸。\x01",
            "你抱着这么大的毛毯做什么呀……\x02\x03",
            "难道说……那就是给我的礼物？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#4P呵呵，你眼睛真尖……\x02\x03",
            "#080F嘿嘿……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4924():
        OP_6D(-400, 0, -2200, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4924)
    Fade(1500)
    OP_8C(0x8, 315, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x8,
        "男孩",
        "#305F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#293F#1P…………啊？\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#081F#4P看，就是这个了。\x02\x03",
            "很帅的小伙子吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#293F#1P什、什、什……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0xB,
        "#294F#3S#1P什么呀，这男孩！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#4P别这么大声，\x01",
            "不然会把他吵醒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#292F#1P吵醒……\x01",
            "这孩子还活着吧？\x02\x03",
            "看起来很虚弱的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F#4P我已经给他包扎好伤口了，\x01",
            "这小子应该不会有生命危险的。\x02\x03",
            "不过，总而言之……\x01",
            "还是先让他好好休息一下才行。\x02\x03",
            "我把他抱到床上去，\x01",
            "艾丝蒂尔你赶快去烧些开水。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#291F#1P嗯，知道了～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_66(0x1)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, 8900, 0, 68600, 180)
    SetChrPos(0x8, 8550, 0, 69460, 180)
    SetChrPos(0xC, 8550, 500, 67500, 270)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0xC, 15)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xC, 0x80)
    OP_72(0x5, 0x4)
    OP_72(0x5, 0x20)
    OP_6F(0x5, 0)
    OP_6D(8550, 0, 69460, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#290F#2P睡得真香啊……\x02\x03",
            "这男孩……\x01",
            "和我差不多大吧。\x02\x03",
            "这么乌黑的头发，\x01",
            "我还是头一次见呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F确实是很漂亮的黑发啊。\x02\x03",
            "而且眼睛还是琥珀色的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#290F#2P嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)

    ChrTalk(
        0xB,
        (
            "#292F#2P先不说这个……\x01",
            "现在该把事情交代清楚了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#084F噢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#292F#2P这小男孩到底是谁？\x02\x03",
            "为什么他会受伤？\x02\x03",
            "还有，\x01",
            "为什么爸爸你要把他带回家来？\x02\x03",
            "难道是私生子？\x01",
            "难道你背叛了妈妈！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#083F唉……\x01",
            "我说你到底是从哪学来这些话的。\x02\x03",
            "#080F一定是那个雪拉扎德教的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#291F#2P嗯，没错！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F那个不知天高地厚的女人也真是的……\x02\x03",
            "#080F其实爸爸我也是\x01",
            "因为工作关系才认识这孩子的。\x02\x03",
            "我连他的名字都还不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#290F#2P工作？是指游击士的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F是啊。\x02\x03",
            "哦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#293F#2P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#080F好像醒了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    def lambda_5068():
        OP_6D(8900, 0, 68600, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5068)
    Sleep(2000)
    OP_99(0xC, 0x0, 0x1, 0x3E8)
    Sleep(500)

    ChrTalk(
        0xC,
        "#306F嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#293F哇，真的是琥珀色哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#307F…………………………\x02\x03",
            "#307F…………这里是…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F小子，你醒了啊。\x02\x03",
            "这里是我家。\x01",
            "总之你放心就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#301F…………………………\x02\x03",
            "#301F……你这是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#293F哈？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#307F简直无法理解……\x02\x03",
            "#307F为什么这样做……\x01",
            "你其实可以丢下我不管呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#084F你问为什么啊。\x02\x03",
            "#081F也许是所谓的理所当然吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xC, 0x1, 0x2, 0x5DC)
    Sleep(400)

    def lambda_52AB():
        OP_7C(0x0, 0xC8, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_52AB)

    ChrTalk(
        0xC,
        (
            "#302F别、别开玩笑了！\x02\x03",
            "#302F卡西乌斯·布莱特！\x01",
            "你知道自己在做什么吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#294F喂！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x4)
    OP_95(0xB, 0xFFFFFF38, 0x320, 0xFFFFFB50, 0x4B0, 0x1770)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_A1(0x16, 0x5)

    def lambda_537B():
        OP_99(0xC, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_537B)

    def lambda_538B():
        OP_95(0xC, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_538B)

    def lambda_53A9():
        OP_95(0x16, 0x0, 0x0, 0x0, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_53A9)
    OP_22(0x7D, 0x0, 0x64)
    OP_95(0xB, 0xC8, 0xFFFFFCE0, 0x4B0, 0xC8, 0x1770)
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "#294F你一个受伤的小男孩\x01",
            "别这么大声叫嚷好不好！\x02\x03",
            "你不知道这样会弄痛伤口的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#304F…………………………\x02\x03",
            "#304F………………你是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#294F我叫艾丝蒂尔！\x02\x03",
            "艾丝蒂尔·布莱特！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#080F这是我的女儿。\x02\x03",
            "之前不是和你说过吗。\x01",
            "我有一个和你差不多大的女儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#307F好像提起过……\x02\x03",
            "#302F现、现在是说这种事情的时候吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xB, 0xFFFFFF38, 0x320, 0xFFFFFB50, 0x4B0, 0x1770)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_22(0x7D, 0x0, 0x64)

    def lambda_55D6():
        OP_99(0xC, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_55D6)

    def lambda_55E6():
        OP_95(0xC, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_55E6)

    def lambda_5604():
        OP_95(0x16, 0x0, 0x0, 0x0, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5604)
    OP_95(0xB, 0xC8, 0xFFFFFCE0, 0x4B0, 0xC8, 0x1770)
    OP_95(0xB, 0xFFFFFF38, 0x320, 0xFFFFFB50, 0x5DC, 0x1770)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0x7D, 0x0, 0x64)

    def lambda_5666():
        OP_99(0xC, 0x0, 0x2, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5666)

    def lambda_5676():
        OP_95(0xC, 0x0, 0x0, 0x0, 0xFA, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5676)

    def lambda_5694():
        OP_95(0x16, 0x0, 0x0, 0x0, 0x64, 0x5DC)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5694)
    OP_95(0xB, 0xC8, 0xFFFFFCE0, 0x4B0, 0x1F4, 0x1770)
    Sleep(400)

    ChrTalk(
        0xC,
        "#303F疼啊☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#294F不要那么大声！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#300F知、知道了……\x02\x03",
            "#300F但是你这么做……\x01",
            "不是反而会让我伤口更痛吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#292F你说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#300F我是说会伤上加伤……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#291F#3S你·刚·才·说·什·么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#304F没、没什么了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#081F呵呵，\x01",
            "在这个家里千万不要和艾丝蒂尔作对哦。\x02\x03",
            "她要是真的发起脾气来，\x01",
            "连我也对付不了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#304F看得出来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#292F对了，我说你。\x01",
            "是不是忘了一件事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#304F啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#291F名字啊，你的名字。\x01",
            "我刚才不是说了我的吗。\x02\x03",
            "你知道我的，我却不知道你的。\x01",
            "这不公平！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#304F……啊……\x02\x03",
            "#301F…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xC, 0x2, 0x1, 0x5DC)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#080F嗯，有道理。\x01",
            "事到如今也没必要再隐瞒了吧。\x02\x03",
            "不知道名字也不方便，能告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#301F…………………………\x02\x03",
            "#307F#40W我……知道了……\x02\x03",
            "#307F#40W我……#400W　\x01",
            "#80W我的名字是……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B7C")
    Fade(3000)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    OP_77(0x0, 0x0, 0x0, 0xBB800, 0x0)
    OP_6B(3100, 3000)
    OP_20(0x5DC)
    OP_21()
    OP_6D(-9880, 0, -44600, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    PlayMovie(0x0, "ed6_op.avi")

    label("loc_5B4E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B7C")
    Sleep(10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_5B79")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "")
    NewScene("ED6_DT01/T0300   ._SN", 3, 0, 0)
    IdleLoop()

    label("loc_5B79")

    Jump("loc_5B4E")

    label("loc_5B7C")

    Fade(3000)
    OP_77(0x0, 0x0, 0x0, 0xBB800, 0x0)
    OP_6B(3100, 3000)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Call(1, 15)
    Return()

    # Function_14_429A end

    def Function_15_5BB0(): pass

    label("Function_15_5BB0")

    EventBegin(0x0)
    AddParty(0x0, 0xFF)
    AddParty(0x1, 0xFF)
    AddParty(0x2, 0xFF)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x103, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6D(78732, 0, -740, 0)
    SetChrPos(0x102, 78554, 0, -1046, 0)
    SetChrPos(0x101, 78930, 0, 1500, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#013F…………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔，你还好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "……约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F晚饭已经准备好了。\x02\x03",
            "顺便告诉你一声，\x01",
            "今天晚上的菜是香酱烤鸡肉，\x01",
            "还有你最喜欢的洋葱奶汁烤菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "……听起来很丰盛呢……\x02\x03",
            "嗯，我一会儿就去，\x01",
            "你们两个先吃吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这样啊……\x02\x03",
            "我知道了。\x01",
            "可别等菜都凉了才下来哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(2000)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 16)
    SetChrSubChip(0x103, 11)
    SetChrPos(0x102, 3066, 0, -2366, 0)
    SetChrPos(0x101, 3066, 0, -2366, 0)
    SetChrPos(0x103, -9810, 250, 2050, 200)
    SetChrSubChip(0x14, 2)
    SetChrSubChip(0xE, 8)
    SetChrSubChip(0xF, 8)
    SetChrSubChip(0x10, 8)
    SetChrPos(0x14, -8500, 750, 1000, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0xE, -8060, 750, 300, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xF, -9320, 750, 300, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, -9520, 750, 1100, 0)
    ClearChrFlags(0x10, 0x80)
    OP_6B(3000, 0)
    OP_69(0x103, 0x0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#026F『命运之轮』……\x01",
            "又是这张牌啊。\x02\x03",
            "看来，有什么事情正在发生，\x01",
            "已经是无可置疑的事实了……\x02\x03",
            "不过，现在还不知道是怎样的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x103, 0xB, 0x9, 0x3E8)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 11)
    SetChrSubChip(0x103, 0)
    OP_62(0x103, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    SetChrSubChip(0x103, 1)

    def lambda_5F48():
        OP_6D(-7800, 1150, 1700, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F48)
    OP_8E(0x102, 0xFFFFEDEA, 0x0, 0xFA, 0xBB8, 0x0)

    ChrTalk(
        0x103,
        "#023F啊，艾丝蒂尔怎样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P刚才我叫她下来吃饭……\x01",
            "不过她好像没什么食欲的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#522F是吗……\x02\x03",
            "就算是平时多么活泼的女孩，\x01",
            "遇到这种事情也承受不了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#2P……这也是没办法的事啊。\x02\x03",
            "不管怎么说，\x01",
            "他们父女俩的感情那么好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F是啊……\x02\x03",
            "……………………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_60D5():
        OP_6D(-8020, 0, 1120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60D5)
    OP_8E(0x102, 0xFFFFE214, 0x0, 0xFFFFF902, 0xBB8, 0x0)
    OP_8E(0x102, 0xFFFFD7A6, 0x0, 0xFFFFFA60, 0xBB8, 0x0)
    SetChrSubChip(0x103, 0)
    OP_8E(0x102, 0xFFFFD76A, 0x0, 0xFFFFFDB2, 0xBB8, 0x0)
    Fade(1000)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 9)
    SetChrPos(0x102, -9550, 200, -520, 20)
    Sleep(1000)
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(
        0x102,
        (
            "#012F#4P雪拉姐姐你是怎么想的？\x02\x03",
            "这次的事件是单纯的事故，\x01",
            "还是人为的案件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#522F#1P……说实话，我也不能断定。\x02\x03",
            "老师是一流的游击士。\x01",
            "对于任何突发的危机\x01",
            "都有着十分果断的应付能力。\x02\x03",
            "不管是意外还是案件，\x01",
            "只要有老师在场的话，\x01",
            "都应该能够立刻解决掉的。\x02\x03",
            "#026F可是实际情况却是，\x01",
            "定期船和老师都失踪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F#4P不可能发生的事情却出现了……\x01",
            "你是这个意思吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#1P呵呵，不要这么沮丧嘛。\x02\x03",
            "你应该更加振作起来，\x01",
            "因为你现在是艾丝蒂尔唯一支柱啊。\x02\x03",
            "明天，我也要开始行动了……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(
        0x101,
        (
            "#3P哈啊～真香啊～\x02\x03",
            "已经饿得受不了了～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_21()
    OP_1D(0xF)

    def lambda_6497():
        OP_6D(-5000, 0, 1000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6497)
    SetChrSubChip(0x103, 1)
    Sleep(500)
    SetChrSubChip(0x102, 2)
    OP_8E(0x101, 0xFFFFEDEA, 0x0, 0xFA, 0xBB8, 0x0)

    ChrTalk(
        0x102,
        "#014F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F#5P艾丝蒂尔……\x01",
            "你没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不行啦不行啦。\x01",
            "肚子已经快要饿扁了。\x02\x03",
            "#501F哇～看上去好好吃呢！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_655F():
        OP_6D(-8590, 200, 780, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_655F)
    OP_8E(0x101, 0xFFFFE2C8, 0x0, 0xFFFFFDEE, 0xBB8, 0x0)
    Fade(1000)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 8)
    SetChrPos(0x101, -8230, 200, -520, 0)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#001F#2P我不客气啦～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x103)
    OP_63(0x102)
    SetChrSubChip(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#501F#2P哎，你们怎么不吃啊？\x02\x03",
            "奶汁烤菜很好吃呢。\x01",
            "洋葱的甜味也特别爽口。\x02\x03",
            "#001F不愧是约修亚。\x01",
            "做得真不错⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6P过、过奖了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#2P哎呀哎呀。\x01",
            "雪拉姐也别客气了。\x02\x03",
            "#004F啊，老爸藏起来的\x01",
            "白兰地你要不要喝点？\x02\x03",
            "#505F我记得好像是\x01",
            "２０年陈酿的『圣蔷薇』……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#024F#5P圣、圣蔷薇？\x01",
            "而且还是２０年陈酿！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0)

    ChrTalk(
        0x102,
        "#017F#6P我说啊，雪拉姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F#5P…………啊。\x01",
            "咳咳，这个等会再说吧。\x02\x03",
            "#020F话说回来，你这是怎么了？\x02\x03",
            "刚才约修亚去叫你，\x01",
            "你不是不肯下来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#2P嗯？\x01",
            "啊啊，我正在找替换用的睡衣呢。\x02\x03",
            "因为一直忙着在里面找东西，\x01",
            "所以没有注意啦～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 2)

    ChrTalk(
        0x102,
        "#018F#6P睡、睡衣？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P而且还有套装旅行用具。\x02\x03",
            "虽然不知道能不能派上用场，\x01",
            "不过不是有句话叫『有备无患』嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#023F#5P你难道要……\x02\x03",
            "为了确认老师的消息\x01",
            "而打算去趟柏斯吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P那当然啦。\x02\x03",
            "虽然觉得那个霉运超强的老爸\x01",
            "不会发生什么事情……\x02\x03",
            "不过就这样干等着实在不是我的性格，\x01",
            "所以想亲自去确认一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#011F#6P哈哈……\x01",
            "你这孩子真是……\x02\x03",
            "#011F不知道该说是乐观呢，\x01",
            "还是粗神经呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#2P什么呀～真没礼貌。\x02\x03",
            "#006F反正约修亚你\x01",
            "一定会和我一起去吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P那是当然的了。\x02\x03",
            "但是要知道，\x01",
            "定期船在军队的搜索行动结束之前\x01",
            "是不会恢复航运的。\x02\x03",
            "所以，我们要到柏斯去的话，\x01",
            "也只能从街道上走过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F#2P步行到柏斯……\x01",
            "要花多长时间呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#026F#5P按照游击士的脚力，\x01",
            "快的话半天左右就能到了。\x02\x03",
            "#020F不过也真是的……\x01",
            "这些话你应该早点说嘛。\x02\x03",
            "我也正打算这么做呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F#2P哎……\x01",
            "雪拉姐也要一起去吗？\x02\x03",
            "可是，工作不是很忙吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#5P我可是卡西乌斯老师的徒弟哦。\x02\x03",
            "听说老师出了事，\x01",
            "我怎么能够安心在这里留守呢？\x02\x03",
            "协会的工作，\x01",
            "我已经拜托爱娜让其它的成员去做了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#2P雪拉姐……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0)

    ChrTalk(
        0x102,
        "#010F#6P雪拉姐姐，谢谢你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F#5P不用感谢我啦。\x02\x03",
            "这种事件交给新人去调查，\x01",
            "我也放心不下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F#2P呜～真不甘心……\x01",
            "不过这样说好像也没错。\x02\x03",
            "#007F算了，反正有雪拉姐一起，\x01",
            "我们也更加放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F#6P那就请多关照了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F#5P呵呵，彼此彼此。\x02\x03",
            "#020F总之，\x01",
            "明早出发前去一趟协会吧。\x02\x03",
            "必须向爱娜说明一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_AD(0x4003D, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_15_5BB0 end

    def Function_16_71F3(): pass

    label("Function_16_71F3")

    EventBegin(0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x10, -8260, 700, 1100, 0)
    SetChrPos(0x14, -9520, 700, 1100, 0)
    SetChrPos(0x10, -8360, 800, 300, 0)
    SetChrPos(0x14, -9620, 800, 300, 0)
    SetChrChipByIndex(0x10, 13)
    SetChrChipByIndex(0x14, 12)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x14, 0)

    ChrTalk(
        0x0,
        "0\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 1)
    SetChrSubChip(0x14, 1)

    ChrTalk(
        0x0,
        "1\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 2)
    SetChrSubChip(0x14, 2)

    ChrTalk(
        0x0,
        "2\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 3)
    SetChrSubChip(0x14, 3)

    ChrTalk(
        0x0,
        "3\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 4)
    SetChrSubChip(0x14, 4)

    ChrTalk(
        0x0,
        "4\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 5)
    SetChrSubChip(0x14, 5)

    ChrTalk(
        0x0,
        "5\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 6)
    SetChrSubChip(0x14, 6)

    ChrTalk(
        0x0,
        "6\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 7)
    SetChrSubChip(0x14, 7)

    ChrTalk(
        0x0,
        "7\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 8)
    SetChrSubChip(0x14, 8)

    ChrTalk(
        0x0,
        "8\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 9)
    SetChrSubChip(0x14, 9)

    ChrTalk(
        0x0,
        "9\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 10)
    SetChrSubChip(0x14, 10)

    ChrTalk(
        0x0,
        "10\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 11)
    SetChrSubChip(0x14, 11)

    ChrTalk(
        0x0,
        "11\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 12)
    SetChrSubChip(0x14, 12)

    ChrTalk(
        0x0,
        "12\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 13)
    SetChrSubChip(0x14, 13)

    ChrTalk(
        0x0,
        "13\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 14)
    SetChrSubChip(0x14, 14)

    ChrTalk(
        0x0,
        "14\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 15)
    SetChrSubChip(0x14, 15)

    ChrTalk(
        0x0,
        "15\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 16)
    SetChrSubChip(0x14, 16)

    ChrTalk(
        0x0,
        "16\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 17)
    SetChrSubChip(0x14, 17)

    ChrTalk(
        0x0,
        "17\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 18)
    SetChrSubChip(0x14, 18)

    ChrTalk(
        0x0,
        "18\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 19)
    SetChrSubChip(0x14, 19)

    ChrTalk(
        0x0,
        "19\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 20)
    SetChrSubChip(0x14, 20)

    ChrTalk(
        0x0,
        "20\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 21)
    SetChrSubChip(0x14, 21)

    ChrTalk(
        0x0,
        "21\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 22)
    SetChrSubChip(0x14, 22)

    ChrTalk(
        0x0,
        "22\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 23)
    SetChrSubChip(0x14, 23)

    ChrTalk(
        0x0,
        "23\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 24)
    SetChrSubChip(0x14, 24)

    ChrTalk(
        0x0,
        "24\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 25)
    SetChrSubChip(0x14, 25)

    ChrTalk(
        0x0,
        "25\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 26)
    SetChrSubChip(0x14, 26)

    ChrTalk(
        0x0,
        "26\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 27)
    SetChrSubChip(0x14, 27)

    ChrTalk(
        0x0,
        "27\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 28)
    SetChrSubChip(0x14, 28)

    ChrTalk(
        0x0,
        "28\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 29)
    SetChrSubChip(0x14, 29)

    ChrTalk(
        0x0,
        "29\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 30)
    SetChrSubChip(0x14, 30)

    ChrTalk(
        0x0,
        "30\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 31)
    SetChrSubChip(0x14, 31)

    ChrTalk(
        0x0,
        "31\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x14, 0x80)
    EventEnd(0x0)
    Return()

    # Function_16_71F3 end

    def Function_17_7490(): pass

    label("Function_17_7490")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "休息\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7528")
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_7528")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7542")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_7542")

    Return()

    # Function_17_7490 end

    SaveToFile()

Try(main)
