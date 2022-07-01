import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拉文努山道方向'),
    TXT(0x02, '拉文努废坑方向'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1200.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2F8
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
        ScenaNpcData(
            x                   = -2080,
            z                   = 0,
            y                   = -80,
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
        ScenaNpcData(
            x                   = 7170,
            z                   = 8000,
            y                   = 78890,
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

# id: 0x10003 offset: 0xE8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xE8
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 5000,
            y           = 0,
            z           = 34240,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 5150,
            y           = 4550,
            z           = 41780,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 5310,
            y           = 0,
            z           = 23020,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 6000,
            y           = 4400,
            z           = 54640,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10005 offset: 0x168
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 34960,
            triggerZ            = -3850,
            triggerY            = 8220,
            triggerRange        = 1000,
            actorX              = 35010,
            actorZ              = -4200,
            actorY              = 5190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x18C
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_19C',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0002)

    def _loc_19C(): pass

    label('loc_19C')

    Return()

# id: 0x0001 offset: 0x19D
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE5638, 0xFFFE98A0, 0x00230043)

    Return()

# id: 0x0002 offset: 0x1B0
@scena.Code('ReInit')
def ReInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006D, 'loc_1BC'),
        (-1, 'loc_1C8'),
    )

    def _loc_1BC(): pass

    label('loc_1BC')

    NewScene('ED6_DT21/T1201._SN', 109, 0, 0)
    IdleLoop()

    Jump('loc_1C8')

    def _loc_1C8(): pass

    label('loc_1C8')

    Return()

# id: 0x0003 offset: 0x1C9
@scena.Code('func_03_1C9')
def func_03_1C9():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0201')
    def lambda_0201():
        OP_6D(35190, -3850, 5430, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0201)

    @scena.Lambda('lambda_0219')
    def lambda_0219():
        OP_6B(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0219)

    @scena.Lambda('lambda_0229')
    def lambda_0229():
        OP_6C(225000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_0229)

    Sleep(1000)

    SetChrName('')

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
        'loc_2CE',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x101, 0x28),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    OP_C0(0x0E, 0x0000000A, 0x00008976, 0xFFFFF0F6, 0x000021D4, 0x000000B4, 0x000088C2, 0xFFFFEF98, 0x00001446)

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushReg, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()
    EventEnd(0x01)

    Jump('loc_2DD')

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DD',
    )

    EventEnd(0x01)

    def _loc_2DD(): pass

    label('loc_2DD')

    Return()

# id: 0x0004 offset: 0x2DE
@scena.Code('func_04_2DE')
def func_04_2DE():
    SetPlaceName(0x002E)

    Return()

# id: 0x0005 offset: 0x2E2
@scena.Code('func_05_2E2')
def func_05_2E2():
    SetPlaceName(0x002D)

    Return()

# id: 0x0006 offset: 0x2E6
@scena.Code('func_06_2E6')
def func_06_2E6():
    SetPlaceName(0x002F)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
