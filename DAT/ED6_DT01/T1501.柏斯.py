from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1501   ._SN',
        MapName             = 'Bose',
        Location            = 'T1501.x',
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
        '小船',                                 # 9
        '吉尔',                                 # 10
        '乔丝特',                               # 11
        '黑衣男子',                             # 12
        '特务兵',                               # 13
        '安塞尔新街方向',                       # 14
    )

    DeclEntryPoint(
        Unknown_00              = -7000,
        Unknown_04              = 0,
        Unknown_08              = 82000,
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
        Unknown_30              = 225,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 50,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02120 ._CH',             # 00
        'ED6_DT07/CH02130 ._CH',             # 01
        'ED6_DT07/CH02200 ._CH',             # 02
        'ED6_DT07/CH00444 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH02120P._CP',             # 00
        'ED6_DT07/CH02130P._CP',             # 01
        'ED6_DT07/CH02200P._CP',             # 02
        'ED6_DT07/CH00444P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8640,
        Z                   = 0,
        Y                   = 96040,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -8691,
        Y                   = 3000,
        Z                   = 54000,
        Range               = -10060,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xDEEE,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -29705,
        Y                   = -3000,
        Z                   = 53403,
        Range               = -31123,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xC4FE,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -4352,
        Y                   = -1000,
        Z                   = 81810,
        Range               = -10405,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x142A8,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -5850,
        Y                   = -1000,
        Z                   = 80880,
        Range               = -10140,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x14438,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -43330,
        Y                   = -3000,
        Z                   = 38850,
        Range               = -46440,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xA046,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    ScpFunction(
        "Function_0_22A",          # 00, 0
        "Function_1_23E",          # 01, 1
        "Function_2_25B",          # 02, 2
        "Function_3_271",          # 03, 3
        "Function_4_34E",          # 04, 4
        "Function_5_7AC",          # 05, 5
        "Function_6_7E1",          # 06, 6
        "Function_7_80F",          # 07, 7
        "Function_8_833",          # 08, 8
        "Function_9_B78",          # 09, 9
        "Function_10_2490",        # 0A, 10
        "Function_11_252E",        # 0B, 11
        "Function_12_26A6",        # 0C, 12
    )


    def Function_0_22A(): pass

    label("Function_0_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_23D")
    OP_A3(0x3FA)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_23D")

    Return()

    # Function_0_22A end

    def Function_1_23E(): pass

    label("Function_1_23E")

    OP_16(0x2, 0xFA0, 0xFFFDC998, 0xFFFEE2D8, 0x30046)
    OP_71(0x1, 0x4)
    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_23E end

    def Function_2_25B(): pass

    label("Function_2_25B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_270")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_25B")

    label("loc_270")

    Return()

    # Function_2_25B end

    def Function_3_271(): pass

    label("Function_3_271")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(-7046, 500, 43491, 0)
    OP_6B(5900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, -9345, 0, 78200, 180)
    SetChrPos(0x102, -10370, 0, 78100, 180)
    SetChrPos(0x104, -8638, 0, 79300, 180)
    SetChrPos(0x103, -9788, 0, 79400, 180)

    def lambda_2EE():
        OP_6C(327000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EE)
    Sleep(1000)

    def lambda_303():
        OP_67(0, 4100, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_303)

    def lambda_31B():
        OP_6D(-12358, 3550, 46969, 7000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31B)
    OP_6B(3547, 7000)
    FadeToDark(1000, 0, -1)
    OP_A2(0x3FA)
    OP_0D()
    NewScene("ED6_DT01/T1511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_271 end

    def Function_4_34E(): pass

    label("Function_4_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AB")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x34F)
    OP_28(0x38, 0x1, 0x200)
    SetChrPos(0x9, -8576, 0, 86453, 0)
    SetChrPos(0xA, -7848, 0, 86453, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x0, 0, 400)
    OP_8C(0x1, 0, 400)
    OP_8C(0x2, 0, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB")

    ChrTalk(
        0x101,
        "#004F那、那是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_457")

    label("loc_3FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F")

    ChrTalk(
        0x102,
        "#012F好像来了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_457")

    label("loc_42F")


    ChrTalk(
        0x103,
        "#027F有人过来了……\x02",
    )

    CloseMessageWindow()

    label("loc_457")

    Sleep(100)
    Fade(1000)

    def lambda_467():
        OP_6D(-8786, 0, 78490, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_467)

    def lambda_47F():
        OP_6C(0, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47F)
    OP_0D()

    def lambda_490():
        OP_8E(0xFE, 0xFFFFDE80, 0x0, 0x12D90, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_490)
    Sleep(600)
    OP_8E(0xA, 0xFFFFE158, 0x0, 0x13178, 0xBB8, 0x0)

    ChrTalk(
        0x9,
        (
            "#200F到了……\x01",
            "看来我们来得有点早。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 400)

    ChrTalk(
        0xA,
        (
            "#210F#2P是啊。\x02\x03",
            "啊～如果现在是早上就好了，\x01",
            "可以在这家旅馆吃上一顿。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 45, 400)

    ChrTalk(
        0x9,
        (
            "#203F别说这种没用的话了。\x01",
            "你明知我们现在被王国军通缉。\x02\x03",
            "#200F好了，快点走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x5)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xA,
        "#213F#2P#5A啊，等等，吉尔哥。\x05\x02",
    )

    Sleep(1500)
    OP_43(0xA, 0x1, 0x0, 0x6)

    def lambda_649():
        OP_6D(-15030, 0, 60460, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_649)

    def lambda_661():
        OP_6C(225000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_661)
    WaitChrThread(0xA, 0x1)
    Sleep(1000)
    SetChrPos(0x101, -12740, 4000, 55150, 315)
    SetChrPos(0x102, -11650, 4000, 55060, 315)
    SetChrPos(0x103, -10600, 4000, 55110, 270)
    OP_6D(-11630, 4000, 55050, 2000)

    ChrTalk(
        0x101,
        "#002F……果然是这些家伙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F好像往栈桥的方向走去了。\x01",
            "　\x02\x03",
            "他们打算做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F反正我们就拭目以待吧。\x02\x03",
            "别被他们察觉，静静地跟在后面就行了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_7AB")

    Return()

    # Function_4_34E end

    def Function_5_7AC(): pass

    label("Function_5_7AC")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFD88C, 0x0, 0xFF78, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFAB46, 0x0, 0xD8C2, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_7AC end

    def Function_6_7E1(): pass

    label("Function_6_7E1")

    OP_8E(0xFE, 0xFFFFD88C, 0x0, 0xFF78, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFAB46, 0x0, 0xD8C2, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_7E1 end

    def Function_7_80F(): pass

    label("Function_7_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_822")
    Call(0, 9)
    Jump("loc_832")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_832")
    Call(0, 11)

    label("loc_832")

    Return()

    # Function_7_80F end

    def Function_8_833(): pass

    label("Function_8_833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_END)), "loc_83D")
    Jump("loc_B77")

    label("loc_83D")

    OP_A2(0x36A)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -45460, -2000, 38500, 180)
    SetChrPos(0x102, -44530, -2000, 39140, 180)
    SetChrPos(0x103, -45500, -2000, 39550, 180)
    OP_6D(-45030, -2000, 38970, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#007F#6P唔……一个人都没有呢～\x02\x03",
            "#505F虽然不知道他们的目的，\x01",
            "不过那对兄妹真的会出现吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)

    ChrTalk(
        0x102,
        (
            "#012F#4P目前还没有确实的证据……\x01",
            "但如果罗伊德先生的情报没错的话，\x01",
            "那他们今晚肯定会出现的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 135, 400)

    ChrTalk(
        0x103,
        (
            "#022F不过，要是我们随处乱走的话，\x01",
            "说不定会打草惊蛇哦。\x02\x03",
            "那些空贼应该会从街道那边过来，\x01",
            "我们最好还是仔细注意门口。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(
        0x101,
        (
            "#006F#6P的确是啊……\x01",
            "那么躲在哪里守候比较好呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F#4P能够看到街道方向而又\x01",
            "不容易被别人发现的地方……\x02\x03",
            "#010F看来也只有那里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x38, 0x1, 0x100)
    EventEnd(0x0)

    label("loc_B77")

    Return()

    # Function_8_833 end

    def Function_9_B78(): pass

    label("Function_9_B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_248F")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x350)
    OP_28(0x38, 0x1, 0x400)
    SetChrPos(0x9, -44910, -1970, 38660, 180)
    SetChrPos(0xA, -44520, -1970, 39860, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_BC6():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC6)
    OP_6D(-44910, -1970, 38660, 3000)
    SetChrPos(0x101, -31171, 0, 56060, 180)
    SetChrPos(0x102, -32244, 0, 56400, 180)
    SetChrPos(0x103, -30520, 0, 55440, 180)

    ChrTalk(
        0x9,
        (
            "#200F果然还没来。\x02\x03",
            "今天怎么了……\x01",
            "平时他们都是很准时的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#212F本小姐可不太喜欢那些家伙。\x02\x03",
            "老是摆出一副高傲的架子……\x01",
            "而且行事又那么鬼鬼祟祟的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(
        0x9,
        (
            "#200F确实……\x01",
            "一群来历不明的家伙。\x02\x03",
            "不过没法啦。\x01",
            "这可是多伦大哥的命令啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6C(45000, 0)
    OP_6D(-30885, 0, 55794, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#020F（这个距离应该没问题吧……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F#5P（嗯，可以清楚听到他们说话呢。）\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6C(225000, 0)
    OP_6D(-44910, -1970, 38660, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#215F………………………………\x02\x03",
            "喂，吉尔哥……\x02\x03",
            "不觉得多伦大哥最近怪怪的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#204F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#212F真的很怪呢。\x01",
            "无缘无故叫我们去劫定期船。\x02\x03",
            "虽说干这个收获肯定不少，\x01",
            "不过现在军队已经全力介入了……\x02\x03",
            "就连那些多管闲事的\x01",
            "游击士也插了一脚进来……\x02\x03",
            "而且我们还扣押人质，\x01",
            "要求数额这么大的赎金……\x02\x03",
            "我们是不是干得太过分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#200F你在说什么呀？\x01",
            "也难怪，毕竟你是个女孩子。\x02\x03",
            "身为空贼的觉悟果然还不够啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#216F什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#202F我这可是在称赞你哦。\x02\x03",
            "#200F如果觉得不适应，\x01",
            "也可以自己一个人先回老家嘛。\x02\x03",
            "只要不介意老家有点落后，\x01",
            "在那生活倒也挺轻松自在的。\x02\x03",
            "不过那里可比这国家冷很多哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#214F你、你再这么说我可要生气了。\x02\x03",
            "你没看到我不在的时候，\x01",
            "做饭洗衣服这些家务通通没人管吗！？\x02\x03",
            "难道你们还想重现\x01",
            "我去洛连特那段时期自己的惨状吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#203F好啦好啦……\x01",
            "算我刚才说错了，不好意思。\x02\x03",
            "#200F不过我还是希望你能想清楚。\x01",
            "再跟我们干下去，想回头可就难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#215F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#203F算了，先不说这个。\x02\x03",
            "其实我也觉得，\x01",
            "多伦大哥最近的行为挺怪异的。\x02\x03",
            "为了提高赎金的数额而拖延时间，\x01",
            "完全没考虑到做事要有限度。\x02\x03",
            "按道理，多伦大哥应该\x01",
            "不会蠢到连这一点也不知道吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#212F就是啊……\x01",
            "特别是在那个家伙来了之后。\x02\x03",
            "不过我们也唯有照办啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#200F确实……\x01",
            "那家伙还介绍蒙面人给我们。\x02\x03",
            "总有种被他们唆使着的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6C(45000, 0)
    OP_6D(-30885, 0, 55794, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#505F#5P（那家伙？蒙面人？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#022F（嗯，应该是在说谁吧。）\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_20(0x5DC)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#014F（那、那是……）\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        "#004F#5P（怎么了？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F（好像有人来了。）\x02",
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x51)
    Sleep(100)
    Fade(1000)
    OP_6C(225000, 0)
    OP_6D(-45040, -1970, 29060, 0)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_8C(0x9, 180, 0)
    OP_8C(0xA, 180, 0)
    SetChrPos(0x8, -45110, -2700, 20060, 180)
    SetChrFlags(0x8, 0x40)
    OP_A1(0x8, 0x1)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x0, 0x8, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x8, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    OP_72(0x1, 0x4)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x400)
    OP_71(0x1, 0x40)
    OP_48()
    OP_89(0xB, -45060, -2000, 21500, 0)
    OP_89(0xC, -45060, -2000, 20000, 0)
    OP_22(0xD4, 0x0, 0x64)

    def lambda_18E0():
        OP_6D(-45380, -1970, 36390, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_18E0)

    def lambda_18F8():
        OP_91(0xFE, 0x0, 0x0, 0x11170, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18F8)
    Sleep(2000)

    def lambda_1918():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1918)
    Sleep(800)

    def lambda_1938():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1938)
    Sleep(700)

    def lambda_1958():
        OP_91(0xFE, 0x0, 0x0, 0x124F8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1958)
    Sleep(600)
    OP_82(0x1, 0x2)

    def lambda_197B():
        OP_91(0xFE, 0x0, 0x0, 0x124F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_197B)
    Sleep(500)

    def lambda_199B():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_199B)
    Sleep(400)

    def lambda_19BB():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19BB)
    PlayEffect(0x4, 0x2, 0x8, 0, -300, 2400, 180, 0, 0, 1100, 100, 1600, 0xFF, 0, 0, 0, 0)
    Sleep(400)

    def lambda_1A10():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A10)
    Sleep(300)
    OP_82(0x0, 0x2)

    def lambda_1A33():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A33)
    Sleep(300)

    def lambda_1A53():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A53)
    Sleep(300)

    def lambda_1A73():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A73)
    Sleep(300)

    def lambda_1A93():
        OP_91(0xFE, 0x0, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A93)
    OP_82(0x2, 0x2)
    WaitChrThread(0x0, 0x1)

    ChrTalk(
        0x9,
        (
            "#200F哟，终于来了。\x02\x03",
            "不是说好按约定的时间来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#210F哼，今天也太迟了吧。\x01",
            "我们可是在这等了很久哦。\x02\x03",
            "真是的，一点都不可爱的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#280F呵……\x01",
            "严守时间可是我们一贯的准则。\x02\x03",
            "要是有什么得罪的地方，还请多包涵。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#214F你、你好像在讽刺我们哦！\x02\x03",
            "真是的，一点都不可爱的……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(
        0x9,
        "#201F#5P算了，别再说了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(
        0x9,
        (
            "#200F总之……\x01",
            "我们还是先回正题吧。\x02\x03",
            "那件事进展得如何了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#280F啊啊，陛下终于出面了。\x02\x03",
            "她打算动用自己的资产\x01",
            "来支付你们所要求的赎金。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#202F这、这还真是……\x01",
            "竟然让女王陛下亲自掏腰包……\x02\x03",
            "看来这件事也到了尾声了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#210F王国军方面怎么样了？\x02\x03",
            "他们应该不会发现\x01",
            "我们的据点在那种地方吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#280F暂时还不会。\x01",
            "不过这也只是时间上的问题。\x02\x03",
            "我这里收到情报，\x01",
            "游击士协会的人也在行动了。\x02\x03",
            "你们不会在快要得手的时候\x01",
            "舍弃自己的基地吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#200F啊啊……\x01",
            "没那么容易被找到的。\x02\x03",
            "况且大哥他肯定不舍得丢下那里。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-30885, 0, 55794, 0)
    OP_8C(0x101, 180, 0)
    OP_6C(45000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#002F#5P（又有一个奇怪的人物出现了。）\x02\x03",
            "（雪拉姐，怎么办？\x01",
            "　一口气冲出去把他们抓住吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(
        0x103,
        (
            "#026F（还不行……\x01",
            "　比起这样做，我反而有个良策。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#5P（良策？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F（既然那对兄妹出现了，\x01",
            "　那这附近应该会停泊有空贼飞艇。）\x02\x03",
            "#027F（这次一定不能再让他们逃走，\x01",
            "　我们可以先找出空贼飞艇让他们无处可逃。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#5P（原来是这样啊……\x01",
            "　我们要先截断他们的退路。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(
        0x101,
        "#006F#5P（我赞成这样做，约修亚你呢？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#510F（………………………………）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#505F#5P（你怎么了……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F（啊，啊啊……）\x02\x03",
            "（先找出空贼飞艇的确是个良策，\x01",
            "　嗯，我也赞同这个做法。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F#5P（……你没事吧？）\x02\x03",
            "（怎么了，这么凝重的脸色？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#013F（没什么……）\x02\x03",
            "（可能是错觉吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F#5P（………………？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F（看来还有一点时间。）\x02\x03",
            "（趁他们还没有谈完，\x01",
            "　我们赶快到街道找空贼飞艇吧。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x5DC)
    Sleep(50)
    EventEnd(0x4)
    OP_21()
    OP_1E()

    label("loc_248F")

    Return()

    # Function_9_B78 end

    def Function_10_2490(): pass

    label("Function_10_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_252D")
    EventBegin(0x0)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "离开川蝉亭的艾丝蒂尔等人\x01",
            "到街道去搜索空贼飞艇能停降的地方。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x38, 0x1, 0x800)
    OP_28(0x39, 0x4, 0x2)
    OP_28(0x39, 0x4, 0x4)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R1403   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_252D")

    Return()

    # Function_10_2490 end

    def Function_11_252E(): pass

    label("Function_11_252E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26A5")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25AE")

    ChrTalk(
        0x101,
        (
            "#006F（得先控制住空贼艇才行。\x01",
            "　赶快去街道上找找吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268A")

    label("loc_25AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2638")

    ChrTalk(
        0x102,
        (
            "#012F（我们要首先控制空贼艇……\x01",
            "　去街道周边地区搜索一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268A")

    label("loc_2638")


    ChrTalk(
        0x103,
        (
            "#022F（没时间了……\x01",
            "　要赶快去街道上找到空贼艇。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268A")

    OP_8E(0x0, 0xFFFF8F8A, 0x0, 0xCB20, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_26A5")

    Return()

    # Function_11_252E end

    def Function_12_26A6(): pass

    label("Function_12_26A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2801")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271E")

    ChrTalk(
        0x101,
        (
            "#006F（啊，这边是街道。\x01",
            "　现在最好去栈桥那边看看。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E3")

    label("loc_271E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_278E")

    ChrTalk(
        0x102,
        (
            "#012F（去街道上也没有用……\x01",
            "　现在要赶快去栈桥那边。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E3")

    label("loc_278E")


    ChrTalk(
        0x103,
        (
            "#022F（这边是街道……\x01",
            "　现在要赶快去栈桥那边。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E3")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_2951")

    label("loc_2801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2951")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2825")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_282C")

    label("loc_2825")

    TurnDirection(0x103, 0x0, 400)

    label("loc_282C")


    def lambda_2832():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2832)

    def lambda_2840():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2840)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_END)), "loc_28CE")

    ChrTalk(
        0x103,
        (
            "#022F现在没有回到街道上的必要。\x02\x03",
            "要先找到能够监视\x01",
            "街道方向来人的地点。\x02",
        )
    )

    Jump("loc_2935")

    label("loc_28CE")


    ChrTalk(
        0x103,
        (
            "#022F现在没有回到街道上的必要。\x01",
            "　\x02\x03",
            "还是先去栈桥那边巡视一下吧。\x01",
            "　\x02",
        )
    )


    label("loc_2935")

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2951")

    Return()

    # Function_12_26A6 end

    SaveToFile()

Try(main)
