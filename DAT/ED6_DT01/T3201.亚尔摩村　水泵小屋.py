from ED6ScenarioHelper import *

def main():
    # 亚尔摩村　水泵小屋

    CreateScenaFile(
        FileName            = 'T3201   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3201.x',
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
        '朵洛希',                               # 9
        '毛婆婆',                               # 10
        '拜舍尔',                               # 11
        '艾德',                                 # 12
        '林',                                   # 13
        '莉西亚',                               # 14
        '希利尔',                               # 15
        '艾缇',                                 # 16
        '拉克',                                 # 17
        '希玛',                                 # 18
        '库安',                                 # 19
        '西加罗',                               # 20
        '艾德尔',                               # 21
        '托兰特平原道方向',                     # 22
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02430 ._CH',             # 01
        'ED6_DT07/CH02300 ._CH',             # 02
        'ED6_DT07/CH02310 ._CH',             # 03
        'ED6_DT07/CH02290 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01270 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01150 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01130 ._CH',             # 0A
        'ED6_DT07/CH01160 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH01060 ._CH',             # 0D
        'ED6_DT07/CH01040 ._CH',             # 0E
        'ED6_DT07/CH01210 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02430P._CP',             # 01
        'ED6_DT07/CH02300P._CP',             # 02
        'ED6_DT07/CH02310P._CP',             # 03
        'ED6_DT07/CH02290P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01270P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01150P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01130P._CP',             # 0A
        'ED6_DT07/CH01160P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH01060P._CP',             # 0D
        'ED6_DT07/CH01040P._CP',             # 0E
        'ED6_DT07/CH01210P._CP',             # 0F
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
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -30790,
        Z                   = -2000,
        Y                   = 15330,
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


    DeclEvent(
        X                   = 28950,
        Y                   = 1000,
        Z                   = 4030,
        Range               = 2500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 980,
        Y                   = -250,
        Z                   = 18420,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 42330,
        Y                   = 5750,
        Z                   = 36020,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )


    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 6000,
        TriggerY            = 49730,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 7000,
        ActorY              = 49730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 42130,
        TriggerZ            = 0,
        TriggerY            = -860,
        TriggerRange        = 1250,
        ActorX              = 44880,
        ActorZ              = 3000,
        ActorY              = 1020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_614",          # 01, 1
        "Function_2_665",          # 02, 2
        "Function_3_67B",          # 03, 3
        "Function_4_8F2",          # 04, 4
        "Function_5_B1D",          # 05, 5
        "Function_6_C47",          # 06, 6
        "Function_7_C4E",          # 07, 7
        "Function_8_C55",          # 08, 8
        "Function_9_10E2",         # 09, 9
        "Function_10_10E9",        # 0A, 10
        "Function_11_10F0",        # 0B, 11
        "Function_12_1508",        # 0C, 12
        "Function_13_150F",        # 0D, 13
        "Function_14_1916",        # 0E, 14
        "Function_15_1F7A",        # 0F, 15
        "Function_16_3683",        # 10, 16
        "Function_17_36D2",        # 11, 17
        "Function_18_380F",        # 12, 18
        "Function_19_38A8",        # 13, 19
        "Function_20_38AC",        # 14, 20
        "Function_21_38B0",        # 15, 21
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3A0")
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_3A0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_3AC"),
        (SWITCH_DEFAULT, "loc_3C2"),
    )


    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BF")
    OP_A2(0x527)
    Event(0, 14)

    label("loc_3BF")

    Jump("loc_3C2")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_40E")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 30590, 4500, 35260, 249)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 28630, 4000, 36530, 176)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 28800, 4000, 33220, 0)
    Jump("loc_613")

    label("loc_40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_45A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 41610, 6000, 48020, 219)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 9750, 2000, 15450, 181)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 9820, 2000, 13580, 351)
    Jump("loc_613")

    label("loc_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4A6")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39080, 6000, 47390, 7)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 40560, 6000, 47840, 342)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 39640, 6000, 44670, 353)
    Jump("loc_613")

    label("loc_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4B0")
    Jump("loc_613")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4E6")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 47620, 0, 7310, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 48380, 0, 7130, 180)
    Jump("loc_613")

    label("loc_4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_51C")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16830, 2500, 13990, 11)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 39080, 6000, 47390, 7)
    Jump("loc_613")

    label("loc_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_568")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 13770, 2500, 18660, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 17190, 2500, 13960, 351)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 15890, 2500, 13840, 32)
    Jump("loc_613")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5CA")
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 13770, 2500, 18660, 90)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 13780, 2500, 19720, 153)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 17190, 2500, 13960, 351)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 15890, 2500, 13840, 32)
    Jump("loc_613")

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_613")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 13400, 2500, 18050, 224)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 14390, 2500, 16520, 263)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 12490, 2000, 16460, 41)

    label("loc_613")

    Return()

    # Function_0_392 end

    def Function_1_614(): pass

    label("Function_1_614")

    OP_16(0x2, 0xFA0, 0xFFFE8130, 0xFFFE5E08, 0x30054)
    OP_72(0xB, 0x10)
    OP_1B(0x0, 0x0, 0x11)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_644")
    OP_28(0x2A, 0x1, 0x800)

    label("loc_644")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2E, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_664")
    OP_65(0x1, 0x1)

    label("loc_664")

    Return()

    # Function_1_614 end

    def Function_2_665(): pass

    label("Function_2_665")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_665")

    label("loc_67A")

    Return()

    # Function_2_665 end

    def Function_3_67B(): pass

    label("Function_3_67B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_688")
    Jump("loc_8EE")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_692")
    Jump("loc_8EE")

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_8EE")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6A6")
    Jump("loc_8EE")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_70E")

    ChrTalk(
        0xFE,
        (
            "月光映照下的\x01",
            "东方风格的庭园……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，简直就像梦幻一样啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EE")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_791")

    ChrTalk(
        0xFE,
        "唔～我想去后山看看啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村子里都已经\x01",
            "没有可以去探险的地方了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_824")

    label("loc_791")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "这里面的后山\x01",
            "好像有温泉的源头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我很想去看看，\x01",
            "但是村民不允许进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_824")

    Jump("loc_8EE")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_831")
    Jump("loc_8EE")

    label("loc_831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_8E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_87E")

    ChrTalk(
        0xFE,
        (
            "啊，\x01",
            "那个好像是特产店啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，虽然我有点心急，\x01",
            "不过现在就想去看一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E4")

    label("loc_87E")

    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "如我所料，\x01",
            "这是个恬静的温泉胜地啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "到处都是东方的风格，\x01",
            "也让人感到很新鲜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E4")

    Jump("loc_8EE")

    label("loc_8E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8EE")

    label("loc_8EE")

    TalkEnd(0xFE)
    Return()

    # Function_3_67B end

    def Function_4_8F2(): pass

    label("Function_4_8F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8FF")
    Jump("loc_B19")

    label("loc_8FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_909")
    Jump("loc_B19")

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_913")
    Jump("loc_B19")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_91D")
    Jump("loc_B19")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_9F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(
        0xFE,
        (
            "在温泉里泡得有点晕，\x01",
            "吹吹夜晚的冷气真是舒服啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F4")

    label("loc_964")

    OP_A2(0x9)

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
            "能把讨厌的事都抛在脑后。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F4")

    Jump("loc_B19")

    label("loc_9F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_A01")
    Jump("loc_B19")

    label("loc_A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_A0B")
    Jump("loc_B19")

    label("loc_A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_A3F")

    ChrTalk(
        0xFE,
        "哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "艾德尔那家伙\x01",
            "到底跑到哪儿去了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B19")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A8A")

    ChrTalk(
        0xFE,
        (
            "哎呀，能来这里真是好啊。\x01",
            "这个温泉好像能治病呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B19")

    label("loc_A8A")

    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "啊，是因为温泉吧。\x01",
            "觉得空气也很潮湿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "只要在这里，\x01",
            "妻子就会忘掉购物欲，\x01",
            "能好好地放松一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B19")

    TalkEnd(0xFE)
    Return()

    # Function_4_8F2 end

    def Function_5_B1D(): pass

    label("Function_5_B1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_B2A")
    Jump("loc_C43")

    label("loc_B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_B34")
    Jump("loc_C43")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_B3E")
    Jump("loc_C43")

    label("loc_B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B48")
    Jump("loc_C43")

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_B52")
    Jump("loc_C43")

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BA8")

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这口井……\x01",
            "大小正好适合做钓鱼池啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C25")

    label("loc_BA8")

    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "偶尔把钓鱼的事忘掉，\x01",
            "休息一下也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "简直感觉\x01",
            "像心灵被清洗了一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C25")

    Jump("loc_C43")

    label("loc_C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_C32")
    Jump("loc_C43")

    label("loc_C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_C3C")
    Jump("loc_C43")

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C43")

    label("loc_C43")

    TalkEnd(0xFE)
    Return()

    # Function_5_B1D end

    def Function_6_C47(): pass

    label("Function_6_C47")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_C47 end

    def Function_7_C4E(): pass

    label("Function_7_C4E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_C4E end

    def Function_8_C55(): pass

    label("Function_8_C55")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CD9")

    ChrTalk(
        0xFE,
        "啊，喂，库安。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你在刚才的战斗中\x01",
            "一直在用导力魔法，\x01",
            "那可不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "使用魔法\x01",
            "需要待机时间啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D93")

    label("loc_CD9")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "还在玩武术大会游戏……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且是在大马路上，\x01",
            "不觉得害羞吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是个小鬼头。\x02",
    )

    CloseMessageWindow()

    label("loc_D93")

    Jump("loc_10DE")

    label("loc_D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E32")

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "在蔡斯发生大事的同时，\x01",
            "这边的水泵也出了故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是解乏又温暖的\x01",
            "亚尔摩温泉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA7")

    label("loc_E32")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        "嗯，不愧是蔡斯啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "恐怖事件……\x01",
            "真是了不得的大新闻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "《利贝尔通讯》中\x01",
            "也会登载这个爆炸性新闻吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA7")

    Jump("loc_10DE")

    label("loc_EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F1E")

    ChrTalk(
        0xFE,
        (
            "好啦，拉克。\x01",
            "不能去栅栏那边啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要不然我又要\x01",
            "被毛婆婆骂了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F97")

    label("loc_F1E")

    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "只是去后山而已，\x01",
            "有什么了不起的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们啊，\x01",
            "真是一群小鬼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F97")

    Jump("loc_10DE")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_FA4")
    Jump("loc_10DE")

    label("loc_FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_FAE")
    Jump("loc_10DE")

    label("loc_FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_FB8")
    Jump("loc_10DE")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_FC2")
    Jump("loc_10DE")

    label("loc_FC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_FCC")
    Jump("loc_10DE")

    label("loc_FCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1037")

    ChrTalk(
        0xFE,
        (
            "嗯～\x01",
            "蔡斯的人果然都很酷啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "该怎么说呢，\x01",
            "就像这样给人以干练的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DE")

    label("loc_1037")

    OP_A2(0x3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1060")

    ChrTalk(
        0xFE,
        "哇，哥哥真帅呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_108E")

    label("loc_1060")


    ChrTalk(
        0xFE,
        (
            "哇，\x01",
            "那边的哥哥看起来真帅呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108E")


    ChrTalk(
        0xFE,
        (
            "喂，喂？\x01",
            "你们是从蔡斯来的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在那边\x01",
            "正流行什么啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DE")

    TalkEnd(0xFE)
    Return()

    # Function_8_C55 end

    def Function_9_10E2(): pass

    label("Function_9_10E2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_10E2 end

    def Function_10_10E9(): pass

    label("Function_10_10E9")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_10E9 end

    def Function_11_10F0(): pass

    label("Function_11_10F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1136")

    ChrTalk(
        0xFE,
        (
            "上啊～！\x01",
            "看我的导力魔法！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "咚～～啪！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1180")

    label("loc_1136")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "喂，莉西亚姐姐。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xD, 400)

    ChrTalk(
        0xFE,
        (
            "你是裁判，\x01",
            "要好好看着才行哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1180")

    Jump("loc_1504")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1222")

    ChrTalk(
        0xFE,
        (
            "嘿，你知道吗？\x01",
            "蔡斯出事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像是不得了的大事件。\x01",
            "这个村子里\x01",
            "也有游击士来调查了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "好想看看真正的游击士呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1504")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_132D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1288")

    ChrTalk(
        0xFE,
        (
            "啊啊～\x01",
            "真想去后山探险一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "村子里面\x01",
            "我都已经玩够了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132A")

    label("loc_1288")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "温泉的源头\x01",
            "一定非常大吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "温泉水从那里\x01",
            "涌出了几十年，\x01",
            "也没有见它干涸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊～真想去看看。\x02",
    )

    CloseMessageWindow()

    label("loc_132A")

    Jump("loc_1504")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1337")
    Jump("loc_1504")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1341")
    Jump("loc_1504")

    label("loc_1341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_134B")
    Jump("loc_1504")

    label("loc_134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_13AD")

    ChrTalk(
        0xFE,
        "唔～果然很奇怪啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "绝对没错。\x01",
            "因为我每天都看着呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FE")

    label("loc_13AD")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "哎～真奇怪啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就在刚才，\x01",
            "温泉的水流看起来有点弱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FE")

    Jump("loc_1504")

    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_149B")

    ChrTalk(
        0xFE,
        (
            "这么年轻\x01",
            "就来泡温泉啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "肯定是相当累了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1504")

    label("loc_149B")

    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "啊，有客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎～真少见啊。\x01",
            "这么年轻的客人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1504")

    TalkEnd(0xFE)
    Return()

    # Function_11_10F0 end

    def Function_12_1508(): pass

    label("Function_12_1508")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_12_1508 end

    def Function_13_150F(): pass

    label("Function_13_150F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_15DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_156B")

    ChrTalk(
        0xFE,
        (
            "可恶！不能认输！\x01",
            "我也发动魔法！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿呀呀呀呀～～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_15D8")

    label("loc_156B")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿～说起诞辰庆典，\x01",
            "果然还是武术大会最吸引人吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D8")

    Jump("loc_1912")

    label("loc_15DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_16A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1646")

    ChrTalk(
        0xFE,
        "真是件大事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然好像和我们村子\x01",
            "没什么关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A6")

    label("loc_1646")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "蔡斯出了大事吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "城市里果然可怕啊。\x02",
    )

    CloseMessageWindow()

    label("loc_16A6")

    Jump("loc_1912")

    label("loc_16A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_17D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_171A")

    ChrTalk(
        0xFE,
        (
            "……但是，\x01",
            "莉西亚姐姐也真是的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们都已经是大人了，\x01",
            "不要管我们那么多嘛。\x01",
            "有这时间倒不如去旅馆帮帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17D3")

    label("loc_171A")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        "后山的温泉源头吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我经常听说，\x01",
            "但是从来没有亲眼见过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "虽说不能越过这个栅栏，\x01",
            "但我还是很想去看看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D3")

    Jump("loc_1912")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_17E0")
    Jump("loc_1912")

    label("loc_17E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_17EA")
    Jump("loc_1912")

    label("loc_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_17F4")
    Jump("loc_1912")

    label("loc_17F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1856")

    ChrTalk(
        0xFE,
        (
            "拉克那家伙\x01",
            "说温泉的样子有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是吗？\x01",
            "对我来说没感到什么不同。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1912")

    label("loc_1856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1912")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_18D4")

    ChrTalk(
        0xFE,
        "嘿嘿，拉克真是小鬼啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说到情侣，\x01",
            "果然要一起去温泉才浪漫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1912")

    label("loc_18D4")

    OP_A2(0x8)

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，很浪漫啊。\x01",
            "情侣一起到温泉旅游。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1912")

    TalkEnd(0xFE)
    Return()

    # Function_13_150F end

    def Function_14_1916(): pass

    label("Function_14_1916")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(53490, 2500, 9430, 0)
    OP_67(0, 5410, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 52820, 2500, -3040, 270)
    SetChrPos(0x101, 42000, 2500, -2430, 45)
    SetChrPos(0x102, 41080, 2500, -1680, 45)
    SetChrPos(0x107, 40890, 2500, -2710, 45)
    FadeToBright(1000, 0)
    OP_6D(40870, 2500, -2620, 5000)

    ChrTalk(
        0x101,
        "#501F哇～天色已经这么暗了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F东方风格的庭院……的确很风雅。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P啊～！\x01",
            "是小艾你们啊～！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(46060, 2500, -3350, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 41530, 2500, -2520, 90)
    SetChrPos(0x107, 41120, 2500, -3580, 90)
    SetChrPos(0x102, 40830, 2500, -1900, 90)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x102, 0x4)

    def lambda_1AC4():
        OP_8E(0xFE, 0xB842, 0x9C4, 0xFFFFF498, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AC4)
    OP_0D()
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x101,
        "#501F咦，朵洛希？\x02",
    )

    CloseMessageWindow()

    def lambda_1AFB():
        OP_8E(0xFE, 0xB068, 0x9C4, 0xFFFFF4DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AFB)
    Sleep(300)

    def lambda_1B1B():
        OP_8E(0xFE, 0xADA2, 0x9C4, 0xFFFFF1C8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1B1B)
    Sleep(300)

    def lambda_1B3B():
        OP_8E(0xFE, 0xADE8, 0x9C4, 0xFFFFF6FA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B3B)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x8,
        (
            "#151F嘿嘿～～\x01",
            "小艾你们也来泡澡吗～？\x02\x03",
            "这里的澡堂很好哦～\x01",
            "又大又舒适。\x02\x03",
            "不过要是泡过头了，\x01",
            "脑袋会晕晕乎乎的哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F难道说你回到旅馆之后，\x01",
            "就一～直泡到现在？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#151F没错。\x01",
            "哇～真是好舒服哦～\x02\x03",
            "#153F咦，这个女孩子是……\x01",
            "我们还是第一次见面吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#560F啊，初次见面……\x01",
            "我叫提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#150F哎～初次见面。\x02\x03",
            "我叫朵洛希。\x02\x03",
            "我在王都的一家杂志社里\x01",
            "当一名摄影师的哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#061F摄影师……\x01",
            "哇～好棒的职业哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#151F嘿嘿，过奖啦～\x02\x03",
            "#150F啊，对了～\x01",
            "小艾你们今天\x01",
            "也在这家旅馆过夜吧。\x02\x03",
            "可以的话待会儿一起吃饭吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F嗯，那也好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在我们泡完温泉之前，\x01",
            "可以请你先等一会儿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#151F嗯，没问题～\x01",
            "那我就一边喝水果牛奶一边等～\x02\x03",
            "那么，待会见哦～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EAB():

        label("loc_1EAB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1EAB")

    QueueWorkItem2(0x101, 1, lambda_1EAB)

    def lambda_1EBC():

        label("loc_1EBC")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1EBC")

    QueueWorkItem2(0x102, 1, lambda_1EBC)

    def lambda_1ECD():

        label("loc_1ECD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1ECD")

    QueueWorkItem2(0x107, 1, lambda_1ECD)
    OP_8F(0x102, 0xACE4, 0x9C4, 0xFFFFF510, 0x7D0, 0x0)
    SetChrFlags(0x8, 0x40)
    OP_8E(0x8, 0xB34C, 0x9C4, 0xFFFFF6FA, 0xBB8, 0x0)
    OP_8E(0x8, 0x9E98, 0x9C4, 0xFFFFF4DE, 0xBB8, 0x0)
    OP_70(0x5, 0x1D)
    OP_73(0x5)
    OP_8E(0x8, 0x9826, 0x9C4, 0xFFFFF51A, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x80)
    Sleep(500)
    OP_72(0x5, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x5, 29)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_71(0x5, 0x800)
    OP_44(0x101, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x102, 0xFF)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x102, 0x4)
    EventEnd(0x0)
    Return()

    # Function_14_1916 end

    def Function_15_1F7A(): pass

    label("Function_15_1F7A")

    OP_22(0x1C7, 0x1, 0x64)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_11(0xEF, 0xEC, 0xF1, 0x8534, 0x99E8, 0x0)
    SetMapFlags(0x10)
    OP_6D(67020, 1000, 15120, 0)
    OP_67(0, 9190, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    SetChrChipByIndex(0x101, 2)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x107, 3)
    SetChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x107, 0x80)
    SetChrPos(0x101, 68840, 2000, 6530, 0)
    SetChrPos(0x102, 66060, 1000, 21730, 225)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x10496, 0x7D0, 0x2BB6, 0xBB8, 0x0)

    ChrTalk(
        0x101,
        (
            "#441F（呼～好紧张……\x01",
            "　心脏还在咚咚地跳呢……）\x02\x03",
            "（我……\x01",
            "　刚才到底是怎么了……）\x02\x03",
            "（到现在为止，\x01",
            "　都没对约修亚有过这样的感觉……）\x02\x03",
            "#377F（…………………………）\x02\x03",
            "#376F（啊啊啊，不想了！\x01",
            "　一味苦恼根本不是我的性格！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_211D():
        OP_6D(65160, 1000, 17980, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_211D)

    def lambda_2135():
        OP_6C(11000, 3500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2135)
    OP_8E(0x101, 0xF64A, 0x7D0, 0x2ABC, 0x7D0, 0x0)
    OP_8E(0x101, 0xF21C, 0x3E8, 0x3B42, 0x7D0, 0x0)
    OP_8E(0x101, 0xFE42, 0x3E8, 0x45EC, 0x3E8, 0x0)
    OP_8C(0x101, 225, 300)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x101,
        (
            "#371F哇～好舒服～！\x02\x03",
            "里面的澡堂也很不错，\x01",
            "不过外面的可是更特别呢。\x02\x03",
            "#370F嗯～\x01",
            "又大又舒适……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "少年的声音",
        (
            "……话说在前头，\x01",
            "这里面可不许游泳的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#444F嘁……\x01",
            "我才不会那么做呢！\x02\x03",
            "…………………………\x02\x03",
            "#374F………………哎。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_22BF():
        OP_6D(65630, 1000, 20540, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22BF)
    OP_67(0, 8970, -10000, 1000)
    TurnDirection(0x101, 0x102, 400)
    Fade(2500)
    ClearMapFlags(0x10)
    Sleep(2500)
    OP_6C(45000, 2500)

    ChrTalk(
        0x102,
        (
            "#380F哟，艾丝蒂尔，\x01",
            "我已经先进来了。\x02\x03",
            "#389F哈哈……说起来，\x01",
            "这幅样子还真是有点难为情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#374F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#389F不、不过温泉\x01",
            "真是出乎意料的有效啊。\x02\x03",
            "伤口似乎好多了，\x01",
            "体内的疲劳也都释放出来了。\x02\x03",
            "对我们游击士来说，\x01",
            "这种调节是最合适不过的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#374F……………………………\x01",
            "……………………………\x01",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#388F喂，那个……\x02\x03",
            "在这种气氛下保持沉默，\x01",
            "会让人觉得很不自然的……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    ChrTalk(
        0x101,
        "#373F哎、唔、啊……\x02",
    )

    CloseMessageWindow()
    OP_9E(0x101, 0xF, 0x0, 0x3E8, 0xBB8)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#375F#20A#5S呀啊啊啊啊啊啊啊！\x05\x02",
    )

    FadeToDark(3000, 0, -1)
    OP_6B(15700, 2000)
    Sleep(2000)
    OP_6D(67030, 2000, 13540, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 66930, 2000, 12000, 0)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x101, 65690, 1000, 15170, 180)
    SetChrPos(0x107, 64620, 1000, 15010, 180)
    SetChrPos(0x102, 65430, 1000, 16430, 180)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_1E()
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#682F发出那么大声的惨叫，\x01",
            "我还以为岀了啥事呢……\x02\x03",
            "真是会添乱的小姑娘呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#377F呜……对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#682F听好了。\x01",
            "这个露天温泉是男女混浴的。\x02\x03",
            "你刚才没看清楚\x01",
            "更衣室外那张大大的告示吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#373F呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#387F……真是的，\x01",
            "肯定是连看都没看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#681F再说了，裸体被看个一两次，\x01",
            "也没啥好慌张的嘛。\x02\x03",
            "女孩子的肌肤就是要\x01",
            "保养得漂漂亮亮给人看的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#393F是、是吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#372F提妲，不要相信呀！\x02\x03",
            "而且而且……\x01",
            "我根本就没被人看到裸体呀！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#680F哎呀，就别管那么多啦。\x01",
            "泡个澡而已，亲亲热热地去泡就是啦。\x02\x03",
            "这里本来就是\x01",
            "给一家人开开心心混浴的嘛。\x02\x03",
            "好了，我先走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    def lambda_2939():
        OP_8E(0x9, 0x10C98, 0x7D0, 0x1982, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2939)
    Sleep(1000)

    def lambda_2959():
        OP_6D(65269, 1000, 15580, 2000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2959)
    WaitChrThread(0x9, 0x2)
    OP_6F(0x8, 29)
    OP_70(0x8, 0x1D)
    Sleep(1000)
    OP_72(0x8, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x8, 0x0)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#377F唉～……\x01",
            "突然觉得好累……\x02\x03",
            "#444F唔～都怪你，约修亚。\x01",
            "搞出那么难为情的事情！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x102,
        (
            "#387F为什么是我……\x02\x03",
            "#388F根本就是你一个人\x01",
            "引起了那么大的骚动。\x02\x03",
            "连更衣室的告示也没看到，\x01",
            "这就是平日注意力不够的证明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#379F要、要你多事啦！\x02\x03",
            "真是的……\x01",
            "一点儿也不可爱！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#382F哦，是吗。\x02\x03",
            "#385F算了，没关系。\x02\x03",
            "反正就算被你觉得可爱，\x01",
            "我也没什么好高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#372F你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#383F说到底，刚刚那算什么。\x01",
            "看到人家就像见鬼似的发出惨叫……\x02\x03",
            "你竟然会有那样的反应，\x01",
            "……我真是做梦都没想到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#441F那……那是……\x01",
            "因为时机实在是太……\x02\x03",
            "反正不是因为\x01",
            "讨厌见到约修亚你啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#385F没关系，不用勉强。\x02\x03",
            "#380F反正碍事的人已经洗好了，\x01",
            "你们俩就继续泡吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#375F什、什么嘛！？\x01",
            "碍事什么的，我根本一句也没说过呀！\x02\x03",
            "约修亚是笨蛋！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#382F哼……谁才是笨蛋啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#391F嘻嘻……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#441F你、你看！\x02\x03",
            "都怪你。\x01",
            "连提妲都在笑我们了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#388F为什么又怪我……\x02",
    )

    CloseMessageWindow()

    def lambda_2E53():
        OP_69(0x107, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E53)

    def lambda_2E61():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E61)
    TurnDirection(0x102, 0x107, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x102,
        (
            "#389F抱、抱歉。\x01",
            "让你看到这么丢人的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#396F啊，没有啦。\x01",
            "只是忍不住笑了，真不好意思。\x02\x03",
            "其实呢……\x01",
            "我挺羡慕你们俩的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#374F#3P羡、羡慕？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#384F哎……为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#390F我没有兄弟姐妹，\x01",
            "也没有跟别人吵过架。\x02\x03",
            "爷爷很疼我，\x01",
            "也很少很少会责骂我……\x02\x03",
            "还有的是，\x01",
            "爸爸妈妈又很少在我身边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#374F#3P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#382F那个……\x01",
            "提妲的爸爸妈妈是……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#390F我爸爸妈妈是导力技术者，\x01",
            "所以需要一直呆在国外。\x02\x03",
            "听说是到导力器还没普及的地方\x01",
            "去做技术指导……\x02\x03",
            "而且……\x01",
            "他们俩已经好几年没回来过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#373F#3P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#383F那会……很寂寞吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#396F也没有啦。\x01",
            "因为还有爷爷和我在一起嘛。\x02\x03",
            "而且中央工房的员工对我也很好，\x01",
            "大家都是很亲切的人。\x02\x03",
            "#395F不过……\x01",
            "见到艾丝蒂尔姐姐你们之后，\x01",
            "我就总觉得有点羡慕……\x02\x03",
            "嘿嘿，也许这就是\x01",
            "所谓得不到的东西总是好的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#382F提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#440F#3P…………………………\x02\x03",
            "#376F我有个好主意哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#393F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#384F艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#371F#3P从现在开始，\x01",
            "我就做提妲的姐姐吧！\x02\x03",
            "而约修亚嘛，就做哥哥好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#394F哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#387F唉……\x01",
            "又说这么唐突的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#379F#3P什么呀，你有意见吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#381F没有……\x01",
            "这本来是艾丝蒂尔的风格。\x02\x03",
            "我也没意见。\x01",
            "只要提妲觉得合适的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#396F……啊……\x02\x03",
            "#395F谢、谢谢……\x01",
            "艾丝蒂尔姐姐、约修亚哥哥。\x02\x03",
            "我、我……\x01",
            "实在是太高兴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#371F#3P那好，就这样决定了！\x02\x03",
            "#376F啊，对了对了。\x01",
            "以后说话可不要那么见外哦。\x02\x03",
            "嘿嘿～\x01",
            "当然我们也会比较随便的啦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#389F是啊。\x02\x03",
            "以后只要像和博士说话那样，\x01",
            "轻松点自然点就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#397F啊，嗯……\x01",
            "轻松点自然点说话……\x02\x03",
            "…………………………\x02\x03",
            "#396F艾丝蒂尔姐姐，\x01",
            "还有约修亚哥哥。\x02\x03",
            "#395F……这、这样行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#371F#3P嗯，非常好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#389F以后我们就是三兄妹了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3223   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1F7A end

    def Function_16_3683(): pass

    label("Function_16_3683")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁，无法打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_3683 end

    def Function_17_36D2(): pass

    label("Function_17_36D2")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3774")
    TurnDirection(0x102, 0x1, 400)

    ChrTalk(
        0x102,
        (
            "#010F晚上的平原很危险。\x01",
            "我们还是回去吧。\x02\x03",
            "想散步的话，在村子里走走就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F3")

    label("loc_3774")

    TurnDirection(0x102, 0x0, 400)

    ChrTalk(
        0x102,
        (
            "#010F晚上的平原很危险。\x02\x03",
            "想散步的话，\x01",
            "在村子里走走就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F3")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_17_36D2 end

    def Function_18_380F(): pass

    label("Function_18_380F")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "发现了一个油纸包。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "里面放着\x07\x02",
            "艾尔贝啄木鸟的生态\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x343, 1)
    OP_64(0x1, 0x1)
    OP_28(0x2E, 0x1, 0x10)
    TalkEnd(0xFF)
    Return()

    # Function_18_380F end

    def Function_19_38A8(): pass

    label("Function_19_38A8")

    SetPlaceName(0x88) # 亚尔摩村　水泵小屋
    Return()

    # Function_19_38A8 end

    def Function_20_38AC(): pass

    label("Function_20_38AC")

    SetPlaceName(0x87) # 亚尔摩村　水泵小屋
    Return()

    # Function_20_38AC end

    def Function_21_38B0(): pass

    label("Function_21_38B0")

    SetPlaceName(0x89) # 亚尔摩村　水泵小屋
    Return()

    # Function_21_38B0 end

    SaveToFile()

Try(main)
