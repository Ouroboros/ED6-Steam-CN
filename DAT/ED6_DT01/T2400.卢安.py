from ED6ScenarioHelper import *

def main():
    # 卢安

    CreateScenaFile(
        FileName            = 'T2400   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '特蕾莎院长',                           # 9
        '达尼艾尔',                             # 10
        '玛丽',                                 # 11
        '克拉姆',                               # 12
        '基库',                                 # 13
        '目标用摄像机',                         # 14
        '鸡',                                   # 15
        '鸡',                                   # 16
        '鸡',                                   # 17
        '梅威海道方向',                         # 18
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
        'ED6_DT07/CH02590 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02570 ._CH',             # 03
        'ED6_DT07/CH02320 ._CH',             # 04
        'ED6_DT06/CH20051 ._CH',             # 05
        'ED6_DT07/CH00040 ._CH',             # 06
        'ED6_DT07/CH00041 ._CH',             # 07
        'ED6_DT07/CH01720 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02590P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02570P._CP',             # 03
        'ED6_DT07/CH02320P._CP',             # 04
        'ED6_DT06/CH20051P._CP',             # 05
        'ED6_DT07/CH00040P._CP',             # 06
        'ED6_DT07/CH00041P._CP',             # 07
        'ED6_DT07/CH01720P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 33500,
        Direction           = 180,
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
        X                   = 6000,
        Z                   = 200,
        Y                   = 22200,
        Direction           = 180,
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
        X                   = 5800,
        Z                   = 0,
        Y                   = 23600,
        Direction           = 180,
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
        X                   = 4300,
        Z                   = 200,
        Y                   = 22900,
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
        X                   = 800,
        Z                   = 6000,
        Y                   = -13810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 1060,
        Z                   = 0,
        Y                   = -23220,
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
        X                   = -1880,
        Y                   = 2000,
        Z                   = 4450,
        Range               = 2800,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x14B4,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_252",          # 00, 0
        "Function_1_2D9",          # 01, 1
        "Function_2_2EC",          # 02, 2
        "Function_3_302",          # 03, 3
        "Function_4_455",          # 04, 4
        "Function_5_4E1",          # 05, 5
        "Function_6_507",          # 06, 6
        "Function_7_1CE4",         # 07, 7
        "Function_8_1D31",         # 08, 8
        "Function_9_1DE5",         # 09, 9
        "Function_10_1E91",        # 0A, 10
        "Function_11_287F",        # 0B, 11
        "Function_12_28AA",        # 0C, 12
        "Function_13_28EE",        # 0D, 13
        "Function_14_2965",        # 0E, 14
        "Function_15_29DA",        # 0F, 15
    )


    def Function_0_252(): pass

    label("Function_0_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_25C")
    Jump("loc_28B")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_266")
    Jump("loc_28B")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_END)), "loc_270")
    Jump("loc_28B")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_27A")
    Jump("loc_28B")

    label("loc_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_284")
    Jump("loc_28B")

    label("loc_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_28B")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_299")
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_2B0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 14)

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_2C7")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 15)

    label("loc_2C7")

    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_252 end

    def Function_1_2D9(): pass

    label("Function_1_2D9")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE5A20, 0x30067)
    Return()

    # Function_1_2D9 end

    def Function_2_2EC(): pass

    label("Function_2_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_301")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2EC")

    label("loc_301")

    Return()

    # Function_2_2EC end

    def Function_3_302(): pass

    label("Function_3_302")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, -8760, 13210, 8700, 24630, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_330")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_454")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_419")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2238), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x339A), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x21FC), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6036), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EE")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_3DB():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DB)
    Jump("loc_411")

    label("loc_3EE")


    def lambda_3F4():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F4)
    Sleep(200)

    label("loc_411")

    Sleep(30)
    Jump("loc_451")

    label("loc_419")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451")
    OP_44(0xFE, 0x2)

    def lambda_439():
        OP_8D(0xFE, -8760, 13210, 8700, 24630, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_439)

    label("loc_451")

    Jump("loc_330")

    label("loc_454")

    Return()

    # Function_3_302 end

    def Function_4_455(): pass

    label("Function_4_455")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E0")
    OP_43(0xFE, 0x2, 0x0, 0x5)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_4E0")
    TalkBegin(0xFE)
    OP_A2(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "新鲜鸡蛋\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_4E0")

    Return()

    # Function_4_455 end

    def Function_5_4E1(): pass

    label("Function_5_4E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_5_4E1")

    label("loc_4FC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_4E1 end

    def Function_6_507(): pass

    label("Function_6_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE3")
    OP_A2(0x410)
    EventBegin(0x0)
    TurnDirection(0xB, 0x9, 0)
    TurnDirection(0x9, 0xB, 0)
    TurnDirection(0xA, 0xB, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_563")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_57A")

    label("loc_563")

    OP_62(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_57A")


    def lambda_580():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_580)
    OP_6D(5200, 0, 22840, 2000)
    AddParty(0x35, 0xFF)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x136, 0x1)
    SetChrPos(0x101, -690, 0, 17260, 45)
    SetChrPos(0x102, -130, 0, 16010, 45)
    SetChrPos(0x136, 0, 0, 31800, 90)
    SetChrFlags(0x136, 0x80)

    ChrTalk(
        0xA,
        (
            "克拉姆，\x01",
            "你刚才到哪儿去了嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "科洛丝姐姐担心死了，\x01",
            "到处去找你呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#770F嘿嘿，用不着担心。\x02\x03",
            "今天我可是有大收获哦～\x01",
            "弄到了一个超～棒的东西呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "是什么啊？给我们看看吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#771F嘿嘿嘿，看了可别吃惊哦～\x02\x03",
            "这东西是我从一个没头脑的\x01",
            "大姐头身上弄过来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "……你说谁没头脑啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#774F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_749():

        label("loc_749")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_749")

    QueueWorkItem2(0x101, 2, lambda_749)

    def lambda_75A():

        label("loc_75A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_75A")

    QueueWorkItem2(0x102, 2, lambda_75A)

    def lambda_76B():

        label("loc_76B")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_76B")

    QueueWorkItem2(0xB, 1, lambda_76B)

    def lambda_77C():

        label("loc_77C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_77C")

    QueueWorkItem2(0x9, 1, lambda_77C)

    def lambda_78D():

        label("loc_78D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_78D")

    QueueWorkItem2(0xA, 1, lambda_78D)

    def lambda_79E():
        OP_8E(0xFE, 0x654, 0x0, 0x56E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_79E)

    def lambda_7B9():
        OP_8E(0xFE, 0x618, 0x0, 0x5276, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B9)
    TurnDirection(0xB, 0x101, 400)
    OP_6D(3750, 0, 22850, 1000)
    WaitChrThread(0x101, 0x1)
    OP_95(0xB, 0x0, 0x0, 0x0, 0x3E8, 0x2710)
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0xB, 0xB4, 0x1F4, 0xBB8, 0x0)

    ChrTalk(
        0xB,
        "#774F你、你们怎么会来这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F哼哼哼。\x01",
            "你也太小看我们游击士了吧？\x02\x03",
            "像你这种淘气的调皮蛋一翘起尾巴，\x01",
            "姐姐我就知道你有什么坏主意！\x01",
            "更何况是找到你住在哪里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#772F可、可恶……\x01",
            "乖乖等你捉的是小狗！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xB, 0x15F4, 0x64, 0x52F8, 0x1B58, 0x0)
    OP_8E(0xB, 0x2468, 0xC8, 0x529E, 0x1B58, 0x0)
    OP_8E(0xB, 0x21CA, 0xFFFFFF38, 0x4AA6, 0x1B58, 0x0)

    ChrTalk(
        0x101,
        "#005F喂！给我站住！\x02",
    )

    CloseMessageWindow()

    def lambda_96D():
        OP_6D(5748, -175, 18851, 1000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_96D)

    def lambda_985():
        OP_8E(0xFE, 0x166C, 0x0, 0x50B4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_985)

    def lambda_9A0():
        OP_96(0xFE, 0x18EC, 0xFFFFFF38, 0x42A4, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9A0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xB, 0x1)
    OP_8E(0x102, 0x10CC, 0xC8, 0x5974, 0xBB8, 0x0)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x3E8)
    OP_6A(0xD)
    OP_43(0x101, 0x1, 0x0, 0x9)
    OP_43(0xB, 0x1, 0x0, 0x8)
    OP_43(0x102, 0x1, 0x0, 0x7)
    WaitChrThread(0x102, 0x1)
    Sleep(1800)
    Fade(1000)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    TurnDirection(0x9, 0x102, 0)
    TurnDirection(0xA, 0x102, 0)
    OP_6A(0x0)
    ClearMapFlags(0x1)
    OP_6D(4800, 185, 22555, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "那个，大哥哥……\x01",
            "这是怎么回事呀？\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x40)
    SetChrPos(0x101, -4998, 0, 29194, 0)
    SetChrPos(0xB, -1998, 0, 29194, 0)

    def lambda_AC4():
        OP_8E(0xFE, 0x2818, 0x0, 0x7D00, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AC4)

    def lambda_ADF():
        OP_8E(0xFE, 0x256C, 0x0, 0x7C06, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ADF)

    ChrTalk(
        0x9,
        (
            "难道克拉姆\x01",
            "又恶作剧了吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    ChrTalk(
        0x102,
        (
            "#019F啊，那个……\x01",
            "来打扰你们真是不好意思了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 8300, 200, 31590, 90)
    SetChrPos(0x101, 7700, 0, 31590, 90)

    def lambda_B8E():

        label("loc_B8E")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_B8E")

    QueueWorkItem2(0xB, 1, lambda_B8E)

    ChrTalk(
        0xB,
        (
            "#776F#4P我不要～！\x01",
            "放开我！快点放开我～！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)

    def lambda_BD2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BD2)

    def lambda_BE0():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE0)

    def lambda_BEE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BEE)
    OP_6D(8880, 0, 32490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xB,
        "#776F#2P我要去告发你虐待儿童！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F#3P什～什么虐待儿童啊？\x01",
            "小小年纪竟然说出这种话来！\x02\x03",
            "我的徽章呢？\x01",
            "马上还给我！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#776F#2P说我拿了你的东西，\x01",
            "你有证据吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F#3P证据倒是没有……\x01",
            "不过，让我调查一下就知道了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D49():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D49)
    OP_97(0xB, 0x1E5A, 0x7B66, 0x2BF20, 0xFA0, 0x3)
    OP_44(0xB, 0xFF)
    SetChrSubChip(0xB, 0)
    OP_9E(0xB, 0x1E, 0x0, 0x190, 0x1388)

    ChrTalk(
        0xB,
        (
            "#778F#3P哎呀呀……！\x02\x03",
            "你、你在摸哪里啊！？\x01",
            "好～痒～痒～啊！\x02\x03",
            "大变态！粗暴女！\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xB, 0x1E, 0x0, 0x258, 0x1388)

    ChrTalk(
        0x101,
        (
            "#006F#2P行啦行啦，反抗是没有用的，\x01",
            "还是乖乖地交出来吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x10)
    OP_6F(0x0, 20)
    SetChrPos(0x136, 10, 0, 30720, 90)
    ClearChrFlags(0x136, 0x80)

    NpcTalk(
        0x136,
        "女孩的声音",
        "#2P基库！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_6D(9390, 0, 34800, 800)
    Sleep(500)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, 0, 6000, 31900, 0)
    OP_22(0x8C, 0x0, 0x64)
    OP_8E(0xC, 0x1E14, 0x2BC, 0x7B66, 0x4E20, 0x0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_EDE():
        OP_95(0xFE, 0x12C, 0x0, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EDE)

    def lambda_EFC():
        OP_95(0xFE, 0x12C, 0x0, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_EFC)
    OP_8E(0xC, 0x36A6, 0x1770, 0x8278, 0x4E20, 0x0)

    ChrTalk(
        0x101,
        (
            "#004F#2P哇哇～！？\x02\x03",
            "刚、刚才那个东西是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F5D():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F5D)

    def lambda_F6B():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F6B)

    def lambda_F79():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F79)

    def lambda_F87():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F87)

    def lambda_F95():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F95)

    def lambda_FA3():
        OP_6D(3420, 0, 32210, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_FA3)

    def lambda_FBB():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_FBB)

    def lambda_FCB():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_FCB)
    WaitChrThread(0x0, 0x2)
    OP_92(0xC, 0x136, 0x1388, 0x2710, 0x0)
    OP_92(0xC, 0x136, 0xFA0, 0x1F40, 0x0)
    OP_92(0xC, 0x136, 0xBB8, 0x1770, 0x0)
    OP_92(0xC, 0x136, 0x7D0, 0xBB8, 0x0)
    OP_8E(0xC, 0xA, 0x3E8, 0x7B0C, 0x5DC, 0x0)

    def lambda_102C():
        OP_8C(0xFE, 135, 200)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_102C)
    SetChrChipByIndex(0x136, 5)
    SetChrSubChip(0x136, 3)
    OP_8F(0xC, 0xFFFFFFCE, 0xC8, 0x7ADA, 0x3E8, 0x0)
    WaitChrThread(0xC, 0x3)
    Sleep(100)
    Fade(250)
    SetChrFlags(0xC, 0x80)
    SetChrSubChip(0x136, 1)
    SetChrFlags(0x136, 0x20)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x136,
        "穿制服的少女",
        (
            "#046F请放了那个孩子！\x02\x03",
            "如果再对他动粗的话，\x01",
            "就别怪我不客……\x02\x03",
            "#044F………………哎呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊，你不就是……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x136,
        "穿制服的少女",
        "#044F在玛诺利亚村见过的……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "白隼",
        "#310F#1P啾？\x02",
    )

    CloseMessageWindow()
    OP_96(0xB, 0x1A40, 0x0, 0x7B0C, 0x1F4, 0x1388)
    ClearChrFlags(0xB, 0x4)
    OP_8E(0xB, 0x15EA, 0x0, 0x7BD4, 0x1B58, 0x0)

    ChrTalk(
        0xB,
        (
            "#775F救救我……科洛丝姐姐！\x02\x03",
            "我、我什么事情也没干，\x01",
            "这姐姐就无缘无故地把我抓住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#005F什、什么事情也没干？\x01",
            "明明就是你把我的徽章给偷走的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "#770F#1P嘿嘿，证据呢？\x01",
            "有本事就拿出证据来！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1254():
        OP_8E(0xFE, 0x17B6, 0x0, 0x7C9C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1254)
    Sleep(200)
    OP_8F(0xB, 0x1194, 0x0, 0x78D2, 0x1388, 0x0)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(
        0xB,
        "#774F#1P啊，可不要再挠我痒痒了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F你这个调皮蛋……\x02",
    )

    CloseMessageWindow()

    def lambda_12CD():
        OP_6D(2050, 0, 30810, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12CD)

    def lambda_12E5():
        OP_8E(0xFE, 0xADC, 0x0, 0x6EC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12E5)
    Sleep(300)

    def lambda_1305():
        OP_8E(0xFE, 0x1040, 0x0, 0x6F7C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1305)
    Sleep(400)

    def lambda_1325():
        OP_8E(0xFE, 0x384, 0x0, 0x71D4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1325)
    Sleep(300)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x136, 0)

    ChrTalk(
        0x102,
        "#010F你好，我们又见面了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x136, 135, 400)

    ChrTalk(
        0x136,
        (
            "#045F啊，上次给你们添麻烦了……\x02\x03",
            "刚才真不好意思，\x01",
            "我还以为是强盗……\x02\x03",
            "#043F啊，对了……\x01",
            "究竟发生了什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "科洛丝姐姐，\x01",
            "不用问也能猜到啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "肯定是克拉姆\x01",
            "又惹出什么祸来了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)

    ChrTalk(
        0x9,
        (
            "嗯……姐姐～\x01",
            "苹果派做好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F啊，再等一下好吗，\x01",
            "苹果派要烤一下才能吃的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F这个臭小鬼！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#776F#1P粗暴女！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "克拉姆你也真是的。\x01",
            "什么时候才能不这么孩子气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "苹果派，好了没有啊～\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x136, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#019F……总觉得\x01",
            "情况好像变得越来越复杂了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#045F啊，呵呵……\x01",
            "我也觉得是呢……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "白隼",
        "#311F#2P啾。\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "女性的声音",
        (
            "#3P哎呀哎呀～\x01",
            "怎么外面这么吵呢……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x0, 0x0, 0x7C38, 0x5DC, 0x0)
    OP_8C(0x8, 90, 400)

    def lambda_1635():

        label("loc_1635")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1635")

    QueueWorkItem2(0xB, 1, lambda_1635)

    def lambda_1646():

        label("loc_1646")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1646")

    QueueWorkItem2(0x9, 1, lambda_1646)

    def lambda_1657():

        label("loc_1657")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1657")

    QueueWorkItem2(0xA, 1, lambda_1657)

    def lambda_1668():

        label("loc_1668")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1668")

    QueueWorkItem2(0x101, 1, lambda_1668)

    def lambda_1679():

        label("loc_1679")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_1679")

    QueueWorkItem2(0x102, 1, lambda_1679)

    def lambda_168A():

        label("loc_168A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_168A")

    QueueWorkItem2(0x136, 1, lambda_168A)

    ChrTalk(
        0x136,
        "#044F特蕾莎老师！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#750F#1P虽然详细情况我不太清楚……\x02\x03",
            "不过看起来，\x01",
            "又是克拉姆做了什么恶作剧吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#772F才、才不会呢。\x01",
            "我可是什么都没干哦。\x02\x03",
            "老师你可不要听\x01",
            "这个粗暴的姐姐乱说话哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#009F谁、谁是粗暴的姐姐啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#750F#1P哎呀哎呀～真是伤脑筋。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xA14, 0x0, 0x771A, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)

    ChrTalk(
        0x8,
        (
            "#750F#1P克拉姆……\x01",
            "你真的什么都没有做吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#771F嗯，那当然啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#750F#1P你敢向空之女神发誓吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#775F当、当然敢啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#754F#1P是吗……\x02\x03",
            "#750F刚才我在你们的房间里\x01",
            "捡到了一枚徽章之类的东西……\x02\x03",
            "那不是你的东西吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#772F咦，不可能……\x01",
            "我明明塞进自己裤袋里面的……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#774F啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F果然是你～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#044F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F老师套话还真是有一手……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#752F#1P克拉姆……\x01",
            "这下你无话可说了吧。\x02\x03",
            "马上把你拿走的东西\x01",
            "还给这位姐姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#773F呜呜呜呜呜呜呜……\x02",
    )

    CloseMessageWindow()
    OP_44(0xB, 0x1)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(
        0xB,
        (
            "#776F#1P算我倒霉！\x01",
            "还你就还你！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0x136, 0x1)

    def lambda_1A47():

        label("loc_1A47")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A47")

    QueueWorkItem2(0x101, 1, lambda_1A47)

    def lambda_1A58():

        label("loc_1A58")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A58")

    QueueWorkItem2(0x8, 1, lambda_1A58)

    def lambda_1A69():

        label("loc_1A69")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A69")

    QueueWorkItem2(0x102, 1, lambda_1A69)

    def lambda_1A7A():

        label("loc_1A7A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A7A")

    QueueWorkItem2(0xA, 1, lambda_1A7A)

    def lambda_1A8B():

        label("loc_1A8B")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A8B")

    QueueWorkItem2(0x9, 1, lambda_1A8B)

    def lambda_1A9C():

        label("loc_1A9C")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_1A9C")

    QueueWorkItem2(0x136, 1, lambda_1A9C)
    OP_92(0xB, 0x101, 0x4B0, 0xFA0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克拉姆将徽章扔在地上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x35C, 1)
    OP_8F(0xB, 0x1194, 0x0, 0x78D2, 0xFA0, 0x0)

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()
    OP_95(0xB, 0x0, 0x0, 0x0, 0x320, 0x1770)

    ChrTalk(
        0xB,
        "#772F#1P哼，你好样的！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    OP_8E(0xB, 0x1405, 0x0, 0x709E, 0x1770, 0x0)
    OP_8E(0xB, 0x1107, 0x0, 0x50A0, 0x1B58, 0x0)

    ChrTalk(
        0x136,
        "#043F啊，克拉姆！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#750F#1P不要紧，让他自己清醒一下也好。\x01",
            "一会儿就会回来的。\x02\x03",
            "#750F啊，对了……\x01",
            "大家都不要站在这里说话了。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)
    Sleep(400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x136, 0xFF)
    OP_44(0xA, 0x1)
    OP_44(0x9, 0x1)

    def lambda_1C5D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C5D)

    def lambda_1C6B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C6B)

    def lambda_1C79():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_1C79)
    Sleep(400)

    ChrTalk(
        0x8,
        (
            "#750F#1P详细的情况，\x01",
            "我们到屋子里边喝茶边谈吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2410   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1CE3")

    Return()

    # Function_6_507 end

    def Function_7_1CE4(): pass

    label("Function_7_1CE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D30")
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_7_1CE4")

    label("loc_1D30")

    Return()

    # Function_7_1CE4 end

    def Function_8_1D31(): pass

    label("Function_8_1D31")

    OP_8E(0xFE, 0xE9C, 0xFFFFFF38, 0x425E, 0x1B58, 0x0)
    OP_96(0xFE, 0x3F2, 0xC8, 0x425E, 0x7D0, 0x1B58)
    OP_8E(0xFE, 0xFFFFF7F4, 0x64, 0x3764, 0x1B58, 0x0)
    OP_8E(0xFE, 0xFFFFEE6C, 0xFFFFFF38, 0x3912, 0x1B58, 0x0)

    def lambda_1D8A():

        label("loc_1D8A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_1D8A")

    QueueWorkItem2(0xFE, 2, lambda_1D8A)
    Sleep(1600)
    OP_8F(0xFE, 0xFFFFEDC2, 0xFFFFFF9C, 0x4880, 0x1B58, 0x0)
    Sleep(1200)
    OP_8F(0xFE, 0xFFFFED54, 0xFFFFFF38, 0x4F2E, 0x1B58, 0x0)
    Sleep(500)
    OP_44(0xFE, 0x2)
    OP_8E(0xFE, 0xFFFFEC6E, 0x0, 0x7C06, 0x2AF8, 0x0)
    Return()

    # Function_8_1D31 end

    def Function_9_1DE5(): pass

    label("Function_9_1DE5")

    Sleep(500)
    OP_8E(0xFE, 0x4D8, 0x0, 0x532A, 0x1B58, 0x0)
    OP_8E(0xFE, 0xFFFFF984, 0xC8, 0x4B28, 0x1B58, 0x0)
    OP_96(0xFE, 0xFFFFF38A, 0xFFFFFF38, 0x4902, 0x7D0, 0x1B58)
    Sleep(1000)
    OP_8F(0xFE, 0xFFFFF3D0, 0xFFFFFF9C, 0x3796, 0x1B58, 0x0)
    Sleep(1000)
    OP_8F(0xFE, 0xFFFFF3D0, 0xFFFFFF9C, 0x3796, 0x1B58, 0x0)
    OP_8F(0xFE, 0xFFFFEE6C, 0xFFFFFF38, 0x3912, 0x1B58, 0x0)
    Sleep(500)
    OP_44(0x102, 0xFF)
    OP_44(0xFE, 0x2)
    OP_8E(0xFE, 0xFFFFEC6E, 0x0, 0x7C06, 0x2AF8, 0x0)
    Return()

    # Function_9_1DE5 end

    def Function_10_1E91(): pass

    label("Function_10_1E91")

    EventBegin(0x0)
    OP_6D(-1130, 80, 31130, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x136, 0x80)
    SetChrPos(0x101, 0, 0, 32900, 0)
    SetChrPos(0x102, 0, 0, 32900, 0)
    SetChrPos(0x136, 0, 0, 32900, 0)
    SetChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_70(0x0, 0x14)
    OP_73(0x0)
    OP_43(0x101, 0x1, 0x0, 0xB)
    OP_43(0x102, 0x1, 0x0, 0xC)
    OP_43(0x136, 0x1, 0x0, 0xD)
    WaitChrThread(0x136, 0x1)

    ChrTalk(
        0x101,
        (
            "#000F嗯……特蕾莎院长\x01",
            "真是一位非常和蔼可亲的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是啊……\x01",
            "感觉就像是母亲那样的亲切。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#041F#2P呵呵，那些孩子一直都\x01",
            "把老师看成是自己的母亲呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x136, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -5000, 8000, 13000, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_204F():

        label("loc_204F")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_204F")

    QueueWorkItem2(0x101, 1, lambda_204F)

    def lambda_2060():

        label("loc_2060")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_2060")

    QueueWorkItem2(0x102, 1, lambda_2060)
    OP_8C(0x136, 180, 0)
    OP_92(0xC, 0x136, 0x1388, 0x2710, 0x0)
    OP_22(0x8C, 0x0, 0x64)
    OP_92(0xC, 0x136, 0xFA0, 0x1F40, 0x0)
    OP_92(0xC, 0x136, 0xBB8, 0x1770, 0x0)
    OP_92(0xC, 0x136, 0x7D0, 0xBB8, 0x0)
    OP_8E(0xC, 0xFFFFFD8A, 0x3E8, 0x765C, 0x5DC, 0x0)

    def lambda_20C9():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_20C9)
    SetChrChipByIndex(0x136, 5)
    SetChrSubChip(0x136, 2)
    OP_8C(0x136, 135, 0)
    OP_8F(0xC, 0xFFFFFEB6, 0xC8, 0x7788, 0x3E8, 0x0)
    Fade(250)
    SetChrSubChip(0x136, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x136, 0x20)
    OP_0D()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(
        0x136,
        (
            "#040F#2P基库。\x01",
            "让你久等了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#310F#1P啾。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F#2P嗯，是的。\x01",
            "他们并不是坏人哦。\x02\x03",
            "他们是我的新朋友，\x01",
            "艾丝蒂尔和约修亚。\x02\x03",
            "你记住他们的名字了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#311F#1P啾！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#041F#2P呵呵，乖孩子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F厉、厉害啊。\x01",
            "你在和它说话吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F#2P也不能算是说话，\x01",
            "不过我能知道它想表达什么。\x02\x03",
            "也许是因为\x01",
            "大家能够感受到彼此的心情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#501F哇～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F这就是所谓的心灵相通吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#041F#2P是啊。\x02",
    )

    CloseMessageWindow()
    OP_92(0x101, 0xC, 0x320, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#501F你好啊，基库。\x02\x03",
            "#001F我叫艾丝蒂尔，多多指教哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#310F#1P啾？\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0xC)

    ChrTalk(
        0xC,
        "#310F#1P啾——\x02",
    )

    CloseMessageWindow()

    def lambda_23F6():

        label("loc_23F6")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_23F6")

    QueueWorkItem2(0x101, 1, lambda_23F6)

    def lambda_2407():

        label("loc_2407")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2407")

    QueueWorkItem2(0x102, 1, lambda_2407)

    def lambda_2418():

        label("loc_2418")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_2418")

    QueueWorkItem2(0x136, 1, lambda_2418)
    OP_22(0x8C, 0x0, 0x64)
    Fade(250)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x136, 0x20)
    SetChrSubChip(0x136, 2)
    OP_0D()

    def lambda_2443():
        OP_8E(0xFE, 0xFFFFD260, 0x1B58, 0x6EFA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2443)
    Sleep(400)

    def lambda_2463():
        OP_8E(0xFE, 0xFFFFD260, 0x1B58, 0x6EFA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2463)
    Sleep(400)

    def lambda_2483():
        OP_8E(0xFE, 0xFFFFD260, 0x1B58, 0x6EFA, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2483)
    Sleep(400)

    def lambda_24A3():
        OP_8E(0xFE, 0xFFFFD260, 0x1B58, 0x6EFA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_24A3)

    ChrTalk(
        0x101,
        (
            "#004F啊啊……\x02\x03",
            "#007F呜呜……看来我被甩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈，真是可惜呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        "#045F#2P呵呵……\x02",
    )

    CloseMessageWindow()
    OP_44(0x136, 0xFF)
    SetChrChipByIndex(0x136, 6)
    SetChrSubChip(0x136, 0)
    OP_8C(0x136, 135, 400)

    ChrTalk(
        0x136,
        (
            "#040F#2P话说回来，\x01",
            "艾丝蒂尔你们等一下要去卢安市吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x136, 200)
    OP_44(0x101, 0xFF)
    TurnDirection(0x101, 0x136, 400)

    ChrTalk(
        0x101,
        (
            "#006F嗯，我们要到那里的\x01",
            "协会支部办理转属手续。\x02\x03",
            "要不然就不能接受工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F#2P卢安的协会支部啊，\x01",
            "我去过很那里多次呢。\x02\x03",
            "不介意的话，可以让我带你们去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哇～这真是太好了。\x01",
            "我们可是求之不得呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那样没关系吗？\x01",
            "你不赶快回学院的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#040F#2P没关系的。\x01",
            "今天我向学院请了一天的假。\x02\x03",
            "在天黑之前回去就没事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F那就这样决定啦⊙\x02\x03",
            "目的地卢安，出发～！\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x80)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x101, -120, 10, 29740, 180)
    SetChrPos(0x102, -120, 10, 29740, 180)
    SetChrPos(0x136, -120, 10, 29740, 180)
    OP_6D(-120, 10, 29740, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(500, 0)
    EventEnd(0x0)
    Return()

    # Function_10_1E91 end

    def Function_11_287F(): pass

    label("Function_11_287F")

    ClearChrFlags(0x101, 0x80)
    OP_8E(0x101, 0x0, 0x0, 0x724C, 0x7D0, 0x0)

    def lambda_289E():

        label("loc_289E")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_289E")

    QueueWorkItem2(0xFE, 2, lambda_289E)
    Return()

    # Function_11_287F end

    def Function_12_28AA(): pass

    label("Function_12_28AA")

    Sleep(800)
    ClearChrFlags(0x102, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0x7BB6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5DC, 0x0, 0x7698, 0x7D0, 0x0)

    def lambda_28E2():

        label("loc_28E2")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_28E2")

    QueueWorkItem2(0xFE, 2, lambda_28E2)
    Return()

    # Function_12_28AA end

    def Function_13_28EE(): pass

    label("Function_13_28EE")

    Sleep(800)
    Sleep(800)
    ClearChrFlags(0x136, 0x80)
    OP_8E(0xFE, 0x0, 0x0, 0x7BB6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_72(0x0, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 20)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0x136, 0xFFFFFF7E, 0xA, 0x7850, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_13_28EE end

    def Function_14_2965(): pass

    label("Function_14_2965")

    EventBegin(0x0)
    OP_6D(310, 0, -160, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    FadeToBright(2000, 0)
    OP_6D(1900, 0, 36890, 10000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2411   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2965 end

    def Function_15_29DA(): pass

    label("Function_15_29DA")

    EventBegin(0x0)
    OP_6D(3610, 0, 34400, 0)
    OP_6C(57000, 0)
    LoadEffect(0x0, "map\\\\mpfire0.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 3450, 2000, 34330, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 3650, 1000, 33330, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    OP_6C(351000, 4000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2411   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_29DA end

    SaveToFile()

Try(main)
