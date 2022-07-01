import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5316_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5316   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5316.x'
    header.mapIndex       = 1
    header.bgm            = 64
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x70C
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
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_B9',
    )

    OP_A3(0x10F0)
    Event(0, 0x0003)

    Jump('loc_CE')

    def _loc_B9(): pass

    label('loc_B9')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CE',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0002)

    def _loc_CE(): pass

    label('loc_CE')

    Return()

# id: 0x0001 offset: 0xCF
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xD0
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E7',
    )

    Call(0, 0x0006)
    Call(0, 0x0007)

    def _loc_E7(): pass

    label('loc_E7')

    OP_6D(-90, 13760, -140, 0)
    OP_67(0, 7950, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 0, 1760, 1000, 0)
    SetChrPos(0x0102, 1000, 1760, 0, 90)
    SetChrPos(0x00F8, -1000, 1760, 0, 270)
    SetChrPos(0x00F9, 0, 1760, -1000, 180)
    OP_B0(0x0000, 0x8C)
    OP_6F(0x0000, 230)
    OP_70(0x0000, 0x0000001E)
    ClearMapFlags(0x00100000)
    OP_22(0x00EB, 0x01, 0x64)

    @scena.Lambda('lambda_018A')
    def lambda_018A():
        OP_6D(-90, 3000, -140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_018A)

    @scena.Lambda('lambda_01A2')
    def lambda_01A2():
        OP_67(0, 6470, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_01A2)

    @scena.Lambda('lambda_01BA')
    def lambda_01BA():
        OP_6B(3680, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_01BA)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(2000)

    @scena.Lambda('lambda_01DE')
    def lambda_01DE():
        OP_6D(-90, 2000, -140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_01DE)

    @scena.Lambda('lambda_01F6')
    def lambda_01F6():
        OP_67(0, 5000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_01F6)

    @scena.Lambda('lambda_020E')
    def lambda_020E():
        OP_6B(3900, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_020E)

    Sleep(2000)

    Sleep(2000)

    @scena.Lambda('lambda_0228')
    def lambda_0228():
        OP_6D(-90, -9740, -140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0228)

    @scena.Lambda('lambda_0240')
    def lambda_0240():
        OP_67(0, 2180, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0240)

    @scena.Lambda('lambda_0258')
    def lambda_0258():
        OP_6B(4320, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0258)

    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5313._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x27F
@scena.Code('func_03_27F')
def func_03_27F():
    EventBegin(0x00)
    OP_6D(0, 1760, 0, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 1000, 1760, 0, 90)
    SetChrPos(0x0001, 0, 1760, -1000, 180)
    SetChrPos(0x0002, 0, 1760, 1000, 0)
    SetChrPos(0x0003, -1000, 1760, 0, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 4, 0x228C)),
            Expr.Return,
        ),
        'loc_319',
    )

    Call(0, 0x0004)
    NewScene('ED6_DT21/C5301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 5, 0x228D)),
            Expr.Return,
        ),
        'loc_330',
    )

    Call(0, 0x0005)
    NewScene('ED6_DT21/C5300._SN', 119, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_330(): pass

    label('loc_330')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 6, 0x228E)),
            Expr.Return,
        ),
        'loc_347',
    )

    Call(0, 0x0004)
    NewScene('ED6_DT21/C5303._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0451, 7, 0x228F)),
            Expr.Return,
        ),
        'loc_35E',
    )

    Call(0, 0x0005)
    NewScene('ED6_DT21/C5302._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_35E(): pass

    label('loc_35E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 0, 0x2290)),
            Expr.Return,
        ),
        'loc_375',
    )

    Call(0, 0x0004)
    NewScene('ED6_DT21/C5304._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_375(): pass

    label('loc_375')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 1, 0x2291)),
            Expr.Return,
        ),
        'loc_38C',
    )

    Call(0, 0x0005)
    NewScene('ED6_DT21/C5303._SN', 114, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 2, 0x2292)),
            Expr.Return,
        ),
        'loc_3A3',
    )

    Call(0, 0x0004)
    NewScene('ED6_DT21/C5306._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_3A3(): pass

    label('loc_3A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 3, 0x2293)),
            Expr.Return,
        ),
        'loc_3BA',
    )

    Call(0, 0x0005)
    NewScene('ED6_DT21/C5305._SN', 114, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_3BA(): pass

    label('loc_3BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 4, 0x2294)),
            Expr.Return,
        ),
        'loc_3D1',
    )

    Call(0, 0x0004)
    NewScene('ED6_DT21/C5307._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3E5')

    def _loc_3D1(): pass

    label('loc_3D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0452, 5, 0x2295)),
            Expr.Return,
        ),
        'loc_3E5',
    )

    Call(0, 0x0005)
    NewScene('ED6_DT21/C5306._SN', 122, 0, 0)
    IdleLoop()

    def _loc_3E5(): pass

    label('loc_3E5')

    Return()

