from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4111   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60089",
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
        '修女艾伦',                             # 9
        '魔兽',                                 # 10
        '魔兽',                                 # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '魔兽',                                 # 16
        '魔兽',                                 # 17
        '特务兵',                               # 18
        '特务兵',                               # 19
        '卡露娜',                               # 20
        '亚妮拉丝',                             # 21
        '库拉茨',                               # 22
        '克鲁茨',                               # 23
        '尤莉亚中尉',                           # 24
        '亲卫队员',                             # 25
        '亲卫队员',                             # 26
        '亲卫队员',                             # 27
        '亲卫队员',                             # 28
        '亲卫队员',                             # 29
        '亲卫队员',                             # 30
        '亲卫队员',                             # 31
        '亲卫队员',                             # 32
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
        'ED6_DT07/CH01410 ._CH',             # 00
        'ED6_DT09/CH10820 ._CH',             # 01
        'ED6_DT09/CH10821 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00110 ._CH',             # 05
        'ED6_DT07/CH00111 ._CH',             # 06
        'ED6_DT07/CH00170 ._CH',             # 07
        'ED6_DT07/CH00172 ._CH',             # 08
        'ED6_DT07/CH01330 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
        'ED6_DT07/CH00112 ._CH',             # 0B
        'ED6_DT07/CH01240 ._CH',             # 0C
        'ED6_DT07/CH01630 ._CH',             # 0D
        'ED6_DT07/CH01260 ._CH',             # 0E
        'ED6_DT07/CH01620 ._CH',             # 0F
        'ED6_DT07/CH02090 ._CH',             # 10
        'ED6_DT07/CH01320 ._CH',             # 11
        'ED6_DT06/CH20116 ._CH',             # 12
        'ED6_DT06/CH20117 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01410P._CP',             # 00
        'ED6_DT09/CH10820P._CP',             # 01
        'ED6_DT09/CH10821P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00110P._CP',             # 05
        'ED6_DT07/CH00111P._CP',             # 06
        'ED6_DT07/CH00170P._CP',             # 07
        'ED6_DT07/CH00172P._CP',             # 08
        'ED6_DT07/CH01330P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
        'ED6_DT07/CH00112P._CP',             # 0B
        'ED6_DT07/CH01240P._CP',             # 0C
        'ED6_DT07/CH01630P._CP',             # 0D
        'ED6_DT07/CH01260P._CP',             # 0E
        'ED6_DT07/CH01620P._CP',             # 0F
        'ED6_DT07/CH02090P._CP',             # 10
        'ED6_DT07/CH01320P._CP',             # 11
        'ED6_DT06/CH20116P._CP',             # 12
        'ED6_DT06/CH20117P._CP',             # 13
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 32110,
        Y                   = -1000,
        Z                   = -45500,
        Range               = 35850,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF84AE,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -88800,
        Y                   = -1000,
        Z                   = -3040,
        Range               = -85900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFB7EE,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 70260,
        Y                   = -1000,
        Z                   = 32570,
        Range               = 56300,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7602,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -18470,
        TriggerZ            = 0,
        TriggerY            = -5070,
        TriggerRange        = 1500,
        ActorX              = -18470,
        ActorZ              = 1700,
        ActorY              = -5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4CE",          # 00, 0
        "Function_1_4F4",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_266C",         # 03, 3
        "Function_4_30F1",         # 04, 4
        "Function_5_3406",         # 05, 5
        "Function_6_3581",         # 06, 6
        "Function_7_36FD",         # 07, 7
    )


    def Function_0_4CE(): pass

    label("Function_0_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4E5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_4F3")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_4F3")

    Return()

    # Function_0_4CE end

    def Function_1_4F4(): pass

    label("Function_1_4F4")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFDDD20, 0x30064)
    Return()

    # Function_1_4F4 end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266B")
    EventBegin(0x0)
    SetChrPos(0x8, 14740, 0, -49400, 225)
    SetChrPos(0x9, 12040, 0, -49370, 90)
    SetChrPos(0xA, 12070, 0, -51990, 45)
    SetChrPos(0xB, 14800, 0, -52250, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    OP_A2(0x616)

    ChrTalk(
        0x8,
        "……呀啊啊～～！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#000F是女人的惨叫！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F在这里面，赶快！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(13190, 0, -50600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(282000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 20850, 0, -44670, 0)
    SetChrPos(0x102, 19400, 0, -43210, 0)

    ChrTalk(
        0x8,
        "呀啊啊啊啊啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "救命啊！\x01",
            "谁来帮忙啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 2)

    def lambda_6BD():
        OP_92(0xFE, 0x8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6BD)
    Sleep(50)
    SetChrChipByIndex(0xA, 2)

    def lambda_6DC():
        OP_92(0xFE, 0x8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6DC)
    Sleep(100)
    SetChrChipByIndex(0xB, 2)

    def lambda_6FB():
        OP_92(0xFE, 0x8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6FB)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)

    def lambda_71A():
        OP_8E(0xFE, 0x3B7E, 0x0, 0xFFFF3B8E, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71A)

    def lambda_735():
        OP_8E(0xFE, 0x35DE, 0x0, 0xFFFF414C, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_735)
    Sleep(600)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 11)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)

    def lambda_769():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_769)

    def lambda_779():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_779)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x9, 1)

    def lambda_793():
        OP_95(0xFE, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_793)
    SetChrChipByIndex(0xB, 1)

    def lambda_7B6():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7B6)
    TurnDirection(0x101, 0xB, 0)
    TurnDirection(0x102, 0x9, 0)

    def lambda_7E2():
        OP_8F(0xFE, 0x38AE, 0x0, 0xFFFF3B16, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E2)

    def lambda_7FD():
        OP_8F(0xFE, 0x35D4, 0x0, 0xFFFF3DF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FD)
    Sleep(150)
    SetChrChipByIndex(0xA, 1)

    def lambda_822():
        OP_95(0xFE, 0xFFFFFD44, 0x0, 0xFFFFFD44, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_822)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x8,
        "哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F修女！\x01",
            "已经没事了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F很危险，\x01",
            "所以请退到后面去！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A0():
        OP_92(0xFE, 0x8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8A0)

    def lambda_8B5():
        OP_92(0xFE, 0x8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8B5)

    def lambda_8CA():
        OP_92(0xFE, 0x8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8CA)
    Sleep(500)
    Battle(0x3A3, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_8F7"),
        (SWITCH_DEFAULT, "loc_8FA"),
    )


    label("loc_8F7")

    OP_B4(0x0)
    Return()

    label("loc_8FA")

    AddParty(0x7, 0xFF)
    SetChrPos(0x108, 22520, 0, -37100, 0)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, 14390, 0, -50980, 225)
    SetChrPos(0x102, 12920, 0, -49800, 225)
    SetChrPos(0x8, 14740, 0, -49400, 225)
    OP_6D(13730, 0, -50080, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(282000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    EventBegin(0x0)

    ChrTalk(
        0x101,
        (
            "#000F呼……\x01",
            "真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(
        0x101,
        "#000F修女，你没事吧？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)

    def lambda_9FE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FE)

    ChrTalk(
        0x8,
        "啊，是的……多亏了你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "嗯……你们到底是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是游击士协会的人。\x02\x03",
            "正在找人的途中，\x01",
            "听到了你的惨叫，所以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "是……这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F怎、怎么了？\x01",
            "看起来好像很没精神的样子……\x02\x03",
            "难道受伤了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "没有……\x01",
            "多亏了你们，才平安无事的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我是王都大圣堂的修女，\x01",
            "名叫艾伦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "真是太感谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈哈。\x01",
            "不用谢啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，\x01",
            "作为圣职者的女性\x01",
            "一个人来这种地方……\x02\x03",
            "你没有和其他人\x01",
            "一起来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是的，不好意思，\x01",
            "只有我一个人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "其实是因为大圣堂里\x01",
            "调药用的草药没有了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "商店里也卖完了，\x01",
            "所以才来这里采集的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这也太危险了。\x01",
            "明明到处都是魔兽啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不，以前这里\x01",
            "没有这么多魔兽的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "好像是从最近\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    Sleep(500)

    def lambda_E13():
        OP_8E(0xFE, 0x3CD2, 0x0, 0xFFFF3EB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E13)
    Sleep(100)

    def lambda_E33():
        OP_8E(0xFE, 0x37C8, 0x0, 0xFFFF4282, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_E33)
    OP_8C(0x8, 45, 400)

    ChrTalk(
        0x8,
        "啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_E77():
        OP_8F(0xFE, 0x3782, 0x0, 0xFFFF3C24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_E77)
    SetChrPos(0x9, 19840, 0, -40400, 0)
    SetChrPos(0xA, 21100, 0, -41220, 0)
    SetChrPos(0xB, 21440, 0, -39410, 0)
    SetChrPos(0xC, 21420, 0, -38390, 0)
    SetChrPos(0xD, 23130, 0, -39910, 0)
    SetChrPos(0xE, 21460, 0, -36780, 0)
    SetChrPos(0xF, 23510, 0, -37150, 0)
    SetChrPos(0x10, 24560, 0, -39000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    def lambda_F42():
        OP_8E(0xFE, 0x3BB0, 0x0, 0xFFFF4E44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F42)

    def lambda_F5D():
        OP_8E(0xFE, 0x43DA, 0x0, 0xFFFF4BA6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F5D)

    def lambda_F78():
        OP_8E(0xFE, 0x40E2, 0x0, 0xFFFF5060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F78)

    def lambda_F93():
        OP_8E(0xFE, 0x3FAC, 0x0, 0xFFFF56B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F93)

    def lambda_FAE():
        OP_8E(0xFE, 0x4A1A, 0x0, 0xFFFF5132, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FAE)

    def lambda_FC9():
        OP_8E(0xFE, 0x433A, 0x0, 0xFFFF5A74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FC9)

    def lambda_FE4():
        OP_8E(0xFE, 0x4AF6, 0x0, 0xFFFF5ACE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_FE4)

    def lambda_FFF():
        OP_8E(0xFE, 0x4A74, 0x0, 0xFFFF55F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_FFF)
    Sleep(300)

    def lambda_101F():
        OP_6D(19250, 0, -43570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_101F)

    def lambda_1037():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1037)
    Sleep(1500)

    def lambda_104C():
        OP_6D(17110, 0, -45970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_104C)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#000F怎么回事啊，这些家伙们……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好像是因为\x01",
            "听到骚动而聚集过来了……\x02\x03",
            "有这么多，还真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，以防万一，\x01",
            "至少先让修女逃出去……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x80)
    OP_8E(0x108, 0x528A, 0x0, 0xFFFF61B8, 0x2EE0, 0x0)

    def lambda_1155():
        OP_6D(17970, 0, -45090, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1155)
    SetChrChipByIndex(0x108, 8)
    SetChrFlags(0x108, 0x20)
    SetChrFlags(0x108, 0x1000)

    def lambda_117C():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_117C)
    OP_8E(0x108, 0x4CD6, 0x0, 0xFFFF5C36, 0x2EE0, 0x0)
    PlayEffect(0x8, 0xFF, 0xFF, 19660, 0, -41900, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_11D5():
        OP_8F(0xFE, 0x43DA, 0x0, 0xFFFF542A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_11D5)

    def lambda_11F0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_11F0)

    def lambda_1202():
        OP_99(0xFE, 0x4, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1202)
    OP_96(0x108, 0x4F9C, 0x0, 0xFFFF5EDE, 0x3E8, 0x1770)

    ChrTalk(
        0x108,
        "哦，看起来你们遇到麻烦了？\x02",
    )

    CloseMessageWindow()

    def lambda_123F():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_123F)

    def lambda_124D():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_124D)

    def lambda_125B():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_125B)

    def lambda_1269():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1269)

    def lambda_1277():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1277)

    ChrTalk(
        0x101,
        "#000F啊，金先生！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F太好了……\x01",
            "终于发现了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嘿嘿，\x01",
            "我还以为是谁，原来是你们啊。\x02\x03",
            "总之，要说的话一会儿再说，\x01",
            "赶快把这些家伙们收拾掉吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白！\x02",
    )

    CloseMessageWindow()

    def lambda_1380():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1380)

    def lambda_1390():
        OP_8E(0xFE, 0x416E, 0x0, 0xFFFF4868, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1390)

    def lambda_13AB():
        OP_8E(0xFE, 0x3A0C, 0x0, 0xFFFF494E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_13AB)
    OP_8E(0x108, 0x492A, 0x0, 0xFFFF5952, 0x1388, 0x0)
    Battle(0x3A4, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_13ED"),
        (SWITCH_DEFAULT, "loc_13F0"),
    )


    label("loc_13ED")

    OP_B4(0x0)
    Return()

    label("loc_13F0")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x101, 16770, 0, -47500, 45)
    SetChrPos(0x102, 15050, 0, -45990, 45)
    SetChrPos(0x108, 17690, 0, -44440, 225)
    SetChrPos(0x8, 14650, 0, -48360, 45)
    OP_6D(15920, 0, -45970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x108, 0x1000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    ClearChrFlags(0x108, 0x20)
    ClearChrFlags(0x108, 0x1000)

    ChrTalk(
        0x108,
        (
            "#070F哎呀哎呀……\x01",
            "多亏了这些家伙们，让我好好地出了一次汗。\x02\x03",
            "不过，真没想到\x01",
            "能在这里见到你们啊。\x02\x03",
            "你们不是在\x01",
            "蔡斯地区工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈哈，确实从那时候起\x01",
            "就一直没有像这样见面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F其实我们已经从蔡斯支部\x01",
            "转属到格兰赛尔支部来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，是这样啊。\x02\x03",
            "也就是说，那个绑架事件，\x01",
            "已经解决了吗。\x02\x03",
            "那个中毒的红发小哥\x01",
            "现在还好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，已经没事了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "……请问…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哦，真是失礼了……\x02\x03",
            "…………啊……………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16F3():

        label("loc_16F3")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_16F3")

    QueueWorkItem2(0x108, 1, lambda_16F3)
    OP_8F(0x108, 0x3D72, 0x0, 0xFFFF4DAE, 0x7D0, 0x0)

    ChrTalk(
        0x108,
        (
            "#070F喂喂……\x01",
            "真是个美人啊。\x02\x03",
            "是你们的同伴吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(
        0x102,
        (
            "#010F不是，\x01",
            "我们也是刚认识的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#000F真是的，这么色迷迷的，\x01",
            "也不知道害羞……\x02\x03",
            "我去告诉雾香小姐吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x108, 0xFF)
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070F呜……\x01",
            "我只是说陈述客观的事实罢了……\x02\x03",
            "喂，\x01",
            "为什么要提到那家伙的名字啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3B92, 0x0, 0xFFFF4674, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "那个……把我从危险的地方救出来，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "你们都是我的救命恩人。\x02",
    )

    CloseMessageWindow()

    def lambda_18F4():

        label("loc_18F4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_18F4")

    QueueWorkItem2(0x108, 1, lambda_18F4)

    def lambda_1905():

        label("loc_1905")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_1905")

    QueueWorkItem2(0x102, 1, lambda_1905)
    OP_8F(0x108, 0x3DC2, 0x0, 0xFFFF491C, 0x7D0, 0x0)

    ChrTalk(
        0x108,
        (
            "#070F没什么没什么，请别放在心上！\x02\x03",
            "作为男人，\x01",
            "就应该贯彻武侠之道嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F好像在装帅呢。\x02\x03",
            "金先生\x01",
            "其实对女人没有办法呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈……\x01",
            "说得没错。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 22440, 0, -38100, 0)
    SetChrPos(0x12, 21240, 0, -37930, 0)

    ChrTalk(
        0x11,
        "你们在干什么！？\x02",
    )

    CloseMessageWindow()

    def lambda_1A63():

        label("loc_1A63")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A63")

    QueueWorkItem2(0x108, 2, lambda_1A63)

    def lambda_1A74():

        label("loc_1A74")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A74")

    QueueWorkItem2(0x101, 2, lambda_1A74)

    def lambda_1A85():

        label("loc_1A85")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A85")

    QueueWorkItem2(0x102, 2, lambda_1A85)

    def lambda_1A96():

        label("loc_1A96")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A96")

    QueueWorkItem2(0x8, 2, lambda_1A96)

    def lambda_1AA7():
        OP_8E(0xFE, 0x48DA, 0x0, 0xFFFF540C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AA7)

    def lambda_1AC2():
        OP_8E(0xFE, 0x4434, 0x0, 0xFFFF55EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1AC2)
    OP_6D(17010, 0, -44670, 3000)

    ChrTalk(
        0x101,
        "#000F哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)

    ChrTalk(
        0x11,
        (
            "在这种没人的地方密谈，\x01",
            "真是可疑的家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "难道……\x01",
            "你们是恐怖分子吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x4182, 0x0, 0xFFFF4BF6, 0xFA0, 0x0)

    ChrTalk(
        0x101,
        (
            "#10A#000F谁、谁是恐怖分子啊！？\x01",
            "我们是——呜。\x05\x02",
        )
    )

    Sleep(1000)
    OP_8E(0x102, 0x3F2A, 0x0, 0xFFFF4BF6, 0xFA0, 0x0)

    def lambda_1C45():
        OP_8E(0xFE, 0x42FE, 0x0, 0xFFFF49D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C45)
    OP_8F(0x102, 0x4182, 0x0, 0xFFFF4BF6, 0x7D0, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F……我们是游击士协会\x01",
            "格兰赛尔支部所属的成员。\x02\x03",
            "就在刚才，我们保护了\x01",
            "这位修女免遭魔兽袭击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "是游击士！？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3A84, 0x0, 0xFFFF4B60, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "那个……\x01",
            "他们说的都是真的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我来这里采摘草药，\x01",
            "结果被魔兽袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F顺便一说，我也是游击士。\x02\x03",
            "我记得和你们的同伴\x01",
            "在预选赛中曾经碰过面对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "卡尔瓦德的武术家……\x01",
            "那个一个人参赛的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "哼……\x01",
            "身份好像可以确定了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "这次就放过你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "不过，这里离艾尔贝离宫很近。\x01",
            "没事不要在这边乱转。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "还有，修女小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我们把你\x01",
            "送回王都去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "不要借助\x01",
            "什么游击士的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哎，但、但是我……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#000F可恶，等一下，你们！\x02\x03",
            "从刚才开始，\x01",
            "就一直在说过分的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔……算了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x11, 400)

    ChrTalk(
        0x102,
        (
            "#010F以后我们会注意的，\x01",
            "这次能宽大处理，真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "哼，算了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "你们到底只不过是普通市民。\x01",
            "弄清楚自己的本分。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "那么，修女小姐，我们走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "好、好的……\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8E(0x8, 0x4268, 0x0, 0xFFFF515A, 0xBB8, 0x0)
    TurnDirection(0x8, 0x108, 400)

    ChrTalk(
        0x8,
        (
            "那个，各位……\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21FB():
        OP_8E(0xFE, 0x5CB2, 0x0, 0xFFFF70F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21FB)
    Sleep(100)

    def lambda_221B():
        OP_8E(0xFE, 0x5CB2, 0x0, 0xFFFF70F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_221B)
    Sleep(200)

    def lambda_223B():
        OP_8E(0xFE, 0x5CB2, 0x0, 0xFFFF70F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_223B)
    Sleep(2000)
    OP_62(0x101, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    OP_6D(17150, 0, -46640, 1000)
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x101,
        (
            "#000F什、什、什……\x02\x03",
            "什么啊！那些家伙们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F是王国军情报部所属的\x01",
            "『特务部队』的人吧。\x02\x03",
            "虽然很厉害，\x01",
            "不过是很阴险的家伙们呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_237F():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_237F)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(
        0x101,
        (
            "#000F比起阴险来说，\x01",
            "倒不如说是品行恶劣呢！\x02\x03",
            "哎……\x02\x03",
            "为什么金先生\x01",
            "你会知道他们的事情呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(
        0x108,
        (
            "#070F啊，武术大会的预选赛，\x01",
            "他们的队伍也出场了。\x02\x03",
            "那时就是这样介绍的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F（那些家伙也有出场……！？）\x02\x03",
            "（平时进行隐秘活动那些家伙们\x01",
            "这样堂堂正正地被人看到……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（大概是没有\x01",
            "再隐藏自己存在的必要了吧……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F总之，在弄清楚原因之前，\x01",
            "我们还是赶快回城去吧。\x02\x03",
            "……对了，\x01",
            "你们为什么会在这里的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊……都忘了重要的事情呢。\x02\x03",
            "其实，\x01",
            "我们是来找金先生你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F嗯？找我？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F其实有件事情\x01",
            "想拜托金先生。\x02\x03",
            "是有关武术大会的事情……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_266B")

    Return()

    # Function_2_507 end

    def Function_3_266C(): pass

    label("Function_3_266C")

    EventBegin(0x0)
    SetChrPos(0x101, 11690, 0, -52560, 225)
    SetChrPos(0x102, 11000, 0, -51680, 225)
    SetChrPos(0x108, 10930, 0, -50240, 196)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x13, 14410, 0, -53900, 257)
    SetChrPos(0x14, 14820, 0, -52280, 244)
    SetChrPos(0x15, 13050, 0, -51640, 207)
    SetChrPos(0x16, 13090, 0, -50260, 213)
    OP_6D(11570, 250, -53400, 0)
    OP_67(0, 7270, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(225000, 0)
    OP_6E(395, 0)
    FadeToBright(3000, 0)

    def lambda_2745():
        OP_6C(249000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2745)
    OP_6E(309, 5000)

    ChrTalk(
        0x101,
        (
            "#006F嗯……\x01",
            "这里就是集合点吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在琥耀石的石碑旁的休息场所，\x01",
            "和这里完全符合。\x02\x03",
            "#013F问题是，\x01",
            "尤莉亚中尉他们还没来啊……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x17, 17080, 0, -45130, 225)
    SetChrPos(0x18, 17100, 0, -43830, 225)
    SetChrPos(0x19, 18380, 0, -45010, 225)
    SetChrPos(0x1A, 17740, 0, -42700, 225)
    SetChrPos(0x1B, 18600, 0, -43670, 225)
    SetChrPos(0x1C, 19480, 0, -44620, 225)
    SetChrPos(0x1D, 18580, 0, -41840, 225)
    SetChrPos(0x1E, 19520, 0, -42690, 225)
    SetChrPos(0x1F, 20400, 0, -43690, 225)

    def lambda_2904():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2904)

    def lambda_291F():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_291F)

    def lambda_293A():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_293A)

    def lambda_2955():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2955)

    def lambda_2970():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2970)

    def lambda_298B():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_298B)

    def lambda_29A6():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_29A6)

    def lambda_29C1():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_29C1)

    def lambda_29DC():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_29DC)

    ChrTalk(
        0x17,
        "#1P……请不用担心。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2A4F():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A4F)

    def lambda_2A5D():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A5D)

    def lambda_2A6B():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A6B)

    def lambda_2A79():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2A79)

    def lambda_2A87():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2A87)

    def lambda_2A95():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2A95)

    def lambda_2AA3():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2AA3)

    def lambda_2AB1():
        OP_6C(335000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2AB1)

    def lambda_2AC1():
        OP_6E(332, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AC1)

    def lambda_2AD1():
        OP_6D(13880, 0, -49890, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AD1)

    def lambda_2AE9():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2AE9)
    Sleep(100)

    def lambda_2B09():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2B09)

    def lambda_2B24():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2B24)
    Sleep(100)

    def lambda_2B44():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2B44)

    def lambda_2B5F():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2B5F)

    def lambda_2B7A():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2B7A)
    Sleep(100)

    def lambda_2B9A():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2B9A)

    def lambda_2BB5():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_2BB5)

    def lambda_2BD0():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2BD0)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x17, 0x1)

    ChrTalk(
        0x101,
        "#004F哇，什么时候……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F哈哈……\x01",
            "原来有这么多人潜伏在王都啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#176F市民中也有很多人支持我们。\x01",
            "　\x02\x03",
            "#170F我们这边已经准备好了，\x01",
            "随时可以开始作战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "好……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 400)

    ChrTalk(
        0x16,
        (
            "#5P艾丝蒂尔，\x01",
            "请发号施令。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D2F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D2F)

    def lambda_2D3D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2D3D)

    def lambda_2D4B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2D4B)

    def lambda_2D59():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2D59)

    def lambda_2D67():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2D67)

    def lambda_2D75():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2D75)

    ChrTalk(
        0x101,
        (
            "#580F咦……？\x02\x03",
            "我、我来！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P因为是由你们\x01",
            "接受女王委托的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5P是啊，\x01",
            "由你来发号施令是理所当然的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F可、可是……\x01",
            "我还只是个新人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6P哈哈，没关系。\x01",
            "由你来我们没有异议的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#6P只要声音别叫得太大，\x01",
            "就不会惊动到敌人的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#171F我们是来协助你们作战的，\x01",
            "所以绝对不会有半点异议。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#503F啊，哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F#5P艾丝蒂尔，要有自信。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#071F#5P不用再细想了。\x02\x03",
            "这可是老规矩了，老规矩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嗯……\x02\x03",
            "#006F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    def lambda_2FDA():

        label("loc_2FDA")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FDA")

    QueueWorkItem2(0x102, 1, lambda_2FDA)

    def lambda_2FEB():

        label("loc_2FEB")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FEB")

    QueueWorkItem2(0x108, 1, lambda_2FEB)

    def lambda_2FFC():

        label("loc_2FFC")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FFC")

    QueueWorkItem2(0x13, 1, lambda_2FFC)

    def lambda_300D():

        label("loc_300D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_300D")

    QueueWorkItem2(0x14, 1, lambda_300D)

    def lambda_301E():

        label("loc_301E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_301E")

    QueueWorkItem2(0x15, 1, lambda_301E)

    def lambda_302F():

        label("loc_302F")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_302F")

    QueueWorkItem2(0x16, 1, lambda_302F)

    def lambda_3040():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3040)
    OP_8E(0x101, 0x2972, 0x1E0, 0xFFFF2F40, 0x5DC, 0x0)
    OP_20(0x7D0)
    OP_8C(0x101, 45, 400)
    WaitChrThread(0x101, 0x3)
    OP_21()

    ChrTalk(
        0x101,
        "#006F#5P我向全体作战成员宣布……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#005F#5P艾尔贝离宫攻略战，\x01",
            "暨人质解救作战现在开始！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4113   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_266C end

    def Function_4_30F1(): pass

    label("Function_4_30F1")

    EventBegin(0x0)
    OP_6D(-26280, 0, -4400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x18, 19)
    SetChrChipByIndex(0x19, 19)
    SetChrChipByIndex(0x1A, 19)
    SetChrChipByIndex(0x1B, 19)
    SetChrSubChip(0x18, 2)
    SetChrSubChip(0x19, 2)
    SetChrSubChip(0x1A, 2)
    SetChrSubChip(0x1B, 2)
    SetChrPos(0x18, -25890, 0, -4510, 180)
    SetChrPos(0x19, -27370, 0, -4510, 180)
    SetChrPos(0x1A, -27240, 0, -2700, 180)
    SetChrPos(0x1B, -25950, 0, -2920, 180)
    SetChrPos(0x108, -26570, 0, -6220, 0)
    SetChrPos(0x102, -28030, 0, -6250, 45)
    SetChrPos(0x101, -25360, 0, -6190, 315)
    Sleep(1000)

    ChrTalk(
        0x108,
        "#072F好，伏击组开始行动了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5P我们先行一步，\x01",
            "去引开前庭的残存兵力！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5P趁此机会，\x01",
            "请你们突入离宫内部！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，知道了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F愿女神保佑你们！\x02",
    )

    CloseMessageWindow()

    def lambda_32E7():

        label("loc_32E7")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_32E7")

    QueueWorkItem2(0x101, 1, lambda_32E7)

    def lambda_32F8():

        label("loc_32F8")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_32F8")

    QueueWorkItem2(0x102, 1, lambda_32F8)

    def lambda_3309():

        label("loc_3309")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_3309")

    QueueWorkItem2(0x108, 1, lambda_3309)
    SetChrChipByIndex(0x1B, 18)

    def lambda_331F():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_331F)

    def lambda_332D():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_332D)
    Sleep(200)
    SetChrChipByIndex(0x1A, 18)

    def lambda_3352():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3352)

    def lambda_3360():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3360)
    Sleep(200)
    SetChrChipByIndex(0x18, 18)

    def lambda_3385():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3385)

    def lambda_3393():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3393)
    Sleep(200)
    SetChrChipByIndex(0x19, 18)

    def lambda_33B8():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_33B8)

    def lambda_33C6():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_33C6)
    Sleep(2000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_A2(0x651)
    EventEnd(0x0)
    Return()

    # Function_4_30F1 end

    def Function_5_3406(): pass

    label("Function_5_3406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3580")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347E")

    ChrTalk(
        0x101,
        (
            "#002F……在突击的时刻是不能逃离的。\x01",
            "　\x02\x03",
            "立刻赶去艾尔贝离宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3565")

    label("loc_347E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F0")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F要突击也只有趁现在了……\x02\x03",
            "赶快去艾尔贝离宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3565")

    label("loc_34F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3565")
    TurnDirection(0x108, 0x1, 400)

    ChrTalk(
        0x108,
        (
            "#072F如果现在不行动的话，\x01",
            "就没有突入离宫的机会了。\x02\x03",
            "……赶快去艾尔贝离宫吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3565")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3580")

    Return()

    # Function_5_3406 end

    def Function_6_3581(): pass

    label("Function_6_3581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36FC")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F9")

    ChrTalk(
        0x101,
        (
            "#002F……在突击的时刻是不能逃离的。\x01",
            "　\x02\x03",
            "立刻赶去艾尔贝离宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_35F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366C")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F要突击也只有趁现在了……\x02\x03",
            "赶快去艾尔贝离宫吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E1")

    label("loc_366C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E1")
    TurnDirection(0x108, 0x1, 400)

    ChrTalk(
        0x108,
        (
            "#072F如果现在不行动的话，\x01",
            "就没有突入离宫的机会了。\x02\x03",
            "……赶快去艾尔贝离宫吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E1")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_36FC")

    Return()

    # Function_6_3581 end

    def Function_7_36FD(): pass

    label("Function_7_36FD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　艾尔贝离宫\x01",
            "东　格鲁纳门　　２２４塞尔矩\x01",
            "西　圣海姆门　　２５６塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_36FD end

    SaveToFile()

Try(main)
