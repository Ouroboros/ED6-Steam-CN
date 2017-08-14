from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1110   ._SN',
        MapName             = 'Bose',
        Location            = 'T1110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '博尔德',                               # 9
        '莉咏',                                 # 10
        '阿尔贝尔',                             # 11
        '库瓦诺老人',                           # 12
        '塞西尔婆婆',                           # 13
        '莫德娜',                               # 14
        '米拉诺',                               # 15
        '西蒙',                                 # 16
        '拉娜',                                 # 17
        '艾尔珂',                               # 18
        '王国军士兵',                           # 19
        '王国军士兵',                           # 20
        '王国军士兵',                           # 21
        '特里诺',                               # 22
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
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
        'ED6_DT07/CH01680 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01000 ._CH',             # 03
        'ED6_DT07/CH01010 ._CH',             # 04
        'ED6_DT07/CH01183 ._CH',             # 05
        'ED6_DT07/CH01230 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01480 ._CH',             # 08
        'ED6_DT07/CH01140 ._CH',             # 09
        'ED6_DT07/CH01640 ._CH',             # 0A
        'ED6_DT07/CH01200 ._CH',             # 0B
        'ED6_DT07/CH01003 ._CH',             # 0C
        'ED6_DT07/CH01010 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01000P._CP',             # 03
        'ED6_DT07/CH01010P._CP',             # 04
        'ED6_DT07/CH01183P._CP',             # 05
        'ED6_DT07/CH01230P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01480P._CP',             # 08
        'ED6_DT07/CH01140P._CP',             # 09
        'ED6_DT07/CH01640P._CP',             # 0A
        'ED6_DT07/CH01200P._CP',             # 0B
        'ED6_DT07/CH01003P._CP',             # 0C
        'ED6_DT07/CH01010P._CP',             # 0D
    )

    DeclNpc(
        X                   = -22100,
        Z                   = 0,
        Y                   = 69250,
        Direction           = 0,
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
        X                   = -21340,
        Z                   = 0,
        Y                   = 72520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -11200,
        Z                   = 5250,
        Y                   = 72600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -21700,
        Z                   = 0,
        Y                   = 3000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -16400,
        Z                   = 0,
        Y                   = -1700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -18730,
        Z                   = 0,
        Y                   = 33060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 19400,
        Z                   = 0,
        Y                   = 31200,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -21100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 20970,
        Z                   = 0,
        Y                   = 67860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 27100,
        Z                   = 4000,
        Y                   = 72200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -20715,
        Z                   = 0,
        Y                   = -1884,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -21300,
        Z                   = 0,
        Y                   = 66800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 21176,
        Z                   = 0,
        Y                   = 66028,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -21100,
        Z                   = 0,
        Y                   = 33600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )


    ScpFunction(
        "Function_0_2DA",          # 00, 0
        "Function_1_49A",          # 01, 1
        "Function_2_49B",          # 02, 2
        "Function_3_4B1",          # 03, 3
        "Function_4_540",          # 04, 4
        "Function_5_564",          # 05, 5
        "Function_6_5D4",          # 06, 6
        "Function_7_696",          # 07, 7
        "Function_8_1379",         # 08, 8
        "Function_9_1C81",         # 09, 9
        "Function_10_247D",        # 0A, 10
        "Function_11_2A96",        # 0B, 11
        "Function_12_428E",        # 0C, 12
        "Function_13_4C67",        # 0D, 13
        "Function_14_55DF",        # 0E, 14
        "Function_15_5E64",        # 0F, 15
        "Function_16_6273",        # 10, 16
        "Function_17_640F",        # 11, 17
        "Function_18_6473",        # 12, 18
        "Function_19_64EB",        # 13, 19
        "Function_20_65F2",        # 14, 20
        "Function_21_671D",        # 15, 21
    )


    def Function_0_2DA(): pass

    label("Function_0_2DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2E9")
    ClearChrFlags(0x15, 0x80)
    Jump("loc_3FD")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_302")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_3FD")

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_316")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_3FD")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_348")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    Jump("loc_3FD")

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_385")
    SetChrPos(0xD, 17400, 300, 28530, 270)
    SetChrPos(0xE, -20530, 0, 33050, 180)
    SetChrPos(0xC, -16400, 0, -1700, 90)
    Jump("loc_3FD")

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3AA")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetChrPos(0xC, -16400, 0, -1700, 90)
    Jump("loc_3FD")

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_3DB")
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xC, -16400, 0, -1700, 135)
    SetChrPos(0xE, -23120, 0, 34500, 180)
    Jump("loc_3FD")

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3FD")
    SetChrPos(0xB, -17620, 0, -680, 135)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_499")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 20852, 0, 68000, 180)
    SetChrPos(0x11, 21329, 0, 68470, 180)
    OP_44(0x11, 0xFF)
    OP_43(0x11, 0x3, 0x0, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x8, -20868, 0, 68402, 180)
    SetChrPos(0xA, -22006, 0, 68102, 135)
    SetChrPos(0x9, -19902, 0, 68102, 225)
    OP_44(0x8, 0xFF)
    OP_43(0x8, 0x3, 0x0, 0x2)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xC, -21950, 0, -570, 135)

    label("loc_499")

    Return()

    # Function_0_2DA end

    def Function_1_49A(): pass

    label("Function_1_49A")

    Return()

    # Function_1_49A end

    def Function_2_49B(): pass

    label("Function_2_49B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_49B")

    label("loc_4B0")

    Return()

    # Function_2_49B end

    def Function_3_4B1(): pass

    label("Function_3_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4D0")

    label("loc_4B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4B8")

    label("loc_4CD")

    Jump("loc_53F")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_51C")

    label("loc_4D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_519")
    OP_8E(0xFE, 0xFFFFA5A6, 0x0, 0x8F0C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xFFFFA5A6, 0x0, 0x7BAC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Jump("loc_4D7")

    label("loc_519")

    Jump("loc_53F")

    label("loc_51C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53F")
    OP_8D(0xFE, 20900, 30000, 15300, 31700, 2000)
    Jump("loc_51C")

    label("loc_53F")

    Return()

    # Function_3_4B1 end

    def Function_4_540(): pass

    label("Function_4_540")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_563")
    OP_8D(0xFE, 26200, 71400, 28400, 72600, 2000)
    Jump("Function_4_540")

    label("loc_563")

    Return()

    # Function_4_540 end

    def Function_5_564(): pass

    label("Function_5_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_591")

    label("loc_56B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58E")
    OP_8D(0xFE, 17430, 68790, 23880, 64870, 1500)
    Jump("loc_56B")

    label("loc_58E")

    Jump("loc_5D3")

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_5B0")

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_598")

    label("loc_5AD")

    Jump("loc_5D3")

    label("loc_5B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D3")
    OP_8D(0xFE, 17430, 68790, 23880, 64870, 1500)
    Jump("loc_5B0")

    label("loc_5D3")

    Return()

    # Function_5_564 end

    def Function_6_5D4(): pass

    label("Function_6_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_62A")

    label("loc_5DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_627")
    OP_8E(0xFE, 0xFFFFA6F0, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFB050, 0x0, 0x11AE4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("loc_5DB")

    label("loc_627")

    Jump("loc_695")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_649")

    label("loc_631")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_646")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_631")

    label("loc_646")

    Jump("loc_695")

    label("loc_649")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_695")
    OP_8E(0xFE, 0xFFFFA6F0, 0x0, 0x11B34, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    OP_8E(0xFE, 0xFFFFB050, 0x0, 0x11AE4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(3000)
    Jump("loc_649")

    label("loc_695")

    Return()

    # Function_6_5D4 end

    def Function_7_696(): pass

    label("Function_7_696")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_7F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "特里诺那家伙\x01",
            "终于平安回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样我就可以\x01",
            "毫无顾虑地专心做生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就碰到了那么点小麻烦， \x01",
            "柏斯的商人不能就这样轻易泄气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F3")

    label("loc_768")


    ChrTalk(
        0xFE,
        (
            "这样我就可以\x01",
            "毫无顾虑地专心做生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就碰到了那么点小麻烦， \x01",
            "柏斯的商人不能就这样轻易泄气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F3")

    Jump("loc_1375")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BB")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "尽管如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特里诺不在柏斯的话，\x01",
            "总觉得哪里有些不对劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们小时候\x01",
            "总是互相打打闹闹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我们在商场上是对手，\x01",
            "但是却好像有一种奇妙的连带感，\x01",
            "这是千真万确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可以说柏斯的商业\x01",
            "就是由我们两人支撑起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哈哈，如果他听到这番话，\x01",
            "肯定要笑掉大牙了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A54")

    label("loc_9BB")


    ChrTalk(
        0xFE,
        (
            "特里诺不在柏斯的话，\x01",
            "总觉得哪里有些不对劲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然我们在商场上是对手，\x01",
            "但是却好像有一种奇妙的连带感，\x01",
            "这是千真万确的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A54")

    Jump("loc_1375")

    label("loc_A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_C7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB2")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "哎呀哎呀，\x01",
            "飞艇的失踪再加上这次的强盗事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "最近的坏消息还真多啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "『赛希莉亚号』的复航\x01",
            "是最近唯一令人高兴的话题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过对我们来说，\x01",
            "到帝国去的国际航线不恢复的话\x01",
            "就没办法继续做生意了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78")

    label("loc_BB2")


    ChrTalk(
        0xFE,
        (
            "不过对我们来说，\x01",
            "到帝国去的国际航线不恢复的话\x01",
            "就没办法继续做生意了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "还是很难办啊。\x02",
    )

    CloseMessageWindow()

    label("loc_C78")

    Jump("loc_1375")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF7")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(
        0x13,
        (
            "我再问一会儿就结束了，\x01",
            "你们要乖乖地等着哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 0)
    Jump("loc_1375")

    label("loc_CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E56")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "由于柏斯领空被军队封锁了，\x01",
            "影响了货物的进出交易。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "从帝国来的定期船\x01",
            "也在国境附近被截停禁止进入……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样子下去\x01",
            "我们就无法做生意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……米拉诺小姐即使在这种情况下\x01",
            "似乎也能够精力充沛地工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "我可不能向她认输。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECD")

    label("loc_E56")


    ChrTalk(
        0xFE,
        (
            "米拉诺小姐即使在这种情况下\x01",
            "似乎也能够精力充沛地工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "我可不能向她认输。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECD")

    Jump("loc_1375")

    label("loc_ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_10B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105D")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "特里诺好像\x01",
            "乘坐了那艘失踪的飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然觉得有点对不起他，\x01",
            "不过对我来说也许是个机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "借这个机会\x01",
            "把特里诺的生意\x01",
            "都揽到我这边来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "米拉诺小姐\x01",
            "现在相当有影响力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "那对父女关系到底是好还是坏呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10B6")

    label("loc_105D")


    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "那对父女关系到底是好还是坏呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B6")

    Jump("loc_1375")

    label("loc_10B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_12AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120B")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        (
            "我们家自古以来就是\x01",
            "在这个柏斯以贸易起家的商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "柏斯的势力范围\x01",
            "基本上被我家\x01",
            "和特里诺家瓜分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过最近\x01",
            "特里诺的女儿米拉诺小姐\x01",
            "势力增长得也很快啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在已经形成\x01",
            "三足鼎立之势了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_120B")


    ChrTalk(
        0xFE,
        (
            "最近，\x01",
            "特里诺的女儿米拉诺小姐\x01",
            "势力增长得也很快啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在已经形成三足鼎立之势了。\x02",
    )

    CloseMessageWindow()

    label("loc_12A7")

    Jump("loc_1375")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1375")

    ChrTalk(
        0xFE,
        (
            "虽然柏斯商人都喜欢自由自在，\x01",
            "但是遵守约定是我们的信条。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以，\x01",
            "我们会十分守时。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1375")

    TalkEnd(0x8)
    Return()

    # Function_7_696 end

    def Function_8_1379(): pass

    label("Function_8_1379")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141E")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "原来那些蒙面男人\x01",
            "就是传说中的空贼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们被抓住真是太好了。\x01",
            "这样我就可以专注于我的事业了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145F")

    label("loc_141E")


    ChrTalk(
        0xFE,
        (
            "那么，这个月的销量\x01",
            "一定要胜过强敌特里诺一家！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145F")

    Jump("loc_1C7D")

    label("loc_1462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_155C")

    ChrTalk(
        0xFE,
        (
            "希望这个城市\x01",
            "能够尽早恢复平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "市场也渐渐变得冷清下来，\x01",
            "这样下去这个月肯定会出现严重赤字了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "上个月好不容易\x01",
            "赢过了特里诺家……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C7D")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_16D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1659")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        "昨天晚上吓死我了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了通风，\x01",
            "我就把窗户打开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到有一伙蒙面的男人\x01",
            "从窗户闯进屋子里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "有好几个人呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D1")

    label("loc_1659")


    ChrTalk(
        0xFE,
        (
            "为了通风，\x01",
            "我就把窗户打开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "没想到有一伙蒙面的男人\x01",
            "从窗户闯进屋子里来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D1")

    Jump("loc_1C7D")

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1751")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(
        0x13,
        (
            "我再问一会儿就结束了，\x01",
            "你们要乖乖地等着哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 0)
    Jump("loc_1C7D")

    label("loc_1751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1921")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1874")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我丈夫在买卖和谈判方面\x01",
            "都进行得非常合理到位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而特里诺却完全相反。\x01",
            "全都是靠劲头和感觉去拼的那种人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "米拉诺则是那两人综合起来的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "与梅贝尔市长属于同一种类型。\x02",
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_1874")


    ChrTalk(
        0xFE,
        (
            "在不久的将来，\x01",
            "我们家的地位说不定会被米拉诺夺走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过呢，\x01",
            "我们也绝不会轻易认输的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_191E")

    Jump("loc_1C7D")

    label("loc_1921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E7")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "难道特里诺\x01",
            "乘坐了那艘定期船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说是对手，\x01",
            "不过一直以来也都是老熟人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果他能够\x01",
            "平安无事回来就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A96")

    label("loc_19E7")


    ChrTalk(
        0xFE,
        (
            "难道特里诺\x01",
            "乘坐了那艘定期船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说是对手，\x01",
            "不过一直以来也都是老熟人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果他能够\x01",
            "平安无事回来就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A96")

    Jump("loc_1C7D")

    label("loc_1A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B8B")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "米拉诺前一段时间\x01",
            "到我们家来玩了。\x01",
            "明明是那么可爱的女孩……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "现在却是我们强大的商业对手。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果我家的阿尔贝尔\x01",
            "也能有这样的气概就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD0")

    label("loc_1B8B")


    ChrTalk(
        0xFE,
        (
            "真希望我家的儿子\x01",
            "也能有米拉诺那样的气概啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD0")

    Jump("loc_1C7D")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1C7D")

    ChrTalk(
        0xFE,
        (
            "自从军队实行戒严以来，\x01",
            "都已经过了很久了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这个月不用说又该是赤字了。\x02",
    )

    CloseMessageWindow()

    label("loc_1C7D")

    TalkEnd(0x9)
    Return()

    # Function_8_1379 end

    def Function_9_1C81(): pass

    label("Function_9_1C81")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1DE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D67")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "卢安的杰尼丝王立学院\x01",
            "有一个叫做社会系的专业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "能学到专业的政治与经济知识，\x01",
            "父亲说不定会同意\x01",
            "让我去学校念书呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE6")

    label("loc_1D67")


    ChrTalk(
        0xFE,
        (
            "如果是社会系专业的话，\x01",
            "父亲说不定会同意\x01",
            "让我去学校念书呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE6")

    Jump("loc_2479")

    label("loc_1DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E98")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "嗯～我要找个时间跟父母说一下\x01",
            "我想去王立学院念书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过总觉得现在\x01",
            "还不是说这件事的时候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F05")

    label("loc_1E98")


    ChrTalk(
        0xFE,
        (
            "如果父母不给我出学费的话，\x01",
            "我就上不起学了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是难办啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1F05")

    Jump("loc_2479")

    label("loc_1F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_2031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC6")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "昨天这附近\x01",
            "发生了强盗事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "母亲好像看到犯人了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才军队上来的人\x01",
            "一直在询问有关的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_1FC6")


    ChrTalk(
        0xFE,
        (
            "昨天这附近\x01",
            "发生了强盗事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "母亲好像看到犯人了。\x02",
    )

    CloseMessageWindow()

    label("loc_202E")

    Jump("loc_2479")

    label("loc_2031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20AD")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(
        0x13,
        (
            "我再问一会儿就结束了，\x01",
            "你们要乖乖地等着哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 0, 0)
    Jump("loc_2479")

    label("loc_20AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2116")

    ChrTalk(
        0xFE,
        (
            "父亲和母亲\x01",
            "在为如今的状况而烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不知道米拉诺姐姐\x01",
            "现在会做出什么样的对策呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2479")

    label("loc_2116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E2")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "失踪飞艇的乘客中\x01",
            "好像有特里诺叔叔呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他虽然和我家是商业上的竞争对手，\x01",
            "不过毕竟是米拉诺姐姐的父亲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我真是担心呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2235")

    label("loc_21E2")


    ChrTalk(
        0xFE,
        (
            "米拉诺姐姐也\x01",
            "正在担心叔叔的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "如果能平安就好了……\x02",
    )

    CloseMessageWindow()

    label("loc_2235")

    Jump("loc_2479")

    label("loc_2238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_234F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2313")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "父亲和母亲\x01",
            "经常教训我，\x01",
            "让我向米拉诺姐姐学习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是我……\x01",
            "我并没有成为商人的打算。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想去卢安的\x01",
            "王立学院学习知识。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234C")

    label("loc_2313")


    ChrTalk(
        0xFE,
        (
            "毕竟米拉诺姐姐\x01",
            "从小就受到商业教育的熏陶…… \x02",
        )
    )

    CloseMessageWindow()

    label("loc_234C")

    Jump("loc_2479")

    label("loc_234F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2405")
    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "我父亲是\x01",
            "从事对外贸易工作的商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我们家族\x01",
            "代代都是从事贸易行业的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是我……\x01",
            "可能不适合成为商人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2479")

    label("loc_2405")


    ChrTalk(
        0xFE,
        (
            "我们家族\x01",
            "代代都是从事贸易行业的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是我……\x01",
            "可能不适合成为商人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2479")

    TalkEnd(0xA)
    Return()

    # Function_9_1C81 end

    def Function_10_247D(): pass

    label("Function_10_247D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_24C8")

    ChrTalk(
        0xFE,
        (
            "那么～\x01",
            "这次去钓什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A92")

    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2598")

    ChrTalk(
        0xFE,
        (
            "那家旅馆就在出城后向南走，\x01",
            "沿着安塞尔新街走就能看到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为它就坐落在湖边，\x01",
            "应该马上就能够看到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A92")

    label("loc_2598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2606")
    OP_A2(0x32D)
    OP_28(0x37, 0x1, 0x1)

    ChrTalk(
        0x12,
        (
            "对不起，请让我们先办完事。\x01",
            "去别的地方看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A92")

    label("loc_2606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2761")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E2")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "男人嘛，不管长多大，\x01",
            "仍然会有孩子气的一面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他们永远都会追求\x01",
            "他们心中的那份浪漫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对女人来说，\x01",
            "可能永远也无法理解这种感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275E")

    label("loc_26E2")


    ChrTalk(
        0xFE,
        (
            "男人嘛，不管长多大，\x01",
            "仍然会有孩子气的一面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对女人来说，\x01",
            "可能永远也无法理解这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275E")

    Jump("loc_2A92")

    label("loc_2761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_28FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286C")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "从柏斯出去往南走\x01",
            "就能到达瓦雷利亚湖的北岸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "众所周知，\x01",
            "瓦雷利亚湖是位于王国正中央的大湖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "湖里生存着\x01",
            "各种各样的鱼类。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_28F9")

    label("loc_286C")


    ChrTalk(
        0xFE,
        (
            "众所周知，\x01",
            "瓦雷利亚湖是位于王国正中央的大湖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "湖里生存着\x01",
            "各种各样的鱼类。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F9")

    Jump("loc_2A92")

    label("loc_28FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2974")

    ChrTalk(
        0xFE,
        (
            "老伴为什么\x01",
            "这么容易生气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "血压上升\x01",
            "对健康可没什么好处。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A92")

    label("loc_2974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_2A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6C")
    OP_A2(0x3)

    ChrTalk(
        0xFE,
        (
            "晚年培养一个兴趣\x01",
            "是非常重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "也不用那么生气吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "生气的话，\x01",
            "满是皱纹的脸上会有更多皱纹的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A92")

    label("loc_2A6C")


    ChrTalk(
        0xFE,
        "哦哦，可怕……\x02",
    )

    CloseMessageWindow()

    label("loc_2A92")

    TalkEnd(0xB)
    Return()

    # Function_10_247D end

    def Function_11_2A96(): pass

    label("Function_11_2A96")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2B10")

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "这几十年光想着怎么钓鱼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "怎么就不觉得腻呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_2B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2C95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C41")
    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "那个人总是在我对他发脾气之后，\x01",
            "就出去钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我啊，\x01",
            "已经让自己好好振作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我看到他毫不在乎地回家，\x01",
            "就忍不住发脾气了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C92")

    label("loc_2C41")


    ChrTalk(
        0xFE,
        (
            "算了，反正他钓鱼的同时\x01",
            "也在解决我买菜的问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C92")

    Jump("loc_428A")

    label("loc_2C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_3F4D")
    OP_A2(0x33A)
    OP_28(0x37, 0x1, 0x10)
    OP_28(0x37, 0x1, 0x20)
    OP_28(0x37, 0x1, 0x40)
    OP_28(0x37, 0x1, 0x80)
    OP_28(0x38, 0x4, 0x2)
    OP_28(0x38, 0x4, 0x4)
    EventBegin(0x0)
    OP_69(0xFE, 0x3E8)

    ChrTalk(
        0xFE,
        "哎哟，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们不就是\x01",
            "刚才来打听事情的游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才真是不好意思，\x01",
            "没办法招呼你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看起来，\x01",
            "你们也是想打听昨晚的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯。\x01",
            "您愿意协助我们的调查吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊，当然了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -19910, -150, 1594, 180)
    SetChrPos(0x101, -18365, 0, 850, 270)
    SetChrPos(0x102, -18365, 0, -120, 315)
    SetChrPos(0x103, -20410, 0, -950, 0)
    SetChrPos(0x104, -19334, 0, -950, 0)
    OP_6D(-19459, 0, 700, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        (
            "就在昨天的深夜，\x01",
            "我听到门外好像有什么响声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时我以为敲门的是老头子。\x01",
            "一想到他这个时候才回家，\x01",
            "我当然是气冲冲地大力打开门啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "结果，我看到的却是\x01",
            "一群刚从导力器工房里\x01",
            "出来的蒙面男人。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当时我可被他们吓死了，\x01",
            "感觉心脏就像要停止似的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过奇怪的是，那群蒙面人比我还害怕。\x01",
            "慌慌张张地就往北门那边逃走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F原来是这样啊……\x01",
            "这么说那些家伙就是空贼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，您的屋子\x01",
            "有没有受到什么特别的损失呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没有，这算是不幸中的万幸吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F可以再问一个问题吗？\x02\x03",
            "您的丈夫深夜才回家，\x01",
            "是因为在酒馆喝醉了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是他敢的话，\x01",
            "我绝对饶不了他！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家的老头子可不光爱喝酒，\x01",
            "最近还迷上这种东西了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "塞西尔婆婆用右手\x01",
            "做了几下上下摆臂的动作。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#023F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F啊，我知道⊙\x02\x03",
            "就是钓鱼，没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F啊啊，原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对！这还不止。\x01",
            "为了钓鱼他可以连危险都不顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "昨天还为了钓什么胡瓜鱼，\x01",
            "在南面的湖畔呆了大半天。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "到现在还没回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，这样的话……\x01",
            "那他还不知道昨天的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "就是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那老头子也真是的……\x01",
            "回来之后我一定要他好看！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, -19980, 0, -5070, 0)

    NpcTalk(
        0xB,
        "老人的声音",
        "喂～我回来了。\x02",
    )

    CloseMessageWindow()

    def lambda_34F9():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_34F9)

    def lambda_3507():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3507)

    def lambda_3515():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3515)

    def lambda_3523():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3523)
    OP_4A(0xB, 255)
    SetChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_22(0x6, 0x0, 0x64)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_354F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_354F)
    OP_8E(0xB, 0xFFFFAFEC, 0x0, 0xFFFFF5AB, 0x7D0, 0x0)

    def lambda_3575():

        label("loc_3575")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3575")

    QueueWorkItem2(0x0, 1, lambda_3575)

    def lambda_3586():

        label("loc_3586")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3586")

    QueueWorkItem2(0x1, 1, lambda_3586)

    def lambda_3597():

        label("loc_3597")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_3597")

    QueueWorkItem2(0x2, 1, lambda_3597)

    def lambda_35A8():

        label("loc_35A8")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_35A8")

    QueueWorkItem2(0x3, 1, lambda_35A8)

    ChrTalk(
        0xB,
        "哈，哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "好不容易等了大半天，\x01",
            "没想到最后栽在那些小孩手里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "哦？怎么了，今天来了这么多客人。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_366A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_366A)

    ChrTalk(
        0xFE,
        "#5S你这个死老头！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xB,
        (
            "什、什么事？\x01",
            "突然冲着我这么大嚷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "别在客人面前失礼啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "失礼的是你才对！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，这种紧要关头\x01",
            "你还能逍遥自在地到处游山玩水。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "啊？紧要关头？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F其实是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "众人向库瓦诺老人\x01",
            "讲述了昨晚发生的强盗事件。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0xB, -21250, 50, 300, 90)
    SetChrChipByIndex(0xB, 12)
    SetChrSubChip(0xB, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "什么～空贼来抢劫了吗？\x01",
            "这种事真是不得了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过嘛，一定是老太婆那招杰作——\x01",
            "『气冲冲地大力打开门』吓走了那群空贼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "哇哈哈，遇到老太婆也算他们倒霉啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F别、别生气啊，老婆婆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过，那些空贼在深夜大肆作乱，\x01",
            "然后又突然神秘地消失……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "难道他所说的那件事\x01",
            "和这案件有关？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F他……\x01",
            "请问您说的『他』是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "啊啊，是我的一个钓友。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我那位钓友就在\x01",
            "南面湖畔的旅馆落脚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "听说他在旅馆附近\x01",
            "看到几个奇怪的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F奇怪的家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F挺耐人寻味的嘛。\x01",
            "可以详细讲给我们听听吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "这没问题……\x01",
            "反正我也只是听别人说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我那位钓友是在前天夜钓时\x01",
            "偶然看到那些家伙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "夜深人静的时候，\x01",
            "有几个家伙从旅馆门口走到外面的街道上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "不过奇怪的是，\x01",
            "旅馆的人都说根本没有这样的客人在留宿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这么说来……\x01",
            "的确是很奇怪啊。\x02\x03",
            "请问那家旅馆\x01",
            "有没有发生过强盗事件呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "旅馆完全没有出现过\x01",
            "像昨天那种骚动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "环境清净而且饭菜美味，\x01",
            "是一个广受好评的休闲胜地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "而且还是一处很好的钓鱼场所。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T1100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_428A")

    label("loc_3F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FC9")
    OP_A2(0x32D)
    OP_28(0x37, 0x1, 0x1)
    TurnDirection(0x12, 0x0, 0)

    ChrTalk(
        0x12,
        (
            "对不起，是我们先来的。\x01",
            "你们到别的地方看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 315, 0)
    Jump("loc_428A")

    label("loc_3FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4036")

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "我为什么会选上那种人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这是我人生最大的失败。\x01",
            "我真是没用真是没用……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_4036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_40B8")

    ChrTalk(
        0xFE,
        (
            "我家老头子说的话\x01",
            "最好不要听。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正净是一些\x01",
            "吹牛皮的话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_40B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_4174")

    ChrTalk(
        0xFE,
        "真是的，我家的老头子啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "什么招呼也没打就出去了，\x01",
            "半天也不回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真的是一个没良心不顾家的老头啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_4174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_428A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4239")
    OP_A2(0x4)
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "哼！\x01",
            "我也不会为那种事情生气！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我说过在出门之前\x01",
            "至少跟我打声招呼再走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_4239")


    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "同样的话他准备让我讲多少年？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_428A")

    TalkEnd(0xC)
    Return()

    # Function_11_2A96 end

    def Function_12_428E(): pass

    label("Function_12_428E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_439C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_433E")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "被空贼抓走的老公\x01",
            "终于平安回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊，太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空之女神爱德丝啊……\x01",
            "十分感谢您……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4399")

    label("loc_433E")


    ChrTalk(
        0xFE,
        (
            "被空贼抓走的老公\x01",
            "终于平安回来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊啊，太好了……\x02",
    )

    CloseMessageWindow()

    label("loc_4399")

    Jump("loc_4C63")

    label("loc_439C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4432")

    ChrTalk(
        0xFE,
        (
            "虽然平时总是东奔西走，\x01",
            "但是他一不在身边心里总觉得不踏实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "求你了，老公……\x01",
            "你快点回来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C63")

    label("loc_4432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_45C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4527")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "幸好我们家没有被殃及。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，这种非常时刻\x01",
            "家里没有男人我还是有点不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "米拉诺把西蒙带来，\x01",
            "真是帮了我的大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45C5")

    label("loc_4527")


    ChrTalk(
        0xFE,
        (
            "这种非常时刻\x01",
            "家里没有男人我还是有点不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "米拉诺把西蒙带来，\x01",
            "真是帮了我的大忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45C5")

    Jump("loc_4C63")

    label("loc_45C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_47C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4754")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "博尔德的太太\x01",
            "正在协助她老公工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我也帮我老公做过事情，\x01",
            "但是我总是失败……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呵呵，我还是比较适合\x01",
            "在家里做老公和米拉诺的后援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……没关系，\x01",
            "现在那个人装着什么事\x01",
            "都没发生的样子回来了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47C2")

    label("loc_4754")


    ChrTalk(
        0xFE,
        (
            "……没关系，\x01",
            "现在那个人装着什么事\x01",
            "都没发生的样子回来了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C2")

    Jump("loc_4C63")

    label("loc_47C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_4A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49A1")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "老公和米拉诺\x01",
            "虽然相处得并不融洽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "我觉得他们只是互相不服输而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "米拉诺毕竟是他的女儿嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在她虽然表面上\x01",
            "不情愿地接手了她父亲的工作，\x01",
            "不过其实应该是出于同情吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对于我来说\x01",
            "真的要感谢米拉诺才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A3C")

    label("loc_49A1")


    ChrTalk(
        0xFE,
        (
            "老公和米拉诺\x01",
            "虽然相处得并不融洽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "我觉得他们只是互相不服输而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A3C")

    Jump("loc_4C63")

    label("loc_4A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_4B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC4")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他乘坐的定期船\x01",
            "竟然失踪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我该怎么办才好呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B19")

    label("loc_4AC4")


    ChrTalk(
        0xFE,
        (
            "他乘坐的定期船\x01",
            "竟然失踪了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我该怎么办才好呢……\x02",
    )

    CloseMessageWindow()

    label("loc_4B19")

    Jump("loc_4C63")

    label("loc_4B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4C63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C0D")
    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "好奇怪啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，\x01",
            "要是他现在回来就正好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "女儿也在家，\x01",
            "分开很久的一家人\x01",
            "都可以齐聚一堂了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C63")

    label("loc_4C0D")


    ChrTalk(
        0xFE,
        (
            "难道是\x01",
            "碰到什么事故了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "真是让人担心啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4C63")

    TalkEnd(0xD)
    Return()

    # Function_12_428E end

    def Function_13_4C67(): pass

    label("Function_13_4C67")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4CFA")

    ChrTalk(
        0xFE,
        "啊～虽然很烦，但是回来了就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果我没有接管这项工作，\x01",
            "现在早就应该呆在卢安了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55DB")

    label("loc_4CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DFA")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "根据梅贝尔小姐所说的来看，\x01",
            "定期船失踪很有可能是空贼团做的好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以赎金的数量来看，\x01",
            "父亲多半还活着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样母亲也总算\x01",
            "能够暂时安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E55")

    label("loc_4DFA")


    ChrTalk(
        0xFE,
        (
            "你们是来调查\x01",
            "这个事件的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托你们了！\x02",
    )

    CloseMessageWindow()

    label("loc_4E55")

    Jump("loc_55DB")

    label("loc_4E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F50")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        "哼，这次又是强盗啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，我搞不明白。\x01",
            "柏斯到底是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……话说回来，\x01",
            "居然没盯上我们家，\x01",
            "强盗们事先的调查还不够啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FAE")

    label("loc_4F50")


    ChrTalk(
        0xFE,
        "哼，这次又是强盗啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "真是的，我搞不明白。\x01",
            "柏斯到底是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAE")

    Jump("loc_55DB")

    label("loc_4FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_516C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50D5")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "反过来说……\x01",
            "飞艇的停航可能对我更有利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我父亲不在家的时候\x01",
            "可以争取到足够的时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "趁这个时候我会\x01",
            "尽力处理我父亲的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5169")

    label("loc_50D5")


    ChrTalk(
        0xFE,
        (
            "我和我父亲都是\x01",
            "从助手开始慢慢学做生意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "父亲的想法\x01",
            "我现在大都能够体会得到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5169")

    Jump("loc_55DB")

    label("loc_516C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_5304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5277")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "唉，\x01",
            "本来想把父亲的工作委任给西蒙的，\x01",
            "不过他还差的很远。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是被博尔德大叔\x01",
            "占了上风就糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，我必须得有一个助手。\x01",
            "还是把他叫上吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5301")

    label("loc_5277")


    ChrTalk(
        0xFE,
        "行商最重要就是信用第一。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "就算自己的业绩不好，\x01",
            "也不能连累其他人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5301")

    Jump("loc_55DB")

    label("loc_5304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_5429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53F7")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "我的父亲乘坐了\x01",
            "那艘失踪的定期船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他预约好的商谈\x01",
            "应该怎么处理才好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不，应该不会有事的，\x01",
            "他一定会好好地活着的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5426")

    label("loc_53F7")


    ChrTalk(
        0xFE,
        (
            "真是的，这个父亲，\x01",
            "老是要让母亲为他担心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5426")

    Jump("loc_55DB")

    label("loc_5429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_55DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5551")
    OP_A2(0x6)

    ChrTalk(
        0xFE,
        (
            "我难得回一次家，\x01",
            "老爸竟然不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我尽早赶回了柏斯，\x01",
            "父亲竟然还没有到家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且母亲她很担心呢，\x01",
            "总之先到外面打听一下是怎么回事再说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55DB")

    label("loc_5551")


    ChrTalk(
        0xFE,
        (
            "我难得回一次家，\x01",
            "老爸竟然不在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "他明明是个很守时的人啊。\x02",
    )

    CloseMessageWindow()

    label("loc_55DB")

    TalkEnd(0xE)
    Return()

    # Function_13_4C67 end

    def Function_14_55DF(): pass

    label("Function_14_55DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14E)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5605")
    Call(0, 21)
    Jump("loc_5E63")

    label("loc_5605")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_571B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5697")

    ChrTalk(
        0xFE,
        (
            "各位，\x01",
            "真的是多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "空贼也被抓住了，\x01",
            "这样我们又可以恢复正常的生活了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5718")

    label("loc_5697")


    ChrTalk(
        0xFE,
        (
            "闯入我家的蒙面男人们\x01",
            "终于被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "被盗走的东西\x01",
            "能够追回来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5718")

    Jump("loc_5E60")

    label("loc_571B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5821")

    ChrTalk(
        0xFE,
        "那可是枚非常重要的戒指……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "军队也好，游击士也行，\x01",
            "总之希望他们能快点把强盗抓住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这样下去，\x01",
            "我根本没有办法安心生活……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E60")

    label("loc_5821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5886")
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(
        0x14,
        (
            "马上就问完了，\x01",
            "你们可以不要打断我们吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 0)
    Jump("loc_5E60")

    label("loc_5886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_5A14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5994")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "昨晚，\x01",
            "我刚要哄孩子睡觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "突然有一群蒙面的男人\x01",
            "破门而入……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我怕丈夫担心，\x01",
            "就没有告诉他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，母亲的……母亲的遗物……\x01",
            "一枚戒指被他们抢走了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A11")

    label("loc_5994")


    ChrTalk(
        0xFE,
        (
            "我怕丈夫担心\x01",
            "就没有告诉他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "母亲的……母亲的遗物……\x01",
            "一枚戒指被他们抢走了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A11")

    Jump("loc_5E60")

    label("loc_5A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_5AB3")

    ChrTalk(
        0xFE,
        (
            "我丈夫的工作进展\x01",
            "好像比想象中的要顺利得多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近脸上也生气勃勃，\x01",
            "这样就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E60")

    label("loc_5AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_5C8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE8")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "自从他开始经营商店，\x01",
            "在家的时间也增多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "当然在家的时候\x01",
            "他也总是在整理商品\x01",
            "或者清查账簿……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是总比在军队时\x01",
            "每周只回来一次要好得多了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "开店做生意\x01",
            "也许不是什么坏事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C88")

    label("loc_5BE8")


    ChrTalk(
        0xFE,
        (
            "自从他开始经营商店，\x01",
            "在家的时间也增多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是总比在军队时\x01",
            "每周只回来一次要好得多了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C88")

    Jump("loc_5E60")

    label("loc_5C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_5E16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D67")
    OP_A2(0x7)

    ChrTalk(
        0xFE,
        (
            "我丈夫辞去了王国军的军官职务，\x01",
            "在柏斯超市开了一家店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "但是，我对此事是反对的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少，\x01",
            "等孩子长大一点\x01",
            "再这样做也不迟啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E13")

    label("loc_5D67")


    ChrTalk(
        0xFE,
        (
            "我丈夫辞去了王国军的军官职务，\x01",
            "在柏斯超市开了一家店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "至少，\x01",
            "等孩子长大一点\x01",
            "再这样做也不迟啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E13")

    Jump("loc_5E60")

    label("loc_5E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_5E60")

    ChrTalk(
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那个人的商店\x01",
            "是否在顺利营业呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E60")

    TalkEnd(0x10)

    label("loc_5E63")

    Return()

    # Function_14_55DF end

    def Function_15_5E64(): pass

    label("Function_15_5E64")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_5F05")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5EBB")

    ChrTalk(
        0xFE,
        (
            "不知道为什么\x01",
            "妈妈好像变得有精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嘿嘿嘿，太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F02")

    label("loc_5EBB")


    ChrTalk(
        0xFE,
        (
            "不知道为什么\x01",
            "街上的人们都很高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是，\x01",
            "妈妈却显得很悲伤……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F02")

    Jump("loc_626F")

    label("loc_5F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5F6C")

    ChrTalk(
        0xFE,
        "爸爸，就不能早点回来吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "妈妈看上去好难过啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_626F")

    label("loc_5F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FE5")
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(
        0x14,
        (
            "马上就问完了，\x01",
            "你们可以不要打断我们吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 0, 0)
    Jump("loc_626F")

    label("loc_5FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_6087")
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有一群不认识的人\x01",
            "昨天闯进我家来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我好害怕好害怕，\x01",
            "就和妈妈躲在床下面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_626F")

    label("loc_6087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_60DF")

    ChrTalk(
        0xFE,
        (
            "这次呀，\x01",
            "妈妈会带我去爸爸的店里玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我好期待呀～\x02",
    )

    CloseMessageWindow()
    Jump("loc_626F")

    label("loc_60DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_6188")

    ChrTalk(
        0xFE,
        (
            "爸爸比在军队的时候\x01",
            "有更多时间陪我玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我喜欢现在的爸爸。\x01",
            "以前呢，他的脸色总是很可怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_626F")

    label("loc_6188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_6205")

    ChrTalk(
        0xFE,
        (
            "什么时候我也能\x01",
            "帮爸爸做衣服就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我想成为爸爸的店员。\x02",
    )

    CloseMessageWindow()
    Jump("loc_626F")

    label("loc_6205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_626F")

    ChrTalk(
        0xFE,
        (
            "我爸爸的店里卖的衣服\x01",
            "很多都是他自己做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的衣服\x01",
            "也是爸爸给我做的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_626F")

    TalkEnd(0x11)
    Return()

    # Function_15_5E64 end

    def Function_16_6273(): pass

    label("Function_16_6273")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_6387")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6326")
    OP_A2(0x9)

    ChrTalk(
        0xFE,
        (
            "米拉诺有急事\x01",
            "去市长官邸找市长了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实市长与米拉诺\x01",
            "很久以前就是很好的朋友了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6384")

    label("loc_6326")


    ChrTalk(
        0xFE,
        (
            "其实市长与米拉诺\x01",
            "很久以前就是很好的朋友了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6384")

    Jump("loc_640B")

    label("loc_6387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_640B")

    ChrTalk(
        0xFE,
        (
            "听说南街区被强盗洗劫，\x01",
            "我还真是吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为昨晚\x01",
            "只有夫人一个人在家啊。 \x02",
        )
    )

    CloseMessageWindow()

    label("loc_640B")

    TalkEnd(0xF)
    Return()

    # Function_16_6273 end

    def Function_17_640F(): pass

    label("Function_17_640F")

    OP_A2(0x32D)
    OP_28(0x37, 0x1, 0x1)
    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "我正在打听情报。\x01",
            "能不能不要妨碍我？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_17_640F end

    def Function_18_6473(): pass

    label("Function_18_6473")

    TalkBegin(0x13)

    ChrTalk(
        0xFE,
        (
            "哟，游击士小姐们。\x01",
            "你们也是来打听情况的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "说真的，我们彼此都很辛苦啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_18_6473 end

    def Function_19_64EB(): pass

    label("Function_19_64EB")

    TalkBegin(0x14)

    ChrTalk(
        0xFE,
        (
            "这个家有件贵重的纪念品\x01",
            "被那些家伙们抢走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊呀呀……\x01",
            "你们就当作什么都没听到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "反正你们可以\x01",
            "直接去问这家的人。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x14)
    Return()

    # Function_19_64EB end

    def Function_20_65F2(): pass

    label("Function_20_65F2")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_6719")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F5")
    OP_A2(0xA)

    ChrTalk(
        0xFE,
        (
            "哎呀～\x01",
            "终于回到自己的家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "之前被关在那种\x01",
            "又阴暗又肮脏的地方，\x01",
            "家的温暖真是让我全身都舒服呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看来我的工作\x01",
            "都被米拉诺那家伙处理掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好～我也要精神十足地投入工作！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6719")

    label("loc_66F5")


    ChrTalk(
        0xFE,
        "好～我也要精神十足地投入工作！\x02",
    )

    CloseMessageWindow()

    label("loc_6719")

    TalkEnd(0x15)
    Return()

    # Function_20_65F2 end

    def Function_21_671D(): pass

    label("Function_21_671D")

    EventBegin(0x0)
    SetChrFlags(0x10, 0x10)
    TalkBegin(0x10)
    TurnDirection(0x0, 0x10, 0)
    TurnDirection(0x1, 0x10, 0)

    ChrTalk(
        0x101,
        "#000F请问，您是拉娜小姐吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        "是的……我就是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "请问找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样的，我们发现了一枚\x01",
            "与您委托中描述的很相似的戒指。\x02\x03",
            "如果可以的话，\x01",
            "请您确认一下好吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x10,
        "啊，真的吗……！？\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "宝石戒指\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)

    ChrTalk(
        0x10,
        "哎呀…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "没想到……\x01",
            "竟然还可以找回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这个就是您被盗的戒指吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(
        0x10,
        "嗯，就是它没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "这个戒指是我母亲的遗物。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样啊…………\x02\x03",
            "……很贵重的物品呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0x10,
        (
            "我真的没有想到，\x01",
            "竟然还有人\x01",
            "能够把它找回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "我该怎么表达\x01",
            "对你们的感激之情呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F呵呵，能够帮您取回这枚重要的戒指，\x01",
            "我们也都很开心呢。\x02\x03",
            "那么，\x01",
            "这样委托就算完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "嗯，\x01",
            "多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F再见。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【被盗的戒指】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x14E, 1)
    OP_28(0x13, 0x4, 0x10)
    OP_28(0x13, 0x1, 0x1)
    EventEnd(0x1)
    ClearChrFlags(0x10, 0x10)
    TalkEnd(0x10)
    Return()

    # Function_21_671D end

    SaveToFile()

Try(main)
