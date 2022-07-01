from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3117_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3117.x',
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
        "Function_3_1167",         # 03, 3
        "Function_4_12FC",         # 04, 4
        "Function_5_2408",         # 05, 5
        "Function_6_2D20",         # 06, 6
        "Function_7_3BE6",         # 07, 7
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
    OP_6D(-2740, 0, 8680, 0)
    SetChrPos(0x101, -2790, 0, 7830, 0)
    SetChrPos(0x102, -1340, 0, 8370, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_105")
    SetChrPos(0x107, -2190, 0, 6710, 315)

    label("loc_105")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0x106, -1500, 0, 6000, 315)

    label("loc_124")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_143")
    SetChrPos(0x110, -2210, 0, 4820, 315)

    label("loc_143")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_162")
    SetChrPos(0x13C, -1500, 0, 6000, 315)

    label("loc_162")

    SetChrFlags(0x9, 0x10)
    TalkBegin(0x9)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2CB")
    ClearChrFlags(0x9, 0x10)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x9, 0x101, 400)
    OP_4A(0x9, 255)

    ChrTalk(
        0x9,
        "嗯？什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是来找雷伊前辈的吗？\x01",
            "他出去吃午饭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F唔，不是的。\x02\x03",
            "我们是看了公告板而来的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x9,
        "啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呀～太感谢了，\x01",
            "很高兴你们能来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我叫蒂亚利，\x01",
            "是中央工房的研究员。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_472")

    label("loc_2CB")

    ClearChrFlags(0x9, 0x10)

    ChrTalk(
        0x9,
        (
            "呼～总之试制品已经做好了。\x01",
            "之后就是等测试人员过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "在那之前，\x01",
            "我还是再调整一下鞋的内垫吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F你好～现在有空吗？\x02\x03",
            "我们是看了公告板而来的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x9, 255)
    Sleep(800)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "哦，终于来了。\x01",
            "哎呀～真是等急我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我叫蒂亚利，\x01",
            "是中央工房的研究员。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_472")


    ChrTalk(
        0x101,
        "#006F我是准游击士艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我是约修亚，\x01",
            "请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "啊，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么我这就把\x01",
            "任务委托给你们……\x01",
            "想问一下你们有空吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F")

    label("loc_538")

    ClearChrFlags(0x9, 0x10)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x9, 0x101, 400)
    OP_4A(0x9, 255)

    ChrTalk(
        0x9,
        "哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "怎么样？\x01",
            "有空了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59F")

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

    MenuEnd(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D6")

    ChrTalk(
        0x101,
        (
            "#007F呼～对不起呢。\x02\x03",
            "现在还不太方便……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔，\x01",
            "游击士真是忙碌啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那等你们\x01",
            "有空时再过来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，请稍微等一会。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F待会儿请您多多关照。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x1, 0x400)

    def lambda_6C2():
        OP_8C(0x9, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C2)
    OP_4B(0x9, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    label("loc_6D6")


    ChrTalk(
        0x101,
        "#000F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F您的委托是测试新型的运动鞋……\x01",
            "没错吧。\x01",
            "　\x02\x03",
            "如果可以的话，\x01",
            "请详细说明一下好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "嗯，当然。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "不过，\x01",
            "在此之前先把这个交给你们。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 400)
    Sleep(300)
    SetChrFlags(0xB, 0x80)
    TurnDirection(0x9, 0x101, 400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斯托雷加α\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x101,
        "#000F这个就是新型的运动鞋吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊，是我们和斯托雷加社\x01",
            "共同研制的新产品……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("蒂亚利")

    ChrTalk(
        0x9,
        (
            "这次的测试内容\x01",
            "就是穿着这双鞋\x01",
            "在蔡斯的周边地区走一圈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这次测试完成之后，\x01",
            "新型运动鞋就可以投放生产了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F呼～原来是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F…………咦！？\x01",
            "等、等一下！\x02\x03",
            "这、这运动鞋\x01",
            "是斯托雷加社制造的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x9,
        "咦…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "啊、啊啊，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊，\x01",
            "难道说这个新型的运动鞋就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "嗯，斯托雷加社的新产品哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这双鞋仅供测试使用，\x01",
            "刚才不已经说了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F………………啊！！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_62(0x101, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#001F啊，女神呀……\x02\x03",
            "感谢您能够赐予我\x01",
            "如此美妙的任务。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_8C(0x102, 225, 400)
    Sleep(800)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "喂，我说……\x01",
            "她没事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "怎么突然之间\x01",
            "就开始祷告起来了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        (
            "#018F…………让您见笑了。\x02\x03",
            "#017F艾丝蒂尔有收集运动鞋的爱好……\x01",
            "　\x02\x03",
            "而且她更是斯托雷加的忠实支持者。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C99")

    ChrTalk(
        0x107,
        "#064F哦……是这样的啊。\x02",
    )

    CloseMessageWindow()

    label("loc_C99")

    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "哦哦，这就是所谓的\x01",
            "运动鞋狂热收藏者啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然我是第一次见到，\x01",
            "不过这样的反应还真是强烈呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)

    ChrTalk(
        0x102,
        (
            "#018F……艾丝蒂尔，拜托，\x01",
            "别在别人面前失礼了。\x02\x03",
            "我知道你很开心，\x01",
            "但也要等接受完任务再开心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(
        0x101,
        (
            "#008F哦、哦哦…………\x01",
            "说得对呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔，不全神贯注的话，\x01",
            "最后很容易徒劳无功的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "请把这个测试坚持到底吧。\x01",
            "只要保持平常状态就行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F哦啊！明白！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(
        0x102,
        "#018F……不至于吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "好、好的。\x01",
            "总之就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那么，\x01",
            "再确认一下任务的内容吧……\x02\x03",
            "#010F穿上刚才拿到的那双鞋子\x01",
            "到各地走走就行了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        "嗯，就是如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "亚尔摩温泉、沃尔费堡垒，\x01",
            "还有圣海姆门……\x01",
            "这三个地方都要走一趟才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "如果觉得\x01",
            "测试已经足够了，\x01",
            "你们就回到我这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我要把鞋子外到鞋子里……\x01",
            "也就是说，\x01",
            "把鞋底和鞋内的情况进行检查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F那么，满足条件之后，\x01",
            "回来报告就行了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "对，不管怎样，\x01",
            "这件事就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "抱着踏破鞋底的决心\x01",
            "去好好测试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11C, 1)
    OP_28(0x2A, 0x4, 0x8)
    OP_28(0x2A, 0x4, 0x4)
    OP_28(0x2A, 0x1, 0x1)
    OP_28(0x2A, 0x1, 0x2)
    OP_28(0x2A, 0x1, 0x4)
    OP_A2(0x2)

    def lambda_1153():
        OP_8C(0x9, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1153)
    OP_4B(0x9, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_2_AC end

    def Function_3_1167(): pass

    label("Function_3_1167")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2740, 0, 8680, 0)
    SetChrPos(0x101, -2790, 0, 7830, 0)
    SetChrPos(0x102, -1340, 0, 8370, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C0")
    SetChrPos(0x107, -2190, 0, 6710, 315)

    label("loc_11C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DF")
    SetChrPos(0x106, -1500, 0, 6000, 315)

    label("loc_11DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FE")
    SetChrPos(0x110, -2210, 0, 4820, 315)

    label("loc_11FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121D")
    SetChrPos(0x13C, -1500, 0, 6000, 315)

    label("loc_121D")

    SetChrFlags(0x9, 0x10)
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x101, 0)
    OP_4A(0x9, 255)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_1259")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1259")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_1272")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1272")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_128B")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_128B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_12A4")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_12BD")
    RunExpression(0x0, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_12CB")
    Call(1, 4)
    Jump("loc_12E2")

    label("loc_12CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DE")
    Call(1, 5)
    Jump("loc_12E2")

    label("loc_12DE")

    Call(1, 6)

    label("loc_12E2")


    def lambda_12E8():
        OP_8C(0x9, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12E8)
    OP_4B(0x9, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_3_1167 end

    def Function_4_12FC(): pass

    label("Function_4_12FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x11C)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C0")
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "哎？\x01",
            "那双鞋子不见了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "呼，\x01",
            "这么一来就不能继续测试了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔～很遗憾，\x01",
            "不过确实是失败了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#007F呜……对不起啊。\x02\x03",
            "尽管专门来接受了任务，\x01",
            "可还是没能帮上一点忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "没、没关系，\x01",
            "最低限度的数据还是有的，\x01",
            "你不用担心了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "再过不久成品就能上市了，\x01",
            "敬请期待哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x4, 0x40)
    OP_A2(0x4)
    Return()

    label("loc_14C0")


    ChrTalk(
        0x101,
        (
            "#000F你好，蒂亚利研究员。\x02\x03",
            "那几个地方都已经走过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哦，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好，\x01",
            "那就让我检查一下这双鞋吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(
        0x9,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D2F")
    OP_2B(0x2A, 0x2)
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "……哦哦，真厉害。\x01",
            "鞋底磨损了很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "从磨损的情况来看，\x01",
            "我选择的材料\x01",
            "是相当合适的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "嗯，测试非常成功。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呼～太好了～\x02\x03",
            "我刚才还在想，\x01",
            "如果您叫我们继续该怎么办。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_16EF")

    ChrTalk(
        0x107,
        "#061F呵呵呵，太好了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1714")

    label("loc_16EF")


    ChrTalk(
        0x107,
        "#061F呵呵呵，太好了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1714")


    ChrTalk(
        0x9,
        "感觉怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "会不会很容易滑倒，\x01",
            "或者说有些太硬了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F有些吧，不过问题不大。\x02\x03",
            "穿上去很合适，\x01",
            "走起来也很舒服。\x02\x03",
            "不愧是斯托雷加啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊，对了。\x01",
            "你是斯托雷加的\x01",
            "忠实支持者对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……那么，\x01",
            "我就把这个作为礼物送给你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为你们做得比我预想的要好得多，\x01",
            "就当成是额外奖励吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斯托雷加β\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#004F这、这是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是厂家专门送过来的，\x01",
            "给研究者参考用的新产品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这可是还没有向外界披露的新型号呢。\x01",
            "商店里面自然也还没出售了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F这样好吗？\x01",
            "这个东西太贵重了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "唔，反正开发已经告一段落了，\x01",
            "我也就不需要了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "把这双鞋送给懂得其价值的人，\x01",
            "也算是体现出它的价值吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#001F哇啊，谢谢～！\x02\x03",
            "既可以协助开发，\x01",
            "又还可以得到新产品……\x02\x03",
            "真的是～一件美妙的任务啊～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "哈哈，彼此彼此吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为你们的努力才使得\x01",
            "我的研究成果得到充分的证明呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F您也要加油哦，\x01",
            "我很期待新产品呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔，我一定会把你这番话\x01",
            "转达给斯托雷加社的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么，多谢您的关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F再见了。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11D, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【测试新产品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_1D2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2173")
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "…………嗯。\x01",
            "鞋底已经磨损得足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "从磨损的情况来看，\x01",
            "我选择的材料\x01",
            "是相当合适的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "好，测试成功。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呼～太好了～\x02\x03",
            "我刚才还在想，\x01",
            "如果您叫我们继续该怎么办。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1EAB")

    ChrTalk(
        0x107,
        "#061F呵呵呵，太好了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ED0")

    label("loc_1EAB")


    ChrTalk(
        0x107,
        "#061F呵呵呵，太好了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1ED0")


    ChrTalk(
        0x9,
        "感觉怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "会不会很容易滑倒，\x01",
            "或者说有些太硬了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F有些吧，不过问题不大。\x02\x03",
            "穿上去很合适，\x01",
            "走起来也很舒服。\x02\x03",
            "不愧是斯托雷加啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这还只是样品，\x01",
            "相信成品会更加出色的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是辛苦你们了。\x01",
            "你们做得很好，帮了我大忙啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F您也要加油哦，\x01",
            "我很期待新产品呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哈哈哈，我一定会把你这番话\x01",
            "转达给斯托雷加社的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么，多谢您的关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F再见了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【测试新产品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_2173")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2407")
    OP_63(0x9)
    Sleep(400)

    ChrTalk(
        0x9,
        "…………唔～～唔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "很抱歉，\x01",
            "还走得不太够。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "鞋底还没怎么磨损，\x01",
            "这样是无法得到测试结果的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F嗯～这样啊。\x02\x03",
            "我还以为已经走得够多了呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔～\x01",
            "可是已经没有时间了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "很遗憾，\x01",
            "任务已经失败了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#007F呜……对不起啊。\x02\x03",
            "尽管专门来接受了任务，\x01",
            "可还是没能帮上一点忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "最低限度的数据还是有的，\x01",
            "我想没什么问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "再过不久成品就能上市了，\x01",
            "敬请期待哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x4, 0x40)
    OP_28(0x2A, 0x1, 0x20)
    OP_A2(0x4)
    Return()

    label("loc_2407")

    Return()

    # Function_4_12FC end

    def Function_5_2408(): pass

    label("Function_5_2408")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x11C)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2490")
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "哎？\x01",
            "那双鞋子不见了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "没有『斯托雷加α』的话\x01",
            "就不能继续测试了。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    label("loc_2490")


    ChrTalk(
        0x101,
        (
            "#000F蒂亚利研究员，\x01",
            "我们来汇报情况了。\x02\x03",
            "因为我们还有急事，\x01",
            "所以请赶快检查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哦，是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么，\x01",
            "这就检查一下这双鞋吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(
        0x9,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_29A9")
    OP_2B(0x2A, 0x2)
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "……哦哦，真厉害。\x01",
            "鞋底磨损了很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "从磨损的情况来看，\x01",
            "我选择的材料\x01",
            "是相当合适的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "嗯，测试非常成功。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呼，太好了～\x02\x03",
            "那么任务就此完成了吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是啊，辛苦大家了。\x01",
            "你们帮了我大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊，等一下。\x01",
            "你是斯托雷加的爱好者对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……那么，\x01",
            "这个送给你作为礼物吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斯托雷加β\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#000F这、这是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是厂家专门送过来的，\x01",
            "给研究者参考用的新产品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "开发已经告一段落了，\x01",
            "这东西对我来说也不需要了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#001F哇啊，谢谢～！\x02\x03",
            "我期待着新产品的上市哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我一定会把你这番话\x01",
            "转达给斯托雷加社的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那么，你们请多保重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F真是麻烦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F再见了。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11D, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【测试新产品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_29A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2A")
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "…………嗯。\x01",
            "鞋底已经磨损得足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "从磨损的情况来看，\x01",
            "我选择的材料\x01",
            "是相当合适的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "好，测试成功。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呼，太好了～\x02\x03",
            "那么任务就此完成了吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是啊，辛苦大家了。\x01",
            "你们帮了我大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F我期待着新产品的上市哦。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我一定会把你这番话\x01",
            "转达给斯托雷加社的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "那么，你们请多保重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F真是麻烦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F再见了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【测试新产品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_2C2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2D1F")
    OP_63(0x9)
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "很抱歉，\x01",
            "还走得不太够。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "鞋底还没怎么磨损，\x01",
            "这样是无法得到测试结果的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～这样啊。\x02\x03",
            "#000F那么，我们再继续吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "啊，麻烦你们了，\x01",
            "这件事就继续拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x1, 0x8)
    Return()

    label("loc_2D1F")

    Return()

    # Function_5_2408 end

    def Function_6_2D20(): pass

    label("Function_6_2D20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x11C)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA8")
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "哎？\x01",
            "那双鞋子不见了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "没有『斯托雷加α』的话\x01",
            "就不能继续测试了。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    label("loc_2DA8")


    ChrTalk(
        0x101,
        (
            "#000F你好，蒂亚利研究员。\x02\x03",
            "那几个地方都已经走过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "哦，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好，那就让我\x01",
            "检查一下这双鞋吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(
        0x9,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3618")
    OP_2B(0x2A, 0x2)
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "……哦哦，真厉害。\x01",
            "鞋底磨损了很多啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "从磨损的情况来看，\x01",
            "我选择的材料\x01",
            "是相当合适的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "嗯，测试非常成功。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呼～太好了～\x02\x03",
            "我刚才还在想，\x01",
            "如果您叫我们继续该怎么办。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2FD7")

    ChrTalk(
        0x107,
        "#061F呵呵呵，太好了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FFC")

    label("loc_2FD7")


    ChrTalk(
        0x107,
        "#061F呵呵呵，太好了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_2FFC")


    ChrTalk(
        0x9,
        "感觉怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "会不会很容易滑倒，\x01",
            "或者说有些太硬了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F有些吧，不过问题不大。\x02\x03",
            "穿上去很合适，\x01",
            "走起来也很舒服。\x02\x03",
            "不愧是斯托雷加啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊，对了。\x01",
            "你是斯托雷加的\x01",
            "忠实支持者对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……那么，\x01",
            "我就把这个作为礼物送给你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为你们做得比我预想的要好得多，\x01",
            "就当成是额外奖励吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "斯托雷加β\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        "#004F这、这是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是厂家专门送过来的，\x01",
            "给研究者参考用的新产品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这可是还没有向外界披露的新型号呢。\x01",
            "商店里面自然也还没出售了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F这样好吗？\x01",
            "这个东西太贵重了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(
        0x9,
        (
            "唔，反正开发已经告一段落了，\x01",
            "我也就不需要了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "把这双鞋送给懂得其价值的人，\x01",
            "也算是体现出它的价值吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#001F哇啊，谢谢～！\x02\x03",
            "既可以协助开发，\x01",
            "又还可以得到新产品……\x02\x03",
            "真的是～一件美妙的任务啊～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "哈哈，彼此彼此吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "因为你们的努力才使得\x01",
            "我的研究成果得到充分的证明呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F您也要加油哦，\x01",
            "我很期待新产品呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔，我一定会把你这番话\x01",
            "转达给斯托雷加社的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么，多谢您的关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F再见了。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x11D, 1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【测试新产品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_3618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5D")
    OP_63(0x9)
    Sleep(400)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            "…………嗯。\x01",
            "鞋底已经磨损得足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "从磨损的情况来看，\x01",
            "我选择的材料\x01",
            "是相当合适的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        "好，测试成功。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F呼～太好了～\x02\x03",
            "我刚才还在想，\x01",
            "如果您叫我们继续该怎么办。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3794")

    ChrTalk(
        0x107,
        "#061F呵呵呵，太好了呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37B9")

    label("loc_3794")


    ChrTalk(
        0x107,
        "#061F呵呵呵，太好了呢。\x02",
    )

    CloseMessageWindow()

    label("loc_37B9")


    ChrTalk(
        0x9,
        "感觉怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "会不会很容易滑倒，\x01",
            "或者说有些太硬了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F有些吧，不过问题不大。\x02\x03",
            "穿上去很合适，\x01",
            "走起来也很舒服。\x02\x03",
            "不愧是斯托雷加啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这还只是样品，\x01",
            "相信成品会更加出色的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是辛苦你们了。\x01",
            "你们做得很好，帮了我大忙啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F您也要加油哦，\x01",
            "我很期待新产品呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "哈哈哈，我一定会把你这番话\x01",
            "转达给斯托雷加社的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么，多谢您的关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F再见了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【测试新产品】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x1, 0x10)
    OP_A2(0x3)
    Return()

    label("loc_3A5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3BE5")
    OP_63(0x9)
    Sleep(400)

    ChrTalk(
        0x9,
        "…………唔～～唔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "很抱歉，\x01",
            "还走得不太够。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "鞋底还没怎么磨损，\x01",
            "这样是无法得到测试结果的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～这样啊。\x02\x03",
            "我还以为已经走得够多了呢……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F没办法，\x01",
            "我们再继续吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊，麻烦你们了，\x01",
            "不过还是请尽量多走些吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F嗯，我知道了。\x02\x03",
            "那我们待会儿再来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "这件事就继续拜托你们了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x2A, 0x1, 0x8)
    Return()

    label("loc_3BE5")

    Return()

    # Function_6_2D20 end

    def Function_7_3BE6(): pass

    label("Function_7_3BE6")

    SetChrFlags(0xC, 0x80)
    OP_64(0x2, 0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "明日料理\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x341, 1)
    OP_28(0x2D, 0x1, 0x8)
    TalkEnd(0xFF)
    Return()

    # Function_7_3BE6 end

    SaveToFile()

Try(main)
