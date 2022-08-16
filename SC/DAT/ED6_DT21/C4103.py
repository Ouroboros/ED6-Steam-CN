import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4103   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4103.x'
    header.mapIndex       = 1
    header.bgm            = 21
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
            name                = '艾尔贝周游道方向',
            x                   = 267460,
            z                   = 0,
            y                   = -13160,
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
            triggerX            = 309300,
            triggerZ            = -70,
            triggerY            = 19380,
            triggerRange        = 1000,
            actorX              = 314040,
            actorZ              = -1000,
            actorY              = 19290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xEC
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xED
@scena.Code('func_01_ED')
def func_01_ED():
    OP_16(0x02, 4000, 180000, -123000, 2293862)
    PlaySE(460, 0x01, 0x64)
    PlaySE(455, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x10A
@scena.Code('func_02_10A')
def func_02_10A():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0142')
    def lambda_0142():
        CameraMove(312040, -50, 18590, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0142)

    @scena.Lambda('lambda_015A')
    def lambda_015A():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_015A)

    @scena.Lambda('lambda_0172')
    def lambda_0172():
        CameraSetDistance(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0172)

    @scena.Lambda('lambda_0182')
    def lambda_0182():
        OP_6C(315000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_0182)

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
        'loc_209',
    )

    OP_C0(0x0E, 0x00000028, 0x0004B834, 0xFFFFFFBA, 0x00004BB4, 0x0000005A, 0x0004CAB8, 0xFFFFFFBA, 0x00004B5A)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_218')

    def _loc_209(): pass

    label('loc_209')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_218',
    )

    EventEnd(0x01)

    def _loc_218(): pass

    label('loc_218')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
