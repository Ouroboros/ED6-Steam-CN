from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4211   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4211.x',
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
        '理查德上校',                           # 9
        '凯诺娜上尉',                           # 10
        '杜南公爵',                             # 11
        '管家菲利普',                           # 12
        '克劳斯市长',                           # 13
        '科林兹校长',                           # 14
        '玛多克工房长',                         # 15
        '莉拉',                                 # 16
        '梅贝尔市长',                           # 17
        '索蕾拉',                               # 18
        '妮舒',                                 # 19
        '布莉姆',                               # 20
        '艾科尔',                               # 21
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
        'ED6_DT07/CH02030 ._CH',             # 00
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH02140 ._CH',             # 02
        'ED6_DT07/CH02470 ._CH',             # 03
        'ED6_DT07/CH02350 ._CH',             # 04
        'ED6_DT07/CH02600 ._CH',             # 05
        'ED6_DT07/CH02620 ._CH',             # 06
        'ED6_DT07/CH02370 ._CH',             # 07
        'ED6_DT07/CH02360 ._CH',             # 08
        'ED6_DT07/CH02460 ._CH',             # 09
        'ED6_DT07/CH02230 ._CH',             # 0A
        'ED6_DT07/CH02240 ._CH',             # 0B
        'ED6_DT07/CH01350 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02030P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH02140P._CP',             # 02
        'ED6_DT07/CH02470P._CP',             # 03
        'ED6_DT07/CH02350P._CP',             # 04
        'ED6_DT07/CH02600P._CP',             # 05
        'ED6_DT07/CH02620P._CP',             # 06
        'ED6_DT07/CH02370P._CP',             # 07
        'ED6_DT07/CH02360P._CP',             # 08
        'ED6_DT07/CH02460P._CP',             # 09
        'ED6_DT07/CH02230P._CP',             # 0A
        'ED6_DT07/CH02240P._CP',             # 0B
        'ED6_DT07/CH01350P._CP',             # 0C
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1020,
        Z                   = 0,
        Y                   = 85000,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2500,
        Z                   = 0,
        Y                   = 76500,
        Direction           = 53,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 0,
        Y                   = 81150,
        Direction           = 255,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5950,
        Z                   = 0,
        Y                   = 68110,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_36A",          # 01, 1
        "Function_2_374",          # 02, 2
        "Function_3_38A",          # 03, 3
        "Function_4_503",          # 04, 4
        "Function_5_67E",          # 05, 5
        "Function_6_7A5",          # 06, 6
        "Function_7_BAC",          # 07, 7
        "Function_8_3950",         # 08, 8
        "Function_9_3994",         # 09, 9
        "Function_10_39C4",        # 0A, 10
        "Function_11_3A1C",        # 0B, 11
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2C0")
    OP_A3(0x3FA)
    Event(0, 7)

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA")
    SetChrChipByIndex(0x0, 9)
    SetChrChipByIndex(0x1, 10)
    SetChrChipByIndex(0x138, 11)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_308")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_369")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_31C")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_369")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_33A")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_369")

    label("loc_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_358")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Jump("loc_369")

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_362")
    Jump("loc_369")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_369")

    label("loc_369")

    Return()

    # Function_0_2B2 end

    def Function_1_36A(): pass

    label("Function_1_36A")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_36A end

    def Function_2_374(): pass

    label("Function_2_374")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_389")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_374")

    label("loc_389")

    Return()

    # Function_2_374 end

    def Function_3_38A(): pass

    label("Function_3_38A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_397")
    Jump("loc_4FF")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_410")

    ChrTalk(
        0xFE,
        (
            "因为诞辰庆典，\x01",
            "今天大街上很热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要不是还有工作，\x01",
            "也会出去好好玩玩的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF")

    label("loc_410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_41A")
    Jump("loc_4FF")

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_424")
    Jump("loc_4FF")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_468")

    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "茜亚和希尔丹夫人到哪儿去了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF")

    label("loc_468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_4FF")

    ChrTalk(
        0xFE,
        (
            "还要让客人们专程\x01",
            "来陪公爵他消磨时间，\x01",
            "真是够麻烦的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "明明大家都那么忙。\x02",
    )

    CloseMessageWindow()

    label("loc_4FF")

    TalkEnd(0xFE)
    Return()

    # Function_3_38A end

    def Function_4_503(): pass

    label("Function_4_503")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_510")
    Jump("loc_67A")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_51A")
    Jump("loc_67A")

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_524")
    Jump("loc_67A")

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_52E")
    Jump("loc_67A")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_598")

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "理查德上校实在是帅呆了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "和那个公爵相比\x01",
            "根本就是天壤之别嘛～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5F7")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "公爵用那双讨厌的眼睛\x01",
            "在我身上转来转去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哼，太无礼了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_5F7")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "刚才在走廊上\x01",
            "和杜南公爵擦肩而过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公爵他用\x01",
            "那双讨厌的眼睛\x01",
            "在我身上转来转去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哼，太无礼了。\x02",
    )

    CloseMessageWindow()

    label("loc_67A")

    TalkEnd(0xFE)
    Return()

    # Function_4_503 end

    def Function_5_67E(): pass

    label("Function_5_67E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_68B")
    Jump("loc_7A1")

    label("loc_68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_695")
    Jump("loc_7A1")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_69F")
    Jump("loc_7A1")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_7A1")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(
        0xFE,
        "终于结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "赶快收拾好东西，\x01",
            "早点回家去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A1")

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_7A1")

    ChrTalk(
        0xFE,
        "有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对不起呀，\x01",
            "我现在正忙着晚宴的准备工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A1")

    TalkEnd(0xFE)
    Return()

    # Function_5_67E end

    def Function_6_7A5(): pass

    label("Function_6_7A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_7B2")
    Jump("loc_BA8")

    label("loc_7B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_84B")

    ChrTalk(
        0xFE,
        (
            "特务部队的队长\x01",
            "取下面具之后，\x01",
            "真是帅呆了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "为何他要戴面具呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_900")

    label("loc_84B")


    ChrTalk(
        0xFE,
        "我悄悄对你们说哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特务部队的队长\x01",
            "取下面具之后，\x01",
            "真是帅呆了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "为何他要戴面具呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_900")

    Jump("loc_BA8")

    label("loc_903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_90D")
    Jump("loc_BA8")

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_917")
    Jump("loc_BA8")

    label("loc_917")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9AD")

    ChrTalk(
        0xFE,
        (
            "公爵喝醉之后\x01",
            "会变得更加无耻下流……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直不敢相信他和女王陛下\x01",
            "还有公主殿下是同一血脉的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5F")

    label("loc_9AD")


    ChrTalk(
        0xFE,
        "我悄悄对你们说哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "公爵喝醉之后\x01",
            "会变得更加无耻下流……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直不敢相信他和女王陛下\x01",
            "还有公主殿下是同一血脉的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5F")

    Jump("loc_BA8")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_BA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AF7")

    ChrTalk(
        0xFE,
        (
            "虽然人手已经足够了，\x01",
            "但公爵还要叫希尔丹夫人\x01",
            "不断增加侍女的数量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正他肯定是\x01",
            "不怀什么好意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA8")

    label("loc_AF7")


    ChrTalk(
        0xFE,
        "我悄悄对你们说哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然人手已经足够了，\x01",
            "但公爵还要叫希尔丹夫人\x01",
            "不断增加侍女的数量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正他肯定是\x01",
            "不怀什么好意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA8")

    TalkEnd(0xFE)
    Return()

    # Function_6_7A5 end

    def Function_7_BAC(): pass

    label("Function_7_BAC")

    EventBegin(0x0)
    OP_6D(1430, 30, 80070, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(371, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xC, -2450, 0, 82370, 90)
    SetChrPos(0xD, -2450, 0, 79820, 90)
    SetChrPos(0xE, -2450, 0, 77340, 90)
    SetChrPos(0x10, -2450, 0, 74860, 90)
    SetChrPos(0xF, -3070, 0, 74030, 90)
    SetChrPos(0x108, 2490, 0, 79820, 270)
    SetChrPos(0x102, 2490, 0, 74860, 270)
    SetChrPos(0x101, 2490, 0, 77340, 270)

    ChrTalk(
        0x101,
        (
            "#000F啊……\x01",
            "这就是晚餐会了吗？\x02\x03",
            "可是为什么餐具是摆放好了的，\x01",
            "关键的料理却没有呢？\x02\x03",
            "为何刀子和叉子\x01",
            "要这样并排放在一起呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F因为这是很正式的晚宴啊。\x02\x03",
            "先是凉菜，然后接着\x01",
            "就上各种各样的料理。\x02\x03",
            "还有就是刀子和叉子\x01",
            "要从侧边来拿着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F麻烦……\x01",
            "这就是所谓的餐桌礼仪吧。\x02\x03",
            "我还有些紧张了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F嘻嘻……\x01",
            "不用那么在意的呢。\x02\x03",
            "因为品尝料理的\x01",
            "美味才是最重要的呢。\x02\x03",
            "礼仪啊，礼貌的做法都是其次的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#600F对呀对呀。\x02\x03",
            "再说了，你们两人对\x01",
            "在场出席的各位不都是\x01",
            "很熟悉的吗。\x02\x03",
            "没有必要那么拘束嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊，说的也是啊⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F这样一来就没办法了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F嘻嘻……\x02\x03",
            "对了，那位朋友对于\x01",
            "刀子和叉子习惯吗？\x02\x03",
            "我听说东方那边\x01",
            "主要是使用筷子的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，您知道的很清楚啊。\x02\x03",
            "不过俗话说得好，\x01",
            "入乡随俗嘛。\x02\x03",
            "虽说用的不好，但还是会一点\x01",
            "用刀子和叉子的方法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F啊……很了不起呢。\x02\x03",
            "不愧是取得武术大会优胜的达人，\x01",
            "说起话来都和普通人不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈～哈～哈。\x01",
            "哪里，您过奖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（确实是对美人没有抵抗力呢……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（可是我并不觉得\x01",
            "他是一个喜好女色的人……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#800F话说回来……\x01",
            "公爵大人真慢呢。\x02\x03",
            "究竟想要做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#600F嗯……的确。\x02\x03",
            "而且如果说上座是公爵大人的，\x01",
            "那么那边的座位又是谁的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#780F是啊……\x02\x03",
            "科洛蒂娅公主座那里\x01",
            "的可能性会比较高……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -250, 0, 62670, 0)
    SetChrPos(0x9, 460, 0, 62290, 0)
    SetChrPos(0xA, -110, 0, 64099, 0)
    SetChrPos(0xB, 10, 0, 62670, 0)

    def lambda_13E7():
        OP_6D(370, 0, 72370, 3500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13E7)
    Sleep(1000)

    def lambda_1404():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1404)

    def lambda_1416():
        OP_8E(0xFE, 0xA, 0x0, 0x10586, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1416)
    WaitChrThread(0xB, 0x1)

    def lambda_1436():
        OP_8E(0xFE, 0xFFFFF772, 0x0, 0x105F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1436)
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 0, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xB,
        (
            "#720F各位……\x01",
            "让你们久等了。\x02\x03",
            "公爵大人大驾光临。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_14E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_14E7)

    def lambda_14F9():
        OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x10DE2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14F9)
    Sleep(300)

    def lambda_1519():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1519)

    def lambda_152B():
        OP_8E(0xFE, 0x438, 0x0, 0x10C3E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_152B)
    Sleep(600)

    def lambda_154B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_154B)

    def lambda_155D():
        OP_8E(0xFE, 0x190, 0x0, 0x1070C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_155D)
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#220F哎呀，诸位，\x01",
            "让你们等那么久真是不好意思。\x02\x03",
            "因为稍稍协商了一下，\x01",
            "所以拖延了一会儿时间。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(
        0xA,
        (
            "#220F这位是理查德上校。\x01",
            "王国军情报部的负责人。\x02\x03",
            "为了解决恐怖事件，\x01",
            "他日夜操劳，尽心尽力，\x01",
            "作为礼节我就邀请他来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)

    ChrTalk(
        0x8,
        (
            "#110F初次与大家见面。\x01",
            "我是王国军情报部的理查德。\x02\x03",
            "承蒙公爵大人的好意，\x01",
            "邀请我来参加晚宴。\x02\x03",
            "这身与这里不相称的军服有些失礼了，\x01",
            "但还请允许我与各位同席。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0xA)
    Sleep(300)
    Sleep(100)

    def lambda_17C7():
        OP_6D(330, 60, 81510, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17C7)
    OP_43(0x8, 0x1, 0x0, 0x8)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0xB)
    Sleep(200)
    OP_43(0x9, 0x1, 0x0, 0x9)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#000F（竟、竟然会和上校一起\x01",
            "在餐桌上用餐……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（虽然猜到了几分，\x01",
            "但果然还是些紧张……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(50, 1210, 79220, 0)
    OP_67(0, 2920, -10000, 0)
    OP_6B(2090, 0)
    OP_6C(0, 0)
    OP_6E(424, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#220F哈～哈～哈，哎呀，愉快愉快。\x02\x03",
            "怎么样，梅贝尔市长。\x01",
            "王城格兰赛尔这儿的厨艺如何？\x02\x03",
            "与柏斯的『安特洛丝』\x01",
            "相比也毫不逊色对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F嗯，很精妙的厨艺呢。\x02\x03",
            "搭配上葡萄酒可以说是完美了，\x01",
            "出乎预料的出类拔萃呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F哈～哈～哈，既然都这么说\x01",
            "肯定就不是吹牛的了。\x02\x03",
            "如何，你是叫金对吧，\x01",
            "东方人对于这些感觉不大合胃口吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哪里，非常美味啊。\x02\x03",
            "虽说在下的舌头很迟钝，\x01",
            "但也感觉得出其中蕴涵的美味。\x02\x03",
            "品味出了利贝尔\x01",
            "料理的精髓所在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F嗯嗯，说得好。\x02\x03",
            "怎么样啊，两位年轻的游击士？\x02\x03",
            "这样豪华的料理\x01",
            "今天还是第一次吃到吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔－嗯，的确\x01",
            "非常非常美味啊。\x02\x03",
            "邀请的人姑且不论如何，\x01",
            "就这个料理真的很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F哈～哈～哈。\x01",
            "说的好，说的好啊……\x02\x03",
            "……嗯？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F哦，实在是\x01",
            "很棒的料理呢。\x02\x03",
            "而且至今为止我们还没有\x01",
            "这样正式的被邀请入席的机会，\x01",
            "还很是有些不习惯呢。\x02\x03",
            "承蒙您的款待，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F哈～哈～哈。\x01",
            "你很会说话嘛。\x02\x03",
            "不过经管家的提醒，\x01",
            "我总算是想起来了……\x02\x03",
            "你们两位曾经在卢安的事件中\x01",
            "和我见过一面。\x02\x03",
            "缘分这个东西真是奇妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哈、哈哈……是－是呀。\x02\x03",
            "（管家没有提醒之前\x01",
            "难道就没有想起来吗……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F好啊，今晚不醉不归！\x02\x03",
            "料理和酒都是绰绰有余，\x01",
            "不用有顾虑，想吃就尽管说！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F公爵大人……\x02\x03",
            "我们把之前谈到的内容\x01",
            "先了结了如何呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F……哦哦！\x01",
            "对啊，还有那些内容呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F事实上把作为王国代表的诸位\x01",
            "集中在这里没有什么别的意思……\x02\x03",
            "就是借这个晚宴的机会\x01",
            "宣布一件重要的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#600F重大的事情……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#800F这究竟……\x01",
            "是什么样的事情呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F嗯。\x02\x03",
            "在这里先由理查德上校\x01",
            "替我说明相关内容。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F……惶恐之至。\x02\x03",
            "女王陛下身体欠佳，\x01",
            "是各位之前已知的事实。\x02\x03",
            "不过陛下正在缓缓的康复中，\x01",
            "很快就会以健康的状态与人民见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#600F哦……这就好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F那去探望陛下\x01",
            "也是可以的了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F真对不起，照陛下的意向，\x01",
            "还是希望暂时先谢绝探望。\x02\x03",
            "然而这几天扰乱王都周边\x01",
            "秩序的恐怖组织，要先予以铲除。\x02\x03",
            "这件事成功之后，女王陛下\x01",
            "的诞辰庆典才能按预定顺利进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#780F嗯……这样能让市民们\x01",
            "安居乐业，愉快的生活，\x01",
            "真是值得庆贺的事啊。\x02\x03",
            "不过，想要说的\x01",
            "应该不止是这些吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#800F……是啊，如果只是这些的话，\x01",
            "联络我们并说明就可以了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F呵呵，能察觉到就好啊。\x02\x03",
            "女王陛下的健康状况正在恢复，\x01",
            "之前也已经说到了……\x02\x03",
            "陛下因为这次身体欠佳\x01",
            "而下了一个决定。\x02\x03",
            "那个决定就是——\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F陛下自身退位，让在座的\x01",
            "杜南公爵大人继承王位。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)
    OP_62(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0xE,
        "#800F什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#610F真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（约修亚，这是……！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯……\x01",
            "阴谋终于浮出水面了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F……我虽比较愚钝，\x01",
            "不过很意外，陛下并没有轻视我。\x02\x03",
            "并非是勉强，在这近４０年间，\x01",
            "经历了动荡时期的利贝尔\x01",
            "都是由一位女性来领导的。\x02\x03",
            "基于这一点，在诞辰庆典之后\x01",
            " \x02\x03",
            "转交王位的继承权\x01",
            "的决定就是出于这样的原因。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#600F竟然……陛下一直为此\x01",
            "而深感苦恼……\x02\x03",
            "每年见到她的时候\x01",
            "都没能感觉到，是我们的不对啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F可、可是……\x01",
            "怎能在这样一个觥筹交错的宴席\x01",
            "宣布如此重大的决议呢。\x02\x03",
            "冒昧的问一句，这些究竟\x01",
            "算不算数呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#220F唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F哼哼，梅贝尔市长。\x02\x03",
            "大人的话毫无信用可言，\x01",
            "……这就你的本意吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#610F我、我没有那么说过！\x02\x03",
            "可是通过市长的选举\x01",
            "来表决王位的继承人\x01",
            "的这项程序竟然会没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#800F是啊……\x02\x03",
            "可以的话，我们想直接\x01",
            "向陛下询问一下刚才那些决议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#220F呜、呜－嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F各位的情绪动摇我很理解。\x02\x03",
            "不过还请冷静下来，\x01",
            "暂且先知道就可以了。\x02\x03",
            "更进一步的来说，\x01",
            "在诞辰庆典时将会由陛下自身\x01",
            "来公布这项决议。\x02\x03",
            "是真是假到那时就可以\x01",
            "见分晓了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#800F这、这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F问题在于公布这项决议时\x01",
            "会给普通市民带来什么样的影响。\x02\x03",
            "为了避免无益的混乱，\x01",
            "所以才把各地的负责人也就是在座的\x01",
            "各位召集到这里来传达这项决议……\x02\x03",
            "公爵大人也是这么认为的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F咳咳……\x01",
            "嗯，就是这样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F而且陛下如果退位了的话，\x01",
            "这个消息肯定不止是滞留在国内。\x02\x03",
            "大陆各国，尤其是作为威胁的北方\x01",
            "埃雷波尼亚肯定会注意到这个变动。\x02\x03",
            "正因为如此，在座的各位\x01",
            "应该扶植新的国王陛下，\x01",
            "如果不团结起来是绝对不行的……\x02\x03",
            "特别是在这样一个关键时期即将来临的时刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(
        0x101,
        (
            "#000F（居、居然说的如此\x01",
            "冠冕堂皇……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（嗯……\x01",
            "好一个煽动者啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE)

    ChrTalk(
        0xE,
        (
            "#800F正式的决定可以在诞辰庆典时\x01",
            "向陛下直接请示……\x02\x03",
            "不过要事先做好心里准备，\x01",
            "就是这样的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F哼哼……\x01",
            "能够理解真是万幸啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC)

    ChrTalk(
        0xC,
        (
            "#600F唔－嗯……\x02\x03",
            "一旦这件事情落实了，\x01",
            "我们就有的忙碌了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10)

    ChrTalk(
        0x10,
        (
            "#610F是呢……\x01",
            "还要向市民们宣布。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD)

    ChrTalk(
        0xD,
        "#780F……我还有一事相问。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#780F公爵大人具有王位的继承权\x01",
            "这点我也承认……\x02\x03",
            "我认为具有同样资格的继承者\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#220F这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F还有陛下的孙女\x01",
            "科洛蒂娅殿下。\x02\x03",
            "的确，依据王室典范的规定，\x01",
            "她和公爵大人拥有同等资格……\x02\x03",
            "因为她的年纪还比较小，\x01",
            "所以陛下就推选了公爵大人。\x02\x03",
            "而且之前也说到过……\x01",
            "对于女性都过于沉重的责任\x01",
            "要一位小姑娘来承担是不行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F对呀对呀，就是这样的！\x02\x03",
            "对了，正在打算为科洛蒂娅\x01",
            "公主寻找良缘佳偶。\x02\x03",
            "虽然是非正式的，但是之前其他国家\x01",
            "的王家已经提出过了相关的事宜……\x02\x03",
            "如果可能的话准备在\x01",
            "今年年中实现这个婚约。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#610F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#780F……唔，您说的话我明白了。\x02\x03",
            "这么以来就可以让\x01",
            "好事成双了对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#600F唔……公主殿下……\x02\x03",
            "要此时结婚似乎\x01",
            "也太过年幼了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F……打搅一下。\x01",
            "我问个问题好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F金、金大哥？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#220F呵……？\x02\x03",
            "没关系，但说无妨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F很抱歉，但刚才听到的那番话，\x01",
            "对于我们这几个与此事无关的人\x01",
            "是不应该提及的。\x02\x03",
            "况且我并非是王国的国民。\x02\x03",
            "因此，为何还要特地要在\x01",
            "这样的酒席间发表决议呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F这是因为取得优胜的几位\x01",
            "恰好就是游击士的缘故。\x02\x03",
            "陛下退位这个重大的事情\x01",
            "也要传达给游击士协会。\x02\x03",
            "所以我才给公爵提议\x01",
            "让你们得知这件事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F原来如此……\x02\x03",
            "在利贝尔军队和协会\x01",
            "有着良好的关系的传言\x01",
            "看来果真不假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#110F哈哈，和帝国及共和国相比，\x01",
            "我国的军力不是很充实。\x02\x03",
            "只有携起手来，\x01",
            "才能面对苛刻的现实……\x02\x03",
            "总之就是这样的，\x01",
            "你明白其中的意思了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F呼……明白了。\x02\x03",
            "我会把今天从宴席中得知的情况\x01",
            "转达给王都支部的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4222   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_BAC end

    def Function_8_3950(): pass

    label("Function_8_3950")

    OP_8E(0xFE, 0x10D6, 0x0, 0x10FC2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1176, 0x0, 0x14460, 0xBB8, 0x0)
    OP_8E(0xFE, 0x9F6, 0x0, 0x141B8, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_8_3950 end

    def Function_9_3994(): pass

    label("Function_9_3994")

    OP_8E(0xFE, 0x10D6, 0x0, 0x10FC2, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1176, 0x0, 0x14460, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_3994 end

    def Function_10_39C4(): pass

    label("Function_10_39C4")

    OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x117EC, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEF48, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFBFA, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xA, 0x0, 0x14C08, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 0)
    Return()

    # Function_10_39C4 end

    def Function_11_3A1C(): pass

    label("Function_11_3A1C")

    OP_8E(0xFE, 0xFFFFEEE4, 0x0, 0x117EC, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEF48, 0x0, 0x14D02, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFFC72, 0x0, 0x15126, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_11_3A1C end

    SaveToFile()

Try(main)
