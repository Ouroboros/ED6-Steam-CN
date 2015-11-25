from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T2130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_2502",         # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x335)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D")
    Call(1, 1)
    Jump("loc_2501")

    label("loc_7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1DA")
    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_101")

    ChrTalk(
        0xFE,
        (
            "如果有什么发现，\x01",
            "一定要马上回来告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拜托了！\x01",
            "如果找到了财宝，我会分给你们的！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Jump("loc_1D7")

    label("loc_101")


    ChrTalk(
        0xFE,
        "哦～你们回来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，找到财宝了没有？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F抱歉，还没有找到。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "如果有什么发现，\x01",
            "一定要马上回来告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "拜托了！\x01",
            "如果找到了财宝，我会分给你们的！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)

    label("loc_1D7")

    Jump("loc_2501")

    label("loc_1DA")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x11, 0x10)
    Fade(1000)
    SetChrPos(0x101, 54200, 0, 49000, 270)
    SetChrPos(0x102, 54200, 0, 47500, 270)
    SetChrPos(0x105, 56000, 0, 48500, 270)
    TalkBegin(0x11)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x3E8)
    ClearChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_3CF")
    OP_2B(0x1E, 0x2)
    OP_2C(0x1E, 0x3E8)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "………咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "你们不是前些日子的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#508F啊，我说呢，\x01",
            "你不就是我们在沙滩遇到的那个人吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "请叫我吉米。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "幸亏你们那时救了我啊。\x01",
            "再次向你们表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嗯………………\x01",
            "这次你们是\x01",
            "看了公告板而来的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_435")

    label("loc_3CF")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "………………咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "喂，\x01",
            "你们是游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对了，\x01",
            "一定是看了公告板才来的对吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_653")
    OP_28(0x1E, 0x4, 0x4)
    OP_28(0x1E, 0x4, 0x8)
    OP_28(0x1E, 0x1, 0x1)
    OP_28(0x1E, 0x1, 0x2)
    OP_28(0x1E, 0x1, 0x4)
    OP_28(0x1E, 0x1, 0x8)
    OP_A2(0x0)

    ChrTalk(
        0x101,
        (
            "#000F嗯，正是……\x02\x03",
            "为什么你会选在\x01",
            "这种地方等我们来啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "因为这里很好找啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我要是一直在这里，\x01",
            "就不能去赚钱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "单是委托游击士办事，\x01",
            "就要花掉不少的费用啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F那你就快点告诉我们委托的内容吧。\x01",
            "　\x02\x03",
            "不管怎么说，\x01",
            "公告板上写的那些东西\x01",
            "让人有些好奇呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，我说了之后，\x01",
            "你们可不要太过期待哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_873")

    label("loc_653")

    OP_28(0x1E, 0x4, 0x8)
    OP_28(0x1E, 0x4, 0x4)
    OP_28(0x1E, 0x4, 0x2)
    OP_28(0x1E, 0x1, 0x1)
    OP_28(0x1E, 0x1, 0x2)
    OP_28(0x1E, 0x1, 0x4)
    OP_28(0x1E, 0x1, 0x8)
    OP_A2(0x0)

    ChrTalk(
        0x101,
        (
            "#004F哎？\x01",
            "委托的事情是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "什么，你们没看见吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还以为你们\x01",
            "仔细看过委托内容之后\x01",
            "才来见面地点的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0x102,
        (
            "#014F见面地点……\x01",
            "就是这个教堂吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "因为这里很好找啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过我要是一直在这里，\x01",
            "就不能去赚钱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "单是委托游击士办事，\x01",
            "就要花掉不少的费用啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(
        0x101,
        "#006F那么，到底是什么委托呢？\x02",
    )

    CloseMessageWindow()

    label("loc_873")

    OP_8C(0xFE, 90, 0)

    ChrTalk(
        0xFE,
        (
            "事实上我最近得到了\x01",
            "一幅出乎意料的古地图。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "没想到那幅地图竟然是…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F那幅地图是……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "竟然是大海盗希鲁玛\x01",
            "留下来的藏宝图啊！！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎呀啊！？真的吗！\x02\x03",
            "#000F……的确是大发现呢！\x01",
            "但那个海盗又是什么人呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "连、连希鲁玛是谁\x01",
            "你都不知道！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "难以置信啊，\x01",
            "你还算是卢安的市民吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#509F……不要主观臆断地\x01",
            "把所有人都当成卢安的市民好不好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#040F希鲁玛这个人好像是……\x02",
    )

    CloseMessageWindow()

    def lambda_AD5():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD5)

    def lambda_AE3():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE3)

    def lambda_AF1():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF1)

    ChrTalk(
        0x105,
        (
            "#040F一百年以前在卢安周围\x01",
            "盘踞的一个海盗……吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "对呀！你真棒！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王立学院就是不一样！\x01",
            "不只是校服可爱而已哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F啊～\x01",
            "科洛丝，好厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F哎呀，艾丝蒂尔……\x01",
            "别这么夸我了。\x02\x03",
            "我只是因为听到你们讨论，\x01",
            "才偶然想起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "其实我就是想委托你们\x01",
            "帮我去找希鲁玛的财宝。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CAB():
        TurnDirection(0x101, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CAB)

    def lambda_CB9():
        TurnDirection(0x102, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB9)

    ChrTalk(
        0xFE,
        (
            "首先从地图上\x01",
            "标有记号的地方开始……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_E9D")

    ChrTalk(
        0xFE,
        (
            "还记得我上次\x01",
            "遇到你们的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看，\x01",
            "沙滩中有一个看似洼地的地形。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在梅威海道的中部\x01",
            "稍微靠边一点的地方。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        "没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "藏宝图上也把那个洼地\x01",
            "作为标志画了出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F也就是说那个地方有什么东西吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "对，就是这样的。\x01",
            "我本想去现场调查的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好不容易找到了洼地，\x01",
            "但是接下来\x01",
            "就遇上了魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以啦，\x01",
            "这次就只能拜托你们这些职业人士了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBA")

    label("loc_E9D")


    ChrTalk(
        0xFE,
        (
            "梅威海道沿岸的沙滩上\x01",
            "有一处被山崖\x01",
            "围起来的洼地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "藏宝图上也把那个洼地\x01",
            "作为标志画了出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但我去那里调查的时候\x01",
            "被魔兽袭击了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "所以这次我只能\x01",
            "拜托你们这些职业人士了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FBA")


    ChrTalk(
        0x101,
        "#000F那找到洼地之后呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "在地图上洼地的东南方向\x01",
            "有一个标记了×的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎么想，\x01",
            "那里都应该是埋藏了财宝的场所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，\x01",
            "的确是有这种可能。\x02\x03",
            "#004F…………哎呀，对了，\x01",
            "应该把这些记录下来才是。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    ChrTalk(
        0x102,
        (
            "#010F那么就先好好地整理一下思路吧……\x01",
            "　\x02\x03",
            "到达洼地后往其东南方向……\x01",
            "也就是卢安所在方向的沙滩，\x01",
            "对那里进行调查。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x335)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206D")
    OP_28(0x1E, 0x1, 0x20)
    OP_63(0x101)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F往卢安方向的沙滩啊……\x02\x03",
            "#004F啊，对了，在这之前\x01",
            "我们曾在沙滩边上发现过有趣的东西啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0xFE,
        "什、什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "发、发、\x01",
            "发现了什么东西？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F我想起来了，\x01",
            "是那个飘到岸上的木桶……\x02\x03",
            "而且还找到了短剑和一幅航海图。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F说起那张航海图，\x01",
            "都已经烂得差不多了……\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    OP_63(0xFE)

    ChrTalk(
        0xFE,
        (
            "航、航海图！\x01",
            "哇哦～～这可是大发现！\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0xFE, 0x0, 0x2BC, 0xBB8, 0x0)
    TurnDirection(0x101, 0xFE, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)

    ChrTalk(
        0xFE,
        "快、快点给我看看～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F不、不要那么激动嘛。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "古海图的残片\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x335, 1)
    OP_28(0x1E, 0x1, 0x40)
    OP_28(0x1E, 0x4, 0x10)
    OP_8E(0xFE, 0xCF08, 0x0, 0xBBE4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(800)
    OP_63(0xFE)
    Sleep(400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "哇啊～～\x01",
            "这、这个是～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太、太好了！\x01",
            "这玩意儿，简直绝了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(
        0xFE,
        (
            "这个肯定就是\x01",
            "海盗希鲁玛的藏宝图！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#044F#4P#1K…………咦？\x02",
    )


    ChrTalk(
        0x105,
        "#004F#2P#1K啊？\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(
        0x101,
        (
            "#509F我说大哥。\x02\x03",
            "你从刚才开始不是一直都说\x01",
            "自己手上拿的就是藏宝图吗。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)

    ChrTalk(
        0xFE,
        (
            "不不，我那个肯定就是\x01",
            "『藏宝图的藏宝图』了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是用来标示财宝的隐藏地点的\x01",
            "地图所在的隐藏地点的地图啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x105,
        "#045F哎呀，好像有点复杂啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F…………可是，\x01",
            "那个航海图是从木桶里面找到的啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F算了，就这样吧。\x01",
            "　\x02\x03",
            "虽然怎么想都觉得\x01",
            "里面会有那幅航海图是一种偶然……\x02\x03",
            "不过那个位置的确是\x01",
            "地图上标记了×的地方。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        "#040F嗯，是呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F至少他本人是非常高兴的，\x01",
            "这不就已经足够了吗。\x02\x03",
            "#004F……哦，对了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    def lambda_1998():
        TurnDirection(0x102, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1998)

    def lambda_19A6():
        TurnDirection(0x105, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19A6)

    ChrTalk(
        0x101,
        (
            "#000F请问，吉米先生。\x01",
            "和图一起找到的短剑怎么处理呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "那个就送给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为谢礼可能有些寒酸，\x01",
            "就算是我的一点点心意吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们就收下，\x01",
            "想怎么用就怎么用吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "哎呀，真是太好了。\x01",
            "终于找到了这幅航海图。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿， \x01",
            "现在开始可有的忙了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好～的，\x01",
            "快点解读它，\x01",
            "让欧尼尔爷爷大吃一惊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F……欧尼尔爷爷？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "再见啦！\x01",
            "谢谢你们的帮助！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BCE():

        label("loc_1BCE")

        TurnDirection(0x101, 0x11, 0)
        OP_48()
        Jump("loc_1BCE")

    QueueWorkItem2(0x101, 1, lambda_1BCE)

    def lambda_1BDF():

        label("loc_1BDF")

        TurnDirection(0x102, 0x11, 0)
        OP_48()
        Jump("loc_1BDF")

    QueueWorkItem2(0x102, 1, lambda_1BDF)

    def lambda_1BF0():

        label("loc_1BF0")

        TurnDirection(0x105, 0x11, 0)
        OP_48()
        Jump("loc_1BF0")

    QueueWorkItem2(0x105, 1, lambda_1BF0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD160, 0x0, 0xB5A4, 0x1770, 0x0)
    OP_8C(0xFE, 135, 0)
    OP_96(0xFE, 0xD6D8, 0x0, 0xAFC8, 0x5DC, 0x1B58)
    OP_8E(0xFE, 0xE1A0, 0x0, 0xAFFA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0x91B4, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x320)

    ChrTalk(
        0x105,
        (
            "#043F是欧尼尔爷爷……吗。\x02\x03",
            "原来如此……\x01",
            "是这么一回事啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1CF4():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CF4)

    def lambda_1D02():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D02)

    ChrTalk(
        0x101,
        (
            "#501F嗯？\x01",
            "欧尼尔爷爷怎么了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F他是经营杂货店的那个老爷爷……\x01",
            "　\x02\x03",
            "要说他有什么缺点的话，\x01",
            "就是谈到无论什么事\x01",
            "他都要夸大其词吹嘘一番。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哎呀，还有这样的人啊。\x02\x03",
            "这么说吉米先生就是\x01",
            "把那个爷爷的夸夸其谈\x01",
            "当作真的去对待了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F对啊，\x01",
            "看起来好像就是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉，\x01",
            "思想太过单纯也很麻烦啊。\x02\x03",
            "#000F啊，不过……\x02\x03",
            "虽说这样，\x01",
            "但他还是通过那个爷爷说的话\x01",
            "才找到了那张航海图。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F嗯，的确是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F呵呵，\x01",
            "真是让人觉得不可思议啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F只要去相信，就会有回报呢。\x01",
            "　\x02\x03",
            "……说实话，\x01",
            "我觉得吉米先生也有点信过头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F用尽全力追寻自己的梦想，\x01",
            "又何尝不是一种人生呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查古地图】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_24F5")

    label("loc_206D")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(
        0xFE,
        "就是这样吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯，相当不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F……过奖了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F唔～不过不太好找啊。\x02\x03",
            "照刚才所说的线索，\x01",
            "从洼地向东南方向找就行了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 0)

    ChrTalk(
        0x105,
        "#043F嗯，可是海滩范围相当大……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#013F的确…………\x01",
            "线索还不太够呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "哦～\x01",
            "各位不用有什么顾虑。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xFE, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "沿着梅威海道的边上\x01",
            "走遍每个角落的话，\x01",
            "我想就一定可以找到的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(
        0x101,
        (
            "#007F可关键是……\x01",
            "要仔细找一遍，\x01",
            "不知道有没有那么多体力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F你肯定没问题的，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F算了，虽然不是非常困难的事情……\x02\x03",
            "但做起来也并不是很轻松…… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F这样效率虽然很低，\x01",
            "但是也仅有这个办法了。\x02\x03",
            "只有沿着海道边彻底走一遍了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#007F呼，没办法了。\x02",
    )

    CloseMessageWindow()

    def lambda_2452():
        TurnDirection(0x101, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2452)

    def lambda_2460():
        TurnDirection(0x102, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2460)

    ChrTalk(
        0x102,
        (
            "#010F那么，要是发现了什么，\x01",
            "我们会再来汇报的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "拜托了！\x01",
            "如果找到了财宝，我会分给你们的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F5")

    EventEnd(0x0)
    TalkEnd(0x11)
    OP_8C(0x11, 90, 0)

    label("loc_2501")

    Return()

    # Function_0_66 end

    def Function_1_2502(): pass

    label("Function_1_2502")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0x11, 0x10)
    Fade(1000)
    SetChrPos(0x101, 54200, 0, 49000, 270)
    SetChrPos(0x102, 54200, 0, 47500, 270)
    SetChrPos(0x105, 56000, 0, 48500, 270)
    TalkBegin(0x11)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x3E8)
    ClearChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2612")

    ChrTalk(
        0x101,
        (
            "#501F啊，吉米先生。\x01",
            "我们回来晚了，真抱歉。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "哦哦，终于回来了吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，找到财宝了没有？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2666")

    label("loc_2612")


    ChrTalk(
        0x101,
        "#001F呀嗬～吉米先生。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "哦～你们回来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那么，找到财宝了没有？\x02",
    )

    CloseMessageWindow()

    label("loc_2666")


    ChrTalk(
        0x101,
        (
            "#505F嗯～财宝倒是没有找到……\x01",
            "　\x02\x03",
            "#508F不过，\x01",
            "却发现了一把古代的短剑和一张航海图。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    OP_63(0xFE)

    ChrTalk(
        0xFE,
        (
            "航、航海图！\x01",
            "哇哦～～这可是大发现！\x02",
        )
    )

    CloseMessageWindow()
    OP_94(0x1, 0xFE, 0x0, 0x2BC, 0xBB8, 0x0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0xFE, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)

    ChrTalk(
        0xFE,
        "快、快点给我看看～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F不、不要那么激动嘛。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "古海图的残片\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x335, 1)
    OP_28(0x1E, 0x1, 0x40)
    OP_28(0x1E, 0x4, 0x10)
    OP_8E(0xFE, 0xCF08, 0x0, 0xBBE4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Sleep(400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0xFE,
        (
            "哇啊～～\x01",
            "这、这个是～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "太、太好了！\x01",
            "这玩意儿，简直绝了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(
        0xFE,
        (
            "这个肯定就是\x01",
            "海盗希鲁玛的藏宝图！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#044F#4P#1K…………咦？\x02",
    )


    ChrTalk(
        0x105,
        "#004F#2P#1K啊？\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    ChrTalk(
        0x101,
        (
            "#509F我说大哥。\x02\x03",
            "你从刚才开始不是一直都说\x01",
            "自己手上拿的就是藏宝图吗。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)

    ChrTalk(
        0xFE,
        (
            "不不，我那个肯定就是\x01",
            "『藏宝图的藏宝图』了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是用来标示财宝的隐藏地点的\x01",
            "地图所在的隐藏地点的地图啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(
        0x105,
        "#045F哎呀，好像有点复杂啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F…………可是，\x01",
            "那个航海图是从木桶里面找到的啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F5A")

    ChrTalk(
        0x102,
        (
            "#010F算了，就这样吧。\x01",
            "　\x02\x03",
            "现在可不是拘泥于\x01",
            "这种小事的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哦，对了。\x02\x03",
            "#002F对不起，吉米先生。\x01",
            "我们有很急的事要办，\x01",
            "不得不走了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        (
            "啊啊，没关系。\x01",
            "总之今天要谢谢你们啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "我也不能再在这里磨蹭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要尽早解读它，\x01",
            "然后让欧尼尔爷爷\x01",
            "大吃一惊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "再见啦！谢谢你们的帮助！\x02",
    )

    CloseMessageWindow()

    def lambda_2DB6():

        label("loc_2DB6")

        TurnDirection(0x101, 0x11, 0)
        OP_48()
        Jump("loc_2DB6")

    QueueWorkItem2(0x101, 1, lambda_2DB6)

    def lambda_2DC7():

        label("loc_2DC7")

        TurnDirection(0x102, 0x11, 0)
        OP_48()
        Jump("loc_2DC7")

    QueueWorkItem2(0x102, 1, lambda_2DC7)

    def lambda_2DD8():

        label("loc_2DD8")

        TurnDirection(0x105, 0x11, 0)
        OP_48()
        Jump("loc_2DD8")

    QueueWorkItem2(0x105, 1, lambda_2DD8)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD160, 0x0, 0xB5A4, 0x1770, 0x0)
    OP_8C(0xFE, 135, 0)
    OP_96(0xFE, 0xD6D8, 0x0, 0xAFC8, 0x5DC, 0x1B58)
    OP_8E(0xFE, 0xE1A0, 0x0, 0xAFFA, 0x1388, 0x0)
    OP_8E(0xFE, 0xE678, 0x0, 0x91B4, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x320)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F好，\x01",
            "那我们也赶快走吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2ED0():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ED0)

    def lambda_2EDE():
        TurnDirection(0x105, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2EDE)

    ChrTalk(
        0x101,
        "#002F嗯！\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查古地图】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_383E")

    label("loc_2F5A")


    ChrTalk(
        0x102,
        (
            "#010F算了，就这样吧。\x01",
            "　\x02\x03",
            "#010F虽然怎么想都觉得\x01",
            "里面会有那幅航海图是一种偶然……\x02\x03",
            "不过正因为吉米先生\x01",
            "相信有那张古地图的存在，\x01",
            "所以才有这样的发现吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        "#040F呵呵，的确是这样。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F唔～仔细想想看。\x02\x03",
            "至少他本人是非常高兴的，\x01",
            "这不就已经足够了吗。\x02\x03",
            "#004F……哦，对了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    def lambda_3138():
        TurnDirection(0x102, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3138)

    def lambda_3146():
        TurnDirection(0x105, 0x11, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3146)

    ChrTalk(
        0x101,
        (
            "#000F请问，吉米先生。\x01",
            "和图一起找到的短剑怎么处理呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(
        0xFE,
        "…………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "那个就送给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "作为谢礼可能有些寒酸，\x01",
            "就算是我的一点点心意吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "你们就收下，\x01",
            "想怎么用就怎么用吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "这次你们完成了一件\x01",
            "了不起的工作呢。\x01",
            "这幅航海图肯定是个大发现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿， \x01",
            "现在开始可有的忙了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦，\x01",
            "我也不能再在这里磨蹭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要尽早解读它，\x01",
            "然后让欧尼尔爷爷\x01",
            "大吃一惊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#044F……欧尼尔爷爷？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "再见啦！谢谢你们的帮助！\x02",
    )

    CloseMessageWindow()

    def lambda_33A7():

        label("loc_33A7")

        TurnDirection(0x101, 0x11, 0)
        OP_48()
        Jump("loc_33A7")

    QueueWorkItem2(0x101, 1, lambda_33A7)

    def lambda_33B8():

        label("loc_33B8")

        TurnDirection(0x102, 0x11, 0)
        OP_48()
        Jump("loc_33B8")

    QueueWorkItem2(0x102, 1, lambda_33B8)

    def lambda_33C9():

        label("loc_33C9")

        TurnDirection(0x105, 0x11, 0)
        OP_48()
        Jump("loc_33C9")

    QueueWorkItem2(0x105, 1, lambda_33C9)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xD160, 0x0, 0xB5A4, 0x1770, 0x0)
    OP_8C(0xFE, 135, 0)
    ClearChrFlags(0xFE, 0x1)
    OP_96(0xFE, 0xD6D8, 0x0, 0xAFC8, 0x5DC, 0x1B58)
    OP_8E(0xFE, 0xE1A0, 0x0, 0xAFFA, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xE678, 0x0, 0x91B4, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x105, 0x1)
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x12, 0x320)

    ChrTalk(
        0x105,
        (
            "#043F是欧尼尔爷爷……吗。\x02\x03",
            "原来如此……\x01",
            "是这么一回事啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34C8():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34C8)

    def lambda_34D6():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34D6)

    ChrTalk(
        0x101,
        (
            "#501F嗯…………？\x01",
            "欧尼尔爷爷怎么了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#040F他是经营杂货店的那个老爷爷……\x01",
            "　\x02\x03",
            "要说他有什么缺点的话，\x01",
            "就是谈到无论什么事\x01",
            "他都要夸大其词吹嘘一番。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F哎呀，还有这样的人啊。\x02\x03",
            "这么说吉米先生就是\x01",
            "把那个爷爷的夸夸其谈\x01",
            "当作真的去对待了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#045F对啊，\x01",
            "看起来好像就是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉，\x01",
            "思想太过单纯也很麻烦啊。\x02\x03",
            "#000F啊，不过……\x02\x03",
            "虽说这样，\x01",
            "但他还是通过那个爷爷说的话\x01",
            "才找到了那张航海图。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F嗯，的确是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#040F呵呵，\x01",
            "真是让人觉得不可思议啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#505F只要去相信，就会有回报呢。\x01",
            "　\x02\x03",
            "……说实话，\x01",
            "我觉得吉米先生也有点信过头了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F用尽全力追寻自己的梦想，\x01",
            "又何尝不是一种人生呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查古地图】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_383E")

    EventEnd(0x0)
    TalkEnd(0x11)
    Return()

    # Function_1_2502 end

    SaveToFile()

Try(main)
