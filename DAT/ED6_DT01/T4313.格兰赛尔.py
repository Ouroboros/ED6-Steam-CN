from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4313   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4313.x',
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
        '管家费特',                             # 9
        '特务兵',                               # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '科洛丝',                               # 15
        '奥利维尔',                             # 16
        '雪拉',                                 # 17
        '尤莉亚中尉',                           # 18
        '基库',                                 # 19
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
        'ED6_DT07/CH01570 ._CH',             # 06
        'ED6_DT07/CH01330 ._CH',             # 07
        'ED6_DT07/CH02340 ._CH',             # 08
        'ED6_DT07/CH00030 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH02090 ._CH',             # 0B
        'ED6_DT07/CH02320 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH00100P._CP',             # 00
        'ED6_DT07/CH00101P._CP',             # 01
        'ED6_DT07/CH00110P._CP',             # 02
        'ED6_DT07/CH00111P._CP',             # 03
        'ED6_DT07/CH00170P._CP',             # 04
        'ED6_DT07/CH00171P._CP',             # 05
        'ED6_DT07/CH01570P._CP',             # 06
        'ED6_DT07/CH01330P._CP',             # 07
        'ED6_DT07/CH02340P._CP',             # 08
        'ED6_DT07/CH00030P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH02090P._CP',             # 0B
        'ED6_DT07/CH02320P._CP',             # 0C
    )

    DeclNpc(
        X                   = -11780,
        Z                   = 0,
        Y                   = 20150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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


    DeclActor(
        TriggerX            = 25980,
        TriggerZ            = 0,
        TriggerY            = 50580,
        TriggerRange        = 800,
        ActorX              = 25690,
        ActorZ              = 1000,
        ActorY              = 51500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22140,
        TriggerZ            = 0,
        TriggerY            = 50600,
        TriggerRange        = 800,
        ActorX              = 21830,
        ActorZ              = 890,
        ActorY              = 51760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BA",          # 00, 0
        "Function_1_2EB",          # 01, 1
        "Function_2_2EC",          # 02, 2
        "Function_3_680",          # 03, 3
        "Function_4_1446",         # 04, 4
        "Function_5_159A",         # 05, 5
        "Function_6_163E",         # 06, 6
    )


    def Function_0_2BA(): pass

    label("Function_0_2BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2C8")
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_2C8")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2EA"),
    )


    label("loc_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E7")
    OP_A2(0x656)
    Event(0, 3)

    label("loc_2E7")

    Jump("loc_2EA")

    label("loc_2EA")

    Return()

    # Function_0_2BA end

    def Function_1_2EB(): pass

    label("Function_1_2EB")

    Return()

    # Function_1_2EB end

    def Function_2_2EC(): pass

    label("Function_2_2EC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54A")
    OP_A2(0x679)
    OP_28(0x4C, 0x1, 0x10)
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "说明了最深处的豪华大门\x01",
            "被锁上了的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "是啊，那里\x01",
            "是被锁上了的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个钥匙是由情报部的队长\x01",
            "保管着的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因为出现了恐怖分子，\x01",
            "中队长好像出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也就是说，是到尤莉亚中尉\x01",
            "他们埋伏的地方去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，这可就麻烦了。\x01",
            "没时间回去了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "等等……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "还有一个备用钥匙\x01",
            "是保管在某个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想应该是藏匿\x01",
            "在展示室里面的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F展示室！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F立刻去调查。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_67C")

    label("loc_54A")


    ChrTalk(
        0xFE,
        (
            "啊，他们集中在这个建筑\x01",
            "最深处的『纹章之间』里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "用来签署条约的，\x01",
            "具有光辉历史的大厅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F最深处的『纹章之间』吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还有一个备用钥匙\x01",
            "是保管在某个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我想应该是藏匿\x01",
            "在展示室里面的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67C")

    TalkEnd(0x8)
    Return()

    # Function_2_2EC end

    def Function_3_680(): pass

    label("Function_3_680")

    EventBegin(0x0)
    OP_6D(-14960, 0, 17380, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, -11780, 0, 20150, 225)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x102, 2)
    SetChrChipByIndex(0x108, 4)
    SetChrPos(0x101, -16850, 0, 13660, 45)
    SetChrPos(0x108, -18160, 0, 13760, 45)
    SetChrPos(0x102, -16690, 0, 12820, 45)
    SetChrPos(0x9, -10960, 0, 18200, 352)
    SetChrPos(0xA, -12000, 0, 18190, 61)
    SetChrPos(0xB, -15540, 0, 19130, 135)
    SetChrPos(0xC, -14400, 0, 18870, 285)
    SetChrPos(0xD, -18830, 0, 18070, 82)

    ChrTalk(
        0x8,
        "你、你们几个是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哇哇……\x01",
            "聚集了不少人啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B5():
        TurnDirection(0xFE, 0x101, 150)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7B5)
    TurnDirection(0xB, 0x101, 200)

    ChrTalk(
        0xB,
        (
            "嗯～……\x01",
            "什么，你们是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "唔～……\x01",
            "是不认识的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F晚上好。\x01",
            "我们是游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_84C)

    def lambda_85A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_85A)
    OP_96(0xD, 0xFFFFBA00, 0x0, 0x465A, 0x12C, 0xBB8)
    TurnDirection(0xD, 0x101, 200)

    ChrTalk(
        0xD,
        "啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F你们就在这儿\x01",
            "好好睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D4():
        OP_8E(0xFE, 0xFFFFC7AC, 0x0, 0x7210, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_8D4)

    def lambda_8EF():
        OP_8E(0xFE, 0xFFFFC3C4, 0x0, 0x481C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8EF)

    def lambda_90A():
        OP_8E(0xFE, 0x550, 0x0, 0x8642, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_90A)
    OP_6D(-14540, 0, 19000, 500)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)
    Battle(0x3AF, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_955"),
        (SWITCH_DEFAULT, "loc_958"),
    )


    label("loc_955")

    OP_B4(0x0)
    Return()

    label("loc_958")

    EventBegin(0x0)
    OP_6D(-14300, 0, 17270, 0)
    SetChrPos(0x9, -10570, 0, 16410, 121)
    SetChrPos(0xA, -11440, 0, 14650, 198)
    SetChrPos(0xB, -11940, 0, 15850, 225)
    SetChrPos(0xC, -18230, 0, 18530, 225)
    SetChrPos(0xD, -19110, 0, 14890, 135)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    SetChrPos(0x101, -14770, 0, 16800, 45)
    SetChrPos(0x108, -17220, 0, 15660, 350)
    SetChrPos(0x102, -15540, 0, 15160, 45)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -12550, -10, 19850, 225)

    ChrTalk(
        0x101,
        "#000F呼，解决掉一批。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F几下就打晕了，\x01",
            "真是没有挑战性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这里和城里面一样，\x01",
            "也是个有酒卖的谈话室呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "留、留我一条小命……\x02",
    )

    CloseMessageWindow()

    def lambda_AF1():
        OP_8F(0xFE, 0xFFFFD0EE, 0x0, 0x4F92, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AF1)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)

    def lambda_B1B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B1B)

    def lambda_B29():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B29)

    def lambda_B37():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B37)
    OP_6D(-12590, 0, 19790, 2000)

    def lambda_B56():

        label("loc_B56")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_B56")

    QueueWorkItem2(0x108, 1, lambda_B56)

    def lambda_B67():

        label("loc_B67")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_B67")

    QueueWorkItem2(0x101, 1, lambda_B67)

    def lambda_B78():

        label("loc_B78")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_B78")

    QueueWorkItem2(0x102, 1, lambda_B78)

    ChrTalk(
        0x8,
        (
            "我、我、我\x01",
            "不是他们的同伙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我们知道了，\x01",
            "你是离宫的工作人员对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们是接受女王陛下的委托\x01",
            "来解救被拘捕的人们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "咦……真、真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "真的是来\x01",
            "救我们的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，因此你可以放心了。\x02",
    )

    CloseMessageWindow()

    def lambda_C8F():
        OP_6D(-15830, 0, 17600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C8F)
    OP_8E(0x8, 0xFFFFCD7E, 0x0, 0x538E, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFC22A, 0x0, 0x51EA, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFC054, 0x0, 0x46BE, 0xBB8, 0x0)

    ChrTalk(
        0x8,
        "哈……太好了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "记者朋友被捕后，\x01",
            "我认为我已经活不成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "他应该没事吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F记者朋友……\x02\x03",
            "啊，奈尔的朋友\x01",
            "莫非就是你吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔说明了\x01",
            "奈尔失踪事件的经过。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "是啊，那时联络\x01",
            "奈尔的确实是我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "他想对保护在这里的公主\x01",
            "进行一次采访……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "看到他那么热心，我不忍心拒绝，\x01",
            "于是我就把他悄悄带了进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F结果事情暴露而被捕了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是啊，说来惭愧，\x01",
            "那时我还没有觉察到真相。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "只是听说公主被恐怖分子列为目标，\x01",
            "那伙人给囚禁了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "公主要来的事情让我们很高兴，\x01",
            "所以根本就没有注意到实情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F算了算了，\x01",
            "不要灰心丧气嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您知道被捕的人们\x01",
            "关在哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "啊，他们集中在这个建筑\x01",
            "最深处的『纹章之间』里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "用来签署条约的，\x01",
            "具有光辉历史的大厅。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AE")

    ChrTalk(
        0x101,
        "#000F最深处的『纹章之间』吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F好，赶快去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x4C, 0x1, 0x4)
    Jump("loc_1443")

    label("loc_11AE")

    OP_A2(0x679)
    OP_28(0x4C, 0x1, 0x10)

    ChrTalk(
        0x101,
        (
            "#000F最深处的大厅……\x01",
            "不就是在刚才那边吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊，是里面那扇\x01",
            "上了锁的豪华的大门吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "是啊，那里\x01",
            "是被锁上了的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那个钥匙是由情报部的队长\x01",
            "保管着的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "因为出现了恐怖分子，\x01",
            "中队长好像出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F也就是说，是到尤莉亚中尉\x01",
            "他们埋伏的地方去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，这可就麻烦了。\x01",
            "没时间回去了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "等等……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "还有一个备用钥匙\x01",
            "是保管在某个地方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我想应该是藏匿\x01",
            "在展示室里面的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F展示室！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F立刻去调查。\x02",
    )

    CloseMessageWindow()

    label("loc_1443")

    EventEnd(0x0)
    Return()

    # Function_3_680 end

    def Function_4_1446(): pass

    label("Function_4_1446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156D")
    EventBegin(0x0)
    OP_A2(0x657)
    OP_28(0x4C, 0x1, 0x20)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个豪华的深红色花瓶。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们调查了一下，\x01",
            "经过调查，\x01",
            "发现其底部粘有什么东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "备用钥匙\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x36F, 1)

    ChrTalk(
        0x101,
        "#000F啊，就是它！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这样就可以打开\x01",
            "里面那扇门了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_1599")

    label("loc_156D")


    ChrTalk(
        0x101,
        "#000F…干得好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "（假定）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1599")

    Return()

    # Function_4_1446 end

    def Function_5_159A(): pass

    label("Function_5_159A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1611")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有○○○○○○○。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们调查了一下，\x01",
            "没有找到什么特别的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_163A")

    label("loc_1611")


    ChrTalk(
        0x101,
        "#000F…干得好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "（假定）\x02",
    )

    CloseMessageWindow()

    label("loc_163A")

    TalkEnd(0xFF)
    Return()

    # Function_5_159A end

    def Function_6_163E(): pass

    label("Function_6_163E")

    EventBegin(0x0)
    OP_6D(11600, 0, -11080, 0)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0xE, 11330, 0, -10500, 135)
    SetChrPos(0x11, 12980, 0, -9840, 233)
    SetChrPos(0x12, 9810, 700, -10140, 315)
    SetChrPos(0x101, 10700, 0, -11900, 66)
    SetChrPos(0x102, 11920, 0, -12750, 353)
    SetChrPos(0x108, 11030, 0, -13350, 31)
    SetChrPos(0x10, 13240, 0, -12800, 311)
    SetChrPos(0xF, 14330, 0, -11910, 252)
    TurnDirection(0xE, 0x11, 0)
    TurnDirection(0x12, 0x11, 0)
    TurnDirection(0x101, 0x11, 0)
    TurnDirection(0x102, 0x11, 0)
    TurnDirection(0x108, 0x11, 0)
    TurnDirection(0x10, 0x11, 0)
    TurnDirection(0xF, 0x11, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x108, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x80)

    ChrTalk(
        0x11,
        (
            "#170F我真的……\x01",
            "真是不好意思。\x02\x03",
            "由于我的不中用，\x01",
            "而让大家这么的辛苦……\x02\x03",
            "如果没能完成任务，办事不周的我将会\x01",
            "用自己的双手将身体撕裂，以谢此罪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "请不要这么说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "能够这样和大家再次相会，\x01",
            "我已经觉得非常开心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "你们能够来救我……\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#170F殿下……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎呀，在这样的场所感动，\x01",
            "总感觉有些不太合适呢……\x02\x03",
            "为何基库也在这里呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18F2():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_18F2)

    def lambda_1900():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1900)

    def lambda_190E():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_190E)

    def lambda_191C():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_191C)

    def lambda_192A():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_192A)

    def lambda_1938():
        TurnDirection(0xFE, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1938)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(
        0x12,
        "啾？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(
        0x11,
        (
            "#170F呵呵，基库在作为\x01",
            "殿下的护卫的同时，\x01",
            "也是亲卫队的传令员哦。\x02\x03",
            "你们忘了在旅馆收到的\x01",
            "那封信了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19F7():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_19F7)

    def lambda_1A05():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A05)

    def lambda_1A13():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A13)

    def lambda_1A21():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1A21)

    def lambda_1A2F():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A2F)

    def lambda_1A3D():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1A3D)

    ChrTalk(
        0x101,
        "#000F啊……是那天晚上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F果然是这样。\x02\x03",
            "这么说来，让尤莉亚中尉\x01",
            "得知女王陛下委托的也是它了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#170F嗯，是女王陛下直接\x01",
            "通过基库告知我的。\x02\x03",
            "不过殿下所在的这个大房间\x01",
            "没有基库可以进入的窗户。\x02\x03",
            "不能及时取得联系真让我很担心啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(
        0xE,
        "呵呵，说得没错呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(
        0x101,
        (
            "#000F还真是的……\x01",
            "我完全没有想到呢。\x02\x03",
            "喂，基库。\x01",
            "悄悄的把信放下后就离开了，\x01",
            "是不是有些薄情了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啾～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#040F嘻嘻……\x01",
            "它说『对不起』。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(
        0x101,
        (
            "#000F哎呀，没关系的啦。\x02\x03",
            "对了，那些特务兵已经\x01",
            "全部解决了吗?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D3D():
        TurnDirection(0xFE, 0x11, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D3D)

    ChrTalk(
        0x11,
        (
            "#170F在离宫这里值勤的部队\x01",
            "基本上都被我们控制了。\x02\x03",
            "但是在格兰赛尔城内\x01",
            "应该还有相当一部分的残党。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DCB():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DCB)

    ChrTalk(
        0x10,
        (
            "#020F各地的王国军，至今还\x01",
            "处于情报部的掌控之下。\x02\x03",
            "最糟糕的是，他们有可能会以镇压\x01",
            "叛军的名义对这里展开进攻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊……\x01",
            "我还没有想到这一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x02\x03",
            "至少让科洛丝\x01",
            "先去别的地方避难吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#030F如果可能的话，去寻求\x01",
            "帝国或共和国大使馆的保护如何？\x02\x03",
            "在大使馆里有治外法权保护……\x01",
            "敌人是不会轻举妄动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F可以用刚才作战所缴获的\x01",
            "特务艇作为逃跑的办法。\x02\x03",
            "虽然不能从根本上解决问题，\x01",
            "但可以拖延一些时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#170F说得是啊……\x01",
            "也只有选择逃亡了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "大家……听我说。\x02",
    )

    CloseMessageWindow()

    def lambda_217D():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_217D)

    def lambda_218B():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_218B)

    def lambda_2199():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2199)

    def lambda_21A7():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21A7)

    def lambda_21B5():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_21B5)
    OP_8C(0xE, 135, 400)

    ChrTalk(
        0xE,
        (
            "在这种状况下，我还可以\x01",
            "委托任务给作为游击士的大家吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F人质救出任务已经\x01",
            "完成了。所以应该没有问题。\x02\x03",
            "当然，要视委托的内容而定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "如果可以……\x01",
            "请接受我无理的请求。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "能够帮助我\x01",
            "解放王城并救出陛下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#170F殿、殿下……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F对啊……还有女王陛下呢。\x02\x03",
            "我们一定要把她也救出来啊！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F说实话，我就知道\x01",
            "有可能会变成这样。\x02\x03",
            "不过，公主殿下……\x01",
            "这个委托相当棘手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#020F是啊……\x02\x03",
            "以我们现在的战斗力，就算全员齐聚，\x01",
            "也不可能从正面攻入王城的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果利用那艘特务艇的话，\x01",
            "也不是没有可能……\x02\x03",
            "然而，非常充足的\x01",
            "准备是行动的必要条件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "……这些我已经考虑过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "各位，你们看这个可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F这个是……哪儿的地图？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这是记载着王都地下水路\x01",
            "内部结构的古代文献。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "这上面标记出了通往\x01",
            "王城地下的隐藏水路。\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x357, 1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_163E end

    SaveToFile()

Try(main)
