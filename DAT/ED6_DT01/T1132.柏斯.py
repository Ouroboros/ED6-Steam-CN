from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'T1132   ._SN',
        MapName             = 'Bose',
        Location            = 'T1132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1132   ._SN',
            'ED6_DT01/T1132_1 ._SN',
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
        '巴雷里奥',                             # 9
        '蒂娜',                                 # 10
        '哈尔德',                               # 11
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
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01120 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01120P._CP',             # 02
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = 190600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -130180,
        Z                   = 0,
        Y                   = 130460,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -86950,
        Z                   = 0,
        Y                   = 119700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )


    DeclActor(
        TriggerX            = 6598,
        TriggerZ            = 0,
        TriggerY            = 190158,
        TriggerRange        = 700,
        ActorX              = 4500,
        ActorZ              = 1500,
        ActorY              = 190662,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3130,
        TriggerZ            = 0,
        TriggerY            = 192000,
        TriggerRange        = 800,
        ActorX              = 3130,
        ActorZ              = 1000,
        ActorY              = 192000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_20A",          # 01, 1
        "Function_2_20B",          # 02, 2
        "Function_3_221",          # 03, 3
        "Function_4_32D",          # 04, 4
        "Function_5_3AA",          # 05, 5
        "Function_6_B68",          # 06, 6
        "Function_7_1233",         # 07, 7
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_185")
    SetChrPos(0x9, -49700, 0, 119900, 0)
    Jump("loc_209")

    label("loc_185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1A0")
    SetChrPos(0x9, -128400, 0, 139800, 0)
    Jump("loc_209")

    label("loc_1A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1CC")
    SetChrPos(0x9, -84700, 0, 152800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9")
    ClearChrFlags(0xA, 0x80)

    label("loc_1C9")

    Jump("loc_209")

    label("loc_1CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1E7")
    SetChrPos(0x9, -84300, 0, 119900, 0)
    Jump("loc_209")

    label("loc_1E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_202")
    SetChrPos(0x9, -124300, 0, 179000, 0)
    Jump("loc_209")

    label("loc_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_209")

    label("loc_209")

    Return()

    # Function_0_16A end

    def Function_1_20A(): pass

    label("Function_1_20A")

    Return()

    # Function_1_20A end

    def Function_2_20B(): pass

    label("Function_2_20B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_220")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_20B")

    label("loc_220")

    Return()

    # Function_2_20B end

    def Function_3_221(): pass

    label("Function_3_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_24E")

    label("loc_228")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_8D(0xFE, -51500, 121100, -47400, 118400, 2000)
    Jump("loc_228")

    label("loc_24B")

    Jump("loc_32C")

    label("loc_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_27B")

    label("loc_255")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_278")
    OP_8D(0xFE, -130100, 142200, -127100, 126500, 2000)
    Jump("loc_255")

    label("loc_278")

    Jump("loc_32C")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2A8")

    label("loc_282")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A5")
    OP_8D(0xFE, -86300, 154100, -82400, 151500, 2000)
    Jump("loc_282")

    label("loc_2A5")

    Jump("loc_32C")

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2D5")

    label("loc_2AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D2")
    OP_8D(0xFE, -86000, 121200, -81700, 118700, 2000)
    Jump("loc_2AF")

    label("loc_2D2")

    Jump("loc_32C")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_302")

    label("loc_2DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FF")
    OP_8D(0xFE, -126000, 180700, -122800, 177900, 2000)
    Jump("loc_2DC")

    label("loc_2FF")

    Jump("loc_32C")

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_32C")

    label("loc_309")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32C")
    OP_8D(0xFE, -130120, 126680, -127550, 142940, 2000)
    Jump("loc_309")

    label("loc_32C")

    Return()

    # Function_3_221 end

    def Function_4_32D(): pass

    label("Function_4_32D")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D")
    OP_0D()
    OP_A9(0xD)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_38D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39E")
    TalkEnd(0x8)
    Return()

    label("loc_39E")

    Call(0, 5)
    OP_8C(0x8, 90, 0)
    Return()

    # Function_4_32D end

    def Function_5_3AA(): pass

    label("Function_5_3AA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "在时代的洪流中\x01",
            "顽固地保持着传统……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我明白这是\x01",
            "非常困难的一件事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "看来，\x01",
            "我也不能被陈旧的习惯所束缚，\x01",
            "要与时俱进地改善服务质量才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502")

    label("loc_4A1")


    ChrTalk(
        0x8,
        (
            "在时代的洪流中\x01",
            "顽固地保持着传统……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "我明白这是\x01",
            "非常困难的一件事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_502")

    Jump("loc_B64")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5AE")

    ChrTalk(
        0x8,
        (
            "虽然我明白\x01",
            "那些年轻员工所说的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "但是我自己\x01",
            "已经是个落伍的人了，\x01",
            "绝对不能接受他们所说的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "哈哈……\x01",
            "这个时代变得有些不可理喻了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B64")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_749")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AB")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "以前的员工都是团结一心\x01",
            "为了满足顾客而共同努力的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "最近年轻人的思考方式\x01",
            "也改变了许多啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "有很多事情\x01",
            "都无法顺利开展了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_6AB")


    ChrTalk(
        0x8,
        (
            "以前的员工都是团结一心\x01",
            "为了满足顾客而共同努力的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "最近年轻人的思考方式\x01",
            "也改变了许多啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_746")

    Jump("loc_B64")

    label("loc_749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_858")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "本酒店自创立以来，\x01",
            "一直在国内保有非常高的人气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然经常会忙不过来，\x01",
            "不过，这家酒店就是我的生存价值……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "将这种勤劳肯干的传统\x01",
            "传给下一任主管是我的职责。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8ED")

    label("loc_858")


    ChrTalk(
        0x8,
        (
            "本酒店自创立以来，\x01",
            "一直在国内保有非常高的人气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "虽然经常会忙不过来，\x01",
            "不过，这家酒店就是我的生存价值。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ED")

    Jump("loc_B64")

    label("loc_8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BC")
    OP_A2(0x0)

    ChrTalk(
        0x8,
        (
            "迎接客人的时候\x01",
            "必须要遵守严格的纪律……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而且要把时时刻刻\x01",
            "保持微笑作为行为准则。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "要向着提供更优质的服务\x01",
            "这一目标努力再努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A37")

    label("loc_9BC")


    ChrTalk(
        0x8,
        (
            "迎接客人的时候\x01",
            "必须要遵守严格的纪律……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "而且要把时时刻刻\x01",
            "保持微笑作为行为准则。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A37")

    Jump("loc_B64")

    label("loc_A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_B08")

    ChrTalk(
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "本酒店自创业以来已经１２０年了。\x01",
            "在柏斯也算是拥有悠久历史的酒店了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请您务必要好好享受一下\x01",
            "拥有悠久传统的本酒店所独有的高级服务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B64")

    label("loc_B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_B64")

    ChrTalk(
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "请您务必要好好享受一下\x01",
            "拥有悠久传统的本酒店所独有的高级服务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B64")

    TalkEnd(0x8)
    Return()

    # Function_5_3AA end

    def Function_6_B68(): pass

    label("Function_6_B68")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BA5")

    ChrTalk(
        0xFE,
        (
            "哎呀，真是的！\x01",
            "今天也忙得要命！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D14")
    OP_A2(0x1)

    ChrTalk(
        0xFE,
        (
            "我是为了自己\x01",
            "才来干这份工作的，\x01",
            "而不是为了这个酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "虽然主管说过\x01",
            "做什么都要以酒店利益为前提，\x01",
            "然后再行动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以酒店利益为前提，\x01",
            "是主管的工作吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我可不是\x01",
            "来这里当佣人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "我说错了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_DDA")

    label("loc_D14")


    ChrTalk(
        0xFE,
        (
            "虽然主管说过\x01",
            "做什么都要以酒店利益为前提，\x01",
            "然后再行动……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "以酒店利益为前提，\x01",
            "是主管的工作吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDA")

    Jump("loc_122F")

    label("loc_DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_E8E")

    ChrTalk(
        0xFE,
        (
            "今天不管主管说什么，\x01",
            "我都要依我自己的安排去逛街购物！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "要将上次的郁闷一扫而光！\x02",
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_F7B")

    ChrTalk(
        0xFE,
        "你听我说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "明明是休息时间，\x01",
            "主管却突然叫我来工作！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "好不容易订到了安特洛丝餐厅的位子，\x01",
            "现在却去不成了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1066")

    ChrTalk(
        0xFE,
        (
            "今天不管怎么样也要\x01",
            "订到安特洛丝餐厅的座位！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "为了这一天\x01",
            "我已经存了很长时间的钱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "啊啊，我的心情好激动。\x01",
            "要赶快把工作搞定！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_1066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_11B9")

    ChrTalk(
        0xFE,
        (
            "工作完成之后，\x01",
            "先去吃饭，\x01",
            "然后到超市去看看衣服……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "最近那家店的评价挺不错。\x01",
            "衣服的设计也很可爱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "我要去看看\x01",
            "有没有新的款式出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_11B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_122F")

    ChrTalk(
        0xFE,
        "哈～忙死了忙死了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "好想把讨厌的工作赶快解决掉，\x01",
            "然后马上出去玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122F")

    TalkEnd(0x9)
    Return()

    # Function_6_B68 end

    def Function_7_1233(): pass

    label("Function_7_1233")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　　洗衣房　　　　　　　\x01",
            "※工作人员以外禁止进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_1233 end

    SaveToFile()

Try(main)
