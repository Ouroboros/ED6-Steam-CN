from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3118   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3118.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3118   ._SN',
            'ED6_DT01/T3118_1 ._SN',
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
        '米妮亚姆医生',                         # 9
        '阿加特',                               # 10
        '鲁迪',                                 # 11
        '安东尼',                               # 12
        '提妲',                                 # 13
        '玛多克工房长',                         # 14
        '书2',                                  # 15
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
        'ED6_DT07/CH01500 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
        'ED6_DT07/CH00060 ._CH',             # 04
        'ED6_DT07/CH02620 ._CH',             # 05
        'ED6_DT06/CH20061 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
        'ED6_DT07/CH01500P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
        'ED6_DT07/CH00060P._CP',             # 04
        'ED6_DT07/CH02620P._CP',             # 05
        'ED6_DT06/CH20061P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x196,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 8,
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
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 6,
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
        X                   = -9560,
        Z                   = 800,
        Y                   = -1360,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1769479,
        ChipIndex           = 0x7,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -9560,
        TriggerZ            = 0,
        TriggerY            = -1360,
        TriggerRange        = 800,
        ActorX              = -9560,
        ActorZ              = 800,
        ActorY              = -1360,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_471",          # 01, 1
        "Function_2_564",          # 02, 2
        "Function_3_57A",          # 03, 3
        "Function_4_5C8",          # 04, 4
        "Function_5_641",          # 05, 5
        "Function_6_6ED",          # 06, 6
        "Function_7_9E8",          # 07, 7
        "Function_8_2950",         # 08, 8
        "Function_9_2995",         # 09, 9
        "Function_10_313F",        # 0A, 10
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1FC")
    OP_A3(0x3FA)
    Event(0, 9)

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_20A")
    OP_A3(0x3FB)
    Event(1, 4)

    label("loc_20A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_216"),
        (SWITCH_DEFAULT, "loc_22E"),
    )


    label("loc_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22B")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_22B")

    Jump("loc_22E")

    label("loc_22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_24E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    Jump("loc_455")

    label("loc_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_26E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    Jump("loc_455")

    label("loc_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2BA")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -3440, 0, -6430, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1530, 400, -6000, 0)
    Jump("loc_455")

    label("loc_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_2F0")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1530, 400, -6000, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    Jump("loc_455")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_326")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -4680, 0, 6630, 90)
    Jump("loc_455")

    label("loc_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_330")
    Jump("loc_455")

    label("loc_330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3AC")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_35F")
    SetChrPos(0x8, -5680, 0, 6400, 337)
    Jump("loc_393")

    label("loc_35F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_382")
    SetChrPos(0x8, -1160, 0, 6790, 110)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_393")

    label("loc_382")

    SetChrPos(0x8, -1160, 0, 6790, 110)

    label("loc_393")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -6210, 0, 6890, 143)
    Jump("loc_455")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3E2")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -6210, 0, 6890, 143)
    Jump("loc_455")

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_418")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -6210, 0, 6890, 143)
    Jump("loc_455")

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_438")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)
    Jump("loc_455")

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_455")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1750, 0, 6610, 269)

    label("loc_455")

    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_470")
    ClearChrFlags(0xE, 0x80)

    label("loc_470")

    Return()

    # Function_0_1EE end

    def Function_1_471(): pass

    label("Function_1_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_489")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B6")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B6")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CE")
    OP_72(0x2, 0x20)
    OP_6F(0x2, 20)

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_530")
    LoadEffect(0x1, "map\\\\mpfog.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_543")
    SetChrFlags(0xB, 0x80)

    label("loc_543")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2D, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_563")
    OP_65(0x0, 0x1)

    label("loc_563")

    Return()

    # Function_1_471 end

    def Function_2_564(): pass

    label("Function_2_564")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_579")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_564")

    label("loc_579")

    Return()

    # Function_2_564 end

    def Function_3_57A(): pass

    label("Function_3_57A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x1000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A4")

    label("loc_58C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_58C")

    label("loc_5A1")

    Jump("loc_5C7")

    label("loc_5A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C7")
    OP_8D(0xFE, -5120, 8029, -7290, 5400, 1000)
    Jump("loc_5A4")

    label("loc_5C7")

    Return()

    # Function_3_57A end

    def Function_4_5C8(): pass

    label("Function_4_5C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_606")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x38A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F0")
    Call(1, 3)
    Jump("loc_603")

    label("loc_5F0")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵～呀。\x02",
    )

    CloseMessageWindow()

    label("loc_603")

    Jump("loc_63D")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_623")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵－噢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_63D")

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_63D")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵～呵。\x02",
    )

    CloseMessageWindow()

    label("loc_63D")

    TalkEnd(0xFE)
    Return()

    # Function_4_5C8 end

    def Function_5_641(): pass

    label("Function_5_641")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_68A")

    ChrTalk(
        0x9,
        (
            "#053F………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E9")

    label("loc_68A")


    ChrTalk(
        0x9,
        (
            "#551F………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F阿加特大哥哥………………\x02",
    )

    CloseMessageWindow()

    label("loc_6E9")

    TalkEnd(0xFE)
    Return()

    # Function_5_641 end

    def Function_6_6ED(): pass

    label("Function_6_6ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_9E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_745")

    ChrTalk(
        0xFE,
        (
            "#060F我还想在这里\x01",
            "照顾一会儿阿加特大哥哥。\x02\x03",
            "姐姐你们要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E4")

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 4)), scpexpr(EXPR_END)), "loc_7DF")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "#060F啊，哥哥，姐姐……\x02\x03",
            "阿加特大哥哥\x01",
            "现在好像已经没事了。\x02\x03",
            "#066F不过…………\x01",
            "我还想在这里\x01",
            "照顾一会儿阿加特大哥哥。\x02\x03",
            "姐姐你们要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E4")

    label("loc_7DF")

    OP_A2(0x2)
    OP_A2(0x58C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA")

    ChrTalk(
        0xFE,
        "#560F啊，艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F怎么样？阿加特现在的情况。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#060F嗯，睡得很熟。\x01",
            "好像已经没事了。\x02\x03",
            "姐姐你们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我们还在调查那件事。\x01",
            "　\x02\x03",
            "调查就交给我们，\x01",
            "你就好好看着阿加特吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#060F嗯，我知道了。\x02\x03",
            "姐姐你们也要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E4")

    label("loc_8EA")


    ChrTalk(
        0xFE,
        "#560F啊，约修亚哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F阿加特现在的情况怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#060F嗯，睡得很熟。\x01",
            "好像已经没事了。\x02\x03",
            "哥哥你们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F现在我们正在尽全力调查。\x01",
            "　\x02\x03",
            "提妲你就不用担心了，\x01",
            "在这里好好照顾病人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#060F嗯，我知道了。\x02\x03",
            "哥哥你们也要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E4")

    TalkEnd(0xFE)
    Return()

    # Function_6_6ED end

    def Function_7_9E8(): pass

    label("Function_7_9E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A4E")

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "军队那边也不可能就这样善罢甘休。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还是赶快想想\x01",
            "有没有什么对策吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADE")

    label("loc_A4E")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "啊，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "营救作战的结果\x01",
            "我也已经知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "博士他们平安无事\x01",
            "比什么都好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来我们也只能期待\x01",
            "他们能顺利逃脱追捕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADE")

    Jump("loc_294C")

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 3)), scpexpr(EXPR_END)), "loc_B24")

    ChrTalk(
        0xFE,
        "你们要小心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "阿加特你也不要擅自行事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE1")

    label("loc_B24")

    OP_A2(0x58B)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(
        0xFE,
        (
            "啊，阿加特。\x01",
            "你要去哪儿！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我都叮嘱过你\x01",
            "要静养一段时间的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F已经没事啦，医生。\x02\x03",
            "身体都变得僵硬了，\x01",
            "我去稍微散个步。\x02\x03",
            "#053F……而且还打算做些轻量的运动。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        (
            "#509F散、散步……\x02\x03",
            "唉～阿加特。\x01",
            "这是你自己说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "真是没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "你可是一名游击士，\x01",
            "要为自己负起责任才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好吧，随你的便了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……不过，千万不要勉强自己。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F啊，\x01",
            "我不会再带给医生添麻烦的。\x02\x03",
            "多谢你的照顾啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE1")

    Jump("loc_294C")

    label("loc_CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_E1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D6E")

    ChrTalk(
        0xFE,
        (
            "虽然阿加特还没有醒过来，\x01",
            "不过我想他应该已经脱离危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "提妲那么热心地\x01",
            "一直在旁边看护着他，\x01",
            "真的是帮了我大忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E18")

    label("loc_D6E")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "昨天辛苦了。\x01",
            "多亏了你们阿加特才能够得救。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然还没有醒过来，\x01",
            "不过他已经度过危险期了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在与其说是失去意识，\x01",
            "不如说是在沉睡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "一定会很快醒过来的。\x02",
    )

    CloseMessageWindow()

    label("loc_E18")

    Jump("loc_294C")

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_EB0")

    ChrTalk(
        0xFE,
        (
            "七耀教会积累了\x01",
            "上千年的传统医疗方法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "皮克塞恩教区长说不定会知道\x01",
            "这种未知毒药的解毒方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想有必要去教会\x01",
            "和他商量一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_294C")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_133D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_F1B")

    ChrTalk(
        0xFE,
        (
            "关于烟草搜查的委托\x01",
            "就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然有些遗憾，\x01",
            "不过再有什么事还请多多照顾哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133A")

    label("loc_F1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1140")
    OP_28(0x2C, 0x1, 0x4000)
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "据我所知，\x01",
            "好像没有人受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然案件很严重，\x01",
            "不过大家都还平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了对了，说到案件，\x01",
            "之前拜托你们调查烟草的那件事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然很遗憾， \x01",
            "不过调查就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F咦……为什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "被拿走的烟草\x01",
            "不知道什么时候又回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没有证据，\x01",
            "就不能抓到犯人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就是这样，\x01",
            "这次就放弃吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#013F是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唔～真是对不起…………\x02\x03",
            "唉，如果能够\x01",
            "早一点展开调查就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，如果还有什么事\x01",
            "就再和我们联络吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "嗯，到时候还请多关照。\x02",
    )

    CloseMessageWindow()
    Jump("loc_133A")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11A4")

    ChrTalk(
        0xFE,
        (
            "据我所知，\x01",
            "好像没有人受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然案件很严重，\x01",
            "不过大家都还平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133A")

    label("loc_11A4")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "啊，各位辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "据我所知，\x01",
            "好像没有人受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然案件很严重，\x01",
            "不过大家都还平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_133A")

    ChrTalk(
        0x107,
        "#063F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0xFE,
        "提妲，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "有哪里不舒服吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#064F啊……\x02\x03",
            "#060F没、没什么事啦。\x02\x03",
            "我、我只是\x01",
            "稍微发个呆而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是吗，可不要勉强哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "也许你已经有些疲劳了。\x01",
            "今天就早点休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，好的。\x01",
            "我知道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133A")

    Jump("loc_294C")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_161E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13B0")

    ChrTalk(
        0xFE,
        (
            "今天辛苦你们了。\x01",
            "感谢你们为我解决这件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果再有什么事的话，\x01",
            "还请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EC")

    label("loc_13B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1416")

    ChrTalk(
        0xFE,
        (
            "现、现在我正在研究\x01",
            "利用动物来减轻压力的方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "别看我这么说，\x01",
            "我可不是在开玩笑哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EC")

    label("loc_1416")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "小安东尼～～～\x01",
            "你很清楚犯人是谁啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "真是了不起的孩子～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "……啊！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "咳咳……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎、哎呀，是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "请问找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    label("loc_14EC")

    Jump("loc_161B")

    label("loc_14EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155F")

    ChrTalk(
        0xFE,
        "啊，安东尼也在一起啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它肯定会给你们\x01",
            "提供什么线索的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，请慢走～\x02",
    )

    CloseMessageWindow()
    Jump("loc_15CC")

    label("loc_155F")


    ChrTalk(
        0xFE,
        (
            "带着安东尼一起去\x01",
            "说不定会得到什么线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它最喜欢的新鲜牛奶\x01",
            "在杂货店就可以买得到，\x01",
            "你们不妨试一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CC")

    Jump("loc_161B")

    label("loc_15CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_15E0")
    Call(1, 2)
    Jump("loc_161B")

    label("loc_15E0")


    ChrTalk(
        0xFE,
        "唔～真是奇怪了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我明明记得\x01",
            "之前放在这里的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161B")

    Jump("loc_294C")

    label("loc_161E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_20AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1672")

    ChrTalk(
        0xFE,
        "哎，还有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之先去演算室\x01",
            "看一看情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CE")

    label("loc_1672")


    ChrTalk(
        0xFE,
        "是啊，中央工房太大了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不知道想去的地方在哪里，\x01",
            "就去一楼的接待处\x01",
            "打听一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CE")

    Jump("loc_20A9")

    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 2)), scpexpr(EXPR_END)), "loc_1758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1715")

    ChrTalk(
        0xFE,
        "啊，调查已经完成了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "演算室就在五楼。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1755")

    label("loc_1715")


    ChrTalk(
        0xFE,
        (
            "如果不知道想去的地方在哪里，\x01",
            "就去一楼的接待处\x01",
            "打听一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1755")

    Jump("loc_20A9")

    label("loc_1758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D42")
    OP_A2(0x0)
    OP_A2(0x58A)
    OP_A2(0x58A)
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "昨天大家可都够呛呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个医务室倒还没事，\x01",
            "不过其他地方就\x01",
            "被弄得一塌糊涂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天早上回来的时候，\x01",
            "发现安东尼睡在床上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定是其他地方发生骚动，\x01",
            "没有地方可以去吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#505F安东尼？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0xFE,
        "#560F就是那只小猫的名字。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#560F它很早以前\x01",
            "就已经住在中央工房了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18C0")

    def lambda_18B8():
        TurnDirection(0x1, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_18B8)

    label("loc_18C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18DA")

    def lambda_18D2():
        TurnDirection(0x2, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_18D2)

    label("loc_18DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18F4")

    def lambda_18EC():
        TurnDirection(0x3, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_18EC)

    label("loc_18F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_190E")

    def lambda_1906():
        TurnDirection(0x4, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_1906)

    label("loc_190E")

    TurnDirection(0x0, 0xB, 400)
    TurnDirection(0xFE, 0xB, 400)

    ChrTalk(
        0xFE,
        (
            "应该不是某户人家里养的猫，\x01",
            "所以谁有兴趣谁就来照顾它了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F原来是这样啊，\x01",
            "就算是大家一起养的猫吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "安东尼自己\x01",
            "也丝毫不在意\x01",
            "成为家猫呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后在别的地方碰见它，\x01",
            "可要好好照顾它哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F嗯，那当然啦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A27")

    def lambda_1A1F():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1A1F)

    label("loc_1A27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A41")

    def lambda_1A39():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1A39)

    label("loc_1A41")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A5B")

    def lambda_1A53():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1A53)

    label("loc_1A5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A75")

    def lambda_1A6D():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_1A6D)

    label("loc_1A75")

    TurnDirection(0x0, 0x8, 400)

    ChrTalk(
        0xFE,
        (
            "……那么，\x01",
            "安东尼也介绍过了，\x01",
            "我也差不多该开始工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB1")
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "你们不是也\x01",
            "有事情要办吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，\x01",
            "我们打算去五楼的演算室。\x02\x03",
            "稍微有些事情要调查。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0xFE,
        "啊，到演算室？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～没问题吗……\x01",
            "最近那里的设备好像一直在调整中啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F有什么问题吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "没什么，因为是精密仪器，\x01",
            "所以要维持正常的机能十分不容易。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "你们去那里看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F唔～没关系吗。\x01",
            "好像气氛有一些可疑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F总之先按照医生说的\x01",
            "到演算室去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，说的也是。\x02\x03",
            "医生，再见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好的，你们慢走。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D3F")

    label("loc_1CB1")

    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "你们不是也\x01",
            "有事情要办吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F啊，对了。\x01",
            "我们要去取汽油和内燃引擎设备了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么先告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好的，你们慢走。\x02",
    )

    CloseMessageWindow()

    label("loc_1D3F")

    Jump("loc_20A9")

    label("loc_1D42")

    OP_A2(0x0)
    OP_A2(0x58A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5E")

    ChrTalk(
        0xFE,
        "咦，是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "和拉赛尔博士见过面了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，当然。\x01",
            "现在我们正在给博士帮忙。\x02\x03",
            "要去演算室\x01",
            "调查一些事情。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0xFE,
        "去演算室调查一些事情？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～没问题吗……\x01",
            "最近那里的设备好像一直在调整中啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F有什么问题吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "没什么，因为是精密仪器，\x01",
            "所以要维持正常的机能十分不容易。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "你们去那里看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔～没关系吗。\x01",
            "好像气氛有一些可疑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F总之先按照医生说的\x01",
            "到演算室去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，说的也是。\x02\x03",
            "医生，再见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好的，你们慢走。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20A9")

    label("loc_1F5E")


    ChrTalk(
        0xFE,
        "咦，是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "和拉赛尔博士见过面了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，当然。\x01",
            "现在我们正在给博士帮忙。\x02\x03",
            "我们正准备去替博士\x01",
            "拿一些研究必要的东西。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "是吗，中央工房很大，\x01",
            "不要迷路了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果不知道想去的地方在哪里，\x01",
            "就去一楼的接待处\x01",
            "打听一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好的，多谢您的提醒。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么我也要工作了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好，我们告辞了。\x02",
    )

    CloseMessageWindow()

    label("loc_20A9")

    Jump("loc_294C")

    label("loc_20AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2680")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2105")

    ChrTalk(
        0xFE,
        (
            "拉赛尔博士\x01",
            "应该在三楼的工作室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想他应该\x01",
            "已经开始工作了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267D")

    label("loc_2105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_END)), "loc_2157")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "你们去找过拉赛尔博士了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "博士肯定就在\x01",
            "三楼的工作室里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267D")

    label("loc_2157")

    OP_A2(0x0)
    OP_A2(0x589)

    ChrTalk(
        0xFE,
        "啊，早上好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "昨天大家可都够呛呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#065F啊，那个……\x02\x03",
            "米妮亚姆医生这里\x01",
            "没出什么事吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "医务室倒没遇到什么麻烦，\x01",
            "和平时一样一切都很正常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过其他地方好像就\x01",
            "被弄得一塌糊涂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天早上回来的时候，\x01",
            "发现安东尼睡在床上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一定是其他地方发生骚动，\x01",
            "没有地方可以去吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#505F安东尼？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#560F就是那只小猫的名字。\x02\x03",
            "它很早以前\x01",
            "就已经住在中央工房了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2340")

    def lambda_2338():
        TurnDirection(0x1, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2338)

    label("loc_2340")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_235A")

    def lambda_2352():
        TurnDirection(0x2, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2352)

    label("loc_235A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2374")

    def lambda_236C():
        TurnDirection(0x3, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_236C)

    label("loc_2374")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_238E")

    def lambda_2386():
        TurnDirection(0x4, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_2386)

    label("loc_238E")

    TurnDirection(0x0, 0xB, 400)
    TurnDirection(0xFE, 0xB, 400)

    ChrTalk(
        0xFE,
        (
            "应该不是某户人家里养的猫，\x01",
            "所以谁有兴趣谁就来照顾它了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F原来是这样啊，\x01",
            "就算是大家一起养的猫吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F嘿嘿，\x01",
            "就～是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "安东尼自己\x01",
            "也丝毫不在意\x01",
            "成为家猫呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以后在别的地方碰见它，\x01",
            "可要好好照顾它哦～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        "#001F嗯，那当然啦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24BC")

    def lambda_24B4():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_24B4)

    label("loc_24BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24D6")

    def lambda_24CE():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_24CE)

    label("loc_24D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24F0")

    def lambda_24E8():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_24E8)

    label("loc_24F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_250A")

    def lambda_2502():
        TurnDirection(0x4, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_2502)

    label("loc_250A")

    TurnDirection(0x0, 0x8, 400)

    ChrTalk(
        0xFE,
        (
            "……那么，\x01",
            "安东尼也介绍过了，\x01",
            "我也差不多该开始工作了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(
        0xFE,
        (
            "提妲你们\x01",
            "不是也有事情要办吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，对了，是啊。\x02\x03",
            "我们正要去爷爷那里呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是吗，\x01",
            "拉赛尔博士应该在三楼的工作室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "今天一大早\x01",
            "就过来工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F三楼的工作室吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F那我们快去吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F嗯，好的。\x02\x03",
            "米妮亚姆医生，\x01",
            "我们就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好的，你们慢走。\x02",
    )

    CloseMessageWindow()
    OP_28(0x3F, 0x1, 0x40)

    label("loc_267D")

    Jump("loc_294C")

    label("loc_2680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_28CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 0)), scpexpr(EXPR_END)), "loc_26F8")

    ChrTalk(
        0xFE,
        (
            "拉赛尔博士\x01",
            "如果也像提妲一样听话，\x01",
            "就能让我省不少心了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "下一次的体检\x01",
            "真希望他能够好好配合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CA")

    label("loc_26F8")

    OP_A2(0x588)
    TurnDirection(0x8, 0x107, 0)

    ChrTalk(
        0xFE,
        "啊，这不是提妲吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近拉赛尔博士身体怎么样？\x01",
            "有没有哪里不舒服的感觉？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，是。\x01",
            "和平常一样很～健康哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是吗，那样就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，如果他再继续保持这样\x01",
            "无规律的生活习惯，肯定会出问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以防万一，回去请转告博士\x01",
            "务必要来我这里\x01",
            "定期检查一下身体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F啊，好的，我会转告的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼～拉赛尔博士\x01",
            "如果也像提妲\x01",
            "一样听话就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经常编造各种理由\x01",
            "逃避身体检查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "跟小孩子一样任性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#067F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_28CA")

    Jump("loc_294C")

    label("loc_28CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_294C")

    ChrTalk(
        0xFE,
        "有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里是工房附属的\x01",
            "医疗技术研究所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们这里也做一般的诊疗，\x01",
            "要是感到身体不舒服的话就过来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294C")

    TalkEnd(0xFE)
    Return()

    # Function_7_9E8 end

    def Function_8_2950(): pass

    label("Function_8_2950")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_2991")

    ChrTalk(
        0xFE,
        "咳、咳咳……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "还是感觉胸腔里面很不舒服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2991")

    TalkEnd(0xFE)
    Return()

    # Function_8_2950 end

    def Function_9_2995(): pass

    label("Function_9_2995")

    EventBegin(0x0)
    OP_6D(-3770, 0, 7220, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 20)
    SetChrPos(0x9, -1530, 400, -6000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x5, 0xFF)
    SetChrPos(0x8, -1330, 0, -4950, 180)
    SetChrPos(0x107, -2140, 0, -4950, 180)
    SetChrPos(0x101, -3440, 0, -6060, 90)
    SetChrPos(0x102, 840, 0, 1080, 270)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_6D(-1680, 0, -3300, 4000)

    ChrTalk(
        0x8,
        (
            "#5P总之要先帮他\x01",
            "做一下应急的治疗才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过……\x01",
            "这好像是相当特殊的神经毒药。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P一般的解毒剂是没有效果的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(
        0x107,
        (
            "#063F#1P那、那个……\x01",
            "阿加特大哥哥会怎么样呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P像他这么健壮的人，\x01",
            "应该还能撑得住……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过，要是一直持续这种昏睡状态，\x01",
            "还是会有生命危险的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#069F#1P…………！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#6P怎、怎么会……\x02",
    )

    CloseMessageWindow()
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_8E(0x102, 0xFFFFFBBE, 0x0, 0x3A2, 0xBB8, 0x0)
    OP_6F(0x0, 30)
    OP_70(0x0, 0x0)
    OP_8E(0x102, 0xFFFFF1DC, 0x0, 0xFFFFFE84, 0xBB8, 0x0)

    def lambda_2BFD():
        OP_8E(0xFE, 0xFFFFF1DC, 0x0, 0xFFFFEE08, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BFD)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    def lambda_2C3B():

        label("loc_2C3B")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_2C3B")

    QueueWorkItem2(0x101, 1, lambda_2C3B)

    ChrTalk(
        0x101,
        "#002F#6P啊，约修亚……\x02",
    )

    CloseMessageWindow()

    def lambda_2C68():

        label("loc_2C68")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_2C68")

    QueueWorkItem2(0x107, 1, lambda_2C68)

    def lambda_2C79():

        label("loc_2C79")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_2C79")

    QueueWorkItem2(0x8, 1, lambda_2C79)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x102,
        (
            "#010F#1P抱歉来迟了。\x01",
            "我已经向雾香小姐报告过了。\x02\x03",
            "军队方面也拜托她通报过了，\x01",
            "我想过几天应该能得到一些情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F#6P是吗……辛苦你了。\x02\x03",
            "#004F对了，金先生呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P啊……\x01",
            "他和雾香姐好像是旧识。\x02\x03",
            "我想他们之间有很多话要聊吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F#6P原来是这样啊……\x01",
            "说起来他们两个都是东方出身的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        (
            "#012F#1P那么……\x01",
            "阿加特兄的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F#6P那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F#5P………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F#1P是吗……\x01",
            "看来还是有生命危险对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P很遗憾，以我的知识……\x01",
            "只要不知道这种毒物的具体成分，\x01",
            "就没办法为这位先生解毒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P不过……\x01",
            "或许皮克塞恩教区长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F#5P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#6P皮克塞恩教区长？\x02",
    )

    CloseMessageWindow()
    OP_44(0x107, 0xFF)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#560F#5P那、那个……\x01",
            "他是蔡斯教区的神父呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F4A():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F4A)

    def lambda_2F58():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F58)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#2P七耀教会积累了\x01",
            "近千年的传统医疗知识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P特别是在药学方面，\x01",
            "他们有各种各样的独到秘方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P或许教会那里会有\x01",
            "关于未知毒物的对应疗法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F#6P原来是这样啊。\x01",
            "以前在洛连特的教区长那里也开过药方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#1P看来有必要去拜访一下了。\x02\x03",
            "虽然已经很晚了……\x01",
            "我们还是尽快去一趟教会吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        "#062F#5P嗯、嗯……！\x02",
    )

    CloseMessageWindow()
    OP_28(0x42, 0x4, 0x2)
    OP_28(0x42, 0x4, 0x4)
    OP_28(0x42, 0x1, 0x1)
    OP_28(0x42, 0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x8, 0xFF)
    OP_43(0x8, 0x0, 0x0, 0x2)
    OP_8C(0x8, 180, 0)
    SetChrPos(0x101, -4490, 0, -1400, 0)
    SetChrPos(0x102, -4490, 0, -1400, 0)
    SetChrPos(0x107, -4490, 0, -1400, 0)
    OP_6D(-4490, 0, -1400, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x800)
    EventEnd(0x0)
    Return()

    # Function_9_2995 end

    def Function_10_313F(): pass

    label("Function_10_313F")

    EventBegin(0x0)
    ClearMapFlags(0x10000000)
    OP_6D(-2250, 0, -130, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 20)
    SetChrPos(0x9, -1530, 400, -6000, 0)
    SetChrPos(0x8, -3660, 0, -5180, 135)
    SetChrPos(0x101, -1990, 0, 1000, 225)
    SetChrPos(0x102, -1280, 0, 1910, 225)
    SetChrPos(0x108, -940, 0, 820, 225)
    SetChrPos(0x107, -1410, 0, 160, 225)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#006F医生，让您久等了！\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 0, 600)

    def lambda_3227():
        OP_6D(-2250, 0, 1000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3227)
    OP_8E(0x8, 0xFFFFF20E, 0x0, 0xFFFFFB78, 0xFA0, 0x0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(
        0x8,
        "#6P怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F终于拿到了！\x01",
            "教区长已经把药给我们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P真的！？\x01",
            "不愧是皮克塞恩教区长啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFF45C, 0x0, 0xFFFFFDF8, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "亚鲁福灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x366, 1)
    OP_8F(0x101, 0xFFFFF678, 0x0, 0x10E, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        (
            "#6P原来如此……\x01",
            "是活化免疫力的药啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P可以试试看。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x8, -1330, 0, -4950, 180)
    SetChrPos(0x107, -2140, 0, -4950, 180)
    SetChrPos(0x101, -3440, 0, -6060, 90)
    SetChrPos(0x102, -3430, 0, -6960, 90)
    SetChrPos(0x108, -3630, 0, -5030, 135)
    OP_6D(-1680, 0, -3300, 0)
    Sleep(1500)

    ChrTalk(
        0x8,
        (
            "#5P那么……\x01",
            "就给他喝喝看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "米妮亚姆医生用吸管\x01",
            "轻轻地往阿加特的嘴里喂亚鲁福灵药。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#6P……（吞口水）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F#5P……女神啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#053F#2P………………………\x02",
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x9,
        "#053F#2P……呜……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x14, 0x0, 0x190, 0xFA0)

    ChrTalk(
        0x9,
        "#056F#2P呜……呜唔唔……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 5)
    OP_9E(0x9, 0x1E, 0x0, 0x1F4, 0xFA0)

    ChrTalk(
        0x9,
        "#059F#2P啊啊啊……唔啊啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#069F#5P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#6P哇哇……！\x01",
            "他怎么好像很痛苦啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#6P不要紧……\x01",
            "我想，阿加特兄已经没事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#6P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F#5P药力已经开始起效了。\x02\x03",
            "会感到痛觉得苦就表明\x01",
            "身体机能已经重新恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P呵呵，正是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P这下他已经脱离了\x01",
            "神经毒药引起的危险昏睡状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F#3P是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#063F#5P但、但是……\x01",
            "阿加特大哥哥好像很痛苦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P嗯……\x01",
            "至少要这样痛苦一天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P不过不要紧，\x01",
            "痛苦过后就能完全痊愈了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，中毒的阿加特总算度过了危险期。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当大家放下心来之时已经是夜深了，\x01",
            "艾丝蒂尔他们决定整夜轮流照看阿加特。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_56(0x0)
    OP_20(0x3E8)
    OP_21()
    OP_77(0x70, 0x91, 0xFF, 0x0, 0x0)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x107, -1160, 0, 6540, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_6D(-1160, 0, 6540, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    OP_1D(0x53)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        (
            "#064F咦，好奇怪……\x02\x03",
            "更换的毛巾明明放在这儿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P呼呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1P……呜啊啊啊啊……\x02",
    )

    CloseMessageWindow()
    OP_4A(0x107, 255)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 180, 400)

    ChrTalk(
        0x107,
        "#062F！！！\x02",
    )

    CloseMessageWindow()

    def lambda_3917():
        OP_6D(-1300, 0, -4950, 4500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3917)
    OP_8E(0x107, 0xFFFFEACA, 0x0, 0x1446, 0x1388, 0x0)
    OP_8E(0x107, 0xFFFFF114, 0x0, 0xFFFFED90, 0x1388, 0x0)
    OP_8E(0x107, 0xFFFFFAEC, 0x0, 0xFFFFECAA, 0x1388, 0x0)
    OP_8C(0x107, 180, 400)
    WaitChrThread(0x107, 0x1)

    ChrTalk(
        0x107,
        (
            "#065F#5P阿、阿加特大哥哥……\x02\x03",
            "好、好多汗……\x01",
            "得帮他擦一下……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x9,
        "#553F#2P……呜呜……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x9, 1)
    OP_0D()
    Sleep(500)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#560F#5P啊，阿加特大哥哥！\x01",
            "你醒了吗？\x02\x03",
            "我马上去帮你拿水……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x1, 0x3, 0x320)
    Sleep(500)

    ChrTalk(
        0x9,
        "#553F#2P米、米夏吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#554F#2P太、太好了……\x01",
            "……你在这啊……\x02\x03",
            "……有哥哥陪着你……\x01",
            "已经……不用害怕了……\x02\x03",
            "……所以……所以……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x9, 0x3, 0x5, 0x2BC)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x9,
        "#053F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F#5P阿、阿加特大哥哥！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "提妲慌张地确认阿加特的情况。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "和先前相比，阿加特的呼吸平和了许多，\x01",
            "而且还安安稳稳地睡着了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(
        0x107,
        (
            "#561F#5P呼，\x01",
            "太、太好了……\x02\x03",
            "#066F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1600)
    OP_63(0x107)
    Sleep(500)

    ChrTalk(
        0x107,
        (
            "#063F#5P米夏……\x01",
            "刚才是这么叫的吧……\x02\x03",
            "……会是……谁呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0xD, 0x0, 0x64)
    SetMapFlags(0x100000)
    Sleep(3000)
    OP_A2(0x558)
    OP_28(0x42, 0x1, 0x200)
    ClearMapFlags(0x800)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_313F end

    SaveToFile()

Try(main)
