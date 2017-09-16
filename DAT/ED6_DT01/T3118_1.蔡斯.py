from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3118_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3118.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_11F9",         # 03, 3
        "Function_4_13DA",         # 04, 4
        "Function_5_2069",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2930, 0, 6630, 0)
    SetChrPos(0x101, -2950, 0, 6740, 90)
    SetChrPos(0x102, -2810, 0, 5490, 45)
    SetChrPos(0x107, -3850, 0, 6140, 90)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465")

    ChrTalk(
        0xFE,
        "呼，真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我绝对不会\x01",
            "放过这个家伙。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A8")

    ChrTalk(
        0x101,
        "#000F米妮亚姆医生，您好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F您好～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "哎呀，你好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，还有两位客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F我们是看了公告板而来的。\x02\x03",
            "啊，说起来\x01",
            "还没有自我介绍过呢。\x02\x03",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F和她一样，我叫约修亚。\x02\x03",
            "好像发生了什么案件呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)
    Jump("loc_3D2")

    label("loc_2A8")

    OP_A2(0x589)
    OP_A2(0x58A)

    ChrTalk(
        0x107,
        "#060F米妮亚姆医生，您好～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "哎呀，你好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，还有两位客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，我们是看了公告板而来的。\x02\x03",
            "我是准游击士艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F和她一样，我叫约修亚。\x02\x03",
            "好像发生了什么案件呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    label("loc_3D2")


    ChrTalk(
        0xFE,
        "嗯……实际上是这样的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果可以的话，\x01",
            "我希望你们现在就展开调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "可以吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C9")

    label("loc_465")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "哎呀，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如何？\x01",
            "现在可以进行调查了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_647")
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#505F嗯～\x01",
            "现在还不行呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "这可就麻烦了，\x01",
            "情况很紧急呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "可是既然你们没空，\x01",
            "那也就没办法了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F对不起，\x01",
            "我们会尽快回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x2000)

    def lambda_63C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63C)
    EventEnd(0x0)
    Return()

    label("loc_647")

    Sleep(100)

    ChrTalk(
        0x101,
        "#006F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F请您立刻说明案件详情吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "说起来其实很简单。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)

    ChrTalk(
        0xFE,
        (
            "不知道是谁从这个橱柜里\x01",
            "把香烟拿走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#505F这里是医务室啊，\x01",
            "怎么会有香烟呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "在我的倡导下，\x01",
            "工房这几年都在开展禁烟运动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这个运动中所没收的香烟，\x01",
            "都被集中到这里来放置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这么说来，\x01",
            "有嫌疑的就是以前香烟被没收过的人了。\x02\x03",
            "拿走香烟的很可能就是那些人。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F啊，的确是这样呢～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "嗯，我也是这么估计的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "现在，禁烟运动\x01",
            "好不容易才算得到了推广……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果让这个不守规矩的家伙\x01",
            "再这么恣意妄为下去，\x01",
            "持续至今的努力就会化为泡影了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F总而言之，\x01",
            "嫌疑就集中在原来那些吸烟者身上吧……\x02\x03",
            "有没有怀疑的对象呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最为可疑的就是\x01",
            "演算室的特莱斯主任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "主任看上去就是那种\x01",
            "老烟鬼级别的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他刚开始戒烟不久，\x01",
            "具有非常充分的动机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F呼～不太记得他的样子。\x02\x03",
            "#004F……啊，我要先做一下笔记。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "然后就是\x01",
            "设计室的雨果先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他现在应该在\x01",
            "一楼的大厅和别人谈话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "他很早以前就来工房工作了，\x01",
            "也有吸烟的习惯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#064F哦～原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F演算室的特莱斯主任以及\x01",
            "在一楼和别人谈话的雨果先生对吧。\x02\x03",
            "还有什么别的情报吗？\x02\x03",
            "没有的话我们就展开调查了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，还有一件事，\x01",
            "不知道能不能对你们有帮助……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "当时有一个目击者哦。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#004F………………啊！？\x02\x03",
            "这、这不就是\x01",
            "决定性的线索吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F目击者是谁呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xB, 400)

    ChrTalk(
        0xFE,
        "就在你们后面啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "安东尼。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE3")

    def lambda_DDB():
        TurnDirection(0x1, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DDB)

    label("loc_DE3")

    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E02")

    def lambda_DFA():
        TurnDirection(0x2, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DFA)

    label("loc_E02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E1C")

    def lambda_E14():
        TurnDirection(0x3, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E14)

    label("loc_E1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E36")

    def lambda_E2E():
        TurnDirection(0x4, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_E2E)

    label("loc_E36")

    TurnDirection(0x0, 0xB, 400)
    Sleep(800)
    OP_4A(0xB, 255)
    OP_62(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xB, 0x101, 400)
    Sleep(400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xB,
        "喵～～呵。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#004F小、小猫～～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "明白了吧？\x01",
            "所以我才说不知道能不能帮上你们啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F……原来如此，我了解了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(
        0x107,
        (
            "#063F可、可是，\x01",
            "安东尼是一只很聪明的小猫呢。\x02\x03",
            "也许它真的知道犯人是谁呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是啊，如果带着它进行搜查，\x01",
            "所不定会找到什么线索呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "猫的嗅觉也是很灵敏的呢，\x01",
            "与狗相比也毫不逊色哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F啊，真期待它的表现呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果把它喜欢的\x01",
            "『新鲜牛奶』拿来的话， \x01",
            "它一定会很高兴地跟随在你们后面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果实在找不到线索，\x01",
            "那就一定要用它来试试看。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        "#000F嗯，我们会参考这一点的。\x02",
    )

    CloseMessageWindow()

    def lambda_112C():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_112C)
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        (
            "#010F如果我们有什么收获，\x01",
            "会立刻来通知您的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "期待你们的表现。\x01",
            "一定要抓住犯人哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x4, 0x8)
    OP_28(0x2C, 0x4, 0x4)
    OP_28(0x2C, 0x1, 0x1)
    OP_28(0x2C, 0x1, 0x2)
    OP_28(0x2C, 0x1, 0x4)
    ClearChrFlags(0xFE, 0x10)

    def lambda_11EA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11EA)
    EventEnd(0x0)
    OP_4B(0xB, 255)
    Return()

    # Function_2_AC end

    def Function_3_11F9(): pass

    label("Function_3_11F9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【喂它新鲜牛奶】\x01",      # 0
            "【放弃】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1265")
    Return()

    label("loc_1265")

    OP_3F(0x38A, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DB")

    ChrTalk(
        0x101,
        (
            "#507F乖，安东尼，\x01",
            "你最喜欢的牛奶哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵呀～～噢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C8")

    label("loc_12DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1351")

    ChrTalk(
        0x102,
        (
            "#019F安东尼。\x01",
            "给，牛奶。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵呀～～噢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C8")

    label("loc_1351")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C8")

    ChrTalk(
        0x107,
        (
            "#066F安东尼～乖孩子～\x01",
            "我给你带来了牛奶哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵呀～～噢。\x02",
    )

    CloseMessageWindow()

    label("loc_13C8")

    Fade(1000)
    SetChrFlags(0xB, 0x80)
    AddParty(0x3B, 0xFF)
    OP_0D()
    TalkEnd(0xFE)
    Return()

    # Function_3_11F9 end

    def Function_4_13DA(): pass

    label("Function_4_13DA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F2")
    RemoveParty(0x3B, 0xFF)
    ClearChrFlags(0xB, 0x80)

    label("loc_13F2")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_4A(0x8, 0)
    OP_6D(-6080, 0, 7020, 0)
    OP_6C(16000, 0)
    SetChrPos(0x8, -6740, 0, 7040, 135)
    SetChrPos(0xD, -5840, 0, 6240, 315)
    SetChrPos(0xB, -7340, 0, 6050, 130)
    SetChrPos(0x101, -4730, 0, 6330, 225)
    SetChrPos(0x102, -5570, 0, 5260, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_148E")
    SetChrPos(0x107, -4620, 0, 5220, 324)

    label("loc_148E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14AD")
    SetChrPos(0x106, -3390, 0, 6350, 267)

    label("loc_14AD")

    OP_0D()
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "……真是的，\x01",
            "我真是想不吃惊都不行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我怎么也想不到，\x01",
            "竟然是工房长您的所为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#805F#2P实、实在对不起……\x02\x03",
            "我其实只是想抽一支而已。\x01",
            "　\x02\x03",
            "没想到就鬼使神差地……\x01",
            "我不知道怎么形容才好。\x02\x03",
            "#803F米妮亚姆医生……\x01",
            "我真的很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "可是，工房长。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我的确记得很早以前\x01",
            "您就已经戒烟了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#802F#2P啊、啊啊，是啊。\x02\x03",
            "已经差不多戒了十年了吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊？那么久了。\x02\x03",
            "可怎么会突然之间\x01",
            "又想要抽烟了呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 45, 400)

    ChrTalk(
        0xD,
        (
            "#806F#2P唔唔，\x01",
            "连我自己也不是很清楚……\x02\x03",
            "导力停止现象之后，\x01",
            "市民的抱怨变得很厉害。\x02\x03",
            "我一直在想怎么解决，\x01",
            "那时不知为何\x01",
            "竟然又想抽起烟来了。\x02\x03",
            "呼啊～…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(120)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x107,
        (
            "#065F工、工房长叔叔……\x02\x03",
            "#561F对、对不起啊。\x01",
            "都是爷爷的缘故……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xD, 135, 400)

    ChrTalk(
        0xD,
        (
            "#805F#2P不、不是的，提妲。\x01",
            "你用不着道歉。\x02\x03",
            "这次的事情和博士无关，\x01",
            "是我的错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F工房长您还是好好休息一下吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F想吸烟的原因\x01",
            "很可能是由于压力过高。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "工房长…………\x01",
            "事情我已经明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这次的事情\x01",
            "就既往不咎。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0xD, 315, 400)

    ChrTalk(
        0xD,
        (
            "#802F#2P啊？\x01",
            "真、真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过我希望……\x01",
            "您能好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这样子下去\x01",
            "身体会吃不消的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#806F#2P啊，是啊……\x02\x03",
            "#806F等事情告一段落之后，\x01",
            "我保证会好好休息的。\x02\x03",
            "#803F米妮亚姆医生……\x01",
            "今天实在是太过意不去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "好了，过去的就算了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "保重身体才是最重要的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#800F#2P啊，我会好好注意的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 135, 400)

    ChrTalk(
        0xD,
        "#800F#2P那么我就告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_1C25():

        label("loc_1C25")

        TurnDirection(0x8, 0xD, 0)
        OP_48()
        Jump("loc_1C25")

    QueueWorkItem2(0x8, 1, lambda_1C25)

    def lambda_1C36():

        label("loc_1C36")

        TurnDirection(0x101, 0xD, 0)
        OP_48()
        Jump("loc_1C36")

    QueueWorkItem2(0x101, 1, lambda_1C36)

    def lambda_1C47():

        label("loc_1C47")

        TurnDirection(0x102, 0xD, 0)
        OP_48()
        Jump("loc_1C47")

    QueueWorkItem2(0x102, 1, lambda_1C47)

    def lambda_1C58():

        label("loc_1C58")

        TurnDirection(0x107, 0xD, 0)
        OP_48()
        Jump("loc_1C58")

    QueueWorkItem2(0x107, 1, lambda_1C58)
    SetChrFlags(0xD, 0x40)
    OP_8E(0xD, 0xFFFFE6B0, 0x0, 0x13A6, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFE804, 0x0, 0x7BC, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFF42A, 0x0, 0x2EE, 0xBB8, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x107, 0x1)
    OP_8E(0xD, 0xFFFFFECA, 0x0, 0x3B6, 0xBB8, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    Sleep(800)
    OP_22(0x6D, 0x0, 0x64)

    def lambda_1CE7():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CE7)

    def lambda_1CF5():
        OP_8C(0x102, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CF5)

    def lambda_1D03():
        OP_8C(0x107, 315, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1D03)
    OP_8C(0x8, 135, 400)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#007F呼～真是好可怜啊。\x02\x03",
            "并不是因为工房长自身的缘故而犯的错误……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F可是，作为工房的领导者，\x01",
            "认真负责也是工作的内容之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，的确是这样的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……嗯。\x01",
            "我对你们大家真是感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这次事件\x01",
            "你们解决得很漂亮。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F不用谢啦。\x02\x03",
            "#000F还要多亏了安东尼的帮忙呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#061F呵呵呵，是～啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呵呵，\x01",
            "看来我的推荐起了不少作用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以后再碰见它\x01",
            "可要好好照顾它哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，好啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那么，\x01",
            "今天真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "如果以后有什么事的话，\x01",
            "还要拜托你们多多帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F彼此彼此。\x02\x03",
            "那么我们就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F再见了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【禁烟强化周】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0x8, 0)
    OP_28(0x2C, 0x4, 0x10)
    OP_28(0x2C, 0x1, 0x1000)
    OP_A2(0x3)
    EventEnd(0x0)
    Return()

    # Function_4_13DA end

    def Function_5_2069(): pass

    label("Function_5_2069")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "猫语日常会话入门\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x340, 1)
    SetChrFlags(0xE, 0x80)
    OP_64(0x0, 0x1)
    OP_28(0x2D, 0x1, 0x10)
    TalkEnd(0xFF)
    Return()

    # Function_5_2069 end

    SaveToFile()

Try(main)
