from ED6ScenarioHelper import *

def main():
    # 罗恩鲍姆酒店

    CreateScenaFile(
        FileName            = 'T4153   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4153.x',
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
        '士兵',                                 # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '王都格兰赛尔·西街区',                 # 17
        '格兰赛尔城方向',                       # 18
        '王都格兰赛尔·东街区',                 # 19
        '王都格兰赛尔·南街区',                 # 20
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 66000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 4200,
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
        'ED6_DT07/CH01650 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01650P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
    )

    DeclNpc(
        X                   = -2980,
        Z                   = 0,
        Y                   = 68330,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3120,
        Z                   = 0,
        Y                   = 68420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -32570,
        Z                   = 0,
        Y                   = 50050,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9530,
        Z                   = 250,
        Y                   = 32240,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9480,
        Z                   = 250,
        Y                   = 37480,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2560,
        Z                   = 0,
        Y                   = 29100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2640,
        Z                   = 0,
        Y                   = 29290,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3800,
        Z                   = 0,
        Y                   = 65780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -40080,
        Z                   = 0,
        Y                   = 17660,
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
        X                   = 100,
        Z                   = 0,
        Y                   = 104130,
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
        X                   = 40430,
        Z                   = 0,
        Y                   = 64060,
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
        X                   = 20,
        Z                   = 0,
        Y                   = -3500,
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
        X                   = 18520,
        Y                   = 0,
        Z                   = 44050,
        Range               = 1500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_299",          # 01, 1
        "Function_2_3BF",          # 02, 2
        "Function_3_53C",          # 03, 3
        "Function_4_93F",          # 04, 4
        "Function_5_9D5",          # 05, 5
        "Function_6_9D6",          # 06, 6
        "Function_7_A33",          # 07, 7
        "Function_8_C7C",          # 08, 8
        "Function_9_EC5",          # 09, 9
        "Function_10_108D",        # 0A, 10
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_268")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_276")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_276")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (110, "loc_282"),
        (SWITCH_DEFAULT, "loc_298"),
    )


    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295")
    OP_A2(0x62C)
    Event(0, 9)

    label("loc_295")

    Jump("loc_298")

    label("loc_298")

    Return()

    # Function_0_25A end

    def Function_1_299(): pass

    label("Function_1_299")

    OP_16(0x2, 0xFA0, 0xFFFDE4F0, 0xFFFECF50, 0x3005E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ED")
    OP_72(0x6, 0x8)
    OP_72(0x6, 0x20)
    OP_72(0x6, 0x2)
    OP_6F(0x6, 0)
    OP_72(0x2, 0x10)
    OP_72(0x5, 0x8)
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x2)
    OP_6F(0x5, 0)
    OP_72(0x3, 0x10)

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BE")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_43(0x8, 0x1, 0x0, 0x8)
    OP_43(0x9, 0x1, 0x0, 0x8)
    OP_43(0xA, 0x1, 0x0, 0x8)
    OP_43(0xB, 0x1, 0x0, 0x8)
    OP_43(0xC, 0x1, 0x0, 0x8)
    OP_43(0xD, 0x1, 0x0, 0x8)
    OP_43(0xE, 0x1, 0x0, 0x8)
    OP_43(0xF, 0x1, 0x0, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_364")

    label("loc_364")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_378")
    SetChrFlags(0xF, 0x80)
    OP_44(0xF, 0xFF)

    label("loc_378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_383")

    label("loc_383")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_3A0")
    SetChrFlags(0xC, 0x80)
    OP_44(0xC, 0xFF)
    SetChrFlags(0xE, 0x80)
    OP_44(0xE, 0xFF)

    label("loc_3A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x48, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_3AB")

    label("loc_3AB")

    OP_6B(4200, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BE")

    Return()

    # Function_1_299 end

    def Function_2_3BF(): pass

    label("Function_2_3BF")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_526")

    label("loc_3E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_526")

    label("loc_3FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_416")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_526")

    label("loc_416")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_526")

    label("loc_42F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_448")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_526")

    label("loc_448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_461")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_526")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_526")

    label("loc_47A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_526")

    label("loc_493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_526")

    label("loc_4AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_526")

    label("loc_4C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_526")

    label("loc_4DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_526")

    label("loc_4F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_510")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_526")

    label("loc_510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_526")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_526")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_526")

    label("loc_53B")

    Return()

    # Function_2_3BF end

    def Function_3_53C(): pass

    label("Function_3_53C")

    EventBegin(0x0)
    OP_6D(4100, 0, 67150, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x102, 3070, 0, 73100, 0)
    SetChrPos(0x101, 4410, 0, 72960, 0)

    def lambda_5A3():
        OP_8E(0xFE, 0x11A8, 0x0, 0x10482, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A3)
    Sleep(300)

    def lambda_5C3():
        OP_8E(0xFE, 0xC1C, 0x0, 0x1057C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5C3)
    WaitChrThread(0x101, 0x1)

    def lambda_5E3():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E3)
    WaitChrThread(0x102, 0x1)

    def lambda_5F6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F6)

    ChrTalk(
        0x101,
        (
            "#000F唔……\x01",
            "比想象中收获更大呢。\x02\x03",
            "而且，那个公爵\x01",
            "竟然是女王陛下的代理人……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F实际掌权的，\x01",
            "是理查德上校吧。\x02\x03",
            "而且，自己的阴谋\x01",
            "周围的人都浑然不觉。\x02\x03",
            "演技和操纵情报的手段\x01",
            "还真是高明啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F真是的，约修亚。\x01",
            "这可不是称赞敌人的时候啊。\x02\x03",
            "对了，那个公爵\x01",
            "好像去武术大会了呢。\x02\x03",
            "我们也去看看如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是呀……\x02\x03",
            "调查一下公爵的行动，\x01",
            "也没什么损失。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F那么就决定了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F我们赶快去王立竞技场吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，王立竞技场\x01",
            "是在哪个方向呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我记得应该是在东街区吧。\x02\x03",
            "先回到大街上然后往东走吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_53C end

    def Function_4_93F(): pass

    label("Function_4_93F")

    EventBegin(0x0)
    OP_6D(2190, 0, 46270, 0)
    OP_67(0, 29260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(432, 0)

    def lambda_984():
        OP_6C(90000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_984)
    Sleep(1000)

    def lambda_999():
        OP_6D(10350, 3620, 43920, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_999)

    def lambda_9B1():
        OP_67(0, 3740, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9B1)
    Sleep(10000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4132   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_93F end

    def Function_5_9D5(): pass

    label("Function_5_9D5")

    Return()

    # Function_5_9D5 end

    def Function_6_9D6(): pass

    label("Function_6_9D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A32")
    OP_8E(0xFE, 0xED8, 0x0, 0x9E3E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF466, 0x0, 0x9E3E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF466, 0x0, 0x10018, 0xBB8, 0x0)
    OP_8E(0xFE, 0xED8, 0x0, 0x100F4, 0xBB8, 0x0)
    Jump("Function_6_9D6")

    label("loc_A32")

    Return()

    # Function_6_9D6 end

    def Function_7_A33(): pass

    label("Function_7_A33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7B")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A66")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B83")

    label("loc_A66")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B83")

    label("loc_A8C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B83")

    label("loc_AB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B83")

    label("loc_AD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B83")

    label("loc_AFF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B25")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B83")

    label("loc_B25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B83")

    label("loc_B4A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B83")

    label("loc_B6F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B83")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C78")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C69")

    ChrTalk(
        0xFE,
        "你们是干什么的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F（糟糕……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（被发现了吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_C69")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 105, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_C78")

    Jump("Function_7_A33")

    label("loc_C7B")

    Return()

    # Function_7_A33 end

    def Function_8_C7C(): pass

    label("Function_8_C7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC4")
    OP_48()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCC")

    label("loc_CAF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCC")

    label("loc_CD5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF8), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCC")

    label("loc_CFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xCA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D22")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCC")

    label("loc_D22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D48")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCC")

    label("loc_D48")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCC")

    label("loc_D6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x44), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D93")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCC")

    label("loc_D93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCC")

    label("loc_DB8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DCC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xFE, 0x0)
    EventBegin(0x0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB2")

    ChrTalk(
        0xFE,
        "你们是干什么的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F（糟糕……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（被发现了吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_EB2")

    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4133   ._SN", 106, 0, 0)
    IdleLoop()
    EventEnd(0x1)
    Return()

    label("loc_EC1")

    Jump("Function_8_C7C")

    label("loc_EC4")

    Return()

    # Function_8_C7C end

    def Function_9_EC5(): pass

    label("Function_9_EC5")

    EventBegin(0x0)
    OP_6D(17700, 510, 43970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    OP_6C(90000, 0)
    SetChrPos(0x101, 17540, 510, 44210, 270)
    SetChrPos(0x102, 17540, 510, 43360, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#004F啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_F47():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F47)
    OP_6D(4010, 0, 38720, 3000)
    SetChrPos(0x101, 13280, 250, 49870, 225)
    SetChrPos(0x102, 14070, 250, 49980, 225)
    Sleep(1000)
    OP_6D(13610, 250, 50130, 3000)

    ChrTalk(
        0x102,
        (
            "#012F（巡逻好像已经开始了呢。）\x02\x03",
            "（如果被士兵发现了\x01",
            "　就会被送回旅馆……）\x02\x03",
            "（尽量避开士兵的巡逻视线，\x01",
            "　不被他们发现而到达大圣堂。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F（嗯，ＯＫ！）\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_9_EC5 end

    def Function_10_108D(): pass

    label("Function_10_108D")

    SetPlaceName(0xB4) # 罗恩鲍姆酒店
    Return()

    # Function_10_108D end

    SaveToFile()

Try(main)
