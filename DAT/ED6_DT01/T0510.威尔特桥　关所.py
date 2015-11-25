from ED6ScenarioHelper import *

def main():
    # 威尔特桥　关所

    CreateScenaFile(
        FileName            = 'T0510   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0510.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0510   ._SN',
            'ED6_DT01/T0510_1 ._SN',
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
        '阿斯顿队长',                           # 9
        '戴恩副长',                             # 10
        '目标用摄像机',                         # 11
    )

    DeclEntryPoint(
        Unknown_00              = 24000,
        Unknown_04              = 0,
        Unknown_08              = 52000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 24100,
        Unknown_04              = 0,
        Unknown_08              = 56200,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 24100,
        Unknown_04              = 0,
        Unknown_08              = 56200,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
    )

    DeclNpc(
        X                   = 29850,
        Z                   = 0,
        Y                   = -73420,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 26800,
        Z                   = 0,
        Y                   = 29900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 28310,
        TriggerZ            = 0,
        TriggerY            = -73420,
        TriggerRange        = 500,
        ActorX              = 29850,
        ActorZ              = 1500,
        ActorY              = -73420,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28250,
        TriggerZ            = 0,
        TriggerY            = 29800,
        TriggerRange        = 500,
        ActorX              = 26800,
        ActorZ              = 1500,
        ActorY              = 29900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20640,
        TriggerZ            = 0,
        TriggerY            = 33000,
        TriggerRange        = 1000,
        ActorX              = 20640,
        ActorZ              = 1000,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20E",          # 00, 0
        "Function_1_233",          # 01, 1
        "Function_2_27D",          # 02, 2
        "Function_3_293",          # 03, 3
        "Function_4_298",          # 04, 4
        "Function_5_1BB9",         # 05, 5
        "Function_6_1BBE",         # 06, 6
        "Function_7_2533",         # 07, 7
    )


    def Function_0_20E(): pass

    label("Function_0_20E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_21A"),
        (SWITCH_DEFAULT, "loc_232"),
    )


    label("loc_21A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_22F")
    OP_28(0x8, 0x2, 0x4000)
    Event(1, 1)

    label("loc_22F")

    Jump("loc_232")

    label("loc_232")

    Return()

    # Function_0_20E end

    def Function_1_233(): pass

    label("Function_1_233")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_233 end

    def Function_2_27D(): pass

    label("Function_2_27D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_292")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_27D")

    label("loc_292")

    Return()

    # Function_2_27D end

    def Function_3_293(): pass

    label("Function_3_293")

    Call(0, 4)
    Return()

    # Function_3_293 end

    def Function_4_298(): pass

    label("Function_4_298")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_359")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xA, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xA, 0x3E8)

    ChrTalk(
        0x8,
        (
            "艾丝蒂尔……\x01",
            "啊，约修亚也来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F阿斯顿队长，你好。\x02",
    )

    CloseMessageWindow()

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_511")
    OP_A2(0x281)
    OP_A2(0x1)

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊啊，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我都听说了，\x01",
            "我家的鲁克给你们添了很多麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "作为父亲，真是感到惭愧啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F没事，像他这种年纪的男孩子\x01",
            "喜欢恶作剧也是没有办法的事。\x02\x03",
            "就算是我，\x01",
            "小的时候也经常到城镇外面乱跑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F你不是女孩子吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哈哈，还是这么精神啊。\x02",
    )

    CloseMessageWindow()

    label("loc_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F7")

    ChrTalk(
        0x8,
        (
            "那边的那位……\x01",
            "不就是雪拉扎德小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#020F你好啊，队长先生。\x02\x03",
            "这次是来向你申请\x01",
            "往柏斯地区的通行许可证的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不会是……\x01",
            "和之前发生的那个事件有关吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#003F嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "众人说明了关于卡西乌斯乘坐了\x01",
            "行踪不明的定期船的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x8,
        "怎么会，卡西乌斯先生他……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这可是件大事。\x01",
            "这就给你们办理通行许可证吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)
    Sleep(500)
    TurnDirection(0x8, 0x0, 400)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x32F, 1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "通行许可证\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x101,
        (
            "#001F谢谢，阿斯顿队长。\x02\x03",
            "#000F可是，这就行了？\x01",
            "这么简单就办理了通行许可证……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "没什么，都是熟人嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而且，作为王国军，\x01",
            "也应该鼎力协助游击士协会才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊，不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#004F哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "……要是到北边的哈肯门去的话，\x01",
            "有件事需要你们注意一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "到那里的时候\x01",
            "最好还是隐瞒自己游击士的身份。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F为什么这么说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不好意思，\x01",
            "我不能再往下说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "总之，要是你们打算调查这件事的话，\x01",
            "行动的时候还是谨慎点比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我也会向空之女神\x01",
            "祈祷卡西乌斯先生平安归来。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    OP_A2(0x303)
    Jump("loc_A7C")

    label("loc_9F7")


    ChrTalk(
        0x8,
        (
            "要是你们打算调查这件事的话，\x01",
            "行动的时候还是谨慎点比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我也会向空之女神\x01",
            "祈祷卡西乌斯先生平安归来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7C")

    Jump("loc_1BB5")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_127A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E47")
    OP_A2(0x281)
    OP_A2(0x1)

    ChrTalk(
        0x8,
        (
            "哦哦，\x01",
            "这不是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F阿斯顿队长，你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊啊，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我都听说了，\x01",
            "我家的鲁克给你们添了不少麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "作为父亲，真是感到惭愧啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F没事，像他这种年纪的男孩子\x01",
            "喜欢恶作剧也是没有办法的事。\x02\x03",
            "#001F就算是我，\x01",
            "小的时候也经常到城镇外面乱跑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F你不是女孩子吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哈哈，还是这么精神啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "说起来，\x01",
            "听说柏斯地区相继\x01",
            "发生了多宗的盗窃案件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F柏斯？\x01",
            "真是多事之秋啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "嗯，这下我们守备队\x01",
            "也必须提高警惕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是总觉得\x01",
            "我的部下紧张感不足啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "真伤脑筋啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10FA")

    label("loc_E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1031")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F65")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "最近柏斯地区\x01",
            "接连发生了强盗事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们守备队\x01",
            "也必须提高警惕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是总觉得\x01",
            "我的部下紧张感不足啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102E")

    label("loc_F65")


    ChrTalk(
        0x8,
        (
            "柏斯发生了空贼事件，\x01",
            "我们守备队必须提高警惕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是总觉得\x01",
            "我的部下紧张感不足啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102E")

    Jump("loc_10FA")

    label("loc_1031")


    ChrTalk(
        0x8,
        (
            "柏斯发生了空贼事件，\x01",
            "我们守备队必须提高警惕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是总觉得\x01",
            "我的部下紧张感不足啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FA")

    Jump("loc_1277")

    label("loc_10FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E0")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "最近柏斯地区好像\x01",
            "接连发生了强盗事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我们在这里也\x01",
            "丝毫不能掉以轻心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "希望部下们能够\x01",
            "活用在训练中取得的经验。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1277")

    label("loc_11E0")


    ChrTalk(
        0x8,
        (
            "柏斯地区好像\x01",
            "接连发生了强盗事件啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "希望部下们能够\x01",
            "活用在训练中取得的经验。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1277")

    Jump("loc_1BB5")

    label("loc_127A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1535")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_129B")
    Call(1, 0)
    Jump("loc_1532")

    label("loc_129B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1346")

    ChrTalk(
        0x8,
        (
            "能站在对方的角度去思考，\x01",
            "就可以非常的客观公正了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "希望你们能够在今后的舞台中大展身手。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1532")

    label("loc_1346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A3")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "训练辛苦了。\x01",
            "对士兵们应该是一剂强心剂啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不好意思，你们在城里的时候，\x01",
            "帮我看着点鲁克那小子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "那家伙从一生出来\x01",
            "就不是一个听话的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我母亲拿他\x01",
            "也没什么办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "或许我应该\x01",
            "更加严厉地管教他才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1532")

    label("loc_14A3")


    ChrTalk(
        0x8,
        (
            "鲁克那小子\x01",
            "真不是一个听话的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我母亲拿他\x01",
            "也没什么办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不好意思，\x01",
            "今后请你们也多照顾一下鲁克。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1532")

    Jump("loc_1BB5")

    label("loc_1535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_17AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1556")
    Call(1, 0)
    Jump("loc_17A9")

    label("loc_1556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1601")

    ChrTalk(
        0x8,
        (
            "能站在对方的角度去思考，\x01",
            "就可以非常的客观公正了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "希望你们能够在今后的舞台中大展身手。\x02",
    )

    CloseMessageWindow()
    Jump("loc_17A9")

    label("loc_1601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F6")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "从新进士兵的态度来看，\x01",
            "他们似乎感到非常不安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "这次的训练好像让他们\x01",
            "找回点紧张感了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呼，今后也有必要\x01",
            "对他们进行严厉地锻炼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A9")

    label("loc_16F6")


    ChrTalk(
        0x8,
        (
            "这次的训练好像让士兵们\x01",
            "找回点紧张感了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "呼，今后也有必要\x01",
            "对他们进行严厉地锻炼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A9")

    Jump("loc_1BB5")

    label("loc_17AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A63")
    OP_A2(0x281)
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "哦哦，\x01",
            "这不是艾丝蒂尔和约修亚吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#000F阿斯顿队长，你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#010F很久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "啊啊，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我都听说了，\x01",
            "我家的鲁克给你们添了不少麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "作为父亲，真是感到惭愧啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#001F没事，像他这种年纪的男孩子\x01",
            "喜欢恶作剧也是没有办法的事。\x02\x03",
            "#001F就算是我，\x01",
            "小的时候也经常到城镇外面乱跑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#017F你不是女孩子吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "哈哈，还是这么精神啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "说实话，\x01",
            "我也想早点回洛连特去\x01",
            "和家人团聚啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "不过来这里接任的时间还很短。\x01",
            "要做的事情还有很多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB5")

    label("loc_1A63")


    ChrTalk(
        0x8,
        (
            "在１０年前的战争中，\x01",
            "关所在封锁帝国军各部队的战斗上\x01",
            "起了非常重要的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然现在通行的人很少，\x01",
            "但是守备也绝不能马虎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是，\x01",
            "这里的新进士兵态度实在是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "既然我来到这里了，\x01",
            "就有必要进行一次严格的训练。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB5")

    TalkEnd(0x8)
    Return()

    # Function_4_298 end

    def Function_5_1BB9(): pass

    label("Function_5_1BB9")

    Call(0, 6)
    Return()

    # Function_5_1BB9 end

    def Function_6_1BBE(): pass

    label("Function_6_1BBE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CBB")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "听说失踪的定期船\x01",
            "已经被发现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "好像是情报部和国境守备队\x01",
            "联合起来解决的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "真～是的，\x01",
            "这下终于能够恢复普通执勤了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFF")

    label("loc_1CBB")


    ChrTalk(
        0x9,
        (
            "真～是的，\x01",
            "这下终于能够恢复普通执勤了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFF")

    Jump("loc_252F")

    label("loc_1D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E11")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "虽然消息还没有确认，\x01",
            "但听说不仅是国境守备队，\x01",
            "连新设的情报部也出动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "不过，这样拖延下去，\x01",
            "也关系到军队的威严啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "希望他们能好好加油。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E99")

    label("loc_1E11")


    ChrTalk(
        0x9,
        (
            "虽然消息还没有确认，\x01",
            "但是听说不仅是国境守备队，\x01",
            "连新设的情报部也出动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E99")

    Jump("loc_252F")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_200D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7D")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "行踪不明的定期船\x01",
            "终于被发现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但是，\x01",
            "还是没有收到解除盘查的命令……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "这是怎么一回事呢。\x01",
            "我想要情报啊，情报。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200A")

    label("loc_1F7D")


    ChrTalk(
        0x9,
        (
            "行踪不明的定期船\x01",
            "终于被发现了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "但是，\x01",
            "还是没有收到解除盘查的命令……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200A")

    Jump("loc_252F")

    label("loc_200D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2179")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "说起来，\x01",
            "定期船竟然整个消失不见……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "真是无奇不有啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "那么庞大的家伙，\x01",
            "应该能够马上就发现的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "就算是摩尔根将军，\x01",
            "这次也遇到难题了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊呀，\x01",
            "说这种话要被队长骂的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2222")

    label("loc_2179")


    ChrTalk(
        0x9,
        (
            "就算是摩尔根将军，\x01",
            "这次也遇到难题了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "啊呀，\x01",
            "说这种话要被队长骂的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2222")

    Jump("loc_252F")

    label("loc_2225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_22FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B6")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "好像只是解除了\x01",
            "钢壁之路的封锁呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "而且不是因为找到了定期船，\x01",
            "那到底发生了什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F8")

    label("loc_22B6")


    ChrTalk(
        0x9,
        (
            "还有，\x01",
            "定期船到底什么时候能恢复航行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F8")

    Jump("loc_252F")

    label("loc_22FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_249D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F5")
    OP_A2(0x2)

    ChrTalk(
        0x9,
        (
            "说起来，\x01",
            "不仅禁止了全地区的飞行，\x01",
            "而且连钢壁之路都封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "看来这次可要来大手笔的了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "可以看出国境守备队的那些人\x01",
            "也非常焦急呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_249A")

    label("loc_23F5")


    ChrTalk(
        0x9,
        (
            "说起来，\x01",
            "不仅禁止了全地区的飞行，\x01",
            "而且连钢壁之路都封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "看来这次可要来大手笔的了。\x02",
    )

    CloseMessageWindow()

    label("loc_249A")

    Jump("loc_252F")

    label("loc_249D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_252F")

    ChrTalk(
        0x9,
        (
            "哦，这次是游击士吗？\x01",
            "步行过来还真是了不起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "你们路上要小心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_252F")

    TalkEnd(0x9)
    Return()

    # Function_6_1BBE end

    def Function_7_2533(): pass

    label("Function_7_2533")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在此休息\x01",      # 0
            "离开\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_274E")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 20640, 1000, 33000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x32)
    OP_73(0x1)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 21970, 0, 33230, 269)
    SetChrPos(0x1, 21970, 0, 33230, 269)
    SetChrPos(0x2, 21970, 0, 33230, 269)
    SetChrPos(0x3, 21970, 0, 33230, 269)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_274E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2768")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2768")

    Return()

    # Function_7_2533 end

    SaveToFile()

Try(main)
