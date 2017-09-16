from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3233   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3233.x',
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
        '艾丝蒂尔的篮子',                       # 20
        '提妲的篮子',                           # 21
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
        'ED6_DT07/CH02300 ._CH',             # 00
        'ED6_DT07/CH02310 ._CH',             # 01
        'ED6_DT07/CH02290 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01270 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01120 ._CH',             # 07
        'ED6_DT07/CH01130 ._CH',             # 08
        'ED6_DT07/CH01160 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01060 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
        'ED6_DT06/CH20021 ._CH',             # 0E
        'ED6_DT06/CH20145 ._CH',             # 0F
        'ED6_DT06/CH20146 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02300P._CP',             # 00
        'ED6_DT07/CH02310P._CP',             # 01
        'ED6_DT07/CH02290P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01270P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01120P._CP',             # 07
        'ED6_DT07/CH01130P._CP',             # 08
        'ED6_DT07/CH01160P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01060P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
        'ED6_DT06/CH20021P._CP',             # 0E
        'ED6_DT06/CH20145P._CP',             # 0F
        'ED6_DT06/CH20146P._CP',             # 10
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
        TalkScenaIndex      = 5,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1245198,
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
        Unknown3            = 1310734,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_31A",          # 00, 0
        "Function_1_3B4",          # 01, 1
        "Function_2_3BF",          # 02, 2
        "Function_3_3D5",          # 03, 3
        "Function_4_433",          # 04, 4
        "Function_5_577",          # 05, 5
        "Function_6_793",          # 06, 6
        "Function_7_79A",          # 07, 7
        "Function_8_7A1",          # 08, 8
        "Function_9_7A8",          # 09, 9
        "Function_10_7AF",         # 0A, 10
        "Function_11_7B6",         # 0B, 11
        "Function_12_7BD",         # 0C, 12
        "Function_13_7C4",         # 0D, 13
        "Function_14_7CB",         # 0E, 14
        "Function_15_1F27",        # 0F, 15
        "Function_16_1FC7",        # 10, 16
    )


    def Function_0_31A(): pass

    label("Function_0_31A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_324")
    Jump("loc_3B3")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_3B3")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_34E")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1080, 0, 440, 85)
    Jump("loc_3B3")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_36E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1090, 0, -900, 82)
    Jump("loc_3B3")

    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_378")
    Jump("loc_3B3")

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_382")
    Jump("loc_3B3")

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_38C")
    Jump("loc_3B3")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_396")
    Jump("loc_3B3")

    label("loc_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B3")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1090, 0, -900, 82)

    label("loc_3B3")

    Return()

    # Function_0_31A end

    def Function_1_3B4(): pass

    label("Function_1_3B4")

    OP_72(0x8, 0x10)
    OP_72(0x9, 0x10)
    Return()

    # Function_1_3B4 end

    def Function_2_3BF(): pass

    label("Function_2_3BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3BF")

    label("loc_3D4")

    Return()

    # Function_2_3BF end

    def Function_3_3D5(): pass

    label("Function_3_3D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3E2")
    Jump("loc_42F")

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3EC")
    Jump("loc_42F")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3F6")
    Jump("loc_42F")

    label("loc_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_400")
    Jump("loc_42F")

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_40A")
    Jump("loc_42F")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_414")
    Jump("loc_42F")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_41E")
    Jump("loc_42F")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_428")
    Jump("loc_42F")

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42F")

    label("loc_42F")

    TalkEnd(0xFE)
    Return()

    # Function_3_3D5 end

    def Function_4_433(): pass

    label("Function_4_433")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_440")
    Jump("loc_573")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_44A")
    Jump("loc_573")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4C6")

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
    Jump("loc_573")

    label("loc_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4D0")
    Jump("loc_573")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_54E")

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
    Jump("loc_573")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_558")
    Jump("loc_573")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_562")
    Jump("loc_573")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_56C")
    Jump("loc_573")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_573")

    label("loc_573")

    TalkEnd(0xFE)
    Return()

    # Function_4_433 end

    def Function_5_577(): pass

    label("Function_5_577")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_584")
    Jump("loc_78F")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_58E")
    Jump("loc_78F")

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_598")
    Jump("loc_78F")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_608")

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
    Jump("loc_6BC")

    label("loc_608")

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

    label("loc_6BC")

    Jump("loc_78F")

    label("loc_6BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_6C9")
    Jump("loc_78F")

    label("loc_6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_6D3")
    Jump("loc_78F")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_6DD")
    Jump("loc_78F")

    label("loc_6DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6E7")
    Jump("loc_78F")

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_78F")

    ChrTalk(
        0xFE,
        (
            "从大白天开始\x01",
            "就一直泡澡，\x01",
            "这可是温泉的绝妙之处啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀，从温泉出来的时候\x01",
            "迎面吹来的风真是清爽啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78F")

    TalkEnd(0xFE)
    Return()

    # Function_5_577 end

    def Function_6_793(): pass

    label("Function_6_793")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_793 end

    def Function_7_79A(): pass

    label("Function_7_79A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_79A end

    def Function_8_7A1(): pass

    label("Function_8_7A1")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_7A1 end

    def Function_9_7A8(): pass

    label("Function_9_7A8")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_7A8 end

    def Function_10_7AF(): pass

    label("Function_10_7AF")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_7AF end

    def Function_11_7B6(): pass

    label("Function_11_7B6")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_7B6 end

    def Function_12_7BD(): pass

    label("Function_12_7BD")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_12_7BD end

    def Function_13_7C4(): pass

    label("Function_13_7C4")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_7C4 end

    def Function_14_7CB(): pass

    label("Function_14_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F26")
    EventBegin(0x0)
    OP_A2(0x528)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B3")
    Fade(1000)
    OP_6D(-1360, 0, 5070, 0)
    SetChrPos(0x101, -150, 0, 4200, 270)
    SetChrPos(0x102, -800, 0, 3380, 0)
    SetChrPos(0x107, -580, 0, 5360, 270)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "这里就是澡堂的入口吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯，这里是女浴室，\x01",
            "那边的是男浴室。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99F")

    label("loc_8B3")

    Fade(1000)
    OP_6D(-1360, 0, -4840, 0)
    SetChrPos(0x101, -150, 0, -5600, 270)
    SetChrPos(0x102, -800, 0, -6530, 0)
    SetChrPos(0x107, -580, 0, -4450, 270)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#000F嗯……\x01",
            "这里就是澡堂的入口吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x107,
        (
            "#065F艾、艾丝蒂尔姐姐。\x01",
            "这边是男浴室。\x02\x03",
            "前面那个才是女浴室呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99F")


    ChrTalk(
        0x101,
        (
            "#004F啊，原来是这样啊。\x01",
            "男女分开的啊。\x02\x03",
            "#001F哈哈，不过那也是当然的。\x01",
            "因为要换衣服嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F咳咳……\x02\x03",
            "#010F那样的话，\x01",
            "我们要暂时分开一会儿了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#001F嗯，待会见⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F失陪了～\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-32439, 0, 28640, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, -31500, 1300, 29300, 0)
    SetChrPos(0x14, -30300, 1300, 29300, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1500)
    Fade(1000)
    OP_6D(-63400, -750, 28960, 0)
    SetChrPos(0x107, -65290, -550, 25260, 90)
    SetChrPos(0x101, -64140, -550, 26490, 180)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x107, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrChipByIndex(0x101, 15)
    SetChrChipByIndex(0x107, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x107, 0)
    OP_22(0xA2, 0x0, 0x64)
    OP_22(0x1C7, 0x1, 0x64)
    OP_6D(-65690, -750, 27830, 3000)
    Sleep(400)
    OP_99(0x101, 0x0, 0x2, 0x320)
    OP_99(0x101, 0x2, 0x1, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#378F#2P呼～真是享受啊，享受。\x02\x03",
            "这还是我第一次泡温泉呢，\x01",
            "真是出乎意料的舒服。\x02\x03",
            "#443F虽然没到朵洛希那样痴迷的程度，\x01",
            "但还真是挺容易上瘾的哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 7)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#391F#5P呵呵……\x01",
            "其实我的瘾也挺大的哦。\x02\x03",
            "从我还小的时候开始，\x01",
            "爷爷就经常带我来这里泡温泉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 3)
    Sleep(400)

    ChrTalk(
        0x101,
        "#370F#2P是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0xC8, 1600, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0x101, 0x3, 0x5, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        "#374F#4P咦，那个门是做什么用的？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 1)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#390F#6P啊，刚才不是说过吗，\x01",
            "那扇门是连着露天温泉的。\x02\x03",
            "里面可是很大的，\x01",
            "大概可以十个人一起泡哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#370F#4P哎～是这样啊～……\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x5, 0x3, 0x320)
    Sleep(100)
    SetChrSubChip(0x101, 6)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#377F#2P呼～这样泡一下，\x01",
            "感觉之前旅行的疲劳都释放了出来～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 7)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#390F#5P艾丝蒂尔姐姐，\x01",
            "你们是徒步旅行的吗？\x02\x03",
            "为什么不搭乘定期船呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x3, 0x2, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#442F#2P嗯……算是为了修行吧。\x02\x03",
            "#442F#2P还有……\x01",
            "用老爸的话来说，\x01",
            "是为了获得在各地修行时的阅历吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0x7, 0x9, 0x4B0)
    OP_99(0x107, 0x9, 0x7, 0x4B0)
    OP_99(0x107, 0x7, 0x9, 0x4B0)
    OP_99(0x107, 0x9, 0x7, 0x4B0)
    Sleep(400)

    ChrTalk(
        0x107,
        "#393F#5P卡西乌斯叔叔……？\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x2, 0x4, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#376F#2P老爸的徒弟雪拉扎德\x01",
            "这样对我和约修亚说的。\x02\x03",
            "因为老爸以前劝导雪拉姐\x01",
            "在修行的时候一定要徒步旅行。\x02\x03",
            "要守护一片土地，\x01",
            "首先就要自己脚踏实地去看一看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#396F#5P哇，好帅呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#378F#2P虽然老爸平时总是爱开玩笑，\x01",
            "不过关键时刻还是挺靠得住的。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x4, 0x3, 0x320)
    Sleep(100)
    SetChrSubChip(0x101, 6)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#377F#2P唉……\x01",
            "不知他现在又跑到哪里去了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#392F#5P……艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x3, 0x4, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#443F#2P啊哈哈，不好意思，\x01",
            "这话题好像沉重了点。\x02\x03",
            "#376F#2P不过，游击士为了修行，\x01",
            "总不能担心这个那个的而停滞不前吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x4, 0x0, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#440F#2P现在能做到的……\x01",
            "嗯……只有相信老爸他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#393F#5P相信……\x02\x03",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0xC8, 1600, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_99(0x101, 0x0, 0x4, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x101,
        "#370F#2P咦，怎么了？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 2)
    Sleep(80)
    SetChrSubChip(0x107, 3)
    Sleep(80)
    SetChrSubChip(0x107, 2)
    Sleep(80)
    SetChrSubChip(0x107, 4)
    Sleep(80)
    SetChrSubChip(0x107, 2)
    Sleep(80)
    SetChrSubChip(0x107, 3)
    Sleep(80)
    SetChrSubChip(0x107, 2)
    Sleep(80)
    SetChrSubChip(0x107, 4)
    Sleep(80)
    SetChrSubChip(0x107, 2)
    Sleep(400)

    ChrTalk(
        0x107,
        "#390F#5P不，没什么。\x02",
    )

    CloseMessageWindow()
    OP_99(0x107, 0x9, 0x7, 0x320)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#396F#5P啊……对了！\x02\x03",
            "我有一个问题\x01",
            "想问艾丝蒂尔姐姐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#370F#2P有问题要问我？\x02\x03",
            "什么什么？\x01",
            "问什么都可以哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#395F#5P嗯嗯，就是～～那个……\x02\x03",
            "艾丝蒂尔姐姐和约修亚哥哥\x01",
            "是不是已经结婚了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#371F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#396F#5P……（紧张紧张）\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x101, 9)
    OP_0D()
    OP_99(0x101, 0x9, 0x7, 0x320)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#370F#2P哎，不好意思。\x01",
            "刚才没听清楚你说的那句话。\x02\x03",
            "我和约修亚怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0x7, 0x5, 0x320)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#397F#5P啊～嗯，人家是说……\x01",
            "你们俩是不是已经结婚了～\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(
        0x101,
        "#374F#2P怎、怎、怎……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        "#372F#2P#3S怎么会有这种想法！？\x02",
    )

    SetChrSubChip(0x101, 10)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_99(0x107, 0x7, 0x9, 0x514)
    OP_99(0x107, 0x9, 0x7, 0x514)
    OP_99(0x107, 0x7, 0x9, 0x514)
    OP_99(0x107, 0x9, 0x7, 0x514)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#394F#5P因、因为你们用同一个姓氏啊……\x02\x03",
            "而且你们的长相又不像兄妹，\x01",
            "我还以为一定是……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 11)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#444F#2P长、长相不像是因为\x01",
            "我们没有血缘关系啦！\x02\x03",
            "姓氏相同是因为\x01",
            "约修亚是老爸的养子啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#393F#5P啊，原来是这样啊……\x02\x03",
            "#395F嘿嘿，对不起。\x01",
            "我之前一直误会你们俩是……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 12)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#377F#2P根、根本就是天大的误会……\x02\x03",
            "而且……\x01",
            "我和约修亚都只有１６岁。\x02\x03",
            "结婚什么的还早得很呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#395F#5P说、说的也是啊。\x02\x03",
            "无论两人怎样喜欢对方，\x01",
            "都不能这么早就结婚的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#377F#2P……（晕倒）\x02",
    )

    SetChrSubChip(0x101, 13)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#375F#2P#3S都、都说了嘛！\x01",
            "我和约修亚根本\x01",
            "就不是什么恋人啦！\x02",
        )
    )

    SetChrSubChip(0x101, 14)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#375F#2P#3S只是家人啦，家人！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_99(0x107, 0xA, 0xC, 0x3E8)
    OP_99(0x107, 0xC, 0xA, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x107,
        "#394F#5P是、是这样吗！？\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0xE, 0x10, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#377F#2P当然是这样啦……\x02\x03",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 11)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#444F#2P那个，提妲。\x02\x03",
            "我和约修亚之间……\x01",
            "看起来像那样的关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#393F#5P那样的关系？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 17)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#441F#2P就、就是说……\x01",
            "恋、恋人那样的……关系啦。\x02\x03",
            "爱意浓浓、情意绵绵……\x01",
            "如胶似漆、难舍难分……之类的啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0xB, 0xC, 0x320)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#395F#5P啊……\x01",
            "倒没那样的感觉呢。\x02\x03",
            "可是可是，你们总是在一起，\x01",
            "相处得又那么自然、那么温馨，\x01",
            "感觉两人好像彼此都互通心意似的……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 10)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#442F#2P唔，如果是你说的那样，\x01",
            "倒是可能有那么的一点……\x02\x03",
            "可是这种……\x01",
            "不是家人或亲友间的关系吗？\x02\x03",
            "也许，我和约修亚之间\x01",
            "真的一直都是那样的关系……\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x40029, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_AD(0x40027, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_AD(0x4002A, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_AD(0x40028, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_AD(0x4002B, 0x0, 0x0, 0x1F4)
    Sleep(1200)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_AE(0x1F4)
    Sleep(500)
    OP_62(0x101, 0xC8, 1600, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#375F#2P#3S（呀！我在想什么呀～！）\x02",
    )

    SetChrSubChip(0x101, 19)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrSubChip(0x101, 18)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#441F#2P（这么说，到现在为止，\x01",
            "　我竟然连那样令人害羞的事都坦然地……）\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x107, 0xB, 0xA, 0x320)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#393F#5P？？？\x02\x03",
            "艾丝蒂尔姐姐？\x01",
            "你的脸……好红呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0xC, 0xA, 0x3E8)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#378F#2P咦咦咦咦……\x01",
            "没什么啦，什么都没有！\x02\x03",
            "哎呀～话说回来，\x01",
            "这里的温泉真的很舒服不是吗！？\x02\x03",
            "不过对血液循环的促进过于有效了吧。\x01",
            "头开始有点晕乎乎的了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#393F#5P是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#371F#2P说、说起来，\x01",
            "外面就是露天澡堂是吧？\x02\x03",
            "头有点晕了，\x01",
            "我稍微出去散步一下哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#393F#5P啊，好……\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xF)
    SetChrSubChip(0x107, 1)
    Sleep(500)

    ChrTalk(
        0x107,
        (
            "#393F#3P啊，对了……\x01",
            "艾丝蒂尔姐姐，露天澡堂是……\x02\x03",
            "#394F#3P男女混浴……的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E85")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_1E85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E98")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_1E98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAB")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_1EAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EBE")
    OP_31(0x3, 0xFB, 0x0)

    label("loc_1EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED1")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_1ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EE4")
    OP_31(0x4, 0xFB, 0x0)

    label("loc_1EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF7")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_1EF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0A")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_1F0A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x10000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1F26")

    Return()

    # Function_14_7CB end

    def Function_15_1F27(): pass

    label("Function_15_1F27")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    OP_96(0xFE, 0xFFFF0736, 0x0, 0x6C7A, 0x4B0, 0x1770)
    OP_8E(0xFE, 0xFFFEFE80, 0xFA, 0x7134, 0x1388, 0x0)
    OP_8C(0xFE, 270, 800)
    OP_70(0x6, 0x3C)
    Sleep(60)
    OP_8E(0x101, 0xFFFEF7A0, 0x0, 0x72CE, 0x1388, 0x0)
    Sleep(500)
    OP_72(0x6, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    Return()

    # Function_15_1F27 end

    def Function_16_1FC7(): pass

    label("Function_16_1FC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FE5")
    OP_99(0xFE, 0xE, 0x10, 0x514)
    OP_99(0xFE, 0x10, 0xF, 0x514)
    Jump("Function_16_1FC7")

    label("loc_1FE5")

    Return()

    # Function_16_1FC7 end

    SaveToFile()

Try(main)
