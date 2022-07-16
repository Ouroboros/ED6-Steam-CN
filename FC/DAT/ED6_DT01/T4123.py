import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4123_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4123   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '亚妮拉丝'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4123.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2C1
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
    )

# id: 0x10003 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xD2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F4',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 10500, 0, 5390, 90)

    def _loc_F4(): pass

    label('loc_F4')

    Return()

# id: 0x0001 offset: 0xF5
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xF6
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 4, 0x64C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B7',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 9240, 0, 5790, 90)
    SetChrPos(0x0102, 9180, 0, 4760, 90)
    SetChrPos(0x0108, 8280, 0, 5410, 90)
    ChrTurnDirection(0x0008, 0x0108, 0)
    SetScenaFlags(ScenaFlag(0x00C9, 4, 0x64C))
    CameraMove(9900, 0, 5380, 1000)

    ChrTalk(
        0x0008,
        (
            '啊呀，\n',
            '这不是两位新人和金大哥吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120130130V这么快就从城里回来啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，虽然是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F亚妮拉丝前辈。\n',
            '占用你一点时间好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '什么事，什么事？\n',
            '有什么好玩儿的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130135V好玩儿倒是不至于，\n',
            '但是会下人一跳的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '咦……\n',
            '好像不太好玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在这儿站着不好说话，\n',
            '我们到外面的休息处去如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2B7(): pass

    label('loc_2B7')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
