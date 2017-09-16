from ED6ScenarioHelper import *

def main():
    # 封印区域　最下层

    CreateScenaFile(
        FileName            = 'C4302   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4302.x',
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


    DeclEvent(
        X                   = -5160,
        Y                   = -1000,
        Z                   = 29010,
        Range               = 5000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x68A6,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = 0,
        Y                   = -5000,
        Z                   = -62000,
        Range               = 3000,
        Unknown_10          = 0x5DC,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 7320,
        TriggerZ            = 0,
        TriggerY            = 38820,
        TriggerRange        = 1000,
        ActorX              = 7320,
        ActorZ              = 1000,
        ActorY              = 38820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_10E",          # 00, 0
        "Function_1_122",          # 01, 1
        "Function_2_174",          # 02, 2
        "Function_3_4DC",          # 03, 3
        "Function_4_56B",          # 04, 4
        "Function_5_631",          # 05, 5
    )


    def Function_0_10E(): pass

    label("Function_0_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_11C")
    OP_A3(0x3FA)
    Event(0, 4)

    label("loc_11C")

    OP_72(0x0, 0x20)
    Return()

    # Function_0_10E end

    def Function_1_122(): pass

    label("Function_1_122")

    OP_10(0x0, 0x0)
    OP_72(0x0, 0x20)
    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x6, 0xFF, 7300, 1200, 38800, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_122 end

    def Function_2_174(): pass

    label("Function_2_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 1)), scpexpr(EXPR_END)), "loc_17C")
    Return()

    label("loc_17C")

    OP_A2(0x669)
    OP_28(0x4F, 0x1, 0x10)
    EventBegin(0x0)

    def lambda_18D():
        OP_6D(370, 0, 41310, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18D)

    def lambda_1A5():
        OP_6E(406, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A5)
    Sleep(4000)
    Fade(1000)
    OP_6D(10, 0, 31240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1170, 0, 31250, 0)
    SetChrPos(0x1, 1120, 0, 31250, 0)
    SetChrPos(0x2, -640, 0, 29640, 0)
    SetChrPos(0x3, 530, 0, 29730, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#580F这里……\x02\x03",
            "为什么这里的感觉和\x01",
            "之前经过的地方不同呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F7")

    ChrTalk(
        0x107,
        (
            "#062F这里的导力压很高，\x01",
            "大概是接近封印地点了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_461")

    label("loc_2F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347")

    ChrTalk(
        0x103,
        (
            "#022F没错，虽然没有风，\x01",
            "可是身体能感到强大的压迫感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_461")

    label("loc_347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_387")

    ChrTalk(
        0x106,
        (
            "#057F确实……\x01",
            "有种难以呼吸的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_461")

    label("loc_387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DB")

    ChrTalk(
        0x105,
        (
            "#047F能够感到……\x01",
            "巨大的能量在流动着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_461")

    label("loc_3DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_421")

    ChrTalk(
        0x108,
        (
            "#072F啊啊……\x01",
            "能感到像龙穴一般的气息流动……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_461")

    label("loc_421")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_461")

    ChrTalk(
        0x104,
        (
            "#032F这个是……\x01",
            "导力波的流动吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_461")


    ChrTalk(
        0x102,
        (
            "#015F这里应该就是终点了。\x02\x03",
            "#012F做好充足的准备之后，\x01",
            "我们就一鼓作气冲进去吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_2_174 end

    def Function_3_4DC(): pass

    label("Function_3_4DC")

    EventBegin(0x0)
    Fade(1000)
    OP_89(0x0, -800, 20000, -62800, 0)
    OP_89(0x1, 800, 20000, -62800, 0)
    OP_89(0x2, 800, 20000, -61200, 0)
    OP_89(0x3, -800, 20000, -61200, 0)
    OP_6D(0, -4000, -62000, 1500)
    Sleep(100)
    OP_B0(0x0, 0x5A)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 1600)
    OP_70(0x0, 0x3E8)
    Sleep(2000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_4DC end

    def Function_4_56B(): pass

    label("Function_4_56B")

    EventBegin(0x0)
    SetPlaceName(0xE3) # 封印区域　最下层
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x0, 1300)
    OP_70(0x0, 0x640)
    OP_48()
    OP_89(0x0, -800, 20000, -62800, 0)
    OP_89(0x1, 800, 20000, -62800, 0)
    OP_89(0x2, 800, 20000, -61200, 0)
    OP_89(0x3, -800, 20000, -61200, 0)
    OP_6D(0, -4000, -62000, 0)
    OP_73(0x0)
    Sleep(100)
    Fade(1000)
    SetChrPos(0x0, 0, -4000, -58600, 0)
    SetChrPos(0x1, 0, -4000, -58600, 0)
    SetChrPos(0x2, 0, -4000, -58600, 0)
    SetChrPos(0x3, 0, -4000, -58600, 0)
    EventEnd(0x0)
    Return()

    # Function_4_56B end

    def Function_5_631(): pass

    label("Function_5_631")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F3")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x7, 0x20)
    OP_6F(0x7, 300)
    OP_70(0x7, 0x1F4)
    OP_73(0x7)
    OP_6F(0x7, 500)
    OP_70(0x7, 0x2BC)
    OP_71(0x7, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x6, 0x2)
    LoadEffect(0x5, "map\\\\mp027_01.eff")
    PlayEffect(0x5, 0x6, 0xFF, 7300, 1200, 38800, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
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
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x6, 0x0)
    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x0, 0xFF, 7300, 1200, 38800, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_7F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_80D")

    Return()

    # Function_5_631 end

    SaveToFile()

Try(main)
