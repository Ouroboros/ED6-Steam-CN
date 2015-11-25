from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4205   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4205.x',
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
        '艾莉茜雅女王',                         # 9
        '尤莉亚中尉',                           # 10
        '约修亚',                               # 11
        '奥利维尔',                             # 12
        '金',                                   # 13
        '洛伦斯少尉',                           # 14
        '洛伦斯残像',                           # 15
        '洛伦斯残像',                           # 16
        '洛伦斯残像',                           # 17
        '洛伦斯残像',                           # 18
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02090 ._CH',             # 01
        'ED6_DT07/CH00010 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT07/CH00260 ._CH',             # 05
        'ED6_DT07/CH00262 ._CH',             # 06
        'ED6_DT07/CH00100 ._CH',             # 07
        'ED6_DT07/CH00101 ._CH',             # 08
        'ED6_DT07/CH00120 ._CH',             # 09
        'ED6_DT07/CH00121 ._CH',             # 0A
        'ED6_DT07/CH00140 ._CH',             # 0B
        'ED6_DT07/CH00141 ._CH',             # 0C
        'ED6_DT07/CH02200 ._CH',             # 0D
        'ED6_DT07/CH00264 ._CH',             # 0E
        'ED6_DT07/CH00104 ._CH',             # 0F
        'ED6_DT07/CH00124 ._CH',             # 10
        'ED6_DT07/CH00144 ._CH',             # 11
        'ED6_DT07/CH02460 ._CH',             # 12
        'ED6_DT07/CH02230 ._CH',             # 13
        'ED6_DT07/CH02240 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02090P._CP',             # 01
        'ED6_DT07/CH00010P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT07/CH00260P._CP',             # 05
        'ED6_DT07/CH00262P._CP',             # 06
        'ED6_DT07/CH00100P._CP',             # 07
        'ED6_DT07/CH00101P._CP',             # 08
        'ED6_DT07/CH00120P._CP',             # 09
        'ED6_DT07/CH00121P._CP',             # 0A
        'ED6_DT07/CH00140P._CP',             # 0B
        'ED6_DT07/CH00141P._CP',             # 0C
        'ED6_DT07/CH02200P._CP',             # 0D
        'ED6_DT07/CH00264P._CP',             # 0E
        'ED6_DT07/CH00104P._CP',             # 0F
        'ED6_DT07/CH00124P._CP',             # 10
        'ED6_DT07/CH00144P._CP',             # 11
        'ED6_DT07/CH02460P._CP',             # 12
        'ED6_DT07/CH02230P._CP',             # 13
        'ED6_DT07/CH02240P._CP',             # 14
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
        TalkScenaIndex      = 3,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_301",          # 01, 1
        "Function_2_32E",          # 02, 2
        "Function_3_344",          # 03, 3
        "Function_4_576",          # 04, 4
        "Function_5_3151",         # 05, 5
        "Function_6_31F3",         # 06, 6
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_29E"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B1")
    OP_A2(0x666)
    Event(0, 4)

    label("loc_2B1")

    Jump("loc_2B4")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DE")
    SetChrChipByIndex(0x0, 18)
    SetChrChipByIndex(0x1, 19)
    SetChrChipByIndex(0x138, 20)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_300")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2170, 12000, 62700, 0)

    label("loc_300")

    Return()

    # Function_0_292 end

    def Function_1_301(): pass

    label("Function_1_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_31D")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)
    Jump("loc_32D")

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_32D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32D")

    Return()

    # Function_1_301 end

    def Function_2_32E(): pass

    label("Function_2_32E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_343")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_32E")

    label("loc_343")

    Return()

    # Function_2_32E end

    def Function_3_344(): pass

    label("Function_3_344")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 0)), scpexpr(EXPR_END)), "loc_3CC")
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(
        0x8,
        (
            "#090F艾丝蒂尔、约修亚，\x01",
            "我好久没有像今天这样开心了。\x02\x03",
            "可以的话，以后一定要再来\x01",
            "和我一起喝喝茶、谈谈心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_572")

    label("loc_3CC")

    OP_A2(0x6F8)
    TurnDirection(0x8, 0x138, 0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#097F咦……\x02\x03",
            "#090F约修亚刚才竟然也能来到这里，\x01",
            "我原本觉得很不可思议……\x02\x03",
            "不过现在看来，我算是明白了。\x02\x03",
            "#091F呵呵，特务兵们\x01",
            "会被骗过去也是很正常的呢。\x02\x03",
            "#090F……艾丝蒂尔、约修亚，\x01",
            "我好久没有像今天这样开心了。\x02\x03",
            "可以的话，以后一定要再来\x01",
            "和我一起喝喝茶、谈谈心哦。\x02\x03",
            "下次也把科洛蒂娅和卡西乌斯上校\x01",
            "他们一起叫来聊聊天吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_572")

    TalkEnd(0xFE)
    Return()

    # Function_3_344 end

    def Function_4_576(): pass

    label("Function_4_576")

    EventBegin(0x0)
    OP_28(0x4E, 0x1, 0x8)
    OP_6D(2240, 12000, 50930, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(135000, 0)
    OP_6E(255, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 2170, 12000, 62700, 0)
    SetChrPos(0xD, 4080, 12000, 64099, 180)
    SetChrPos(0x101, 1870, 12000, 45230, 0)
    SetChrPos(0x105, 1870, 12000, 45230, 0)
    SetChrPos(0x103, 1870, 12000, 45230, 0)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x103, 9)
    SetChrChipByIndex(0x105, 11)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_650():
        OP_6D(1570, 12000, 55660, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_650)

    def lambda_668():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_668)

    def lambda_67A():
        OP_8E(0xFE, 0x730, 0x2EE0, 0xD566, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_67A)
    Sleep(500)

    def lambda_69A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_69A)

    def lambda_6AC():
        OP_8E(0xFE, 0xBCC, 0x2EE0, 0xD0AC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AC)
    Sleep(500)

    def lambda_6CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6CC)

    def lambda_6DE():
        OP_8E(0xFE, 0x26C, 0x2EE0, 0xD19C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DE)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x105,
        "#040F祖母大人，您没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F我们来救您了，女王陛下！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(
        0x8,
        (
            "#090F科洛蒂娅……\x01",
            "还有艾丝蒂尔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "总算来了……\x01",
            "我已经等的有些不耐烦了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CC():
        OP_8E(0xD, 0xAD2, 0x2EE0, 0xF3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_7CC)

    def lambda_7E7():

        label("loc_7E7")

        TurnDirection(0xD, 0x105, 0)
        OP_48()
        Jump("loc_7E7")

    QueueWorkItem2(0xD, 1, lambda_7E7)

    def lambda_7F8():
        OP_6D(2180, 13000, 59350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F8)

    def lambda_810():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_810)

    def lambda_820():
        OP_6E(321, 3000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_820)

    def lambda_830():
        OP_67(0, 6360, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_830)
    Sleep(800)

    def lambda_84D():
        OP_8F(0xFE, 0x88E, 0x2EE0, 0xF744, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_84D)
    Sleep(200)

    def lambda_86D():
        OP_8E(0xFE, 0x83E, 0x2EE0, 0xDDC2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_86D)
    Sleep(110)

    def lambda_88D():
        OP_8E(0xFE, 0xD20, 0x2EE0, 0xDFB6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88D)
    Sleep(100)

    def lambda_8AD():
        OP_8E(0xFE, 0x280, 0x2EE0, 0xE074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8AD)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#000F洛、洛伦斯少尉！\x01",
            "你怎么会在这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "#280F呵呵……\x01",
            "我的任务是保护女王陛下。\x02\x03",
            "出现在这里也没什么不可思议的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F别开玩笑了！\x02\x03",
            "不管你的实力有多强，\x01",
            "我们这边可是有三个人的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F怎么会，这家伙……\x01",
            "好强的压迫感。\x02\x03",
            "到底是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F他是情报部、特务部队队长，\x01",
            "洛伦斯·博格少尉！\x02\x03",
            "过去是猎兵出身，\x01",
            "后来被上校招入麾下！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#280F哦，竟然调查到这样的程度了。\x02\x03",
            "不愧是Ｓ级游击士\x01",
            "卡西乌斯·布莱特的女儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F居然连从未向外界公布过的\x01",
            "老师的级别也知道……\x02\x03",
            "这家伙，不是个等闲之辈啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#280F呵呵……\x01",
            "你的事情我也很清楚。\x02\x03",
            "级别Ｃ、『银闪』\x01",
            "雪拉扎德·哈维。\x02\x03",
            "近日似乎就要升成级别Ｂ了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F对、对不起……\x01",
            "请把祖母交还给我好吗。\x02\x03",
            "如果你只是被\x01",
            "上校所雇佣的话，\x01",
            "现在已经没有必要再战斗了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#280F呵呵，驱动着这个世界的，\x01",
            "并非只有眼睛能够看得到的东西。\x02\x03",
            "就像只看结晶回路盘是无法\x01",
            "知晓齿轮的运动一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#280F注意听好了，科洛蒂娅公主。\x02\x03",
            "所谓国家，与巨大而复杂\x01",
            "的导力器是相似的。\x02\x03",
            "将人的力量像结晶回路一样充分调动起来的，\x01",
            "就是所谓组织、制度这样的齿轮……\x02\x03",
            "而将其包裹着的就是国土这样的框架。\x02\x03",
            "对于这些知识，如果不能掌握，\x01",
            "那你就没有作为女王的资格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F非常有趣的比喻啊。\x02\x03",
            "而且……\x01",
            "的确有可能如你所说的那般。\x02\x03",
            "真没有想到在这样的地方\x01",
            "竟然能听到国家论……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0xD,
        (
            "#280F呵呵……刚才失礼了。\x01",
            "这些说法对于陛下您来说是没有必要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F虽然不太明白是怎么回事儿……\x02\x03",
            "不过看起来，你好像\x01",
            "没有释放女王陛下的打算了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(
        0xD,
        "#280F就算如此……你们想要怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那还用说……\x01",
            "拼尽全力也要救回女王陛下！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F是啊……\x01",
            "既然已经到了这里，就没有理由后退了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F……虽然从你身上\x01",
            "感觉不到什么敌意……\x02\x03",
            "但是为了将祖母大人救回来，\x01",
            "我会向你挥起手中的剑的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#280F哼哼，不错啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)
    OP_8E(0xD, 0x9E2, 0x2EE0, 0xF4E2, 0x7D0, 0x0)

    def lambda_121E():
        OP_90(0xFE, 0x0, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_121E)

    def lambda_1239():
        OP_91(0xFE, 0x0, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1239)

    def lambda_1254():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1254)

    def lambda_126C():
        OP_6E(295, 3000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_126C)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0xD, 0x20)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 6)
    TurnDirection(0xD, 0x105, 400)

    def lambda_129D():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_129D)
    OP_96(0xD, 0x8AC, 0x2EE0, 0xEEFC, 0x190, 0x1B58)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0xD,
        "#280F来……我当你们的对手。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Battle(0x39A, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrPos(0x101, 3360, 12000, 57270, 0)
    SetChrPos(0x105, 2110, 12000, 56770, 0)
    SetChrPos(0x103, 640, 12000, 57460, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1348"),
        (1, "loc_1785"),
        (SWITCH_DEFAULT, "loc_18D2"),
    )


    label("loc_1348")

    OP_28(0x4E, 0x1, 0x10)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 14)
    SetChrPos(0xD, 2220, 12000, 61180, 180)
    OP_2B(0x4D, 0x3)

    ChrTalk(
        0xD,
        (
            "#280F……真令人吃惊啊……\x01",
            "没想到你们可以达到这种程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呼呼……\x02\x03",
            "你、你这家伙！\x01",
            "当初决赛的时候没有尽全力吧！？\x02\x03",
            "和那时相比强悍得判若两人！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F竟、竟然可以\x01",
            "打败这样的怪物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F的、的确难以置信啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#280F艾丝蒂尔·布莱特……\x01",
            "刚才对你太过轻视，在下深表歉意。\x02\x03",
            "你如果能继续这么走下去……\x01",
            "达到你父亲那种境界也未尝不可。　　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#280F不过……现在还有一定差距。\x02",
    )

    CloseMessageWindow()

    def lambda_1554():
        OP_6D(2400, 12000, 57540, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1554)
    OP_99(0xD, 0x3, 0x0, 0x7D0)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 6)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x32, 0x0)
    SetChrPos(0xE, 2220, 12000, 61180, 180)
    SetChrPos(0xF, 2220, 12000, 61180, 180)
    SetChrPos(0x10, 2220, 12000, 61180, 180)
    SetChrPos(0x11, 2220, 12000, 61180, 180)
    OP_43(0xD, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0xE, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0xF, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0x10, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0x11, 0x1, 0x0, 0x5)
    OP_A6(0x0)

    def lambda_162F():
        OP_6C(24000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_162F)
    OP_A6(0x0)

    def lambda_1642():
        OP_67(0, 6730, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1642)
    OP_A6(0x2)
    PlayEffect(0x8, 0xFF, 0xFF, 2360, 14000, 57260, 0, 0, 0, 2400, 2400, 2400, 0xFF, 0, 0, 0, 0)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 17)
    TurnDirection(0x105, 0xD, 0)

    def lambda_16A9():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_16A9)

    def lambda_16BF():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16BF)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 16)
    TurnDirection(0x103, 0xD, 0)

    def lambda_16E6():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_16E6)

    def lambda_16FC():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16FC)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 15)
    TurnDirection(0x101, 0xD, 0)

    def lambda_1723():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1723)

    def lambda_1739():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1739)
    Sleep(500)

    ChrTalk(
        0x101,
        "#000F啊啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F呜……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F呀啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_1785")

    OP_28(0x4E, 0x1, 0x20)
    SetChrChipByIndex(0x105, 17)
    SetChrChipByIndex(0x103, 16)
    SetChrChipByIndex(0x101, 15)

    ChrTalk(
        0xD,
        (
            "#280F……真让人失望。\x02\x03",
            "原本还以为\x01",
            "可以让我有些起劲呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F为、为什么……\x02\x03",
            "和当初的决赛时完全不同……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F……可能那时他\x01",
            "还没有尽全力吧……\x02\x03",
            "这样强大的力量……\x01",
            "或许已经可以和老师匹敌了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F祖母大人……\x01",
            "……对不起……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_18D2")


    ChrTalk(
        0x8,
        (
            "#090F科洛蒂娅！\x01",
            "艾丝蒂尔！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18F4():
        OP_8E(0xFE, 0x6F4, 0x2EE0, 0xF1EA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18F4)
    Sleep(200)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    TurnDirection(0xD, 0x8, 400)

    def lambda_192F():
        OP_6D(2260, 12000, 60490, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_192F)

    def lambda_1947():

        label("loc_1947")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1947")

    QueueWorkItem2(0xD, 1, lambda_1947)
    OP_96(0xD, 0xB0E, 0x2EE0, 0xF1FE, 0x3E8, 0xFA0)
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0xD,
        (
            "#280F陛下，她们只是\x01",
            "暂时不能动了而已。\x02\x03",
            "并没有生命危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#090F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#280F哼哼，不错啊……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x20)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 13)
    OP_44(0xD, 0xFF)
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(
        0xD,
        (
            "#280F那么……\x01",
            "就让我好好活动一下吧。\x02\x03",
            "恕我失礼……\x01",
            "让我摘下这东西。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xD, 400)
    TurnDirection(0x105, 0xD, 0)
    OP_99(0x105, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0x105, 11)
    TurnDirection(0x101, 0xD, 0)
    OP_99(0x101, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0x101, 7)
    TurnDirection(0x103, 0xD, 0)
    OP_99(0x103, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0x103, 9)

    ChrTalk(
        0x101,
        "#000F银、银发……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F不……\x01",
            "是苍金色的……\x02\x03",
            "这家伙……\x01",
            "看起来似乎是出生在北方的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#280F呵呵……\x01",
            "的确是北方没错。\x02\x03",
            "不过离这里\x01",
            "也不算很遥远。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F那双眼眸……\x01",
            "为何会有那么深邃的颜色呢。\x02\x03",
            "明明还这么年轻……\x01",
            "可是却好像经历了巨大的苦难啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0xD,
        (
            "#280F……………………………\x02\x03",
            "女王啊，您是没有\x01",
            "怜悯我的资格的。\x02\x03",
            "对于知道『哈梅尔』\x01",
            "这个名字的您来说……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#090F哎……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(
        0xD,
        (
            "#280F好了，差不多是时候了。\x02\x03",
            "如你们所愿，\x01",
            "我将女王予以归还。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#280F如果想要阻止上校，\x01",
            "就赶快前去地下吧。\x02\x03",
            "虽然可能已经来不及了……\x02\x03",
            "不过还可以抑制住\x01",
            "不必要的伤亡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F地下……\x02\x03",
            "难道是说从那个地方\x01",
            "降到地下的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(
        0xD,
        (
            "#280F哼哼……现在的您对其中的含义，\x01",
            "应该清楚的不能再清楚了吧。\x02\x03",
            "为他们指引前进的道路吧。\x02\x03",
            "……那么，再会了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EC1():

        label("loc_1EC1")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1EC1")

    QueueWorkItem2(0x8, 1, lambda_1EC1)

    def lambda_1ED2():
        OP_6D(1670, 12000, 63950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1ED2)

    def lambda_1EEA():
        OP_6E(347, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EEA)

    def lambda_1EFA():
        OP_67(0, 6160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_1EFA)
    OP_8E(0xD, 0xBFE, 0x2EE0, 0xFC26, 0x1B58, 0x0)
    OP_8E(0xD, 0x906, 0x2EE0, 0x1054A, 0x1B58, 0x0)
    OP_96(0xD, 0x5E6, 0x3138, 0x108C4, 0x320, 0x1B58)
    OP_96(0xD, 0x51E, 0xFFFFD120, 0x12066, 0x3E8, 0x1B58)
    WaitChrThread(0xD, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)

    ChrTalk(
        0x101,
        "#000F怎么！？\x02",
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)

    def lambda_1FFD():
        OP_8E(0xFE, 0xEEC, 0x2EE0, 0x1064E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FFD)

    ChrTalk(
        0x103,
        "#020F来、来真的！？\x02",
    )

    CloseMessageWindow()

    def lambda_2031():
        OP_6D(2270, 12000, 66180, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2031)

    def lambda_2049():
        OP_6C(129000, 2000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2049)
    Sleep(200)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)

    def lambda_206E():
        OP_8E(0xFE, 0x2EE, 0x2EE0, 0x106DA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_206E)
    Sleep(500)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)

    def lambda_209E():
        OP_8E(0xFE, 0x6EA, 0x2EE0, 0xED4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_209E)
    WaitChrThread(0x105, 0x1)

    def lambda_20BE():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20BE)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F不、不见了……\x02\x03",
            "落到湖里去了……？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)

    ChrTalk(
        0x103,
        (
            "#020F这么说来……\x01",
            "可是湖面并没有波痕……\x02\x03",
            "那个男的，究竟……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F祖母大人……\x01",
            "您没有受伤吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F没有呢，科洛蒂娅。\x01",
            "他并没有伤害我。\x02\x03",
            "话说回来……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0xB, 1870, 12000, 45230, 0)
    SetChrPos(0xA, 1870, 12000, 45230, 0)
    SetChrPos(0xC, 1870, 12000, 45230, 0)
    SetChrPos(0x9, 1870, 12000, 45230, 0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    ChrTalk(
        0xA,
        "艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    def lambda_2271():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2271)

    def lambda_227F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_227F)

    def lambda_228D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_228D)

    def lambda_229B():
        OP_6D(2540, 12000, 61390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_229B)

    def lambda_22B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_22B3)

    def lambda_22C5():
        OP_8E(0xFE, 0xD2A, 0x2EE0, 0xE394, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_22C5)
    Sleep(500)

    def lambda_22E5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_22E5)

    def lambda_22F7():
        OP_8E(0xFE, 0x7D0, 0x2EE0, 0xE876, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22F7)
    Sleep(500)

    def lambda_2317():

        label("loc_2317")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2317")

    QueueWorkItem2(0xB, 1, lambda_2317)

    def lambda_2328():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2328)

    def lambda_233A():
        OP_8E(0xFE, 0x816, 0x2EE0, 0xE204, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_233A)
    Sleep(500)

    def lambda_235A():

        label("loc_235A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_235A")

    QueueWorkItem2(0xC, 1, lambda_235A)

    def lambda_236B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_236B)

    def lambda_237D():
        OP_8E(0xFE, 0x2C6, 0x2EE0, 0xE448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_237D)

    def lambda_2398():
        OP_8E(0xFE, 0xDF2, 0x2EE0, 0xE826, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2398)
    Sleep(500)

    def lambda_23B8():
        OP_8E(0xFE, 0x96, 0x2EE0, 0xEBB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23B8)

    def lambda_23D3():
        OP_6D(2140, 12000, 59300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23D3)

    def lambda_23EB():
        OP_6E(307, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_23EB)
    SetChrFlags(0x105, 0x40)
    OP_8E(0x105, 0xB22, 0x2EE0, 0xF000, 0x7D0, 0x0)
    TurnDirection(0x105, 0x9, 400)
    WaitChrThread(0x103, 0x1)

    def lambda_2420():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2420)
    WaitChrThread(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F约修亚！？\x02\x03",
            "太好了，你平安无事！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#010F艾丝蒂尔你那边才是……\x02\x03",
            "因为理查德上校和洛伦斯少尉\x01",
            "都没有在城内，我很是有些担心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那个戴红色头盔的，\x01",
            "倒是刚才还在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#010F咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F他撞破窗户\x01",
            "一跃而下，逃走了。\x02\x03",
            "真是一个超越常理的怪物啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#010F哦，原来是这样啊……\x02\x03",
            "真是太好了……\x01",
            "你能够平安无事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F约、约修亚……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0x730, 0x2EE0, 0xEBD2, 0x7D0, 0x0)

    ChrTalk(
        0x9,
        "#170F陛下……幸好您没事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F尤莉亚中尉……\x01",
            "能再见到你我真的很愉快呢。\x02\x03",
            "而且，大家……\x01",
            "我对你们的感激也是一言难尽啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2672():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2672)

    def lambda_2680():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2680)

    def lambda_268E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_268E)

    def lambda_269C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_269C)

    def lambda_26AA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26AA)

    def lambda_26B8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_26B8)

    ChrTalk(
        0xB,
        (
            "#030F呵呵，女王陛下。\x01",
            "您过奖了，我感到非常荣幸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#070F能够为您服务，我已深感荣幸了。\x02\x03",
            "不过现在还\x01",
            "没有到结束的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#170F虽然已镇压住了城内的特务兵，\x01",
            "但又传来了不利的消息。\x02\x03",
            "各地的正规军部队\x01",
            "正朝着王都方向攻来……\x02\x03",
            "很可能是被\x01",
            "情报部给操控了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#090F是这样的啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#170F虽然很抱歉，不过已经没时间了。\x02\x03",
            "务必请您乘坐\x01",
            "飞行艇从这儿离开吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F不行……我办不到。\x02\x03",
            "话说回来……\x01",
            "可怕的事情就要发生了。\x02\x03",
            "无论如何也要\x01",
            "阻止理查德上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#170F怎、怎么回事呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F昨夜，我和上校谈话之后，　　\x01",
            "总算明白了其真正的目的。\x02\x03",
            "他企图将『辉之环』\x01",
            "据为己有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F『辉之环』……\x02\x03",
            "好、好像在哪里\x01",
            "好像在哪儿听到过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#010F……女神赐予古代人的\x01",
            "『七至宝』之一……\x02\x03",
            "可以支配世间一切的\x01",
            "传说中的古代遗迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哦，是亚鲁瓦教授说过的……\x02\x03",
            "可是那只是教会\x01",
            "流传下来的故事啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#090F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#030F嗯，应该存在吧？\x02\x03",
            "在这个利贝尔王国的某处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F古老的王家传承如下。\x02\x03",
            "『辉之环，总有一天会带来灾难，\x01",
            "将人类之子的灵魂与炼狱相接。』\x02\x03",
            "『我等，为了作为人而存在，\x01",
            "在昏暗的狭间将其封印……』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#070F『将人类之子的灵魂与炼狱相接』……\x02\x03",
            "实在是……令人感到可怕的说法啊。　　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F这些箴言，作为戒律\x01",
            "从一代代的国王那里相传至今。\x02\x03",
            "也许那个被称作『辉之环』的\x01",
            "东西具备这样的危险性，因此\x01",
            "王家的祖先才将其封印起来了。\x02\x03",
            "而且，在王都的地下\x01",
            "还检测出了巨大的导力反应……\x02\x03",
            "如果把这两者结合起来考虑的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#010F王都的地下\x01",
            "封印着『辉之环』……\x02\x03",
            "这么想是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F是啊……\x01",
            "上校肯定也是这么推断的。\x02\x03",
            "『辉之环』究竟是什么样的东西，\x01",
            "这一点并没有被传承下来……\x02\x03",
            "一旦其被人唤醒，\x01",
            "说不定会发生十分可怕的事情。\x02\x03",
            "甚至有可能和过去所发生的，\x01",
            "传说中的『大崩坏』匹敌……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F怎么、怎么会这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F没有想到，竟然会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F女王陛下！\x02\x03",
            "洛伦斯少尉曾说过\x01",
            "『到地下去吧』这样的话……\x02\x03",
            "那是代表什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#090F在这个格兰赛尔城里\x01",
            "有一间奇怪的屋子……\x02\x03",
            "是一个什么东西也不保管，\x01",
            "而且从很久以前就禁止入内的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#170F是宝物库吧！？\x02",
    )

    CloseMessageWindow()
    OP_28(0x4E, 0x1, 0x40)
    OP_28(0x4E, 0x1, 0x80)
    OP_28(0x4E, 0x1, 0x100)
    OP_28(0x4E, 0x1, 0x200)
    OP_28(0x4E, 0x1, 0x400)
    OP_28(0x4F, 0x4, 0x2)
    OP_28(0x4F, 0x4, 0x4)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4240   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_576 end

    def Function_5_3151(): pass

    label("Function_5_3151")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    OP_96(0xFE, 0x83E, 0x2EE0, 0xEB28, 0x190, 0x1770)
    SetChrChipByIndex(0xFE, 6)

    def lambda_3187():
        OP_99(0xFE, 0x0, 0x1, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3187)
    OP_96(0xFE, 0x79E, 0x3A98, 0xE6AA, 0xBB8, 0x1F40)
    OP_A2(0x0)
    Sleep(300)
    OP_A2(0x1)

    def lambda_31B9():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31B9)
    OP_96(0xFE, 0x744, 0x2EE0, 0xE204, 0x0, 0x3A98)
    OP_A2(0x2)
    Sleep(1000)

    def lambda_31E8():
        OP_99(0xFE, 0x3, 0xB, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31E8)
    Return()

    # Function_5_3151 end

    def Function_6_31F3(): pass

    label("Function_6_31F3")

    OP_1F(0x50, 0xC8)
    Return()

    # Function_6_31F3 end

    SaveToFile()

Try(main)
