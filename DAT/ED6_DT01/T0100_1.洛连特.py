from ED6ScenarioHelper import *

def main():
    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0100.x',
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

    ScpFunction(
        "Function_0_64",           # 00, 0
        "Function_1_FA9",          # 01, 1
        "Function_2_198D",         # 02, 2
        "Function_3_1EF2",         # 03, 3
        "Function_4_2DB0",         # 04, 4
        "Function_5_32EC",         # 05, 5
        "Function_6_3311",         # 06, 6
        "Function_7_332A",         # 07, 7
        "Function_8_3343",         # 08, 8
        "Function_9_339F",         # 09, 9
        "Function_10_33E9",        # 0A, 10
        "Function_11_36CF",        # 0B, 11
        "Function_12_395B",        # 0C, 12
        "Function_13_3983",        # 0D, 13
        "Function_14_398D",        # 0E, 14
        "Function_15_39B2",        # 0F, 15
        "Function_16_39DE",        # 10, 16
        "Function_17_3A0A",        # 11, 17
        "Function_18_3A26",        # 12, 18
        "Function_19_3A42",        # 13, 19
        "Function_20_3C6C",        # 14, 20
        "Function_21_3C7E",        # 15, 21
        "Function_22_3CCA",        # 16, 22
        "Function_23_3CEF",        # 17, 23
        "Function_24_3D1B",        # 18, 24
        "Function_25_3D47",        # 19, 25
        "Function_26_3F72",        # 1A, 26
        "Function_27_3F84",        # 1B, 27
        "Function_28_3FD0",        # 1C, 28
        "Function_29_4007",        # 1D, 29
        "Function_30_4020",        # 1E, 30
        "Function_31_402F",        # 1F, 31
        "Function_32_4291",        # 20, 32
        "Function_33_42A3",        # 21, 33
        "Function_34_42CE",        # 22, 34
        "Function_35_42F0",        # 23, 35
    )


    def Function_0_64(): pass

    label("Function_0_64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_176")
    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "之前真是多谢了。\x01",
            "真的是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这里明明是空港城市，\x01",
            "还能坚持卖这些小玩意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我嘛，觉得这样正好哦。\x01",
            "老妈也真是反应迟钝。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_170")

    label("loc_10C")


    ChrTalk(
        0xFE,
        (
            "这里明明是空港城市，\x01",
            "还能坚持卖这些小玩意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我嘛，觉得这样正好哦。\x01",
            "老妈也真是反应迟钝。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_170")

    TalkEnd(0x12)
    Jump("loc_FA8")

    label("loc_176")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x325)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AB1")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 31400, 0, 29390, 120)
    SetChrPos(0x102, 30330, 0, 28560, 120)
    OP_4A(0x12, 255)
    OP_6D(31410, 0, 29350, 0)
    OP_6C(0, 0)
    OP_0D()
    Sleep(400)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x12,
        "啊…………！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……那块石头。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F难道……\x02\x03",
            "这就是你刚才在找的石头？\x02",
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
            "交出了\x07\x02",
            "结晶回路的碎片\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x12,
        (
            "啊，就是它没错。\x01",
            "我美丽的石头……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(400)

    ChrTalk(
        0x12,
        "……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x12)

    ChrTalk(
        0x12,
        (
            "……怎么回事，\x01",
            "怎么弄得这么脏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F喂喂，\x01",
            "发牢骚也要在表示过谢意之后吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "啊，知道啦。\x01",
            "你们是游击士对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "我可是向游击士协会\x01",
            "付过酬金的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "这下我总该有\x01",
            "发牢骚的权利了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#005F问题的关键根本不在这～里！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#017F艾丝蒂尔，冷静点，\x01",
            "对方只是个孩子而已。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#009F哼，知道啦。\x02",
    )

    CloseMessageWindow()

    def lambda_44B():
        TurnDirection(0x102, 0x12, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44B)
    Sleep(200)
    TurnDirection(0x101, 0x12, 400)

    ChrTalk(
        0x102,
        (
            "#010F你在找的就是\x01",
            "这块结晶回路的碎片吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊，没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "……这块石头，\x01",
            "是结晶回路？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "装在导力器里面的\x01",
            "那种结晶回路？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F嗯，\x01",
            "这的确就是用耀晶片制成的结晶回路。\x02\x03",
            "因为已经碎了，\x01",
            "所以也没什么能量了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 45, 400)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(400)

    ChrTalk(
        0x12,
        (
            "这块石头，\x01",
            "果然是结晶回路啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F？？？\x02\x03",
            "怎么回事呢？\x01",
            "干嘛站在那里发呆？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(
        0x12,
        "……嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "啊，没什么，没事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "不管怎样，\x01",
            "谢谢你们帮我找东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "那就这样吧。\x02",
    )

    CloseMessageWindow()

    def lambda_679():

        label("loc_679")

        TurnDirection(0x101, 0x12, 400)
        OP_48()
        Jump("loc_679")

    QueueWorkItem2(0x101, 1, lambda_679)

    def lambda_68A():

        label("loc_68A")

        TurnDirection(0x102, 0x12, 400)
        OP_48()
        Jump("loc_68A")

    QueueWorkItem2(0x102, 1, lambda_68A)
    OP_8E(0xFE, 0x7D5A, 0x0, 0x5E1A, 0x1388, 0x0)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x12,
        "啊，对了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x7A12, 0x0, 0x7080, 0x1388, 0x0)

    ChrTalk(
        0x12,
        (
            "……差点忘了，\x01",
            "这东西就给你吧。\x02",
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
            "得到了５个\x07\x02",
            "肉馅丸子\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x1A5, 5)

    ChrTalk(
        0x12,
        (
            "这些肉丸子对身体很有好处，\x01",
            "是老妈刚才给我的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "不过味道有些苦，\x01",
            "我不喜欢吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "总之，今天还真是谢谢你们啦。\x02",
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0x7D8C, 0x0, 0x46AA, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)

    ChrTalk(
        0x101,
        (
            "#007F呼～～\x01",
            "真是个傲慢的小孩啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F一定是因为正值年少气盛吧。\x02\x03",
            "#010F可是，那个孩子……\x02\x03",
            "为什么要寻找\x01",
            "结晶回路这样的东西呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F…………嗯？\x02\x03",
            "这么说来，\x01",
            "的确有点不可思议……\x02\x03",
            "#001F哎呀，管他呢。\x01",
            "每个人喜欢的东西都不一样嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#019F哈哈，说得也是。\x02\x03",
            "说不定那个孩子\x01",
            "对结晶回路非常有兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯～\x01",
            "真不知道那种复杂的机械有什么好。\x02\x03",
            "真是个让我无法理解的世界啊～\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不过，从现在开始\x01",
            "你也要主动去了解才行啊。\x02\x03",
            "如果不能把结晶回路运用自如，\x01",
            "是不能胜任游击士这个工作的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#007F好～啦，我加把劲就是了。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x12, 62400, 250, 22000, 270)
    OP_3F(0x325, 1)
    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x1, 0x40)
    OP_44(0x12, 0xFF)
    OP_43(0x12, 0x0, 0x0, 0x8)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找发光的石头】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x0)
    Jump("loc_FA8")

    label("loc_AB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_B34")
    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "如果你们找到发光石头的话，\x01",
            "赶快来告诉我。应该就在这附近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "杂货店这边也找过了，\x01",
            "……接下来该找哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Jump("loc_FA8")

    label("loc_B34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_E9F")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 31400, 0, 29390, 120)
    SetChrPos(0x102, 30690, 0, 29150, 133)
    OP_4A(0x12, 255)
    OP_6D(31410, 0, 29350, 0)
    OP_6C(0, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x12,
        "真是奇怪啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……到底掉到哪儿去了呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x12, 0x101, 400)
    Sleep(400)

    ChrTalk(
        0x12,
        "啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "……喂喂，\x01",
            "我有点事想问你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "在这附近看到过\x01",
            "一块漂亮的石头吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    ChrTalk(
        0x101,
        (
            "#004F啊？\x02\x03",
            "漂亮的石头？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "对呀，漂亮的石头，\x01",
            "闪闪发光的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "那样的石头\x01",
            "会掉到哪儿去呢？ \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F是弄丢的东西吗？\x02\x03",
            "#505F嗯～\x01",
            "我们好像也没看到。\x02\x03",
            "大概掉在什么位置呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "刚才老妈叫我，\x01",
            "我就到杂货铺去了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "一开始石头还在手里的，\x01",
            "回头的时候就不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F杂货铺是里农老板开的那间吧。\x01",
            "　\x02\x03",
            "你在杂货铺的门口仔细找过了吗？\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "还用你说！\x01",
            "不要把我当成小孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎呀，好傲慢的小子～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "还好已经委托游击士了，\x01",
            "相信很快就能找到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "如果你们找到发光石头的话，\x01",
            "一定要赶快来告诉我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "我想应该就在这附近。\x02",
    )

    CloseMessageWindow()
    OP_28(0x4, 0x4, 0x4)
    OP_28(0x4, 0x4, 0x8)
    OP_28(0x4, 0x1, 0x1)
    OP_28(0x4, 0x1, 0x2)
    OP_65(0x1, 0x1)
    OP_4B(0x12, 255)
    OP_8C(0x12, 45, 0)
    EventEnd(0x0)
    Jump("loc_FA8")

    label("loc_E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_F44")
    SetChrFlags(0x12, 0x10)
    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF9")

    ChrTalk(
        0xFE,
        (
            "可恶，\x01",
            "到哪里去了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "有可能的地方\x01",
            "已经全找过了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3C")

    label("loc_EF9")


    ChrTalk(
        0xFE,
        (
            "真是奇怪啊……\x01",
            "为什么会找不到呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "啊，到底掉到哪儿去了。\x02",
    )

    CloseMessageWindow()

    label("loc_F3C")

    ClearChrFlags(0x12, 0x10)
    Jump("loc_FA5")

    label("loc_F44")

    SetChrFlags(0x12, 0x10)
    TalkBegin(0x12)

    ChrTalk(
        0xFE,
        (
            "啊～\x01",
            "这附近有各种各样的破烂啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽说都是些有趣的东西，\x01",
            "不过通通都不值钱。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)

    label("loc_FA5")

    TalkEnd(0x12)

    label("loc_FA8")

    Return()

    # Function_0_64 end

    def Function_1_FA9(): pass

    label("Function_1_FA9")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1064")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102C")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        (
            "这里明明是空港城市，\x01",
            "还能坚持卖这些小玩意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "老妈反应这么迟钝，真是可叹啊。\x01",
            "哎呀，我说真的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1061")

    label("loc_102C")


    ChrTalk(
        0xFE,
        (
            "老妈反应这么迟钝，真是可叹啊。\x01",
            "哎呀，我说真的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1061")

    Jump("loc_1989")

    label("loc_1064")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x325)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_10EE")
    TurnDirection(0xFE, 0x101, 0)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        "啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……喂，那个。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(
        0x101,
        (
            "#000F是这个吗？\x01",
            "你要找的齿轮。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F3")

    label("loc_10EE")


    ChrTalk(
        0xFE,
        "喂喂，我有点事想问你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "在这附近看到过一个齿轮吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(
        0x101,
        "#000F啊？齿轮？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "对啊。\x01",
            "闪着金属光泽的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "会掉到哪儿去呢？ \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还好已经委托游击士了，\x01",
            "相信很快就能找到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，说起来。\x02\x03",
            "#000F难道是这个？\x01",
            "你要找的齿轮。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F3")

    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x1, 0x4)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了\x07\x02",
            "齿轮\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x325, 1)

    ChrTalk(
        0xFE,
        "啊，就是它没错。我的齿轮……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……怎么回事，怎么弄得这么脏啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F喂喂，\x01",
            "发牢骚也要在表示过谢意之后吧。\x02\x03",
            "#000F这可是我们特地从\x01",
            "排水沟里帮你捞上来的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可是向游击士协会\x01",
            "付过酬金的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这下我总该有发牢骚的权利了吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        "#002F#5S问题的关键根本不在这～里！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……不管怎样，\x01",
            "谢谢你们帮我找东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那就这样吧。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x40)
    OP_43(0x101, 0x0, 0x1, 0x6)
    OP_43(0x102, 0x0, 0x1, 0x7)
    OP_43(0x12, 0x0, 0x1, 0x5)
    OP_A2(0x11)
    OP_A2(0xE)
    OP_A2(0xF)
    OP_A5(0x11)
    OP_A5(0xE)
    OP_A5(0xF)
    SetChrPos(0x12, 62400, 250, 22000, 270)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0xFE, 0x80)
    OP_85(0x12)
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#002F呼～～真是个傲慢的小孩啊～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010F艾丝蒂尔，冷静一点。\x01",
            " \x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        "#000F我、我知道啦。\x02",
    )

    CloseMessageWindow()
    OP_8B(0x102, 0x10ACC, 0x9858, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#010F可是，那个孩子……\x02\x03",
            "#010F为什么要找齿轮这样的东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F……啊？\x02\x03",
            "#000F嗯，\x01",
            "听你这么一说，的确有点不可思议……\x02\x03",
            "#000F哎呀，管他呢。\x01",
            "每个人喜欢的东西都不一样嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#010F哈哈，说得也是。\x02\x03",
            "#010F……那，\x01",
            "那么我们也走吧。\x02\x03",
            "#010F还得回协会\x01",
            "报告一下情况呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_30(0x0)
    EventEnd(0x0)
    Jump("loc_1989")

    label("loc_15EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_18B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_166B")

    ChrTalk(
        0xFE,
        (
            "如果你们找到齿轮的话，\x01",
            "赶快来告诉我。应该就在这附近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……杂货店这边也找过了，\x01",
            "接下来该找哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B5")

    label("loc_166B")

    OP_28(0x4, 0x4, 0x4)
    OP_28(0x4, 0x4, 0x8)
    OP_28(0x4, 0x1, 0x1)
    OP_28(0x4, 0x4, 0x2)

    ChrTalk(
        0xFE,
        (
            "喂喂，我有点事想问你们。\x01",
            "在这附近看到过一个齿轮吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 0)

    ChrTalk(
        0x101,
        "#000F啊？齿轮？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "对啊。\x01",
            "闪着金属光泽的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "会掉到哪儿去呢？ \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F弄丢了？\x01",
            "嗯～我们好像也没看到。\x02\x03",
            "#000F大概掉在什么位置呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "刚才老妈叫我，\x01",
            "我就到杂货铺去了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "一开始石头还在手里的，\x01",
            "回头的时候就不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那应该就很可能掉在店前面了。\x01",
            "你已经找过了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还用你说！\x01",
            "不要把我当成小孩子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#002F哎呀，好傲慢的小子～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "还好已经委托游击士了，\x01",
            "相信很快就能找到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "要是找到了，赶快来告诉我。\x01",
            "我想应该就在这附近。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B5")

    Jump("loc_1989")

    label("loc_18B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193C")
    OP_A2(0x10)

    ChrTalk(
        0xFE,
        "……飞艇这东西真不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我来的时候也坐过，\x01",
            "又大又舒服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的经验告诉我，\x01",
            "这东西肯定是由导力器驱动的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1989")

    label("loc_193C")


    ChrTalk(
        0xFE,
        "不错嘛，飞艇这玩意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我的经验告诉我，\x01",
            "这东西肯定是由导力器驱动的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1989")

    TalkEnd(0x12)
    Return()

    # Function_1_FA9 end

    def Function_2_198D(): pass

    label("Function_2_198D")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1DCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_END)), "loc_1A36")
    TurnDirection(0x13, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "没办法，再在这里呆一阵\x01",
            "就上格兰赛尔去试试吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家那傻小子\x01",
            "真是一点用都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "才刚帮了一会儿忙\x01",
            "又不知道跑到哪儿去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 0)
    Jump("loc_1DCB")

    label("loc_1A36")

    OP_A2(0x280)

    ChrTalk(
        0xFE,
        "哈啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "特地大老远跑来这里，\x01",
            "真是白折腾一场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "又没有顾客，\x01",
            "商店也比想象中的破旧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "乡下果然\x01",
            "就是乡下啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(200)

    ChrTalk(
        0x101,
        "#009F（哼。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "……嗯？\x01",
            "你们是谁？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "算了，不管是谁，\x01",
            "我给你们打折，随便买点什么吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这个木雕小工艺品怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这么精细的工艺，\x01",
            "只有在卡尔瓦德才买得到哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F卡尔瓦德，嗯～\x01",
            "是我们的邻国吗……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F卡尔瓦德共和国是\x01",
            "利贝尔王国东面的国家哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#008F这、这我当然知道啦。\x02",
    )

    CloseMessageWindow()

    def lambda_1C33():
        TurnDirection(0x102, 0x13, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C33)
    TurnDirection(0x101, 0x13, 400)

    ChrTalk(
        0x102,
        (
            "#010F但是，卡尔瓦德的民间工艺品吗……\x02\x03",
            "我想要是在王都摆卖的话，\x01",
            "一定会更受欢迎的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 400)

    ChrTalk(
        0xFE,
        (
            "哈啊……\x01",
            "果然是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我本来以为稍微乡下点的地方会更好卖，\x01",
            "但这里也实在有点乡下过头了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(200)

    ChrTalk(
        0x101,
        "#009F（哼哼。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "没办法，再在这里呆一阵\x01",
            "就上格兰赛尔去试试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……话说回来，\x01",
            "我家的卡雷尔在做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "才刚帮了一会儿忙\x01",
            "又在到处乱转了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 0)

    label("loc_1DCB")

    Jump("loc_1EEE")

    label("loc_1DCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7E")
    OP_A2(0x19)

    ChrTalk(
        0xFE,
        (
            "这里虽然是个小的城镇，\x01",
            "不过商店里东西的品种还是不少哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "托导力器的福， \x01",
            "利贝尔王国和以前大不相同了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，明天要更加努力才行，\x01",
            "销售额可不能降低呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEE")

    label("loc_1E7E")


    ChrTalk(
        0xFE,
        (
            "这里虽然是个小的城镇，\x01",
            "不过商店里东西的品种还是不少哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "呼，明天要更加努力才行，\x01",
            "销售额可不能降低呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EEE")

    TalkEnd(0x13)
    Return()

    # Function_2_198D end

    def Function_3_1EF2(): pass

    label("Function_3_1EF2")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1F5A")

    ChrTalk(
        0xFE,
        (
            "唔～～啊，\x01",
            "今天天气依旧很暖和啊～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "睡个午觉\x01",
            "一定很舒服呢～～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA7")

    label("loc_1F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_20A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_1FC7")
    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(
        0xFE,
        "…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔呀唔呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "……咕噜咕噜咕噜咕噜。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_20A4")

    label("loc_1FC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_204C")
    OP_28(0x9, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#004F（啊……！）\x02\x03",
            "（小猫回来了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔呀唔呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……咕噜咕噜咕噜咕噜。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_20A4")

    label("loc_204C")

    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(
        0xFE,
        "…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔呀唔呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "……咕噜咕噜咕噜咕噜。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)

    label("loc_20A4")

    Jump("loc_2DA7")

    label("loc_20A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2342")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_21AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2154")
    OP_A2(0x12)
    ClearChrFlags(0x14, 0x10)

    ChrTalk(
        0xFE,
        (
            "哎呀～～\x01",
            "这不是尤基士君吗～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦呵呵～㈱\x01",
            "要不要和阿姨一起来午睡呢～～？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x102,
        "#018F……还是免了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21AB")

    label("loc_2154")

    ClearChrFlags(0x14, 0x10)

    ChrTalk(
        0xFE,
        (
            "哎呀～～\x01",
            "这不是尤基士君吗～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哦呵呵～㈱\x01",
            "要不要和阿姨一起来午睡呢～～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AB")

    Jump("loc_233F")

    label("loc_21AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2213")

    ChrTalk(
        0xFE,
        (
            "尤基士君～\x01",
            "不好意思呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小安莉尔\x01",
            "自己回我这里来了哦～～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_233F")

    label("loc_2213")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22DC")
    OP_28(0x9, 0x1, 0x8000)

    ChrTalk(
        0x101,
        (
            "#004F啊……！\x02\x03",
            "猫也会自己回家？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎哟哟～～\x01",
            "这不是尤基士君吗～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小安莉尔\x01",
            "自己回我这里来了哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔～～啊，\x01",
            "多么可爱伶俐的小乖乖啊～～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_233F")

    label("loc_22DC")


    ChrTalk(
        0xFE,
        (
            "真是的～～\x01",
            "那个小安莉尔\x01",
            "到底去了哪儿呢～～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我真的是好担心呢～～\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～呼。\x02",
    )

    CloseMessageWindow()

    label("loc_233F")

    Jump("loc_2DA7")

    label("loc_2342")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23A6")

    ChrTalk(
        0xFE,
        (
            "已经中午了， \x01",
            "我要好好地睡上顿午觉～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "喂～～小安莉尔～～㈱\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA7")

    label("loc_23A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_251C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249D")
    OP_A2(0x12)
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(
        0xFE,
        "找到小安莉尔了吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯！找到了。\x02\x03",
            "#007F……但是又被它给跑掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀，怎么会这样呢～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "奇怪了啊～\x01",
            "它本来不是很怕陌生人的啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿姨会一直在这里等着的，\x01",
            "拜托了啊，尤基士君。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2519")

    label("loc_249D")

    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "真是奇怪啊，怎么会逃跑呢～？\x01",
            "它本来不是很怕陌生人的啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿姨会一直在这里等着的，\x01",
            "拜托了啊，尤基士君。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2519")

    Jump("loc_2DA7")

    label("loc_251C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2CA3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C48")
    OP_28(0x9, 0x4, 0x4)
    OP_28(0x9, 0x4, 0x8)
    OP_28(0x9, 0x4, 0x2)
    OP_28(0x9, 0x1, 0x1)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(36950, 0, 57050, 0)
    OP_6C(0, 0)
    SetChrPos(0x101, 38560, 0, 57230, 270)
    SetChrPos(0x102, 37800, 0, 58080, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25B9")
    SetChrPos(0x2, 39290, 0, 58080, 211)
    SetChrPos(0x3, 40280, 0, 58050, 212)
    Jump("loc_25D8")

    label("loc_25B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D8")
    SetChrPos(0x2, 39290, 0, 58080, 211)

    label("loc_25D8")

    OP_0D()
    Sleep(100)

    ChrTalk(
        0xFE,
        (
            "真是的～\x01",
            "究竟跑到哪儿去了呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唉～～\x01",
            "不知道尤基士看到委托了没有～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F阿姨，您在等游击士吗？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(
        0xFE,
        "嗯，是啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～～？\x01",
            "难道你就是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯⊙我就是游击士。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 0)

    ChrTalk(
        0xFE,
        "难道～那边那位也是～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x14, 0)

    ChrTalk(
        0x102,
        "#010F嗯，我也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀呀，阿姨真的很高兴啊～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近叫做尤基士的人\x01",
            "好像很多呢～～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#501F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "哎呀，你们好像是姐弟嘛～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "对呀，对呀～～\x01",
            "有相同的名字的一般就是一家人的嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯……\x01",
            "可以说是姐弟没错啦……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(
        0x102,
        (
            "#014F（……艾丝蒂尔，\x01",
            "　这位阿姨好像不知道什么是游击士啊。）\x02\x03",
            "#014F（她好像把游击士这个词的读音\x01",
            "　当作人的名字了啊。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F（…………不、不会吧～）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎呀～～你们两个\x01",
            "在唧唧喳喳的说些什么呢～～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F（有些麻烦啊，只有顺着她的话说了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#506F（……知道～了。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x14, 400)
    Sleep(200)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(
        0x102,
        (
            "#010F是这样，\x01",
            "您有什么困难吗……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 0)

    ChrTalk(
        0xFE,
        (
            "哎呀～这孩子看上去这么可爱，\x01",
            "没想到洞察力这么敏锐呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "男孩子果然就是用心啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#509F……阿姨，您到底有没有困难？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "啊，对了对了。\x01",
            "说实话啊～\x01",
            "我真的好苦恼的哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我家的小安莉尔\x01",
            "到现在还没有回来啊～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我只不过在茶座小睡了一觉，\x01",
            "就那么一不留神，它就不见了～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F小安莉尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "是小猫呀～\x01",
            "好可爱的小猫呢～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且不仅是外表可爱，\x01",
            "内心也好温顺的哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F是什么颜色的小猫呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "嗯～让我想想啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好像在秋天的夕阳中\x01",
            "那种小麦田的颜色哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F……小麦色，对吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "它可能正在外面到处乱跑呢，\x01",
            "拜托你们帮我把它捉回来好吗～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我明白了，\x01",
            "首先从茶座周围开始找吧。\x02\x03",
            "#010F一旦找到了，\x01",
            "我们就会回来告诉您的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "阿姨就在这里\x01",
            "等着你们哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托了啊，尤基士君。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_2CA0")

    label("loc_2C48")

    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "阿姨就在这里\x01",
            "等着你们哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "小安莉尔就拜托你们去找了啊，\x01",
            "尤基士君。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA0")

    Jump("loc_2DA7")

    label("loc_2CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2CE5")

    ChrTalk(
        0xFE,
        "哎～～真是不省心的孩子～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "是不是在哪儿睡觉呢～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA7")

    label("loc_2CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2D47")
    OP_62(0x14, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(500)

    ChrTalk(
        0xFE,
        "…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……唔呀唔呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "……咕噜咕噜咕噜咕噜。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14)
    Jump("loc_2DA7")

    label("loc_2D47")


    ChrTalk(
        0xFE,
        (
            "嗯呼呼呼，\x01",
            "今天天气很暖和哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "可以睡上美美的一觉了～～\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵喵喵～～～咪咪。\x02",
    )

    CloseMessageWindow()

    label("loc_2DA7")

    TalkEnd(0x14)
    SetChrFlags(0x14, 0x10)
    Return()

    # Function_3_1EF2 end

    def Function_4_2DB0(): pass

    label("Function_4_2DB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_2DBC")
    Return()

    label("loc_2DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2ECC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E40")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F如果想要弄清是什么掉下去的话，\x01",
            "就去地下水路调查一下吧？\x02\x03",
            "地下水路的入口在教堂的后面。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC6")

    label("loc_2E40")


    ChrTalk(
        0x101,
        (
            "#505F唔……\x01",
            "什么东西掉下去了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F如果想要弄清楚的话，\x01",
            "我们就去下面调查一下吧？\x02\x03",
            "地下水路的入口在教堂的后面。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC6")

    TalkEnd(0xFF)
    Jump("loc_32EB")

    label("loc_2ECC")

    OP_28(0x4, 0x1, 0x4)
    OP_28(0x4, 0x1, 0x8)
    OP_28(0x4, 0x1, 0x10)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x0, 46120, 0, 26090, 225)
    SetChrPos(0x1, 45540, 0, 27200, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F28")
    OP_6C(350000, 0)
    Jump("loc_2F49")

    label("loc_2F28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F49")
    OP_6C(350000, 0)
    Jump("loc_2F49")

    label("loc_2F49")

    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3072")
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        "#004F……哎？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F那是什么……\x01",
            "排水沟里面好像有东西在发光。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xB176, 0x0, 0x67AC, 0x7D0, 0x0)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 45050, 200, 25150, 0, 0, 0, 200, 400, 200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#014F………果然。\x02\x03",
            "好像有东西落到排水沟的沟底了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C7")

    label("loc_3072")

    Sleep(400)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x102,
        "#014F……嗯？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x0, 0)

    ChrTalk(
        0x101,
        "#000F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F那是什么……\x01",
            "排水沟里面好像有东西在发光。\x02",
        )
    )

    CloseMessageWindow()
    OP_8B(0x101, 0xB176, 0x67AC, 0x190)

    ChrTalk(
        0x101,
        "#000F哪里哪里？\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xB176, 0x0, 0x67AC, 0x7D0, 0x0)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 45050, 200, 25150, 0, 0, 0, 200, 400, 200, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#004F啊，是真的。\x01",
            "还在闪闪发光呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F好像有东西落到排水沟的沟底了。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C7")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#505F排水沟的沟底？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#015F你忘记了城里的地下有什么了吗？\x01",
            "　\x02\x03",
            "不久之前我们才去过的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#508F啊，对呀！是地下水路。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F在实地研修时下去过的。\x02\x03",
            "地下水路的入口在教堂的后面。\x01",
            "　\x02\x03",
            "如果想要弄清楚的话，\x01",
            "我们就去下面调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_65(0x2, 0x1)
    OP_82(0x0, 0x0)
    OP_84(0x0)
    EventEnd(0x0)

    label("loc_32EB")

    Return()

    # Function_4_2DB0 end

    def Function_5_32EC(): pass

    label("Function_5_32EC")

    SetChrFlags(0x12, 0x40)
    OP_A6(0x11)
    OP_8E(0xFE, 0x10ACC, 0x0, 0x9858, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x11)
    Return()

    # Function_5_32EC end

    def Function_6_3311(): pass

    label("Function_6_3311")

    OP_A6(0xE)

    label("loc_3314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_3326")
    TurnDirection(0xFE, 0x12, 0)
    OP_48()
    Jump("loc_3314")

    label("loc_3326")

    OP_A3(0xE)
    Return()

    # Function_6_3311 end

    def Function_7_332A(): pass

    label("Function_7_332A")

    OP_A6(0xF)

    label("loc_332D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_333F")
    TurnDirection(0xFE, 0x12, 0)
    OP_48()
    Jump("loc_332D")

    label("loc_333F")

    OP_A3(0xF)
    Return()

    # Function_7_332A end

    def Function_8_3343(): pass

    label("Function_8_3343")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "进入地下水路\x01",      # 0
            "离开\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3387"),
        (1, "loc_3393"),
        (SWITCH_DEFAULT, "loc_3399"),
    )


    label("loc_3387")

    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_3399")

    label("loc_3393")

    TalkEnd(0xFF)
    Jump("loc_3399")

    label("loc_3399")

    Sleep(30)
    Return()

    # Function_8_3343 end

    def Function_9_339F(): pass

    label("Function_9_339F")

    FadeToBright(500, 0)
    OP_6D(76970, 0, 20370, 0)
    SetChrPos(0x101, 76970, 0, 20370, 180)
    SetChrPos(0x102, 76970, 0, 20370, 0)
    OP_30(0x0)
    OP_0D()
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    Return()

    # Function_9_339F end

    def Function_10_33E9(): pass

    label("Function_10_33E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_33F6")
    Jump("loc_36CE")

    label("loc_33F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36CE")
    OP_28(0x9, 0x1, 0x2)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x16, 58830, 0, 40470, 165)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x40)
    OP_6D(59150, 0, 42330, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 59390, 0, 55350, 176)
    SetChrPos(0x102, 57010, 0, 55120, 164)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34A0")
    SetChrPos(0x2, 59390, 0, 57350, 176)
    SetChrPos(0x3, 57010, 0, 57120, 164)
    Jump("loc_34BF")

    label("loc_34A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34BF")
    SetChrPos(0x2, 59390, 0, 57350, 176)

    label("loc_34BF")

    OP_0D()

    def lambda_34C6():
        OP_6C(180000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_34C6)

    def lambda_34D6():
        OP_6D(58950, 0, 46580, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_34D6)
    OP_8E(0x16, 0xE63C, 0x0, 0xB63A, 0x7D0, 0x0)
    OP_8E(0x101, 0xE61E, 0x0, 0xCC6A, 0x1770, 0x0)

    ChrTalk(
        0x101,
        "#004F啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    def lambda_355B():
        OP_8E(0x101, 0xE95C, 0x0, 0xAB18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_355B)

    def lambda_3576():
        OP_8E(0x102, 0xE48E, 0x0, 0xB450, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3576)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35D2")

    def lambda_359F():
        OP_8E(0x2, 0xE75E, 0x0, 0xBF5E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_359F)

    def lambda_35BA():
        OP_8E(0x3, 0xE394, 0x0, 0xBD56, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_35BA)
    Jump("loc_35FB")

    label("loc_35D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35FB")

    def lambda_35E6():
        OP_8E(0x2, 0xE75E, 0x0, 0xBF5E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_35E6)

    label("loc_35FB")

    OP_8E(0x16, 0xE6C8, 0x0, 0xAD16, 0x1770, 0x0)

    def lambda_3615():
        OP_6D(59770, 0, 44910, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3615)
    OP_8E(0x16, 0xF082, 0x0, 0x95BA, 0x1770, 0x0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x40)
    WaitChrThread(0x0, 0x3)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#002F约修亚，刚才那只小猫……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F似乎就是那位阿姨要找的小猫呢。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F绝对错不了啦，\x01",
            "快追上它！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_36CE")

    label("loc_36CE")

    Return()

    # Function_10_33E9 end

    def Function_11_36CF(): pass

    label("Function_11_36CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_36DC")
    Jump("loc_395A")

    label("loc_36DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_395A")
    OP_28(0x9, 0x1, 0x2)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x16, 48900, 0, 84200, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    OP_43(0x16, 0x0, 0x1, 0xC)
    OP_43(0x16, 0x1, 0x1, 0xD)
    Fade(1000)
    SetChrPos(0x2, 47800, 0, 50200, 0)
    SetChrPos(0x3, 46800, 0, 50200, 0)
    Sleep(2000)
    SetChrPos(0x0, 48800, 0, 50200, 0)
    SetChrPos(0x1, 48800, 0, 50200, 0)
    OP_62(0x16, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_8E(0x16, 0xBFCC, 0x0, 0x116E8, 0xBB8, 0x0)
    OP_63(0x16)
    Sleep(500)
    SetChrPos(0x0, 48800, 0, 59200, 0)
    SetChrPos(0x1, 48800, 0, 59200, 0)

    ChrTalk(
        0x101,
        "#004F啊！\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)
    OP_43(0x101, 0x0, 0x1, 0xF)
    OP_43(0x102, 0x0, 0x1, 0x10)
    OP_43(0x16, 0x0, 0x1, 0xE)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A2(0x14)
    OP_A5(0x15)
    OP_A5(0x13)
    OP_A5(0x14)
    SetChrPos(0x16, 5488, 0, 16806, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8)

    ChrTalk(
        0x101,
        "#002F约修亚，刚才那只小猫……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F好像是刚才说的那只小猫。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F绝对错不了啦，\x01",
            "快追上它！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x2, 48800, 0, 62200, 0)
    SetChrPos(0x3, 48800, 0, 61200, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3916")
    OP_43(0x10F, 0x0, 0x1, 0x11)
    OP_43(0x110, 0x0, 0x1, 0x12)
    OP_A2(0x17)
    OP_A2(0x16)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_A5(0x16)
    OP_A5(0x17)
    Jump("loc_3949")

    label("loc_3916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_393B")
    OP_43(0x10F, 0x0, 0x1, 0x11)
    OP_A2(0x16)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    OP_A5(0x16)
    Jump("loc_3949")

    label("loc_393B")

    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)

    label("loc_3949")

    OP_30(0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x1)
    Jump("loc_395A")

    label("loc_395A")

    Return()

    # Function_11_36CF end

    def Function_12_395B(): pass

    label("Function_12_395B")

    OP_6D(49100, 0, 76400, 3000)
    Sleep(500)
    OP_6D(49100, 0, 70400, 2500)
    Return()

    # Function_12_395B end

    def Function_13_3983(): pass

    label("Function_13_3983")

    OP_6C(0, 3000)
    Return()

    # Function_13_3983 end

    def Function_14_398D(): pass

    label("Function_14_398D")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_8E(0x16, 0xE420, 0x0, 0x11170, 0x1B58, 0x0)
    SetChrFlags(0x16, 0x80)
    OP_A3(0x15)
    Return()

    # Function_14_398D end

    def Function_15_39B2(): pass

    label("Function_15_39B2")

    OP_A6(0x13)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xC094, 0x0, 0x10108, 0x1B58, 0x0)
    OP_8C(0x101, 45, 0)
    ClearChrFlags(0x101, 0x40)
    OP_A3(0x13)
    Return()

    # Function_15_39B2 end

    def Function_16_39DE(): pass

    label("Function_16_39DE")

    OP_A6(0x14)
    SetChrFlags(0x102, 0x40)
    OP_8E(0x102, 0xBBE4, 0x0, 0xFE4B, 0xBB8, 0x0)
    OP_8C(0x102, 45, 0)
    ClearChrFlags(0x102, 0x40)
    OP_A3(0x14)
    Return()

    # Function_16_39DE end

    def Function_17_3A0A(): pass

    label("Function_17_3A0A")

    SetChrFlags(0x10F, 0x40)
    OP_92(0x10F, 0x0, 0x0, 0xBB8, 0x0)
    ClearChrFlags(0x10F, 0x40)
    OP_A3(0x16)
    Return()

    # Function_17_3A0A end

    def Function_18_3A26(): pass

    label("Function_18_3A26")

    SetChrFlags(0x110, 0x40)
    OP_92(0x110, 0x0, 0x0, 0xBB8, 0x0)
    ClearChrFlags(0x110, 0x40)
    OP_A3(0x17)
    Return()

    # Function_18_3A26 end

    def Function_19_3A42(): pass

    label("Function_19_3A42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_3A4F")
    Jump("loc_3C6B")

    label("loc_3A4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C6B")
    OP_28(0x9, 0x1, 0x4)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x16, 60700, 0, 14400, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    Fade(1000)
    OP_43(0x16, 0x0, 0x1, 0x14)
    OP_43(0x16, 0x1, 0x1, 0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AD6")
    SetChrPos(0x2, 47400, 0, 50200, 0)
    SetChrPos(0x3, 46400, 0, 50200, 0)
    Jump("loc_3AF5")

    label("loc_3AD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF5")
    SetChrPos(0x2, 47400, 0, 50200, 0)

    label("loc_3AF5")

    OP_8E(0x16, 0xC5A8, 0x0, 0x3840, 0xBB8, 0x0)
    OP_8E(0x16, 0xBDD8, 0x0, 0x3DB8, 0xBB8, 0x0)
    SetChrPos(0x0, 48800, 0, 29600, 0)
    SetChrPos(0x1, 48800, 0, 29600, 0)

    ChrTalk(
        0x101,
        "#004F呀！是那只小猫！\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8E(0x16, 0xBDD8, 0x0, 0x3E80, 0xBB8, 0x0)
    Sleep(500)
    OP_63(0x16)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    ChrTalk(
        0x101,
        "#005F你给我站住～～！\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x1, 0x17)
    OP_43(0x102, 0x0, 0x1, 0x18)
    OP_43(0x16, 0x0, 0x1, 0x16)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A2(0x14)
    OP_A5(0x15)
    OP_A5(0x13)
    OP_A5(0x14)
    SetChrPos(0x16, 5488, 0, 16806, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8)

    ChrTalk(
        0x102,
        (
            "#017F呼～\x01",
            "怎么感觉和帕赛尔农场的情形差不多……\x02\x03",
            "#017F为什么最近总是在追过来赶过去的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x1)
    Jump("loc_3C6B")

    label("loc_3C6B")

    Return()

    # Function_19_3A42 end

    def Function_20_3C6C(): pass

    label("Function_20_3C6C")

    OP_6D(48800, 0, 16800, 3000)
    Return()

    # Function_20_3C6C end

    def Function_21_3C7E(): pass

    label("Function_21_3C7E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9F")
    OP_6C(0, 3000)
    Jump("loc_3CC9")

    label("loc_3C9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CC0")
    OP_6C(0, 3000)
    Jump("loc_3CC9")

    label("loc_3CC0")

    OP_6C(180000, 3000)

    label("loc_3CC9")

    Return()

    # Function_21_3C7E end

    def Function_22_3CCA(): pass

    label("Function_22_3CCA")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_8E(0x16, 0xD994, 0x0, 0x3840, 0x1B58, 0x0)
    SetChrFlags(0x16, 0x80)
    OP_A3(0x15)
    Return()

    # Function_22_3CCA end

    def Function_23_3CEF(): pass

    label("Function_23_3CEF")

    OP_A6(0x13)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0xBC48, 0x0, 0x4E84, 0x1B58, 0x0)
    OP_8C(0x101, 135, 0)
    ClearChrFlags(0x101, 0x40)
    OP_A3(0x13)
    Return()

    # Function_23_3CEF end

    def Function_24_3D1B(): pass

    label("Function_24_3D1B")

    OP_A6(0x14)
    SetChrFlags(0x102, 0x40)
    OP_8E(0x102, 0xC0F8, 0x0, 0x558C, 0xBB8, 0x0)
    OP_8C(0x102, 135, 0)
    ClearChrFlags(0x102, 0x40)
    OP_A3(0x14)
    Return()

    # Function_24_3D1B end

    def Function_25_3D47(): pass

    label("Function_25_3D47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_3D54")
    Jump("loc_3F71")

    label("loc_3D54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F71")
    OP_28(0x9, 0x1, 0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6C(180000, 0)
    OP_6D(64629, 0, 38310, 0)
    SetChrPos(0x16, 75500, 0, 40200, 270)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    OP_0D()
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0xFD84, 0x0, 0x9DD0, 0xBB8, 0x0)
    TurnDirection(0x101, 0x16, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F啊，在那里！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFBF4, 0x0, 0x8BD8, 0x1770, 0x0)
    TurnDirection(0x101, 0x16, 0)
    TurnDirection(0x16, 0x101, 0)

    def lambda_3E47():
        OP_92(0x102, 0x101, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E47)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x16, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F等一下，艾丝蒂尔，听我说。\x02\x03",
            "#014F那只小猫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，它要跑了！\x02",
    )

    CloseMessageWindow()
    OP_90(0x101, 0x0, 0x0, 0x3E8, 0x1B58, 0x0)
    OP_43(0x101, 0x0, 0x1, 0x1D)
    OP_43(0x16, 0x0, 0x1, 0x1C)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A5(0x15)
    OP_A5(0x13)

    ChrTalk(
        0x101,
        (
            "#005F它朝教会那里跑去了，\x01",
            "这回可一定要把它给捉住！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F唉……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_3F71")

    label("loc_3F71")

    Return()

    # Function_25_3D47 end

    def Function_26_3F72(): pass

    label("Function_26_3F72")

    OP_6D(64300, 0, 38200, 3000)
    Return()

    # Function_26_3F72 end

    def Function_27_3F84(): pass

    label("Function_27_3F84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FA5")
    OP_6C(0, 3000)
    Jump("loc_3FCF")

    label("loc_3FA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FC6")
    OP_6C(0, 3000)
    Jump("loc_3FCF")

    label("loc_3FC6")

    OP_6C(180000, 3000)

    label("loc_3FCF")

    Return()

    # Function_27_3F84 end

    def Function_28_3FD0(): pass

    label("Function_28_3FD0")

    SetChrFlags(0x16, 0x40)
    OP_A6(0x15)
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0x11BFC, 0x1F4, 0x87F0, 0x1B58, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_A3(0x15)
    Return()

    # Function_28_3FD0 end

    def Function_29_4007(): pass

    label("Function_29_4007")

    OP_A6(0x13)

    label("loc_400A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_401C")
    TurnDirection(0x101, 0x16, 0)
    OP_48()
    Jump("loc_400A")

    label("loc_401C")

    OP_A3(0x13)
    Return()

    # Function_29_4007 end

    def Function_30_4020(): pass

    label("Function_30_4020")

    OP_92(0x102, 0x101, 0x5DC, 0xBB8, 0x0)
    Return()

    # Function_30_4020 end

    def Function_31_402F(): pass

    label("Function_31_402F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_403C")
    Jump("loc_4290")

    label("loc_403C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4290")
    OP_28(0x9, 0x1, 0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    Fade(1000)
    OP_6C(90000, 0)
    OP_6D(64500, 0, 40400, 0)
    SetChrPos(0x16, 75500, 0, 40200, 270)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x8)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x101, 61000, 0, 40300, 90)
    SetChrPos(0x102, 60000, 0, 42300, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40FB")
    SetChrPos(0x2, 59000, 0, 41300, 90)
    SetChrPos(0x3, 59000, 0, 42800, 90)
    Jump("loc_411A")

    label("loc_40FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_411A")
    SetChrPos(0x2, 59000, 0, 41300, 90)

    label("loc_411A")

    OP_0D()
    OP_62(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x16, 0x1016C, 0x0, 0x9DD0, 0xBB8, 0x0)
    TurnDirection(0x101, 0x16, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(
        0x101,
        "#004F啊，在那里！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 0)
    TurnDirection(0x16, 0x101, 0)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x16, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F等一下，艾丝蒂尔，听我说。\x02\x03",
            "#014F那只小猫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，它要跑了！\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x1, 0x22)
    OP_43(0x16, 0x0, 0x1, 0x1C)
    OP_A2(0x15)
    OP_A2(0x13)
    OP_A5(0x15)
    OP_A5(0x13)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#005F它朝教会那里跑去了，\x01",
            "这回可一定要把它给捉住！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F唉……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4290")

    label("loc_4290")

    Return()

    # Function_31_402F end

    def Function_32_4291(): pass

    label("Function_32_4291")

    OP_6D(64300, 0, 40200, 3000)
    Return()

    # Function_32_4291 end

    def Function_33_42A3(): pass

    label("Function_33_42A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42C4")
    OP_6C(90000, 3000)
    Jump("loc_42CD")

    label("loc_42C4")

    OP_6C(270000, 3000)

    label("loc_42CD")

    Return()

    # Function_33_42A3 end

    def Function_34_42CE(): pass

    label("Function_34_42CE")

    OP_A6(0x13)
    OP_90(0x101, 0xBB8, 0x0, 0x0, 0x1B58, 0x0)
    OP_8C(0x101, 135, 400)
    OP_A3(0x13)
    Return()

    # Function_34_42CE end

    def Function_35_42F0(): pass

    label("Function_35_42F0")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_6C(45000, 0)
    OP_6D(36470, 0, 58400, 0)
    OP_67(0, 11530, -10000, 0)
    OP_6B(2150, 0)
    SetChrPos(0x101, 38560, 0, 57230, 270)
    SetChrPos(0x102, 37800, 0, 58080, 225)
    TurnDirection(0x14, 0x101, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_438B")
    SetChrPos(0x2, 39290, 0, 58080, 211)
    SetChrPos(0x3, 40280, 0, 58050, 212)
    Jump("loc_43AA")

    label("loc_438B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43AA")
    SetChrPos(0x2, 39290, 0, 58080, 211)

    label("loc_43AA")

    SetChrPos(0x15, 36010, 0, 56150, 36)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x15, 0x40)
    TurnDirection(0x14, 0x102, 0)

    def lambda_43D7():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_43D7)
    OP_0D()
    Sleep(3000)

    ChrTalk(
        0x102,
        "#010F……事情的经过就是这样的。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#010F我想刚才安莉尔\x01",
            "可能正要回阿姨您这里来的……\x02\x03",
            "#010F它每次都是朝着茶座这边跑来的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊……\x01",
            "确实，经你这么一说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F或许是我们把它吓跑到其他地方去了……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x102, 400)

    ChrTalk(
        0x14,
        (
            "没有～\x01",
            "没关系的啦～～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x14, 0)

    ChrTalk(
        0x14,
        (
            "能够平安无事把它送回我这里来～\x01",
            "我已经很感激了啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "特别是这位帅气的尤基士君，\x01",
            "阿姨感动得都要哭了啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0x15,
        "喵喵～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#018F您、您实在太客气了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(
        0x101,
        "#507F（嘿嘿，他害羞啦，他害羞啦。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "呜呜～\x01",
            "阿姨是认真的啊～～㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#511F对、对不起，\x01",
            "我们必须要回协会报告情况了……\x02\x03",
            "告、告辞了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x14, 0)

    ChrTalk(
        0x101,
        "#508F阿姨再见～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "哦呵呵～㈱\x01",
            "再见了～～～～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4688():

        label("loc_4688")

        TurnDirection(0x0, 0x14, 0)
        OP_48()
        Jump("loc_4688")

    QueueWorkItem2(0x0, 1, lambda_4688)

    def lambda_4699():

        label("loc_4699")

        TurnDirection(0x1, 0x14, 0)
        OP_48()
        Jump("loc_4699")

    QueueWorkItem2(0x1, 1, lambda_4699)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D7")

    def lambda_46B8():

        label("loc_46B8")

        TurnDirection(0x2, 0x14, 0)
        OP_48()
        Jump("loc_46B8")

    QueueWorkItem2(0x2, 1, lambda_46B8)

    def lambda_46C9():

        label("loc_46C9")

        TurnDirection(0x3, 0x14, 0)
        OP_48()
        Jump("loc_46C9")

    QueueWorkItem2(0x3, 1, lambda_46C9)
    Jump("loc_46F6")

    label("loc_46D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46F6")

    def lambda_46EB():

        label("loc_46EB")

        TurnDirection(0x2, 0x14, 0)
        OP_48()
        Jump("loc_46EB")

    QueueWorkItem2(0x2, 1, lambda_46EB)

    label("loc_46F6")

    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x14, 0x40)

    def lambda_4706():
        OP_8E(0x15, 0x8AB6, 0x0, 0xC7EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4706)

    def lambda_4721():
        OP_8E(0x14, 0x8ACA, 0x0, 0xC918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4721)
    Sleep(400)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x15, 0x1)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4766")
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jump("loc_4778")

    label("loc_4766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4778")
    OP_44(0x2, 0x1)

    label("loc_4778")

    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x14, 0x40)
    SetChrPos(0x14, 39420, 250, 51560, 315)
    SetChrPos(0x15, 38700, 0, 50720, 315)
    SetChrChipByIndex(0x14, 20)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找小猫】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(1000)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_35_42F0 end

    SaveToFile()

Try(main)
