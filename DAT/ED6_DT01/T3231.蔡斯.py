from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3231   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3231.x',
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
        '拜舍尔',                               # 9
        '艾德',                                 # 10
        '林',                                   # 11
        '莉西亚',                               # 12
        '希利尔',                               # 13
        '艾缇',                                 # 14
        '拉克',                                 # 15
        '希玛',                                 # 16
        '库安',                                 # 17
        '西加罗',                               # 18
        '艾德尔',                               # 19
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
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01030 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01160 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01060 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01030P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01160P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01060P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
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
        TalkScenaIndex      = 5,
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
        TalkScenaIndex      = 6,
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 4,
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
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = -1900,
        TriggerZ            = 0,
        TriggerY            = 5070,
        TriggerRange        = 800,
        ActorX              = -1900,
        ActorZ              = 1000,
        ActorY              = 5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1890,
        TriggerZ            = 0,
        TriggerY            = -4990,
        TriggerRange        = 800,
        ActorX              = -1890,
        ActorZ              = 1000,
        ActorY              = -4990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_370",          # 01, 1
        "Function_2_3B0",          # 02, 2
        "Function_3_3C6",          # 03, 3
        "Function_4_424",          # 04, 4
        "Function_5_568",          # 05, 5
        "Function_6_8E2",          # 06, 6
        "Function_7_8E9",          # 07, 7
        "Function_8_8F0",          # 08, 8
        "Function_9_8F7",          # 09, 9
        "Function_10_8FE",         # 0A, 10
        "Function_11_905",         # 0B, 11
        "Function_12_90C",         # 0C, 12
        "Function_13_913",         # 0D, 13
        "Function_14_91A",         # 0E, 14
        "Function_15_BCD",         # 0F, 15
        "Function_16_E7F",         # 10, 16
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2B4")
    Jump("loc_36F")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2BE")
    Jump("loc_36F")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2DE")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1080, 0, 440, 85)
    Jump("loc_36F")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1090, 0, -900, 82)
    Jump("loc_36F")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_31E")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1080, 0, 440, 85)
    Jump("loc_36F")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_328")
    Jump("loc_36F")

    label("loc_328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_332")
    Jump("loc_36F")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_352")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -990, 0, 10, 90)
    Jump("loc_36F")

    label("loc_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -990, 0, 10, 90)

    label("loc_36F")

    Return()

    # Function_0_2AA end

    def Function_1_370(): pass

    label("Function_1_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_388")
    OP_B1("t3231_y")
    Jump("loc_391")

    label("loc_388")

    OP_B1("t3231_n")

    label("loc_391")

    OP_72(0x8, 0x10)
    OP_72(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AF")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)

    label("loc_3AF")

    Return()

    # Function_1_370 end

    def Function_2_3B0(): pass

    label("Function_2_3B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3B0")

    label("loc_3C5")

    Return()

    # Function_2_3B0 end

    def Function_3_3C6(): pass

    label("Function_3_3C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3D3")
    Jump("loc_420")

    label("loc_3D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_420")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3E7")
    Jump("loc_420")

    label("loc_3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3F1")
    Jump("loc_420")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_3FB")
    Jump("loc_420")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_405")
    Jump("loc_420")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_40F")
    Jump("loc_420")

    label("loc_40F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_419")
    Jump("loc_420")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_420")

    label("loc_420")

    TalkEnd(0xFE)
    Return()

    # Function_3_3C6 end

    def Function_4_424(): pass

    label("Function_4_424")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_431")
    Jump("loc_564")

    label("loc_431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_43B")
    Jump("loc_564")

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4B7")

    ChrTalk(
        0xFE,
        (
            "蔡斯那边\x01",
            "好像发生了什么大事件呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "早早地赶到这里真是明智啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564")

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_564")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_53F")

    ChrTalk(
        0xFE,
        (
            "嗯，真是好温泉。\x01",
            "身体从内到外都感觉很暖和。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "泡温泉的时候\x01",
            "可以把讨厌的事全都给忘掉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_564")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_553")
    Jump("loc_564")

    label("loc_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_55D")
    Jump("loc_564")

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_564")

    label("loc_564")

    TalkEnd(0xFE)
    Return()

    # Function_4_424 end

    def Function_5_568(): pass

    label("Function_5_568")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_575")
    Jump("loc_8DE")

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_57F")
    Jump("loc_8DE")

    label("loc_57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_589")
    Jump("loc_8DE")

    label("loc_589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5F9")

    ChrTalk(
        0xFE,
        "原来如此，池钓吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "回到钓公师团的总部之后\x01",
            "就立刻去找钓鱼场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AD")

    label("loc_5F9")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "呵呵，一大早就不由自主\x01",
            "想来露天温泉泡个澡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里的浴池果然很大。\x01",
            "有点像个池塘啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，池塘吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "下次试试池钓吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AD")

    Jump("loc_8DE")

    label("loc_6B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_6BA")
    Jump("loc_8DE")

    label("loc_6BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_6C4")
    Jump("loc_8DE")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_6CE")
    Jump("loc_8DE")

    label("loc_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_772")

    ChrTalk(
        0xFE,
        (
            "虽然听说蔡斯\x01",
            "没有什么好的钓鱼场……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过说不定恰恰会有\x01",
            "没被人发现的好地方呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_826")

    label("loc_772")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "因为水泵坏了，\x01",
            "温泉可能要暂时停业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个刚从王都来的小姐\x01",
            "也很失望呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "在泵修理好之前，\x01",
            "我还是去钓鱼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_826")

    Jump("loc_8DE")

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8DE")

    ChrTalk(
        0xFE,
        (
            "钓完鱼后泡澡\x01",
            "果然是最舒服的事情的啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且还是温泉，\x01",
            "真可以说是太幸福了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊，有点奢侈的感觉呢。\x02",
    )

    CloseMessageWindow()

    label("loc_8DE")

    TalkEnd(0xFE)
    Return()

    # Function_5_568 end

    def Function_6_8E2(): pass

    label("Function_6_8E2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_8E2 end

    def Function_7_8E9(): pass

    label("Function_7_8E9")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_8E9 end

    def Function_8_8F0(): pass

    label("Function_8_8F0")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_8F0 end

    def Function_9_8F7(): pass

    label("Function_9_8F7")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_8F7 end

    def Function_10_8FE(): pass

    label("Function_10_8FE")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_8FE end

    def Function_11_905(): pass

    label("Function_11_905")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_905 end

    def Function_12_90C(): pass

    label("Function_12_90C")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_12_90C end

    def Function_13_913(): pass

    label("Function_13_913")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_913 end

    def Function_14_91A(): pass

    label("Function_14_91A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_928")
    Call(0, 16)
    Jump("loc_BC9")

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_ADE")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "女浴室\x01",
            "　需要使用的时候\x01",
            "　请通知前台。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A66")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D2")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_9D9")

    label("loc_9D2")

    TurnDirection(0x102, 0x0, 400)

    label("loc_9D9")


    ChrTalk(
        0x102,
        (
            "#010F这里就是浴室呢。\x02\x03",
            "先把行李放到房间里，\x01",
            "然后再来泡澡吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A37():
        TurnDirection(0x107, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A37)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001F嗯，好啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADB")

    label("loc_A66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7C")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_A83")

    label("loc_A7C")

    TurnDirection(0x102, 0x0, 400)

    label("loc_A83")


    ChrTalk(
        0x102,
        (
            "#010F这里就是浴室呢。\x02\x03",
            "先把行李放到房间里，\x01",
            "然后再来泡澡吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADB")

    Jump("loc_BC9")

    label("loc_ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_END)), "loc_B6A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "女浴室\x01",
            "　需要使用的时候\x01",
            "　请通知前台。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_BC9")

    label("loc_B6A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上贴着一张纸条。\x01",
            "『打扫中，停止使用』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_BC9")

    TalkEnd(0xFF)
    Return()

    # Function_14_91A end

    def Function_15_BCD(): pass

    label("Function_15_BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_BDE")
    OP_A2(0xC)
    Call(0, 16)
    Jump("loc_E7B")

    label("loc_BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 5)), scpexpr(EXPR_END)), "loc_D92")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "男浴室\x01",
            "　需要使用的时候\x01",
            "　请通知前台。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1A")
    OP_A2(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C86")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_C8D")

    label("loc_C86")

    TurnDirection(0x102, 0x0, 400)

    label("loc_C8D")


    ChrTalk(
        0x102,
        (
            "#010F这里就是浴室呢。\x02\x03",
            "先把行李放到房间里，\x01",
            "然后再来泡澡吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CEB():
        TurnDirection(0x107, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CEB)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001F嗯，好啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8F")

    label("loc_D1A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_D37")

    label("loc_D30")

    TurnDirection(0x102, 0x0, 400)

    label("loc_D37")


    ChrTalk(
        0x102,
        (
            "#010F这里就是浴室呢。\x02\x03",
            "先把行李放到房间里，\x01",
            "然后再来泡澡吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8F")

    Jump("loc_E7B")

    label("loc_D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_END)), "loc_E1C")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "男浴室\x01",
            "　需要使用的时候\x01",
            "　请通知前台。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_E7B")

    label("loc_E1C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上贴着一张纸条。\x01",
            "『打扫中，停止使用』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_E7B")

    TalkEnd(0xFF)
    Return()

    # Function_15_BCD end

    def Function_16_E7F(): pass

    label("Function_16_E7F")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "入浴\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EE0"),
        (1, "loc_110A"),
        (SWITCH_DEFAULT, "loc_110D"),
    )


    label("loc_EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_EFD")
    OP_6F(0x9, 0)
    OP_70(0x9, 0x1D)
    Sleep(200)
    Jump("loc_F10")

    label("loc_EFD")

    OP_6F(0x8, 0)
    OP_70(0x8, 0x1D)
    Sleep(200)

    label("loc_F10")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    Sleep(600)
    OP_22(0xA2, 0x0, 0x64)
    Sleep(1500)
    OP_22(0xB, 0x0, 0x64)
    Sleep(800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_FD4")
    SetChrPos(0x0, -1000, 0, -5090, 90)
    SetChrPos(0x1, -1000, 0, -5090, 90)
    SetChrPos(0x2, -1000, 0, -5090, 90)
    SetChrPos(0x3, -1000, 0, -5090, 90)
    SetChrPos(0x4, -1000, 0, -5090, 90)
    SetChrPos(0x5, -1000, 0, -5090, 90)
    SetChrPos(0x6, -1000, 0, -5090, 90)
    SetChrPos(0x7, -1000, 0, -5090, 90)
    Jump("loc_105C")

    label("loc_FD4")

    SetChrPos(0x0, -1000, 0, 4900, 90)
    SetChrPos(0x1, -1000, 0, 4900, 90)
    SetChrPos(0x2, -1000, 0, 4900, 90)
    SetChrPos(0x3, -1000, 0, 4900, 90)
    SetChrPos(0x4, -1000, 0, 4900, 90)
    SetChrPos(0x5, -1000, 0, 4900, 90)
    SetChrPos(0x6, -1000, 0, 4900, 90)
    SetChrPos(0x7, -1000, 0, 4900, 90)

    label("loc_105C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106F")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_106F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1082")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_1082")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1095")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_1095")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A8")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_10A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BB")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_10BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CE")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_10CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E1")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_10E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F4")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_10F4")

    OP_69(0x0, 0x0)
    OP_30(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_1110")

    label("loc_110A")

    Jump("loc_1110")

    label("loc_110D")

    Jump("loc_1110")

    label("loc_1110")

    OP_A3(0xC)
    TalkEnd(0xFF)
    Return()

    # Function_16_E7F end

    SaveToFile()

Try(main)
