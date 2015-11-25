from ED6ScenarioHelper import *

def main():
    # 柏斯

    CreateScenaFile(
        FileName            = 'C1211_1 ._SN',
        MapName             = 'Bose',
        Location            = 'C1211.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    OP_6D(-10, 0, -7120, 0)
    SetChrPos(0x101, 280, 0, -20580, 0)
    SetChrPos(0x102, 1080, 0, -21780, 0)
    SetChrPos(0x103, -780, 0, -21880, 0)

    def lambda_B7():
        OP_90(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7)
    Sleep(100)

    def lambda_D7():
        OP_90(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D7)
    Sleep(100)

    def lambda_F7():
        OP_90(0x103, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F7)
    FadeToBright(1000, 0)
    OP_6D(480, 0, -17620, 3500)
    OP_0D()
    WaitChrThread(0x103, 0x1)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#000F嗯～…………\x01",
            "这座塔叫什么名字来着？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#010F『琥珀之塔』。\x02\x03",
            "是被世人称作『四轮之塔』的\x01",
            "古代遗迹的其中一座。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(
        0x101,
        (
            "#000F啊，是吗。\x01",
            "怪不得和『翡翠之塔』很像呢。\x02\x03",
            "虽然总体的色调完全不同，\x01",
            "不过气氛是相同的……………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 0, 400)
    Sleep(400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        "#014F…………怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#505F嗯，没什么…………\x01",
            "好像听到了说话的声音……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 19240, 0, 33890, 42)
    SetChrPos(0x9, 10000, 0, 25000, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_8C(0x102, 0, 0)
    OP_6D(170, 0, -8790, 3000)

    ChrTalk(
        0x8,
        "……………………。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "………………、\x01",
            "……………………。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x9,
        (
            "………………！？\x01",
            "……………………。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Fade(1000)
    OP_6D(480, 0, -17620, 0)
    OP_8C(0x102, 0, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#012F…………果然，\x01",
            "好像有谁在里面。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(
        0x101,
        "#002F……啊，难道是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(
        0x103,
        (
            "#027F呵呵，\x01",
            "偶尔绕绕远路也是不错的嘛。\x02\x03",
            "说不定\x01",
            "我们无意中中了头彩哦。\x02\x03",
            "有必要调查一番呢。\x01",
            "…………不过一定要慎重行事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#002F嗯。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_28(0xF, 0x4, 0x2)
    OP_28(0xF, 0x4, 0x4)
    OP_28(0xF, 0x1, 0x1)
    OP_28(0xF, 0x1, 0x2)
    OP_28(0xF, 0x1, 0x8000)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
