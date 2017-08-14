from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3107   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3107.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '凯诺娜上尉',                           # 9
        '洛伦斯少尉',                           # 10
        '理查德上校',                           # 11
        '黑衣男子',                             # 12
        '黑衣男子',                             # 13
        '黑衣男子',                             # 14
        '黑衣男子',                             # 15
        '黑衣男子',                             # 16
        '黑衣男子',                             # 17
        '特务艇',                               # 18
        '特务艇灯光',                           # 19
        '特务艇影子',                           # 20
        '士兵',                                 # 21
        '士兵',                                 # 22
        '士兵',                                 # 23
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
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH02200 ._CH',             # 02
        'ED6_DT07/CH02030 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00150 ._CH',             # 08
        'ED6_DT07/CH00151 ._CH',             # 09
        'ED6_DT07/CH00160 ._CH',             # 0A
        'ED6_DT07/CH00161 ._CH',             # 0B
        'ED6_DT06/CH20042 ._CH',             # 0C
        'ED6_DT07/CH00442 ._CH',             # 0D
        'ED6_DT07/CH01650 ._CH',             # 0E
        'ED6_DT07/CH01640 ._CH',             # 0F
        'ED6_DT07/CH01790 ._CH',             # 10
        'ED6_DT07/CH00502 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH02200P._CP',             # 02
        'ED6_DT07/CH02030P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00150P._CP',             # 08
        'ED6_DT07/CH00151P._CP',             # 09
        'ED6_DT07/CH00160P._CP',             # 0A
        'ED6_DT07/CH00161P._CP',             # 0B
        'ED6_DT06/CH20042P._CP',             # 0C
        'ED6_DT07/CH00442P._CP',             # 0D
        'ED6_DT07/CH01650P._CP',             # 0E
        'ED6_DT07/CH01640P._CP',             # 0F
        'ED6_DT07/CH01790P._CP',             # 10
        'ED6_DT07/CH00502P._CP',             # 11
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
        X                   = 8500,
        Z                   = 0,
        Y                   = 33940,
        Direction           = 90,
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
        X                   = 12530,
        Z                   = 0,
        Y                   = 33790,
        Direction           = 270,
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
        X                   = 21330,
        Z                   = 0,
        Y                   = 25970,
        Direction           = 0,
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
        X                   = 18240,
        Z                   = 0,
        Y                   = 25980,
        Direction           = 0,
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
        X                   = 22510,
        Z                   = 0,
        Y                   = 25840,
        Direction           = 0,
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
        X                   = 17040,
        Z                   = 0,
        Y                   = 25840,
        Direction           = 0,
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
        X                   = 17040,
        Z                   = 0,
        Y                   = 25840,
        Direction           = 0,
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
        X                   = 17040,
        Z                   = 0,
        Y                   = 25840,
        Direction           = 0,
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
        X                   = 17040,
        Z                   = 200,
        Y                   = 25840,
        Direction           = 0,
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 10390,
        Y                   = -1000,
        Z                   = 34100,
        Range               = 11000,
        Unknown_10          = 0x2AF8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 300,
        TriggerZ            = 0,
        TriggerY            = 45490,
        TriggerRange        = 800,
        ActorX              = 300,
        ActorZ              = 1300,
        ActorY              = 45490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_35E",          # 00, 0
        "Function_1_44E",          # 01, 1
        "Function_2_512",          # 02, 2
        "Function_3_528",          # 03, 3
        "Function_4_973",          # 04, 4
        "Function_5_13C4",         # 05, 5
        "Function_6_1583",         # 06, 6
        "Function_7_1D20",         # 07, 7
        "Function_8_1D65",         # 08, 8
        "Function_9_1DBE",         # 09, 9
        "Function_10_2275",        # 0A, 10
        "Function_11_22DA",        # 0B, 11
        "Function_12_2382",        # 0C, 12
        "Function_13_253F",        # 0D, 13
    )


    def Function_0_35E(): pass

    label("Function_0_35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_36C")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_37A")
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_388")
    OP_A3(0x3FC)
    Event(0, 12)

    label("loc_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DD")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 11810, 0, 31000, 0)
    SetChrPos(0x15, 8930, 0, 32619, 270)
    SetChrPos(0x16, 10250, 500, 34340, 180)

    label("loc_3DD")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_END)), "loc_42E")
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 12)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xB, 7830, 0, 33420, 199)
    SetChrPos(0xC, 11920, 0, 31940, 272)

    label("loc_42E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_43A"),
        (SWITCH_DEFAULT, "loc_44D"),
    )


    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A")
    Event(0, 3)

    label("loc_44A")

    Jump("loc_44D")

    label("loc_44D")

    Return()

    # Function_0_35E end

    def Function_1_44E(): pass

    label("Function_1_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_465")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 9)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_END)), "loc_470")
    OP_64(0x0, 0x1)

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_481")
    OP_1B(0x0, 0x0, 0xB)

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505")
    OP_6F(0xB, 1200)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    SetChrPos(0x11, 19820, 0, 15980, 180)
    SetChrPos(0x12, 19820, 0, 15980, 180)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 19820, 400, 15980, 180)
    OP_A1(0x11, 0xB)
    OP_A1(0x13, 0xC)
    OP_A1(0x12, 0xD)
    OP_6F(0xB, 560)
    OP_6F(0xD, 560)

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_511")
    OP_22(0xAC, 0x1, 0x64)

    label("loc_511")

    Return()

    # Function_1_44E end

    def Function_2_512(): pass

    label("Function_2_512")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_527")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_512")

    label("loc_527")

    Return()

    # Function_2_512 end

    def Function_3_528(): pass

    label("Function_3_528")

    EventBegin(0x0)
    OP_6D(20, 0, 6550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2130, 0, 2640, 0)
    SetChrPos(0x102, 870, 0, 2190, 0)
    SetChrPos(0x106, 1560, 0, 3520, 0)
    SetChrPos(0x107, 1680, 0, 1380, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F他们是……\x02",
    )

    CloseMessageWindow()
    OP_66(0x0)

    def lambda_5EB():
        OP_6D(23090, 0, 16160, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EB)
    Sleep(5000)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 6480, 45)
    OP_6D(10200, 0, 35370, 3000)
    Sleep(1000)
    OP_6D(-12420, 0, 7490, 3000)

    ChrTalk(
        0x106,
        (
            "#051F哼……\x01",
            "还真是阴魂不散的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F还有那艘飞艇也是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F那帮家伙果然和军队有关……\x01",
            "　\x02\x03",
            "不过他们好像和普通的士兵不同……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F那些黑衣人大概是被训练成\x01",
            "专门从事破坏工作的特殊部队吧。\x02\x03",
            "难怪他们的实力那么强悍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F爷、爷爷被抓到那里去了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F嗯，可能性越来越高了。\x01",
            "　\x02\x03",
            "不过……\x01",
            "要是在这里和他们产生冲突就糟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F是啊……\x02\x03",
            "不小心引起骚动的话，\x01",
            "恐怕要塞里的士兵都会被引来的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F趁现在还没被发现，\x01",
            "我们快想办法潜进那房子里去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x565)
    OP_28(0x44, 0x1, 0x4)
    Sleep(100)
    Fade(1000)
    OP_66(0x1)
    OP_6D(-13020, 0, 7160, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -13020, 0, 7160, 0)
    SetChrPos(0x102, -13020, 0, 7160, 0)
    SetChrPos(0x106, -13020, 0, 7160, 0)
    SetChrPos(0x107, -13020, 0, 7160, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_3_528 end

    def Function_4_973(): pass

    label("Function_4_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD8")
    EventBegin(0x0)
    OP_6D(10780, 0, 34400, 1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A78")
    OP_A2(0x54F)

    ChrTalk(
        0x14,
        "喂喂……他们被打晕了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "能把这些人打晕，\x01",
            "真是不简单的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "建筑物里面是空的！\x01",
            "赶快在营地里面搜索！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F（哇哇……被发现了！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（我们暂且先回去！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_A78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAD")

    ChrTalk(
        0x101,
        (
            "#002F（糟了！\x01",
            "　只能暂且先回去了！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_AAD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF1")

    ChrTalk(
        0x102,
        (
            "#012F（不好……\x01",
            "　暂时先撤退吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_AF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2A")

    ChrTalk(
        0x106,
        (
            "#057F（嘁……\x01",
            "　得重来一遍吗！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_B2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B62")

    ChrTalk(
        0x107,
        (
            "#065F（哇哇……\x01",
            "　被发现了～！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B62")

    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 7280, 45)
    SetChrPos(0x10B, -13200, 0, 6480, 45)
    OP_6D(-12420, 0, 7490, 0)
    OP_0D()
    EventEnd(0x0)
    Jump("loc_13C3")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_END)), "loc_11E2")
    EventBegin(0x0)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    OP_6D(10780, 0, 34400, 1500)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x106, 8)
    SetChrChipByIndex(0x107, 10)
    SetChrPos(0x106, 7580, 0, 27490, 0)
    SetChrPos(0x101, 8140, 0, 26150, 0)
    SetChrPos(0x102, 6300, 0, 26560, 0)
    SetChrPos(0x107, 7180, 0, 25690, 0)

    ChrTalk(
        0xB,
        (
            "唉……\x01",
            "难得王都有那么大的作战行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "我们竟被派在这里\x01",
            "看守一个老头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "别抱怨、别抱怨。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "为了王国，为了理想，\x01",
            "为了协助上校成就一番伟业……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "看守老头也是我们情报部隐秘部队——\x01",
            "『特务兵』的使命啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "哼！\x01",
            "你们的口号喊得还真响！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xC, 0x20)

    def lambda_DFC():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DFC)
    TurnDirection(0xB, 0x106, 400)

    NpcTalk(
        0xB,
        "特务兵",
        "什么……？\x02",
    )

    CloseMessageWindow()

    def lambda_E33():
        OP_6D(9740, 0, 30350, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E33)
    OP_6C(52000, 1500)

    NpcTalk(
        0xB,
        "特务兵",
        "不、不可能……！\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "特务兵",
        "#4P阿加特·科洛斯纳！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0xB, 13)
    SetChrSubChip(0xB, 0)
    Sleep(100)
    SetChrChipByIndex(0xC, 13)
    SetChrSubChip(0xC, 0)

    ChrTalk(
        0x106,
        "#054F太晚了！\x02",
    )

    CloseMessageWindow()

    def lambda_F05():
        OP_8E(0xFE, 0x299A, 0x0, 0x8476, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_F05)
    Sleep(50)

    def lambda_F25():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F25)
    Sleep(50)

    def lambda_F3F():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F3F)
    Sleep(100)

    def lambda_F59():
        OP_8E(0xFE, 0x299A, 0x0, 0x8476, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_F59)
    Sleep(300)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    Battle(0x252, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_F9C"),
        (SWITCH_DEFAULT, "loc_F9F"),
    )


    label("loc_F9C")

    OP_B4(0x0)
    Return()

    label("loc_F9F")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 12)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    OP_6D(8250, 0, 31140, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 7830, 0, 33420, 199)
    SetChrPos(0xC, 11920, 0, 31940, 272)
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 12)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrPos(0x106, 8240, 0, 31790, 45)
    SetChrPos(0x101, 8960, 0, 30390, 45)
    SetChrPos(0x102, 6540, 0, 31580, 45)
    SetChrPos(0x107, 7210, 0, 30100, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x106,
        (
            "#051F嘁……\x01",
            "两个活该的家伙。\x02\x03",
            "以前欠下这些家伙的旧帐，\x01",
            "这下总算连本带利还清了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        (
            "#506F又在公报私仇了～\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1144():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1144)

    def lambda_1152():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1152)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F现在开始就要抓紧时间了。\x02\x03",
            "闲话少说，\x01",
            "尽快带博士一起逃走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#560F是！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x568)
    OP_28(0x44, 0x1, 0x20)
    EventEnd(0x0)
    Jump("loc_13C3")

    label("loc_11E2")

    EventBegin(0x0)
    OP_6D(10780, 0, 34400, 1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1277")
    OP_A2(0x566)

    ChrTalk(
        0xB,
        (
            "唔……？\x01",
            "好像有什么动静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F（哇哇……被发现了！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（我们暂且先回去！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1361")

    label("loc_1277")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AC")

    ChrTalk(
        0x101,
        (
            "#002F（糟了！\x01",
            "　只能暂且先回去了！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1361")

    label("loc_12AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F0")

    ChrTalk(
        0x102,
        (
            "#012F（不好……\x01",
            "　暂时先撤退吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1361")

    label("loc_12F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1329")

    ChrTalk(
        0x106,
        (
            "#057F（嘁……\x01",
            "　得重来一遍吗！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1361")

    label("loc_1329")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1361")

    ChrTalk(
        0x107,
        (
            "#065F（哇哇……\x01",
            "　被发现了～！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1361")

    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 6480, 45)
    OP_6D(-12420, 0, 7490, 0)
    OP_0D()
    EventEnd(0x0)

    label("loc_13C3")

    Return()

    # Function_4_973 end

    def Function_5_13C4(): pass

    label("Function_5_13C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1582")
    OP_A2(0x567)
    OP_28(0x44, 0x1, 0x8)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-490, 0, 45500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(63000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -490, 0, 45980, 90)
    SetChrPos(0x102, -1420, 0, 46110, 90)
    SetChrPos(0x107, -490, 0, 45040, 90)
    SetChrPos(0x106, -1380, 0, 45220, 90)
    OP_0D()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#006F我说，\x01",
            "从这里潜进去不就行了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F不行……\x01",
            "窗户上有铁栏杆挡着。\x02\x03",
            "要做到一声不响地钻进去，\x01",
            "恐怕不是件容易的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        "#065F……………啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#057F这可真是中头彩了啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(
        0x101,
        "#004F咦……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3115   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1582")

    Return()

    # Function_5_13C4 end

    def Function_6_1583(): pass

    label("Function_6_1583")

    EventBegin(0x0)
    OP_6F(0xB, 1200)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    SetChrPos(0x11, 19820, 0, 15980, 180)
    SetChrPos(0x12, 19820, 0, 15980, 180)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 19820, 400, 15980, 180)
    OP_A1(0x11, 0xB)
    OP_A1(0x13, 0xC)
    OP_A1(0x12, 0xD)
    OP_6F(0xB, 560)
    OP_6F(0xD, 560)
    OP_6D(-1910, 0, 45400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x107, -1470, 0, 45910, 0)
    SetChrPos(0x106, -1230, 0, 44430, 0)
    SetChrPos(0x101, -2870, 0, 44560, 0)
    SetChrPos(0x102, -3200, 0, 46380, 0)
    TurnDirection(0x101, 0x107, 0)
    TurnDirection(0x107, 0x101, 0)
    TurnDirection(0x102, 0x101, 0)
    TurnDirection(0x106, 0x101, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F理查德上校……\x01",
            "那个人竟然就是幕后主谋啊。\x02\x03",
            "而且他好像也在找父亲呢……\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F啊啊……\x01",
            "这到底是怎么回事呢。\x02\x03",
            "而且那个带面具的男人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#057F那个混帐……\x01",
            "竟然在这种地方出现了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x106, 135, 400)

    ChrTalk(
        0x106,
        "#052F啊，少校好像要走了……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(21250, 0, 16520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4170, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x75, 0x1, 0x64)
    OP_6F(0xB, 1200)
    OP_6F(0xD, 1200)
    SetChrPos(0x8, 20330, 0, 28410, 180)
    SetChrPos(0x9, 19810, 0, 30280, 180)
    SetChrPos(0xA, 19810, 0, 27620, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x7)

    def lambda_188F():
        OP_6C(102000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_188F)

    def lambda_189F():
        OP_6D(19600, 3300, 18970, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_189F)
    Sleep(1000)
    OP_43(0xD, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0xE, 0x1, 0x0, 0x8)
    Sleep(400)
    OP_43(0xF, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0x10, 0x1, 0x0, 0x8)
    SetChrBattleFlags(0x9, 0x20)
    OP_8E(0x9, 0x4D80, 0xCE4, 0x4876, 0x7D0, 0x0)
    Sleep(1000)
    TurnDirection(0x9, 0x102, 400)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#280F呵呵……\x01",
            "你们能顺利逃走吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    Sleep(100)
    OP_8E(0x9, 0x4D80, 0xCE4, 0x4592, 0xBB8, 0x0)

    def lambda_1965():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1965)
    OP_8E(0x9, 0x4D80, 0xCE4, 0x3C50, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    Sleep(1000)
    OP_43(0x11, 0x1, 0x0, 0x9)
    WaitChrThread(0x11, 0x1)
    Sleep(3000)
    OP_44(0x101, 0xFF)
    Fade(1000)
    OP_6D(-1180, 0, 35690, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, -1920, 0, 35410, 135)
    SetChrPos(0x101, -840, 0, 35470, 135)
    SetChrPos(0x102, -2220, 0, 36430, 135)
    SetChrPos(0x107, -1130, 0, 36470, 135)
    OP_0D()

    ChrTalk(
        0x106,
        (
            "#051F好了……\x01",
            "一下子就全走光了。\x02\x03",
            "虽然很想和那混蛋做个了断，\x01",
            "但眼下还是把老爷子救出要紧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F既然不能从窗户钻进去，\x01",
            "那么就只有打倒看守的黑衣人了。\x02\x03",
            "速战速决！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#062F嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#510F……………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F约修亚？\x01",
            "你刚才没在听我们说话吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B81():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B81)

    def lambda_1B8F():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1B8F)

    def lambda_1B9D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1B9D)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F啊……艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F没、没事吧？\x01",
            "约修亚哥哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#052F喂喂，小子，没事吧。\x01",
            "这可不像平常那个冷静的你啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F抱、抱歉。\x01",
            "刚才发了一下呆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F约修亚……\x01",
            "哪里不舒服吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不要紧，没问题了。\x02\x03",
            "要先打倒门口那里的黑衣人吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#050F啊……快点开始吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x44, 0x1, 0x10)
    OP_44(0x11, 0xFF)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    EventEnd(0x0)
    Return()

    # Function_6_1583 end

    def Function_7_1D20(): pass

    label("Function_7_1D20")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0x4D80, 0xCE4, 0x4592, 0xBB8, 0x0)

    def lambda_1D3F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1D3F)
    OP_8E(0xFE, 0x4D80, 0xCE4, 0x3C50, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_1D20 end

    def Function_8_1D65(): pass

    label("Function_8_1D65")

    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0x4D80, 0x0, 0x6644, 0xBB8, 0x0)
    OP_8E(0xFE, 0x4D80, 0xCE4, 0x4592, 0xBB8, 0x0)

    def lambda_1D98():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1D98)
    OP_8E(0xFE, 0x4D80, 0xCE4, 0x3C50, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_1D65 end

    def Function_9_1DBE(): pass

    label("Function_9_1DBE")

    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x12, 0x4)
    OP_71(0xB, 0x2)
    OP_71(0xC, 0x2)
    OP_71(0xD, 0x2)
    OP_22(0xE6, 0x0, 0x64)
    OP_6F(0xB, 1200)
    OP_6F(0xD, 1200)
    OP_70(0xB, 0x474)
    OP_70(0xD, 0x474)
    OP_73(0xB)

    def lambda_1E06():
        OP_6C(0, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E06)

    def lambda_1E16():
        OP_6D(19690, 3300, 12830, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E16)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xB, 361)
    OP_6F(0xD, 361)
    OP_70(0xB, 0x230)
    OP_70(0xD, 0x230)
    OP_73(0xB)
    WaitChrThread(0x101, 0x2)
    OP_72(0xD, 0x4)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    PlayEffect(0x1, 0x1, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xB, 561)
    OP_6F(0xD, 561)
    OP_70(0xB, 0x244)
    OP_70(0xD, 0x244)
    OP_73(0xB)
    OP_6F(0xB, 581)
    OP_6F(0xD, 581)
    OP_70(0xB, 0x28A)
    OP_70(0xD, 0x28A)

    def lambda_1EEA():
        OP_6D(19690, 8020, 12830, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EEA)

    def lambda_1F02():
        OP_91(0x12, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1F02)
    OP_91(0x11, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)

    def lambda_1F31():
        OP_91(0x12, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1F31)
    OP_91(0x11, 0x0, 0x3E8, 0x0, 0x5DC, 0x0)

    def lambda_1F60():
        OP_91(0x12, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1F60)
    OP_91(0x11, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)

    def lambda_1F8F():
        OP_91(0x12, 0x0, 0x3E8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1F8F)
    OP_91(0x11, 0x0, 0x3E8, 0x0, 0xBB8, 0x0)

    def lambda_1FBE():
        OP_91(0x12, 0x0, 0x1F4, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1FBE)
    OP_91(0x11, 0x0, 0x1F4, 0x0, 0x7D0, 0x0)

    def lambda_1FED():
        OP_91(0x12, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1FED)
    OP_91(0x11, 0x0, 0x1F4, 0x0, 0x3E8, 0x0)

    def lambda_201C():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_201C)

    def lambda_2037():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2037)

    def lambda_2052():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF7CCA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2052)

    def lambda_206D():
        OP_6D(20020, 10000, -13080, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_206D)
    OP_6F(0xB, 651)
    OP_6F(0xD, 651)
    OP_70(0xB, 0x2A8)
    OP_70(0xD, 0x2A8)
    OP_73(0xB)
    OP_43(0x12, 0x0, 0x0, 0xA)

    def lambda_20AB():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_20AB)

    def lambda_20C6():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_20C6)

    def lambda_20E1():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF7CCA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_20E1)
    OP_71(0xB, 0x20)
    OP_71(0xD, 0x20)
    OP_6F(0xB, 680)
    OP_6F(0xD, 680)
    OP_70(0xB, 0x30C)
    OP_70(0xD, 0x30C)
    Sleep(1000)

    def lambda_2127():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2127)

    def lambda_2142():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2142)

    def lambda_215D():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF079A, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_215D)
    Sleep(500)

    def lambda_217D():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_217D)

    def lambda_2198():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2198)

    def lambda_21B3():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF079A, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_21B3)
    Sleep(500)

    def lambda_21D3():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_21D3)

    def lambda_21EE():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_21EE)

    def lambda_2209():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF079A, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2209)
    Sleep(500)

    def lambda_2229():
        OP_8F(0x11, 0x5370, 0x4E20, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2229)

    def lambda_2244():
        OP_8F(0x12, 0x5370, 0x4E20, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2244)

    def lambda_225F():
        OP_8F(0x13, 0x5370, 0x12C, 0xFFFF079A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_225F)
    Return()

    # Function_9_1DBE end

    def Function_10_2275(): pass

    label("Function_10_2275")

    OP_24(0x75, 0x5A)
    OP_24(0x77, 0x5A)
    Sleep(200)
    OP_24(0x75, 0x50)
    OP_24(0x77, 0x50)
    Sleep(200)
    OP_24(0x75, 0x46)
    OP_24(0x77, 0x46)
    Sleep(200)
    OP_24(0x75, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(200)
    OP_24(0x75, 0x32)
    OP_24(0x77, 0x32)
    Sleep(200)
    OP_24(0x75, 0x28)
    OP_24(0x77, 0x28)
    Sleep(200)
    OP_24(0x75, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(200)
    OP_23(0x75)
    OP_23(0x77)
    OP_23(0xCF)
    Return()

    # Function_10_2275 end

    def Function_11_22DA(): pass

    label("Function_11_22DA")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(11490, 0, 31730, 0)
    OP_0D()
    OP_62(0xC, 0xFFFFFE0C, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xC)

    NpcTalk(
        0xC,
        "特务兵",
        (
            "呜……啊……\x01",
            "怎么能让你们逃走……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_22(0xAC, 0x1, 0x64)
    OP_A2(0x3FA)
    OP_A2(0x56A)
    OP_28(0x44, 0x1, 0x80)
    NewScene("ED6_DT01/C3105   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_11_22DA end

    def Function_12_2382(): pass

    label("Function_12_2382")

    EventBegin(0x0)
    OP_6D(-12420, 0, 7490, 0)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 7280, 45)
    SetChrPos(0x10B, -13200, 0, 6480, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x10B,
        (
            "#102F要绕开飞艇坪到达码头\x01",
            "实在是太困难了。\x02\x03",
            "还是找找其它的逃跑路线吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F嗯，\x01",
            "我们最好不要再靠近飞艇坪了。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 11810, 0, 31000, 0)
    SetChrPos(0x15, 8930, 0, 32619, 270)
    SetChrPos(0x16, 10250, 500, 34340, 180)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2512")
    OP_28(0x44, 0x1, 0x2000)
    Jump("loc_2539")

    label("loc_2512")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2527")
    OP_28(0x44, 0x1, 0x4000)
    Jump("loc_2539")

    label("loc_2527")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2539")
    OP_28(0x44, 0x1, 0x8000)

    label("loc_2539")

    OP_A2(0x54D)
    EventEnd(0x0)
    Return()

    # Function_12_2382 end

    def Function_13_253F(): pass

    label("Function_13_253F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2554")
    OP_28(0x44, 0x1, 0x2000)
    Jump("loc_257B")

    label("loc_2554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2569")
    OP_28(0x44, 0x1, 0x4000)
    Jump("loc_257B")

    label("loc_2569")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257B")
    OP_28(0x44, 0x1, 0x8000)

    label("loc_257B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2763")
    EventBegin(0x0)
    OP_6D(-12420, 0, 7490, 0)
    SetChrPos(0x101, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 7280, 45)
    SetChrPos(0x10B, -13200, 0, 6480, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x107,
        (
            "#561F哈啊哈啊……\x02\x03",
            "#063F不、不要紧吗……\x01",
            "那些士兵们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F啊～不要担心了。\x01",
            "只是让他们晕过去了而已。\x02\x03",
            "#552F不过不管怎么说，\x01",
            "还是尽量避免战斗吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F要避开士兵们的搜索\x01",
            "找到逃出去的路线。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x14, 11810, 0, 31000, 0)
    SetChrPos(0x15, 8930, 0, 32619, 270)
    SetChrPos(0x16, 10250, 500, 34340, 180)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 9)
    OP_A2(0x54E)
    EventEnd(0x0)
    Jump("loc_27CB")

    label("loc_2763")

    OP_6D(-12420, 0, 7490, 0)
    SetChrPos(0x0, -12410, 0, 6160, 45)
    SetChrPos(0x106, -12420, 0, 5400, 45)
    SetChrPos(0x102, -12450, 0, 7280, 45)
    SetChrPos(0x107, -13200, 0, 7280, 45)
    SetChrPos(0x10B, -13200, 0, 6480, 45)
    OP_30(0x1)

    label("loc_27CB")

    Return()

    # Function_13_253F end

    SaveToFile()

Try(main)
