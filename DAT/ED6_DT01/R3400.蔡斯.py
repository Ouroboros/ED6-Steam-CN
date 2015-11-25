from ED6ScenarioHelper import *

def main():
    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3400   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
        '艾尔·雷登关所方向',                   # 9
        '蔡斯方向',                             # 10
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
        'ED6_DT09/CH10130 ._CH',             # 00
        'ED6_DT09/CH10131 ._CH',             # 01
        'ED6_DT09/CH10750 ._CH',             # 02
        'ED6_DT09/CH10751 ._CH',             # 03
        'ED6_DT09/CH10760 ._CH',             # 04
        'ED6_DT09/CH10761 ._CH',             # 05
        'ED6_DT09/CH10770 ._CH',             # 06
        'ED6_DT09/CH10771 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10130P._CP',             # 00
        'ED6_DT09/CH10131P._CP',             # 01
        'ED6_DT09/CH10750P._CP',             # 02
        'ED6_DT09/CH10751P._CP',             # 03
        'ED6_DT09/CH10760P._CP',             # 04
        'ED6_DT09/CH10761P._CP',             # 05
        'ED6_DT09/CH10770P._CP',             # 06
        'ED6_DT09/CH10771P._CP',             # 07
    )

    DeclNpc(
        X                   = -26110,
        Z                   = -20,
        Y                   = -38940,
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
        X                   = 189780,
        Z                   = -20,
        Y                   = -27490,
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


    DeclMonster(
        X                   = 45900,
        Z                   = 20,
        Y                   = -46160,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 40140,
        Z                   = -10,
        Y                   = -13510,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 121900,
        Z                   = -40,
        Y                   = -57020,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1CF,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 115250,
        Z                   = 10,
        Y                   = -35350,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D0,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 19790,
        TriggerZ            = 0,
        TriggerY            = -14460,
        TriggerRange        = 1000,
        ActorX              = 19250,
        ActorZ              = 10,
        ActorY              = -15050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55120,
        TriggerZ            = -70,
        TriggerY            = 8740,
        TriggerRange        = 1000,
        ActorX              = 55870,
        ActorZ              = -70,
        ActorY              = 8740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 19690,
        TriggerZ            = -90,
        TriggerY            = 11550,
        TriggerRange        = 1000,
        ActorX              = 19240,
        ActorZ              = -90,
        ActorY              = 11060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 124260,
        TriggerZ            = -30,
        TriggerY            = -53650,
        TriggerRange        = 1000,
        ActorX              = 124760,
        ActorZ              = -30,
        ActorY              = -53160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22A",          # 00, 0
        "Function_1_239",          # 01, 1
        "Function_2_2B0",          # 02, 2
        "Function_3_96D",          # 03, 3
        "Function_4_ABB",          # 04, 4
        "Function_5_C1D",          # 05, 5
        "Function_6_D52",          # 06, 6
    )


    def Function_0_22A(): pass

    label("Function_0_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_238")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_238")

    Return()

    # Function_0_22A end

    def Function_1_239(): pass

    label("Function_1_239")

    OP_16(0x2, 0xFA0, 0xFFFF5038, 0xFFFDB228, 0x30037)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D")
    OP_6F(0xE, 0)
    Jump("loc_264")

    label("loc_25D")

    OP_6F(0xE, 60)

    label("loc_264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276")
    OP_6F(0xF, 0)
    Jump("loc_27D")

    label("loc_276")

    OP_6F(0xF, 60)

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F")
    OP_6F(0x10, 0)
    Jump("loc_296")

    label("loc_28F")

    OP_6F(0x10, 60)

    label("loc_296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8")
    OP_6F(0x11, 0)
    Jump("loc_2AF")

    label("loc_2A8")

    OP_6F(0x11, 60)

    label("loc_2AF")

    Return()

    # Function_1_239 end

    def Function_2_2B0(): pass

    label("Function_2_2B0")

    EventBegin(0x0)
    OP_6D(-11200, 0, -38700, 0)
    OP_6C(45000, 0)
    OP_6B(2600, 0)
    OP_B8(0x4)
    RemoveParty(0x4, 0xFF)
    SetChrPos(0x101, -13400, 0, -38700, 0)
    SetChrPos(0x102, -15200, 0, -39000, 0)
    FadeToBright(2000, 0)

    def lambda_30B():
        OP_6D(5400, -20, -39270, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30B)

    def lambda_323():
        OP_8E(0xFE, 0x1B80, 0xFFFFFFEC, 0xFFFF66B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_323)
    OP_8E(0x102, 0x1216, 0xFFFFFFEC, 0xFFFF66E0, 0xBB8, 0x0)
    OP_8C(0x102, 270, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(
        0x102,
        "#014F……………………………？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 270, 400)
    OP_8E(0x101, 0x1798, 0xFFFFFFEC, 0xFFFF66B8, 0x7D0, 0x0)

    ChrTalk(
        0x101,
        "#004F怎么了，约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#012F没什么……\x01",
            "感觉好像有什么人过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#501F哎？除了我们之外，\x01",
            "还有其他人要通过这里吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(2400, -20, -39270, 1500)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x101)
    OP_63(0x102)

    ChrTalk(
        0x101,
        "#000F……谁也没来啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#015F是啊……\x02",
    )

    CloseMessageWindow()

    def lambda_493():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_493)
    OP_6D(5400, -20, -39270, 1200)

    ChrTalk(
        0x102,
        "#010F看来是我弄错了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#004F啊，我明白了……\x02\x03",
            "#507F约修亚也真是的～\x01",
            "还对科洛丝恋恋不舍啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F啊？\x02\x03",
            "你在说什么呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#502F别害羞、别害羞。\x01",
            "姐姐我可是很明白你的心情哦㈱\x02\x03",
            "#503F不、不过也难怪嘛……\x02\x03",
            "虽说只是演戏性质，\x01",
            "但已经亲密到接吻的地步了………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#014F………哎………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F还有什么想说的情话，\x01",
            "现在回去找她还来得及哦。\x02\x03",
            "我想应该会有满意的回应吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#014F…………………………………\x02\x03",
            "#017F……难道说\x01",
            "那天你完全没发现吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#004F咦……\x02\x03",
            "没发现什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F就是说，最后那个场景啊。\x02\x03",
            "#018F那是假装的啊，假的。\x02\x03",
            "角度刚好错开了，\x01",
            "从旁边看去当然像真的那样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F咦……\x02\x03",
            "……………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x101,
        "#005F#5S你、你说什么～！？\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#017F受不了你了，\x01",
            "到现在也还是那么粗心大意的。\x02\x03",
            "剧本的注释上\x01",
            "不是也写得清清楚楚的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#008F啊、啊哈哈……\x02\x03",
            "是吗，是这样啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 0, 800)
    OP_8C(0x101, 90, 800)

    ChrTalk(
        0x101,
        (
            "#503F（哎呀！我真是的……）\x02\x03",
            "（怎么会感觉\x01",
            "　这样反而松了口气呢～！？）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#014F怎么了……艾丝蒂尔？\x02\x03",
            "你没发烧吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x101, 0x14, 0x0, 0x190, 0xFA0)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 0, 800)
    OP_8C(0x101, 270, 800)

    ChrTalk(
        0x101,
        (
            "#001F啊哈哈！没、没事啦！\x02\x03",
            "好了啦，\x01",
            "马上出发去蔡斯吧！\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_2B0 end

    def Function_3_96D(): pass

    label("Function_3_96D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_9E4")
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
    OP_A2(0x592)
    Jump("loc_A5C")

    label("loc_9E4")

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
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_A5C")

    Jump("loc_AAD")

    label("loc_A5F")

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
    OP_83(0xF, 0x9B)

    label("loc_AAD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_96D end

    def Function_4_ABB(): pass

    label("Function_4_ABB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_B32")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "痊愈之药\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x593)
    Jump("loc_BAA")

    label("loc_B32")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "痊愈之药\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "痊愈之药\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_BAA")

    Jump("loc_C0F")

    label("loc_BAD")

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
    OP_83(0xF, 0x9C)

    label("loc_C0F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_ABB end

    def Function_5_C1D(): pass

    label("Function_5_C1D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_C94")
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
    OP_A2(0x594)
    Jump("loc_D0C")

    label("loc_C94")

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
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_D0C")

    Jump("loc_D44")

    label("loc_D0F")

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
    OP_83(0xF, 0x9D)

    label("loc_D44")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_C1D end

    def Function_6_D52(): pass

    label("Function_6_D52")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E47")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x287, 1)"), scpexpr(EXPR_END)), "loc_DCA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "死之刃２\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x595)
    Jump("loc_E44")

    label("loc_DCA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        (
            "宝箱里装有\x07\x02",
            "死之刃２\x07\x00",
            "。\x01",
            "不过现有的数量太多，\x07\x02",
            "死之刃２\x07\x00",
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_E44")

    Jump("loc_E9C")

    label("loc_E47")

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
    OP_83(0xF, 0x9E)

    label("loc_E9C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_D52 end

    SaveToFile()

Try(main)
