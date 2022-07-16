import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1211_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1211_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1211.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4F4
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    EventBegin(0x00)
    SetMapFlags(0x00400000)
    CameraMove(-10, 0, -7120, 0)
    SetChrPos(0x0101, 280, 0, -20580, 0)
    SetChrPos(0x0102, 1080, 0, -21780, 0)
    SetChrPos(0x0103, -780, 0, -21880, 0)

    @scena.Lambda('lambda_00B5')
    def lambda_00B5():
        ChrMoveToRelative(0x0101, 0, 0, 4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_00B5)

    Sleep(100)

    @scena.Lambda('lambda_00D5')
    def lambda_00D5():
        ChrMoveToRelative(0x0102, 0, 0, 4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_00D5)

    Sleep(100)

    @scena.Lambda('lambda_00F5')
    def lambda_00F5():
        ChrMoveToRelative(0x0103, 0, 0, 4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_00F5)

    FadeIn(1000, 0)
    CameraMove(480, 0, -17620, 3500)
    OP_0D()
    WaitForThreadExit(0x0103, 0x0001)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010151080V#000F嗯～…………\n',
            '这座塔叫什么名字来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151081V#010F『琥珀之塔』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151082V是被世人称作『四轮之塔』的\n',
            '古代遗迹的其中一座。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151083V#000F啊，是吗。\n',
            '怪不得和『翡翠之塔』很像呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151084V虽然总体的色调完全不同，\n',
            '不过气氛是相同的……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0101, 0, 400)
    Sleep(400)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151085V#014F…………怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151086V#505F嗯，没什么…………\n',
            '好像听到了说话的声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0008, 19240, 0, 33890, 42)
    SetChrPos(0x0009, 10000, 0, 25000, 45)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrDirection(0x0102, 0, 0)
    CameraMove(170, 0, -8790, 3000)

    ChrTalk(
        0x0008,
        (
            '#0150151087V……………………。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0150151088V………………，\n',
            '……………………。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '#0150151089V………………！？\n',
            '……………………。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    Fade(1000)
    CameraMove(480, 0, -17620, 0)
    SetChrDirection(0x0102, 0, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020151090V#012F…………果然，\n',
            '好像有谁在里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151091V#002F……啊，难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151092V#027F呵呵，\n',
            '偶尔绕绕远路也是不错的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151093V说不定\n',
            '我们无意中中了头彩哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151094V有必要调查一番呢。\n',
            '…………不过一定要慎重行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151095V#002F嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    OP_28(0x000F, 0x04, 0x02)
    OP_28(0x000F, 0x04, 0x04)
    OP_28(0x000F, 0x01, 0x0001)
    OP_28(0x000F, 0x01, 0x0002)
    OP_28(0x000F, 0x01, 0x8000)
    ClearMapFlags(0x00400000)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
