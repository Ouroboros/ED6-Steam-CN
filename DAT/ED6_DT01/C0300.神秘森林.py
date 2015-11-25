from ED6ScenarioHelper import *

def main():
    # 神秘森林

    CreateScenaFile(
        FileName            = 'C0300   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0300.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        '森林之雾',                             # 9
        '森林之雾',                             # 10
        '菠萝怪',                               # 11
        '菠萝怪',                               # 12
        '巨型雪猿',                             # 13
        '巨型雪猿',                             # 14
        '巨型雪猿',                             # 15
        '巨型雪猿',                             # 16
        '巨型雪猿',                             # 17
        '巨型雪猿',                             # 18
    )

    DeclEntryPoint(
        Unknown_00              = 20000,
        Unknown_04              = 0,
        Unknown_08              = 17000,
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
        Unknown_3A              = 19,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10010 ._CH',             # 00
        'ED6_DT09/CH10011 ._CH',             # 01
        'ED6_DT09/CH10280 ._CH',             # 02
        'ED6_DT09/CH10281 ._CH',             # 03
        'ED6_DT09/CH10230 ._CH',             # 04
        'ED6_DT09/CH10231 ._CH',             # 05
        'ED6_DT09/CH10240 ._CH',             # 06
        'ED6_DT09/CH10241 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10010P._CP',             # 00
        'ED6_DT09/CH10011P._CP',             # 01
        'ED6_DT09/CH10280P._CP',             # 02
        'ED6_DT09/CH10281P._CP',             # 03
        'ED6_DT09/CH10230P._CP',             # 04
        'ED6_DT09/CH10231P._CP',             # 05
        'ED6_DT09/CH10240P._CP',             # 06
        'ED6_DT09/CH10241P._CP',             # 07
    )

    DeclMonster(
        X                   = -24000,
        Z                   = 0,
        Y                   = -7000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10000,
        Z                   = 0,
        Y                   = 17000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24000,
        Z                   = 0,
        Y                   = 33000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x44,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12000,
        Z                   = 0,
        Y                   = 51000,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -16000,
        Z                   = 0,
        Y                   = -20000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14000,
        Z                   = 0,
        Y                   = -8000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3000,
        Z                   = 0,
        Y                   = 32000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x40,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15000,
        Z                   = 0,
        Y                   = 8000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x40,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11000,
        Z                   = 0,
        Y                   = 18000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x40,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14000,
        Z                   = 0,
        Y                   = 37000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x40,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 28180,
        TriggerZ            = 0,
        TriggerY            = 33590,
        TriggerRange        = 1500,
        ActorX              = 28180,
        ActorZ              = 1500,
        ActorY              = 33590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 21340,
        TriggerZ            = -170,
        TriggerY            = 17550,
        TriggerRange        = 1000,
        ActorX              = 22310,
        ActorZ              = 1340,
        ActorY              = 17540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_26A",          # 01, 1
        "Function_2_299",          # 02, 2
        "Function_3_535",          # 03, 3
        "Function_4_5FF",          # 04, 4
        "Function_5_753",          # 05, 5
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_256"),
        (SWITCH_DEFAULT, "loc_269"),
    )


    label("loc_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266")
    Event(0, 2)

    label("loc_266")

    Jump("loc_269")

    label("loc_269")

    Return()

    # Function_0_24A end

    def Function_1_26A(): pass

    label("Function_1_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C")
    OP_6F(0x2, 0)
    Jump("loc_283")

    label("loc_27C")

    OP_6F(0x2, 60)

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_END)), "loc_298")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_298")

    Return()

    # Function_1_26A end

    def Function_2_299(): pass

    label("Function_2_299")

    EventBegin(0x0)
    OP_A2(0x265)
    OP_6D(-19820, 80, -24370, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -18840, -230, -46470, 0)
    SetChrPos(0x102, -20460, -330, -47080, 0)
    SetChrPos(0x103, -19740, -300, -45510, 0)
    FadeToBright(1000, 0)
    OP_6D(-19740, -320, -44250, 5000)

    ChrTalk(
        0x101,
        "#002F这里就是神秘森林啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x102,
        "#012F雪拉姐姐，能看出什么来吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#026F#2P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(
        0x103,
        (
            "#022F#2P……没错了。\x02\x03",
            "#022F看得出来不久之前\x01",
            "有好几个人从这里通过。\x02\x03",
            "#022F十有八九是料中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F这、这也能看出来吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F#2P追踪逃走的犯人\x01",
            "也是游击士必要的技能呢。\x02\x03",
            "#020F总之我们进森林里调查一下吧。\x01",
            "注意不要发出太大的声音哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#006F知道～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F明白了。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_299 end

    def Function_3_535(): pass

    label("Function_3_535")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x386, 1)"), scpexpr(EXPR_END)), "loc_5A6")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "熊刺草\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x0, 0x1)
    OP_A2(0x287)
    Jump("loc_5F6")

    label("loc_5A6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "熊刺草\x07\x00",
            "发现了，\x01\x07\x00",
            "不过现有的数量太多，不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5F6")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_535 end

    def Function_4_5FF(): pass

    label("Function_4_5FF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_675")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "回复药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x292)
    Jump("loc_6EB")

    label("loc_675")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "回复药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "回复药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_6EB")

    Jump("loc_745")

    label("loc_6EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么东西都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x1)

    label("loc_745")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5FF end

    def Function_5_753(): pass

    label("Function_5_753")

    EventBegin(0x0)
    Return()

    # Function_5_753 end

    SaveToFile()

Try(main)
