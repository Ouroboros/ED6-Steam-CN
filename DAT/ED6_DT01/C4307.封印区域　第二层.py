from ED6ScenarioHelper import *

def main():
    # 封印区域　第二层

    CreateScenaFile(
        FileName            = 'C4307   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4307.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60035",
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
        'ED6_DT09/CH11090 ._CH',             # 00
        'ED6_DT09/CH11091 ._CH',             # 01
        'ED6_DT09/CH11100 ._CH',             # 02
        'ED6_DT09/CH11101 ._CH',             # 03
        'ED6_DT09/CH10940 ._CH',             # 04
        'ED6_DT09/CH10941 ._CH',             # 05
        'ED6_DT09/CH11000 ._CH',             # 06
        'ED6_DT09/CH11001 ._CH',             # 07
        'ED6_DT09/CH10920 ._CH',             # 08
        'ED6_DT09/CH10921 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH11090P._CP',             # 00
        'ED6_DT09/CH11091P._CP',             # 01
        'ED6_DT09/CH11100P._CP',             # 02
        'ED6_DT09/CH11101P._CP',             # 03
        'ED6_DT09/CH10940P._CP',             # 04
        'ED6_DT09/CH10941P._CP',             # 05
        'ED6_DT09/CH11000P._CP',             # 06
        'ED6_DT09/CH11001P._CP',             # 07
        'ED6_DT09/CH10920P._CP',             # 08
        'ED6_DT09/CH10921P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -1320,
        Z                   = -8000,
        Y                   = -82980,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 84650,
        Z                   = -8000,
        Y                   = 22370,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -3000,
        Y                   = -9000,
        Z                   = 124000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -40770,
        TriggerZ            = -8000,
        TriggerY            = -12300,
        TriggerRange        = 1000,
        ActorX              = -41050,
        ActorZ              = -8000,
        ActorY              = -13100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15250,
        TriggerZ            = -8000,
        TriggerY            = -12250,
        TriggerRange        = 1000,
        ActorX              = 14900,
        ActorZ              = -8000,
        ActorY              = -12990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43320,
        TriggerZ            = -8000,
        TriggerY            = 38970,
        TriggerRange        = 1000,
        ActorX              = 44000,
        ActorZ              = -8000,
        ActorY              = 38940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3160,
        TriggerZ            = -8000,
        TriggerY            = 131230,
        TriggerRange        = 1000,
        ActorX              = -3090,
        ActorZ              = -8000,
        ActorY              = 131910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_231",          # 01, 1
        "Function_2_299",          # 02, 2
        "Function_3_2AF",          # 03, 3
        "Function_4_33A",          # 04, 4
        "Function_5_400",          # 05, 5
        "Function_6_629",          # 06, 6
        "Function_7_843",          # 07, 7
        "Function_8_A53",          # 08, 8
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_230")
    OP_A3(0x3FA)
    Event(0, 4)

    label("loc_230")

    Return()

    # Function_0_222 end

    def Function_1_231(): pass

    label("Function_1_231")

    OP_10(0x10, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246")
    OP_6F(0x1, 0)
    Jump("loc_24D")

    label("loc_246")

    OP_6F(0x1, 60)

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F")
    OP_6F(0x2, 0)
    Jump("loc_266")

    label("loc_25F")

    OP_6F(0x2, 60)

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278")
    OP_6F(0x3, 0)
    Jump("loc_27F")

    label("loc_278")

    OP_6F(0x3, 60)

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291")
    OP_6F(0x4, 0)
    Jump("loc_298")

    label("loc_291")

    OP_6F(0x4, 60)

    label("loc_298")

    Return()

    # Function_1_231 end

    def Function_2_299(): pass

    label("Function_2_299")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2AE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_299")

    label("loc_2AE")

    Return()

    # Function_2_299 end

    def Function_3_2AF(): pass

    label("Function_3_2AF")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -2200, 20000, 124800, 0)
    OP_89(0x1, -3800, 20000, 124800, 0)
    OP_89(0x2, -3800, 20000, 123200, 0)
    OP_89(0x3, -2200, 20000, 123200, 0)
    OP_6D(-3000, -8000, 124000, 1500)
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x12C)
    Sleep(2000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4308   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2AF end

    def Function_4_33A(): pass

    label("Function_4_33A")

    EventBegin(0x0)
    SetPlaceName(0xDF) # 封印区域　第二层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 150)
    OP_70(0x0, 0x0)
    OP_48()
    OP_89(0x0, -2200, 20000, 124800, 0)
    OP_89(0x1, -3800, 20000, 124800, 0)
    OP_89(0x2, -3800, 20000, 123200, 0)
    OP_89(0x3, -2200, 20000, 123200, 0)
    OP_6D(-3000, -8000, 124000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, 480, -8000, 124010, 90)
    OP_89(0x1, 480, -8000, 124010, 90)
    OP_89(0x2, 480, -8000, 124010, 90)
    OP_89(0x3, 480, -8000, 124010, 90)
    EventEnd(0x0)
    Return()

    # Function_4_33A end

    def Function_5_400(): pass

    label("Function_5_400")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -41050, -5500, -13100, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_44F():
        OP_8F(0xFE, 0xFFFF5FA6, 0xFFFFE4A8, 0xFFFFCCD4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_44F)

    def lambda_46A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_46A)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x311, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4C9"),
        (2, "loc_4DB"),
        (1, "loc_4EB"),
        (SWITCH_DEFAULT, "loc_4EE"),
    )


    label("loc_4C9")

    OP_A2(0x6B2)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_4EE")

    label("loc_4DB")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_4EB")

    OP_B4(0x0)
    Return()

    label("loc_4EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x11A, 1)"), scpexpr(EXPR_END)), "loc_548")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "风神之靴\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6B1)
    Jump("loc_5C4")

    label("loc_548")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "风神之靴\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "风神之靴\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_5C4")

    Jump("loc_61B")

    label("loc_5C7")

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
    OP_83(0xF, 0x5E)

    label("loc_61B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_400 end

    def Function_6_629(): pass

    label("Function_6_629")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_717")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 14900, -5500, -12990, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_678():
        OP_8F(0xFE, 0x3A34, 0xFFFFE4A8, 0xFFFFCD42, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_678)

    def lambda_693():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_693)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x30F, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6F2"),
        (2, "loc_704"),
        (1, "loc_714"),
        (SWITCH_DEFAULT, "loc_717"),
    )


    label("loc_6F2")

    OP_A2(0x6B4)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_717")

    label("loc_704")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_714")

    OP_B4(0x0)
    Return()

    label("loc_717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x80, 1)"), scpexpr(EXPR_END)), "loc_76E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "水晶剑\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6B3)
    Jump("loc_7E4")

    label("loc_76E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "水晶剑\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "水晶剑\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_7E4")

    Jump("loc_835")

    label("loc_7E7")

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
    OP_83(0xF, 0x5F)

    label("loc_835")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_629 end

    def Function_7_843(): pass

    label("Function_7_843")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_931")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 44000, -5500, 38940, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_892():
        OP_8F(0xFE, 0xABE0, 0xFFFFE4A8, 0x981C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_892)

    def lambda_8AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8AD)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x311, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_90C"),
        (2, "loc_91E"),
        (1, "loc_92E"),
        (SWITCH_DEFAULT, "loc_931"),
    )


    label("loc_90C")

    OP_A2(0x6B6)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_931")

    label("loc_91E")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_92E")

    OP_B4(0x0)
    Return()

    label("loc_931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xFE, 1)"), scpexpr(EXPR_END)), "loc_98C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "女武神战甲\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6B5)
    Jump("loc_A0A")

    label("loc_98C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "女武神战甲\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "女武神战甲\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_A0A")

    Jump("loc_A45")

    label("loc_A0D")

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
    OP_83(0xF, 0x60)

    label("loc_A45")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_843 end

    def Function_8_A53(): pass

    label("Function_8_A53")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B45")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_ACA")
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
    OP_A2(0x6B7)
    Jump("loc_B42")

    label("loc_ACA")

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

    label("loc_B42")

    Jump("loc_B7E")

    label("loc_B45")

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
    OP_83(0xF, 0x61)

    label("loc_B7E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A53 end

    SaveToFile()

Try(main)
