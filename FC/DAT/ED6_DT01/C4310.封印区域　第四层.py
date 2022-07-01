from ED6ScenarioHelper import *

def main():
    # 封印区域　第四层

    CreateScenaFile(
        FileName            = 'C4310   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4310.x',
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
        'ED6_DT09/CH10920 ._CH',             # 04
        'ED6_DT09/CH10921 ._CH',             # 05
        'ED6_DT09/CH10940 ._CH',             # 06
        'ED6_DT09/CH10941 ._CH',             # 07
        'ED6_DT09/CH10950 ._CH',             # 08
        'ED6_DT09/CH10951 ._CH',             # 09
        'ED6_DT09/CH10990 ._CH',             # 0A
        'ED6_DT09/CH10991 ._CH',             # 0B
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
        'ED6_DT09/CH10950P._CP',             # 08
        'ED6_DT09/CH10951P._CP',             # 09
        'ED6_DT09/CH10990P._CP',             # 0A
        'ED6_DT09/CH10991P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        X                   = -201120,
        Z                   = 0,
        Y                   = -162390,
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
        X                   = -112960,
        Z                   = 0,
        Y                   = -242130,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x292,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -201000,
        Y                   = -1000,
        Z                   = -86000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 40890,
        TriggerZ            = 0,
        TriggerY            = -264350,
        TriggerRange        = 1000,
        ActorX              = 40980,
        ActorZ              = 0,
        ActorY              = -263640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -31240,
        TriggerZ            = 0,
        TriggerY            = -394340,
        TriggerRange        = 1000,
        ActorX              = -31150,
        ActorZ              = 0,
        ActorY              = -395080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -273090,
        TriggerZ            = 0,
        TriggerY            = -231510,
        TriggerRange        = 1000,
        ActorX              = -272960,
        ActorZ              = 0,
        ActorY              = -230820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -198990,
        TriggerZ            = 0,
        TriggerY            = -287980,
        TriggerRange        = 1000,
        ActorX              = -199140,
        ActorZ              = 0,
        ActorY              = -288780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -151070,
        TriggerZ            = 0,
        TriggerY            = -263420,
        TriggerRange        = 1000,
        ActorX              = -151090,
        ActorZ              = 0,
        ActorY              = -262790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -33050,
        TriggerZ            = 0,
        TriggerY            = -271460,
        TriggerRange        = 1000,
        ActorX              = -33050,
        ActorZ              = 0,
        ActorY              = -270780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 110870,
        TriggerZ            = 0,
        TriggerY            = -327410,
        TriggerRange        = 1000,
        ActorX              = 111060,
        ActorZ              = 0,
        ActorY              = -326790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 81310,
        TriggerZ            = 0,
        TriggerY            = -385050,
        TriggerRange        = 1000,
        ActorX              = 81950,
        ActorZ              = 0,
        ActorY              = -385040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31260,
        TriggerZ            = 0,
        TriggerY            = -385140,
        TriggerRange        = 1000,
        ActorX              = 31920,
        ActorZ              = 0,
        ActorY              = -385090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2E6",          # 00, 0
        "Function_1_2F5",          # 01, 1
        "Function_2_3DF",          # 02, 2
        "Function_3_3F5",          # 03, 3
        "Function_4_484",          # 04, 4
        "Function_5_54A",          # 05, 5
        "Function_6_742",          # 06, 6
        "Function_7_955",          # 07, 7
        "Function_8_A99",          # 08, 8
        "Function_9_BEA",          # 09, 9
        "Function_10_D29",         # 0A, 10
        "Function_11_E71",         # 0B, 11
        "Function_12_FC3",         # 0C, 12
        "Function_13_10F9",        # 0D, 13
    )


    def Function_0_2E6(): pass

    label("Function_0_2E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_2F4")
    OP_A3(0x3FA)
    Event(0, 4)

    label("loc_2F4")

    Return()

    # Function_0_2E6 end

    def Function_1_2F5(): pass

    label("Function_1_2F5")

    OP_10(0x21, 0x0)
    OP_72(0x0, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F")
    OP_6F(0x5, 0)
    Jump("loc_316")

    label("loc_30F")

    OP_6F(0x5, 60)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_6F(0x9, 0)
    Jump("loc_32F")

    label("loc_328")

    OP_6F(0x9, 60)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x1, 0)
    Jump("loc_348")

    label("loc_341")

    OP_6F(0x1, 60)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    OP_6F(0x2, 0)
    Jump("loc_361")

    label("loc_35A")

    OP_6F(0x2, 60)

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373")
    OP_6F(0x3, 0)
    Jump("loc_37A")

    label("loc_373")

    OP_6F(0x3, 60)

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38C")
    OP_6F(0x4, 0)
    Jump("loc_393")

    label("loc_38C")

    OP_6F(0x4, 60)

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5")
    OP_6F(0x6, 0)
    Jump("loc_3AC")

    label("loc_3A5")

    OP_6F(0x6, 60)

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE")
    OP_6F(0x7, 0)
    Jump("loc_3C5")

    label("loc_3BE")

    OP_6F(0x7, 60)

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7")
    OP_6F(0x8, 0)
    Jump("loc_3DE")

    label("loc_3D7")

    OP_6F(0x8, 60)

    label("loc_3DE")

    Return()

    # Function_1_2F5 end

    def Function_2_3DF(): pass

    label("Function_2_3DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3DF")

    label("loc_3F4")

    Return()

    # Function_2_3DF end

    def Function_3_3F5(): pass

    label("Function_3_3F5")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -200200, 20000, -86800, 0)
    OP_89(0x1, -201800, 20000, -86800, 0)
    OP_89(0x2, -201800, 20000, -85200, 0)
    OP_89(0x3, -200200, 20000, -85200, 0)
    OP_6D(-201000, 0, -86000, 1500)
    Sleep(100)
    OP_B0(0x0, 0x5A)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 1600)
    OP_70(0x0, 0x3E8)
    Sleep(2000)
    OP_A2(0x3FC)
    NewScene("ED6_DT01/C4308   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3F5 end

    def Function_4_484(): pass

    label("Function_4_484")

    EventBegin(0x0)
    SetPlaceName(0xE1) # 封印区域　第四层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 1300)
    OP_70(0x0, 0x640)
    OP_48()
    OP_89(0x0, -200200, 20000, -86800, 0)
    OP_89(0x1, -201800, 20000, -86800, 0)
    OP_89(0x2, -201800, 20000, -85200, 0)
    OP_89(0x3, -200200, 20000, -85200, 0)
    OP_6D(-201000, 0, -86000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    OP_89(0x0, -201020, 0, -89200, 180)
    OP_89(0x1, -201020, 0, -89200, 180)
    OP_89(0x2, -201020, 0, -89200, 180)
    OP_89(0x3, -201020, 0, -89200, 180)
    EventEnd(0x0)
    Return()

    # Function_4_484 end

    def Function_5_54A(): pass

    label("Function_5_54A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_638")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 40980, 1500, -263640, 320)
    TurnDirection(0x8, 0x0, 0)

    def lambda_599():
        OP_8F(0xFE, 0xA014, 0x3E8, 0xFFFBFA28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_599)

    def lambda_5B4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5B4)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x312, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_613"),
        (2, "loc_625"),
        (1, "loc_635"),
        (SWITCH_DEFAULT, "loc_638"),
    )


    label("loc_613")

    OP_A2(0x69E)
    OP_6F(0x5, 60)
    Sleep(500)
    Jump("loc_638")

    label("loc_625")

    OP_6F(0x5, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_635")

    OP_B4(0x0)
    Return()

    label("loc_638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xA, 1)"), scpexpr(EXPR_END)), "loc_68C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "光弧棍\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x69D)
    Jump("loc_6FC")

    label("loc_68C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "光弧棍\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "光弧棍\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_6FC")

    Jump("loc_734")

    label("loc_6FF")

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
    OP_83(0xF, 0x69)

    label("loc_734")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_54A end

    def Function_6_742(): pass

    label("Function_6_742")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_903")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_830")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -31150, 1500, -395080, 320)
    TurnDirection(0x9, 0x0, 0)

    def lambda_791():
        OP_8F(0xFE, 0xFFFF8652, 0x3E8, 0xFFF9F8B8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_791)

    def lambda_7AC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7AC)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "机械人形出现了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x313, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_80B"),
        (2, "loc_81D"),
        (1, "loc_82D"),
        (SWITCH_DEFAULT, "loc_830"),
    )


    label("loc_80B")

    OP_A2(0x6A0)
    OP_6F(0x9, 60)
    Sleep(500)
    Jump("loc_830")

    label("loc_81D")

    OP_6F(0x9, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_82D")

    OP_B4(0x0)
    Return()

    label("loc_830")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xFD, 1)"), scpexpr(EXPR_END)), "loc_888")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "皇家骑士铠甲\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x69F)
    Jump("loc_900")

    label("loc_888")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "皇家骑士铠甲\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "皇家骑士铠甲\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_900")

    Jump("loc_947")

    label("loc_903")

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
    OP_83(0xF, 0x6A)

    label("loc_947")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_742 end

    def Function_7_955(): pass

    label("Function_7_955")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A50")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_9CF")
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
    OP_A2(0x6A1)
    Jump("loc_A4D")

    label("loc_9CF")

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
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_A4D")

    Jump("loc_A8B")

    label("loc_A50")

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
    OP_83(0xF, 0x6B)

    label("loc_A8B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_955 end

    def Function_8_A99(): pass

    label("Function_8_A99")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B94")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_B13")
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
    OP_A2(0x6A2)
    Jump("loc_B91")

    label("loc_B13")

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
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_B91")

    Jump("loc_BDC")

    label("loc_B94")

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
    OP_83(0xF, 0x6C)

    label("loc_BDC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A99 end

    def Function_9_BEA(): pass

    label("Function_9_BEA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_C64")
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
    OP_A2(0x6A3)
    Jump("loc_CE2")

    label("loc_C64")

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
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_CE2")

    Jump("loc_D1B")

    label("loc_CE5")

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
    OP_83(0xF, 0x6D)

    label("loc_D1B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_BEA end

    def Function_10_D29(): pass

    label("Function_10_D29")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E24")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_DA3")
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
    OP_A2(0x6A4)
    Jump("loc_E21")

    label("loc_DA3")

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
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_E21")

    Jump("loc_E63")

    label("loc_E24")

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
    OP_83(0xF, 0x6E)

    label("loc_E63")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_D29 end

    def Function_11_E71(): pass

    label("Function_11_E71")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_EEC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "圣灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6A5)
    Jump("loc_F6C")

    label("loc_EEC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "圣灵药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "圣灵药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_F6C")

    Jump("loc_FB5")

    label("loc_F6F")

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
    OP_83(0xF, 0x6F)

    label("loc_FB5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_E71 end

    def Function_12_FC3(): pass

    label("Function_12_FC3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_103E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "圣灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6A6)
    Jump("loc_10BE")

    label("loc_103E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "圣灵药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "圣灵药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_10BE")

    Jump("loc_10EB")

    label("loc_10C1")

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
    OP_83(0xF, 0x70)

    label("loc_10EB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_FC3 end

    def Function_13_10F9(): pass

    label("Function_13_10F9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1174")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "圣灵药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x6A7)
    Jump("loc_11F4")

    label("loc_1174")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "圣灵药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "圣灵药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_11F4")

    Jump("loc_1250")

    label("loc_11F7")

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
    OP_83(0xF, 0x71)

    label("loc_1250")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_10F9 end

    SaveToFile()

Try(main)
