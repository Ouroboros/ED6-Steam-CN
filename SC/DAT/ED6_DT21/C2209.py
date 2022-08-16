import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2209_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2209   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2209.x'
    header.mapIndex       = 84
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/C2209._SN', 'ED6_DT21/C2209_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ScenaNpcData(
            name                = '玛诺利亚间道方向',
            x                   = 1330,
            z                   = -430,
            y                   = -46450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0xC8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xC8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xC8
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -960,
            triggerZ            = 25000,
            triggerY            = -770,
            triggerRange        = 800,
            actorX              = -960,
            actorZ              = 26500,
            actorY              = -770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 15480,
            triggerZ            = 20,
            triggerY            = -7900,
            triggerRange        = 1000,
            actorX              = 23640,
            actorZ              = -10010,
            actorY              = -9260,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x110
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_123',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(1, 0x0000)

    def _loc_123(): pass

    label('loc_123')

    Return()

# id: 0x0001 offset: 0x124
@scena.Code('func_01_124')
def func_01_124():
    OP_16(0x02, 4000, -128000, -140000, 2293840)
    OP_B0(0x0000, 0x78)
    OP_B0(0x0001, 0x78)
    OP_1C(0x00, 0x00, 0x0002)
    OP_1C(0x01, 0x00, 0x0003)
    PlaySE(453, 0x01, 0x64)
    OP_E8(0xB8, 0x0B, 0x00, 0x00)

    Return()

# id: 0x0002 offset: 0x153
@scena.Code('func_02_153')
def func_02_153():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x15A
@scena.Code('func_03_15A')
def func_03_15A():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x161
@scena.Code('func_04_161')
def func_04_161():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　危险！　　　\n',
            '※非工作人员禁止进入',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0005 offset: 0x1BB
@scena.Code('func_05_1BB')
def func_05_1BB():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_01F3')
    def lambda_01F3():
        CameraMove(20710, 20, -9100, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_01F3)

    @scena.Lambda('lambda_020B')
    def lambda_020B():
        CameraMove(17710, 20, -13100, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_020B)

    @scena.Lambda('lambda_0223')
    def lambda_0223():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0223)

    @scena.Lambda('lambda_023B')
    def lambda_023B():
        CameraSetDistance(3250, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_023B)

    @scena.Lambda('lambda_024B')
    def lambda_024B():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_024B)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
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
            TXT(0x00, '钓鱼\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D2',
    )

    OP_C0(0x0E, 0x00000014, 0x00003C3C, 0x0000000A, 0xFFFFE0B6, 0x0000005A, 0x00005F78, 0xFFFFCE00, 0xFFFFE0C0)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_2E1')

    def _loc_2D2(): pass

    label('loc_2D2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E1',
    )

    EventEnd(0x01)

    def _loc_2E1(): pass

    label('loc_2E1')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
