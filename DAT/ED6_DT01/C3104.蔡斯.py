from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3104   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3104.x',
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
        'ED6_DT06/CH20141 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT06/CH20141P._CP',             # 00
    )

    ScpFunction(
        "Function_0_B2",           # 00, 0
        "Function_1_C6",           # 01, 1
        "Function_2_E4",           # 02, 2
        "Function_3_1B52",         # 03, 3
        "Function_4_1B53",         # 04, 4
        "Function_5_1B54",         # 05, 5
    )


    def Function_0_B2(): pass

    label("Function_0_B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_C5")
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_C5")

    Return()

    # Function_0_B2 end

    def Function_1_C6(): pass

    label("Function_1_C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E3")

    label("loc_DE")

    OP_22(0x1CD, 0x1, 0x64)

    label("loc_E3")

    Return()

    # Function_1_C6 end

    def Function_2_E4(): pass

    label("Function_2_E4")

    ClearMapFlags(0x10000000)
    AddParty(0x5, 0xFF)
    AddParty(0x6, 0xFF)
    AddParty(0xA, 0xFF)
    EventBegin(0x0)
    OP_66(0x0)
    OP_6D(3160, 0, 9050, 0)
    OP_67(-16400, 26840, -56180, 0)
    OP_6B(1000, 0)
    OP_6C(16000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 24790, 110, -35590, 270)
    SetChrPos(0x102, 25200, 30, -36550, 270)
    SetChrPos(0x106, 22990, 20, -36670, 90)
    SetChrPos(0x10B, 23610, 10, -37570, 45)
    SetChrPos(0x107, 23250, 30, -35430, 90)
    FadeToBright(2000, 0)

    def lambda_198():
        OP_6D(24300, 60, -35590, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_198)
    Sleep(4000)

    def lambda_1B5():
        OP_67(-16400, 37480, -56180, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B5)

    def lambda_1CD():
        OP_6B(800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1CD)
    Sleep(4000)
    Fade(1000)
    OP_44(0x101, 0xFF)
    OP_66(0x1)
    OP_6D(24380, 30, -36240, 0)
    OP_67(0, 37430, -45510, 0)
    OP_6B(600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F呼……\x01",
            "总算逃出来了。\x02\x03",
            "看来还没有搜查到这边来呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F希德少校刚才下令搜查\x01",
            "也是为了故意牵制他们吧。\x02\x03",
            "#013F不过再磨磨蹭蹭的话，\x01",
            "追踪部队恐怕就要追来了。\x02\x03",
            "得先带博士逃到安全的地方……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#102F………唔……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F#3P姐姐、哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F啊，不用担心。\x02\x03",
            "我们一定会\x01",
            "保护好提妲和博士的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x106)

    ChrTalk(
        0x106,
        (
            "#050F……不。\x02\x03",
            "你们俩在这里撤手吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        "#580F咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F经过这次的事件，\x01",
            "我已经完全被情报部的那帮家伙盯上了。\x02\x03",
            "而且老爷子和提妲\x01",
            "也同样会被他们追踪下去。\x02\x03",
            "#051F我带他们两个逃走，\x01",
            "你们也赶快逃去安全的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(
        0x107,
        "#064F阿加特大哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#102F原来如此，变成这样了吗。\x02\x03",
            "的确有道理，\x01",
            "不能再让你们卷入这件事里了，\x01",
            "总之和我们在一起的人越少越好。\x02\x03",
            "#104F可以的话，\x01",
            "我也不想把提妲卷进来……\x02\x03",
            "但考虑到她可能会被抓作人质，\x01",
            "还不如让她和我一起比较好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x10B, 400)

    ChrTalk(
        0x107,
        "#560F爷爷……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F等、等一下！\x02\x03",
            "只有我们安全逃走，\x01",
            "这种做法我绝对接受不了！\x02\x03",
            "约修亚也这么想吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B9():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7B9)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#013F不……\x01",
            "阿加特兄说得很正确。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(
        0x101,
        "#004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F从逃亡还有潜伏的角度来说，\x01",
            "一起行动的人越多，\x01",
            "隐蔽起来就越困难。\x02\x03",
            "所以由阿加特兄单独\x01",
            "带博士他们一起逃比较好。\x02\x03",
            "#015F你的心情我很理解……\x01",
            "但这次还是听阿加特兄的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#580F怎、怎么这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F不错嘛，约修亚，\x01",
            "任何时候都这么明白事理。\x02\x03",
            "#050F艾丝蒂尔。\x01",
            "就在这里坦率地分手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F但、但是……\x02\x03",
            "虽然道理我也明白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#063F#3P艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#104F嗯……\x01",
            "看来还是一副难以接受的样子啊。\x02\x03",
            "#100F这样吧……\x01",
            "你们能不能代我完成一项工作？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AEC():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_AEC)

    def lambda_AFA():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFA)

    def lambda_B08():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B08)
    TurnDirection(0x102, 0x10B, 400)

    ChrTalk(
        0x101,
        "#004F咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#102F首先，希望你们能前往王都。\x02\x03",
            "到了王都之后，\x01",
            "去见格兰赛尔城的艾莉茜雅陛下。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#005F和女王陛下见面？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F此话怎讲？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#102F那个『黑色导力器』……\x02\x03",
            "原本是理查德上校不知从哪里得到的。\x01",
            "　\x02\x03",
            "#104F他把『黑色导力器』叫做『福音』。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F『福音』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F嘁……\x01",
            "很华丽的名字嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#104F这个『福音』之前好像\x01",
            "被某人偷偷地从情报部取了出来。\x02\x03",
            "然后又被做成包裹寄给了卡西乌斯。\x01",
            "　\x02\x03",
            "然而，之前的那个导力停止事件\x01",
            "让情报部知道了导力器的所在。\x02\x03",
            "#102F那些黑衣人『特务兵』\x01",
            "袭击中央工房的真正原因，\x01",
            "既不是我，也不是演算导力器。\x02\x03",
            "他们只是为了回收那东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F是、是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F原来如此……\x01",
            "这样一来，很多事就说得通了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#102F理查德上校很有可能\x01",
            "想利用那东西在王都做些什么。\x02\x03",
            "如果我猜得没错……\x01",
            "应该会发生非常糟糕的事态。\x02\x03",
            "希望你们把这件事传达给女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F非常糟糕的事态……\x01",
            "是指那个导力停止现象吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#104F不……\x01",
            "恐怕利用那个是为了……\x02\x03",
            "#102F抱歉。\x01",
            "我只能言尽于此了。\x02\x03",
            "总之，我希望你们能早日\x01",
            "把那个『福音』的事禀告陛下。\x02\x03",
            "作为逃亡中的我的代理人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F唉……真是的。\x02\x03",
            "#006F听了这么一番话，\x01",
            "我们想拒绝都拒绝不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F如果博士您没问题的话，\x01",
            "我们很乐意接受这个神圣的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        "#101F抱歉，那就拜托你们俩了。\x02",
    )

    CloseMessageWindow()

    def lambda_11AA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_11AA)
    Sleep(400)

    ChrTalk(
        0x107,
        (
            "#063F#3P那、那个……\x02\x03",
            "艾丝蒂尔姐姐。\x01",
            "……约修亚哥哥……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11E9():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_11E9)

    def lambda_11F7():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11F7)
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(
        0x102,
        (
            "#010F提妲……\x01",
            "我们要暂时分别了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F不好意思……\x01",
            "之后我们不能陪你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#065F#3P没、没有的事……\x01",
            "你们根本不用和我道歉。\x02\x03",
            "#562F我一直都受姐姐你们的照顾……\x01",
            "　\x02\x03",
            "对我那么的好、那么的亲切，\x01",
            "对我简直就像妹妹一样……\x02\x03",
            "#069F……呜呜……呜哇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F提妲……\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_134B():
        OP_6D(25380, 30, -36240, 1000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_134B)

    def lambda_1363():

        label("loc_1363")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_1363")

    QueueWorkItem2(0x101, 1, lambda_1363)

    def lambda_1374():

        label("loc_1374")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_1374")

    QueueWorkItem2(0x102, 1, lambda_1374)

    def lambda_1385():

        label("loc_1385")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_1385")

    QueueWorkItem2(0x106, 1, lambda_1385)

    def lambda_1396():

        label("loc_1396")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_1396")

    QueueWorkItem2(0x10B, 1, lambda_1396)
    OP_92(0x107, 0x101, 0x190, 0x1388, 0x0)

    def lambda_13B5():
        OP_94(0x1, 0x107, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_13B5)
    OP_48()
    OP_8C(0x107, 0, 0)
    SetChrChipByIndex(0x107, 0)
    SetChrSubChip(0x107, 1)
    SetChrFlags(0x107, 0x20)
    SetChrFlags(0x107, 0x40)
    OP_8C(0x101, 292, 0)
    OP_94(0x1, 0x101, 0xB4, 0x12C, 0x7D0, 0x0)
    WaitChrThread(0x107, 0x3)

    ChrTalk(
        0x107,
        (
            "#069F#3P谢、谢谢你们救了爷爷……\x01",
            "　\x02\x03",
            "呜……还有……\x01",
            "谢谢你们对我那么好……\x02\x03",
            "#067F……我最喜欢……你们俩了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F嗯……\x01",
            "我也最喜欢你了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2P和你在一起我们也很开心……\x01",
            "　\x02\x03",
            "我们也要谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#053F………………………\x02\x03",
            "#050F虽然依依不舍，\x01",
            "但还是就到此为止吧。\x02\x03",
            "眼泪留到再会那一刻再流吧？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F呜……真是……\x01",
            "你这没血没泪的家伙……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x10B, 0xFF)
    ClearChrFlags(0x107, 0x20)
    SetChrChipByIndex(0x107, 65535)
    TurnDirection(0x107, 0x101, 0)
    OP_94(0x1, 0x107, 0xB4, 0x258, 0x7D0, 0x0)

    def lambda_15EC():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15EC)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(
        0x101,
        (
            "#501F不过……\x01",
            "我们也要和你暂别一段时间了。\x02\x03",
            "虽然发生了很多事，\x01",
            "但和你一起工作得到了很多经验。\x02\x03",
            "谢谢了，阿加特前辈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#055F哎呀……\x01",
            "不要叫得那么肉麻啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#001F啊哈哈，害羞了㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#551F真是的……\x01",
            "不愧是大叔的女儿。\x02\x03",
            "#051F约修亚，\x01",
            "注意看好这个冲动的家伙哦。\x02\x03",
            "除了武术可以独当一面之外，\x01",
            "其他方面都是让人放心不下的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F哼，要你多管闲事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F#2P哈哈，明白了。\x02\x03",
            "#010F阿加特兄也要多加小心。\x02\x03",
            "博士和提妲就拜托你了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#051F啊啊，交给我吧。\x02\x03",
            "那么……\x01",
            "我们先走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10B,
        (
            "#101F再见了！\x01",
            "卡西乌斯的孩子！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#069F保、保重啊！\x01",
            "艾丝蒂尔姐姐、约修亚哥哥！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯！提妲你们也是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#2P愿女神保佑你们！\x01",
            "请各位务必小心！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1957():
        OP_6D(21340, 70, -35800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1957)
    OP_8C(0x106, 315, 400)

    def lambda_1976():
        OP_8E(0xFE, 0x2878, 0x50, 0xFFFF7DB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1976)
    OP_8C(0x107, 270, 400)

    def lambda_1998():
        OP_8E(0xFE, 0x27EC, 0x5A, 0xFFFF7A2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1998)
    Sleep(400)
    OP_8C(0x10B, 315, 400)

    def lambda_19BF():
        OP_8E(0xFE, 0x2878, 0x50, 0xFFFF7DB0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_19BF)
    OP_8C(0x101, 270, 400)
    Sleep(2000)
    OP_20(0x9C4)
    FadeToDark(2000, 0, -1)
    OP_24(0x1CD, 0x5A)
    Sleep(200)
    OP_24(0x1CD, 0x50)
    Sleep(200)
    OP_24(0x1CD, 0x46)
    Sleep(200)
    OP_24(0x1CD, 0x3C)
    Sleep(200)
    OP_24(0x1CD, 0x32)
    Sleep(200)
    OP_24(0x1CD, 0x28)
    Sleep(200)
    OP_24(0x1CD, 0x1E)
    Sleep(200)
    OP_24(0x1CD, 0x14)
    Sleep(200)
    OP_24(0x1CD, 0xA)
    Sleep(200)
    OP_24(0x1CD, 0x0)
    OP_0D()
    Sleep(1000)
    OP_AD(0x40044, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_83(0x14, 0x0)
    OP_A2(0x5CE)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xF3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACF")
    ShowSaveMenu()

    label("loc_1ACF")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x571)
    OP_A2(0x533)
    OP_A2(0x5CF)
    OP_B8(0x6)
    OP_B8(0x5)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0xA, 0xFF)
    OP_28(0x54, 0x4, 0x2)
    OP_28(0x54, 0x4, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_1B1A")
    Jump("loc_1B45")

    label("loc_1B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1B2D")
    OP_2B(0x43, 0x1)
    Jump("loc_1B45")

    label("loc_1B2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x44, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_1B40")
    OP_2B(0x43, 0x2)
    Jump("loc_1B45")

    label("loc_1B40")

    OP_2B(0x43, 0x3)

    label("loc_1B45")

    OP_A2(0x3FA)
    NewScene("ED6_DT01/R4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E4 end

    def Function_3_1B52(): pass

    label("Function_3_1B52")

    Return()

    # Function_3_1B52 end

    def Function_4_1B53(): pass

    label("Function_4_1B53")

    Return()

    # Function_4_1B53 end

    def Function_5_1B54(): pass

    label("Function_5_1B54")

    Return()

    # Function_5_1B54 end

    SaveToFile()

Try(main)
