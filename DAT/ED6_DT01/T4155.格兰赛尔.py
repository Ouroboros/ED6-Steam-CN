from ED6ScenarioHelper import *

def main():
    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4155   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4155.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        '拉尔夫',                               # 9
        '王都格兰赛尔·东街区',                 # 10
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01450 ._CH',             # 03
        'ED6_DT07/CH01550 ._CH',             # 04
        'ED6_DT07/CH01450 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01450P._CP',             # 03
        'ED6_DT07/CH01550P._CP',             # 04
        'ED6_DT07/CH01450P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
    )

    DeclNpc(
        X                   = 87150,
        Z                   = -10400,
        Y                   = 161910,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 51050,
        Z                   = 0,
        Y                   = 83440,
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
        TriggerX            = 53710,
        TriggerZ            = 250,
        TriggerY            = 137720,
        TriggerRange        = 800,
        ActorX              = 53710,
        ActorZ              = 2450,
        ActorY              = 137720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71160,
        TriggerZ            = -10000,
        TriggerY            = 151550,
        TriggerRange        = 800,
        ActorX              = 71160,
        ActorZ              = -8500,
        ActorY              = 151550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_16B",          # 01, 1
        "Function_2_19B",          # 02, 2
        "Function_3_1B1",          # 03, 3
        "Function_4_427",          # 04, 4
        "Function_5_4FC",          # 05, 5
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Return()

    # Function_0_16A end

    def Function_1_16B(): pass

    label("Function_1_16B")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x3005F)
    OP_71(0xE, 0x4)
    OP_6F(0x4, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19A")
    OP_72(0x6, 0x10)

    label("loc_19A")

    Return()

    # Function_1_16B end

    def Function_2_19B(): pass

    label("Function_2_19B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_19B")

    label("loc_1B0")

    Return()

    # Function_2_19B end

    def Function_3_1B1(): pass

    label("Function_3_1B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDD, 2)), scpexpr(EXPR_END)), "loc_218")

    ChrTalk(
        0xFE,
        (
            "可怜可怜我，\x01",
            "请你们不要将我在这儿的事情告诉士兵好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托了…… \x02",
    )

    CloseMessageWindow()
    Jump("loc_423")

    label("loc_218")

    OP_A2(0x6EA)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "哇啊、被、被发现了。 \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……明天就是决赛了，\x01",
            "为了妻子我无论如何也要占到好的席位。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "本来打算通宵\x01",
            "在竞技场前面排队等候的，\x01",
            "可是却被士兵赶回去了。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "因此，\x01",
            "我打算再一次隐蔽地前往竞技场…… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "拜托你们帮我保密！！ \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我给你们这个，\x01",
            "请你们不要将我在这儿的事情告诉士兵好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x21B, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "得到了\x07\x02",
            "红耀石　第10卷\x07\x00",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0xFE,
        (
            "这样就可以了吧。\x01",
            "明天我一定要抢到最前面的座位。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_423")

    TalkEnd(0xFE)
    Return()

    # Function_3_1B1 end

    def Function_4_427(): pass

    label("Function_4_427")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "定期船起降坪\x01",
            "≡　开往洛连特市\x01",
            "≡　开往蔡斯市\x01",
            "≡　开往卡尔瓦德共和国\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※请勿携带易燃物和危险品\x01",
            "　　　　　利贝尔飞艇公社\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_427 end

    def Function_5_4FC(): pass

    label("Function_5_4FC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　飞艇坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "『利贝尔飞艇公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_4FC end

    SaveToFile()

Try(main)
