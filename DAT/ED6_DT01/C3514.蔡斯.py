from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3514   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3514.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10710 ._CH',             # 00
        'ED6_DT09/CH10711 ._CH',             # 01
        'ED6_DT09/CH10720 ._CH',             # 02
        'ED6_DT09/CH10721 ._CH',             # 03
        'ED6_DT09/CH10730 ._CH',             # 04
        'ED6_DT09/CH10731 ._CH',             # 05
        'ED6_DT09/CH10740 ._CH',             # 06
        'ED6_DT09/CH10741 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10710P._CP',             # 00
        'ED6_DT09/CH10711P._CP',             # 01
        'ED6_DT09/CH10720P._CP',             # 02
        'ED6_DT09/CH10721P._CP',             # 03
        'ED6_DT09/CH10730P._CP',             # 04
        'ED6_DT09/CH10731P._CP',             # 05
        'ED6_DT09/CH10740P._CP',             # 06
        'ED6_DT09/CH10741P._CP',             # 07
    )

    DeclMonster(
        X                   = 2040,
        Z                   = 0,
        Y                   = 3920,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3970,
        Z                   = 0,
        Y                   = -1960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1920,
        Z                   = 0,
        Y                   = -4010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4080,
        Z                   = 0,
        Y                   = 1890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FC,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -120,
        Z                   = 0,
        Y                   = -17970,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1FA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -4690,
        TriggerZ            = 0,
        TriggerY            = -22750,
        TriggerRange        = 1000,
        ActorX              = -4690,
        ActorZ              = 0,
        ActorY              = -23410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4740,
        TriggerZ            = 0,
        TriggerY            = -22710,
        TriggerRange        = 1000,
        ActorX              = 4800,
        ActorZ              = 0,
        ActorY              = -23330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_1BF",          # 01, 1
        "Function_2_1F2",          # 02, 2
        "Function_3_355",          # 03, 3
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Return()

    # Function_0_1BE end

    def Function_1_1BF(): pass

    label("Function_1_1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1")
    OP_6F(0x0, 0)
    Jump("loc_1D8")

    label("loc_1D1")

    OP_6F(0x0, 60)

    label("loc_1D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA")
    OP_6F(0x1, 0)
    Jump("loc_1F1")

    label("loc_1EA")

    OP_6F(0x1, 60)

    label("loc_1F1")

    Return()

    # Function_1_1BF end

    def Function_2_1F2(): pass

    label("Function_2_1F2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_269")
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
    OP_A2(0x5AF)
    Jump("loc_2E1")

    label("loc_269")

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
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2E1")

    Jump("loc_347")

    label("loc_2E4")

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
    OP_83(0xF, 0x33)

    label("loc_347")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1F2 end

    def Function_3_355(): pass

    label("Function_3_355")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_450")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1AF, 1)"), scpexpr(EXPR_END)), "loc_3CF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "地狱煎蛋\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5B0)
    Jump("loc_44D")

    label("loc_3CF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "地狱煎蛋\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "地狱煎蛋\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_44D")

    Jump("loc_496")

    label("loc_450")

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
    OP_83(0xF, 0x34)

    label("loc_496")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_355 end

    SaveToFile()

Try(main)
