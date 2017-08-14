from ED6ScenarioHelper import *

def main():
    # 鲁希尔工房

    CreateScenaFile(
        FileName            = 'T1100   ._SN',
        MapName             = 'Bose',
        Location            = 'T1100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        '王国军士兵',                           # 9
        '王国军士兵',                           # 10
        '王国军士兵',                           # 11
        '王国军士兵',                           # 12
        '王国军军官',                           # 13
        '穿黑衣的将校',                         # 14
        '女性军官',                             # 15
        '奈尔',                                 # 16
        '朵洛希',                               # 17
        '安塞尔新街方向',                       # 18
        '柏斯市·北街区',                       # 19
    )

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH02030 ._CH',             # 02
        'ED6_DT07/CH02100 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT07/CH02070 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH02030P._CP',             # 02
        'ED6_DT07/CH02100P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT07/CH02070P._CP',             # 05
    )

    DeclNpc(
        X                   = 52155,
        Z                   = -3000,
        Y                   = 17688,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = -3000,
        Y                   = 27604,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 72117,
        Z                   = 3000,
        Y                   = 28437,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 36188,
        Z                   = 0,
        Y                   = 16750,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48683,
        Z                   = -3000,
        Y                   = 29357,
        Direction           = 270,
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
        X                   = 48626,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
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
        X                   = 47692,
        Z                   = 0,
        Y                   = 39390,
        Direction           = 270,
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
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
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
        X                   = -620,
        Z                   = -1000,
        Y                   = -3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 47970,
        Z                   = -3000,
        Y                   = 4220,
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

    DeclNpc(
        X                   = 48070,
        Z                   = 0,
        Y                   = 48590,
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
        X                   = 41890,
        Y                   = -6000,
        Z                   = 37580,
        Range               = 56300,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x4A88,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 53090,
        Y                   = -3000,
        Z                   = 20940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 15,
    )

    DeclEvent(
        X                   = 55320,
        Y                   = -3000,
        Z                   = 33040,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 16,
    )


    ScpFunction(
        "Function_0_29A",          # 00, 0
        "Function_1_332",          # 01, 1
        "Function_2_39A",          # 02, 2
        "Function_3_3B0",          # 03, 3
        "Function_4_432",          # 04, 4
        "Function_5_456",          # 05, 5
        "Function_6_50D",          # 06, 6
        "Function_7_5D1",          # 07, 7
        "Function_8_68A",          # 08, 8
        "Function_9_75C",          # 09, 9
        "Function_10_873",         # 0A, 10
        "Function_11_24E5",        # 0B, 11
        "Function_12_2513",        # 0C, 12
        "Function_13_2AED",        # 0D, 13
        "Function_14_2EAD",        # 0E, 14
        "Function_15_3090",        # 0F, 15
        "Function_16_3094",        # 10, 16
    )


    def Function_0_29A(): pass

    label("Function_0_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_323")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_323")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 48000, -3000, 30522, 180)
    SetChrPos(0x9, 49200, -3000, 30522, 180)
    SetChrPos(0xA, 48000, -3000, 31900, 180)
    SetChrPos(0xB, 49200, -3000, 31900, 180)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)

    label("loc_323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_331")
    OP_A3(0x3FA)
    Event(0, 12)

    label("loc_331")

    Return()

    # Function_0_29A end

    def Function_1_332(): pass

    label("Function_1_332")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFE7960, 0x30040)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A")
    OP_1B(0xD, 0x0, 0xD)
    Jump("loc_367")

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_367")
    OP_1B(0xD, 0x0, 0xD)

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_387")
    OP_1B(0xD, 0x0, 0xD)
    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0xE)
    OP_1B(0x2, 0x0, 0xE)

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_399")
    OP_10(0xE, 0x1)
    OP_10(0x5, 0x0)

    label("loc_399")

    Return()

    # Function_1_332 end

    def Function_2_39A(): pass

    label("Function_2_39A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_39A")

    label("loc_3AF")

    Return()

    # Function_2_39A end

    def Function_3_3B0(): pass

    label("Function_3_3B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_431")
    OP_8E(0xFE, 0xBBF8, 0xFFFFF448, 0x7DC8, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 500)
    Sleep(500)
    OP_8C(0xFE, 270, 500)
    Sleep(500)
    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xBBE4, 0xFFFFF448, 0x4D26, 0x7D0, 0x0)
    Sleep(300)
    Sleep(500)
    OP_8C(0xFE, 90, 500)
    Sleep(500)
    OP_8C(0xFE, 270, 500)
    Sleep(500)
    OP_8C(0xFE, 0, 500)
    Jump("Function_3_3B0")

    label("loc_431")

    Return()

    # Function_3_3B0 end

    def Function_4_432(): pass

    label("Function_4_432")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_455")
    OP_8D(0xFE, 75166, 31996, 63100, 26500, 2000)
    Jump("Function_4_432")

    label("loc_455")

    Return()

    # Function_4_432 end

    def Function_5_456(): pass

    label("Function_5_456")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50C")
    Sleep(2000)
    OP_8E(0xFE, 0x5442, 0x0, 0x416B, 0x7D0, 0x0)
    Sleep(1000)
    OP_8E(0xFE, 0x4EDE, 0xBB8, 0x7DB6, 0x7D0, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0x4FC4, 0xBB8, 0x6ECA, 0x7D0, 0x0)
    Sleep(1000)
    OP_8E(0xFE, 0x5B04, 0xBB8, 0x6C06, 0x7D0, 0x0)
    Sleep(4000)
    OP_8E(0xFE, 0x548D, 0xBB8, 0x6706, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5442, 0x0, 0x416B, 0x7D0, 0x0)
    Sleep(2000)
    OP_8E(0xFE, 0x8D5E, 0x0, 0x416E, 0x7D0, 0x0)
    Jump("Function_5_456")

    label("loc_50C")

    Return()

    # Function_5_456 end

    def Function_6_50D(): pass

    label("Function_6_50D")

    TalkBegin(0x8)

    ChrTalk(
        0xFE,
        (
            "你们就是那几个\x01",
            "游击士协会的人啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看在市长的份上这次就饶过你们，\x01",
            "但是不能再妨碍我们办事哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_6_50D end

    def Function_7_5D1(): pass

    label("Function_7_5D1")

    TalkBegin(0x9)

    ChrTalk(
        0xFE,
        (
            "竟然在我们搜索的背后捣乱，\x01",
            "公然在大街上实行抢劫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "很漂亮地将了我们一军啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_7_5D1 end

    def Function_8_68A(): pass

    label("Function_8_68A")

    TalkBegin(0xA)

    ChrTalk(
        0xFE,
        (
            "在废坑里的空贼\x01",
            "好像是二女一男的团伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "根据传言，\x01",
            "其中好像还有小孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "什么，你说他们不是空贼？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_8_68A end

    def Function_9_75C(): pass

    label("Function_9_75C")

    TalkBegin(0xB)

    ChrTalk(
        0xFE,
        (
            "摩尔根将军虽然很顽固，\x01",
            "但是他指挥得当，是个很厉害的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不愧是在１０年前\x01",
            "击退帝国军的元老啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但是，\x01",
            "他这次也遇到了如此棘手的问题。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_9_75C end

    def Function_10_873(): pass

    label("Function_10_873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24E4")
    OP_A2(0x339)
    OP_28(0x37, 0x1, 0x4)
    OP_28(0x37, 0x1, 0x8)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    def lambda_8B3():

        label("loc_8B3")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8B3")

    QueueWorkItem2(0xC, 1, lambda_8B3)

    def lambda_8C4():

        label("loc_8C4")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8C4")

    QueueWorkItem2(0x8, 1, lambda_8C4)

    def lambda_8D5():

        label("loc_8D5")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8D5")

    QueueWorkItem2(0x9, 1, lambda_8D5)

    def lambda_8E6():

        label("loc_8E6")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8E6")

    QueueWorkItem2(0xA, 1, lambda_8E6)

    def lambda_8F7():

        label("loc_8F7")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_8F7")

    QueueWorkItem2(0xB, 1, lambda_8F7)

    ChrTalk(
        0xC,
        "喂！你们几个！\x02",
    )

    CloseMessageWindow()

    def lambda_920():

        label("loc_920")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_920")

    QueueWorkItem2(0x0, 2, lambda_920)
    Sleep(100)
    Fade(1000)

    def lambda_93B():

        label("loc_93B")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_93B")

    QueueWorkItem2(0x1, 2, lambda_93B)

    def lambda_94C():

        label("loc_94C")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_94C")

    QueueWorkItem2(0x2, 2, lambda_94C)

    def lambda_95D():

        label("loc_95D")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_95D")

    QueueWorkItem2(0x3, 2, lambda_95D)

    def lambda_96E():
        OP_69(0xC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_96E)

    def lambda_97C():
        OP_6C(0, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_97C)

    def lambda_98C():
        OP_6B(2800, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_98C)
    SetChrPos(0x102, 47362, -3000, 27682, 0)
    SetChrPos(0x101, 48132, -3000, 27051, 0)
    SetChrPos(0x103, 49152, -3000, 27309, 0)
    SetChrPos(0x104, 49977, -3000, 28146, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#501F嗯？怎么了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "有一句话要忠告你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "虽说是在为市长办事，\x01",
            "但你们压根儿还是普通市民。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "在调查正紧张进行的时候，\x01",
            "别老是在我们面前走来走去。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#509F什、什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F说是忠告，其实是警告才对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "我只是把丑话说在前面。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "你们那么喜欢多管闲事的话，\x01",
            "等我们撤退之后，再去调查个够吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "不自量力只会惹来麻烦，\x01",
            "再被招待进牢房可不好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#027F别在意，艾丝蒂尔。\x01",
            "反正我们也没有做错任何事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F那当然了，\x01",
            "狐假虎威之辈根本不足为惧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xC,
        "什、什么！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "男性的声音",
        "#6P……你们在做什么？\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x65)
    OP_44(0xC, 0xFF)
    OP_8C(0xC, 0, 400)

    def lambda_DF1():
        OP_6D(48924, -3000, 31700, 2000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_DF1)
    OP_44(0xC, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    def lambda_E2D():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E2D)

    def lambda_E3B():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E3B)

    def lambda_E49():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E49)

    def lambda_E57():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E57)

    def lambda_E65():

        label("loc_E65")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_E65")

    QueueWorkItem2(0x0, 1, lambda_E65)

    def lambda_E76():

        label("loc_E76")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_E76")

    QueueWorkItem2(0x1, 1, lambda_E76)

    def lambda_E87():

        label("loc_E87")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_E87")

    QueueWorkItem2(0x2, 1, lambda_E87)

    def lambda_E98():

        label("loc_E98")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_E98")

    QueueWorkItem2(0x3, 1, lambda_E98)
    Sleep(1000)

    def lambda_EAE():
        OP_8E(0xD, 0xBDF2, 0xFFFFF448, 0x79F9, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EAE)
    Sleep(600)

    def lambda_ECE():
        OP_8E(0xE, 0xBA4C, 0xFFFFF448, 0x7CA5, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_ECE)

    def lambda_EE9():

        label("loc_EE9")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_EE9")

    QueueWorkItem2(0x8, 2, lambda_EE9)

    def lambda_EFA():

        label("loc_EFA")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_EFA")

    QueueWorkItem2(0x9, 2, lambda_EFA)

    def lambda_F0B():

        label("loc_F0B")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_F0B")

    QueueWorkItem2(0xA, 2, lambda_F0B)

    def lambda_F1C():

        label("loc_F1C")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_F1C")

    QueueWorkItem2(0xB, 2, lambda_F1C)
    Sleep(900)

    def lambda_F32():
        OP_8F(0xFE, 0xC2C7, 0xFFFFF448, 0x7D5F, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F32)

    def lambda_F4D():
        OP_8F(0xFE, 0xC727, 0xFFFFF448, 0x7D5F, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F4D)
    Sleep(500)

    def lambda_F6D():
        OP_8F(0xFE, 0xC2C7, 0xFFFFF448, 0x7869, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F6D)

    def lambda_F88():
        OP_8F(0xFE, 0xC727, 0xFFFFF448, 0x7869, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F88)
    WaitChrThread(0xE, 0x1)

    ChrTalk(
        0xC,
        "是、是上校！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#112F#5P身为王国军的军人，\x01",
            "竟然在这里威胁善良的市民……\x02\x03",
            "真是的，简直不知廉耻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "可、可是上校，\x01",
            "这几个家伙都不是普通人啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "他们是游击士啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#113F#5P啊，原来如此……\x02\x03",
            "#112F所以你们更不应如此无礼，\x01",
            "军队和协会向来就存在合作关系。\x02\x03",
            "难道你们想煽动两方对立吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "可、可我这也是\x01",
            "遵照将军的意思行事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#115F#5P你错了。这样做只会\x01",
            "给摩尔根将军增添无谓的麻烦。\x02\x03",
            "#110F这里就交给我处理吧。\x01",
            "你召集好自己的部下马上撤走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "可、可是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#110F#5P从早上就开始调查，\x01",
            "应该已经收集到足够的情报了吧。\x02\x03",
            "至于将军那里，\x01",
            "我稍后会亲自向他交代。\x02\x03",
            "你们还有什么疑问吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "明、明白……\x02",
    )

    CloseMessageWindow()
    OP_44(0xC, 0xFF)
    OP_8C(0xC, 45, 400)

    def lambda_1362():

        label("loc_1362")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1362")

    QueueWorkItem2(0x8, 2, lambda_1362)

    def lambda_1373():

        label("loc_1373")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1373")

    QueueWorkItem2(0x9, 2, lambda_1373)

    def lambda_1384():

        label("loc_1384")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1384")

    QueueWorkItem2(0xA, 2, lambda_1384)

    def lambda_1395():

        label("loc_1395")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_1395")

    QueueWorkItem2(0xB, 2, lambda_1395)
    Sleep(400)

    ChrTalk(
        0xC,
        (
            "撤退！\x01",
            "返回哈肯大门！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13F2():
        OP_6D(48683, -3000, 30000, 2000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_13F2)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xC, 90, 400)
    OP_43(0xC, 0x1, 0x0, 0xB)
    Sleep(700)
    OP_43(0x9, 0x1, 0x0, 0xB)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0xB)
    Sleep(400)
    OP_43(0xB, 0x1, 0x0, 0xB)
    Sleep(400)
    OP_43(0xA, 0x1, 0x0, 0xB)
    Sleep(1500)

    ChrTalk(
        0xD,
        "#115F#5P那么……\x02",
    )

    CloseMessageWindow()
    OP_8E(0xD, 0xBDF2, 0xFFFFF448, 0x72AD, 0x7D0, 0x0)

    ChrTalk(
        0xD,
        (
            "#110F#5P游击士协会的各位，\x01",
            "刚才我的同僚说了些失礼的话。\x02\x03",
            "请允许我代他们说声抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F没什么，您太客气了。\x02\x03",
            "其实我们也有失言的地方，\x01",
            "这次就算扯平了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#110F#5P你这么说是最好不过了。\x02\x03",
            "……我之前也说过，\x01",
            "军队和协会向来就存在合作关系。\x02\x03",
            "而作为王国的重要组织，\x01",
            "两者的关系更是互不可缺。\x02\x03",
            "对于最近发生的一系列事件，\x01",
            "我十分期待你们会有出色的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F呵呵，我们会更加努力，\x01",
            "一定不会让您失望的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F（看、看起来……\x01",
            "　是个超级正派的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（嗯……他是谁呢？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#181F上校……\x01",
            "已经到时间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#113F#5P噢，是吗。\x02\x03",
            "#110F那么各位……\x01",
            "我这就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    OP_8E(0xD, 0xBDF2, 0xFFFFF448, 0x7611, 0x7D0, 0x0)
    Sleep(400)

    ChrTalk(
        0xD,
        (
            "#115F#5P……啊，对了。\x01",
            "我还没有报上名字。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)
    Sleep(400)

    NpcTalk(
        0xD,
        "理查德上校",
        (
            "#110F#5P王国军上校，理查德。\x02\x03",
            "如果有什么事情不妨和我联系。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_8C(0xD, 0, 400)

    def lambda_1923():
        OP_8E(0xD, 0xBDF2, 0x0, 0x99DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1923)
    Sleep(900)
    OP_8C(0xE, 0, 400)

    def lambda_194A():
        OP_8E(0xE, 0xBA4C, 0x0, 0x99DE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_194A)
    OP_21()
    OP_1E()
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    ChrTalk(
        0x101,
        (
            "#505F理查德上校……\x01",
            "好像在哪听过这个名字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，奈尔先生提过这个人。\x02\x03",
            "王国军情报部的负责人，\x01",
            "据说是位十分能干的年轻将校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#506F啊，这样啊☆\x02\x03",
            "#006F不过，以军人来讲，\x01",
            "也算是一位通情达理的人物呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F嗯，年纪才三十出头，\x01",
            "长相也十分之帅气哦。\x02\x03",
            "比起军人，更适合成为政治家吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 55617, -2500, 33010, 270)
    SetChrPos(0x10, 55617, -2500, 33010, 270)

    NpcTalk(
        0xF,
        "男人的声音",
        "#3P喂，你们几个。\x02",
    )

    CloseMessageWindow()

    def lambda_1BDF():
        OP_6D(49974, -3000, 30500, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1BDF)

    def lambda_1BF7():

        label("loc_1BF7")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_1BF7")

    QueueWorkItem2(0x0, 1, lambda_1BF7)

    def lambda_1C08():

        label("loc_1C08")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_1C08")

    QueueWorkItem2(0x1, 1, lambda_1C08)

    def lambda_1C19():

        label("loc_1C19")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_1C19")

    QueueWorkItem2(0x2, 1, lambda_1C19)

    def lambda_1C2A():

        label("loc_1C2A")

        TurnDirection(0xFE, 0xF, 0)
        OP_48()
        Jump("loc_1C2A")

    QueueWorkItem2(0x3, 1, lambda_1C2A)

    def lambda_1C3B():
        OP_8E(0xFE, 0xC45E, 0xFFFFF448, 0x7A19, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C3B)
    ClearChrFlags(0x10, 0x80)
    Sleep(500)

    def lambda_1C60():
        OP_8E(0xFE, 0xC8DC, 0xFFFFF448, 0x78E9, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1C60)
    OP_62(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xF, 0x1)
    TurnDirection(0xF, 0x101, 400)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(
        0xF,
        (
            "#140F刚才穿黑衣服的军人是谁啊？\x02\x03",
            "这身打扮好像在哪见过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#3P难道你没见过他吗？\x02\x03",
            "他就是你之前提到的那个\x01",
            "掌管情报部的理查德上校啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#143F什、什么————？\x02\x03",
            "喂喂，这是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F#3P嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F#3P他本人亲口报上自己的名字，\x01",
            "我想应该不会有错的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#141F没想到能在这种地方\x01",
            "碰到如此难得一见的人物。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(
        0xF,
        (
            "#144F这机会绝对不能放过！\x01",
            "朵洛希，我们赶快去追上他！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(
        0x10,
        (
            "#151F好啊好啊～！\x01",
            "虽然不清楚怎么回事～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FEA():
        OP_8E(0xF, 0xBAA4, 0x0, 0x99DE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1FEA)
    Sleep(300)
    OP_8E(0x10, 0xBAA4, 0x0, 0x99DE, 0x1770, 0x0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    ChrTalk(
        0x101,
        (
            "#008F#3P啊，还真有干劲啊～\x01",
            "又要去采访了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#021F#4P呵呵，要做报道的话，\x01",
            "的确就要首选这样的重要人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#032F#4P……唔………\x02",
    )

    CloseMessageWindow()
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    def lambda_211B():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_211B)

    def lambda_2129():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2129)

    def lambda_2137():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2137)

    def lambda_2145():
        OP_6D(48950, -3000, 29000, 1200)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2145)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#004F嗯？怎么了？\x01",
            "你会这么认真地板着脸还真是稀奇啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#032F#2P没什么，刚才那位上校……\x02\x03",
            "的确是相当有男子气概，\x01",
            "这一点我绝对不吝否认。\x02\x03",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F不过……怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 225, 400)
    OP_62(0x104, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    ChrTalk(
        0x104,
        (
            "#031F#2P不过想要达到我这种境界，\x01",
            "还要继续修行才行哦。\x02\x03",
            "期待他有更精彩的演出。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#007F又开始自我陶醉了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#019F这种自信到底是从哪涌出来的呢？\x01",
            "真有点不可思议啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104)

    ChrTalk(
        0x103,
        (
            "#020F呵呵，好了……\x02\x03",
            "既然士兵都撤走了，\x01",
            "我们就继续展开调查吧。\x02\x03",
            "刚才没办法和那些住户交谈，\x01",
            "我们再回去打听一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F嗯，明白。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_24E4")

    Return()

    # Function_10_873 end

    def Function_11_24E5(): pass

    label("Function_11_24E5")

    OP_8E(0xFE, 0xCE6C, 0xFFFFF448, 0x70AC, 0x1388, 0x0)
    OP_8E(0xFE, 0xDB2C, 0xFFFFFB1E, 0x70E9, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_24E5 end

    def Function_12_2513(): pass

    label("Function_12_2513")

    EventBegin(0x0)
    OP_6D(44480, -3000, 27780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 43850, -3000, 27070, 45)
    SetChrPos(0x102, 45240, -3000, 27130, 270)
    SetChrPos(0x103, 45170, -3000, 28450, 225)
    SetChrPos(0x104, 43750, -3000, 28620, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#020F虽然这起强盗事件\x01",
            "暂时还没有什么重要的线索……\x02\x03",
            "不过却听到了很耐人寻味的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F嗯，同感。\x02\x03",
            "特别是\x01",
            "『旅馆的饭菜美味』那一句。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#007F不是这句话吧。\x02\x03",
            "#000F不过，我听说那里能钓鱼时，\x01",
            "也觉得心里痒痒的……\x02\x03",
            "但既然没出什么事件，\x01",
            "也就没有调查的价值了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#015F不，我的意见正好相反。\x02\x03",
            "因为发生案件的场所\x01",
            "绝对会受到军队的彻底调查。\x02\x03",
            "所以空贼反而应该挑那些\x01",
            "风平浪静之处作为活动场所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F对啊……\x01",
            "这种说法也很有道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#022F的确这一连串的事件……\x02\x03",
            "先不说军队里是否有间谍，\x01",
            "那些空贼的慎密行事也让人捉摸不透。\x02\x03",
            "我想只靠调查现有案件的话，\x01",
            "要找到他们的藏身之处相当困难。\x02\x03",
            "既然他们有可能在旅馆出现，\x01",
            "那么我们也就有必要走一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F原来是这样啊……\x01",
            "与其守株待兔，不如先发制人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#035F赞成，那我们出发吧……\x02\x03",
            "被誉为利贝尔的珍珠——\x01",
            "美丽的瓦雷利亚湖，我们来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0xD, 0x0, 0xFFFF)
    OP_1B(0x0, 0x0, 0xFFFF)
    OP_1B(0x1, 0x0, 0xFFFF)
    OP_1B(0x2, 0x0, 0xFFFF)
    EventEnd(0x0)
    Return()

    # Function_12_2513 end

    def Function_13_2AED(): pass

    label("Function_13_2AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D16")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B11")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2B18")

    label("loc_2B11")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_2BC3")

    ChrTalk(
        0x103,
        (
            "#027F现在去其他地方调查\x01",
            "也是没有用的。\x02\x03",
            "先听听刚才没有问过的居民\x01",
            "是怎么说的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC0")

    label("loc_2BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6F")
    OP_A2(0x0)

    ChrTalk(
        0x103,
        (
            "#020F还没有得到\x01",
            "重要的情报呢。\x02\x03",
            "继续在这一带\x01",
            "打听打听消息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC0")

    label("loc_2C6F")


    ChrTalk(
        0x103,
        (
            "#020F好了，\x01",
            "赶快继续打听情报吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC0")

    Fade(1000)
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    SetChrPos(0x3, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x2)
    Jump("loc_2EAC")

    label("loc_2D16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x33)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DC9")
    EventBegin(0x2)
    TurnDirection(0x134, 0x0, 400)

    ChrTalk(
        0x134,
        (
            "#620F各位要到哪里去呢？\x01",
            "　\x02\x03",
            "市长应该就在\x01",
            "柏斯超市视察。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    SetChrPos(0x3, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x2)
    Jump("loc_2EAC")

    label("loc_2DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EAC")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE9")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2DF0")

    label("loc_2DE9")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2DF0")


    ChrTalk(
        0x103,
        (
            "#020F先回协会支部\x01",
            "确认一下现在的状况吧。\x02\x03",
            "柏斯支部在北街区。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrPos(0x0, 47790, -3000, 17080, 0)
    SetChrPos(0x1, 47790, -3000, 17080, 0)
    SetChrPos(0x2, 47790, -3000, 17080, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x2)

    label("loc_2EAC")

    Return()

    # Function_13_2AED end

    def Function_14_2EAD(): pass

    label("Function_14_2EAD")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC5")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2ECC")

    label("loc_2EC5")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 1)), scpexpr(EXPR_END)), "loc_2F77")

    ChrTalk(
        0x103,
        (
            "#027F现在去其他地方调查\x01",
            "也是没有用的。\x02\x03",
            "先听听刚才没有问过的居民\x01",
            "是怎么说的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3074")

    label("loc_2F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3023")
    OP_A2(0x0)

    ChrTalk(
        0x103,
        (
            "#020F还没有得到\x01",
            "重要的情报呢。\x02\x03",
            "继续在这一带\x01",
            "打听打听消息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3074")

    label("loc_3023")


    ChrTalk(
        0x103,
        (
            "#020F好了，\x01",
            "赶快继续打听情报吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3074")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_2EAD end

    def Function_15_3090(): pass

    label("Function_15_3090")

    SetPlaceName(0x22) # 鲁希尔工房
    Return()

    # Function_15_3090 end

    def Function_16_3094(): pass

    label("Function_16_3094")

    SetPlaceName(0x24) # 鲁希尔工房
    Return()

    # Function_16_3094 end

    SaveToFile()

Try(main)
