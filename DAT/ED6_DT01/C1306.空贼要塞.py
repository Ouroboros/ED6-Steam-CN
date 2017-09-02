from ED6ScenarioHelper import *

def main():
    # 空贼要塞

    CreateScenaFile(
        FileName            = 'C1306   ._SN',
        MapName             = 'Bose',
        Location            = 'C1306.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60031",
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
        '空贼阿伦',                             # 9
        '空贼洛西',                             # 10
        '空贼蒂诺',                             # 11
        '空贼雷古',                             # 12
        '空贼',                                 # 13
        '空贼',                                 # 14
        '空贼',                                 # 15
        '空贼',                                 # 16
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
        Unknown_3A              = 52,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00360 ._CH',             # 00
        'ED6_DT07/CH00364 ._CH',             # 01
        'ED6_DT07/CH00361 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT07/CH00130 ._CH',             # 06
        'ED6_DT09/CH10380 ._CH',             # 07
        'ED6_DT09/CH10381 ._CH',             # 08
        'ED6_DT09/CH10390 ._CH',             # 09
        'ED6_DT09/CH10391 ._CH',             # 0A
        'ED6_DT09/CH10250 ._CH',             # 0B
        'ED6_DT09/CH10251 ._CH',             # 0C
        'ED6_DT06/CH20074 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH00360P._CP',             # 00
        'ED6_DT07/CH00364P._CP',             # 01
        'ED6_DT07/CH00361P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT07/CH00130P._CP',             # 06
        'ED6_DT09/CH10380P._CP',             # 07
        'ED6_DT09/CH10381P._CP',             # 08
        'ED6_DT09/CH10390P._CP',             # 09
        'ED6_DT09/CH10391P._CP',             # 0A
        'ED6_DT09/CH10250P._CP',             # 0B
        'ED6_DT09/CH10251P._CP',             # 0C
        'ED6_DT06/CH20074P._CP',             # 0D
    )

    DeclNpc(
        X                   = 800,
        Z                   = 500,
        Y                   = 500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 500,
        Y                   = -2800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -57220,
        Z                   = 0,
        Y                   = -50730,
        Unknown_0C          = 179,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xA6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -7780,
        Z                   = 0,
        Y                   = 56000,
        Unknown_0C          = 261,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xAA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 53910,
        Z                   = 0,
        Y                   = 56840,
        Unknown_0C          = 123,
        Unknown_0E          = 11,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xAB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 104400,
        Z                   = 0,
        Y                   = 10510,
        Unknown_0C          = 331,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xAB,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -1020,
        TriggerZ            = 0,
        TriggerY            = -145940,
        TriggerRange        = 800,
        ActorX              = -1020,
        ActorZ              = 1000,
        ActorY              = -145940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -57350,
        TriggerZ            = 0,
        TriggerY            = 108350,
        TriggerRange        = 800,
        ActorX              = -57350,
        ActorZ              = 1000,
        ActorY              = 108350,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -142790,
        TriggerZ            = 0,
        TriggerY            = 58560,
        TriggerRange        = 1000,
        ActorX              = -142760,
        ActorZ              = 1500,
        ActorY              = 59200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -55470,
        TriggerZ            = 0,
        TriggerY            = -105270,
        TriggerRange        = 1000,
        ActorX              = -54920,
        ActorZ              = 1500,
        ActorY              = -105280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_31A",          # 00, 0
        "Function_1_4ED",          # 01, 1
        "Function_2_54F",          # 02, 2
        "Function_3_565",          # 03, 3
        "Function_4_A8E",          # 04, 4
        "Function_5_AC3",          # 05, 5
        "Function_6_B11",          # 06, 6
        "Function_7_B4B",          # 07, 7
        "Function_8_B7E",          # 08, 8
        "Function_9_DE1",          # 09, 9
        "Function_10_EFB",         # 0A, 10
        "Function_11_12EB",        # 0B, 11
        "Function_12_16FF",        # 0C, 12
        "Function_13_19A2",        # 0D, 13
        "Function_14_1B0E",        # 0E, 14
    )


    def Function_0_31A(): pass

    label("Function_0_31A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_32E"),
        (131, "loc_340"),
        (101, "loc_353"),
        (SWITCH_DEFAULT, "loc_366"),
    )


    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_A2(0x354)
    Event(0, 3)

    label("loc_33D")

    Jump("loc_366")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350")
    Event(0, 10)

    label("loc_350")

    Jump("loc_366")

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_363")
    Event(0, 11)

    label("loc_363")

    Jump("loc_366")

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_END)), "loc_429")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    SetChrPos(0xA, 56490, 0, -52990, 350)
    SetChrPos(0xB, 56660, 0, -56070, 0)
    SetChrPos(0xD, 55510, 0, -54710, 45)
    SetChrPos(0xE, 55110, 0, -52150, 90)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    SetChrChipByIndex(0xA, 13)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xA, 0xFF)

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 2)), scpexpr(EXPR_END)), "loc_4EC")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrFlags(0xF, 0x800)
    SetChrPos(0x8, 940, 0, -770, 0)
    SetChrPos(0x9, 930, 0, -3680, 90)
    SetChrPos(0xC, 510, 0, -2250, 300)
    SetChrPos(0xF, 500, 0, 580, 45)
    SetChrChipByIndex(0xC, 13)
    SetChrChipByIndex(0xF, 13)
    SetChrChipByIndex(0x8, 13)
    SetChrChipByIndex(0x9, 13)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xC, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)

    label("loc_4EC")

    Return()

    # Function_0_31A end

    def Function_1_4ED(): pass

    label("Function_1_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_509")
    OP_1B(0x26, 0x0, 0x8)
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    Jump("loc_50D")

    label("loc_509")

    OP_64(0x0, 0x1)

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F")
    OP_6F(0x2, 0)
    Jump("loc_526")

    label("loc_51F")

    OP_6F(0x2, 60)

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538")
    OP_6F(0x3, 0)
    Jump("loc_53F")

    label("loc_538")

    OP_6F(0x3, 60)

    label("loc_53F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_54E")
    OP_64(0x1, 0x1)

    label("loc_54E")

    Return()

    # Function_1_4ED end

    def Function_2_54F(): pass

    label("Function_2_54F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_564")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_54F")

    label("loc_564")

    Return()

    # Function_2_54F end

    def Function_3_565(): pass

    label("Function_3_565")

    EventBegin(0x0)
    OP_6D(3220, 1250, 4120, 0)
    SetChrPos(0x101, 5490, 3500, 5190, 270)
    SetChrPos(0x102, 5490, 3500, 5190, 270)
    SetChrPos(0x103, 5490, 3500, 5190, 270)
    SetChrPos(0x104, 5490, 3500, 5190, 270)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)

    def lambda_5D6():
        OP_6D(3150, 0, 510, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D6)
    OP_43(0x101, 0x1, 0x0, 0x4)
    OP_43(0x102, 0x1, 0x0, 0x5)
    OP_43(0x103, 0x1, 0x0, 0x6)
    OP_43(0x104, 0x1, 0x0, 0x7)
    WaitChrThread(0x104, 0x1)

    ChrTalk(
        0x101,
        (
            "#002F说起来……\x01",
            "这里到底是个什么地方啊？\x02\x03",
            "就算是他们建的基地，\x01",
            "也未免太大、太古老了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    ChrTalk(
        0x103,
        (
            "#020F应该是古时候残存下来的堡垒。\x02\x03",
            "空贼团发现这里之后，\x01",
            "当作是自己的基地来用了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F『大崩坏』之后，\x01",
            "整个世界可是持续了数百年的战乱啊。\x02\x03",
            "有这样大规模的堡垒残留下来，\x01",
            "也没什么不可思议的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F『大崩坏』？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F就是距今１２００年前\x01",
            "所发生的古代塞姆里亚文明崩溃。\x02\x03",
            "传说是因为天地异变造成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F啊，之前亚鲁瓦教授也说过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F把这种地方用作自己的基地，\x01",
            "空贼还真是完全没品位可言呢。\x02\x03",
            "#027F不仅四周有魔兽游荡……\x01",
            "而且充满男人的臭汗味。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#018F我说雪拉姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#034F这还真是激烈又极端的看法啊。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_565 end

    def Function_4_A8E(): pass

    label("Function_4_A8E")

    ClearChrFlags(0x101, 0x80)
    OP_8E(0xFE, 0xBD3, 0x7D0, 0x1255, 0x1388, 0x0)
    OP_8E(0xFE, 0xAB4, 0x0, 0xFFFFFB5A, 0x1388, 0x0)
    TurnDirection(0xFE, 0x102, 400)
    Return()

    # Function_4_A8E end

    def Function_5_AC3(): pass

    label("Function_5_AC3")

    Sleep(800)
    ClearChrFlags(0x102, 0x80)
    OP_8E(0xFE, 0xBD3, 0x7D0, 0x1255, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA82, 0x0, 0x370, 0xBB8, 0x0)
    OP_8E(0xFE, 0x726, 0x0, 0x6E, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_5_AC3 end

    def Function_6_B11(): pass

    label("Function_6_B11")

    Sleep(1600)
    ClearChrFlags(0x103, 0x80)
    OP_8E(0xFE, 0xBD3, 0x7D0, 0x1255, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD1B, 0x0, 0xC8, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_6_B11 end

    def Function_7_B4B(): pass

    label("Function_7_B4B")

    Sleep(2400)
    ClearChrFlags(0x104, 0x80)
    OP_8E(0xFE, 0xBD3, 0x7D0, 0x1255, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA82, 0x0, 0x370, 0xBB8, 0x0)
    Return()

    # Function_7_B4B end

    def Function_8_B7E(): pass

    label("Function_8_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE0")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC8")

    def lambda_BA8():
        OP_6D(-4700, 0, -147260, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_BA8)
    Sleep(600)
    OP_8C(0x102, 90, 400)

    ChrTalk(
        0x102,
        (
            "#012F等一下……\x02\x03",
            "从那道门可以听到说话的声音。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C25():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C25)

    def lambda_C33():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C33)
    OP_8C(0x103, 90, 400)

    ChrTalk(
        0x103,
        (
            "#022F看起来空贼就在这里呢。\x01",
            "先把他们解决掉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC5")

    label("loc_CC8")


    def lambda_CCE():
        OP_6D(-4700, 0, -147260, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_CCE)
    Sleep(600)
    OP_8C(0x104, 90, 400)

    ChrTalk(
        0x104,
        (
            "#033F哎呀……\x02\x03",
            "从那道门可以听到说话的声音呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D5A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D5A)

    def lambda_D68():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D68)
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        (
            "#002F难道是空贼？\x01",
            "那先把这里解决掉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC5")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_DE0")

    Return()

    # Function_8_B7E end

    def Function_9_DE1(): pass

    label("Function_9_DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFA")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有男人说话的声音传出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x102,
        (
            "#012F又有说话声。\x01",
            "……要闯进去吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【闯进去】\x01",        # 0
            "【还是算了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_EE6"),
        (0, "loc_EEB"),
        (SWITCH_DEFAULT, "loc_EFA"),
    )


    label("loc_EE6")

    EventEnd(0x1)
    Jump("loc_EFA")

    label("loc_EEB")

    OP_A2(0x3FB)
    NewScene("ED6_DT01/C1304   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_EFA")

    label("loc_EFA")

    Return()

    # Function_9_DE1 end

    def Function_10_EFB(): pass

    label("Function_10_EFB")

    EventBegin(0x0)
    OP_6D(59090, 0, -54570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 57770, 0, -52340, 180)
    SetChrPos(0xB, 59050, 0, -52450, 180)
    SetChrPos(0xD, 60650, 0, -51550, 180)
    SetChrPos(0xE, 56680, 0, -51410, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x101, 58000, 0, -56220, 0)
    SetChrPos(0x102, 57090, 0, -57040, 0)
    SetChrPos(0x103, 59130, 0, -56480, 0)
    SetChrPos(0x104, 59940, 0, -57280, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x103, 5)
    SetChrChipByIndex(0x104, 6)
    OP_0D()

    ChrTalk(
        0xB,
        "给我站住！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "有我们在，你们休想通过这里！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F已、已经醒过来了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F很顽强的家伙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#024F呼，既然不听劝，\x01",
            "就别怪我们动用武力了！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrChipByIndex(0xB, 2)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xD, 2)
    SetChrChipByIndex(0xE, 2)

    def lambda_112B():
        OP_8E(0xFE, 0xE2A4, 0x0, 0xFFFECD7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_112B)

    def lambda_1146():
        OP_8E(0xFE, 0xE2A4, 0x0, 0xFFFECD7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1146)

    def lambda_1161():
        OP_8E(0xFE, 0xE2A4, 0x0, 0xFFFECD7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1161)

    def lambda_117C():
        OP_8E(0xFE, 0xE2A4, 0x0, 0xFFFECD7A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_117C)
    Sleep(400)
    Battle(0x38D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_11AF"),
        (SWITCH_DEFAULT, "loc_11B2"),
    )


    label("loc_11AF")

    OP_B4(0x0)
    Return()

    label("loc_11B2")

    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    SetChrPos(0xA, 56490, 0, -52990, 350)
    SetChrPos(0xB, 56660, 0, -56070, 0)
    SetChrPos(0xD, 55510, 0, -54710, 45)
    SetChrPos(0xE, 55110, 0, -52150, 90)
    SetChrChipByIndex(0xB, 13)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    SetChrChipByIndex(0xA, 13)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    SetChrPos(0x101, 58700, 0, -53950, 270)
    SetChrPos(0x102, 58700, 0, -53950, 270)
    SetChrPos(0x103, 58700, 0, -53950, 270)
    SetChrPos(0x104, 58700, 0, -53950, 270)
    OP_6D(58700, 0, -53950, 0)
    OP_6B(2600, 0)
    FadeToBright(1000, 0)
    OP_A2(0x359)
    EventEnd(0x0)
    Return()

    # Function_10_EFB end

    def Function_11_12EB(): pass

    label("Function_11_12EB")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(2880, 0, -3610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 2970, 0, -700, 180)
    SetChrPos(0x9, 1580, 0, -1100, 180)
    SetChrPos(0xC, 3050, 0, 910, 180)
    SetChrPos(0xF, 1640, 0, 500, 180)
    SetChrPos(0x101, 1560, 0, -5690, 0)
    SetChrPos(0x102, 510, 0, -6570, 0)
    SetChrPos(0x103, 2530, 0, -5860, 0)
    SetChrPos(0x104, 3240, 0, -6510, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x103, 5)
    SetChrChipByIndex(0x104, 6)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "哼！\x01",
            "别想再上去了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "快点带着人质滚吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F又来了……\x01",
            "真是不知悔改的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F为了让首领逃跑，\x01",
            "打算这样拖延时间吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哈，我们平时受到\x01",
            "大哥他们很多的照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "这回是报恩的时候了！\x02",
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrChipByIndex(0xC, 2)
    SetChrChipByIndex(0xF, 2)
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 2)

    def lambda_153F():
        OP_8E(0xFE, 0x730, 0x0, 0xFFFFC54A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_153F)

    def lambda_155A():
        OP_8E(0xFE, 0x730, 0x0, 0xFFFFC54A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_155A)

    def lambda_1575():
        OP_8E(0xFE, 0x730, 0x0, 0xFFFFC54A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1575)

    def lambda_1590():
        OP_8E(0xFE, 0x730, 0x0, 0xFFFFC54A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1590)
    Sleep(500)
    Battle(0x38E, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_15C3"),
        (SWITCH_DEFAULT, "loc_15C6"),
    )


    label("loc_15C3")

    OP_B4(0x0)
    Return()

    label("loc_15C6")

    SetChrPos(0x8, 940, 0, -770, 0)
    SetChrPos(0x9, 930, 0, -3680, 90)
    SetChrPos(0xC, 510, 0, -2250, 300)
    SetChrPos(0xF, 500, 0, 580, 45)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrFlags(0xF, 0x800)
    SetChrChipByIndex(0xC, 13)
    SetChrChipByIndex(0xF, 13)
    SetChrChipByIndex(0x8, 13)
    SetChrChipByIndex(0x9, 13)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xC, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrPos(0x101, 3010, 0, -1740, 270)
    SetChrPos(0x102, 3010, 0, -1740, 270)
    SetChrPos(0x103, 3010, 0, -1740, 270)
    SetChrPos(0x104, 3010, 0, -1740, 270)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0x104, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0x104, 65535)
    OP_6D(3010, 0, -1740, 0)
    OP_6B(2600, 0)
    FadeToBright(1000, 0)
    OP_A2(0x35A)
    EventEnd(0x0)
    Return()

    # Function_11_12EB end

    def Function_12_16FF(): pass

    label("Function_12_16FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A1")
    SetMapFlags(0x8000000)
    EventBegin(0x1)
    Fade(1000)
    SetChrPos(0x101, -56980, 0, 107430, 0)
    SetChrPos(0x102, -57900, 0, 106910, 0)
    SetChrPos(0x103, -57000, 0, 105940, 0)
    SetChrPos(0x104, -57970, 0, 105640, 0)
    OP_0D()
    Sleep(100)

    ChrTalk(
        0x101,
        "#501F这是什么…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是导力吸尘器。\x02\x03",
            "而且好像还是最新型号的，\x01",
            "也许是被偷来的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呼～原来是这样啊……\x02\x03",
            "#004F……咦？\x02\x03",
            "那是什么啊？\x01",
            "吸尘器盖子上夹着什么东西。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "黑色笔记本\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x14, 0x1, 0x8000)
    OP_3E(0x338, 1)
    OP_64(0x1, 0x1)
    Sleep(100)

    ChrTalk(
        0x102,
        "#014F这是……笔记本？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，好像是呢……\x02\x03",
            "不过为什么吸尘器里面\x01",
            "会有这种东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F这东西的来头可能不简单。\x02\x03",
            "为了慎重起见，还是把它保管起来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#006F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    ClearMapFlags(0x8000000)

    label("loc_19A1")

    Return()

    # Function_12_16FF end

    def Function_13_19A2(): pass

    label("Function_13_19A2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x60, 1)"), scpexpr(EXPR_END)), "loc_1A1B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "狩猎枪\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x370)
    Jump("loc_1A97")

    label("loc_1A1B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "狩猎枪\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "狩猎枪\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1A97")

    Jump("loc_1B00")

    label("loc_1A9A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x13)

    label("loc_1B00")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_19A2 end

    def Function_14_1B0E(): pass

    label("Function_14_1B0E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x116, 1)"), scpexpr(EXPR_END)), "loc_1B83")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斯托雷加Ｒ\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x371)
    Jump("loc_1BF7")

    label("loc_1B83")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "斯托雷加Ｒ\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "斯托雷加Ｒ\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1BF7")

    Jump("loc_1C42")

    label("loc_1BFA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x14)

    label("loc_1C42")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1B0E end

    SaveToFile()

Try(main)
