from ED6ScenarioHelper import *

def main():
    # 古罗尼山道

    CreateScenaFile(
        FileName            = 'C1501_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C1501.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60022",
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_67",           # 01, 1
        "Function_2_21DF",         # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Return()

    # Function_0_66 end

    def Function_1_67(): pass

    label("Function_1_67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F")
    Return()

    label("loc_7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21DE")
    OP_28(0x1F, 0x1, 0x4000)
    OP_28(0x1F, 0x4, 0x8)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB")
    TurnDirection(0x101, 0x8, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0x101,
        "#004F啊…………！\x02",
    )

    CloseMessageWindow()
    Jump("loc_177")

    label("loc_DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121")
    TurnDirection(0x102, 0x8, 0)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0x102,
        "#014F那是…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_177")

    label("loc_121")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177")
    TurnDirection(0x105, 0x8, 0)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(
        0x105,
        "#044F那、那是…………！\x02",
    )

    CloseMessageWindow()

    label("loc_177")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_191():
        OP_6D(-101100, 3350, 66300, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_191)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1BB():
        OP_8E(0x8, 0xFFFE7514, 0xD16, 0x102FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BB)

    def lambda_1D6():
        OP_8E(0x9, 0xFFFE744C, 0xD16, 0x10298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D6)

    def lambda_1F1():
        OP_8E(0xA, 0xFFFE7514, 0xD16, 0x1016C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F1)

    def lambda_20C():
        OP_8E(0xB, 0xFFFE74B0, 0xD16, 0x103C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_20C)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x105, 0x40)

    def lambda_23B():
        OP_8E(0x101, 0xFFFE889C, 0xFA0, 0x11FE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23B)

    def lambda_256():
        OP_8E(0x102, 0xFFFE8C84, 0xFA0, 0x123CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_256)

    def lambda_271():
        OP_8E(0x105, 0xFFFE906C, 0xFA0, 0x127B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_271)
    OP_8C(0x8, 0, 400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    OP_43(0x8, 0x1, 0x1, 0x2)
    WaitChrThread(0x9, 0x1)

    def lambda_2C7():
        OP_8E(0x9, 0xFFFE6A24, 0x834, 0xF8D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C7)
    WaitChrThread(0xA, 0x1)

    def lambda_2E7():
        OP_8E(0xA, 0xFFFE7064, 0x9C4, 0xFA00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2E7)
    WaitChrThread(0xB, 0x1)

    def lambda_307():
        OP_8E(0xB, 0xFFFE7578, 0xA5A, 0xF6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_307)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0x9, 0x1)

    def lambda_32C():
        OP_8E(0x9, 0xFFFE6A24, 0x834, 0xE9FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32C)

    def lambda_347():
        OP_8E(0x101, 0xFFFE72BC, 0x960, 0xF80C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_347)
    WaitChrThread(0xA, 0x1)

    def lambda_367():
        OP_8E(0xA, 0xFFFE6DA8, 0x834, 0xEF10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_367)

    def lambda_382():
        OP_8E(0x102, 0xFFFE6E70, 0xA28, 0xFC57, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_382)
    WaitChrThread(0xB, 0x1)

    def lambda_3A2():
        OP_8E(0xB, 0xFFFE7640, 0x8B6, 0xEE48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A2)

    def lambda_3BD():
        OP_8E(0x105, 0xFFFE74B0, 0xC1C, 0xFFDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3BD)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 0)
    SetChrChipByIndex(0x101, 3)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_42D():
        OP_69(0xC, 0x320)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_42D)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 0)
    SetChrChipByIndex(0x102, 5)
    WaitChrThread(0x105, 0x1)
    TurnDirection(0x105, 0x8, 0)
    SetChrChipByIndex(0x105, 7)
    WaitChrThread(0x8, 0x1)

    ChrTalk(
        0x8,
        "哇、哇～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "救、救救我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#005F约修亚，我们上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#012F嗯！\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 8)

    def lambda_4D6():
        OP_94(0x1, 0x101, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D6)

    def lambda_4EC():
        OP_94(0x1, 0x102, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4EC)

    def lambda_502():
        OP_94(0x1, 0x105, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_502)
    Sleep(400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x3F4, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_4A(0x8, 255)
    AddParty(0x36, 0x3)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    SetChrChipByIndex(0x105, 7)
    SetChrPos(0x101, -101700, 2400, 63500, 180)
    SetChrPos(0x102, -104300, 2000, 63100, 180)
    SetChrPos(0x105, -102900, 2500, 64200, 180)
    SetChrPos(0x137, -102260, 1950, 58980, 356)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x0)
    OP_6C(265000, 0)
    OP_0D()
    SetChrChipByIndex(0x105, 65535)
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(
        0x105,
        (
            "#043F呼……\x01",
            "我们总算是赶上了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)

    def lambda_658():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_658)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        (
            "#002F是啊，\x01",
            "真是千钧一发。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(
        0x102,
        "#010F您没有受伤吧？\x02",
    )

    CloseMessageWindow()

    def lambda_6C0():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(
        0x8,
        "嗯，我没事。\x02",
    )

    CloseMessageWindow()
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_73B():
        OP_69(0xC, 0x320)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_73B)
    OP_8E(0x137, 0xFFFE6DA8, 0x834, 0xF0A0, 0x7D0, 0x0)
    WaitChrThread(0x137, 0x1)
    TalkBegin(0x137)
    TurnDirection(0x137, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_126D")
    OP_28(0x1F, 0x1, 0x8)
    OP_28(0x1F, 0x1, 0x10)

    ChrTalk(
        0x137,
        (
            "多亏了你们，\x01",
            "我没有受一点伤…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "………………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "我好像…………\x01",
            "在哪里见过你啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(
        0x101,
        "#000F咦，这么说来……\x02",
    )

    CloseMessageWindow()
    OP_62(0x137, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x137,
        "哦，想起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "你不就是洛连特的\x01",
            "那个小村姑吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F啊？\x02\x03",
            "#005F你、你是那个\x01",
            "寻找蘑菇的大奸商！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F艾丝蒂尔……\x01",
            "不要太失礼了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(
        0x137,
        (
            "还是和以前一样，\x01",
            "连最基本的礼貌都不懂啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "真是的，\x01",
            "这就是在乡下长大的关系吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#009F胡、胡说八道～\x01",
            "你自己才是个怪异食材的收集狂。\x02\x03",
            "反正这次也肯定是\x01",
            "为了找那些奇怪的食物吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "哼，\x01",
            "今天我已经采集到了珍贵的野菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "跟你说，\x01",
            "这种野菜可是比『荧光菇』\x01",
            "更有个性的食材哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "哼哼，\x01",
            "这次的生意一定会很顺利的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#004F哎呀呀？\x01",
            "『这次的』一定……\x02\x03",
            "#507F那个叫『荧光菇』的东西\x01",
            "果然没有卖出去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x137, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(
        0x137,
        "胡、胡说！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "只、只是\x01",
            "碰巧没人需要罢了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#044F啊，艾丝蒂尔。\x02\x03",
            "听到和野菜有关的事情，\x01",
            "你有没有想起什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#505F嗯，听你这么一说……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#010F是和玛诺利亚村的\x01",
            "阿梅莉娅小姐有关的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(
        0x137,
        "你说阿梅莉娅？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "我的侄女\x01",
            "就叫做阿梅莉娅……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊…………？\x02\x03",
            "……这么说，\x01",
            "这个人就是阿梅莉娅小姐的叔父吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(
        0x102,
        "#010F看来就是如此。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x137, 400)

    ChrTalk(
        0x137,
        (
            "你们说什么？\x01",
            "我侄女她怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F实际上，\x01",
            "就是阿梅莉娅小姐\x01",
            "委托我们为您做护卫的……\x02\x03",
            "可是当我们到达玛诺利亚村时，\x01",
            "您已经出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "……嗯，是这样啊。\x01",
            "的确是让阿梅莉娅担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "可是，我也没有办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "为了下次的生意，\x01",
            "我好歹也要准备一些礼品嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F可是就为了这种荒唐的事，\x01",
            "你差一点就成为\x01",
            "危险魔兽的食物了啊。\x02\x03",
            "如果变成那样，\x01",
            "做生意什么的也就毫无意义了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x101, 400)

    ChrTalk(
        0x137,
        "…………唔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F回去后好好地\x01",
            "向阿梅莉娅小姐道歉吧。\x02\x03",
            "她现在一定很担心你的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "…………嗯，我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "等这回在格兰赛尔的\x01",
            "生意做完之后，\x01",
            "我保证好好向她道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "我也觉得应该这样做。\x02\x03",
            "…………那么，\x01",
            "我们这就出发吧。\x02\x03",
            "把您送回村子里。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(
        0x137,
        "哦，那太感谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "回去的路上就拜托你们了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C3")

    label("loc_126D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1B10")
    OP_28(0x1F, 0x1, 0x8)
    OP_28(0x1F, 0x1, 0x10)

    ChrTalk(
        0x137,
        (
            "多亏了你们，\x01",
            "我没有受一点伤…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "…………嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "我好像…………\x01",
            "在哪里见过你啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_142D")

    ChrTalk(
        0x101,
        (
            "#004F啊？\x02\x03",
            "#005F你、你是那个\x01",
            "寻找蘑菇的大奸商！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#018F艾丝蒂尔……\x01",
            "不要太失礼了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)
    Jump("loc_1443")

    label("loc_142D")


    ChrTalk(
        0x101,
        "#004F哎，是吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1443")

    OP_62(0x137, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(
        0x137,
        "哦，想起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "你们不就是\x01",
            "我在洛连特见过的游击士吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(
        0x102,
        (
            "#010F很久不见了。\x02\x03",
            "工作还顺利吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(
        0x137,
        (
            "唔，\x01",
            "今天也采到了贵重的野菜呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "跟你说，\x01",
            "这种野菜可是比『荧光菇』\x01",
            "更有个性的食材哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "这次的商谈\x01",
            "肯定会进行得很顺利。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#044F啊，艾丝蒂尔。\x02\x03",
            "听到和野菜有关的事情，\x01",
            "你有没有想起什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#505F嗯，听你这么一说……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#010F是和玛诺利亚村的\x01",
            "阿梅莉娅小姐有关的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(
        0x137,
        "你说阿梅莉娅？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "我的侄女\x01",
            "就叫做阿梅莉娅……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊…………？\x02\x03",
            "……这么说，\x01",
            "这个人就是阿梅莉娅小姐的叔父吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(
        0x102,
        "#010F看来就是如此。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x137, 400)

    ChrTalk(
        0x137,
        (
            "你们说什么？\x01",
            "我侄女她怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F实际上，\x01",
            "就是阿梅莉娅小姐\x01",
            "委托我们为您做护卫的……\x02\x03",
            "可是当我们到达玛诺利亚村时，\x01",
            "您已经出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "……嗯，是这样啊。\x01",
            "的确是让阿梅莉娅担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "可是，我也没有办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "为了下次的生意，\x01",
            "我好歹也要准备一些礼品嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F可是就为了这种荒唐的事，\x01",
            "你差一点就成为\x01",
            "危险魔兽的食物了啊。\x02\x03",
            "如果变成那样，\x01",
            "做生意什么的也就毫无意义了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x101, 400)

    ChrTalk(
        0x137,
        "…………唔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F回去后好好地\x01",
            "向阿梅莉娅小姐道歉吧。\x02\x03",
            "她现在一定很担心你的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "…………嗯，我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "等这回在格兰赛尔的\x01",
            "生意做完之后，\x01",
            "我保证好好向她道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "我也觉得应该这样做。\x02\x03",
            "…………那么，\x01",
            "我们这就出发吧。\x02\x03",
            "把您送回村子里。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(
        0x137,
        "哦，那太感谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "回去的路上就拜托你们了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C3")

    label("loc_1B10")

    OP_28(0x1F, 0x1, 0x20)
    OP_28(0x1F, 0x1, 0x40)

    ChrTalk(
        0x137,
        (
            "多亏了你们，\x01",
            "我也毫发无伤呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "不愧是游击士，\x01",
            "功夫真是厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(
        0x101,
        (
            "#501F那么，你在这种山路上\x01",
            "到底是想干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "唔，\x01",
            "我是专门收集高级食材的商人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "今天是为了\x01",
            "寻找贵重的野菜\x01",
            "才来这种地方的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(
        0x105,
        (
            "#044F野菜…………？\x02\x03",
            "啊，艾丝蒂尔。\x02\x03",
            "听到和野菜有关的事情，\x01",
            "你有没有想起什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(
        0x101,
        "#505F嗯，听你这么一说……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(
        0x102,
        (
            "#010F是和玛诺利亚村的\x01",
            "阿梅莉娅小姐有关的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(
        0x137,
        "你说阿梅莉娅？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "我的侄女\x01",
            "就叫做阿梅莉娅……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(
        0x101,
        (
            "#004F啊…………？\x02\x03",
            "……这么说，\x01",
            "这个人就是阿梅莉娅小姐的叔父吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(
        0x102,
        "#010F看来就是如此。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x137, 400)

    ChrTalk(
        0x137,
        (
            "你们说什么？\x01",
            "我侄女她怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F实际上，\x01",
            "就是阿梅莉娅小姐\x01",
            "委托我们为您做护卫的……\x02\x03",
            "可是当我们到达玛诺利亚村时，\x01",
            "您已经出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "……嗯，是这样啊。\x01",
            "的确是让阿梅莉娅担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "可是，我也没有办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "为了下次的生意，\x01",
            "我好歹也要准备一些礼品嘛……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F可是就为了这种荒唐的事，\x01",
            "你差一点就成为\x01",
            "危险魔兽的食物了啊。\x02\x03",
            "如果变成那样，\x01",
            "做生意什么的也就毫无意义了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x101, 400)

    ChrTalk(
        0x137,
        "…………唔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#002F回去后好好地\x01",
            "向阿梅莉娅小姐道歉吧。\x02\x03",
            "她现在一定很担心你的。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "…………嗯，我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        (
            "等这回在格兰赛尔的\x01",
            "生意做完之后，\x01",
            "我保证好好向她道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F嗯，\x01",
            "我也觉得应该这样做。\x02\x03",
            "…………那么，\x01",
            "我们这就出发吧。\x02\x03",
            "把您送回村子里。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(
        0x137,
        "哦，那太感谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x137,
        "回去的路上就拜托你们了。\x02",
    )

    CloseMessageWindow()

    label("loc_21C3")

    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x137, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x137, 0x40)
    EventEnd(0x0)

    label("loc_21DE")

    Return()

    # Function_1_67 end

    def Function_2_21DF(): pass

    label("Function_2_21DF")

    OP_44(0xC, 0x1)

    def lambda_21E9():
        OP_6D(-102000, 1930, 59600, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_21E9)
    OP_8E(0x8, 0xFFFE70C8, 0x9C4, 0xF424, 0xBB8, 0x0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x8, 0, 400)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x8, 0x4)
    OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
    Sleep(400)
    OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
    Sleep(400)
    OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
    Sleep(400)
    OP_8C(0x8, 180, 400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)
    OP_8C(0x8, 0, 400)
    Return()

    # Function_2_21DF end

    SaveToFile()

Try(main)
