from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3105   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3105.x',
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
        '格斯塔夫维修长',                       # 9
        '吉拉尔',                               # 10
        '玛多克工房长',                         # 11
        '朵洛希',                               # 12
        '安东尼',                               # 13
        '凯诺娜上尉',                           # 14
        '鲁特尔',                               # 15
        '多杰',                                 # 16
        '巴拉特',                               # 17
        '蔡斯市·工房区',                       # 18
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH02440 ._CH',             # 01
        'ED6_DT07/CH02620 ._CH',             # 02
        'ED6_DT07/CH02070 ._CH',             # 03
        'ED6_DT07/CH01700 ._CH',             # 04
        'ED6_DT07/CH02100 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH02440P._CP',             # 01
        'ED6_DT07/CH02620P._CP',             # 02
        'ED6_DT07/CH02070P._CP',             # 03
        'ED6_DT07/CH01700P._CP',             # 04
        'ED6_DT07/CH02100P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
    )

    DeclNpc(
        X                   = -37000,
        Z                   = -3800,
        Y                   = 145500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -20110,
        Z                   = 8000,
        Y                   = 121830,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -18770,
        Z                   = 8000,
        Y                   = 89560,
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


    DeclActor(
        TriggerX            = -41010,
        TriggerZ            = 8000,
        TriggerY            = 122500,
        TriggerRange        = 800,
        ActorX              = -41010,
        ActorZ              = 10200,
        ActorY              = 122500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38900,
        TriggerZ            = 8400,
        TriggerY            = 122040,
        TriggerRange        = 800,
        ActorX              = -38900,
        ActorZ              = 9900,
        ActorY              = 122040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_27A",          # 00, 0
        "Function_1_4DC",          # 01, 1
        "Function_2_4EF",          # 02, 2
        "Function_3_66C",          # 03, 3
        "Function_4_690",          # 04, 4
        "Function_5_6B4",          # 05, 5
        "Function_6_6D8",          # 06, 6
        "Function_7_6FC",          # 07, 7
        "Function_8_F5E",          # 08, 8
        "Function_9_11B9",         # 09, 9
        "Function_10_11F2",        # 0A, 10
        "Function_11_2414",        # 0B, 11
        "Function_12_3271",        # 0C, 12
        "Function_13_35EE",        # 0D, 13
        "Function_14_36D6",        # 0E, 14
        "Function_15_36DB",        # 0F, 15
        "Function_16_3F81",        # 10, 16
        "Function_17_44F5",        # 11, 17
        "Function_18_4835",        # 12, 18
        "Function_19_5924",        # 13, 19
        "Function_20_59DF",        # 14, 20
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_2B7")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -17880, 8000, 118110, 183)
    OP_43(0xE, 0x0, 0x0, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44660, 8000, 129500, 5)
    Jump("loc_4DB")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2F4")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -17880, 8000, 118110, 183)
    OP_43(0xE, 0x0, 0x0, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44660, 8000, 129500, 5)
    Jump("loc_4DB")

    label("loc_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_314")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_37D")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -47500, -4000, 151780, 261)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -47500, -4000, 152840, 261)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -40130, 8000, 125930, 237)
    OP_43(0xC, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3BD")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -44530, -4000, 142000, 176)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44510, -4000, 140610, 21)
    SetChrFlags(0x10, 0x10)
    Jump("loc_4DB")

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3FA")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -58040, 4000, 125930, 187)
    OP_43(0x8, 0x0, 0x0, 0x6)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_404")
    Jump("loc_4DB")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_441")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -49800, 8000, 117400, 3)
    OP_43(0x8, 0x0, 0x0, 0x5)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_461")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_481")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4A1")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)
    Jump("loc_4DB")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4DB")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -40130, 8000, 125930, 237)
    OP_43(0xC, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -44750, -4000, 146070, 81)

    label("loc_4DB")

    Return()

    # Function_0_27A end

    def Function_1_4DC(): pass

    label("Function_1_4DC")

    OP_16(0x2, 0xFA0, 0xFFFD6020, 0x4E20, 0x30053)
    Return()

    # Function_1_4DC end

    def Function_2_4EF(): pass

    label("Function_2_4EF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_656")

    label("loc_514")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_656")

    label("loc_52D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_656")

    label("loc_546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_656")

    label("loc_55F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_578")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_656")

    label("loc_578")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_591")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_656")

    label("loc_591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_656")

    label("loc_5AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C3")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_656")

    label("loc_5C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_656")

    label("loc_5DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_656")

    label("loc_5F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_656")

    label("loc_60E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_627")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_656")

    label("loc_627")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_640")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_656")

    label("loc_640")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_656")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_656")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_656")

    label("loc_66B")

    Return()

    # Function_2_4EF end

    def Function_3_66C(): pass

    label("Function_3_66C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68F")
    OP_8D(0xFE, -19390, 119560, -16690, 116060, 3000)
    Jump("Function_3_66C")

    label("loc_68F")

    Return()

    # Function_3_66C end

    def Function_4_690(): pass

    label("Function_4_690")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_8D(0xFE, -35820, 123780, -43940, 129220, 3000)
    Jump("Function_4_690")

    label("loc_6B3")

    Return()

    # Function_4_690 end

    def Function_5_6B4(): pass

    label("Function_5_6B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D7")
    OP_8D(0xFE, -45240, 117320, -51970, 121500, 3000)
    Jump("Function_5_6B4")

    label("loc_6D7")

    Return()

    # Function_5_6B4 end

    def Function_6_6D8(): pass

    label("Function_6_6D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FB")
    OP_8D(0xFE, -56420, 122640, -59470, 129340, 3000)
    Jump("Function_6_6D8")

    label("loc_6FB")

    Return()

    # Function_6_6D8 end

    def Function_7_6FC(): pass

    label("Function_7_6FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_77F")

    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "都不通知一下就检查，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "王国军真是的，\x01",
            "实在太乱来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5A")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_7EB")

    ChrTalk(
        0xFE,
        (
            "一会儿『赛希莉亚号』\x01",
            "就要开过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "必须马上开始\x01",
            "确认下拢岸的状况了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5A")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_8AB")

    ChrTalk(
        0xFE,
        (
            "工房船现在\x01",
            "马上就要出航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过，\x01",
            "却比预定去要塞的时间提前了很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "那边发生了什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F5A")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_8FB")

    ChrTalk(
        0xFE,
        (
            "好了，\x01",
            "这样飞船起航就告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "趁这段时间整理一下货物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5A")

    label("loc_8FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_9E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_97D")

    ChrTalk(
        0xFE,
        (
            "话说回来，这种时候\x01",
            "真是羡慕雷曼那家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那家伙兼任驾驶员，\x01",
            "飞行前为了调整身体状态，\x01",
            "早早地就回家去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E3")

    label("loc_97D")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "呼，明天还是要去要塞啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近的工作\x01",
            "好像很多啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)

    label("loc_9E3")

    Jump("loc_F5A")

    label("loc_9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_ABB")

    ChrTalk(
        0xFE,
        (
            "中央工房的事件\x01",
            "应该解决了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哎？\x01",
            "犯人到现在都还没抓到？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "那还真是糟糕啊。\x01",
            "下次不会来袭击工房船吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5A")

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_BB2")

    ChrTalk(
        0xFE,
        (
            "呼，都是因为那个公爵大人，\x01",
            "搞得大家都对王家的印象变差了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "哼，很久以前\x01",
            "那种快乐纯粹的女王诞辰庆典\x01",
            "是很难再出现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "该死，那个混账公爵。\x01",
            "还我的诞辰庆典来！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D00")

    label("loc_BB2")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        (
            "之前的休假\x01",
            "我去参观了\x01",
            "艾尔·雷登瀑布……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "竟遇到那个叫杜什么的公爵，\x01",
            "那个王家的人微服出行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且那个人\x01",
            "还蛮横任性得要命。\x01",
            "真是倒了大霉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "唔，大家都没想到\x01",
            "王家的人竟会是那个样子。\x01",
            "真是失望透了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D00")

    Jump("loc_F5A")

    label("loc_D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D33")

    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "差不多该到返航的时候了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB1")

    label("loc_D33")


    ChrTalk(
        0xFE,
        "怎么样？很漂亮吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "这可是中央工房引以为傲的\x01",
            "『莱普尼兹号』啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB1")

    Jump("loc_F5A")

    label("loc_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_E40")

    ChrTalk(
        0xFE,
        (
            "工房好像还没找出\x01",
            "昨天那种现象的原因所在吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不管怎样，\x01",
            "希望不要再发生这种事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_E40")

    OP_A2(0x5)

    ChrTalk(
        0xFE,
        "昨天晚上，导力供应停止了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "不过还好不是在白天发生，\x01",
            "真是万幸呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "如果在飞艇上出现这种情况，\x01",
            "真不知道会发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F13")

    Jump("loc_F5A")

    label("loc_F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F5A")

    ChrTalk(
        0xFE,
        "好的，拢岸准备好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "接下来，\x01",
            "要快点进行出发前的检查了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5A")

    TalkEnd(0xFE)
    Return()

    # Function_7_6FC end

    def Function_8_F5E(): pass

    label("Function_8_F5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_FF8")

    ChrTalk(
        0xFE,
        (
            "#690F哦，稍微晚了些真是不好意思。\x02\x03",
            "要塞那边又来要求我们出动了。\x01",
            "我想今天之内\x01",
            "就可以做好准备了。\x02\x03",
            "嗯，希望和平时一样\x01",
            "不要发生什么意外就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B5")

    label("loc_FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_10BF")

    ChrTalk(
        0xFE,
        (
            "#690F哦，是提妲丫头。\x01",
            "没有受伤吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F…………………………\x02\x03",
            "啊…………\x02\x03",
            "啊……是、是的！\x01",
            "没事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#690F怎么啦？\x01",
            "你一直在发呆啊。\x02\x03",
            "不过，没受伤的话，\x01",
            "那比什么都好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B5")

    label("loc_10BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_11B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10F1")

    ChrTalk(
        0xFE,
        (
            "#690F哦，是提妲丫头。\x01",
            "多多保重哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B5")

    label("loc_10F1")

    OP_A2(0x4)

    ChrTalk(
        0xFE,
        (
            "#690F哦，是提妲丫头。\x02\x03",
            "又是拉赛尔老爷子的差使吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F啊，是呢。\x02\x03",
            "要到亚尔摩村去一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#690F是吗，那么\x01",
            "多多保重哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F嗯，\x01",
            "那么我们就出发了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B5")

    TalkEnd(0xFE)
    Return()

    # Function_8_F5E end

    def Function_9_11B9(): pass

    label("Function_9_11B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_11D7")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵－噢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11EE")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11EE")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(
        0xFE,
        "喵～噢？\x02",
    )

    CloseMessageWindow()

    label("loc_11EE")

    TalkEnd(0xFE)
    Return()

    # Function_9_11B9 end

    def Function_10_11F2(): pass

    label("Function_10_11F2")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1600")
    OP_A2(0x604)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -20510, 8000, 119230, 0)
    SetChrPos(0x102, -18980, 8000, 119430, 0)

    def lambda_1233():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1233)

    def lambda_1243():
        OP_6B(2750, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1243)
    OP_6D(-20210, 8000, 122050, 2000)

    ChrTalk(
        0x9,
        "啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就像刚才我说的，\x01",
            "飞艇什么时候能来还不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "实在抱歉，\x01",
            "你们在游击士协会等一会儿吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯～其实……\x01",
            "我们稍微改变了一下计划。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F抱歉，\x01",
            "搭乘手续能取消吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是这样吗……\x01",
            "唉，也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "在定期船到来之前，\x01",
            "不需要付取消手续费的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "把刚才的船票\x01",
            "还给我就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把两张船票还给了接待员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3F(0x36A, 2)

    ChrTalk(
        0x9,
        (
            "哦……\x01",
            "好像是军用警备飞艇来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "来的还真早啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F那、那么\x01",
            "我们赶快……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14BC():
        OP_8E(0xFE, 0xFFFFB12C, 0x1F40, 0x192A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14BC)

    ChrTalk(
        0x102,
        (
            "#010F麻烦您了，\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14FA():
        OP_8E(0xFE, 0xFFFFB7F8, 0x1F40, 0x192A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14FA)

    ChrTalk(
        0x9,
        (
            "啊啊。\x01",
            "欢迎下次再来乘坐啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#180F哼哼……\x01",
            "还真是忙啊。\x02\x03",
            "首先，还是去\x01",
            "拜见一下工房长吧。\x02\x03",
            "不过，不愧是上校大人……\x01",
            "能想出这样的方法。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2410")

    label("loc_1600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17BC")
    OP_A2(0x602)
    OP_28(0x54, 0x1, 0x2)
    EventBegin(0x0)
    OP_69(0x9, 0x3E8)

    ChrTalk(
        0x9,
        "啊，你们好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "我已经从雾香那里听说了。\x01",
            "现在就办理搭乘手续吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，麻烦您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么，在这张单子上\x01",
            "填写姓名和联络方式吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔\x01",
            "办理了搭乘手续。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        (
            "好了，\x01",
            "这个就是你们的船票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船到了之后，\x01",
            "把这个出示给乘务员就可以了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "得到两张船票。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3E(0x36A, 2)
    EventEnd(0x1)
    Jump("loc_2410")

    label("loc_17BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E09")
    OP_A2(0x517)
    ClearMapFlags(0x1)
    OP_69(0x9, 0x3E8)

    ChrTalk(
        0x9,
        "哟！要乘坐飞行船吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "去西面的定期船的话\x01",
            "正好刚刚开走……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F没有啊，\x01",
            "我们不是来乘飞行船的。\x02\x03",
            "格斯塔夫维修长\x01",
            "我想让你们两人办点事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "什么，找大叔的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "大叔的话，\x01",
            "现在不在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎！出去了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "是呀。有两三天了。\x01",
            "去了雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好像很急，是个有\x01",
            "军用警备飞艇的家伙的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F到雷斯顿要塞呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F是位于瓦雷利亚湖畔的\x01",
            "王国军最大的军事基地。\x02\x03",
            "在蔡斯地区的北侧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呼～～这样的话\x01",
            "就不是简单能回来的了。\x02\x03",
            "博士要的准备，怎么办呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然不知道你们有什么事，\x01",
            "但我想他差不多要回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "刚刚有连络通信过来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎……\x01",
            "下一班定期船已经来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "不是的，真是不听人说话的家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#20A莱普尼兹号进入飞艇坪（※假定）\x05\x02",
    )


    ChrTalk(
        0x101,
        (
            "#000F橙色的定期船……\x02\x03",
            "哎呀！\x01",
            "有那样的定期船吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F不……\x01",
            "那好像不是定期船。\x02\x03",
            "无论哪里形状都不同，\x01",
            "还带有作业用的扶手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，的确……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这是中央工房所有的\x01",
            "工房船《莱普尼兹号》。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "虽然和定期船是相同型号，\x01",
            "但追加了各种设备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这个主要是用来\x01",
            "大型设备的支持和制品的搬运。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎～～！\x01",
            "飞空的工房呀。\x02\x03",
            "那么维修长\x01",
            "应该在那艘船上吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "你们快点\x01",
            "去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们就告辞了。\x02",
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)
    Jump("loc_2410")

    label("loc_1E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1E79")

    ChrTalk(
        0x9,
        (
            "嗯？怎么了？\x01",
            "手续已经办好了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船到了之后，\x01",
            "凭刚才的票就可以乘坐了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2410")

    label("loc_1E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_1EF8")

    ChrTalk(
        0x9,
        "哟，你们也很忙呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好像工房船\x01",
            "有很紧急的任务要执行。\x01",
            "这边也已经乱成一团了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2410")

    label("loc_1EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1F41")

    ChrTalk(
        0x9,
        (
            "『赛希莉亚号』\x01",
            "已经按预定的时间出航了………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唔，就趁现在难得的空闲\x01",
            "集中精神看《利贝尔通讯》吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2410")

    label("loc_1F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_20F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2008")

    ChrTalk(
        0x9,
        "嗯嗯，对了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "说到封面……\x01",
            "最近《利贝尔通讯》上面的照片\x01",
            "都变得好漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，一想到这个，\x01",
            "就很期待下期的封面啊。\x01",
            "……偷偷告诉你们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F0")

    label("loc_2008")

    OP_A2(0x0)

    ChrTalk(
        0x9,
        (
            "中央工房的骚动\x01",
            "好像是起严重的事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "竟然敢袭击中央工房，\x01",
            "世上还有这样无法无天的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "唉，这样一来\x01",
            "下期《利贝尔通讯》的封面\x01",
            "就会是蔡斯了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20F0")

    Jump("loc_2410")

    label("loc_20F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_21D4")

    ChrTalk(
        0x9,
        (
            "那个，你们看过\x01",
            "《利贝尔通讯》最新一期了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "听说卢安的市长\x01",
            "是个无法无天的坏家伙，\x01",
            "已经被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，空贼事件也好，\x01",
            "这个叫戴尔蒙的家伙也好……\x01",
            "最近这个世界真是不太平啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2410")

    label("loc_21D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_21FC")

    ChrTalk(
        0x9,
        "你们见到维修长了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2410")

    label("loc_21FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_235F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_228E")

    ChrTalk(
        0x9,
        (
            "听说，最后好象是游击士\x01",
            "解决了这次空贼事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真是的，明明发生了这么严重的事情，\x01",
            "王国军却什么事也做不了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235C")

    label("loc_228E")

    OP_A2(0x0)

    ChrTalk(
        0x9,
        (
            "我读过利贝尔通讯了，\x01",
            "前段时间柏斯的空贼骚动\x01",
            "好像闹得很大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船停航了，\x01",
            "对我们接待员来说可真是噩梦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "要把事情向客人解释清楚，\x01",
            "可是一件很难的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235C")

    Jump("loc_2410")

    label("loc_235F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2410")

    ChrTalk(
        0x9,
        (
            "目前，西向航线的『赛希莉亚号』\x01",
            "正停靠在飞艇坪中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "去往格兰赛尔的旅客，\x01",
            "请前往入口处准备登船。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2410")

    TalkEnd(0x9)
    Return()

    # Function_10_11F2 end

    def Function_11_2414(): pass

    label("Function_11_2414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2608")
    EventBegin(0x0)

    ChrTalk(
        0x8,
        "#690F出发去雷斯顿要塞吗？\x02",
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
            "出发\x01",          # 0
            "整理装备\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24A4"),
        (1, "loc_25CB"),
        (SWITCH_DEFAULT, "loc_2605"),
    )


    label("loc_24A4")

    OP_A2(0x561)
    OP_28(0x43, 0x1, 0x400)
    OP_28(0x44, 0x4, 0x2)
    OP_28(0x44, 0x4, 0x4)

    ChrTalk(
        0x8,
        (
            "#690F好，\x01",
            "那么快上去吧！\x02\x03",
            "工房船《莱普尼兹号》\x01",
            "出发去雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F游击士的各位，\x01",
            "博士的事就拜托你们了。\x02\x03",
            "另外……\x01",
            "请保护好提妲。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2558():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2558)

    def lambda_2566():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2566)

    def lambda_2574():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2574)
    TurnDirection(0x107, 0xA, 400)

    ChrTalk(
        0x107,
        "#060F工房长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，都交给我吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们走了。\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jump("loc_2605")

    label("loc_25CB")

    OP_A2(0x572)

    ChrTalk(
        0x8,
        (
            "#690F我知道了。\x01",
            "准备好了就告诉我一声。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2605")

    Jump("loc_3270")

    label("loc_2608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_311E")
    EventBegin(0x0)
    SetChrPos(0x101, -46160, -4000, 141480, 90)
    SetChrPos(0x106, -44780, -4000, 140260, 0)
    SetChrPos(0x107, -45700, -4000, 140390, 45)
    SetChrPos(0x102, -45780, -4000, 142250, 135)
    Fade(1000)

    def lambda_2665():
        OP_6C(45000, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2665)
    OP_6D(-45150, -4000, 141460, 0)

    ChrTalk(
        0xA,
        (
            "#800F噢，等一下，\x01",
            "你们准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#050F是啊，随时都能出发。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F《莱普尼兹号》的\x01",
            "准备也完成了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F啊，我们运气真好，\x01",
            "军队急着要我们发货。\x02\x03",
            "正好准备出发\x01",
            "要去雷斯顿要塞。\x02\x03",
            "随时都可以出发呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(
        0x101,
        (
            "#000F随时……\x02\x03",
            "那个橙色的飞行船\x01",
            "可我怎么没找到呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 315, 400)
    Sleep(200)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8E(0x102, 0xFFFF467E, 0xFFFFF060, 0x230F0, 0x7D0, 0x0)

    ChrTalk(
        0x102,
        "#010F艾丝蒂尔，往下面看。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    def lambda_287C():
        OP_8E(0x101, 0xFFFF4688, 0xFFFFF060, 0x22CE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_287C)

    def lambda_2897():
        OP_6C(314000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2897)
    OP_6D(-49360, -4000, 145960, 2000)

    ChrTalk(
        0x101,
        (
            "#000F啊，竟然在那里……\x02\x03",
            "那么我们要\x01",
            "下到下面去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F呵呵，姐姐，\x01",
            "不用下去的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        "#000F哎……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2934():

        label("loc_2934")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2934")

    QueueWorkItem2(0xA, 2, lambda_2934)

    def lambda_2945():

        label("loc_2945")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2945")

    QueueWorkItem2(0x107, 2, lambda_2945)

    def lambda_2956():

        label("loc_2956")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2956")

    QueueWorkItem2(0x106, 2, lambda_2956)
    Sleep(1000)
    OP_8C(0x101, 315, 400)

    ChrTalk(
        0x101,
        "#000F为什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F呀，飞行船的轨道……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#050F呀，你们不知道呀吗？\x02\x03",
            "这里的飞行场都是\x01",
            "用超乎常识的方法造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F超，超乎常识？\x02",
    )

    CloseMessageWindow()

    def lambda_2A3F():
        OP_8E(0x101, 0xFFFF4688, 0xFFFFF060, 0x22CE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A3F)

    def lambda_2A5A():
        OP_6C(314000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A5A)
    OP_6D(-49360, -4000, 145960, 2000)
    OP_6F(0x0, 500)
    OP_70(0x0, 0x4B0)

    def lambda_2A89():
        OP_6C(339000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A89)
    OP_6D(-55390, -4000, 147110, 1500)

    def lambda_2AAA():
        OP_6B(2200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AAA)
    OP_67(0, 21600, -10000, 2000)

    def lambda_2ACB():
        OP_6B(3500, 3100)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2ACB)

    def lambda_2ADB():
        OP_6C(27000, 3100)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2ADB)
    OP_6D(-36640, -4000, 148800, 3100)
    SetChrPos(0x101, -46240, -4000, 141000, 90)
    SetChrPos(0x102, -46280, -4000, 142120, 90)

    def lambda_2B1E():
        OP_6B(5500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B1E)

    def lambda_2B2E():
        OP_67(0, 11000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B2E)
    OP_6C(90000, 5000)
    OP_73(0x0)
    Sleep(1000)

    def lambda_2B57():
        OP_6B(3500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B57)
    OP_6D(-45210, -4000, 142090, 2000)

    ChrTalk(
        0x101,
        (
            "#000F大致上我开始\x01",
            "对这种事渐渐习惯了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，想要弄清楚结构的话\x01",
            "得花一番工夫呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F而且这个\x01",
            "飞行场的构造也是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F知道了，\x01",
            "是拉赛尔博士吧。\x02\x03",
            "提妲。\x01",
            "你的爷爷真是\x01",
            "无所不能呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F呵呵……\x01",
            "我也同感。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36460, -4000, 144380, 270)

    ChrTalk(
        0x8,
        "#690F哟，久等了。\x02",
    )

    CloseMessageWindow()
    OP_6D(-40270, -4000, 143040, 1000)

    ChrTalk(
        0x107,
        "#060F呀，维修长。\x02",
    )

    CloseMessageWindow()

    def lambda_2D0C():

        label("loc_2D0C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D0C")

    QueueWorkItem2(0xA, 2, lambda_2D0C)

    def lambda_2D1D():

        label("loc_2D1D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D1D")

    QueueWorkItem2(0x102, 2, lambda_2D1D)

    def lambda_2D2E():

        label("loc_2D2E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D2E")

    QueueWorkItem2(0x101, 2, lambda_2D2E)

    def lambda_2D3F():

        label("loc_2D3F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D3F")

    QueueWorkItem2(0x107, 2, lambda_2D3F)

    def lambda_2D50():

        label("loc_2D50")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2D50")

    QueueWorkItem2(0x106, 2, lambda_2D50)

    def lambda_2D61():
        OP_6D(-44110, -3800, 143890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D61)

    def lambda_2D79():
        OP_8E(0xFE, 0xFFFF4C0A, 0xFFFFF060, 0x2385C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2D79)

    def lambda_2D94():
        OP_8E(0xFE, 0xFFFF4A8E, 0xFFFFF060, 0x2341A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D94)
    Sleep(100)

    def lambda_2DB4():
        OP_8E(0xFE, 0xFFFF4AFC, 0xFFFFF060, 0x23082, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_2DB4)
    Sleep(100)

    def lambda_2DD4():
        OP_8E(0xFE, 0xFFFF4B56, 0xFFFFF060, 0x22CFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_2DD4)
    OP_8E(0x8, 0xFFFF57A4, 0xFFFFF128, 0x2329E, 0x7D0, 0x0)

    ChrTalk(
        0x8,
        (
            "#690F提妲呀，\x01",
            "事情我已经听工房长说了。\x02\x03",
            "没想到老爷子\x01",
            "会遇到这样的事。\x02\x03",
            "能帮上忙的话，\x01",
            "我们维修员随时乐意效劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#060F谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#050F不好意思，麻烦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F不要客气，\x01",
            "老爷子也是我的恩人呀。\x02\x03",
            "那么\x01",
            "我们已经准备好了。\x02\x03",
            "出发去雷斯顿要塞吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0xA, 0xFF)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "出发\x01",          # 0
            "整理装备\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FBA"),
        (1, "loc_30E1"),
        (SWITCH_DEFAULT, "loc_311B"),
    )


    label("loc_2FBA")

    OP_A2(0x561)
    OP_28(0x43, 0x1, 0x400)
    OP_28(0x44, 0x4, 0x2)
    OP_28(0x44, 0x4, 0x4)

    ChrTalk(
        0x8,
        (
            "#690F好，\x01",
            "那么快上去吧！\x02\x03",
            "工房船《莱普尼兹号》\x01",
            "出发去雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F游击士的各位，\x01",
            "博士的事就拜托你们了。\x02\x03",
            "另外……\x01",
            "请保护好提妲。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_306E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_306E)

    def lambda_307C():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_307C)

    def lambda_308A():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_308A)
    TurnDirection(0x107, 0xA, 400)

    ChrTalk(
        0x107,
        "#060F工房长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，都交给我吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F那么我们走了。\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jump("loc_311B")

    label("loc_30E1")

    OP_A2(0x572)

    ChrTalk(
        0x8,
        (
            "#690F我知道了。\x01",
            "准备好了就告诉我一声。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_311B")

    Jump("loc_3270")

    label("loc_311E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3198")

    ChrTalk(
        0xA,
        (
            "#800F这边现在\x01",
            "也正由格斯塔夫维修长\x01",
            "指挥进行起飞前的准备呢。\x02\x03",
            "如果你们准备好了，\x01",
            "就再到这儿来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3270")

    label("loc_3198")

    OP_A2(0x3)

    ChrTalk(
        0xA,
        (
            "#800F哦哦，是你们啊。\x01",
            "已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F非常抱歉，\x01",
            "可能还要再费些时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F是吗，这边现在\x01",
            "也正由格斯塔夫维修长\x01",
            "指挥进行起飞前的准备呢。\x02\x03",
            "如果你们准备好了，\x01",
            "就再到这儿来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3270")

    Return()

    # Function_11_2414 end

    def Function_12_3271(): pass

    label("Function_12_3271")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_END)), "loc_3350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32D9")

    ChrTalk(
        0xFE,
        (
            "看起来定期船\x01",
            "好像会晚点很长时间啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我还是先回家\x01",
            "再做打算吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334D")

    label("loc_32D9")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "看起来定期船\x01",
            "好像会晚点很长时间啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "听说军队要盘检，\x01",
            "真是麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334D")

    Jump("loc_35EA")

    label("loc_3350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3454")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3389")

    ChrTalk(
        0xFE,
        (
            "说起来\x01",
            "我是不是来得太早了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3451")

    label("loc_3389")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "哦～早上好啊。\x01",
            "你们也是要去王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我呀，\x01",
            "是要去飞艇公社办些事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "而且还想赶快把工作搞定，\x01",
            "顺便参观诞辰庆典……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3451")

    Jump("loc_35EA")

    label("loc_3454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_35EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_34EE")

    ChrTalk(
        0xFE,
        (
            "飞艇的技术\x01",
            "真是越来越进步了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "乘坐定期船\x01",
            "到多杰的故乡\x01",
            "也不再是遥远的梦想了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EA")

    label("loc_34EE")

    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "今天早上，\x01",
            "偶然遇到了来自共和国的\x01",
            "导力器商人多杰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因为他要在飞艇坪参观，\x01",
            "我就热情地为他介绍了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "看，多杰。\x01",
            "那是器材的搬入口，\x01",
            "造船设施就在那个地下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EA")

    TalkEnd(0xFE)
    Return()

    # Function_12_3271 end

    def Function_13_35EE(): pass

    label("Function_13_35EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_36D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_367A")

    ChrTalk(
        0xFE,
        (
            "我将来也要\x01",
            "把飞艇作为商品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "但在那之前，\x01",
            "我的城镇得有个飞艇坪才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D2")

    label("loc_367A")

    OP_A2(0x2)

    ChrTalk(
        0xFE,
        (
            "呼，\x01",
            "现在只能感叹眼前的景象了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "实在是太棒了。\x02",
    )

    CloseMessageWindow()

    label("loc_36D2")

    TalkEnd(0xFE)
    Return()

    # Function_13_35EE end

    def Function_14_36D6(): pass

    label("Function_14_36D6")

    Call(0, 10)
    Return()

    # Function_14_36D6 end

    def Function_15_36DB(): pass

    label("Function_15_36DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F80")
    OP_A2(0x518)
    OP_28(0x3F, 0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3F, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_3701")
    OP_28(0x3F, 0x1, 0x2000)

    label("loc_3701")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(
        0x8,
        "年长的维修员",
        (
            "唔……？\x01",
            "这位小姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-42300, -3800, 143800, 1000)

    ChrTalk(
        0x101,
        "#000F啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "年长的维修员",
        (
            "这个《莱普尼兹号》\x01",
            "无关人员是不能进入的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "年长的维修员",
        "对不起，请你们离开吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，我们就是有关人员哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F我们找格斯塔夫维修长\x01",
            "有些事情商量……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "年长的维修员",
        "呀，你们找我什么事呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F叔叔是\x01",
            "维修长呀。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们把\x01",
            "拉赛尔博士委托想要借内燃引擎设备\x01",
            "的事说明了一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        (
            "#690F呀，\x01",
            "是拉赛尔老爷子的事呀。\x02\x03",
            "是要内燃引擎设备的话，\x01",
            "那来得正好呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#690F稍微等一下呀……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x8, -42300, -3800, 143800, 0)

    ChrTalk(
        0x101,
        "#000F怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F嗯……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_6D(-43500, -3800, 143700, 1000)

    ChrTalk(
        0x8,
        (
            "#690F嘿。\x01",
            "很重，小心啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x0, 0x2BC, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾丝蒂尔他们得到了内燃引擎设备设备。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8F(0x8, 0xFFFF5AC4, 0xFFFFF128, 0x231B8, 0xBB8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD9")

    ChrTalk(
        0x101,
        (
            "#000F哇哇……\x01",
            "的确是沉甸甸的呀。\x02\x03",
            "的确是沉甸甸的呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F哎！想不到\x01",
            "小姑娘还很能干嘛。\x02\x03",
            "哈哈，我很中意你呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嘿嘿，没什么啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C9D")

    label("loc_3BD9")


    ChrTalk(
        0x102,
        (
            "#010F确实是很重……\x01",
            "不过也不至于重到拿不动就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F哎……\x01",
            "现在的年轻人\x01",
            "小姑娘还很能干嘛。\x02\x03",
            "哈哈，我很中意你呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F您过奖了。\x02",
    )

    CloseMessageWindow()

    label("loc_3C9D")


    ChrTalk(
        0x8,
        (
            "#690F不过，这也真是个\x01",
            "有趣的偶然呀。\x02\x03",
            "刚从军方里还回来后\x01",
            "马上就被老爷子借走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F从军方，怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F啊，那个货样\x01",
            "被王国军借了一阵子。。\x02\x03",
            "好像什么研究要用到的。\x02\x03",
            "总算是\x01",
            "今天还回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F哎～。\x01",
            "的确是很偶然呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F呀，不……没什么。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_END)), "loc_3EBF")

    ChrTalk(
        0x102,
        (
            "#010F需要的东西都已经拿到了，\x01",
            "快点回博士那里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F0A")

    label("loc_3EBF")


    ChrTalk(
        0x102,
        (
            "#010F剩下的就是汽油了。\x01",
            "去地下工场吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0A")


    ChrTalk(
        0x101,
        (
            "#000F嗯，我知道了。\x02\x03",
            "维修长，ＴＨＡＮＫ　ＹＯＵ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F噢。\x01",
            "帮我向老爷子问好。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    EventEnd(0x0)

    label("loc_3F80")

    Return()

    # Function_15_36DB end

    def Function_16_3F81(): pass

    label("Function_16_3F81")

    EventBegin(0x0)
    SetChrPos(0x108, -45670, -4000, 146000, 0)
    SetChrPos(0x101, -46540, -4000, 147540, 0)
    SetChrPos(0x102, -47220, -4000, 146840, 0)
    SetChrPos(0x107, -47150, -4000, 145610, 0)
    TurnDirection(0x101, 0x108, 0)
    TurnDirection(0x102, 0x108, 0)
    TurnDirection(0x107, 0x108, 0)
    TurnDirection(0x108, 0x102, 0)
    OP_6D(-45760, -4000, 146000, 0)
    OP_67(0, 9090, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    OP_A2(0x559)

    ChrTalk(
        0x108,
        (
            "#070F……真是不好意思，\x01",
            "特地要你们来送我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F这是当然的啰，\x01",
            "我们受了你那么多照顾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F金，你就这样\x01",
            "乘定期船直接去王都吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F啊，我还有\x01",
            "其他事必须去办。\x02\x03",
            "办完事我也\x01",
            "帮忙调查\x01",
            "绑架事件的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x107, 400)

    ChrTalk(
        0x108,
        "#070F对不起了，小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#060F没这回事的啦。\x01",
            "你已经帮了我很多忙了……\x02\x03",
            "真的\x01",
            "多谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F哈哈……\x01",
            "你能这么说真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "开往王都的定期船\x01",
            "《赛希莉亚号》马上就要起飞了。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "请没有上船的乘客尽快上船。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(
        0x108,
        (
            "#070F呀……\x01",
            "差不多要出发了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42CC():
        OP_6D(-40990, -4000, 146200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42CC)

    def lambda_42E4():
        OP_6B(3360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_42E4)

    def lambda_42F4():
        OP_6C(32000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_42F4)
    SetChrFlags(0x108, 0x4)
    OP_8E(0x108, 0xFFFF4BEC, 0xFFFFF060, 0x23780, 0xBB8, 0x0)
    OP_8E(0x108, 0xFFFF4C6E, 0xFFFFF060, 0x232B2, 0xBB8, 0x0)

    def lambda_4331():
        OP_8E(0xFE, 0xFFFF50B0, 0xFFFFF060, 0x23A50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4331)

    def lambda_434C():
        OP_8E(0xFE, 0xFFFF4BD8, 0xFFFFF060, 0x23898, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_434C)

    def lambda_4367():
        OP_8E(0xFE, 0xFFFF4BF6, 0xFFFFF060, 0x23532, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4367)
    OP_8E(0x108, 0xFFFF720C, 0xFFFFF060, 0x236C2, 0xBB8, 0x0)
    TurnDirection(0x108, 0x107, 400)

    ChrTalk(
        0x108,
        (
            "#070F那再见了，\x01",
            "有机会还会碰面的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，好。\x02\x03",
            "对了，金要在\x01",
            "利贝尔呆到什么时候呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F明确时间还不知道……\x01",
            "我想会呆到女王生日庆典吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊，那样的话\x01",
            "也许会再见面的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F到时候还请多多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#070F呵呵，彼此彼此。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    RemoveParty(0x7, 0xFF)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3F81 end

    def Function_17_44F5(): pass

    label("Function_17_44F5")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrPos(0xB, -45980, 0, 129680, 0)
    ClearChrFlags(0xB, 0x80)
    Fade(1000)
    OP_6D(-40270, -4000, 145060, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)

    ChrTalk(
        0xA,
        (
            "#800F拜托你们了，游击士的各位……\x01",
            "（※假定莱普尼兹号出发动画）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "啊，等一下～！\x02",
    )

    CloseMessageWindow()

    def lambda_45BE():
        OP_6D(-45610, -3800, 142980, 2000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_45BE)

    def lambda_45D6():

        label("loc_45D6")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_45D6")

    QueueWorkItem2(0xA, 1, lambda_45D6)
    OP_8E(0xB, 0xFFFF4A52, 0xFFFFF060, 0x23348, 0x1388, 0x0)

    ChrTalk(
        0xB,
        (
            "#150F哈哈……\x02\x03",
            "啊，走掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F哎呀……\x01",
            "朵洛希呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_8E(0xA, 0xFFFF4A2A, 0xFFFFF060, 0x22AC4, 0x7D0, 0x0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(
        0xB,
        (
            "#150F啊，工房长。\x02\x03",
            "刚才的船上，\x01",
            "艾丝蒂尔他们乘着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#800F是呀……\x01",
            "你怎么知道的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#150F游击会的\x01",
            "接待员告诉我的。\x02\x03",
            "我和编辑部连络后\x01",
            "知道了不得了的事，\x01",
            "我想不告诉他们不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#800F不得了的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#150F呀……\x01",
            "这个是公告。\x02\x03",
            "在王都的亲卫队\x01",
            "以反逆罪被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#800F什，什么？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/E0012   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_44F5 end

    def Function_18_4835(): pass

    label("Function_18_4835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5923")
    EventBegin(0x0)
    OP_A2(0x603)
    OP_28(0x54, 0x1, 0x4)
    OP_28(0x54, 0x1, 0x8)
    SetChrPos(0xC, -46060, 0, 127820, 0)
    ClearChrFlags(0xC, 0x80)

    ChrTalk(
        0xC,
        "喵～呵。\x02",
    )

    CloseMessageWindow()

    def lambda_487B():
        OP_6D(-46010, -1000, 131740, 2500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_487B)

    def lambda_4893():
        OP_67(0, 7390, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4893)

    def lambda_48AB():
        OP_6B(3700, 4000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_48AB)

    def lambda_48BB():
        OP_6C(158000, 4000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_48BB)
    Sleep(3000)
    SetChrPos(0x101, -45400, -4000, 140210, 0)
    SetChrPos(0x102, -46510, -4000, 139810, 0)

    def lambda_48F2():

        label("loc_48F2")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_48F2")

    QueueWorkItem2(0x101, 3, lambda_48F2)

    def lambda_4903():

        label("loc_4903")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_4903")

    QueueWorkItem2(0x102, 3, lambda_4903)

    def lambda_4914():
        OP_8E(0xFE, 0xFFFF4D18, 0xFFFFF060, 0x21D40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4914)

    def lambda_492F():
        OP_6D(-45610, -4000, 139000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_492F)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#000F啊，那只猫是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F就是那个时候\x01",
            "钻进集装箱里的那只猫吧。\x02\x03",
            "我记得，\x01",
            "好像是叫做安东尼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "喵呜～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F啊哈哈～真可爱。\x02\x03",
            "真是的，都是因为你，\x01",
            "害我吓了一大跳呢。\x02\x03",
            "你是不是该反省一下呢，嗯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "咪呜？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F都不听我说话啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F哈哈，说不定\x01",
            "它是在装傻呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, -47160, 0, 129750, 0)
    ClearChrFlags(0x8, 0x80)

    ChrTalk(
        0x8,
        "哦，是你们啊！\x02",
    )

    CloseMessageWindow()

    def lambda_4B01():
        OP_6D(-46010, -4000, 137720, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4B01)

    def lambda_4B19():

        label("loc_4B19")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B19")

    QueueWorkItem2(0x101, 3, lambda_4B19)

    def lambda_4B2A():

        label("loc_4B2A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B2A")

    QueueWorkItem2(0x102, 3, lambda_4B2A)

    def lambda_4B3B():
        OP_8E(0xFE, 0xFFFF4ADE, 0xFFFFF060, 0x21AD4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4B3B)
    Sleep(1000)

    def lambda_4B5B():

        label("loc_4B5B")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4B5B")

    QueueWorkItem2(0x101, 3, lambda_4B5B)

    def lambda_4B6C():

        label("loc_4B6C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4B6C")

    QueueWorkItem2(0x102, 3, lambda_4B6C)

    def lambda_4B7D():
        OP_8E(0xFE, 0xFFFF4D4A, 0x0, 0x1F521, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4B7D)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x101,
        "#000F啊，维修长先生！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F工房长都告诉我了。\x01",
            "能成功救出博士，干得真是漂亮啊。\x02\x03",
            "博士对我们这些技术人员来说，\x01",
            "算是师傅一样的人物了。\x02\x03",
            "我也要好好感谢你们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8E(0x101, 0xFFFF4F20, 0xFFFFF060, 0x21E58, 0x7D0, 0x0)
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(
        0x101,
        (
            "#000F嘿嘿，这也多亏了\x01",
            "维修长你们的帮忙啊。\x02\x03",
            "我真是被那孩子\x01",
            "吓坏了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F那个，\x01",
            "果然是你故意把它放进去的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F啊哈哈，要想欺骗敌人，\x01",
            "首先要瞒过伙伴才行啊。\x02\x03",
            "对了，\x01",
            "你们来飞艇坪有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F嗯，受博士的委托，\x01",
            "现在要赶去王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F要乘坐１１点的飞艇，\x01",
            "看来好像来得早了点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F啊啊……\x01",
            "好像要稍微迟到一会儿呢。\x02\x03",
            "因为还要花点时间卸货，\x01",
            "你们到街上再转一会儿\x01",
            "我想也没关系啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯，这样啊……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -47640, 0, 129250, 0)

    ChrTalk(
        0x9,
        "喂，你们！\x02",
    )

    CloseMessageWindow()

    def lambda_4F46():
        OP_8E(0x9, 0xFFFF4EF8, 0xFFFFF15A, 0x2189A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F46)

    def lambda_4F61():
        OP_6D(-46700, -2500, 134910, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4F61)

    def lambda_4F79():

        label("loc_4F79")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4F79")

    QueueWorkItem2(0x101, 2, lambda_4F79)

    def lambda_4F8A():

        label("loc_4F8A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4F8A")

    QueueWorkItem2(0x102, 2, lambda_4F8A)

    def lambda_4F9B():

        label("loc_4F9B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4F9B")

    QueueWorkItem2(0x8, 2, lambda_4F9B)
    Sleep(1500)

    def lambda_4FB1():

        label("loc_4FB1")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4FB1")

    QueueWorkItem2(0x101, 2, lambda_4FB1)

    def lambda_4FC2():

        label("loc_4FC2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4FC2")

    QueueWorkItem2(0x102, 2, lambda_4FC2)

    def lambda_4FD3():

        label("loc_4FD3")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_4FD3")

    QueueWorkItem2(0x8, 2, lambda_4FD3)

    def lambda_4FE4():
        OP_6D(-46010, -4000, 137720, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4FE4)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x102, 0)

    ChrTalk(
        0x8,
        (
            "#690F什么啊，这不是吉拉尔吗。\x02\x03",
            "什么事这么慌张？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "正好，\x01",
            "老爹也在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "实际上，事情变得麻烦起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#690F你说什么，麻烦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，\x01",
            "从飞艇公社来的联络说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "定期船可能要\x01",
            "晚几个小时才能到达呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F喂喂，\x01",
            "到底是怎么回事啊？\x02\x03",
            "又有空贼作乱吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "啊，说起来也差不多。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "据说，有一伙打算妨碍\x01",
            "女王的生日庆典的恐怖分子\x01",
            "不知道在哪里潜伏着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "为了调查这件事，\x01",
            "所有的空降庭都被军队设下了哨卡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F（那，那个是……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F（大概是为了\x01",
            "搜寻逃走的博士他们吧……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(
        0x9,
        (
            "所以，开往王都的飞艇\x01",
            "现在还滞留在卢安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "取而代之的好像是\x01",
            "雷斯顿要塞的军用警备飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F原来如此，是这样啊。\x02\x03",
            "不过这样一来，\x01",
            "你不是就要很忙了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(
        0x9,
        (
            "是啊，\x01",
            "不把这件事告诉旅客们不行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就因为这样，\x01",
            "你们也得再等一段时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "对了……\x01",
            "如果你们愿意在游击士协会等的话，\x01",
            "我去帮你们联系一下吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F请多指教。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFF46F6, 0x0, 0x1F8E2, 0xBB8, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrPos(0x9, -18300, 8000, 121700, 180)

    ChrTalk(
        0x8,
        (
            "#690F……真是可疑啊。\x02\x03",
            "如果军队那伙人这样干的话，\x01",
            "莱普尼兹号肯定也会被检查的。\x02\x03",
            "我这就去和工房长说这件事。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_560F():

        label("loc_560F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_560F")

    QueueWorkItem2(0x101, 2, lambda_560F)

    def lambda_5620():

        label("loc_5620")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_5620")

    QueueWorkItem2(0x102, 2, lambda_5620)

    ChrTalk(
        0x101,
        (
            "#000F对啊，要是调查昨天那件事的话\x01",
            "就不好办了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5682():

        label("loc_5682")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_5682")

    QueueWorkItem2(0x8, 2, lambda_5682)

    ChrTalk(
        0x102,
        "#010F请一定要小心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#690F哈哈，我还没有老得不中用到\x01",
            "让你们这些小孩子担心的份儿上呢。\x02\x03",
            "那么告辞了！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8E(0x8, 0xFFFF46F6, 0x0, 0x1F8E2, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F约修亚……\x01",
            "这样岂不是很危险吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F嗯……\x01",
            "这样的话乘定期船就危险了。\x02\x03",
            "虽然要花点时间，\x01",
            "还是走街道比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F呜，还以为好不容易\x01",
            "可以乘坐久违的飞艇了呢……\x02\x03",
            "我饶不了你，理查德上校！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F算了算了。\x01",
            "当成是继续修行不也很好吗？\x02\x03",
            "那么我们赶快去接待那里\x01",
            "把搭乘手续取消吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x80)
    EventEnd(0x0)

    label("loc_5923")

    Return()

    # Function_18_4835 end

    def Function_19_5924(): pass

    label("Function_19_5924")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "定期船起降坪\x01",
            "≡　开往王都格兰赛尔\x01",
            "≡　开往卢安市\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※请勿携带易燃物和危险品\x01",
            "　　　　　利贝尔飞艇公社\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_5924 end

    def Function_20_59DF(): pass

    label("Function_20_59DF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　飞艇坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "『利贝尔飞艇公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_59DF end

    SaveToFile()

Try(main)
