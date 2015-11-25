from ED6ScenarioHelper import *

def main():
    # 洛连特礼拜堂

    CreateScenaFile(
        FileName            = 'T0130   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0130.x',
        MapIndex            = 3,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0130   ._SN',
            'ED6_DT01/T0130_1 ._SN',
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
        '迪拜恩教区长',                         # 9
        '修女梅',                               # 10
        '西加罗',                               # 11
        '艾德尔',                               # 12
        '米蕾奴夫人',                           # 13
        '安莉尔',                               # 14
        '安莉尔',                               # 15
        '穿制服的少女',                         # 16
        '潘杜爷爷',                             # 17
        '拉欧老人',                             # 18
        '克劳斯市长',                           # 19
        '玲达',                                 # 20
    )

    DeclEntryPoint(
        Unknown_00              = 59000,
        Unknown_04              = 0,
        Unknown_08              = 40000,
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
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 3,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 59000,
        Unknown_04              = 0,
        Unknown_08              = 40000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01043 ._CH',             # 02
        'ED6_DT07/CH01213 ._CH',             # 03
        'ED6_DT07/CH01180 ._CH',             # 04
        'ED6_DT07/CH01700 ._CH',             # 05
        'ED6_DT07/CH01700 ._CH',             # 06
        'ED6_DT07/CH02330 ._CH',             # 07
        'ED6_DT07/CH01250 ._CH',             # 08
        'ED6_DT07/CH01003 ._CH',             # 09
        'ED6_DT07/CH02350 ._CH',             # 0A
        'ED6_DT07/CH01350 ._CH',             # 0B
        'ED6_DT07/CH00014 ._CH',             # 0C
        'ED6_DT07/CH00015 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01043P._CP',             # 02
        'ED6_DT07/CH01213P._CP',             # 03
        'ED6_DT07/CH01180P._CP',             # 04
        'ED6_DT07/CH01700P._CP',             # 05
        'ED6_DT07/CH01700P._CP',             # 06
        'ED6_DT07/CH02330P._CP',             # 07
        'ED6_DT07/CH01250P._CP',             # 08
        'ED6_DT07/CH01003P._CP',             # 09
        'ED6_DT07/CH02350P._CP',             # 0A
        'ED6_DT07/CH01350P._CP',             # 0B
        'ED6_DT07/CH00014P._CP',             # 0C
        'ED6_DT07/CH00015P._CP',             # 0D
    )

    DeclNpc(
        X                   = 58800,
        Z                   = 1000,
        Y                   = 52200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -16832,
        Z                   = 0,
        Y                   = 42888,
        Direction           = 270,
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
        X                   = 56090,
        Z                   = 100,
        Y                   = 46000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55330,
        Z                   = 100,
        Y                   = 45940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 58997,
        Z                   = 1000,
        Y                   = 50050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58960,
        Z                   = 1000,
        Y                   = 49950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 59170,
        Z                   = 1000,
        Y                   = 50210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 61810,
        Z                   = 0,
        Y                   = 45970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 58997,
        Z                   = 1000,
        Y                   = 50050,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 59070,
        Z                   = 1000,
        Y                   = 50010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_302",          # 00, 0
        "Function_1_480",          # 01, 1
        "Function_2_4CA",          # 02, 2
        "Function_3_4E0",          # 03, 3
        "Function_4_4E5",          # 04, 4
        "Function_5_1AF6",         # 05, 5
        "Function_6_2331",         # 06, 6
        "Function_7_249D",         # 07, 7
        "Function_8_25F6",         # 08, 8
        "Function_9_2717",         # 09, 9
        "Function_10_275A",        # 0A, 10
        "Function_11_284C",        # 0B, 11
        "Function_12_2A1C",        # 0C, 12
        "Function_13_2BCE",        # 0D, 13
    )


    def Function_0_302(): pass

    label("Function_0_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_316")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_424")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_32A")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_424")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_36B")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_368")
    OP_8C(0x8, 270, 0)

    label("loc_368")

    Jump("loc_424")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3AC")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A9")
    OP_8C(0x8, 270, 0)

    label("loc_3A9")

    Jump("loc_424")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3D2")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_3CF")

    Jump("loc_424")

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3F5")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_424")

    label("loc_3F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_413")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8)
    Jump("loc_424")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_424")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    label("loc_424")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A")
    OP_28(0x9, 0x1, 0x10)
    Event(1, 6)

    label("loc_44A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F")
    OP_28(0x9, 0x1, 0x20)
    OP_28(0x9, 0x1, 0x40)
    Event(1, 7)

    label("loc_47F")

    Return()

    # Function_0_302 end

    def Function_1_480(): pass

    label("Function_1_480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_498")
    OP_B1("t0130_y")
    Jump("loc_4A1")

    label("loc_498")

    OP_B1("t0130_n")

    label("loc_4A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C9")
    OP_1B(0x1, 0x1, 0x9)

    label("loc_4C9")

    Return()

    # Function_1_480 end

    def Function_2_4CA(): pass

    label("Function_2_4CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4CA")

    label("loc_4DF")

    Return()

    # Function_2_4CA end

    def Function_3_4E0(): pass

    label("Function_3_4E0")

    Call(0, 4)
    Return()

    # Function_3_4E0 end

    def Function_4_4E5(): pass

    label("Function_4_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_69C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50F")
    Call(1, 1)
    Jump("loc_699")

    label("loc_50F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_683")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5A4")

    ChrTalk(
        0x8,
        (
            "为我采集来了药材……\x01",
            "真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "以后的旅程也一定要小心谨慎啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D")

    label("loc_5A4")


    ChrTalk(
        0x8,
        "那封信就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "教会在柏斯市的东侧，\x01",
            "进城后很容易就可以找到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "愿你们能\x01",
            "常受女神的保佑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D")

    TalkEnd(0x8)
    Jump("loc_699")

    label("loc_683")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_695")
    Call(1, 2)
    Jump("loc_699")

    label("loc_695")

    Call(1, 0)

    label("loc_699")

    Jump("loc_1AF5")

    label("loc_69C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72E")
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        "哦？怎么回事呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "好像有什么动物\x01",
            "跑进这里来了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1AF5")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_872")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75C")
    Call(1, 4)
    Jump("loc_86F")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7DD")
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚，\x01",
            "真是非常的感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在你们二人走过的蓝天之下，\x01",
            "空之女神会常伴左右。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_86F")

    label("loc_7DD")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "喔，\x01",
            "你们俩都变得有些成熟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "见到你们身心成长，\x01",
            "我也很高兴。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_86F")

    Jump("loc_1AF5")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_962")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89C")
    Call(1, 4)
    Jump("loc_95F")

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_91D")
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚，\x01",
            "真是非常的感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在你们二人走过的蓝天之下，\x01",
            "空之女神会常伴左右。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_95F")

    label("loc_91D")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "市长大人看来好像\x01",
            "碰上了什么开心事呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_95F")

    Jump("loc_1AF5")

    label("loc_962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_CA3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98C")
    Call(1, 4)
    Jump("loc_CA0")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A0D")
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚，\x01",
            "真是非常的感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在你们二人走过的蓝天之下，\x01",
            "空之女神会常伴左右。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_CA0")

    label("loc_A0D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE0")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "我已经在洛连特市\x01",
            "住了近３０年了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "１０年前看着\x01",
            "这个化作瓦砾的城镇， \x01",
            "我和市民们一样感到绝望。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但如今看着\x01",
            "这个百业俱兴的城市，\x01",
            "又不禁由衷感叹于人的坚强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "脆弱与坚强，\x01",
            "人同时拥有这两种相反特性的矛盾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是， \x01",
            "我却认为这样的人才真的可敬可爱。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_C9D")

    label("loc_BE0")


    ChrTalk(
        0x8,
        (
            "脆弱与坚强，\x01",
            "人同时拥有这两种相反特性的矛盾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是， \x01",
            "我却认为这样的人才真的可敬可爱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9D")

    TalkEnd(0x8)

    label("loc_CA0")

    Jump("loc_1AF5")

    label("loc_CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x386)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39F)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCD")
    Call(1, 4)
    Jump("loc_109F")

    label("loc_CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D4E")
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚，\x01",
            "真是非常的感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在你们二人走过的蓝天之下，\x01",
            "空之女神会常伴左右。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_109F")

    label("loc_D4E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD6")
    OP_A2(0x2B5)

    ChrTalk(
        0x8,
        (
            "光愈强，\x01",
            "则影愈暗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "当曝身于耀眼的光芒下时，\x01",
            "人类会意识到自己的丑恶，\x01",
            "并为此感到悔恨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "对往事耿耿于怀的人\x01",
            "更是如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是，也有人因此\x01",
            "而深知人世的伤痛与悲哀，\x01",
            "从而成为胸怀广阔的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "重要的是对未来要有充分的心理准备，\x01",
            "并明确自己要采取的行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯，真头疼……\x02\x03",
            "教区长还是老样子，\x01",
            "尽说些难懂的话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109C")

    label("loc_FD6")


    ChrTalk(
        0x8,
        (
            "当曝身于耀眼的光芒下时，\x01",
            "人类会意识到自己的丑恶，\x01",
            "并为此感到悔恨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "对往事耿耿于怀的人\x01",
            "更是如此。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109C")

    TalkEnd(0x8)

    label("loc_109F")

    Jump("loc_1AF5")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1388")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EC")
    OP_A2(0x2B4)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔、约修亚，\x01",
            "听说你们当上游击士了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "在满怀憧憬与期待的同时，\x01",
            "想必也充满了紧张与不安吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "唔……\x01",
            "看起来艾丝蒂尔\x01",
            "似乎还有其它的心事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x02\x03",
            "#501F没、没这回事啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "亲人不在身边\x01",
            "的确会让人心神难安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是，\x01",
            "人人都拥有着\x01",
            "克服这种逆境的坚强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请把这看作女神给予的考验，\x01",
            "好好加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……嗯。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1385")

    label("loc_12EC")


    ChrTalk(
        0x8,
        (
            "人人都拥有着\x01",
            "克服这种逆境的坚强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请把这看作女神给予的考验，\x01",
            "好好加油吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_1385")

    Jump("loc_1AF5")

    label("loc_1388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1537")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C6")
    OP_A2(0x2B3)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔……\x01",
            "你好像有什么烦恼呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#501F啊？没、没有啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "人是要伴随烦恼而成长的，\x01",
            "这是女神对人的考验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "女神啊，请引导苦恼的众生吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1534")

    label("loc_14C6")


    ChrTalk(
        0x8,
        (
            "无论将来会走上什么样的道路，\x01",
            "希望你们不要忘记你们两人\x01",
            "在一起走过的每时每刻。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_1534")

    Jump("loc_1AF5")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_17D3")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1715")
    OP_A2(0x2B2)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔，\x01",
            "你看起来非常开心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是不是有什么\x01",
            "高兴的事情啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#001F呵呵呵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F饶了我吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯， \x01",
            "开心虽然是件好事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但要记住，\x01",
            "事情进行得很顺利的时候尤其要提高警觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "空之女神啊，\x01",
            "请引导还未成熟的人们吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_17D0")

    label("loc_1715")


    ChrTalk(
        0x8,
        (
            "事情进行得很顺利的时候\x01",
            "尤其要提高警觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "空之女神啊，\x01",
            "请引导还未成熟的人们吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_17D0")

    Jump("loc_1AF5")

    label("loc_17D3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A75")
    OP_A2(0x2B1)

    ChrTalk(
        0x8,
        "哦，好久不见你们俩了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "你们这么早就来教会，\x01",
            "真是让我感动啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F教区长，早上好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔，你在上主日学校的时候\x01",
            "可是个迟到、逃学的惯犯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "毕业之后的生活态度\x01",
            "有没有改变一些呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#008F哈～哈哈，改了一些吧……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……离做弥撒\x01",
            "还有一些时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "难得你们专程赶来，\x01",
            "我就给你们来一堂特别讲义如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x02\x03",
            "#506F不、不用了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F（为什么连我也给牵连进来了……）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Jump("loc_1AF5")

    label("loc_1A75")


    ChrTalk(
        0x8,
        (
            "离做弥撒\x01",
            "还有一些时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "难得你们专程赶来，\x01",
            "我就给你们来一堂特别讲义如何？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_1AF5")

    Return()

    # Function_4_4E5 end

    def Function_5_1AF6(): pass

    label("Function_5_1AF6")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAE")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "之前上课的时候，\x01",
            "我教给了孩子们游击士协会的相关知识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特别是那个\x01",
            "叫鲁克的男孩子，\x01",
            "他可是非常认真听我讲课呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "游击士果然是\x01",
            "男孩子最为憧憬的职业啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE4")

    label("loc_1BAE")


    ChrTalk(
        0xFE,
        (
            "游击士果然是\x01",
            "男孩子最为憧憬的职业啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE4")

    Jump("loc_232D")

    label("loc_1BE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C7B")

    ChrTalk(
        0xFE,
        (
            "刚才我好像听到\x01",
            "楼梯上有一阵脚步声……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……难道是我的错觉？\x02",
    )

    CloseMessageWindow()
    Jump("loc_232D")

    label("loc_1C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1CFA")

    ChrTalk(
        0xFE,
        (
            "最近， \x01",
            "主日学校的孩子们\x01",
            "在没课的时候也会来找我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我觉得成为修女\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232D")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1DBB")

    ChrTalk(
        0xFE,
        (
            "主日学校的讲课\x01",
            "比想象的顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "多亏了教区长大人的意见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过鲁克\x01",
            "可真是个顽皮的孩子。\x01",
            "我可拿他没辙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232D")

    label("loc_1DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1E36")

    ChrTalk(
        0xFE,
        (
            "我被安排去\x01",
            "下一次主日学校讲课。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但愿孩子们\x01",
            "都能听话就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232D")

    label("loc_1E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2072")
    TurnDirection(0x9, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202A")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "你是艾丝蒂尔小姐吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我听教区长大人\x01",
            "说起过你很多事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎……\x01",
            "都、都是些什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵， \x01",
            "是你上主日学校时的种种事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F打瞌睡啊迟到啊\x01",
            "翘课啊恶作剧啊\x01",
            "她可是个大行家哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "教区长大人似乎挺喜欢\x01",
            "艾丝蒂尔小姐的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F是、是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_206F")

    label("loc_202A")


    ChrTalk(
        0xFE,
        (
            "教区长大人\x01",
            "似乎挺喜欢\x01",
            "艾丝蒂尔小姐的呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206F")

    Jump("loc_232D")

    label("loc_2072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_20E5")

    ChrTalk(
        0x9,
        "女神啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "非常感谢您赐予了我们\x01",
            "这一天的和平安宁。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232D")

    label("loc_20E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_22D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2225")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        "我是这里的新任修女。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是不久之前才从王都\x01",
            "派到洛连特来任职的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这里充满了自然的气息，\x01",
            "而且民风朴实， \x01",
            "真是一个休闲的好地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "迪拜恩教区长\x01",
            "虽然对我比较严厉，\x01",
            "但是他真的很让人值得尊敬。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D4")

    label("loc_2225")


    ChrTalk(
        0x9,
        (
            "我是不久之前才从王都\x01",
            "派到洛连特来任职的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这里充满了自然的气息，\x01",
            "而且民风朴实， \x01",
            "真是一个休闲的好地方呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D4")

    Jump("loc_232D")

    label("loc_22D7")


    ChrTalk(
        0x9,
        (
            "呀，\x01",
            "就要到做弥撒的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "市长夫人也要来参加，\x01",
            "我得马上去做准备才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232D")

    TalkEnd(0x9)
    Return()

    # Function_5_1AF6 end

    def Function_6_2331(): pass

    label("Function_6_2331")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2453")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C9")
    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "我们正在作巡礼之旅，\x01",
            "要走遍王国各地的礼拜堂。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "刚刚才坐定期船\x01",
            "到达洛连特。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2450")

    label("loc_23C9")


    ChrTalk(
        0xA,
        (
            "多亏有了定期船，\x01",
            "旅行也变得轻松愉快了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "工作也不用请太长的假，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2450")

    Jump("loc_2499")

    label("loc_2453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_247B")

    ChrTalk(
        0xA,
        "我真的本应不出现在这里。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2499")

    label("loc_247B")


    ChrTalk(
        0xA,
        "我真的本应不出现在这里。\x02",
    )

    CloseMessageWindow()

    label("loc_2499")

    TalkEnd(0xA)
    Return()

    # Function_6_2331 end

    def Function_7_249D(): pass

    label("Function_7_249D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_25AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2558")
    OP_A2(0x4)

    ChrTalk(
        0xB,
        (
            "呵呵， \x01",
            "我是为了旅游和购物\x01",
            "才跟着老公来这儿的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "洛连特这城市\x01",
            "不单空气清新自然，\x01",
            "而且气氛也很宁静祥和。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A9")

    label("loc_2558")


    ChrTalk(
        0xB,
        (
            "洛连特这城市\x01",
            "不单空气清新自然，\x01",
            "而且气氛也很宁静祥和。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A9")

    Jump("loc_25F2")

    label("loc_25AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_25D4")

    ChrTalk(
        0xB,
        "我真的本应不出现在这里。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25F2")

    label("loc_25D4")


    ChrTalk(
        0xB,
        "我真的本应不出现在这里。\x02",
    )

    CloseMessageWindow()

    label("loc_25F2")

    TalkEnd(0xB)
    Return()

    # Function_7_249D end

    def Function_8_25F6(): pass

    label("Function_8_25F6")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C6")
    OP_A2(0x5)

    ChrTalk(
        0x101,
        (
            "#000F米蕾奴婶婶，早上好。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "呀，是艾丝蒂尔和约修亚啊，\x01",
            "早上好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "你们一大早就出门了？\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2713")

    label("loc_26C6")


    ChrTalk(
        0xC,
        (
            "你们一大早就出门了？\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2713")

    TalkEnd(0xC)
    Return()

    # Function_8_25F6 end

    def Function_9_2717(): pass

    label("Function_9_2717")

    TalkBegin(0xF)

    ChrTalk(
        0xF,
        (
            "原来如此…………\x02\x03",
            "高论，的确是高论啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_9_2717 end

    def Function_10_275A(): pass

    label("Function_10_275A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D2")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "一天又过去了， \x01",
            "和平的日子实在是比什么都好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "战争什么的……\x01",
            "千万不要再发生了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2848")

    label("loc_27D2")


    ChrTalk(
        0xFE,
        (
            "战争什么的……\x01",
            "千万不要再发生了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一想起十年前的那次战争\x01",
            "我就忍不住颤抖。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2848")

    TalkEnd(0x10)
    Return()

    # Function_10_275A end

    def Function_11_284C(): pass

    label("Function_11_284C")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28CD")

    ChrTalk(
        0xFE,
        "怎么这么吵啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "这里可是神圣的祈祷场所啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A18")

    label("loc_28CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298F")
    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "前几天，\x01",
            "我悄悄去森林里看了看女婿的工作情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "原来他也在以\x01",
            "自己的方式努力工作着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "总觉得似乎还是缺点什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A18")

    label("loc_298F")


    ChrTalk(
        0xFE,
        (
            "女婿的辛劳我承认，\x01",
            "但总觉得他还是缺点什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A18")

    TalkEnd(0x11)
    Return()

    # Function_11_284C end

    def Function_12_2A1C(): pass

    label("Function_12_2A1C")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AD2")

    ChrTalk(
        0xFE,
        (
            "#600F喔，是艾丝蒂尔和约修亚啊。\x01",
            "七耀石的事真是麻烦你们了。\x02\x03",
            "看你们这么慌乱，\x01",
            "到底发生了什么事情呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BCA")

    label("loc_2AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7D")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "#601F喔，是艾丝蒂尔和约修亚啊。\x01",
            "七耀石的事真是麻烦你们了。\x02\x03",
            "今天我来这里找教区长有点事。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BCA")

    label("loc_2B7D")


    ChrTalk(
        0xFE,
        (
            "#601F今天我来这里找教区长有点事。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BCA")

    TalkEnd(0x12)
    Return()

    # Function_12_2A1C end

    def Function_13_2BCE(): pass

    label("Function_13_2BCE")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        (
            "女神啊……\x01",
            "请保佑老爷和夫人永远健康……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_13_2BCE end

    SaveToFile()

Try(main)
