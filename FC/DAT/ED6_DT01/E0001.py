from ED6ScenarioHelper import *

def main():
    CreateScenaFile(
        FileName            = 'E0001   ._SN',
        MapName             = 'event',
        Location            = 'E0001.x',
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
        '摩尔根将军',                           # 9
        '王国军士兵Ａ',                         # 10
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
        'ED6_DT07/CH02080 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH02080P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
    )

    DeclNpc(
        X                   = -7752,
        Z                   = -2000,
        Y                   = 4527,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -7116,
        Z                   = -2000,
        Y                   = -197,
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


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_146",          # 01, 1
        "Function_2_147",          # 02, 2
        "Function_3_15D",          # 03, 3
        "Function_4_FF7",          # 04, 4
        "Function_5_1641",         # 05, 5
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115")
    OP_A2(0x328)
    Event(0, 3)

    label("loc_115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_123")
    OP_A3(0x3FA)
    Event(0, 5)

    label("loc_123")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_12F"),
        (SWITCH_DEFAULT, "loc_145"),
    )


    label("loc_12F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142")
    OP_A2(0x329)
    Event(0, 4)

    label("loc_142")

    Jump("loc_145")

    label("loc_145")

    Return()

    # Function_0_FA end

    def Function_1_146(): pass

    label("Function_1_146")

    Return()

    # Function_1_146 end

    def Function_2_147(): pass

    label("Function_2_147")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_147")

    label("loc_15C")

    Return()

    # Function_2_147 end

    def Function_3_15D(): pass

    label("Function_3_15D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(1000, 5000, -3500, 0)
    SetChrPos(0x101, 1000, 5000, -3590, 225)
    SetChrPos(0x102, -360, 5000, -3840, 135)
    SetChrPos(0x103, 730, 5000, -4940, 315)

    ChrTalk(
        0x101,
        (
            "#002F虽然已经调查了一遍，\x01",
            "可是一个人也没有发现……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F看样子乘客被空贼用空贼飞艇\x01",
            "用空贼飞艇带走的可能性很高。\x02\x03",
            "……大概，是到他们的据点去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯……\x02\x03",
            "好不容易\x01",
            "才找到的线索就这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F好了好了。\x01",
            "不要这么愁眉苦脸的。\x02\x03",
            "现在并不是\x01",
            "一点线索都没有哦。\x02\x03",
            "你们想想，为什么那帮家伙\x01",
            "会把定期船藏在这种地方呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F正如刚才所见，\x01",
            "定期船内的导力完全停止了……\x02\x03",
            "这也就意味着，\x01",
            "导力引擎被他们拿走了。\x02\x03",
            "而那些家伙多次\x01",
            "来回运送大量的货物。\x02\x03",
            "考虑这样做所花费的时间和带来的风险，\x01",
            "用定期船把货物运往自己的据点\x01",
            "效率反倒应该高得多吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，确实……\x02\x03",
            "那么，空贼把定期船\x01",
            "藏在这个地方的原因就是……\x02\x03",
            "仔细考虑一下的话……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【为了挑选货物】\x01",                    # 0
            "【为了把人质转移到空贼飞艇上】\x01",      # 1
            "【为了抢夺导力引擎】\x01",                # 2
            "【为了逃避王国军的搜捕】\x01",            # 3
            "【因为据点在特殊的地方】\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6DB"),
        (1, "loc_79B"),
        (2, "loc_851"),
        (3, "loc_90D"),
        (4, "loc_A05"),
        (SWITCH_DEFAULT, "loc_A2D"),
    )


    label("loc_6DB")


    ChrTalk(
        0x103,
        (
            "#026F确实，这里比较宽阔，\x01",
            "挑选货物时也许很方便。\x02\x03",
            "但是这却无法构成\x01",
            "空贼把定期船藏在这个地方的理由。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2D")

    label("loc_79B")


    ChrTalk(
        0x103,
        (
            "#026F确实，在把人质转移到空贼飞艇上的过程中，\x01",
            "定期船必须要着陆。\x02\x03",
            "但是这却无法构成\x01",
            "空贼把定期船藏在这个地方的理由。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2D")

    label("loc_851")


    ChrTalk(
        0x103,
        (
            "#026F确实，要把引擎拔除的话，\x01",
            "定期船必须要着陆。\x02\x03",
            "但是这却无法构成\x01",
            "空贼把定期船藏在这个地方的理由。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2D")

    label("loc_90D")


    ChrTalk(
        0x103,
        (
            "#026F确实，定期船很大，\x01",
            "很容易会被王国军发现……\x02\x03",
            "所以把它藏在据点以外的\x01",
            "据点以外的场所的可能性很高。\x02\x03",
            "但是，这个解释\x01",
            "也不能说是决定性的理由。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2D")

    label("loc_A05")


    ChrTalk(
        0x103,
        "#020F对，就是因为这个。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2D")

    label("loc_A2D")


    ChrTalk(
        0x103,
        (
            "#020F根据我的推测，\x01",
            "他们的据点应该是个地形特殊的地方。\x02\x03",
            "１０～１５亚矩……\x02\x03",
            "也就是说只能让空贼飞艇\x01",
            "这种小型艇降落的特殊场所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F原、原来是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F像山峦、峡谷这样\x01",
            "高低差很大的复杂地形……\x02\x03",
            "应该是最值得怀疑的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F对，我也这么想。\x02\x03",
            "如果真是那样的话……\x01",
            "那真是超出我们能力范围了。\x02\x03",
            "他们的据点很有可能\x01",
            "是在步行所涉足不到的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F怎、怎么办呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F是啊……\x02\x03",
            "虽然让人失望，但现在唯有\x01",
            "向军队说明情况并请求他们协助了。\x02\x03",
            "毕竟他们拥有军用飞艇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F哎～……\x01",
            "搞了半天还是要依靠军队啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F这艘定期船的事情\x01",
            "最后肯定要报告给军队的。\x02\x03",
            "不管他们的态度怎么样，\x01",
            "我认为现在还是合作比较好。\x02\x03",
            "这也是为了早点解放人质啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F嗯，是啊……\x02\x03",
            "现在不是任性的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F总之，我们先回游击士协会\x01",
            "向卢格兰爷爷汇报一下吧。\x02\x03",
            "使用协会的导力通信器，\x01",
            "就可以和哈肯大门联络了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_3_15D end

    def Function_4_FF7(): pass

    label("Function_4_FF7")

    EventBegin(0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)

    ChrTalk(
        0x101,
        (
            "#004F哎、哎哎～～！？\x02\x03",
            "这、这是怎么回事啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F哈……\x01",
            "这真是意料之外的来者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#025F唔，看来这次\x01",
            "连联络的功夫也省了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "发现一干\x01",
            "手持武器的嫌疑犯！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "你们！\x01",
            "老实举起手来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是世态炎凉啊，\x01",
            "连小女孩也做起空贼来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F谁、谁是空贼啊！？\x02\x03",
            "没看到我身上的徽章吗！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "男性的声音",
        "哼，游击士的徽章吗……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "男性的声音",
        (
            "凭这种东西\x01",
            "就能证明自身的清白？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F摩、摩尔根将军！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F为什么会在这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#160F根据各部队的报告，\x01",
            "这里尚未进行细致的搜查。\x01",
            "我们来这里也是理所当然的事情……\x02\x03",
            "但是，万万没想到\x01",
            "你们竟然和空贼勾结。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F在没有真凭实据之前，\x01",
            "请不要这样随意下结论。\x02\x03",
            "我们只是先你们一步\x01",
            "到这里做现场调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#160F那么空贼在哪里？\x02\x03",
            "船内的乘客又在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F只差一步就能抓住那些空贼了，\x01",
            "这是我们的疏忽。\x02\x03",
            "作为人质的乘客也不在定期船里面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#160F哼，真是不打自招……\x02\x03",
            "原来在我们到来之前，\x01",
            "你们已经向空贼通风报信了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F等、等一下！\x01",
            "你这样说实在是太过分了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#162F这是我该讲的台词！\x02\x03",
            "来人！\x01",
            "把这三个嫌疑犯抓起来！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T1410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_FF7 end

    def Function_5_1641(): pass

    label("Function_5_1641")

    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-2670, 5000, -10370, 0)
    OP_6C(315000, 0)
    OP_6B(2400, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x104, 0, 5000, -10200, 180)
    SetChrPos(0x103, 0, 5000, -1650, 180)
    FadeToBright(2000, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("青年的声音")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……以上就是\x01",
            "在王国北部发生的空贼事件的始末。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "是啊……没想到没落的\x01",
            "卡普亚家族子孙竟会沦落到如此田地。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "对了，如果王国方面问起这件事，\x01",
            "你可要帮我做一下适当的应对哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "嗯，结果还是没有遇上他。\x01",
            "也许是因为发生了什么麻烦的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "现在还不能确定这和空贼事件有没有关联，\x01",
            "不过肯定的是有其他势力在暗中活动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "呵呵，才不是。\x01",
            "我也认识了一些有趣的朋友啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "这里料理美味，美人又多。\x01",
            "简直就是我梦寐以求的国度。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "真想一辈子住在这里啊～～\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "……………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "知道啦，知道啦。\x01",
            "拜托你不要发出那么吓人的声音嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "好的，那边就继续拜托你了，\x01",
            "别忘了代我向首相大人问好。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "下次再联络吧，我的好友。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_77(0xFF, 0xFF, 0xFF, 0x7D000, 0x0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#030F呵呵，还是老样子，\x01",
            "总是大惊小怪的家伙。\x02\x03",
            "做事一点也不通融，\x01",
            "这该说是可爱呢还是……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "女性的声音",
        "……是携带用的小型通信器呢。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "女性的声音",
        (
            "就这么带在身边到处走，\x01",
            "也太过显眼了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x104, 0x103, 500)

    def lambda_1BEB():
        OP_6B(3000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BEB)
    OP_6D(-190, 5000, -6110, 1000)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#030F雪……雪拉君。\x02",
    )

    CloseMessageWindow()

    def lambda_1C29():
        OP_6D(100, 5000, -9000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C29)
    OP_8E(0x103, 0x0, 0x1388, 0xFFFFE142, 0x7D0, 0x0)

    ChrTalk(
        0x103,
        (
            "#020F不过没想到的是，\x01",
            "你竟然会有中央工房\x01",
            "还未实用化的导力通信器……\x02\x03",
            "你，到底是什么人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F讨厌啦，干嘛跟人家这么见外～\x01",
            "下次再这样说人家可不依哦。\x02\x03",
            "漂泊的诗人和天才演奏家——\x01",
            "奥利维尔·朗海姆。\x01",
            "你不是应该很清楚吗？\x02\x03",
            "不过，如果想知道得更多的话，\x01",
            "那就只能以枕边话的形式来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F很遗憾，\x01",
            "你这种小丑戏对我来说是不管用的哦。\x02\x03",
            "埃雷波尼亚帝国的谍报员先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F…………………………\x02\x03",
            "呵呵，看来『银闪』这个称号\x01",
            "果然不是浪得虚名啊。\x02\x03",
            "在艾丝蒂尔君他们面前，\x01",
            "你也是假装不知道的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F因为我不想让\x01",
            "那两个孩子再担心多余的事情。\x02\x03",
            "别再把话题扯远了，\x01",
            "老实交代清楚你自己的事情吧。\x02\x03",
            "你的目的是什么？\x01",
            "为什么要潜入利贝尔王国？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F在此之前，\x01",
            "可以让我澄清两点吗？\x02\x03",
            "首先，本人可没演什么小丑戏。\x01",
            "一直以来我都是以真实的性情待人。\x02\x03",
            "说我伪装什么的是不对的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F啊～好吧。\x02\x03",
            "就当白吃白喝\x01",
            "是你真实的性情好了。\x02\x03",
            "不过那之后，借由被逮捕去到\x01",
            "哈肯大门收集情报则是经过计划的吧。\x02\x03",
            "虽然应该不至于\x01",
            "算计到我们会被抓这件事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F呵呵……\x01",
            "随你怎么想好了。\x02\x03",
            "还有一点要澄清的是……\x01",
            "这个装置并不是导力通信器。\x02\x03",
            "而是帝国出土的『古代遗物』。\x02\x03",
            "它不仅能和所有导力通信器进行通信，\x01",
            "而且还能将讯号加密，避免被监听。\x02\x03",
            "对公务繁忙的人来说，可是十分有用哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F『古代遗物』……\x01",
            "是七耀教会管理的神圣遗物吗？\x02\x03",
            "我越来越想知道\x01",
            "你来王国的目的到底是什么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F哎呀，讨厌……\x01",
            "雪拉君你真的好主动哦。\x02\x03",
            "一位神秘美人怎么能\x01",
            "随便打听一位天才美男的秘密呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F……………………………\x02\x03",
            "想亲近真的美人吗？\x01",
            "我的鞭子也许能帮帮你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F不、不要啊，雪拉君。\x01",
            "你就别和我开这种可怕的玩笑了……\x02\x03",
            "还、还是先把说笑放在一边吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F真是的。\x01",
            "一开始老实交代不就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F正如你所说的那样，\x01",
            "本人的确是帝国的谍报人员。\x02\x03",
            "不过……\x01",
            "我来这里的目的并不是为了收集情报。\x02\x03",
            "我是为了来见一个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#020F一个人……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#030F是一个你很熟悉的人。\x02\x03",
            "一位被王国军尊奉为\x01",
            "最强的剑士、稀世的战略家。\x02\x03",
            "大陆上仅有的四个Ｓ级游击士之一。\x02\x03",
            "『剑圣』卡西乌斯·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1641 end

    SaveToFile()

Try(main)
