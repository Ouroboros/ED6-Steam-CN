from ED6ScenarioHelper import *

def main():
    # 艾利兹街道

    CreateScenaFile(
        FileName            = 'R0100   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0100.x',
        MapIndex            = 23,
        MapDefaultBGM       = "ed60020",
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
        '洛连特方向',                           # 9
        '布莱特家方向',                         # 10
        '格鲁纳门方向',                         # 11
    )

    DeclEntryPoint(
        Unknown_00              = -35000,
        Unknown_04              = 1000,
        Unknown_08              = 144000,
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
        Unknown_3A              = 23,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10020 ._CH',             # 00
        'ED6_DT09/CH10021 ._CH',             # 01
        'ED6_DT09/CH10180 ._CH',             # 02
        'ED6_DT09/CH10181 ._CH',             # 03
        'ED6_DT09/CH10260 ._CH',             # 04
        'ED6_DT09/CH10261 ._CH',             # 05
        'ED6_DT09/CH10210 ._CH',             # 06
        'ED6_DT09/CH10211 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10020P._CP',             # 00
        'ED6_DT09/CH10021P._CP',             # 01
        'ED6_DT09/CH10180P._CP',             # 02
        'ED6_DT09/CH10181P._CP',             # 03
        'ED6_DT09/CH10260P._CP',             # 04
        'ED6_DT09/CH10261P._CP',             # 05
        'ED6_DT09/CH10210P._CP',             # 06
        'ED6_DT09/CH10211P._CP',             # 07
    )

    DeclNpc(
        X                   = -14030,
        Z                   = 1000,
        Y                   = 217340,
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

    DeclNpc(
        X                   = -60890,
        Z                   = 1030,
        Y                   = 216800,
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

    DeclNpc(
        X                   = -39320,
        Z                   = 1000,
        Y                   = 90280,
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
        TriggerX            = -36800,
        TriggerZ            = 1000,
        TriggerY            = 152300,
        TriggerRange        = 1500,
        ActorX              = -36800,
        ActorZ              = 2500,
        ActorY              = 152800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39100,
        TriggerZ            = 1000,
        TriggerY            = 153300,
        TriggerRange        = 1500,
        ActorX              = -39100,
        ActorZ              = 2200,
        ActorY              = 153300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_192",          # 00, 0
        "Function_1_20B",          # 01, 1
        "Function_2_24C",          # 02, 2
        "Function_3_2B6",          # 03, 3
        "Function_4_2FB",          # 04, 4
        "Function_5_A73",          # 05, 5
        "Function_6_AA2",          # 06, 6
        "Function_7_AD1",          # 07, 7
    )


    def Function_0_192(): pass

    label("Function_0_192")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_19E"),
        (SWITCH_DEFAULT, "loc_20A"),
    )


    label("loc_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA")
    Return()

    label("loc_1AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(-14000, 1000, 197160, 0)
    SetChrPos(0x102, -13816, 1000, 198240, 180)
    SetChrPos(0x101, -14816, 1000, 199400, 180)
    OP_6C(40000, 0)
    SetMapFlags(0x400000)
    FadeToBright(500, 0)
    Event(0, 4)

    label("loc_207")

    Jump("loc_20A")

    label("loc_20A")

    Return()

    # Function_0_192 end

    def Function_1_20B(): pass

    label("Function_1_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_223")
    OP_B1("R0100_y")
    Jump("loc_22C")

    label("loc_223")

    OP_B1("R0100_n")

    label("loc_22C")

    OP_16(0x2, 0xFA0, 0xFFFD7F60, 0x6D60, 0x30008)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B")
    OP_1B(0x2, 0x0, 0x7)

    label("loc_24B")

    Return()

    # Function_1_20B end

    def Function_2_24C(): pass

    label("Function_2_24C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "北　洛连特市　　　４９塞尔矩\x01",
            "南　格鲁纳门　　２５９塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_2_24C end

    def Function_3_2B6(): pass

    label("Function_3_2B6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西　布莱特家\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_2B6 end

    def Function_4_2FB(): pass

    label("Function_4_2FB")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_43(0x101, 0x0, 0x0, 0x5)
    OP_43(0x102, 0x0, 0x0, 0x6)
    OP_A2(0x0)
    OP_A2(0x1)

    def lambda_31C():
        OP_6D(-13905, 1000, 185268, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31C)
    OP_A5(0x0)

    ChrTalk(
        0x101,
        "#003F对了，约修亚……\x02",
    )

    CloseMessageWindow()
    OP_A5(0x1)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#010F嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F……………………\x02\x03",
            "#003F我……\x01",
            "真的适合做游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F……………………\x02\x03",
            "#015F嗯，我觉得你从父亲那儿继承来的\x01",
            "武术能力有扎实的功底……\x02\x03",
            "#015F遇到有困难的人不会放着不管，\x01",
            "这种爱管闲事的性格也是你的优点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#008F嘿嘿，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F难道……\x01",
            "你还在想刚才塔里那件事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F嗯……\x02\x03",
            "#003F那时候，因为我的大意，\x01",
            "差点把鲁克也牵连进去。\x02\x03",
            "#003F如果老爸没来，\x01",
            "说不定还会让他受重伤。\x02\x03",
            "#003F这样子下去真的能行吗……\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F…………………………\x02\x03",
            "#019F什么呀，说这种话可不是你的风格哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F今天的失败，\x01",
            "就用明天来把它挽回。\x02\x03",
            "#010F顾虑太远的事情而畏缩，\x01",
            "这可一点也不像你哦。\x02\x03",
            "#010F这不是你一直憧憬的工作吗？\x01",
            "遇到这点挫折就沮丧怎么能行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#003F约修亚……\x02\x03",
            "#500F……………………\x02\x03",
            "#500F……嗯，有道理……\x02\x03",
            "#006F这样子，根本不像我嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#011F对对，\x01",
            "凝重的表情不适合艾丝蒂尔。\x02\x03",
            "#011F这种乐天派的笑容才自然嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#009F喂，这话是什么意思啊！\x02\x03",
            "#009F真是的，多此一句……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#019F哈哈，听出来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#000F算了……\x01",
            "谢谢，现在我心情好多了。\x02\x03",
            "#001F那么，赶快回家吧。\x02\x03",
            "#001F不知为什么突然就觉得肚子饿了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F（果然是乐天派……）\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_A2(0x218)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    SetMapFlags(0x1)
    Return()

    # Function_4_2FB end

    def Function_5_A73(): pass

    label("Function_5_A73")

    OP_A6(0x0)
    OP_8E(0xFE, 0xFFFFC729, 0x0, 0x2D7BD, 0xBB8, 0x0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x0)
    Return()

    # Function_5_A73 end

    def Function_6_AA2(): pass

    label("Function_6_AA2")

    OP_A6(0x1)
    OP_8E(0xFE, 0xFFFFCB34, 0x0, 0x2D073, 0xBB8, 0x0)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_92(0xFE, 0x0, 0x0, 0xBB8, 0x0)
    OP_A3(0x1)
    Return()

    # Function_6_AA2 end

    def Function_7_AD1(): pass

    label("Function_7_AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBD")
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_B5F")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#010F已经傍晚了啊。\x02\x03",
            "#010F父亲还在等我们呢，\x01",
            "我们还是早点回家吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        "#000F嗯，明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_B5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#014F艾丝蒂尔，去城里不是这个方向啊。\x02\x03",
            "你该不会还没有睡醒吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#009F真、真啰嗦啊你～\x01",
            "刚才只不过看错路牌而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA2")

    label("loc_C2C")


    ChrTalk(
        0x102,
        (
            "#012F（这方向是往王都地区的……\x01",
            "　要去城里的话往反方向走就行了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    OP_90(0x0, 0x0, 0x0, 0x9C4, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_CBD")

    Return()

    # Function_7_AD1 end

    SaveToFile()

Try(main)
