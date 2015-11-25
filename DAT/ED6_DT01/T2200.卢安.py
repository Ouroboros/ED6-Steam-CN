from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2200   ._SN',
            'ED6_DT01/T2200_1 ._SN',
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
        '戴尔蒙市长',                           # 9
        '奈尔',                                 # 10
        '照相机',                               # 11
        '谜之男人\u3000※仮',                   # 12
        '盖尔多那',                             # 13
        ' ',                                    # 14
        ' ',                                    # 15
        '卢安市·南街区',                       # 16
    )

    DeclEntryPoint(
        Unknown_00              = 88000,
        Unknown_04              = 0,
        Unknown_08              = 22000,
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
        'ED6_DT07/CH02410 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH00005 ._CH',             # 03
        'ED6_DT07/CH00015 ._CH',             # 04
        'ED6_DT07/CH00045 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02410P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH00005P._CP',             # 03
        'ED6_DT07/CH00015P._CP',             # 04
        'ED6_DT07/CH00045P._CP',             # 05
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 111500,
        Z                   = 11000,
        Y                   = 15700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 98500,
        Z                   = 0,
        Y                   = 17600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 68010,
        Z                   = 0,
        Y                   = 21970,
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


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_2A1",          # 01, 1
        "Function_2_2B9",          # 02, 2
        "Function_3_2CF",          # 03, 3
        "Function_4_371",          # 04, 4
        "Function_5_65C",          # 05, 5
        "Function_6_67A",          # 06, 6
        "Function_7_915",          # 07, 7
        "Function_8_E06",          # 08, 8
        "Function_9_10D1",         # 09, 9
        "Function_10_11D5",        # 0A, 10
        "Function_11_12B6",        # 0B, 11
        "Function_12_13B1",        # 0C, 12
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1F5")
    SetChrPos(0xC, 96920, 0, 18630, 90)
    Jump("loc_243")

    label("loc_1F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_210")
    SetChrPos(0xC, 96920, 0, 18630, 90)
    Jump("loc_243")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_22B")
    SetChrPos(0xC, 96920, 0, 18630, 90)
    Jump("loc_243")

    label("loc_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_243")
    SetChrPos(0xC, 96920, 0, 18630, 90)

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_25A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 7)

    label("loc_25A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_26A"),
        (101, "loc_280"),
        (SWITCH_DEFAULT, "loc_2A0"),
    )


    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27D")
    OP_A2(0x43F)
    Event(0, 6)

    label("loc_27D")

    Jump("loc_2A0")

    label("loc_280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29D")
    OP_A3(0x3FC)
    Event(1, 0)

    label("loc_29D")

    Jump("loc_2A0")

    label("loc_2A0")

    Return()

    # Function_0_1DA end

    def Function_1_2A1(): pass

    label("Function_1_2A1")

    OP_16(0x2, 0xFA0, 0xFFFFC180, 0xFFFE5A20, 0x3004A)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_2A1 end

    def Function_2_2B9(): pass

    label("Function_2_2B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B9")

    label("loc_2CE")

    Return()

    # Function_2_2B9 end

    def Function_3_2CF(): pass

    label("Function_3_2CF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_370")
    OP_8E(0xFE, 0x181E6, 0x0, 0x4A60, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x180C4, 0x0, 0x44C0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x17B10, 0x0, 0x42CC, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x17A98, 0x0, 0x48C6, 0xBB8, 0x0)
    OP_8C(0xFE, 120, 400)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xC)
    Jump("Function_3_2CF")

    label("loc_370")

    Return()

    # Function_3_2CF end

    def Function_4_371(): pass

    label("Function_4_371")

    TalkBegin(0xC)
    OP_63(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3D9")

    ChrTalk(
        0xFE,
        (
            "我可是一直在这里\x01",
            "勤勤恳恳地工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "这下薪水该怎么办呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_658")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_450")

    ChrTalk(
        0xFE,
        (
            "刚才，\x01",
            "有一个看起来很了不起的大叔来过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然看起来很了不起，\x01",
            "但是他的发型很奇怪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_658")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_51E")

    ChrTalk(
        0xFE,
        (
            "我总觉得最近这里\x01",
            "有许多显赫人物进进出出啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "经常有打扮高雅的人\x01",
            "从这里经过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_658")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_563")

    ChrTalk(
        0xFE,
        "已经到这个时候啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我觉得肚子有点饿了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_658")

    label("loc_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_5C4")

    ChrTalk(
        0xFE,
        (
            "听说那座铜像是\x01",
            "戴尔蒙家族第一代的主人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "好威猛啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_658")

    label("loc_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_END)), "loc_658")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629")
    OP_A2(0x0)

    ChrTalk(
        0xFE,
        "哦，有事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我呀，是个园丁。\x01",
            "有问题吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_658")

    label("loc_629")


    ChrTalk(
        0xFE,
        (
            "我呀，是个园丁。\x01",
            "有问题吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_658")

    TalkEnd(0xC)
    Return()

    # Function_4_371 end

    def Function_5_65C(): pass

    label("Function_5_65C")

    OP_A2(0x3FB)

    ChrTalk(
        0x102,
        "#010F设立标志\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_5_65C end

    def Function_6_67A(): pass

    label("Function_6_67A")

    EventBegin(0x0)
    SetChrPos(0x101, 82220, 0, 22710, 90)
    SetChrPos(0x102, 82680, 0, 21320, 90)
    SetChrPos(0x105, 81500, 0, 21870, 90)
    OP_6D(120230, 1900, 24150, 0)
    OP_67(0, 6040, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(79000, 0)
    OP_6E(261, 0)
    StopSound(0x9470, 0x30D40, 0x0)
    FadeToBright(1000, 0)

    def lambda_708():
        OP_6D(82030, 0, 22110, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_708)

    def lambda_720():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_720)
    Sleep(2000)

    def lambda_735():
        OP_67(0, 9500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_735)

    def lambda_74D():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_74D)
    StopSound(0x9470, 0x186A0, 0x1F40)
    Sleep(8000)

    ChrTalk(
        0x101,
        (
            "#007F话说回来，还真是好大的房子啊～\x02\x03",
            "#009F果然要坏事做尽，\x01",
            "才能住得起这样的房子吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F我想和这应该没什么关系……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#047F毕竟戴尔蒙家族\x01",
            "曾经是王国的豪门贵族。\x02\x03",
            "这座官邸也应该是\x01",
            "历代主人所继承的产业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F是吗……\x01",
            "的确，屋子本身并没有罪。\x02\x03",
            "#006F算了，不管这些了。\x01",
            "总之要先好好盘问那个市长。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_6_67A end

    def Function_7_915(): pass

    label("Function_7_915")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6D(116010, 2150, 30790, 0)
    OP_6C(225000, 0)
    OP_6B(3510, 0)
    SetChrPos(0xE, 110390, -3000, 39780, 90)
    SetChrFlags(0xE, 0x40)
    OP_A1(0xE, 0x2)
    OP_72(0x2, 0x4)
    OP_72(0x2, 0x2)
    OP_71(0x2, 0x40)
    SetChrPos(0xD, 111540, -3000, 42790, 90)
    SetChrFlags(0xD, 0x40)
    OP_A1(0xD, 0x3)
    OP_72(0x3, 0x4)
    OP_72(0x3, 0x2)
    OP_71(0x3, 0x40)
    OP_43(0x8, 0x1, 0x0, 0x8)
    OP_72(0x4, 0x10)
    OP_70(0x4, 0x1E)
    OP_73(0x4)
    OP_6D(114850, 0, 36610, 4000)

    def lambda_A01():
        OP_6D(114500, -1800, 40890, 4500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A01)
    OP_43(0x101, 0x1, 0x0, 0x9)
    Sleep(600)
    OP_43(0x102, 0x1, 0x0, 0xA)
    Sleep(600)
    OP_43(0x105, 0x1, 0x0, 0xB)
    Sleep(2300)
    OP_4A(0x101, 1)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x101, 270, 0)
    OP_4A(0x102, 1)
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x102, 270, 0)
    Sleep(300)
    OP_4A(0x105, 1)
    OP_51(0x105, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x105, 270, 0)

    ChrTalk(
        0x101,
        "#580F#5P那、那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#046F是戴尔蒙市长的帆船！\x02",
    )

    CloseMessageWindow()
    OP_4B(0x8, 1)

    ChrTalk(
        0x101,
        "#005F#5P给、给我等一下！\x02",
    )

    CloseMessageWindow()
    OP_4B(0x102, 1)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#016F开这条小船去追吧！\x02\x03",
            "快，你们两个也上来！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B45():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B45)
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(
        0x105,
        "#006F#5P#1KＯＫ！\x02",
    )


    ChrTalk(
        0x101,
        "#042F#6P#1K好的！\x02",
    )

    Sleep(500)
    OP_56(0x1)
    OP_59()

    def lambda_B94():

        label("loc_B94")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_B94")

    QueueWorkItem2(0x102, 1, lambda_B94)

    def lambda_BA5():
        OP_6D(111020, -1800, 41170, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BA5)
    OP_4B(0x101, 1)
    Sleep(600)
    OP_4B(0x105, 1)
    OP_43(0x9, 0x1, 0x0, 0xC)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    OP_44(0x102, 0xFF)
    OP_8C(0x102, 90, 400)
    SetChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 4)
    Sleep(300)

    def lambda_BF5():
        OP_6D(107720, -2420, 42540, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BF5)
    OP_22(0x92, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0xD, 0, -300, -1800, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 240)
    OP_70(0x3, 0x12C)

    def lambda_C5A():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_C5A)
    Sleep(300)

    def lambda_C7A():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_C7A)
    OP_73(0x3)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 301)
    OP_70(0x3, 0x168)
    PlayEffect(0x4, 0xFF, 0xD, 0, 50, 2700, 180, 0, 0, 1200, 500, 5000, 0xFF, 0, 0, 0, 0)

    def lambda_CE0():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_CE0)
    Sleep(200)

    def lambda_D00():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_D00)
    Sleep(200)

    def lambda_D20():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_D20)
    Sleep(200)

    def lambda_D40():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_D40)
    Sleep(200)

    def lambda_D60():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_D60)
    Sleep(200)

    def lambda_D80():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_D80)
    Sleep(200)

    def lambda_DA0():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_DA0)
    Sleep(200)

    def lambda_DC0():
        OP_8F(0xD, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_DC0)

    ChrTalk(
        0x9,
        (
            "#144F#5P喂———！\x01",
            "让我也一起去呀～！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3F0)
    NewScene("ED6_DT01/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_915 end

    def Function_8_E06(): pass

    label("Function_8_E06")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_E1C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_E1C)
    SetChrPos(0xFE, 115970, 2150, 29130, 0)
    OP_8E(0xFE, 0x1C502, 0x866, 0x79C2, 0x1770, 0x0)
    OP_8E(0xFE, 0x1B788, 0x0, 0x79C2, 0x1770, 0x0)
    OP_8E(0xFE, 0x1B74C, 0x0, 0x7FE4, 0x1770, 0x0)
    OP_8E(0xFE, 0x1C8EA, 0x0, 0x84E4, 0x1770, 0x0)
    OP_8E(0xFE, 0x1C8EA, 0xFFFFF8F8, 0x902E, 0x1770, 0x0)
    OP_8E(0xFE, 0x1BD6E, 0xFFFFF8F8, 0x9C22, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 0)
    OP_96(0xFE, 0x1B67A, 0xFFFFF4A2, 0x9AF6, 0x3E8, 0x1770)
    SetChrBattleFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x4)
    OP_89(0xFE, 112250, 3000, 39670, 270)
    OP_8C(0xFE, 90, 400)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    OP_22(0x92, 0x0, 0x64)
    PlayEffect(0x5, 0xFF, 0xE, 0, -300, -3000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 240)
    OP_70(0x2, 0x12C)

    def lambda_F55():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_F55)
    Sleep(300)

    def lambda_F75():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_F75)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 301)
    OP_70(0x2, 0x168)
    PlayEffect(0x4, 0xFF, 0xE, 0, 50, 2700, 180, 0, 0, 1200, 500, 5000, 0xFF, 0, 0, 0, 0)

    def lambda_FDB():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_FDB)
    Sleep(200)

    def lambda_FFB():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_FFB)
    Sleep(200)

    def lambda_101B():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_101B)
    Sleep(200)

    def lambda_103B():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_103B)
    Sleep(200)

    def lambda_105B():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_105B)
    Sleep(200)

    def lambda_107B():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_107B)
    Sleep(200)

    def lambda_109B():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_109B)
    Sleep(200)

    def lambda_10BB():
        OP_8F(0xE, 0x12D5E, 0xFFFFF448, 0x9BA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_10BB)
    Return()

    # Function_8_E06 end

    def Function_9_10D1(): pass

    label("Function_9_10D1")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_10E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_10E7)
    SetChrPos(0xFE, 115970, 2150, 29130, 0)
    OP_8E(0xFE, 0x1C53E, 0x866, 0x7BF2, 0x1770, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0x1C494, 0x0, 0x80DE, 0x5DC, 0x1388)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x1C8EA, 0x0, 0x84E4, 0x1388, 0x0)
    OP_8E(0xFE, 0x1C8EA, 0xFFFFF8F8, 0x902E, 0x1388, 0x0)
    OP_8E(0xFE, 0x1C0A2, 0xFFFFF8F8, 0x9C22, 0x1388, 0x0)
    OP_8C(0x101, 270, 0)
    Sleep(800)
    OP_8E(0xFE, 0x1BE7C, 0xFFFFF8F8, 0xAE6A, 0x1388, 0x0)
    OP_8E(0xFE, 0x1B260, 0xFFFFF8F8, 0xAE6A, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0x1AC70, 0xFFFFF56A, 0xA73A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_9_10D1 end

    def Function_10_11D5(): pass

    label("Function_10_11D5")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_11EB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11EB)
    SetChrPos(0xFE, 115970, 2150, 29130, 0)
    OP_8E(0xFE, 0x1C53E, 0x866, 0x7BF2, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0x1C494, 0x0, 0x80DE, 0x5DC, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x1C8EA, 0x0, 0x84E4, 0x1388, 0x0)
    OP_8E(0xFE, 0x1C8EA, 0xFFFFF8F8, 0x902E, 0x1388, 0x0)
    OP_8E(0xFE, 0x1C46C, 0xFFFFF8F8, 0xA3CA, 0x1388, 0x0)
    OP_8E(0xFE, 0x1BE36, 0xFFFFF8F8, 0xA6E0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 270, 0)
    OP_96(0xFE, 0x1B544, 0xFFFFF510, 0xA6E0, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_11D5 end

    def Function_11_12B6(): pass

    label("Function_11_12B6")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_12CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_12CC)
    SetChrPos(0xFE, 115970, 2150, 29130, 0)
    OP_8E(0xFE, 0x1C53E, 0x866, 0x7BF2, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0x1C5DE, 0xAA0, 0x7CF6, 0x258, 0x1388)
    OP_96(0xFE, 0x1C494, 0x0, 0x80DE, 0x258, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0x1C8EA, 0x0, 0x84E4, 0x1388, 0x0)
    OP_8E(0xFE, 0x1C8EA, 0xFFFFF8F8, 0x902E, 0x1388, 0x0)
    OP_8E(0xFE, 0x1BE7C, 0xFFFFF8F8, 0xAE6A, 0x1388, 0x0)
    OP_8E(0xFE, 0x1B260, 0xFFFFF8F8, 0xAE6A, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_96(0xFE, 0x1B116, 0xFFFFF510, 0xA6E0, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 5)
    Return()

    # Function_11_12B6 end

    def Function_12_13B1(): pass

    label("Function_12_13B1")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_13C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_13C7)
    SetChrPos(0xFE, 115970, 2150, 29130, 0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x1C502, 0x866, 0x79C2, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1B788, 0x0, 0x79C2, 0xFA0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x1B74C, 0x0, 0x7FE4, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C8EA, 0x0, 0x84E4, 0xFA0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x1C8EA, 0xFFFFF8F8, 0x902E, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1BE36, 0xFFFFF8F8, 0xA6E0, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0x1B58)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0x1B58)
    Return()

    # Function_12_13B1 end

    SaveToFile()

Try(main)
