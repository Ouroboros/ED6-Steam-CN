from ED6ScenarioHelper import *

def main():
    # 工房船莱普尼兹号

    CreateScenaFile(
        FileName            = 'E0002   ._SN',
        MapName             = 'event',
        Location            = 'E0002.x',
        MapIndex            = 232,
        MapDefaultBGM       = "ed60001",
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
        Unknown_04              = 4000,
        Unknown_08              = -4500,
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
        Unknown_3A              = 232,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_E0",           # 01, 1
        "Function_2_107",          # 02, 2
        "Function_3_1E1",          # 03, 3
        "Function_4_233",          # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_B8")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_B8")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_CC"),
        (103, "loc_CC"),
        (102, "loc_CC"),
        (SWITCH_DEFAULT, "loc_DF"),
    )


    label("loc_CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC")
    Event(0, 4)

    label("loc_DC")

    Jump("loc_DF")

    label("loc_DF")

    Return()

    # Function_0_AA end

    def Function_1_E0(): pass

    label("Function_1_E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1")
    OP_22(0x79, 0x1, 0x64)

    label("loc_F1")

    OP_22(0x1C3, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_106")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_106")

    Return()

    # Function_1_E0 end

    def Function_2_107(): pass

    label("Function_2_107")

    OP_22(0x79, 0x1, 0x14)
    EventBegin(0x0)
    OP_6D(4490, 5000, 36760, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(189000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_43(0x102, 0x0, 0x0, 0x3)
    FadeToBright(2000, 0)

    def lambda_175():
        OP_6D(970, 5000, -15390, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_175)

    def lambda_18D():
        OP_67(0, 8000, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18D)
    Sleep(2000)

    def lambda_1AA():
        OP_6B(5000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AA)

    def lambda_1BA():
        OP_6C(156000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1BA)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/E0012   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_107 end

    def Function_3_1E1(): pass

    label("Function_3_1E1")

    Sleep(300)
    OP_24(0x79, 0x14)
    Sleep(300)
    OP_24(0x79, 0x1E)
    Sleep(300)
    OP_24(0x79, 0x28)
    Sleep(300)
    OP_24(0x79, 0x32)
    Sleep(300)
    OP_24(0x79, 0x3C)
    Sleep(300)
    OP_24(0x79, 0x46)
    Sleep(300)
    OP_24(0x79, 0x50)
    Sleep(300)
    OP_24(0x79, 0x5A)
    Sleep(300)
    OP_24(0x79, 0x64)
    Return()

    # Function_3_1E1 end

    def Function_4_233(): pass

    label("Function_4_233")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(8370, -18350, -3430, 0)
    OP_67(0, 4240, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(90000, 0)
    OP_6E(378, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 3150, 5000, -2260, 90)
    SetChrPos(0x102, 3160, 5000, -3660, 90)

    def lambda_2AC():
        OP_6D(5750, 5000, -1990, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AC)

    def lambda_2C4():
        OP_67(0, 6400, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C4)
    Sleep(2000)

    def lambda_2E1():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E1)

    def lambda_2F1():
        OP_6E(262, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F1)
    Sleep(8000)

    ChrTalk(
        0x101,
        (
            "#001F哇～～好高啊。\x02\x03",
            "我们好像很久没坐过飞艇了吧。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊……\x01",
            "上次潜入空贼飞艇的时候\x01",
            "连看风景的机会和余闲也没有。\x02\x03",
            "#013F虽说现在和那时很相似，\x01",
            "但我觉得这次的状况更为危险……\x02\x03",
            "不能掉以轻心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F嗯……知道啦。\x02\x03",
            "#003F不过，一向和平的利贝尔\x01",
            "竟然会发生那样的事情……\x02\x03",
            "我总觉得好像有什么大事\x01",
            "开始蠢蠢欲动似的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F#4P是啊……我也这么想。\x02\x03",
            "空贼和卢安市长所做的坏事\x01",
            "都是由那些黑衣人在背后操纵。\x02\x03",
            "#015F因此，如果能知道他们的真面目，\x01",
            "一定可以掌握到重要的线索。\x02\x03",
            "#010F说不定……\x01",
            "这也是父亲外出调查的原因。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#501F#5P是吗……\x02\x03",
            "#006F好，救出博士之后，\x01",
            "我们最好也在附近查查看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/E0012   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_233 end

    SaveToFile()

Try(main)
