import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4139_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4139_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4139.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4139_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-60500, 0, -44360, 0)
    OP_67(0, 5480, -10000, 0)
    CameraSetDistance(2850, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -59600, 0, -45100, 270)
    ChrSetPos(0x0105, -58710, 0, -44550, 270)
    ChrSetPos(0x0104, -58080, 0, -45950, 270)
    ChrSetPos(0x0108, -57070, 0, -45700, 270)
    OP_0D()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书页之间\n',
            '夹着一张卡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170460349V　　　门已打开。　\n',
            '参加『勇者们的舞会』吧。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460350V#1019F这、这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460351V#073F原来如此，这个地方地区\n',
            '是在共和国的管辖区内……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460352V#072F正是所谓『异国之馆』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460353V#044F而『苍之骑士』\n',
            '看来是小说的登场人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460354V#1009F真是的……\n',
            '够会给人\n',
            '添麻烦的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460355V#1000F不过，看来这是最后了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460356V#035F『勇者们的舞会』啊……\n',
            '那么，是说哪个地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x0040)
    OP_28(0x00C4, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
