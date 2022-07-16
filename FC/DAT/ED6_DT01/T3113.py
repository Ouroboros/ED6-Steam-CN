import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3113_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3113   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3113.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3BE
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_B4'),
        (-1, 'loc_C3'),
    )

    def _loc_B4(): pass

    label('loc_B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 2, 0x50A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C0',
    )

    Event(0, 0x0002)

    def _loc_C0(): pass

    label('loc_C0')

    Jump('loc_C3')

    def _loc_C3(): pass

    label('loc_C3')

    Return()

# id: 0x0001 offset: 0xC4
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_109')

    def _loc_DC(): pass

    label('loc_DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_109')

    def _loc_F4(): pass

    label('loc_F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_109',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_109(): pass

    label('loc_109')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11B',
    )

    OP_10(0x07, 0x01)
    OP_10(0x06, 0x00)

    def _loc_11B(): pass

    label('loc_11B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_191',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_191',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A8, 7, 0x547)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 0, 0x548)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 1, 0x549)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 2, 0x54A)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 3, 0x54B)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_191',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_191(): pass

    label('loc_191')

    Return()

# id: 0x0002 offset: 0x192
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrPos(0x0101, 300, 0, -3400, 0)
    SetChrPos(0x0102, -700, 0, -4300, 0)
    SetChrPos(0x0107, 600, 0, -4400, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 1, 0x509)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_342',
    )

    CameraMove(-200, 0, 1200, 0)
    OP_67(0, 6400, -10000, 0)
    CameraMove(-200, 34000, 1200, 6000)
    Sleep(1000)

    Fade(1000)
    CameraMove(-200, 0, 1200, 0)
    OP_67(0, 9500, -10000, 0)
    SetScenaFlags(ScenaFlag(0x00A1, 1, 0x509))

    ChrTalk(
        0x0101,
        (
            '#0010070510V#000F哇～……\n',
            '好高的楼梯间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070511V#060F啊，这里是紧急通道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070512V除了紧急时刻，\n',
            '是不能使用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070513V#000F是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070514V唔～有点遗憾呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070515V#010F这有什么遗憾的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070516V还是回走廊里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070517V#000F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AE')

    def _loc_342(): pass

    label('loc_342')

    ChrTalk(
        0x0102,
        (
            '#0020070518V#010F这个楼梯，\n',
            '除了紧急时刻是不能用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070519V还是回走廊里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070520V#000F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AE(): pass

    label('loc_3AE')

    NewScene('ED6_DT01/T3111._SN', 111, 1, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