# id: 0x0004 offset: 0x3E6
@scena.Code('func_04_3E6')
def func_04_3E6():
    OP_B0(0x0000, 0x78)
    OP_6F(0x0000, 230)
    OP_70(0x0000, 0x0000001E)
    SetMapFlags(0x00100000)
    OP_22(0x00EB, 0x00, 0x64)
    OP_6D(-90, 13760, -140, 0)
    OP_67(0, 7950, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0445')
    def lambda_0445():
        OP_6D(-90, 2360, -140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0445)

    @scena.Lambda('lambda_045D')
    def lambda_045D():
        OP_67(0, 6470, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_045D)

    @scena.Lambda('lambda_0475')
    def lambda_0475():
        OP_6B(3680, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0475)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(2000)

    @scena.Lambda('lambda_0499')
    def lambda_0499():
        OP_6D(-90, -9740, -140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0499)

    @scena.Lambda('lambda_04B1')
    def lambda_04B1():
        OP_67(0, 2180, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04B1)

    @scena.Lambda('lambda_04C9')
    def lambda_04C9():
        OP_6B(4320, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_04C9)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()

    Return()

# id: 0x0005 offset: 0x4E4
@scena.Code('func_05_4E4')
def func_05_4E4():
    OP_B0(0x0000, 0x78)
    OP_6F(0x0000, 30)
    OP_70(0x0000, 0x000000E6)
    SetMapFlags(0x00100000)
    OP_22(0x00EB, 0x00, 0x64)
    OP_6D(-90, -9740, -140, 0)
    OP_67(0, 2180, -10000, 0)
    OP_6B(4320, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0543')
    def lambda_0543():
        OP_6D(-90, 2360, -140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0543)

    @scena.Lambda('lambda_055B')
    def lambda_055B():
        OP_67(0, 6470, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_055B)

    @scena.Lambda('lambda_0573')
    def lambda_0573():
        OP_6B(3680, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0573)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(2000)

    @scena.Lambda('lambda_0597')
    def lambda_0597():
        OP_6D(-90, 13760, -140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0597)

    @scena.Lambda('lambda_05AF')
    def lambda_05AF():
        OP_67(0, 7950, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05AF)

    @scena.Lambda('lambda_05C7')
    def lambda_05C7():
        OP_6B(3620, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05C7)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()

    Return()

# id: 0x0006 offset: 0x5E2
@scena.Code('func_06_5E2')
def func_06_5E2():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_65C'),
        (0x00000001, 'loc_662'),
        (-1, 'loc_668'),
    )

    def _loc_65C(): pass

    label('loc_65C')

    OP_A2(0x1200)

    Jump('loc_668')

    def _loc_662(): pass

    label('loc_662')

    OP_A2(0x1201)

    Jump('loc_668')

    def _loc_668(): pass

    label('loc_668')

    Return()

# id: 0x0007 offset: 0x669
@scena.Code('func_07_669')
def func_07_669():
    FadeOut(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
