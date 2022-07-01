import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3603_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3603   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3603.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xA9D
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
        ('ED6_DT29/CH12660._CH', 'ED6_DT29/CH12660P._CP'),
        ('ED6_DT29/CH12661._CH', 'ED6_DT29/CH12661P._CP'),
        ('ED6_DT29/CH12670._CH', 'ED6_DT29/CH12670P._CP'),
        ('ED6_DT29/CH12671._CH', 'ED6_DT29/CH12671P._CP'),
        ('ED6_DT29/CH12680._CH', 'ED6_DT29/CH12680P._CP'),
        ('ED6_DT29/CH12681._CH', 'ED6_DT29/CH12681P._CP'),
        ('ED6_DT29/CH12690._CH', 'ED6_DT29/CH12690P._CP'),
        ('ED6_DT29/CH12691._CH', 'ED6_DT29/CH12691P._CP'),
        ('ED6_DT29/CH12700._CH', 'ED6_DT29/CH12700P._CP'),
        ('ED6_DT29/CH12701._CH', 'ED6_DT29/CH12701P._CP'),
        ('ED6_DT29/CH12710._CH', 'ED6_DT29/CH12710P._CP'),
        ('ED6_DT29/CH12711._CH', 'ED6_DT29/CH12711P._CP'),
        ('ED6_DT29/CH12720._CH', 'ED6_DT29/CH12720P._CP'),
        ('ED6_DT29/CH12721._CH', 'ED6_DT29/CH12721P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 4780,
            z           = -3800,
            y           = -34920,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0411,
            word_18     = 0x1EC2,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6020,
            z           = -3600,
            y           = -34270,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0411,
            word_18     = 0x1EC3,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 28010,
            z           = 200,
            y           = -13660,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EC4,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 33740,
            z           = -50,
            y           = -20750,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0410,
            word_18     = 0x1EC5,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x18A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x18A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x18A
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1A2'),
        (0x00000065, 'loc_1A9'),
        (0x00000066, 'loc_1B0'),
        (0x00000067, 'loc_1B7'),
        (-1, 'loc_1BE'),
    )

    def _loc_1A2(): pass

    label('loc_1A2')

    Event(0, 0x0002)

    Jump('loc_1BE')

    def _loc_1A9(): pass

    label('loc_1A9')

    Event(0, 0x0004)

    Jump('loc_1BE')

    def _loc_1B0(): pass

    label('loc_1B0')

    Event(0, 0x0006)

    Jump('loc_1BE')

    def _loc_1B7(): pass

    label('loc_1B7')

    Event(0, 0x0008)

    Jump('loc_1BE')

    def _loc_1BE(): pass

    label('loc_1BE')

    Return()

# id: 0x0001 offset: 0x1BF
@scena.Code('Init')
def Init():
    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D8, 2, 0x1EC2)),
            Expr.Return,
        ),
        'loc_1F3',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_1F3(): pass

    label('loc_1F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D8, 3, 0x1EC3)),
            Expr.Return,
        ),
        'loc_1FF',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_1FF(): pass

    label('loc_1FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D8, 4, 0x1EC4)),
            Expr.Return,
        ),
        'loc_20B',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_20B(): pass

    label('loc_20B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D8, 5, 0x1EC5)),
            Expr.Return,
        ),
        'loc_217',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_217(): pass

    label('loc_217')

    OP_1B(0x00, 0x00, 0x0003)
    OP_1B(0x01, 0x00, 0x0005)
    OP_1B(0x02, 0x00, 0x0007)
    OP_1B(0x03, 0x00, 0x0009)

    Return()

