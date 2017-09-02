from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4312   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '特务兵',                               # 9
        '特务兵',                               # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '中队长',                               # 13
        '莉安妮',                               # 14
        '基库',                                 # 15
        '奈尔',                                 # 16
        '科洛蒂娅公主',                         # 17
        '尤莉亚中尉',                           # 18
        '雪拉',                                 # 19
        '奥利维尔',                             # 20
        '卡露娜',                               # 21
        '亚妮拉丝',                             # 22
        '库拉茨',                               # 23
        '克鲁茨',                               # 24
        '亲卫队员',                             # 25
        '亲卫队员',                             # 26
        '亲卫队员',                             # 27
        '亲卫队员',                             # 28
        '亲卫队员',                             # 29
        '亲卫队员',                             # 30
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
        'ED6_DT07/CH00100 ._CH',             # 00
        'ED6_DT07/CH00101 ._CH',             # 01
        'ED6_DT07/CH00110 ._CH',             # 02
        'ED6_DT07/CH00111 ._CH',             # 03
        'ED6_DT07/CH00170 ._CH',             # 04
        'ED6_DT07/CH00171 ._CH',             # 05
        'ED6_DT07/CH00340 ._CH',             # 06
        'ED6_DT07/CH00341 ._CH',             # 07
        'ED6_DT07/CH00440 ._CH',             # 08
        'ED6_DT07/CH01480 ._CH',             # 09
        'ED6_DT07/CH02320 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT07/CH02340 ._CH',             # 0C
        'ED6_DT07/CH02090 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00030 ._CH',             # 0F
        'ED6_DT07/CH00122 ._CH',             # 10
        'ED6_DT07/CH00444 ._CH',             # 11
        'ED6_DT07/CH00443 ._CH',             # 12
        'ED6_DT07/CH01240 ._CH',             # 13
        'ED6_DT07/CH01630 ._CH',             # 14
        'ED6_DT07/CH01260 ._CH',             # 15
        'ED6_DT07/CH01620 ._CH',             # 16
        'ED6_DT07/CH01320 ._CH',             # 17
        'ED6_DT07/CH00040 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH00340P._CP',             # 06
        'ED6_DT07/CH00341P._CP',             # 07
        'ED6_DT07/CH00440P._CP',             # 08
        'ED6_DT07/CH01480P._CP',             # 09
        'ED6_DT07/CH02320P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT07/CH02340P._CP',             # 0C
        'ED6_DT07/CH02090P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00030P._CP',             # 0F
        'ED6_DT07/CH00122P._CP',             # 10
        'ED6_DT07/CH00444P._CP',             # 11
        'ED6_DT07/CH00443P._CP',             # 12
        'ED6_DT07/CH01240P._CP',             # 13
        'ED6_DT07/CH01630P._CP',             # 14
        'ED6_DT07/CH01260P._CP',             # 15
        'ED6_DT07/CH01620P._CP',             # 16
        'ED6_DT07/CH01320P._CP',             # 17
        'ED6_DT07/CH00040P._CP',             # 18
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -57400,
        Y                   = 1000,
        Z                   = 2550,
        Range               = -43640,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFFFFFCCC,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_452",          # 00, 0
        "Function_1_4AB",          # 01, 1
        "Function_2_4CB",          # 02, 2
        "Function_3_998",          # 03, 3
        "Function_4_DF9",          # 04, 4
        "Function_5_1021",         # 05, 5
        "Function_6_39CE",         # 06, 6
        "Function_7_4279",         # 07, 7
    )


    def Function_0_452(): pass

    label("Function_0_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_460")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_477")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 6)

    label("loc_477")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_483"),
        (SWITCH_DEFAULT, "loc_499"),
    )


    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_496")
    OP_A2(0x659)
    Event(0, 5)

    label("loc_496")

    Jump("loc_499")

    label("loc_499")

    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_452 end

    def Function_1_4AB(): pass

    label("Function_1_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD")
    OP_1C(0x1, 0x0, 0x4)
    OP_72(0x1, 0x10)

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA")
    OP_1B(0x0, 0x0, 0x7)

    label("loc_4CA")

    Return()

    # Function_1_4AB end

    def Function_2_4CB(): pass

    label("Function_2_4CB")

    EventBegin(0x0)
    OP_6D(640, 0, -4630, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x108, 190, 0, -7530, 0)
    SetChrPos(0x101, -1330, 0, -8480, 0)
    SetChrPos(0x102, 570, 0, -8760, 0)

    ChrTalk(
        0x101,
        (
            "#000F这里就是『艾尔贝离宫』……\x02\x03",
            "唔－嗯，与城里\x01",
            "相比也不惶多让的豪华啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F啊，因为是王家的建筑嘛。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 11320, 0, -6220, 257)
    SetChrPos(0x9, 12050, 0, -5100, 264)
    SetChrPos(0xA, 12230, 0, -6940, 276)
    SetChrPos(0xB, 13520, 0, -5780, 285)
    TurnDirection(0x108, 0x8, 400)

    ChrTalk(
        0x108,
        "#070F好的，冲进去！\x02",
    )

    CloseMessageWindow()

    def lambda_68F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_68F)

    def lambda_69D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69D)

    def lambda_6AB():
        OP_6D(5840, 0, -6950, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6AB)

    def lambda_6C3():
        OP_67(0, 4710, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C3)

    def lambda_6DB():
        OP_6C(68000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6DB)

    ChrTalk(
        0x8,
        "你、你们是什么人！？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFD44, 0x0, 0xFFFFE4F8, 0x1388, 0x0)
    OP_8E(0x101, 0x316, 0x0, 0xFFFFE82C, 0x1388, 0x0)
    TurnDirection(0x101, 0x9, 0)

    ChrTalk(
        0x101,
        "#000F你们这些坏人不配知道！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不必多言，\x01",
            "我们上！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_796():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_796)

    def lambda_7AC():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AC)

    def lambda_7C2():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7C2)
    OP_6D(10400, 0, -6130, 700)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    Battle(0x3AD, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_808"),
        (SWITCH_DEFAULT, "loc_80B"),
    )


    label("loc_808")

    OP_B4(0x0)
    Return()

    label("loc_80B")

    EventBegin(0x0)
    OP_6D(9140, 0, -6380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, 9260, 0, -5570, 81)
    SetChrPos(0x108, 10200, 0, -6390, 96)
    SetChrPos(0x102, 8460, 0, -7540, 100)
    Sleep(500)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F嗯，公主殿下她们\x01",
            "被关在哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F肯定在这个巨大的建筑里面。\x02\x03",
            "一个不漏的\x01",
            "进行调查。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 270, 400)

    ChrTalk(
        0x108,
        (
            "#070F如果再磨磨蹭蹭的话，\x01",
            "前庭的那些家伙就会赶来了。\x02\x03",
            "尽快行动。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_4CB end

    def Function_3_998(): pass

    label("Function_3_998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 4)), scpexpr(EXPR_END)), "loc_9A0")
    Return()

    label("loc_9A0")

    OP_A2(0x654)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -52180, 0, 20500, 180)
    SetChrPos(0x9, -50170, 0, 20530, 180)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_9EE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_9EE)

    def lambda_9FC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FC)

    def lambda_A0A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0A)
    OP_6D(-50570, 0, 17760, 2000)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x108, -50910, 0, 8080, 0)
    SetChrPos(0x102, -50140, 0, 6930, 0)
    SetChrPos(0x101, -52160, 0, 7020, 0)

    def lambda_A6B():
        OP_8E(0xFE, 0xFFFF38C8, 0x0, 0x35D4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A6B)

    def lambda_A86():
        OP_8E(0xFE, 0xFFFF34FE, 0x0, 0x30DE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A86)

    def lambda_AA1():
        OP_8E(0xFE, 0xFFFF3BDE, 0x0, 0x3278, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA1)

    ChrTalk(
        0x8,
        "你们是什么人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "好像在哪儿见过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是他们！\x01",
            "武术大会取得优胜的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "游击士那些家伙！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F真聪明。\x01",
            "为了奖励你们，就让你们尝尝我拳头的滋味吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BB3():
        OP_8E(0xFE, 0xFFFF3878, 0x0, 0x9A92, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_BB3)

    def lambda_BCE():
        OP_8E(0xFE, 0xFFFF3878, 0x0, 0x9A92, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BCE)

    def lambda_BE9():
        OP_8E(0xFE, 0xFFFF3878, 0x0, 0x9A92, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE9)
    OP_6D(-51250, 0, 20190, 500)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x3AE, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_C34"),
        (SWITCH_DEFAULT, "loc_C37"),
    )


    label("loc_C34")

    OP_B4(0x0)
    Return()

    label("loc_C37")

    EventBegin(0x0)
    OP_6D(-48790, 0, 18830, 0)
    SetChrPos(0x8, -53840, 0, 18820, 298)
    SetChrPos(0x9, -53890, 0, 17410, 315)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -50330, 0, 18280, 295)
    SetChrPos(0x108, -50350, 0, 16900, 285)
    SetChrPos(0x102, -49040, 0, 18430, 283)

    ChrTalk(
        0x101,
        (
            "#000F呼，解决掉一批。\x02\x03",
            "看起来，他们好像是在\x01",
            "守卫这个豪华的大门……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D0F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_D0F)
    OP_8C(0x102, 315, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8D")

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "里面大概有什么重要的东西。\x02\x03",
            "进去调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF6")

    label("loc_D8D")


    ChrTalk(
        0x102,
        (
            "#010F这个就是管家先生说的\x01",
            "那个大房间的门吧。\x02\x03",
            "进去调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF6")

    EventEnd(0x0)
    Return()

    # Function_3_998 end

    def Function_4_DF9(): pass

    label("Function_4_DF9")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F92")
    OP_A2(0x655)
    EventBegin(0x0)
    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    OP_8B(0x1, 0xFFFF38FA, 0x5604, 0x190)
    OP_8B(0x2, 0xFFFF38FA, 0x5604, 0x190)
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

    ChrTalk(
        0x101,
        "#000F唉～怎么会这样！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F真是相当坚固的锁呢……\x01",
            "得先找到钥匙才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F44")

    ChrTalk(
        0x108,
        (
            "#070F唔，那就只能暂时\x01",
            "先到别的地方看看了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F8D")

    label("loc_F44")


    ChrTalk(
        0x108,
        (
            "#070F唔，去问问那个\x01",
            "年轻的管家吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x8)

    label("loc_F8D")

    EventEnd(0x1)
    Jump("loc_101B")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_END)), "loc_FE0")
    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
    OP_A2(0x658)
    OP_71(0x1, 0x10)
    OP_1C(0x1, 0x0, 0xFFFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "使用了备用钥匙。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_101B")

    label("loc_FE0")

    OP_8B(0x0, 0xFFFF38FA, 0x5604, 0x190)
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

    label("loc_101B")

    ClearMapFlags(0x80)
    Return()

    # Function_4_DF9 end

    def Function_5_1021(): pass

    label("Function_5_1021")

    EventBegin(0x0)
    OP_6D(-20, 0, 54380, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(57000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, 50, 250, 68860, 180)
    SetChrPos(0xD, 5680, 0, 58650, 180)
    SetChrPos(0xF, 3070, 0, 58560, 249)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x108, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -110, 0, 50960, 0)
    SetChrPos(0x102, -110, 0, 50960, 0)
    SetChrPos(0x108, -110, 0, 50960, 0)
    SetChrPos(0xE, -110, 0, 50960, 0)
    SetChrPos(0x13, -110, 0, 50960, 0)
    SetChrPos(0x11, -110, 0, 50960, 0)
    SetChrPos(0x12, -110, 0, 50960, 0)

    def lambda_114F():
        OP_6D(750, 0, 56890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_114F)

    def lambda_1167():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1167)

    def lambda_1179():
        OP_8E(0xFE, 0xFFFFFFC4, 0x0, 0xDFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1179)
    Sleep(500)

    def lambda_1199():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1199)

    def lambda_11AB():
        OP_8E(0xFE, 0x302, 0x0, 0xDBEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11AB)
    Sleep(500)

    def lambda_11CB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_11CB)

    def lambda_11DD():
        OP_8E(0xFE, 0xFFFFFC4A, 0x0, 0xDA34, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_11DD)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xF,
        "#140F你、你们……！？\x02",
    )

    CloseMessageWindow()

    def lambda_1212():
        OP_6D(2460, 0, 58180, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1212)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)

    def lambda_1239():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1239)

    def lambda_1247():
        TurnDirection(0xFE, 0xF, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1247)
    TurnDirection(0x101, 0xF, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#000F呀呵～我们来救你们了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F奈尔先生，\x01",
            "看起来安然无恙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#140F来救我们的，真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "艾丝蒂尔、约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "没想到能在这里相会……\x02",
    )

    CloseMessageWindow()

    def lambda_1327():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1327)

    def lambda_1335():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1335)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        "#000F……嗯？\x02",
    )

    CloseMessageWindow()

    def lambda_135C():
        OP_6D(70, 250, 68760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_135C)

    def lambda_1374():
        OP_67(0, 4420, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1374)

    def lambda_138C():
        OP_6C(11000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_138C)
    Sleep(1500)

    def lambda_13A1():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0x1041E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A1)
    Sleep(100)

    def lambda_13C1():
        OP_8E(0xFE, 0x1EA, 0x0, 0x1041E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13C1)
    Sleep(300)

    def lambda_13E1():
        OP_8E(0xFE, 0xFFFFF6E6, 0x0, 0x10266, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_13E1)
    Sleep(100)

    def lambda_1401():
        OP_8E(0xFE, 0x8AC, 0x0, 0x10568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1401)

    def lambda_141C():

        label("loc_141C")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_141C")

    QueueWorkItem2(0x108, 1, lambda_141C)

    def lambda_142D():

        label("loc_142D")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_142D")

    QueueWorkItem2(0xF, 1, lambda_142D)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F您、您就是公主殿下吧。\x02\x03",
            "初次见面，我们是\x01",
            "游击士协会的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "不是初次见面呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "艾丝蒂尔、约修亚。\x01",
            "终于按照约定再会了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎……？\x02\x03",
            "……………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0x101,
        "#000F啊啊，你不是科洛丝吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#040F艾丝蒂尔你真是的。\x02\x03",
            "虽没有立刻察觉，\x01",
            "但也不至于那么惊讶嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F话、话虽这么说，\x01",
            "可是身着礼服，长发披肩……\x02\x03",
            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……对不起呢，科洛丝。\x02\x03",
            "艾丝蒂尔这个人\x01",
            "没有什么疑心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我说！\x01",
            "你那是什～么意思！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#040F呵呵，我认为那是艾丝蒂尔\x01",
            "的一个优点哦。\x02\x03",
            "对了，约修亚。\x02\x03",
            "请依旧称呼我……\x01",
            "那个名字好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，我也感觉\x01",
            "你希望如此。\x02\x03",
            "不用本名可以吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#040F完全可以呀……\x01",
            "谢谢，我好开心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F？？？\x02\x03",
            "话说回来，为什么\x01",
            "科洛丝会在这里呢？\x02\x03",
            "还有，原本应该在这儿的公主殿下\x01",
            "为何到处都没有看见呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#140F我说啊，不就在你的面前吗。\x02\x03",
            "这位就是陛下的孙女，\x01",
            "科洛蒂娅公主殿下。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1835():
        OP_67(0, 6000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1835)
    OP_6C(45000, 1500)

    ChrTalk(
        0x101,
        (
            "#000F…………哦。\x02\x03",
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F#10A啊啊啊啊啊啊？\x05\x02",
    )

    OP_6E(253, 1000)
    OP_44(0x108, 0xFF)
    OP_44(0xF, 0xFF)

    ChrTalk(
        0x10,
        "对不起呀，我一直没说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "我本来打算与艾丝蒂尔\x01",
            "你们在王都再会的时候\x01",
            "告诉你们的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "结果被情报部的人拘捕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F可、可是，为什么？\x02\x03",
            "为什么公主殿下要藏身\x01",
            "于一个普通的学校呢……！？\x02\x03",
            "而、而且我们称呼\x01",
            "你科洛丝，这可以吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "以后也请务必\x01",
            "叫我科洛丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "科洛蒂娅·\x01",
            "冯·奥赛雷丝……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "乔儿把我本名的开始和末尾放在一起，\x01",
            "给我起了这样一个爱称。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是这样啊……\x02\x03",
            "嗯，那么头发呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "啊，这是假发。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "如果真的是这种发型，\x01",
            "在学院里面的生活就不方便了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#140F我也有够粗心的了……\x02\x03",
            "虽然以前看过您的照片，\x01",
            "但在市长官邸事件中见到您时\x01",
            "竟然完全没有注意到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "呵呵，对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "杜南王叔和戴尔蒙市长\x01",
            "都没有察觉，\x01",
            "真是有些意外的效果呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哦，说起来\x01",
            "那个公爵还是你的亲戚呢。\x02\x03",
            "嗯，对了。\x01",
            "最重要的事情反而忘记了。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x10, 0x2BC, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把至今为止的事情经过一一道来，\x01",
            "也说明了接受女王的委托\x01",
            "前来营救的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x101, 0xFFFFFDE4, 0x0, 0x1041E, 0x7D0, 0x0)

    ChrTalk(
        0x10,
        "是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "艾丝蒂尔、约修亚。\x01",
            "还有那位金大哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "你们能来营救我们，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈哈，不用那么在意啦。\x02\x03",
            "如果知道被拘捕的\x01",
            "是科洛丝的话，\x01",
            "就算不委托我们也会来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈，的确如此呢。\x02\x03",
            "与我们相比，\x01",
            "更应该感谢的是陛下。\x02\x03",
            "她不顾自己的所处的境况\x01",
            "也要委托我们来救你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F的确，公主殿下既然已经平安无事，\x01",
            "那么陛下就可以拒绝上校的要求了……\x02\x03",
            "也许陛下已经视死如归了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "好……\x01",
            "祖母大人就是那样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "无论如何也不会妥协，\x01",
            "可是这样祖母大人她……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, -230, 0, 55310, 346)
    SetChrChipByIndex(0x8, 8)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xC, 1020, 0, 56140, 0)
    SetChrPos(0x8, 50, 0, 54770, 0)

    ChrTalk(
        0xC,
        (
            "所谓闹剧，就是\x01",
            "这样的吗……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_203D():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_203D)

    def lambda_204B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_204B)

    def lambda_2059():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2059)

    def lambda_2067():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2067)

    def lambda_2075():
        OP_6D(800, 0, 61890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2075)

    def lambda_208D():
        OP_6E(297, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_208D)
    Sleep(2000)

    ChrTalk(
        0xD,
        "公、公主殿下～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "小莉安妮！？\x02",
    )

    CloseMessageWindow()

    def lambda_20C2():
        OP_6D(850, 0, 60760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20C2)

    def lambda_20DA():
        OP_6E(261, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20DA)
    SetChrChipByIndex(0x101, 0)

    def lambda_20EF():
        OP_8E(0xFE, 0xFFFFFD26, 0x0, 0xF9D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20EF)
    Sleep(200)
    SetChrChipByIndex(0x102, 2)

    def lambda_2114():
        OP_8E(0xFE, 0x190, 0x0, 0xF96A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2114)
    Sleep(100)
    SetChrChipByIndex(0x108, 4)

    def lambda_2139():
        OP_8E(0xFE, 0xFFFFF68C, 0x0, 0xF604, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2139)
    Sleep(200)

    def lambda_2159():
        OP_8E(0xFE, 0xA, 0x0, 0xFFEF, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2159)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        "#000F那、那个小女孩是谁！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x1)

    ChrTalk(
        0x10,
        "摩尔根将军的孙女……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "为了动摇囚禁在哈肯大门\x01",
            "的将军的意志，\x01",
            "而被带到这里来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F你们的所作所为\x01",
            "是在与女王陛下作对……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "你说的我收下了，\x01",
            "但是不要以为这样就可以威胁我！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我们情报部的队员，为了理想，\x01",
            "就算化成鬼、化成修罗也在所不惜！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这、这种事\x01",
            "还有脸自吹自擂！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "中队长，我和你做一笔交易。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "请让我代替那个\x01",
            "孩子，作为人质。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哦……\x01",
            "我才不会上当呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "对于我们这些人而言，\x01",
            "是没有亲手杀死王族的勇气的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "与之相比，摩尔根将军的\x01",
            " \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "既有作为人质的价值，\x01",
            "要打伤她又不会很难下手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "……你们…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F……无耻～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F哎呀呀，无可救药的家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "哼，随便你们怎么胡说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "很快就要到巡回部队\x01",
            "从队空中庭园归来的时刻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "到时候会把亲卫队还有游击士\x01",
            "在这儿一网打尽！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊～那已经不可能了哟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "他们在来这儿的途中\x01",
            "就已经被我们全部消灭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2684():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2684)

    def lambda_2692():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2692)

    def lambda_26A0():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_26A0)

    def lambda_26AE():
        OP_6D(500, 0, 59390, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26AE)
    OP_6E(280, 800)

    def lambda_26CF():

        label("loc_26CF")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_26CF")

    QueueWorkItem2(0xC, 1, lambda_26CF)

    def lambda_26E0():

        label("loc_26E0")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_26E0")

    QueueWorkItem2(0x8, 1, lambda_26E0)

    def lambda_26F1():

        label("loc_26F1")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_26F1")

    QueueWorkItem2(0xD, 1, lambda_26F1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0x12, 0x20)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 16)
    ClearChrFlags(0x12, 0x80)

    def lambda_2726():

        label("loc_2726")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2726")

    QueueWorkItem2(0x12, 1, lambda_2726)
    OP_96(0x12, 0xFFFFF7A4, 0x0, 0xD5C0, 0x3E8, 0x1F40)
    OP_99(0x12, 0x2, 0x4, 0xBB8)
    PlayEffect(0x8, 0xFF, 0xFF, 50, 1000, 54770, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    TurnDirection(0x8, 0x12, 0)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 18)

    def lambda_27A3():
        OP_94(0x1, 0xFE, 0xB4, 0xBB8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27A3)
    OP_99(0x12, 0x4, 0x9, 0xBB8)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)

    ChrTalk(
        0x8,
        "#10A啊！\x05\x02",
    )

    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 17)

    def lambda_27E2():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_27E2)
    Sleep(500)

    def lambda_27F7():
        OP_8E(0xFE, 0xFFFFF4DE, 0x0, 0xD912, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27F7)
    Sleep(100)
    OP_8F(0xC, 0x6CC, 0x0, 0xDACA, 0x1388, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_96(0x12, 0xFFFFF858, 0x0, 0xDA16, 0x1F4, 0x1F40)
    TurnDirection(0xD, 0x12, 400)
    Sleep(200)

    ChrTalk(
        0xC,
        "什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "呜……呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "呜哇哇啊啊啊啊啊啊！\x02",
    )

    CloseMessageWindow()

    def lambda_2885():

        label("loc_2885")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2885")

    QueueWorkItem2(0x101, 1, lambda_2885)

    def lambda_2896():

        label("loc_2896")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_2896")

    QueueWorkItem2(0x102, 1, lambda_2896)

    def lambda_28A7():

        label("loc_28A7")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_28A7")

    QueueWorkItem2(0x108, 1, lambda_28A7)

    def lambda_28B8():

        label("loc_28B8")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_28B8")

    QueueWorkItem2(0xF, 1, lambda_28B8)

    def lambda_28C9():

        label("loc_28C9")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_28C9")

    QueueWorkItem2(0x10, 1, lambda_28C9)

    ChrTalk(
        0x12,
        (
            "#020F好了好了，已经没事了哟。\x02\x03",
            "艾丝蒂尔、约修亚。\x01",
            "真是好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F雪、雪拉姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F终于来了吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "哪、哪里有这么\x01",
            "慢条斯理的打招呼！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "哎哟哟，简直不解风情。\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x8, 0xFF, 0xFF, 1590, 1000, 54930, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 18)

    def lambda_2A00():
        OP_96(0xFE, 0xBD6, 0x0, 0xDFFC, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2A00)

    ChrTalk(
        0xC,
        "#10A呜哦……\x05\x02",
    )

    Sleep(400)

    def lambda_2A33():

        label("loc_2A33")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2A33")

    QueueWorkItem2(0x12, 1, lambda_2A33)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2A4F():
        OP_96(0xFE, 0x442, 0x0, 0xDDCC, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2A4F)
    Sleep(200)
    OP_99(0x12, 0x2, 0x4, 0xFA0)
    PlayEffect(0x8, 0xFF, 0xFF, 3180, 1500, 56940, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xC, 0x4)

    def lambda_2AB5():
        OP_6D(6320, 0, 57730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AB5)

    def lambda_2ACD():
        OP_8F(0xFE, 0x2508, 0x1F4, 0xDCE6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2ACD)
    OP_99(0x12, 0x4, 0x9, 0x7D0)
    WaitChrThread(0xC, 0x1)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 17)

    ChrTalk(
        0xC,
        "#10A呜啊！\x05\x02",
    )

    PlayEffect(0x12, 0xFF, 0xC, 0, 0, -500, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6B(3070, 0)
    OP_6B(3000, 80)
    Sleep(500)
    OP_8F(0xC, 0x2512, 0x0, 0xDCE6, 0x3E8, 0x0)
    OP_99(0xC, 0x0, 0x3, 0x7D0)

    ChrTalk(
        0x12,
        "#020F刚才那是附赠品哟。\x02",
    )

    CloseMessageWindow()
    OP_6D(280, 0, 58100, 2000)

    ChrTalk(
        0x101,
        (
            "#000F好、好狠啊～\x02\x03",
            "咦，刚才发起攻击的是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……奥利维尔吗？\x02",
    )

    CloseMessageWindow()
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 14)
    TurnDirection(0x12, 0x13, 400)

    ChrTalk(
        0x13,
        "Bingo⊙\x02",
    )

    CloseMessageWindow()

    def lambda_2C3E():

        label("loc_2C3E")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C3E")

    QueueWorkItem2(0x12, 1, lambda_2C3E)

    def lambda_2C4F():

        label("loc_2C4F")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C4F")

    QueueWorkItem2(0xD, 1, lambda_2C4F)

    def lambda_2C60():

        label("loc_2C60")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C60")

    QueueWorkItem2(0x101, 1, lambda_2C60)

    def lambda_2C71():

        label("loc_2C71")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C71")

    QueueWorkItem2(0x102, 1, lambda_2C71)

    def lambda_2C82():

        label("loc_2C82")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C82")

    QueueWorkItem2(0x108, 1, lambda_2C82)

    def lambda_2C93():

        label("loc_2C93")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2C93")

    QueueWorkItem2(0xF, 1, lambda_2C93)

    def lambda_2CA4():

        label("loc_2CA4")

        TurnDirection(0xFE, 0x13, 0)
        OP_48()
        Jump("loc_2CA4")

    QueueWorkItem2(0x10, 1, lambda_2CA4)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2CC5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2CC5)

    def lambda_2CD7():
        OP_8E(0xFE, 0x1E, 0x0, 0xD7F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2CD7)
    Sleep(100)
    OP_6D(550, 0, 58110, 2000)

    ChrTalk(
        0x13,
        (
            "#030F哎呀呀。\x01",
            "主角华丽登场了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)

    def lambda_2D85():
        OP_8E(0xFE, 0xFFFFFB78, 0x0, 0xE128, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D85)
    Sleep(100)
    SetChrChipByIndex(0x102, 65535)

    def lambda_2DAA():
        OP_8E(0xFE, 0xF0, 0x0, 0xE2C2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2DAA)
    Sleep(300)

    def lambda_2DCA():
        OP_8E(0xFE, 0x78, 0x0, 0xE90C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2DCA)
    Sleep(500)
    SetChrChipByIndex(0x108, 65535)

    def lambda_2DEF():
        OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xE452, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_2DEF)
    Sleep(100)

    def lambda_2E0F():
        OP_8E(0xFE, 0x9A6, 0x0, 0xE902, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2E0F)
    Sleep(100)
    Sleep(2000)
    OP_44(0x12, 0xFF)

    ChrTalk(
        0x108,
        (
            "#070F哈哈，这不是那位\x01",
            "怪腔怪调的兄弟吗。\x02\x03",
            "对了，雪拉扎德，\x01",
            "真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x108, 400)

    ChrTalk(
        0x12,
        (
            "#020F你好，久疏问候了。\x02\x03",
            "没想到金兄你也\x01",
            "到利贝尔来了呢。\x02\x03",
            "听说你和艾丝蒂尔\x01",
            "他们在一起时，\x01",
            "我就没有那么担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈，你真是太过\x01",
            "高估我了。\x02\x03",
            "不过我说你啊……\x01",
            "变得相当漂亮了呢。\x02\x03",
            "说实话，我都有些认不出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#020F哎、哎呀、真的吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 400)
    Sleep(500)
    TurnDirection(0x13, 0x108, 400)
    Sleep(500)
    TurnDirection(0x13, 0x12, 400)

    ChrTalk(
        0x13,
        (
            "#030F哼·哼·哼，\x01",
            "我好生嫉妒。\x02\x03",
            "在把我\x01",
            "尽情的享用了之后，\x01",
            "又像垃圾一样抛弃了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 400)

    ChrTalk(
        0x12,
        (
            "#020F哎呀，奥利维尔，\x01",
            "你不是与爱娜小姐相逢了吗？\x02\x03",
            "还想脚踏两只船啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 400)

    ChrTalk(
        0x13,
        (
            "#030F对不起呢。\x01",
            "都是我的错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F还真是的……\x01",
            "大家都还是老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F可是雪拉姐姐，\x01",
            "竟然来到王都了。\x02\x03",
            "王国军不是把\x01",
            "关所全部封锁了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x102, 400)

    ChrTalk(
        0x12,
        (
            "#020F嗯，所以我们是用小船\x01",
            "从瓦雷利亚湖过来的。\x02\x03",
            "在王都的码头上的岸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F原来如此，深思熟虑呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F可是，为何会又和\x01",
            "这个骗吃骗喝的演奏家在一起呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#020F我刚踏出\x01",
            "王都的协会就撞见他了。\x02\x03",
            "他死皮赖脸的跟着我，甩都甩不掉，\x01",
            "没办法，我就只有带他来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#030F哈·哈·哈。\x02\x03",
            "如此有趣的事情\x01",
            "怎么能缺少了我的参与呢。\x02\x03",
            "对了，那位小姐是……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_8E(0x102, 0x3AC, 0x0, 0xE36C, 0x7D0, 0x0)
    TurnDirection(0x102, 0x10, 400)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，我给你介绍一下。\x02\x03",
            "女王陛下的孙女－\x01",
            "科洛蒂娅公主殿下。\x02\x03",
            "是我和约修亚的朋友。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34D7():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34D7)

    def lambda_34E5():
        TurnDirection(0xFE, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34E5)
    OP_44(0x10, 0xFF)

    ChrTalk(
        0x10,
        "两位，初次见面。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "你们能来协助我\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#020F不用在意，\x01",
            "这也是游击士的义务嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#030F呵，拯救美丽的公主\x01",
            "是绅士的无上荣誉呢。\x02\x03",
            "能见到您是我的光荣，公主殿下。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x11, -110, 0, 50960, 0)
    SetChrPos(0xE, -110, 0, 50960, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    ChrTalk(
        0x11,
        "科洛丝，你没事吧！\x02",
    )

    CloseMessageWindow()

    def lambda_36A3():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36A3)

    def lambda_36B1():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36B1)

    def lambda_36BF():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_36BF)

    def lambda_36CD():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_36CD)

    def lambda_36DB():
        OP_8F(0xFE, 0x4A6, 0x0, 0xD9EE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_36DB)

    def lambda_36F6():
        OP_8F(0xFE, 0xFFFFF948, 0x0, 0xDEF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36F6)
    Sleep(500)

    def lambda_3716():

        label("loc_3716")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3716")

    QueueWorkItem2(0x101, 1, lambda_3716)

    def lambda_3727():

        label("loc_3727")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3727")

    QueueWorkItem2(0x102, 1, lambda_3727)

    def lambda_3738():

        label("loc_3738")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3738")

    QueueWorkItem2(0x108, 1, lambda_3738)

    def lambda_3749():

        label("loc_3749")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3749")

    QueueWorkItem2(0x13, 1, lambda_3749)
    ClearChrFlags(0x11, 0x80)

    def lambda_375F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_375F)

    def lambda_3771():
        OP_8E(0xFE, 0xFFFFFEA2, 0x0, 0xDF7A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3771)
    Sleep(1000)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x4)

    def lambda_37A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_37A0)

    def lambda_37B2():
        OP_8E(0xFE, 0xFFFFFCAE, 0x3E8, 0xDF66, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_37B2)
    Sleep(1000)

    ChrTalk(
        0x10,
        "尤莉亚中尉，基库！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "啾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "啾啾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "啾——啾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "呵呵，太好了。\x01",
            "又和你见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#170F殿下，您平安无事就好……\x02\x03",
            "真的……真的太好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "尤莉亚中尉你也是……\x01",
            "精神焕发呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，大家和伪装行动的\x01",
            "游击士们还有亲卫队队员汇合了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "安顿好其他的人质之后，\x01",
            "艾丝蒂尔她们决定去确认当前的状况。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x4B, 0x4, 0x10)
    OP_28(0x4C, 0x1, 0x40)
    OP_28(0x4C, 0x1, 0x80)
    OP_28(0x4C, 0x1, 0x100)
    OP_28(0x4D, 0x4, 0x2)
    OP_28(0x4D, 0x4, 0x4)
    OP_28(0x4D, 0x1, 0x1)
    OP_28(0x4D, 0x1, 0x2)
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1021 end

    def Function_6_39CE(): pass

    label("Function_6_39CE")

    EventBegin(0x0)
    OP_6D(920, 250, 64110, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(1560, 0)
    OP_6C(45000, 0)
    OP_6E(588, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x11, -140, 250, 68110, 180)
    SetChrPos(0x102, -2000, 0, 66540, 90)
    SetChrPos(0x13, -3440, 0, 65990, 90)
    SetChrPos(0x108, -3210, 0, 67070, 90)
    SetChrPos(0x101, 2020, 0, 66210, 270)
    SetChrPos(0x10, 2630, 0, 67290, 270)
    SetChrPos(0x12, 2980, 0, 66110, 270)
    SetChrPos(0x17, -50, 0, 65269, 0)
    SetChrPos(0x16, 930, 0, 64510, 0)
    SetChrPos(0x14, -1040, 0, 64410, 0)
    SetChrPos(0x15, -50, 0, 63940, 0)
    SetChrPos(0x18, -940, 0, 61330, 0)
    SetChrPos(0x19, 50, 0, 61320, 0)
    SetChrPos(0x1A, 1030, 0, 61320, 0)
    SetChrPos(0x1B, -940, 0, 60000, 0)
    SetChrPos(0x1C, 50, 0, 60000, 0)
    SetChrPos(0x1D, 1030, 0, 60000, 0)
    SetChrChipByIndex(0x10, 24)
    OP_6D(920, 250, 67890, 2000)

    ChrTalk(
        0x11,
        (
            "#170F#5P现在我就对解放格兰赛尔城\x01",
            "和营救女王陛下的作战进行说明。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 400)
    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#170F#5P首先，由约修亚等三人为一组\x01",
            "从地下水路攻入格兰赛尔城的地下。\x01",
            "　\x02\x03",
            "然后迅速赶往亲卫队值勤室，\x01",
            "启动城门的开关装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，巨大的烟花就要开始燃放了啊。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#035F哼哼……不管怎样，\x01",
            "舞台剧最后一幕终于开演了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#170F#5P在城门打开的同时，\x01",
            "全体亲卫队成员以及四名游击士\x01",
            "就从市街区直接冲进城内。\x02\x03",
            "尽量制造草木皆兵的效果，\x01",
            "将敌人全部引入城内集中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "好的，交给我们去办吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "太好了，我已经跃跃欲试了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#176F#5P最后还要说的是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 400)
    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#175F#5P……公主殿下，\x01",
            "您真的下定决心要参战吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#049F#2P对不起……\x01",
            "我一定要救出祖母大人。\x02\x03",
            "#040F而且，我还会操纵飞艇……\x01",
            "　\x02\x03",
            "所以请让我也尽一份力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#175F#5P唉……\x02\x03",
            "如果早知道会发生这样的事情，\x01",
            "当初就不教你操纵飞艇的方法了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#2P不用担心啦，尤莉亚中尉。\x02\x03",
            "科洛丝就交给我们来照顾吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#020F#2P我以『银闪』之名作担保，\x01",
            "发誓一定会保护公主的安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#176F#5P我知道了……拜托你们了。\x02\x03",
            "#170F在将敌人的兵力集中于城内之后，\x01",
            "艾丝蒂尔等三人为一组就乘坐\x01",
            "特务飞艇在空中庭园强行着陆。\x02\x03",
            "然后就冲入女王宫，\x01",
            "救出艾莉茜雅女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#2P明白了！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(400)

    ChrTalk(
        0x11,
        (
            "#176F#5P正午钟响的同时开始作战，\x01",
            "在此之前请在各自的地点等候。\x02\x03",
            "#177F全体听命，行动开始！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(300, 200, -1, -1)
    SetChrName("全员")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5SYes，Madam！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T4302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_39CE end

    def Function_7_4279(): pass

    label("Function_7_4279")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E5")

    ChrTalk(
        0x101,
        (
            "#002F还没有完成女王陛下的委托呢。\x01",
            "　\x02\x03",
            "快点把公主殿下找出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C0")

    label("loc_42E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4350")

    ChrTalk(
        0x102,
        (
            "#012F等把人质都解放了，\x01",
            "再离开这里吧。\x02\x03",
            "总之要先把里面彻底调查一番。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C0")

    label("loc_4350")


    ChrTalk(
        0x108,
        (
            "#072F还没有找到公主殿下和其他人质呢。\x01",
            "　\x02\x03",
            "先把那些坏家伙们\x01",
            "一个不留地干掉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C0")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_4279 end

    SaveToFile()

Try(main)
