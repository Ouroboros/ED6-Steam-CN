import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4302   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4302.x'
    header.mapIndex       = 216
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7CC
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
        ScenaEventData(
            x           = -5160,
            y           = -1000,
            z           = 29010,
            range       = 5000,
            dword_10    = 0x000003E8,
            dword_14    = 0x000068A6,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = 0,
            y           = -5000,
            z           = -62000,
            range       = 3000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0xE8
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 7320,
            triggerZ            = 0,
            triggerY            = 38820,
            triggerRange        = 1000,
            actorX              = 7320,
            actorZ              = 1000,
            actorY              = 38820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x10C
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_11A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0004)

    def _loc_11A(): pass

    label('loc_11A')

    OP_72(0x0000, 0x0020)

    Return()

# id: 0x0001 offset: 0x120
@scena.Code('Init')
def Init():
    OP_10(0x00, 0x00)
    OP_72(0x0000, 0x0020)
    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 7300, 1200, 38800, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x172
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 1, 0x669)),
            Expr.Return,
        ),
        'loc_17A',
    )

    Return()

    def _loc_17A(): pass

    label('loc_17A')

    SetScenaFlags(ScenaFlag(0x00CD, 1, 0x669))
    OP_28(0x004F, 0x01, 0x0010)
    EventBegin(0x00)

    @scena.Lambda('lambda_018B')
    def lambda_018B():
        CameraMove(370, 0, 41310, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_018B)

    @scena.Lambda('lambda_01A3')
    def lambda_01A3():
        OP_6E(406, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_01A3)

    Sleep(4000)

    Fade(1000)
    CameraMove(10, 0, 31240, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -1170, 0, 31250, 0)
    SetChrPos(0x0001, 1120, 0, 31250, 0)
    SetChrPos(0x0002, -640, 0, 29640, 0)
    SetChrPos(0x0003, 530, 0, 29730, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010140141V#580F这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140142V为什么这里的感觉和\n',
            '之前经过的地方不同呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140143V#062F这里的导力压很高，\n',
            '大概是接近封印地点了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_430')

    def _loc_2D5(): pass

    label('loc_2D5')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_327',
    )

    ChrTalk(
        0x0103,
        (
            '#0030140144V#022F没错，虽然没有风，\n',
            '可是身体能感到强大的压迫感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_430')

    def _loc_327(): pass

    label('loc_327')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_367',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140145V#057F确实……\n',
            '有种难以呼吸的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_430')

    def _loc_367(): pass

    label('loc_367')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3AB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140146V#047F能够感到……\n',
            '巨大的能量在流动着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_430')

    def _loc_3AB(): pass

    label('loc_3AB')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3F5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140147V#072F啊啊……\n',
            '能感到像龙穴一般的气息流动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_430')

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_430',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140148V#032F这个是……\n',
            '导力波的流动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_430(): pass

    label('loc_430')

    ChrTalk(
        0x0102,
        (
            '#0020140149V#015F这里应该就是终点了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140150V#012F做好充足的准备之后，\n',
            '我们就一鼓作气冲进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x494
@scena.Code('func_03_494')
def func_03_494():
    EventBegin(0x00)
    Fade(1000)
    OP_89(0x0000, -800, 20000, -62800, 0)
    OP_89(0x0001, 800, 20000, -62800, 0)
    OP_89(0x0002, 800, 20000, -61200, 0)
    OP_89(0x0003, -800, 20000, -61200, 0)
    CameraMove(0, -4000, -62000, 1500)
    Sleep(100)

    OP_B0(0x0000, 0x5A)
    SetMapFlags(0x00100000)
    PlaySE(235, 0x00, 0x64)
    OP_6F(0x0000, 1600)
    OP_70(0x0000, 1000)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4311._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x523
@scena.Code('func_04_523')
def func_04_523():
    EventBegin(0x00)
    OP_13(0x00E3)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xE3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0000, 1300)
    OP_70(0x0000, 1600)
    Yield()
    OP_89(0x0000, -800, 20000, -62800, 0)
    OP_89(0x0001, 800, 20000, -62800, 0)
    OP_89(0x0002, 800, 20000, -61200, 0)
    OP_89(0x0003, -800, 20000, -61200, 0)
    CameraMove(0, -4000, -62000, 0)
    OP_73(0x0000)
    Sleep(100)

    Fade(1000)
    SetChrPos(0x0000, 0, -4000, -58600, 0)
    SetChrPos(0x0001, 0, -4000, -58600, 0)
    SetChrPos(0x0002, 0, -4000, -58600, 0)
    SetChrPos(0x0003, 0, -4000, -58600, 0)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x5E9
@scena.Code('func_05_5E9')
def func_05_5E9():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '在此休息\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A5',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0007, 0x0020)
    OP_6F(0x0007, 300)
    OP_70(0x0007, 500)
    OP_73(0x0007)
    OP_6F(0x0007, 500)
    OP_70(0x0007, 700)
    OP_71(0x0007, 0x0020)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x06, 0x02)
    LoadEffect(0x05, 'map\\\\mp027_01.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 7300, 1200, 38800, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x06, 0x00)
    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x00, 0x00FF, 7300, 1200, 38800, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 250)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_7A5(): pass

    label('loc_7A5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7BF',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_7BF(): pass

    label('loc_7BF')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
