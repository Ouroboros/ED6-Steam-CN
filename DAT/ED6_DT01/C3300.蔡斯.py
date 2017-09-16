from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3300   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        Unknown_00              = 100000,
        Unknown_04              = 0,
        Unknown_08              = -100000,
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
        'ED6_DT09/CH10630 ._CH',             # 00
        'ED6_DT09/CH10631 ._CH',             # 01
        'ED6_DT09/CH10640 ._CH',             # 02
        'ED6_DT09/CH10641 ._CH',             # 03
        'ED6_DT09/CH10650 ._CH',             # 04
        'ED6_DT09/CH10651 ._CH',             # 05
        'ED6_DT09/CH10660 ._CH',             # 06
        'ED6_DT09/CH10661 ._CH',             # 07
        'ED6_DT09/CH10670 ._CH',             # 08
        'ED6_DT09/CH10671 ._CH',             # 09
        'ED6_DT09/CH10680 ._CH',             # 0A
        'ED6_DT09/CH10681 ._CH',             # 0B
        'ED6_DT09/CH10690 ._CH',             # 0C
        'ED6_DT09/CH10691 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT09/CH10630P._CP',             # 00
        'ED6_DT09/CH10631P._CP',             # 01
        'ED6_DT09/CH10640P._CP',             # 02
        'ED6_DT09/CH10641P._CP',             # 03
        'ED6_DT09/CH10650P._CP',             # 04
        'ED6_DT09/CH10651P._CP',             # 05
        'ED6_DT09/CH10660P._CP',             # 06
        'ED6_DT09/CH10661P._CP',             # 07
        'ED6_DT09/CH10670P._CP',             # 08
        'ED6_DT09/CH10671P._CP',             # 09
        'ED6_DT09/CH10680P._CP',             # 0A
        'ED6_DT09/CH10681P._CP',             # 0B
        'ED6_DT09/CH10690P._CP',             # 0C
        'ED6_DT09/CH10691P._CP',             # 0D
    )

    DeclMonster(
        X                   = 93670,
        Z                   = -30,
        Y                   = -101140,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 105420,
        Z                   = 140,
        Y                   = -100870,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 75750,
        Z                   = -50,
        Y                   = -78300,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 106940,
        Z                   = 20,
        Y                   = -79600,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 39780,
        TriggerZ            = -60,
        TriggerY            = -82680,
        TriggerRange        = 1000,
        ActorX              = 39410,
        ActorZ              = 1440,
        ActorY              = -82290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AE",          # 00, 0
        "Function_1_1D1",          # 01, 1
        "Function_2_1F0",          # 02, 2
        "Function_3_5F5",          # 03, 3
    )


    def Function_0_1AE(): pass

    label("Function_0_1AE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1BA"),
        (SWITCH_DEFAULT, "loc_1D0"),
    )


    label("loc_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CD")
    OP_A2(0x553)
    Event(0, 2)

    label("loc_1CD")

    Jump("loc_1D0")

    label("loc_1D0")

    Return()

    # Function_0_1AE end

    def Function_1_1D1(): pass

    label("Function_1_1D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3")
    OP_6F(0x0, 0)
    Jump("loc_1EA")

    label("loc_1E3")

    OP_6F(0x0, 60)

    label("loc_1EA")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_1D1 end

    def Function_2_1F0(): pass

    label("Function_2_1F0")

    EventBegin(0x0)
    SetChrPos(0x101, 93760, 40, -147630, 0)
    SetChrPos(0x108, 93830, 20, -149190, 0)
    SetChrPos(0x102, 94540, 40, -148410, 0)
    SetChrPos(0x107, 92640, -20, -148560, 0)
    OP_6D(92040, -100, -111390, 0)
    OP_67(0, 3470, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_282():
        OP_67(0, 8000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_282)

    def lambda_29A():
        OP_6D(93740, 30, -148330, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29A)
    Sleep(1000)

    def lambda_2B7():
        OP_6C(135000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B7)
    OP_6B(3200, 7000)

    ChrTalk(
        0x101,
        (
            "#501F这里就是钟乳洞啊……\x01",
            "感觉是个很神秘的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F不过……\x01",
            "从里面传来很重的魔兽气息。\x02\x03",
            "看来要花一番工夫来找了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#065F哎，唔唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(
        0x101,
        (
            "#002F提妲，要是害怕的话，\x01",
            "现在离开这里也可以哦。\x02\x03",
            "不能太勉强自己哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_424():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_424)

    def lambda_432():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_432)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(
        0x107,
        (
            "#067F没、没关系呢……\x01",
            "虽然有点害怕，但我没勉强自己。\x02\x03",
            "#560F总之，我们快点去找找哪儿有\x01",
            "『塞姆里亚苔藓』吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#006F是啊……快点走吧。\x02\x03",
            "嗯，雾香姐说过，\x01",
            "苔藓是生长在洞窟湖的岸边对吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#012F嗯，应该是的。\x02\x03",
            "顺带一提，\x01",
            "洞窟湖好像是在钟乳洞的西北方向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#070F嗯，把握了方向和位置，\x01",
            "接下来我们就谨慎地前进吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_1F0 end

    def Function_3_5F5(): pass

    label("Function_3_5F5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6ED")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_66E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "ＥＰ改良填充剂\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x5C0)
    Jump("loc_6EA")

    label("loc_66E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "ＥＰ改良填充剂\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "ＥＰ改良填充剂\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_6EA")

    Jump("loc_72D")

    label("loc_6ED")

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
    OP_83(0xF, 0x25)

    label("loc_72D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5F5 end

    SaveToFile()

Try(main)
