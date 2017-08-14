from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4221   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '玛多克工房长',                         # 9
        '理查德上校',                           # 10
        '杜南公爵',                             # 11
        '管家菲利普',                           # 12
        '雪拉',                                 # 13
        '雷沃尔',                               # 14
        '妮舒',                                 # 15
        '提妲',                                 # 16
        '拉赛尔',                               # 17
        '奥利维尔',                             # 18
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
        'ED6_DT07/CH02620 ._CH',             # 00
        'ED6_DT07/CH02030 ._CH',             # 01
        'ED6_DT07/CH02460 ._CH',             # 02
        'ED6_DT07/CH02230 ._CH',             # 03
        'ED6_DT07/CH02240 ._CH',             # 04
        'ED6_DT07/CH02140 ._CH',             # 05
        'ED6_DT07/CH02470 ._CH',             # 06
        'ED6_DT07/CH00020 ._CH',             # 07
        'ED6_DT07/CH01270 ._CH',             # 08
        'ED6_DT07/CH01350 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH00060 ._CH',             # 0B
        'ED6_DT07/CH02020 ._CH',             # 0C
        'ED6_DT07/CH00030 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02620P._CP',             # 00
        'ED6_DT07/CH02030P._CP',             # 01
        'ED6_DT07/CH02460P._CP',             # 02
        'ED6_DT07/CH02230P._CP',             # 03
        'ED6_DT07/CH02240P._CP',             # 04
        'ED6_DT07/CH02140P._CP',             # 05
        'ED6_DT07/CH02470P._CP',             # 06
        'ED6_DT07/CH00020P._CP',             # 07
        'ED6_DT07/CH01270P._CP',             # 08
        'ED6_DT07/CH01350P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH00060P._CP',             # 0B
        'ED6_DT07/CH02020P._CP',             # 0C
        'ED6_DT07/CH00030P._CP',             # 0D
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
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 141250,
        Z                   = 0,
        Y                   = 7610,
        Direction           = 278,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 78740,
        Z                   = 0,
        Y                   = -1880,
        Direction           = 194,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 83500,
        Z                   = 0,
        Y                   = -53540,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 86170,
        Z                   = 0,
        Y                   = -52670,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 139300,
        Z                   = 0,
        Y                   = 5970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 139320,
        TriggerZ            = 0,
        TriggerY            = 7540,
        TriggerRange        = 400,
        ActorX              = 141250,
        ActorZ              = 1500,
        ActorY              = 7610,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27E",          # 00, 0
        "Function_1_3F3",          # 01, 1
        "Function_2_454",          # 02, 2
        "Function_3_5D1",          # 03, 3
        "Function_4_11F5",         # 04, 4
        "Function_5_13EB",         # 05, 5
        "Function_6_14FC",         # 06, 6
        "Function_7_15ED",         # 07, 7
        "Function_8_1664",         # 08, 8
        "Function_9_1669",         # 09, 9
        "Function_10_18BA",        # 0A, 10
        "Function_11_223F",        # 0B, 11
        "Function_12_361C",        # 0C, 12
        "Function_13_366D",        # 0D, 13
        "Function_14_4B70",        # 0E, 14
        "Function_15_5768",        # 0F, 15
        "Function_16_58C4",        # 10, 16
        "Function_17_592F",        # 11, 17
    )


    def Function_0_27E(): pass

    label("Function_0_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_28C")
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_29A")
    OP_A3(0x3FB)
    Event(0, 14)

    label("loc_29A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_2AA"),
        (108, "loc_2C0"),
        (SWITCH_DEFAULT, "loc_2D6"),
    )


    label("loc_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BD")
    OP_A2(0x646)
    Event(0, 13)

    label("loc_2BD")

    Jump("loc_2D6")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D3")
    OP_A2(0x670)
    Event(0, 15)

    label("loc_2D3")

    Jump("loc_2D6")

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F8")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 38180, 0, -59720, 90)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322")
    SetChrChipByIndex(0x0, 2)
    SetChrChipByIndex(0x1, 3)
    SetChrChipByIndex(0x138, 4)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_34C")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 37930, 0, 59370, 97)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_3F2")

    label("loc_34C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_36B")
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x55, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368")
    ClearChrFlags(0x11, 0x80)

    label("loc_368")

    Jump("loc_3F2")

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_390")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)
    Jump("loc_3F2")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_3B5")
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)
    Jump("loc_3F2")

    label("loc_3B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_3D5")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)
    Jump("loc_3F2")

    label("loc_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_3F2")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 37840, 0, -58890, 90)

    label("loc_3F2")

    Return()

    # Function_0_27E end

    def Function_1_3F3(): pass

    label("Function_1_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409")
    OP_1B(0x0, 0x0, 0x10)
    OP_1B(0x6, 0x0, 0x11)

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_413")
    Jump("loc_44A")

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_41D")
    Jump("loc_44A")

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_42B")
    OP_64(0x0, 0x1)
    Jump("loc_44A")

    label("loc_42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_439")
    OP_64(0x0, 0x1)
    Jump("loc_44A")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_443")
    Jump("loc_44A")

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_44A")

    label("loc_44A")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_3F3 end

    def Function_2_454(): pass

    label("Function_2_454")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_479")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5BB")

    label("loc_479")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_492")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5BB")

    label("loc_492")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5BB")

    label("loc_4AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5BB")

    label("loc_4C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5BB")

    label("loc_4DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5BB")

    label("loc_4F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5BB")

    label("loc_50F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_528")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5BB")

    label("loc_528")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_541")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5BB")

    label("loc_541")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5BB")

    label("loc_55A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_573")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5BB")

    label("loc_573")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5BB")

    label("loc_58C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A5")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5BB")

    label("loc_5A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5BB")

    label("loc_5D0")

    Return()

    # Function_2_454 end

    def Function_3_5D1(): pass

    label("Function_3_5D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x55, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_994")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 137920, 0, 6450, 90)
    SetChrPos(0x102, 137940, 0, 5220, 90)
    OP_8C(0x11, 270, 0)
    SetChrSubChip(0x11, 0)
    OP_6D(138940, 0, 6080, 1000)

    ChrTalk(
        0x11,
        (
            "#030F哟，艾丝蒂尔君、约修亚君。\x02\x03",
            "好不容易迎来了诞辰庆典，\x01",
            "不到市区里面尽情玩乐，\x01",
            "是不是有点可惜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F（我说约修亚啊……\x01",
            "　公告板上委托寻找的对象……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F（毫无疑问就是此人……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#033F呵，难道说你们俩……\x02\x03",
            "想要邀请我\x01",
            "一起享受午后的风花岁月吗？\x02\x03",
            "#032F这样三个人一起……\x01",
            "……也许会更加刺激……\x02\x03",
            "#031F不错嘛，\x01",
            "我就欣然接受吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(
        0x101,
        (
            "#001F哎呀，真巧啊。\x02\x03",
            "有一个热情胜过我们百倍千倍的人\x01",
            "正在等着奥利维尔你哦～\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#033F#5S什、什么……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#032F这、这、这是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F嗯，如果可以的话，\x01",
            "让我们带你去那个人的地方怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#030F呵，既然这样……\x02\x03",
            "#031F请你们立刻就带我去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_11F1")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECB")
    OP_A2(0x6ED)

    ChrTalk(
        0x101,
        "#004F咦，是奥利维尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#030F哟，艾丝蒂尔君、约修亚君。\x02\x03",
            "我从卡西乌斯先生那里听说了，\x01",
            "你们终于成为了正游击士对吧？\x02\x03",
            "#031F呵呵，恭喜恭喜，\x01",
            "不愧是我的小猫咪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不管你是什么态度……\x01",
            "还是要多谢你一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，奥利维尔，\x01",
            "你怎么会在这里呢？\x02\x03",
            "虽然听说你和我们一样，\x01",
            "也被邀请参加今天的晚宴……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#580F对、对啊……\x02\x03",
            "一个比任何人都喜欢庆典的男人，\x01",
            "居然一个人在这种安静的地方喝酒……\x02\x03",
            "#005F难道说你是个冒牌货！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#035F呵呵，\x01",
            "我会让你们在协会获得正游击士资格时\x01",
            "那种愉快的心情得以尽情展现的。\x02\x03",
            "对了，我要在格兰竞技场前\x01",
            "开一个即兴的音乐会。\x02\x03",
            "我的狂热支持者\x01",
            "肯定会让你们满意的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F说谎～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#018F让我想起在哈肯大门\x01",
            "听到你的演奏时的事情了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#030F算了，我就远离诞辰庆典的热闹，\x01",
            "一个人静静地喝点小酒吧。\x02\x03",
            "#035F我那充满孤独和忧郁的背影，\x01",
            "真是一种残酷的美啊……\x02\x03",
            "这就是所谓男人的美学。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F还是不知道你到这里的原因……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F1")

    label("loc_ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110F")
    OP_A2(0x6F6)

    ChrTalk(
        0x101,
        (
            "#501F啊，对了……\x01",
            "老爸赶来的时候……\x02\x03",
            "奥利维尔，\x01",
            "当时你和老爸说的那些话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#033F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F确实……\x02\x03",
            "你们应该从来没有见过面，\x01",
            "但是看起来父亲他\x01",
            "像是知道你的事情一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#036F………………………………\x02\x03",
            "#031F哈·哈·哈。\x01",
            "你们～在说什～么啊？\x02\x03",
            "我们～那时候～可没有～\x01",
            "说什么～重～要的～事情啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F（更觉得可疑了……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F（嗯……\x01",
            "　肯定是有什么事情瞒着我们。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F1")

    label("loc_110F")


    ChrTalk(
        0x11,
        (
            "#035F呵呵，年轻的人们，\x01",
            "尽情享受庆典的火热吧。\x02\x03",
            "我是悠远森林中的隐者，\x01",
            "驰骋于过去和未来的奇想。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F1")

    TalkEnd(0xFE)
    Return()

    # Function_3_5D1 end

    def Function_4_11F5(): pass

    label("Function_4_11F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_12A1")

    ChrTalk(
        0x10B,
        (
            "#100F七至宝之一的『辉之环』……\x02\x03",
            "连陛下也不知道\x01",
            "遗迹到底在什么地方，\x01",
            "上校又是听谁说的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E7")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1305")

    ChrTalk(
        0x10B,
        (
            "#100F虽然理查德上校的政变风波暂时平息了，\x01",
            "但是还留下不少谜团。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E7")

    label("loc_1305")

    OP_A2(0x5)

    ChrTalk(
        0x10B,
        (
            "#100F虽然理查德上校的政变风波暂时平息了，\x01",
            "但是还留下不少谜团。\x01",
            "　\x02\x03",
            "王城的地下竟然有古代导力文明的遗迹……\x01",
            "　\x02\x03",
            "今后要重新对其进行全面的调查才行。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E7")

    TalkEnd(0xFE)
    Return()

    # Function_4_11F5 end

    def Function_5_13EB(): pass

    label("Function_5_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_1475")

    ChrTalk(
        0x107,
        (
            "#060F爷爷，\x01",
            "从刚才开始你好像就一直在沉思。\x02\x03",
            "嗯～\x01",
            "我们什么时候回蔡斯去啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FB")

    label("loc_1475")


    ChrTalk(
        0x107,
        (
            "#060F王城里的饭菜真好吃啊～\x01",
            "　\x02\x03",
            "真是太令人惊讶了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FB")

    Return()

    # Function_5_13EB end

    def Function_6_14FC(): pass

    label("Function_6_14FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_159A")

    ChrTalk(
        0xC,
        (
            "#020F啊？\x01",
            "约修亚不在房间里吗？\x02\x03",
            "他肯定会在城里的，\x01",
            "你去找找他吧。\x02\x03",
            "艾丝蒂尔，加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E9")

    label("loc_159A")


    ChrTalk(
        0xC,
        (
            "#020F约修亚和老师的房间\x01",
            "应该就在隔壁吧。\x02\x03",
            "艾丝蒂尔，加油哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E9")

    TalkEnd(0xFE)
    Return()

    # Function_6_14FC end

    def Function_7_15ED(): pass

    label("Function_7_15ED")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "这边是拉赛尔博士和\x01",
            "提妲小姐的房间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们二人\x01",
            "现在好像外出了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_15ED end

    def Function_8_1664(): pass

    label("Function_8_1664")

    Call(0, 9)
    Return()

    # Function_8_1664 end

    def Function_9_1669(): pass

    label("Function_9_1669")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_168E")

    ChrTalk(
        0xD,
        "哟，今天怎么只有你一个人呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_168E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_17A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16F2")

    ChrTalk(
        0xD,
        "那位理查德上校竟然是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "我至今还认为\x01",
            "他不应该是那种\x01",
            "会反叛女王陛下的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179D")

    label("loc_16F2")

    OP_A2(0x0)

    ChrTalk(
        0xD,
        (
            "理查德上校\x01",
            "每晚都会到这里来\x01",
            "向我打听一些事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "至今我还是觉得他不应该是\x01",
            "会反叛女王陛下的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179D")

    Jump("loc_18B6")

    label("loc_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_17AA")
    Jump("loc_18B6")

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_17B4")
    Jump("loc_18B6")

    label("loc_17B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1824")

    ChrTalk(
        0xD,
        (
            "作为饭后的消遣，\x01",
            "来一杯饮料如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "就算菜单上没有的种类\x01",
            "也可以立刻调配出来的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_18B6")

    ChrTalk(
        0xD,
        (
            "这里是谈话室。\x01",
            "请在这里放松一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "如果客人\x01",
            "需要酒水的话，\x01",
            "请尽管吩咐我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B6")

    TalkEnd(0xD)
    Return()

    # Function_9_1669 end

    def Function_10_18BA(): pass

    label("Function_10_18BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E13")
    OP_A2(0x63C)
    EventBegin(0x0)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 38180, 0, -57660, 171)
    SetChrPos(0x102, 36300, 0, -58410, 135)
    OP_6D(37860, 0, -58600, 1000)

    ChrTalk(
        0x8,
        (
            "#800F哦哦……\x01",
            "艾丝蒂尔、约修亚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F工房长先生！\x01",
            "您果然也被邀请了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F因为邀请的都是市长级别的人物，\x01",
            "所以觉得工房长肯定也会来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F你们才是，\x01",
            "真没想到能得到武术大会冠军\x01",
            "被邀请来格兰赛尔城呢。\x02\x03",
            "呀哈……\x01",
            "不愧是卡西乌斯的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嘿嘿……\x01",
            "因为得到了很多人的帮助嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F对了，最近这些天\x01",
            "有什么动静吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F嗯……\x01",
            "你们刚出发去王都，\x01",
            "情报部的凯诺娜上尉就来了。\x02\x03",
            "虽然没办法拒绝出席晚宴，\x01",
            "不过关于你们潜入要塞的事，\x01",
            "不管怎么说还是瞒过去了。\x02\x03",
            "逃走的拉赛尔博士他们，\x01",
            "好像也没有被军队发现。\x02\x03",
            "不过，这种情况再持续下去，\x01",
            "被抓住也只是时间上的问题了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F刚才，我向凯诺娜上尉提出\x01",
            "要探望女王陛下的要求，\x01",
            "很轻易就被拒绝了……\x02\x03",
            "果然还是很难直接见面吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F好像是呢……\x01",
            "不过别担心，已经有办法了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不管怎么说，\x01",
            "一定要把博士的传言带给女王陛下。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_223E")

    label("loc_1E13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_1F34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_1E91")

    ChrTalk(
        0x8,
        (
            "#800F街上还是那么热闹啊。\x01",
            "　\x02\x03",
            "难得来一趟王都。\x01",
            "回去之前就去酒馆里\x01",
            "放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F31")

    label("loc_1E91")


    ChrTalk(
        0x8,
        (
            "#800F我和拉赛尔博士\x01",
            "这么长时间不在中央工房，\x01",
            "真是担心那边的情况啊。\x02\x03",
            "我打算明天就乘『林德号』\x01",
            "返回蔡斯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F31")

    Jump("loc_223B")

    label("loc_1F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1F3E")
    Jump("loc_223B")

    label("loc_1F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_1F48")
    Jump("loc_223B")

    label("loc_1F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_2182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1FBD")

    ChrTalk(
        0x8,
        (
            "#800F听说陛下的病情有了好转，\x01",
            "让人松了一口气啊。\x02\x03",
            "只要知道这件事，\x01",
            "来王都这一趟就值得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217F")

    label("loc_1FBD")

    OP_A2(0x2)

    ChrTalk(
        0x8,
        (
            "#800F希尔丹夫人，好久不见了。\x01",
            "看到您这么有精神，真是太好了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F玛多克工房长也没变呢。\x02\x03",
            "还是老样子，\x01",
            "总是闲不下来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#800F哈～哈，话说回来，\x01",
            "中央工房优秀的新人辈出，\x01",
            "让人甚感欣慰啊。\x02\x03",
            "而且听说陛下的病情有了好转，\x01",
            "让人松了一口气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F……嗯，我想再过不久\x01",
            "就可以和陛下见面了吧。\x02\x03",
            "玛多克工房长，\x01",
            "如果您有什么需要的话，\x01",
            "请别客气，尽量提出来。\x02\x03",
            "我们会马上为您准备好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#800F哦，让您费心了。\x02",
    )

    CloseMessageWindow()

    label("loc_217F")

    Jump("loc_223B")

    label("loc_2182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_21CB")

    ChrTalk(
        0x8,
        (
            "#800F哦，艾丝蒂尔和约修亚。\x02\x03",
            "怎么样，和女王陛下\x01",
            "见到面了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_223B")

    label("loc_21CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_223B")

    ChrTalk(
        0x8,
        (
            "#800F情报部的那些人\x01",
            "非常地狡猾。\x02\x03",
            "你们两个务必要\x01",
            "谨慎小心地行动哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223B")

    TalkEnd(0xFE)

    label("loc_223E")

    Return()

    # Function_10_18BA end

    def Function_11_223F(): pass

    label("Function_11_223F")

    EventBegin(0x0)
    OP_6D(142500, 4850, 7580, 0)
    OP_67(0, 4770, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(343, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 143590, 4000, 7800, 270)
    SetChrPos(0x101, 141480, 4000, 7160, 90)
    SetChrPos(0x102, 141270, 4000, 8340, 90)

    ChrTalk(
        0x9,
        (
            "#110F……第一次见到卡西乌斯上校时\x01",
            "我还刚从士官学校毕业。\x02\x03",
            "当时就分配到他率领的\x01",
            "独立机动部队去了……\x02\x03",
            "从那以后，直到他辞去军衔，\x01",
            "我都在工作和生活方面受他照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呵、呵－呵……\x01",
            "是这样啊……\x02\x03",
            "嗯，当时的父亲留给\x01",
            "上校您什么样的印象呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#110F一句话，就是『英雄』。\x02\x03",
            "称为『剑圣』也毫不为过的精湛技艺。\x02\x03",
            "任何战况都可以灵活应对，\x01",
            "立体的全方位指挥能力……\x02\x03",
            "而且不仅仅是拥有各种战术，\x01",
            "还有高超的战略能力来指挥部队……\x02\x03",
            "不管哪一项都无人能及。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F总、总感觉听起来\x01",
            "好像不是他本人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F父亲辞退军衔和那个\x01",
            "『百日战役』是同时的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#110F嗯……\x01",
            "我当时在卡西乌斯上校的麾下战斗。\x02\x03",
            "到现在我都还记得很清楚……\x01",
            "他所部署的奇迹般的作战\x01",
            "开始时所带来的热情与兴奋……\x02\x03",
            "一说起那个时候的事情，\x01",
            "再有多少时间都不够，\x01",
            "以后有机会我会和你们慢慢道来的……\x02\x03",
            "但仅凭这些就可以断定了。\x02\x03",
            "如果那时没有一位叫做卡西乌斯·布莱特\x01",
            "的男人，这个利贝尔就已经被\x01",
            "埃雷波尼亚给吸收吞并了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不、不会吧！？\x02\x03",
            "的确有些\x01",
            "难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#110F呵呵，能将难以置信之事\x01",
            "化为可能的就是『英雄』。\x02\x03",
            "而且在战争之后很快就退役了，\x01",
            "拒绝了女王陛下授予的勋章，\x01",
            "不让世人知道其威名……\x02\x03",
            "至今为止，在一部分军人之中\x01",
            "还把卡西乌斯上校的名字作为英雄的代名词。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔－……\x02\x03",
            "那个小气的老爸，这样的事情\x01",
            "竟然一个字也没有给我提起过！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果特地和女儿说这番话，\x01",
            "也不见得她能听得进去啊。\x02\x03",
            "若是责备父亲的话，他也太可怜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F可、可怜的是我们啊！\x02\x03",
            "……说起来，约修亚你\x01",
            "似乎不是很吃惊啊。\x02\x03",
            "难道……\x01",
            "刚才那些话你是都知道的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F理查德上校是\x01",
            "父亲的部下这一点\x01",
            "的确是不知道的……\x02\x03",
            "不过……其他的我是明白的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F什、什么～！？\x02\x03",
            "这么说约修亚就是共犯了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F冷、冷静一点，艾丝蒂尔。\x02\x03",
            "我是从别的地方得知的，父亲\x01",
            "并没有告诉过我。\x02\x03",
            "而且父亲也不需要特地\x01",
            "的来告诉你这些事情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔～不太令人信服哦～……\x02\x03",
            "可真是的，回去之后\x01",
            "一定要好好教训他一顿！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#110F呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非、非常抱歉。\x01",
            "中途打断了您说话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#110F哪里……\x01",
            "看见你们这样我也稍感安心了。\x02\x03",
            "卡西乌斯先生要辞去军衔时，\x01",
            "我拼命的想挽留住他……\x02\x03",
            "不过那样的选择\x01",
            "对于他来说也许是最合适的。\x02\x03",
            "有你们在他身旁陪伴，\x01",
            "失去夫人的悲痛\x01",
            "一定会逐渐化解掉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F理查德上校……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F…………………………\x02",
    )

    CloseMessageWindow()

    def lambda_2DBF():

        label("loc_2DBF")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2DBF")

    QueueWorkItem2(0x101, 1, lambda_2DBF)

    def lambda_2DD0():

        label("loc_2DD0")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_2DD0")

    QueueWorkItem2(0x102, 1, lambda_2DD0)
    OP_8F(0x9, 0x231B8, 0xFA0, 0x1824, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        (
            "#110F那么……\x01",
            "多谢你们能陪我说会儿话。\x02\x03",
            "因为公爵大人\x01",
            "还在等着的，\x01",
            "我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F抱歉，我们完全是\x01",
            "在听您怎么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#110F不，你们让我得知了\x01",
            "我最想知道的。\x02\x03",
            "……这样一来我就没有什么可以留恋的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这究竟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#110F哈哈，最近一段时间\x01",
            "我们还会有机会见面的。\x02\x03",
            "那时就可以和卡西乌斯上校\x01",
            "以及你们一起聊聊了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_43(0x9, 0x1, 0x0, 0xC)

    def lambda_301E():
        OP_6D(143890, 2750, 1780, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_301E)

    def lambda_3036():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3036)
    Sleep(5000)
    OP_63(0x101)
    OP_63(0x102)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_6D(142230, 4850, 7220, 2000)

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x02\x03",
            "刚才那个人\x01",
            "真的是理查德上校吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我说……\x01",
            "你睡迷糊了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F可、可是他如此钦佩的\x01",
            "说着老爸过去的事情……\x02\x03",
            "不过……\x01",
            "和以往留下的印象不同啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……的确。\x01",
            "并不像是一个坏人。\x02\x03",
            "可是，抛开这个不提，\x01",
            "他肯定是有什么企图的。\x02\x03",
            "否则怎么会对父亲的事情\x01",
            "了解的那么清楚明白。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "话是这么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F丑话先说在前面……\x02\x03",
            "把我们这么亲切的找来\x01",
            "也许是有什么目的。\x02\x03",
            "像他那样的情报专家，\x01",
            "要想欺骗我们这样的小孩，\x01",
            "简直是易如反掌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你、你确信刚才你说\x01",
            "的那些没有言过其实吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……确信。\x02\x03",
            "防人之心不可无。\x02\x03",
            "你只要相信你自己\x01",
            "的直觉就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F要做好各种准备，\x01",
            "不可掉以轻心。\x02\x03",
            "游击士所要做到的……\x01",
            "我认为就是这样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F约修亚……\x02\x03",
            "嗯，我明白了。\x02\x03",
            "虽然没有什么自信，不过\x01",
            "我会牢记在心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……谢谢你，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F什么～啊。\x01",
            "约修亚你怎么和我讲起礼来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F接下来我们要立刻\x01",
            "赶到希尔丹夫人那里去。\x02\x03",
            "大概已经等的不耐烦了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是呀……\x01",
            "这就前去女佣休息室吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    SetChrPos(0x101, 142340, 4000, 5440, 169)
    SetChrPos(0x102, 142340, 4000, 5440, 169)
    SetChrFlags(0x9, 0x80)
    EventEnd(0x0)
    Return()

    # Function_11_223F end

    def Function_12_361C(): pass

    label("Function_12_361C")

    OP_8E(0xFE, 0x24298, 0xFA0, 0x146E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x241D0, 0x7D0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8E(0xFE, 0x22632, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_8E(0xFE, 0x20666, 0x0, 0x320, 0xBB8, 0x0)
    Return()

    # Function_12_361C end

    def Function_13_366D(): pass

    label("Function_13_366D")

    EventBegin(0x0)
    OP_6D(88610, 0, 6390, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x138, 2)
    SetChrPos(0x138, 87950, 0, 4590, 0)
    SetChrPos(0x101, 87640, 0, 6230, 90)
    SetChrPos(0x102, 89210, 0, 6370, 270)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "呼……\x01",
            "约修亚你可真受欢迎啊。\x02\x03",
            "那个家伙一听到约修亚的名字，\x01",
            "顿时就两眼放光呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哪、哪有那样的事。\x02\x03",
            "倒是你呀，\x01",
            "不还顶撞了他吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我那个时候面对那个家伙\x01",
            "一点紧张感都没有。\x02\x03",
            "呼，不管怎么说还是\x01",
            "有些不够自信啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F我说……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 93780, 0, 850, 90)
    SetChrPos(0xB, 93780, 0, 850, 90)

    ChrTalk(
        0xA,
        (
            "嗝……\x01",
            "什么东西吵吵嚷嚷的……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)

    def lambda_3863():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3863)

    def lambda_3871():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3871)

    def lambda_387F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_387F)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x138, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(90380, 0, 5100, 1000)

    def lambda_38E3():

        label("loc_38E3")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_38E3")

    QueueWorkItem2(0x101, 1, lambda_38E3)

    def lambda_38F4():

        label("loc_38F4")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_38F4")

    QueueWorkItem2(0x102, 1, lambda_38F4)

    def lambda_3905():

        label("loc_3905")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_3905")

    QueueWorkItem2(0x138, 1, lambda_3905)

    def lambda_3916():
        OP_6D(89070, 0, 5570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3916)

    def lambda_392E():
        OP_8E(0xFE, 0x1630A, 0x0, 0x636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_392E)
    WaitChrThread(0xA, 0x1)
    ClearChrFlags(0xB, 0x80)

    def lambda_3953():
        OP_8E(0xFE, 0x15D06, 0x0, 0x1158, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3953)

    def lambda_396E():
        OP_8E(0xFE, 0x1630A, 0x0, 0x636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_396E)
    WaitChrThread(0xB, 0x1)

    def lambda_398E():
        OP_8E(0xFE, 0x15EA0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_398E)
    WaitChrThread(0xA, 0x1)

    def lambda_39AE():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_39AE)

    ChrTalk(
        0x138,
        "#710F公爵大人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#220F我说什么呢，这不是女管家吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x101, 400)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#220F哦哟……\x01",
            "怎么，那两个侍女是……\x02\x03",
            "嗝……\x01",
            "以前没有见过的生面孔啊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_3AE2")

    ChrTalk(
        0x138,
        (
            "#710F新来的实习侍女，\x01",
            "莱娜和卡玲。\x02\x03",
            "因为对城里还不熟悉，\x01",
            "所以带领她们到处走走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_3AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_3B5D")

    ChrTalk(
        0x138,
        (
            "#710F新来的实习侍女，\x01",
            "雪拉和卡玲。\x02\x03",
            "因为对城里还不熟悉，\x01",
            "所以带领她们到处走走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_3B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_3BD7")

    ChrTalk(
        0x138,
        (
            "#710F新来的实习侍女，\x01",
            "朵洛希和卡玲。\x02\x03",
            "因为对城里还不熟悉，\x01",
            "所以带领她们到处走走。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD7")


    ChrTalk(
        0xB,
        "#720F哦哟……？\x02",
    )

    CloseMessageWindow()
    OP_8E(0xB, 0x16044, 0x0, 0x10AE, 0x7D0, 0x0)
    OP_8E(0xB, 0x15F40, 0x0, 0x14BE, 0x7D0, 0x0)
    TurnDirection(0xB, 0x102, 400)
    Sleep(500)
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(
        0xB,
        "#720F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（啊……注意到了？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（……糟糕了。）\x02\x03",
            "（和这个人见过几次面，\x01",
            "被注意到也不奇怪……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F怎么了，菲利普。\x01",
            "目不转睛的盯着看……\x02\x03",
            "哇哈哈，对于你这样正经古板的人\x01",
            "来说，这真是稀罕得很啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#720F失礼了……\x02\x03",
            "因为和我的侄女比较相似，\x01",
            "所以一下就呆住了。\x02\x03",
            "两位姑娘，\x01",
            "我非常的抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，没关系。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请不要介意……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F呵，仔细一看不管哪一个\x01",
            "都是精选的上等货色啊……\x02\x03",
            "尤其是棕色头发那位，\x01",
            "极为阳光啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（喂喂……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F黑色头发的那位再稍微\x01",
            "把腰挺直一些就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……惶、惶恐之至。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#220F呼，那么……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_3F3A")

    ChrTalk(
        0xA,
        (
            "#220F莱娜！\x01",
            "我命令你今晚来伺候我！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB1")

    label("loc_3F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_3F76")

    ChrTalk(
        0xA,
        (
            "#220F雪拉！\x01",
            "我命令你今晚来伺候我！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB1")

    label("loc_3F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_3FB1")

    ChrTalk(
        0xA,
        (
            "#220F朵洛希！\x01",
            "我命令你今晚来伺候我！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB1")


    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xB,
        "#720F公、公爵大人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（咦，什么叫伺候呢？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（唔，怎么说好呢……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F大人，再怎么说，\x01",
            "玩笑也开得有些过分了……\x02\x03",
            "在城里工作的侍女全都是\x01",
            "诚心服侍女王陛下的。\x02\x03",
            "您忘记了这一点吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F我知道，我知道……\x01",
            "连玩笑的开不起的家伙。\x02\x03",
            "嗝，反正一周之后\x01",
            "这个城就是我的了。\x02\x03",
            "到那时我再来好好\x01",
            "享用这番乐趣吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#710F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#720F大、大人！\x01",
            "请适可而止！\x02\x03",
            "暴饮暴食姑且不论，\x01",
            "沉溺女色简直岂有此理！\x02\x03",
            "我菲利普就算拼了老命\x01",
            "也要劝阻大人……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(
        0xA,
        (
            "#220F我已经说了\x01",
            "我是开玩笑的！\x02\x03",
            "够了！\x01",
            "今晚赶快回去休息吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#720F大、大人\x01",
            "所言极是。\x02\x03",
            "大人您的房间就在前面，\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    def lambda_42E1():
        OP_6D(87270, 0, 5910, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_42E1)

    def lambda_42F9():
        OP_8E(0xFE, 0x15996, 0x0, 0x1482, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_42F9)
    Sleep(600)

    def lambda_4319():
        OP_8E(0xFE, 0x151EE, 0x0, 0x15C2, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4319)
    WaitChrThread(0xA, 0x1)

    def lambda_4339():
        OP_8E(0xFE, 0x14E38, 0x0, 0x15B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4339)
    WaitChrThread(0xA, 0x1)
    Sleep(1000)

    def lambda_435E():

        label("loc_435E")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_435E")

    QueueWorkItem2(0xB, 2, lambda_435E)

    def lambda_436F():
        TurnDirection(0xA, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_436F)
    OP_8F(0xA, 0x14E92, 0x0, 0x18EC, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 6)), scpexpr(EXPR_END)), "loc_43BF")

    ChrTalk(
        0xA,
        (
            "#220F嗯～……\x01",
            "对了，莱娜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442A")

    label("loc_43BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_END)), "loc_43F5")

    ChrTalk(
        0xA,
        (
            "#220F嗯～……\x01",
            "对了，雪拉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442A")

    label("loc_43F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 0)), scpexpr(EXPR_END)), "loc_442A")

    ChrTalk(
        0xA,
        (
            "#220F嗯～……\x01",
            "对了，朵洛希。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_442A")


    ChrTalk(
        0xA,
        (
            "#220F如果有什么困难\x01",
            "不用顾虑，尽管找我商量。\x02\x03",
            "新一代的国王我会\x01",
            "亲自帮你解决的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈……哈哈……\x01",
            "还要多谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F哇哈哈，可爱的宝贝儿。\x02\x03",
            "嗯……愉快愉快！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4506():
        OP_6D(83810, 0, 6600, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4506)
    OP_8E(0xA, 0x13416, 0x0, 0x1B4E, 0x5DC, 0x0)
    OP_8E(0xA, 0x13416, 0x0, 0x2576, 0x5DC, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x138, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    def lambda_455A():

        label("loc_455A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_455A")

    QueueWorkItem2(0x101, 1, lambda_455A)

    def lambda_456B():

        label("loc_456B")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_456B")

    QueueWorkItem2(0x102, 1, lambda_456B)

    def lambda_457C():

        label("loc_457C")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_457C")

    QueueWorkItem2(0x138, 1, lambda_457C)

    def lambda_458D():
        OP_6D(88010, 0, 6080, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_458D)
    OP_8C(0xB, 90, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xB,
        (
            "#720F让你们受惊了。\x02\x03",
            "大人明天一早起来的时候，\x01",
            "就什么也记不起来了。\x02\x03",
            "请你们放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#710F……希望会是如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#720F真的非常抱歉。\x02\x03",
            "夫人、两位姑娘，\x01",
            "那我就告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0xB, 0x149CE, 0x0, 0xE38, 0xBB8, 0x0)
    OP_8E(0xB, 0x13DE4, 0x0, 0xF5A, 0xBB8, 0x0)
    OP_8E(0xB, 0x134B6, 0x0, 0x1888, 0xBB8, 0x0)
    OP_8E(0xB, 0x134B6, 0x0, 0x268E, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x138, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    ChrTalk(
        0x138,
        (
            "#710F唉，谈到那个男的啊……\x02\x03",
            " \x01",
            "那样无益的负担呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        (
            "#000F咦，希尔丹夫人\x01",
            "和菲利普先生认识吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x138, 0x101, 400)

    ChrTalk(
        0x138,
        (
            "#710F在年幼的时候就认识了。\x02\x03",
            "可是到了今天，不管在工作方面\x01",
            "还是在立场方面都有了距离……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x138, 400)

    ChrTalk(
        0x102,
        "#010F是这样的啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F的确，菲利普先生看起来\x01",
            "就是一副饱经沧桑的感觉。\x02\x03",
            "他对公爵被上校唆使这件事\x01",
            "好像非常担心的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F很有可能……\x02\x03",
            "对了，艾丝蒂尔，\x01",
            "你不也很受欢迎吗？\x02\x03",
            "公爵看来很喜欢你呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F哼，你好像有些\x01",
            "幸灾乐祸啊……\x02\x03",
            "啊，到底那个\x01",
            "『伺候』是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这、这个嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#710F艾丝蒂尔。\x02\x03",
            "向异性提出这种问题，\x01",
            "会让对方很难为情哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A11():
        TurnDirection(0xFE, 0x138, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A11)
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        "#000F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#710F……把耳朵凑过来。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)
    OP_8E(0x138, 0x15626, 0x0, 0x1644, 0x7D0, 0x0)
    OP_8C(0x101, 270, 400)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "希尔丹夫人\x01",
            "对艾丝蒂尔说了悄悄话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x138, 0x1578E, 0x0, 0x11EE, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        "#000F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#710F……明白了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x138, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，哦……\x02\x03",
            "…………知道了………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（到底说了些什么呢……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4214   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_366D end

    def Function_14_4B70(): pass

    label("Function_14_4B70")

    EventBegin(0x0)
    RemoveParty(0x1, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 33230, 0, 57840, 90)
    SetChrPos(0x101, 36130, 0, 59420, 0)
    OP_6D(36050, 0, 58110, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_4BDF():

        label("loc_4BDF")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4BDF")

    QueueWorkItem2(0xC, 1, lambda_4BDF)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8E(0x101, 0x8C8C, 0x0, 0xDD68, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8E(0x101, 0x8D22, 0x0, 0xE81C, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    OP_8E(0x101, 0x8C8C, 0x0, 0xDD68, 0x7D0, 0x0)
    Sleep(500)
    OP_63(0x101)

    ChrTalk(
        0x101,
        "#000F唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F怎么了，艾丝蒂尔。\x01",
            "从刚才开始就静不下来。\x02\x03",
            "你在担心什么吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯、嗯……\x02\x03",
            "我说，雪拉姐……\x01",
            "约修亚的样子是不是很奇怪？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F？？？\x02\x03",
            "奇怪的是你啊。\x02\x03",
            "那孩子不是\x01",
            "和平时一样沉着冷静吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F话是这样说没错……\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#020F哈哈。\x02\x03",
            "是吗，原来是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F怎、怎么了突然……\x02",
    )

    CloseMessageWindow()

    def lambda_4DFC():
        OP_6D(35600, 0, 56920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DFC)
    OP_8E(0xC, 0x899E, 0x0, 0xDF0C, 0x7D0, 0x0)

    ChrTalk(
        0xC,
        (
            "#020F你瞒不住我的～⊙\x02\x03",
            "我感到那种气氛了呢……\x01",
            "你自己也明白吧？\x02\x03",
            "你啊……\x01",
            "是不是喜欢上约修亚了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F………呜…………\x02\x03",
            "果、果然知道了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F不好意思哦～让我发现了。\x02\x03",
            "不过你这个样子，\x01",
            "可没办法向约修亚传达真正的心意哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……我也这样觉得……\x02\x03",
            "约修亚从以前开始，\x01",
            "对这方面的事情就很迟钝……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F哎呀，真是单纯的想法啊。\x02\x03",
            "那个不谙世事的艾丝蒂尔，\x01",
            "也终于走到这一步了呢……\x02\x03",
            "姐姐我真是感动啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……再这样的话，\x01",
            "我就不和雪拉姐说啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F抱歉抱歉，\x01",
            "我不开玩笑了。\x02\x03",
            "不过，真是的啊……\x02\x03",
            "仔细想想，你们\x01",
            "在进入青春期以前就已经认识了。\x02\x03",
            "所以没有注意到对方心情的变化\x01",
            "也是没办法的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是，是这样吗……\x02\x03",
            "我在旅行的途中，\x01",
            "开始慢慢有这种感觉……\x02\x03",
            "每次有这样的心情时，\x01",
            "都会很快注意到……\x02\x03",
            "啊啊，真是的，\x01",
            "这样根本不像我嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F呵呵……\x01",
            "没有不会绽放的花蕾呢。\x02\x03",
            "女孩子都是这样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F虽然不能轻率地\x01",
            "就表达自己的心意……\x02\x03",
            "不过，如果你已经下定决心的话，\x01",
            "说出来不是更好吗？\x02\x03",
            "如果不说的话，就什么也不会发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "其实，我已经下定决心了。\x02\x03",
            "而且也和他约定过要听他说自己的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F是吗……\x02\x03",
            "好，这样才是我的妹妹嘛！\x02\x03",
            "哎呀，\x01",
            "姐姐我都要感动地哭了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F能不能给我适可而止啊……\x02\x03",
            "不过，谢谢你，雪拉姐。\x01",
            "我好像有点勇气了呢。\x02\x03",
            "我这就去\x01",
            "约修亚那里看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F哎……！\x02\x03",
            "不、不会现在就要告白吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F不是啦，是另外的事情。\x02\x03",
            "刚才，约修亚的样子\x01",
            "确实有点奇怪呢。\x02\x03",
            "我先问问他是怎么回事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#020F是，是吗……\x02\x03",
            "不过，你还真是\x01",
            "对他的事情很了解啊。\x02\x03",
            "你和约修亚\x01",
            "一定会进行得很顺利的。\x02\x03",
            "如果谈话的时候气氛不错，\x01",
            "干脆就这样告白吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呜……尽量吧……\x02\x03",
            "那么，我走了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_56D8():
        OP_6D(34760, 0, 54010, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56D8)
    OP_8E(0x101, 0x884A, 0x0, 0xC4C2, 0x1388, 0x0)

    def lambda_5704():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5704)
    OP_8E(0x101, 0x88CC, 0x0, 0xBF54, 0x1388, 0x0)

    ChrTalk(
        0xC,
        (
            "#020F……初恋吗……\x02\x03",
            "如果能顺利就好了……\x02",
        )
    )

    CloseMessageWindow()
    NewScene("ED6_DT01/T4221   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_4B70 end

    def Function_15_5768(): pass

    label("Function_15_5768")

    EventBegin(0x0)
    OP_6D(78150, 0, 55830, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 79820, 0, 50600, 0)
    OP_6D(89010, 0, 56310, 3000)
    SetChrPos(0x101, 79700, 0, 55220, 90)
    OP_6D(79690, 0, 55490, 2000)

    ChrTalk(
        0x101,
        (
            "#000F哎……\x01",
            "两个人都不在啊。\x02\x03",
            "对了，\x01",
            "老爸说过还要开会……\x02\x03",
            "可是，约修亚呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F约修亚……\x02\x03",
            "是在哪里吹的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_1B(0x6, 0x0, 0xFFFF)
    EventEnd(0x0)
    Return()

    # Function_15_5768 end

    def Function_16_58C4(): pass

    label("Function_16_58C4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#007F哎呀，我真是的。\x01",
            "这是往哪里走啊。\x02\x03",
            "#000F……不赶快去约修亚的房间的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_58C4 end

    def Function_17_592F(): pass

    label("Function_17_592F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#007F哎呀，我真是的。\x01",
            "这是往哪里走啊。\x02\x03",
            "#000F……不赶快去约修亚的房间的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_17_592F end

    SaveToFile()

Try(main)