# id: 0x0002 offset: 0x22C
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, -3810, -71500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, -500, -3810, -71000, 0)
    SetChrPos(0x0102, 500, -3810, -71000, 0)
    SetChrPos(0x00F8, -500, -3810, -72000, 0)
    SetChrPos(0x00F9, 500, -3810, -72000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x000A)
    Call(0, 0x000C)
    Fade(500)
    OP_6D(-100, -3810, -69250, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0000, -100, -3810, -69250, 0)
    SetChrPos(0x0001, -100, -3810, -69250, 0)
    SetChrPos(0x0002, -100, -3810, -69250, 0)
    SetChrPos(0x0003, -100, -3810, -69250, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0003 offset: 0x33E
@scena.Code('func_03_33E')
def func_03_33E():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(0, -3810, -71500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 500, -3810, -72000, 180)
    SetChrPos(0x0102, -500, -3810, -72000, 180)
    SetChrPos(0x00F8, 500, -3810, -71000, 180)
    SetChrPos(0x00F9, -500, -3810, -71000, 180)
    OP_0D()
    Call(0, 0x000A)
    Call(0, 0x000D)
    NewScene('ED6_DT21/C3602._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x3BF
@scena.Code('func_04_3BF')
def func_04_3BF():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(30800, 4240, 18500, 0)
    SetChrPos(0x0101, 31300, 4240, 18000, 180)
    SetChrPos(0x0102, 30300, 4240, 18000, 180)
    SetChrPos(0x00F8, 31300, 4240, 19000, 180)
    SetChrPos(0x00F9, 30300, 4240, 19000, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x000B)
    Call(0, 0x000C)
    Fade(500)
    OP_6D(30720, 4240, 16250, 0)
    SetChrPos(0x0000, 30720, 4240, 16250, 180)
    SetChrPos(0x0001, 30720, 4240, 16250, 180)
    SetChrPos(0x0002, 30720, 4240, 16250, 180)
    SetChrPos(0x0003, 30720, 4240, 16250, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0005 offset: 0x4BF
@scena.Code('func_05_4BF')
def func_05_4BF():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(30800, 4240, 18500, 0)
    SetChrPos(0x0101, 30300, 4240, 19000, 0)
    SetChrPos(0x0102, 31300, 4240, 19000, 0)
    SetChrPos(0x00F8, 30300, 4240, 18000, 0)
    SetChrPos(0x00F9, 31300, 4240, 18000, 0)
    OP_0D()
    Call(0, 0x000B)
    Call(0, 0x000D)
    NewScene('ED6_DT21/C3604._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x537
@scena.Code('func_06_537')
def func_06_537():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-30500, 190, -17000, 0)
    SetChrPos(0x0101, -30000, 190, -17500, 180)
    SetChrPos(0x0102, -31000, 190, -17500, 180)
    SetChrPos(0x00F8, -30000, 190, -16500, 180)
    SetChrPos(0x00F9, -31000, 190, -16500, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x000B)
    Call(0, 0x000C)
    Fade(500)
    OP_6D(-30690, 190, -19100, 0)
    SetChrPos(0x0000, -30690, 190, -19100, 180)
    SetChrPos(0x0001, -30690, 190, -19100, 180)
    SetChrPos(0x0002, -30690, 190, -19100, 180)
    SetChrPos(0x0003, -30690, 190, -19100, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0007 offset: 0x637
@scena.Code('func_07_637')
def func_07_637():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(-30500, 190, -17000, 0)
    SetChrPos(0x0101, -31000, 190, -16500, 0)
    SetChrPos(0x0102, -30000, 190, -16500, 0)
    SetChrPos(0x00F8, -31000, 190, -17500, 0)
    SetChrPos(0x00F9, -30000, 190, -17500, 0)
    OP_0D()
    Call(0, 0x000B)
    Call(0, 0x000D)
    NewScene('ED6_DT21/C3604._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x6AF
@scena.Code('func_08_6AF')
def func_08_6AF():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 190, 36000, 0)
    SetChrPos(0x0101, 500, 190, 35500, 180)
    SetChrPos(0x0102, -500, 190, 35500, 180)
    SetChrPos(0x00F8, 500, 190, 36500, 180)
    SetChrPos(0x00F9, -500, 190, 36500, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x000B)
    Call(0, 0x000C)
    Fade(500)
    OP_6D(100, 190, 34170, 0)
    SetChrPos(0x0000, 100, 190, 34170, 180)
    SetChrPos(0x0001, 100, 190, 34170, 180)
    SetChrPos(0x0002, 100, 190, 34170, 180)
    SetChrPos(0x0003, 100, 190, 34170, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0009 offset: 0x7AF
@scena.Code('func_09_7AF')
def func_09_7AF():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(0, 190, 36000, 0)
    SetChrPos(0x0101, -500, 190, 36500, 0)
    SetChrPos(0x0102, 500, 190, 36500, 0)
    SetChrPos(0x00F8, -500, 190, 35500, 0)
    SetChrPos(0x00F9, 500, 190, 35500, 0)
    OP_0D()
    Call(0, 0x000B)
    Call(0, 0x000D)
    NewScene('ED6_DT21/C3604._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x827
@scena.Code('func_0A_827')
def func_0A_827():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x000B offset: 0x906
@scena.Code('func_0B_906')
def func_0B_906():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x000C offset: 0x9E5
@scena.Code('func_0C_9E5')
def func_0C_9E5():
    @scena.Lambda('lambda_09EB')
    def lambda_09EB():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_09EB)

    @scena.Lambda('lambda_09FD')
    def lambda_09FD():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_09FD)

    @scena.Lambda('lambda_0A0F')
    def lambda_0A0F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0A0F)

    @scena.Lambda('lambda_0A21')
    def lambda_0A21():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0A21)

    Sleep(2500)

    Return()

# id: 0x000D offset: 0xA33
@scena.Code('func_0D_A33')
def func_0D_A33():
    @scena.Lambda('lambda_0A39')
    def lambda_0A39():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0A39)

    @scena.Lambda('lambda_0A4B')
    def lambda_0A4B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0A4B)

    @scena.Lambda('lambda_0A5D')
    def lambda_0A5D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0A5D)

    @scena.Lambda('lambda_0A6F')
    def lambda_0A6F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0A6F)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
