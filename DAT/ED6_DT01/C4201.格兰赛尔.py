from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        'ED6_DT09/CH10490 ._CH',             # 00
        'ED6_DT09/CH10491 ._CH',             # 01
        'ED6_DT09/CH10500 ._CH',             # 02
        'ED6_DT09/CH10501 ._CH',             # 03
        'ED6_DT09/CH10510 ._CH',             # 04
        'ED6_DT09/CH10511 ._CH',             # 05
        'ED6_DT09/CH11110 ._CH',             # 06
        'ED6_DT09/CH11111 ._CH',             # 07
        'ED6_DT09/CH11120 ._CH',             # 08
        'ED6_DT09/CH11121 ._CH',             # 09
        'ED6_DT09/CH11130 ._CH',             # 0A
        'ED6_DT09/CH11131 ._CH',             # 0B
        'ED6_DT09/CH11140 ._CH',             # 0C
        'ED6_DT09/CH11141 ._CH',             # 0D
        'ED6_DT09/CH11150 ._CH',             # 0E
        'ED6_DT09/CH11151 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10490P._CP',             # 00
        'ED6_DT09/CH10491P._CP',             # 01
        'ED6_DT09/CH10500P._CP',             # 02
        'ED6_DT09/CH10501P._CP',             # 03
        'ED6_DT09/CH10510P._CP',             # 04
        'ED6_DT09/CH10511P._CP',             # 05
        'ED6_DT09/CH11110P._CP',             # 06
        'ED6_DT09/CH11111P._CP',             # 07
        'ED6_DT09/CH11120P._CP',             # 08
        'ED6_DT09/CH11121P._CP',             # 09
        'ED6_DT09/CH11130P._CP',             # 0A
        'ED6_DT09/CH11131P._CP',             # 0B
        'ED6_DT09/CH11140P._CP',             # 0C
        'ED6_DT09/CH11141P._CP',             # 0D
        'ED6_DT09/CH11150P._CP',             # 0E
        'ED6_DT09/CH11151P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 119050,
        Z                   = 0,
        Y                   = 5990,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 140780,
        Z                   = 1000,
        Y                   = -151350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 139310,
        Z                   = 0,
        Y                   = 6070,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 104120,
        Z                   = 0,
        Y                   = 13980,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x27B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 119050,
        Y                   = -1000,
        Z                   = 5990,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = 140780,
        Y                   = 0,
        Z                   = -151350,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 128250,
        TriggerZ            = 0,
        TriggerY            = -152730,
        TriggerRange        = 1000,
        ActorX              = 127270,
        ActorZ              = 1500,
        ActorY              = -152920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 118070,
        TriggerZ            = 0,
        TriggerY            = 19130,
        TriggerRange        = 1000,
        ActorX              = 118680,
        ActorZ              = 1500,
        ActorY              = 19250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 123780,
        TriggerZ            = 0,
        TriggerY            = 19220,
        TriggerRange        = 1000,
        ActorX              = 122910,
        ActorZ              = 1500,
        ActorY              = 19200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103870,
        TriggerZ            = 0,
        TriggerY            = 24400,
        TriggerRange        = 1000,
        ActorX              = 103830,
        ActorZ              = 1500,
        ActorY              = 24960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 136410,
        TriggerZ            = 0,
        TriggerY            = -112150,
        TriggerRange        = 1000,
        ActorX              = 137180,
        ActorZ              = 1500,
        ActorY              = -112180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_2D7",          # 01, 1
        "Function_2_384",          # 02, 2
        "Function_3_452",          # 03, 3
        "Function_4_4E0",          # 04, 4
        "Function_5_7C0",          # 05, 5
        "Function_6_A92",          # 06, 6
        "Function_7_C8A",          # 07, 7
        "Function_8_E74",          # 08, 8
        "Function_9_FC2",          # 09, 9
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    Return()

    # Function_0_2D6 end

    def Function_1_2D7(): pass

    label("Function_1_2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_END)), "loc_2EC")
    OP_6F(0x0, 240)
    OP_6F(0x3, 120)

    label("loc_2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE")
    OP_6F(0x1, 0)
    Jump("loc_305")

    label("loc_2FE")

    OP_6F(0x1, 60)

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_317")
    OP_6F(0x2, 0)
    Jump("loc_31E")

    label("loc_317")

    OP_6F(0x2, 60)

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330")
    OP_6F(0x4, 0)
    Jump("loc_337")

    label("loc_330")

    OP_6F(0x4, 60)

    label("loc_337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349")
    OP_6F(0x5, 0)
    Jump("loc_350")

    label("loc_349")

    OP_6F(0x5, 60)

    label("loc_350")

    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_367")
    ClearChrFlags(0xA, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_367")

    OP_B2(0x0, 0x1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E")
    ClearChrFlags(0xB, 0x80)
    OP_B2(0x1, 0x1, 0x80)

    label("loc_37E")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_2D7 end

    def Function_2_384(): pass

    label("Function_2_384")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_43C")

    label("loc_3A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C2")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_43C")

    label("loc_3C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_43C")

    label("loc_3DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F4")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_43C")

    label("loc_3F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40D")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_43C")

    label("loc_40D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_426")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_43C")

    label("loc_426")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_43C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_451")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_43C")

    label("loc_451")

    Return()

    # Function_2_384 end

    def Function_3_452(): pass

    label("Function_3_452")

    SetMapFlags(0x80)
    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7")
    EventBegin(0x0)
    OP_22(0x64, 0x0, 0x64)
    OP_6F(0x3, 65)
    OP_70(0x3, 0x78)
    OP_73(0x3)
    OP_6F(0x3, 120)
    Sleep(500)
    OP_6D(128919, 0, -146150, 2000)
    OP_22(0xD0, 0x0, 0x64)
    OP_70(0x0, 0xF0)
    OP_73(0x0)
    OP_6F(0x0, 240)
    OP_A2(0x681)
    EventEnd(0x1)
    Jump("loc_4D7")

    label("loc_4B7")


    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "控制杆纹丝不动。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4D7")

    OP_73(0x3)
    ClearMapFlags(0x80)
    Return()

    # Function_3_452 end

    def Function_4_4E0(): pass

    label("Function_4_4E0")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "成群凶暴的魔兽正在四处游荡中。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5E5"),
        (SWITCH_DEFAULT, "loc_67F"),
    )


    label("loc_5E5")

    Fade(1000)
    SetChrPos(0x0, 112770, 0, 5750, 90)
    SetChrPos(0x1, 112770, 0, 5750, 90)
    SetChrPos(0x2, 112770, 0, 5750, 90)
    SetChrPos(0x3, 112770, 0, 5750, 90)
    SetChrPos(0x4, 112770, 0, 5750, 90)
    SetChrPos(0x5, 112770, 0, 5750, 90)
    SetChrPos(0x6, 112770, 0, 5750, 90)
    SetChrPos(0x7, 112770, 0, 5750, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_67F")

    Battle(0x401, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, 112770, 0, 5750, 90)
    SetChrPos(0x1, 112770, 0, 5750, 90)
    SetChrPos(0x2, 112770, 0, 5750, 90)
    SetChrPos(0x3, 112770, 0, 5750, 90)
    SetChrPos(0x4, 112770, 0, 5750, 90)
    SetChrPos(0x5, 112770, 0, 5750, 90)
    SetChrPos(0x6, 112770, 0, 5750, 90)
    SetChrPos(0x7, 112770, 0, 5750, 90)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_72D"),
        (1, "loc_730"),
        (SWITCH_DEFAULT, "loc_733"),
    )


    label("loc_72D")

    EventEnd(0x0)
    Return()

    label("loc_730")

    OP_B4(0x0)
    Return()

    label("loc_733")

    EventBegin(0x1)
    SetChrFlags(0xA, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "成功消灭了地下水路·西部区域中被通缉的魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x6E5)
    OP_28(0x50, 0x4, 0x10)
    OP_28(0x50, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_4_4E0 end

    def Function_5_7C0(): pass

    label("Function_5_7C0")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡中。\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_8B8"),
        (SWITCH_DEFAULT, "loc_952"),
    )


    label("loc_8B8")

    Fade(1000)
    SetChrPos(0x0, 140780, 0, -157740, 0)
    SetChrPos(0x1, 140780, 0, -157740, 0)
    SetChrPos(0x2, 140780, 0, -157740, 0)
    SetChrPos(0x3, 140780, 0, -157740, 0)
    SetChrPos(0x4, 140780, 0, -157740, 0)
    SetChrPos(0x5, 140780, 0, -157740, 0)
    SetChrPos(0x6, 140780, 0, -157740, 0)
    SetChrPos(0x7, 140780, 0, -157740, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_952")

    Battle(0x402, 0x0, 0x0, 0x0, 0xFF)
    SetChrPos(0x0, 140780, 0, -157740, 0)
    SetChrPos(0x1, 140780, 0, -157740, 0)
    SetChrPos(0x2, 140780, 0, -157740, 0)
    SetChrPos(0x3, 140780, 0, -157740, 0)
    SetChrPos(0x4, 140780, 0, -157740, 0)
    SetChrPos(0x5, 140780, 0, -157740, 0)
    SetChrPos(0x6, 140780, 0, -157740, 0)
    SetChrPos(0x7, 140780, 0, -157740, 0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_A00"),
        (1, "loc_A03"),
        (SWITCH_DEFAULT, "loc_A06"),
    )


    label("loc_A00")

    EventEnd(0x0)
    Return()

    label("loc_A03")

    OP_B4(0x0)
    Return()

    label("loc_A06")

    EventBegin(0x1)
    SetChrFlags(0xB, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "成功消灭了地下水路·东部区域中被通缉的魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x6E6)
    OP_28(0x51, 0x4, 0x10)
    OP_28(0x51, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_5_7C0 end

    def Function_6_A92(): pass

    label("Function_6_A92")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C41")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B74")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 118680, 3000, 19250, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_AE1():
        OP_8F(0xFE, 0x1CF98, 0x5DC, 0x4B32, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AE1)

    def lambda_AFC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AFC)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x270, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B4F"),
        (2, "loc_B61"),
        (1, "loc_B71"),
        (SWITCH_DEFAULT, "loc_B74"),
    )


    label("loc_B4F")

    OP_A2(0x6D3)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_B74")

    label("loc_B61")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_B71")

    OP_B4(0x0)
    Return()

    label("loc_B74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xFB, 1)"), scpexpr(EXPR_END)), "loc_BCA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "反射大衣\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6D2)
    Jump("loc_C3E")

    label("loc_BCA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "反射大衣\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "反射大衣\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_C3E")

    Jump("loc_C7C")

    label("loc_C41")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x43)

    label("loc_C7C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A92 end

    def Function_7_C8A(): pass

    label("Function_7_C8A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E30")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6C")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 122910, 3000, 19200, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_CD9():
        OP_8F(0xFE, 0x1E01E, 0x5DC, 0x4B00, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CD9)

    def lambda_CF4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CF4)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔兽出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x279, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D47"),
        (2, "loc_D59"),
        (1, "loc_D69"),
        (SWITCH_DEFAULT, "loc_D6C"),
    )


    label("loc_D47")

    OP_A2(0x6D5)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_D6C")

    label("loc_D59")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D69")

    OP_B4(0x0)
    Return()

    label("loc_D6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xD5, 1)"), scpexpr(EXPR_END)), "loc_DBF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "拳斗士手套\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6D4)
    Jump("loc_E2D")

    label("loc_DBF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "拳斗士手套\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "拳斗士手套\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_E2D")

    Jump("loc_E66")

    label("loc_E30")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x44)

    label("loc_E66")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C8A end

    def Function_8_E74(): pass

    label("Function_8_E74")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F66")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_EEB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6D6)
    Jump("loc_F63")

    label("loc_EEB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_F63")

    Jump("loc_FB4")

    label("loc_F66")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x45)

    label("loc_FB4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_E74 end

    def Function_9_FC2(): pass

    label("Function_9_FC2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1039")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "大回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6D7)
    Jump("loc_10B1")

    label("loc_1039")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "大回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "大回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_10B1")

    Jump("loc_1107")

    label("loc_10B4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x46)

    label("loc_1107")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_FC2 end

    SaveToFile()

Try(main)
