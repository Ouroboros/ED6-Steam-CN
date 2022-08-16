import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import E0010_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0010   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0010.x'
    header.mapIndex       = 49
    header.bgm            = 30
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            word_3A         = 49,
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
        ScenaActorData(
            triggerX            = 58996,
            triggerZ            = -448,
            triggerY            = 48932,
            triggerRange        = 1700,
            actorX              = 58920,
            actorZ              = -200,
            actorY              = 49040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 59075,
            triggerZ            = -2000,
            triggerY            = 54692,
            triggerRange        = 1700,
            actorX              = 59075,
            actorZ              = -1600,
            actorY              = 54692,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 25983,
            triggerZ            = 200,
            triggerY            = -8664,
            triggerRange        = 1700,
            actorX              = 25510,
            actorZ              = 1200,
            actorY              = -8070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 84719,
            triggerZ            = 0,
            triggerY            = 44588,
            triggerRange        = 1700,
            actorX              = 84719,
            actorZ              = 2000,
            actorY              = 44588,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 89364,
            triggerZ            = -1000,
            triggerY            = 53636,
            triggerRange        = 1700,
            actorX              = 89364,
            actorZ              = -600,
            actorY              = 53636,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33110,
            triggerZ            = 0,
            triggerY            = 5650,
            triggerRange        = 1700,
            actorX              = 33110,
            actorZ              = 1500,
            actorY              = 5650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x180
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_198'),
        (0x0000006D, 'loc_1A7'),
        (0x00000073, 'loc_1AD'),
        (0x00000069, 'loc_1B3'),
        (-1, 'loc_1B9'),
    )

    def _loc_198(): pass

    label('loc_198')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 1, 0x321)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A4',
    )

    Event(0, func_02_1DF)

    def _loc_1A4(): pass

    label('loc_1A4')

    Jump('loc_1B9')

    def _loc_1A7(): pass

    label('loc_1A7')

    SetScenaFlags(ScenaFlag(0x0064, 3, 0x323))

    Jump('loc_1B9')

    def _loc_1AD(): pass

    label('loc_1AD')

    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))

    Jump('loc_1B9')

    def _loc_1B3(): pass

    label('loc_1B3')

    SetScenaFlags(ScenaFlag(0x0064, 5, 0x325))

    Jump('loc_1B9')

    def _loc_1B9(): pass

    label('loc_1B9')

    Return()

# id: 0x0001 offset: 0x1BA
@scena.Code('func_01_1BA')
def func_01_1BA():
    OP_72(0x0003, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 0, 0x328)),
            Expr.Return,
        ),
        'loc_1DE',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)

    def _loc_1DE(): pass

    label('loc_1DE')

    Return()

# id: 0x0002 offset: 0x1DF
@scena.Code('func_02_1DF')
def func_02_1DF():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(30980, 0, -4620, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 27350, 0, 5680, 103)
    ChrSetPos(0x0102, 26450, 0, 5010, 114)
    ChrSetPos(0x0103, 27280, 0, 4760, 101)

    @scena.Lambda('lambda_025C')
    def lambda_025C():
        OP_6C(65000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_025C)

    CameraMove(29950, 0, 4840, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010021823V#505F哇～……\n',
            '空荡荡了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021824V一点货物也不剩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021825V#013F好像都被那些空贼给搬运走了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021826V这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021827V#022F……不管怎么样，\n',
            '先到处调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0351')
    def lambda_0351():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0351)

    OP_69(0x0000, 1500)
    SetScenaFlags(ScenaFlag(0x0064, 1, 0x321))
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x368
@scena.Code('func_03_368')
def func_03_368():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_416',
    )

    EventBegin(0x00)
    CameraMove(58996, -448, 48932, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010021838V#501F这好像是机长的座位吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021839V#007F如果是平常的话，\n',
            '真想高兴地坐坐看呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021840V#018F还是不要坐了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_453')

    def _loc_416(): pass

    label('loc_416')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '机长席上没有人坐着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_453(): pass

    label('loc_453')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0004 offset: 0x457
@scena.Code('func_04_457')
def func_04_457():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CD',
    )

    EventBegin(0x00)
    CameraMove(59075, -2000, 54692, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010021836V#505F这个是操纵用的舵轮吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021837V操作的人……\n',
            '现在在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_508')

    def _loc_4CD(): pass

    label('loc_4CD')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是操纵用的舵轮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_508(): pass

    label('loc_508')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0005 offset: 0x50C
@scena.Code('func_05_50C')
def func_05_50C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B4',
    )

    EventBegin(0x00)
    CameraMove(25983, 200, -8664, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010021833V#004F这是什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021834V#022F嗯……\n',
            '是导力引擎的控制面板。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021835V看起来，\n',
            '导力已经完全切断了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_60B')

    def _loc_5B4(): pass

    label('loc_5B4')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是导力引擎的控制面板。\n',
            '   ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '导力完全停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_60B(): pass

    label('loc_60B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0006 offset: 0x60F
@scena.Code('func_06_60F')
def func_06_60F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C7',
    )

    EventBegin(0x00)
    CameraMove(33110, 0, 5650, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010021830V#004F这个是起重车吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021831V#012F和在洛连特飞艇坪\n',
            '见过的是同一种型号呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021832V大概就是用这种东西\n',
            '把货物运出去的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_706')

    def _loc_6C7(): pass

    label('loc_6C7')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是运输货物的起重车。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_706(): pass

    label('loc_706')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

# id: 0x0007 offset: 0x70A
@scena.Code('func_07_70A')
def func_07_70A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_794',
    )

    EventBegin(0x00)
    CameraMove(84719, 1000, 44588, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010021842V#505F这个盆栽……\n',
            '好像没什么生气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021843V#012F应该已经好几天\n',
            '没有浇水了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_7D1')

    def _loc_794(): pass

    label('loc_794')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '盆栽已经有些枯萎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_7D1(): pass

    label('loc_7D1')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0008 offset: 0x7D5
@scena.Code('func_08_7D5')
def func_08_7D5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_827',
    )

    EventBegin(0x00)
    CameraMove(89364, -600, 53636, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010021841V#003F好刺眼……\n',
            '有光线射进来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_864')

    def _loc_827(): pass

    label('loc_827')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '从外面有光线射进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_864(): pass

    label('loc_864')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
