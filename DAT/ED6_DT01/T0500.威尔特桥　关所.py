from ED6ScenarioHelper import *

def main():
    # 威尔特桥　关所

    CreateScenaFile(
        FileName            = 'T0500   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0500.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0500   ._SN',
            'ED6_DT01/T0500_1 ._SN',
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
        '士兵斯科特',                           # 9
        '士兵哈罗德',                           # 10
        '阿斯顿队长',                           # 11
        '士兵安托斯',                           # 12
        '士兵拉科斯',                           # 13
        '斯丁克',                               # 14
        '亚妮拉丝',                             # 15
        '士兵斯科特',                           # 16
        '士兵哈罗德',                           # 17
        '艾丝蒂尔',                             # 18
        '约修亚',                               # 19
        '士兵斯科特',                           # 20
        '士兵哈罗德',                           # 21
        '艾丝蒂尔',                             # 22
        '米尔西街道方向',                       # 23
        '东柏斯街道方向',                       # 24
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
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
        Unknown_36              = 90,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 135,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 90,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH00320 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00110 ._CH',             # 04
        'ED6_DT07/CH00324 ._CH',             # 05
        'ED6_DT07/CH00104 ._CH',             # 06
        'ED6_DT07/CH01620 ._CH',             # 07
        'ED6_DT07/CH01630 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH00320P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00110P._CP',             # 04
        'ED6_DT07/CH00324P._CP',             # 05
        'ED6_DT07/CH00104P._CP',             # 06
        'ED6_DT07/CH01620P._CP',             # 07
        'ED6_DT07/CH01630P._CP',             # 08
    )

    DeclNpc(
        X                   = 2420,
        Z                   = 0,
        Y                   = -19010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 16920,
        Z                   = 120,
        Y                   = -7750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1400,
        Z                   = 0,
        Y                   = 21400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -3300,
        Z                   = 0,
        Y                   = 21400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 12900,
        Z                   = 0,
        Y                   = 4400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 5400,
        Z                   = 0,
        Y                   = 26700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -43000,
        Z                   = 0,
        Y                   = 42000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C9,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1980,
        Z                   = -410,
        Y                   = -40440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 440,
        Z                   = -510,
        Y                   = 41850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 5680,
        TriggerZ            = -260,
        TriggerY            = -27360,
        TriggerRange        = 1500,
        ActorX              = 5680,
        ActorZ              = 1700,
        ActorY              = -27360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -9630,
        TriggerZ            = -150,
        TriggerY            = 27430,
        TriggerRange        = 1500,
        ActorX              = -9630,
        ActorZ              = 1700,
        ActorY              = 27430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37E",          # 00, 0
        "Function_1_3C1",          # 01, 1
        "Function_2_400",          # 02, 2
        "Function_3_416",          # 03, 3
        "Function_4_43A",          # 04, 4
        "Function_5_594",          # 05, 5
        "Function_6_5FB",          # 06, 6
        "Function_7_662",          # 07, 7
        "Function_8_1972",         # 08, 8
        "Function_9_2281",         # 09, 9
        "Function_10_2A17",        # 0A, 10
        "Function_11_30D5",        # 0B, 11
        "Function_12_34BE",        # 0C, 12
        "Function_13_38F1",        # 0D, 13
    )


    def Function_0_37E(): pass

    label("Function_0_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 5)), scpexpr(EXPR_END)), "loc_388")
    Jump("loc_3AD")

    label("loc_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_397")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_3AD")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3A1")
    Jump("loc_3AD")

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3AD")
    ClearChrFlags(0xE, 0x80)

    label("loc_3AD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3B9"),
        (SWITCH_DEFAULT, "loc_3C0"),
    )


    label("loc_3B9")

    Event(1, 0)
    Jump("loc_3C0")

    label("loc_3C0")

    Return()

    # Function_0_37E end

    def Function_1_3C1(): pass

    label("Function_1_3C1")

    OP_16(0x2, 0xFA0, 0xFFFE0818, 0xFFFE0FE8, 0x30005)
    OP_72(0x2, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7")
    OP_6F(0x2, 420)

    label("loc_3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FF")
    OP_6F(0x1, 420)
    OP_72(0x1, 0x10)

    label("loc_3FF")

    Return()

    # Function_1_3C1 end

    def Function_2_400(): pass

    label("Function_2_400")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_415")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_400")

    label("loc_415")

    Return()

    # Function_2_400 end

    def Function_3_416(): pass

    label("Function_3_416")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_439")
    OP_8D(0xFE, 2000, 24900, 7200, 30100, 2000)
    Jump("Function_3_416")

    label("loc_439")

    Return()

    # Function_3_416 end

    def Function_4_43A(): pass

    label("Function_4_43A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_593")
    Sleep(3000)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0x438A, 0xFFFFFFC4, 0xFFFF9E94, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFABBE, 0xFFFFFF88, 0xFFFF9C14, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFAB46, 0xFFFFFEFC, 0xFFFF8DC8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFA, 0xFFFFFEF2, 0xFFFF9034, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8E(0xFE, 0x1054, 0xFFFFFF10, 0xFFFF89B8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x2C10, 0xFFFFFE2A, 0xFFFF8A08, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8E(0xFE, 0x2C1A, 0x50, 0xFFFFD79C, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8E(0xFE, 0x4236, 0xA, 0xFFFFD6E8, 0x9C4, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8E(0xFE, 0x4218, 0x78, 0xFFFFE1BA, 0x9C4, 0x0)
    Jump("Function_4_43A")

    label("loc_593")

    Return()

    # Function_4_43A end

    def Function_5_594(): pass

    label("Function_5_594")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东　洛连特市　１７２塞尔矩\x01",
            "西　柏斯市　　４２０塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_594 end

    def Function_6_5FB(): pass

    label("Function_6_5FB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西　柏斯市　　４２０塞尔矩\x01",
            "东　洛连特市　１７２塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_5FB end

    def Function_7_662(): pass

    label("Function_7_662")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_11C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_END)), "loc_DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D63")
    EventBegin(0x0)
    OP_4A(0x8, 0)
    Fade(1000)
    SetChrPos(0x101, 2370, 0, -20490, 0)
    SetChrPos(0x102, 3130, 0, -21420, 0)
    SetChrPos(0x103, 1570, 0, -21630, 0)
    TurnDirection(0xFE, 0x101, 0)
    OP_6C(45000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A")

    ChrTalk(
        0xFE,
        (
            "哟，各位辛苦了。\x01",
            "你们打算去柏斯吗？ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是的……\x01",
            "你是怎么知道的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "像你们这样的旅行者，\x01",
            "今天有很多从这里通过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "而且是平常通行量的好几倍。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是因为柏斯上空\x01",
            "实行了飞行管制的缘故吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正是如此。\x01",
            "搞得我现在忙死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F要知道，\x01",
            "实施飞行管制的是你们王国军队哦。\x02\x03",
            "难道你还有抱怨的立场吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔，话虽如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "这个关所也实行了通行管制。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要通过的话，\x01",
            "就到旁边的柜台向队长拿通行证吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，我们已经拿到了。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x32F, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "通行许可证\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0xFE,
        "哦，还真是准备充分啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B09")

    label("loc_A7A")


    ChrTalk(
        0x101,
        "#000F给，我们已经拿到通行证了。\x02",
    )

    CloseMessageWindow()
    OP_3F(0x32F, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "通行许可证\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0xFE,
        "哦，真快啊。\x02",
    )

    CloseMessageWindow()

    label("loc_B09")


    ChrTalk(
        0xFE,
        "那么就让你们通行吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "士兵操作遥控装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(500)
    OP_8C(0x101, 315, 400)
    OP_8C(0x102, 315, 400)
    OP_8C(0x103, 315, 400)
    Sleep(1000)

    def lambda_BB6():
        OP_6D(-900, 0, -9960, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BB6)

    def lambda_BCE():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BCE)

    def lambda_BDE():
        OP_67(0, 4000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BDE)

    def lambda_BF6():
        OP_6B(5500, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_BF6)
    Sleep(4000)
    OP_22(0xD0, 0x0, 0x64)
    OP_72(0x1, 0x800)
    OP_70(0x1, 0x1A4)
    OP_73(0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(2200, 0, -20370, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    TurnDirection(0xFE, 0x101, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "好了，可以通过了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    OP_8C(0x103, 0, 400)

    ChrTalk(
        0xFE,
        (
            "顺便提一下，一旦过了这个关所，\x01",
            "不拿到那一边的通行许可证\x01",
            "是不能再回到这边来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这件事请一定要注意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F知道了。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 0)
    EventEnd(0x0)
    OP_28(0x52, 0x1, 0x2)
    OP_A2(0x304)
    Jump("loc_DF6")

    label("loc_D63")


    ChrTalk(
        0xFE,
        (
            "顺便提一下，一旦过了这个关所，\x01",
            "不拿到那一边的通行许可证\x01",
            "是不能再回到这边来的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这件事请一定要注意。\x02",
    )

    CloseMessageWindow()

    label("loc_DF6")

    Jump("loc_11C4")

    label("loc_DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111D")
    EventBegin(0x0)

    ChrTalk(
        0xFE,
        (
            "哟，各位辛苦了。\x01",
            "你们打算去柏斯吗？ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是的……\x01",
            "你是怎么知道的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "像你们这样的旅行者，\x01",
            "今天有很多从这里通过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "而且是平常通行量的好几倍。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是因为柏斯上空\x01",
            "实行了飞行管制的缘故吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正是如此。\x01",
            "搞得我现在忙死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F要知道，\x01",
            "实施飞行管制的是你们王国军队哦。\x02\x03",
            "难道你还有抱怨的立场吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "唔，话虽如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "这个关所也实行了通行管制。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要通过的话，\x01",
            "就到旁边的柜台向队长拿通行证吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x302)
    EventEnd(0x1)
    Jump("loc_11C4")

    label("loc_111D")


    ChrTalk(
        0xFE,
        (
            "目前这个关所\x01",
            "这个关所也实行了通行管制。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "想要通过的话，\x01",
            "就到旁边的柜台向队长拿通行证吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C4")

    Jump("loc_196E")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1350")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127D")

    ChrTalk(
        0xFE,
        (
            "旁边的柏斯地区\x01",
            "最近连续发生了强盗案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好像是空贼干的好事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_134D")

    label("loc_127D")


    ChrTalk(
        0xFE,
        (
            "旁边的柏斯地区\x01",
            "最近连续发生了强盗案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好像是空贼干的好事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这样，事先训练说不定能得到回报……\x02",
    )

    CloseMessageWindow()

    label("loc_134D")

    Jump("loc_196E")

    label("loc_1350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1619")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144E")

    ChrTalk(
        0xFE,
        "不过也只能在这里说说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "队长在王都的总队中\x01",
            "好像非常有威望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然被编配到这种地方来，\x01",
            "是不是出什么事了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1616")

    label("loc_144E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1597")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "队长在王都的总队中\x01",
            "好像非常有威望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟然被编配到这种地方来，\x01",
            "是不是出什么事了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……说起来，\x01",
            "一来就进行战斗训练也太过分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好痛，身子还是很痛啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1616")

    label("loc_1597")


    ChrTalk(
        0xFE,
        "一来就进行战斗训练也太过分了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好痛，身子还是很痛啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1616")

    Jump("loc_196E")

    label("loc_1619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_17E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1775")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FA")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "今天也这样站了一天，\x01",
            "通行的人还真的很少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊，真无聊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无聊的时候就看看云的形状，\x01",
            "然后就开始玩起联想游戏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1772")

    label("loc_16FA")


    ChrTalk(
        0xFE,
        "啊啊，真无聊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "无聊的时候就看看云的形状，\x01",
            "然后就开始玩起联想游戏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1772")

    Jump("loc_17E5")

    label("loc_1775")


    ChrTalk(
        0xFE,
        (
            "虽然我很讨厌无聊，\x01",
            "但是我更讨厌训练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "训练完了之后\x01",
            "浑身上下都痛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好痛…………\x02",
    )

    CloseMessageWindow()

    label("loc_17E5")

    Jump("loc_196E")

    label("loc_17E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_196E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C6")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "定期船开始运航之后，\x01",
            "就基本没有人在街道上旅行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "就这样守卫关所也挺无聊的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只有队长一个人干劲十足啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_196E")

    label("loc_18C6")


    ChrTalk(
        0xFE,
        (
            "因为通行的人减少了，\x01",
            "守卫关所也变得无聊了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "只有队长一个人干劲十足啊。\x02",
    )

    CloseMessageWindow()

    label("loc_196E")

    TalkEnd(0x8)
    Return()

    # Function_7_662 end

    def Function_8_1972(): pass

    label("Function_8_1972")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE8")
    OP_A2(0x29C)

    ChrTalk(
        0xFE,
        (
            "自从我参军之后，\x01",
            "还是第一次这么忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在可不是一边钓鱼，\x01",
            "一边看书的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然这本书刚买不久……\x01",
            "就送给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是被队长发现了，\x01",
            "又要挨骂了。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x213, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第２卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_1BEF")

    label("loc_1AE8")


    ChrTalk(
        0xFE,
        (
            "自从我参军之后，\x01",
            "还是第一次这么忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就这样一直看守着\x01",
            "没什么人经过的关所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我第一次真实地感受到\x01",
            "自己是一名王国军军人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEF")

    Jump("loc_227D")

    label("loc_1BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1D50")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA8")

    ChrTalk(
        0xFE,
        (
            "现在也算是处于警戒状态中。\x01",
            "柏斯地区有一些坏人为非作歹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼呼……\x01",
            "不要来这里就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4D")

    label("loc_1CA8")


    ChrTalk(
        0xFE,
        (
            "现在也算是处于警戒状态中。\x01",
            "柏斯地区有一些坏人为非作歹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼呼……\x01",
            "我只希望在训练中进行战斗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4D")

    Jump("loc_227D")

    label("loc_1D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1F71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E33")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我在那条河里钓鱼，\x01",
            "结果被队长怒斥了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难得河里有那么多鱼，\x01",
            "河水也很清凉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好不容易有点心情……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EC7")

    label("loc_1E33")


    ChrTalk(
        0xFE,
        (
            "我在那条河里钓鱼，\x01",
            "结果被队长怒斥了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "难得这里有这么多鱼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EC7")

    Jump("loc_1F6E")

    label("loc_1ECA")


    ChrTalk(
        0xFE,
        (
            "之前我在那条河里钓鱼，\x01",
            "结果被队长怒斥了一顿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉，是不是因为这个\x01",
            "队长才那么严厉地训练我们……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F6E")

    Jump("loc_227D")

    label("loc_1F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_21FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2109")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206D")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "这个关所平时很少有人通过，\x01",
            "所以非常安静。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "来这里一听，\x01",
            "只有河水的流淌声和鸟鸣声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起我以前工作的农场\x01",
            "还要悠闲自得。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2106")

    label("loc_206D")


    ChrTalk(
        0xFE,
        (
            "站在这里仔细听，\x01",
            "只有河水的流淌声和鸟鸣声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "比起我以前工作的农场\x01",
            "还要悠闲自得。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2106")

    Jump("loc_21FC")

    label("loc_2109")


    ChrTalk(
        0xFE,
        (
            "这个关所平时很少有人通过，\x01",
            "所以非常安静。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "来这里一听，\x01",
            "只有河水的流淌声和鸟鸣声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，如果没有那样的训练，\x01",
            "真的比农场还要悠闲啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FC")

    Jump("loc_227D")

    label("loc_21FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_227D")

    ChrTalk(
        0xFE,
        "我才刚被编配到这里来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来是在农场工作，\x01",
            "但是还是想来参加王国军。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227D")

    TalkEnd(0x9)
    Return()

    # Function_8_1972 end

    def Function_9_2281(): pass

    label("Function_9_2281")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_231E")

    ChrTalk(
        0xFE,
        (
            "柏斯的盗窃案件\x01",
            "原来是空贼干的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "终于能够重归平静，\x01",
            "过回安稳生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A13")

    label("loc_231E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_24E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2428")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        "听说柏斯被强盗袭击了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "发生什么事情了……\x01",
            "我好想现在就赶过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我刚才看到\x01",
            "国境守备队的飞艇飞过来了，\x01",
            "应该是去调查了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E1")

    label("loc_2428")


    ChrTalk(
        0xFE,
        (
            "空贼也好，强盗也好，\x01",
            "真是有点为所欲为了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也不想呆在关所的守备队，\x01",
            "我想去前线啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E1")

    Jump("loc_2A13")

    label("loc_24E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_25B9")

    ChrTalk(
        0xFE,
        (
            "国境守备队好像\x01",
            "逮捕了不少嫌疑犯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一个由凶暴的女孩子领导的团体\x01",
            "和一个性格古怪的骗子，\x01",
            "但是这两者似乎都不是犯人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A13")

    label("loc_25B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2687")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "现在，\x01",
            "关所那边也没有什么新的消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王国军该如何行动，\x01",
            "现在一点也不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是急人啊……\x01",
            "我们也想出动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2713")

    label("loc_2687")


    ChrTalk(
        0xFE,
        (
            "现在，\x01",
            "关所那边也没有什么新的消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王国军该如何行动，\x01",
            "现在一点也不清楚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2713")

    Jump("loc_2A13")

    label("loc_2716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_27CD")

    ChrTalk(
        0xFE,
        (
            "和东侧比起来，\x01",
            "这个关所西侧聚集了更多经验丰富的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "戴恩副长\x01",
            "是个对工作一丝不苟的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A13")

    label("loc_27CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C8")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "对面的阿斯顿队长还真是厉害呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了重新锻炼新兵，\x01",
            "将他们全部都配置到自己的队里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然是个非常厉害而且正直的人，\x01",
            "但是这样要\x01",
            "付出常人两倍的辛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_295D")

    label("loc_28C8")


    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "对面的阿斯顿队长还真是厉害呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然是个非常厉害而且正直的人，\x01",
            "但是这样要\x01",
            "付出常人两倍的辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295D")

    Jump("loc_2A13")

    label("loc_2960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2A13")

    ChrTalk(
        0xFE,
        "喂，你们要去柏斯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在可是非常时期呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我正在检查\x01",
            "从柏斯到洛连特的人群中\x01",
            "有没有可疑的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A13")

    TalkEnd(0xB)
    Return()

    # Function_9_2281 end

    def Function_10_2A17(): pass

    label("Function_10_2A17")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2A91")

    ChrTalk(
        0xFE,
        (
            "定期船的运营\x01",
            "好像已经恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "能将犯人们逮捕归案\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D1")

    label("loc_2A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2B27")

    ChrTalk(
        0xFE,
        (
            "虽然定期船恢复运航，\x01",
            "但是关所的盘查仍在进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "希望能够\x01",
            "早些恢复原状啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D1")

    label("loc_2B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_2CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2C")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "西向航线的『赛希莉亚号』\x01",
            "好像再次开航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因如此，\x01",
            "经过这里的人又变少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "东向航线的『林德号』\x01",
            "什么时候再次开航呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CCE")

    label("loc_2C2C")


    ChrTalk(
        0xFE,
        (
            "西向航线的『赛希莉亚号』\x01",
            "好像再次开航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "正因如此，\x01",
            "经过这里的人又变少了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCE")

    Jump("loc_30D1")

    label("loc_2CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DFE")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "我们的队长和副长\x01",
            "都是参加过百日战役的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然两个人的性格不同，\x01",
            "但是都非常沉着冷静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是副长，\x01",
            "该说他是我行我素的人吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "见到什么都一副\x01",
            "非常感兴趣的样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA2")

    label("loc_2DFE")


    ChrTalk(
        0xFE,
        (
            "我们的队长和副长\x01",
            "都是参加过百日战役的士兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然两个人的性格不同，\x01",
            "但是都非常沉着冷静……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA2")

    Jump("loc_30D1")

    label("loc_2EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2F4A")

    ChrTalk(
        0xFE,
        (
            "如果飞艇失踪是帝国干的好事，\x01",
            "可能又要挑起战争了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "呼呼……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30D1")

    label("loc_2F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2FFE")

    ChrTalk(
        0xFE,
        (
            "采取这样的戒严状态，\x01",
            "还是百日战役以来的首次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样一说，\x01",
            "我就会觉得非常紧张。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D1")

    label("loc_2FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_30D1")

    ChrTalk(
        0xFE,
        (
            "从东柏斯街道\x01",
            "向北方延伸的钢壁之路\x01",
            "现在正处在封锁中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要去北部国境的话，\x01",
            "只能先去柏斯，\x01",
            "然后等待封锁解除。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D1")

    TalkEnd(0xC)
    Return()

    # Function_10_2A17 end

    def Function_11_30D5(): pass

    label("Function_11_30D5")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33CC")
    OP_A2(0x35F)
    OP_A2(0x4)

    ChrTalk(
        0x101,
        (
            "#000F（约修亚，\x01",
            "　这个人难道是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯，好像和我们一样\x01",
            "　都是游击士呢。\x02",
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
        "#000F你好？\x02",
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
            "#020F你还是那样讨人厌呢，\x01",
            "斯丁克。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(
        0xFE,
        (
            "你……\x01",
            "上次的实习游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F很漂亮的回答。\x02\x03",
            "托您的福，现在\x01",
            "我已经取得正游击士称号了。\x02",
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
        "#020F嗯，现在就在工作中。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近发生了很多事情，\x01",
            "柏斯的游击士都出动了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……那就靠你了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 0)

    ChrTalk(
        0x101,
        (
            "#000F（是雪拉姐的朋友。\x01",
            "　总觉得他有点可怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（但是那走路的动作……\x01",
            "　看来是个非常厉害的人物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BA")

    label("loc_33CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346A")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        "唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样仅今天\x01",
            "就打败了四头魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果库拉茨\x01",
            "从王都回来的话，\x01",
            "我们还能开心一些……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BA")

    label("loc_346A")


    ChrTalk(
        0xFE,
        (
            "如果库拉茨\x01",
            "从王都回来的话，\x01",
            "我们还能开心一些……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BA")

    TalkEnd(0xD)
    Return()

    # Function_11_30D5 end

    def Function_12_34BE(): pass

    label("Function_12_34BE")

    TalkBegin(0xE)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378F")
    OP_A2(0x360)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "#814F啊，难不成……\x01",
            "这不是雪拉扎德前辈吗？\x02\x03",
            "#850F很久不见了啊。\x01",
            "自从您去修行之后就再没见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F这不是亚妮拉丝吗。\x01",
            "你在这里做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F呵呵，协会委派我来这里\x01",
            "执行击退魔兽的任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是这样啊……辛苦了。\x02\x03",
            "对了，你已经找到\x01",
            "所谓的剑之道了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#819F呵呵，前辈您就别问了。\x01",
            "我还是处在修行阶段呢。\x02\x03",
            "#810F说起来，前辈您也是在\x01",
            "执行协会的任务吗？\x02",
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
            "这个地方\x01",
            "最近发生很多事呢。\x02\x03",
            "您路上一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38ED")

    label("loc_378F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3870")
    OP_A2(0x5)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        "#850F啊，雪拉扎德前辈！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F亚妮拉丝，来这里工作吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#810F是啊，虽然都不是大事，\x01",
            "但是最近这里\x01",
            "发生了不少各式各样的事情。\x02\x03",
            "#856F连休息的时间都没有～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38ED")

    label("loc_3870")


    ChrTalk(
        0xFE,
        (
            "#810F虽然都不是大事，\x01",
            "但是最近这里\x01",
            "发生了不少各式各样的事情。\x02\x03",
            "#856F连休息的时间都没有～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38ED")

    TalkEnd(0xE)
    Return()

    # Function_12_34BE end

    def Function_13_38F1(): pass

    label("Function_13_38F1")

    EventBegin(0x0)
    Return()

    # Function_13_38F1 end

    SaveToFile()

Try(main)
