from ED6ScenarioHelper import *

def main():
    # 封印区域　第三层

    CreateScenaFile(
        FileName            = 'C4308   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4308.x',
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
        'ED6_DT09/CH10950 ._CH',             # 04
        'ED6_DT09/CH10951 ._CH',             # 05
        'ED6_DT09/CH10920 ._CH',             # 06
        'ED6_DT09/CH10921 ._CH',             # 07
        'ED6_DT09/CH10940 ._CH',             # 08
        'ED6_DT09/CH10941 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH11090P._CP',             # 00
        'ED6_DT09/CH11091P._CP',             # 01
        'ED6_DT09/CH11100P._CP',             # 02
        'ED6_DT09/CH11101P._CP',             # 03
        'ED6_DT09/CH10950P._CP',             # 04
        'ED6_DT09/CH10951P._CP',             # 05
        'ED6_DT09/CH10920P._CP',             # 06
        'ED6_DT09/CH10921P._CP',             # 07
        'ED6_DT09/CH10940P._CP',             # 08
        'ED6_DT09/CH10941P._CP',             # 09
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


    DeclMonster(
        X                   = -83130,
        Z                   = 0,
        Y                   = 68890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -189080,
        Z                   = 0,
        Y                   = -151150,
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
        Y                   = -1000,
        Z                   = 156000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -170000,
        Y                   = -1000,
        Z                   = 72000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -201000,
        Y                   = -1000,
        Z                   = -86000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = -265110,
        TriggerZ            = 0,
        TriggerY            = -137400,
        TriggerRange        = 1000,
        ActorX              = -265080,
        ActorZ              = 0,
        ActorY              = -136680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -187270,
        TriggerZ            = 0,
        TriggerY            = -290980,
        TriggerRange        = 1000,
        ActorX              = -188020,
        ActorZ              = 0,
        ActorY              = -291100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -129000,
        TriggerZ            = 0,
        TriggerY            = -229340,
        TriggerRange        = 1000,
        ActorX              = -129000,
        ActorZ              = 0,
        ActorY              = -228660,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21E",          # 00, 0
        "Function_1_249",          # 01, 1
        "Function_2_29E",          # 02, 2
        "Function_3_2B4",          # 03, 3
        "Function_4_343",          # 04, 4
        "Function_5_409",          # 05, 5
        "Function_6_498",          # 06, 6
        "Function_7_55E",          # 07, 7
        "Function_8_5E9",          # 08, 8
        "Function_9_6AF",          # 09, 9
        "Function_10_8C6",         # 0A, 10
        "Function_11_A14",         # 0B, 11
    )


    def Function_0_21E(): pass

    label("Function_0_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_22C")
    OP_A3(0x3FA)
    Event(0, 4)

    label("loc_22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_23A")
    OP_A3(0x3FB)
    Event(0, 6)

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_248")
    OP_A3(0x3FC)
    Event(0, 8)

    label("loc_248")

    Return()

    # Function_0_21E end

    def Function_1_249(): pass

    label("Function_1_249")

    OP_10(0x14, 0x0)
    OP_10(0x13, 0x0)
    OP_10(0x12, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264")
    OP_6F(0x5, 0)
    Jump("loc_26B")

    label("loc_264")

    OP_6F(0x5, 60)

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D")
    OP_6F(0x3, 0)
    Jump("loc_284")

    label("loc_27D")

    OP_6F(0x3, 60)

    label("loc_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296")
    OP_6F(0x4, 0)
    Jump("loc_29D")

    label("loc_296")

    OP_6F(0x4, 60)

    label("loc_29D")

    Return()

    # Function_1_249 end

    def Function_2_29E(): pass

    label("Function_2_29E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_29E")

    label("loc_2B3")

    Return()

    # Function_2_29E end

    def Function_3_2B4(): pass

    label("Function_3_2B4")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -2200, 20000, 156800, 0)
    OP_89(0x1, -3800, 20000, 156800, 0)
    OP_89(0x2, -3800, 20000, 155200, 0)
    OP_89(0x3, -2200, 20000, 155200, 0)
    OP_6D(-3000, 0, 156000, 1500)
    Sleep(100)
    OP_B0(0x0, 0x5A)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 1600)
    OP_70(0x0, 0x3E8)
    Sleep(2000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4307   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2B4 end

    def Function_4_343(): pass

    label("Function_4_343")

    EventBegin(0x0)
    SetPlaceName(0xE0) # 封印区域　第三层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 1300)
    OP_70(0x0, 0x640)
    OP_48()
    OP_89(0x0, -2200, 20000, 156800, 0)
    OP_89(0x1, -3800, 20000, 156800, 0)
    OP_89(0x2, -3800, 20000, 155200, 0)
    OP_89(0x3, -2200, 20000, 155200, 0)
    OP_6D(-3000, 0, 156000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -3030, 0, 152600, 180)
    OP_89(0x1, -3030, 0, 152600, 180)
    OP_89(0x2, -3030, 0, 152600, 180)
    OP_89(0x3, -3030, 0, 152600, 180)
    EventEnd(0x0)
    Return()

    # Function_4_343 end

    def Function_5_409(): pass

    label("Function_5_409")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -169200, 20000, 72800, 0)
    OP_89(0x1, -170800, 20000, 72800, 0)
    OP_89(0x2, -170800, 20000, 71200, 0)
    OP_89(0x3, -169200, 20000, 71200, 0)
    OP_6D(-170000, 0, 72000, 1500)
    Sleep(100)
    OP_B0(0x1, 0x5A)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x1, 1600)
    OP_70(0x1, 0x3E8)
    Sleep(2000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C4306   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_409 end

    def Function_6_498(): pass

    label("Function_6_498")

    EventBegin(0x0)
    SetPlaceName(0xE0) # 封印区域　第三层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_48()
    OP_89(0x0, -169200, 20000, 72800, 0)
    OP_89(0x1, -170800, 20000, 72800, 0)
    OP_89(0x2, -170800, 20000, 71200, 0)
    OP_89(0x3, -169200, 20000, 71200, 0)
    OP_6D(-170000, 0, 72000, 0)
    OP_73(0x1)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -166430, 0, 72020, 90)
    OP_89(0x1, -166430, 0, 72020, 90)
    OP_89(0x2, -166430, 0, 72020, 90)
    OP_89(0x3, -166430, 0, 72020, 90)
    EventEnd(0x0)
    Return()

    # Function_6_498 end

    def Function_7_55E(): pass

    label("Function_7_55E")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -200200, 20000, -86800, 0)
    OP_89(0x1, -201800, 20000, -86800, 0)
    OP_89(0x2, -201800, 20000, -85200, 0)
    OP_89(0x3, -200200, 20000, -85200, 0)
    OP_6D(-201000, 0, -86000, 1500)
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x12C)
    Sleep(4000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_55E end

    def Function_8_5E9(): pass

    label("Function_8_5E9")

    EventBegin(0x0)
    SetPlaceName(0xE0) # 封印区域　第三层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x2, 150)
    OP_70(0x2, 0x0)
    OP_48()
    OP_89(0x0, -200200, 20000, -86800, 0)
    OP_89(0x1, -201800, 20000, -86800, 0)
    OP_89(0x2, -201800, 20000, -85200, 0)
    OP_89(0x3, -200200, 20000, -85200, 0)
    OP_6D(-201000, 0, -86000, 0)
    OP_73(0x2)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -200910, 0, -89200, 180)
    OP_89(0x1, -200910, 0, -89200, 180)
    OP_89(0x2, -200910, 0, -89200, 180)
    OP_89(0x3, -200910, 0, -89200, 180)
    EventEnd(0x0)
    Return()

    # Function_8_5E9 end

    def Function_9_6AF(): pass

    label("Function_9_6AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79D")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -265080, 1500, -136680, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_6FE():
        OP_8F(0xFE, 0xFFFBF488, 0x3E8, 0xFFFDEA18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6FE)

    def lambda_719():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_719)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x313, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_778"),
        (2, "loc_78A"),
        (1, "loc_79A"),
        (SWITCH_DEFAULT, "loc_79D"),
    )


    label("loc_778")

    OP_A2(0x6AE)
    OP_6F(0x5, 60)
    Sleep(500)
    Jump("loc_79D")

    label("loc_78A")

    OP_6F(0x5, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_79A")

    OP_B4(0x0)
    Return()

    label("loc_79D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x119, 1)"), scpexpr(EXPR_END)), "loc_7F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "天神之靴\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6AD)
    Jump("loc_86A")

    label("loc_7F4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "天神之靴\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "天神之靴\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_86A")

    Jump("loc_8B8")

    label("loc_86D")

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
    OP_83(0xF, 0x62)

    label("loc_8B8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_6AF end

    def Function_10_8C6(): pass

    label("Function_10_8C6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_93D")
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
    OP_A2(0x6AF)
    Jump("loc_9B5")

    label("loc_93D")

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
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_9B5")

    Jump("loc_A06")

    label("loc_9B8")

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
    OP_83(0xF, 0x63)

    label("loc_A06")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_8C6 end

    def Function_11_A14(): pass

    label("Function_11_A14")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B06")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_A8B")
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
    OP_A2(0x6B0)
    Jump("loc_B03")

    label("loc_A8B")

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

    label("loc_B03")

    Jump("loc_B52")

    label("loc_B06")

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
    OP_83(0xF, 0x64)

    label("loc_B52")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_A14 end

    SaveToFile()

Try(main)
