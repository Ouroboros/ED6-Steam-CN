from ED6ScenarioHelper import *

def main():
    # 封印区域　第二层

    CreateScenaFile(
        FileName            = 'C4306   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4306.x',
        MapIndex            = 216,
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
        'ED6_DT09/CH10920 ._CH',             # 04
        'ED6_DT09/CH10921 ._CH',             # 05
        'ED6_DT09/CH10940 ._CH',             # 06
        'ED6_DT09/CH10941 ._CH',             # 07
        'ED6_DT09/CH11000 ._CH',             # 08
        'ED6_DT09/CH11001 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH11090P._CP',             # 00
        'ED6_DT09/CH11091P._CP',             # 01
        'ED6_DT09/CH11100P._CP',             # 02
        'ED6_DT09/CH11101P._CP',             # 03
        'ED6_DT09/CH10920P._CP',             # 04
        'ED6_DT09/CH10921P._CP',             # 05
        'ED6_DT09/CH10940P._CP',             # 06
        'ED6_DT09/CH10941P._CP',             # 07
        'ED6_DT09/CH11000P._CP',             # 08
        'ED6_DT09/CH11001P._CP',             # 09
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -231330,
        Z                   = -4000,
        Y                   = 174900,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -312320,
        Z                   = -4000,
        Y                   = 177560,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -114720,
        Z                   = -4000,
        Y                   = 169370,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -219720,
        Z                   = 0,
        Y                   = -69080,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -227710,
        Z                   = 0,
        Y                   = 48930,
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
        X                   = -200130,
        Z                   = -4000,
        Y                   = -68440,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -239000,
        Y                   = -5000,
        Z                   = 42000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -376000,
        Y                   = -1000,
        Z                   = 55000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -168000,
        Y                   = -5000,
        Z                   = 40000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = -229350,
        TriggerZ            = -4000,
        TriggerY            = 41150,
        TriggerRange        = 1000,
        ActorX              = -230090,
        ActorZ              = -4000,
        ActorY              = 40900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -156290,
        TriggerZ            = -8000,
        TriggerY            = 39000,
        TriggerRange        = 1000,
        ActorX              = -157060,
        ActorZ              = -8000,
        ActorY              = 38850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -317160,
        TriggerZ            = -4000,
        TriggerY            = 256510,
        TriggerRange        = 1000,
        ActorX              = -317010,
        ActorZ              = -4000,
        ActorY              = 257160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -368260,
        TriggerZ            = -4000,
        TriggerY            = 188860,
        TriggerRange        = 1000,
        ActorX              = -368940,
        ActorZ              = -4000,
        ActorY              = 188980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -82670,
        TriggerZ            = -8000,
        TriggerY            = -135220,
        TriggerRange        = 1000,
        ActorX              = -82050,
        ActorZ              = -8000,
        ActorY              = -135090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2F6",          # 00, 0
        "Function_1_321",          # 01, 1
        "Function_2_3A8",          # 02, 2
        "Function_3_3BE",          # 03, 3
        "Function_4_44D",          # 04, 4
        "Function_5_513",          # 05, 5
        "Function_6_5A2",          # 06, 6
        "Function_7_668",          # 07, 7
        "Function_8_6F3",          # 08, 8
        "Function_9_7B9",          # 09, 9
        "Function_10_9E3",         # 0A, 10
        "Function_11_BEA",         # 0B, 11
        "Function_12_D3F",         # 0C, 12
        "Function_13_E82",         # 0D, 13
    )


    def Function_0_2F6(): pass

    label("Function_0_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_304")
    OP_A3(0x3FA)
    Event(0, 4)

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_312")
    OP_A3(0x3FB)
    Event(0, 6)

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_320")
    OP_A3(0x3FC)
    Event(0, 8)

    label("loc_320")

    Return()

    # Function_0_2F6 end

    def Function_1_321(): pass

    label("Function_1_321")

    OP_10(0x22, 0x0)
    OP_10(0x23, 0x0)
    OP_10(0x24, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C")
    OP_6F(0x3, 0)
    Jump("loc_343")

    label("loc_33C")

    OP_6F(0x3, 60)

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355")
    OP_6F(0x6, 0)
    Jump("loc_35C")

    label("loc_355")

    OP_6F(0x6, 60)

    label("loc_35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E")
    OP_6F(0x4, 0)
    Jump("loc_375")

    label("loc_36E")

    OP_6F(0x4, 60)

    label("loc_375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_387")
    OP_6F(0x5, 0)
    Jump("loc_38E")

    label("loc_387")

    OP_6F(0x5, 60)

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0")
    OP_6F(0x7, 0)
    Jump("loc_3A7")

    label("loc_3A0")

    OP_6F(0x7, 60)

    label("loc_3A7")

    Return()

    # Function_1_321 end

    def Function_2_3A8(): pass

    label("Function_2_3A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3A8")

    label("loc_3BD")

    Return()

    # Function_2_3A8 end

    def Function_3_3BE(): pass

    label("Function_3_3BE")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -238200, 20000, 42800, 0)
    OP_89(0x1, -240000, 20000, 42800, 0)
    OP_89(0x2, -240000, 20000, 41200, 0)
    OP_89(0x3, -238200, 20000, 41200, 0)
    OP_6D(-239000, -4000, 42000, 1500)
    Sleep(100)
    OP_B0(0x0, 0x5A)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 1600)
    OP_70(0x0, 0x3E8)
    Sleep(2000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4305   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3BE end

    def Function_4_44D(): pass

    label("Function_4_44D")

    EventBegin(0x0)
    SetPlaceName(0xDF) # 封印区域　第二层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 1300)
    OP_70(0x0, 0x640)
    OP_48()
    OP_89(0x0, -238200, 20000, 42800, 0)
    OP_89(0x1, -238200, 20000, 41200, 0)
    OP_89(0x2, -239800, 20000, 42800, 0)
    OP_89(0x3, -239800, 20000, 41200, 0)
    OP_6D(-239000, -4000, 42000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -238960, -4000, 45410, 0)
    OP_89(0x1, -238960, -4000, 45410, 0)
    OP_89(0x2, -238960, -4000, 45410, 0)
    OP_89(0x3, -238960, -4000, 45410, 0)
    EventEnd(0x0)
    Return()

    # Function_4_44D end

    def Function_5_513(): pass

    label("Function_5_513")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -375200, 20000, 55800, 0)
    OP_89(0x1, -376800, 20000, 55800, 0)
    OP_89(0x2, -376800, 20000, 54200, 0)
    OP_89(0x3, -375200, 20000, 54200, 0)
    OP_6D(-376000, 0, 55000, 1500)
    Sleep(100)
    OP_B0(0x1, 0x5A)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x1, 1600)
    OP_70(0x1, 0x3E8)
    Sleep(2000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4305   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_513 end

    def Function_6_5A2(): pass

    label("Function_6_5A2")

    EventBegin(0x0)
    SetPlaceName(0xDF) # 封印区域　第二层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x1, 1300)
    OP_70(0x1, 0x640)
    OP_48()
    OP_89(0x0, -375200, 20000, 55800, 0)
    OP_89(0x1, -376800, 20000, 55800, 0)
    OP_89(0x2, -376800, 20000, 54200, 0)
    OP_89(0x3, -375200, 20000, 54200, 0)
    OP_6D(-376000, 0, 55000, 0)
    OP_73(0x1)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -372650, 0, 55060, 90)
    OP_89(0x1, -372650, 0, 55060, 90)
    OP_89(0x2, -372650, 0, 55060, 90)
    OP_89(0x3, -372650, 0, 55060, 90)
    EventEnd(0x0)
    Return()

    # Function_6_5A2 end

    def Function_7_668(): pass

    label("Function_7_668")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -167200, 20000, 40800, 0)
    OP_89(0x1, -168800, 20000, 40800, 0)
    OP_89(0x2, -168800, 20000, 39200, 0)
    OP_89(0x3, -167200, 20000, 39200, 0)
    OP_6D(-168000, -4000, 40000, 1500)
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x12C)
    Sleep(2000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4308   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_668 end

    def Function_8_6F3(): pass

    label("Function_8_6F3")

    EventBegin(0x0)
    SetPlaceName(0xDF) # 封印区域　第二层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x2, 150)
    OP_70(0x2, 0x0)
    OP_48()
    OP_89(0x0, -167200, 20000, 40800, 0)
    OP_89(0x1, -168800, 20000, 40800, 0)
    OP_89(0x2, -168800, 20000, 39200, 0)
    OP_89(0x3, -167200, 20000, 39200, 0)
    OP_6D(-168000, -4000, 40000, 0)
    OP_73(0x2)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -171410, -4000, 39970, 270)
    OP_89(0x1, -171410, -4000, 39970, 270)
    OP_89(0x2, -171410, -4000, 39970, 270)
    OP_89(0x3, -171410, -4000, 39970, 270)
    EventEnd(0x0)
    Return()

    # Function_8_6F3 end

    def Function_9_7B9(): pass

    label("Function_9_7B9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_980")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A7")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -230090, -1500, 40900, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_808():
        OP_8F(0xFE, 0xFFFC7D36, 0xFFFFF448, 0x9FC4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_808)

    def lambda_823():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_823)
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
        (0, "loc_882"),
        (2, "loc_894"),
        (1, "loc_8A4"),
        (SWITCH_DEFAULT, "loc_8A7"),
    )


    label("loc_882")

    OP_A2(0x6B9)
    OP_6F(0x3, 60)
    Sleep(500)
    Jump("loc_8A7")

    label("loc_894")

    OP_6F(0x3, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_8A4")

    OP_B4(0x0)
    Return()

    label("loc_8A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xBB, 1)"), scpexpr(EXPR_END)), "loc_901")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "高能量粒子炮\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6B8)
    Jump("loc_97D")

    label("loc_901")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "高能量粒子炮\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "高能量粒子炮\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_97D")

    Jump("loc_9D5")

    label("loc_980")

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
    OP_83(0xF, 0x59)

    label("loc_9D5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_7B9 end

    def Function_10_9E3(): pass

    label("Function_10_9E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD1")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, -157060, -5500, 38850, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_A32():
        OP_8F(0xFE, 0xFFFD9A7C, 0xFFFFE4A8, 0x97C2, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A32)

    def lambda_A4D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A4D)
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
        (0, "loc_AAC"),
        (2, "loc_ABE"),
        (1, "loc_ACE"),
        (SWITCH_DEFAULT, "loc_AD1"),
    )


    label("loc_AAC")

    OP_A2(0x6BB)
    OP_6F(0x6, 60)
    Sleep(500)
    Jump("loc_AD1")

    label("loc_ABE")

    OP_6F(0x6, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_ACE")

    OP_B4(0x0)
    Return()

    label("loc_AD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x119, 1)"), scpexpr(EXPR_END)), "loc_B28")
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
    OP_A2(0x6BA)
    Jump("loc_B9E")

    label("loc_B28")

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
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_B9E")

    Jump("loc_BDC")

    label("loc_BA1")

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
    OP_83(0xF, 0x5A)

    label("loc_BDC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_9E3 end

    def Function_11_BEA(): pass

    label("Function_11_BEA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_C61")
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
    OP_A2(0x6BC)
    Jump("loc_CD9")

    label("loc_C61")

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

    label("loc_CD9")

    Jump("loc_D31")

    label("loc_CDC")

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
    OP_83(0xF, 0x5B)

    label("loc_D31")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_BEA end

    def Function_12_D3F(): pass

    label("Function_12_D3F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E31")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_DB6")
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
    OP_A2(0x6BD)
    Jump("loc_E2E")

    label("loc_DB6")

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

    label("loc_E2E")

    Jump("loc_E74")

    label("loc_E31")

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
    OP_83(0xF, 0x5C)

    label("loc_E74")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_D3F end

    def Function_13_E82(): pass

    label("Function_13_E82")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_EFC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "全回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6BE)
    Jump("loc_F7A")

    label("loc_EFC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "全回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "全回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_F7A")

    Jump("loc_FC8")

    label("loc_F7D")

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
    OP_83(0xF, 0x5D)

    label("loc_FC8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_E82 end

    SaveToFile()

Try(main)
