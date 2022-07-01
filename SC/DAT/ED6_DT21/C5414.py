import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5414_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5414   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'Loewe'),
    TXT(0x02, '結社挺'),
    TXT(0x03, '結社挺'),
    TXT(0x04, '結社挺'),
    TXT(0x05, '結社挺'),
    TXT(0x06, '結社挺'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'other'
    header.mapModel       = 'C5414.x'
    header.mapIndex       = 1
    header.bgm            = 28
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x86D
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
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x172
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x172
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x172
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x172
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_183',
    )

    OP_A3(0x10F0)
    Event(0, 0x0002)

    Jump('loc_19A')

    def _loc_183(): pass

    label('loc_183')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_19A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x72),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F1)
    Event(0, 0x0003)

    def _loc_19A(): pass

    label('loc_19A')

    Return()

# id: 0x0001 offset: 0x19B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B9',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B9(): pass

    label('loc_1B9')

    OP_22(0x01C3, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x1BF
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_6D(4910, -1800, 22110, 0)
    OP_67(0, 4400, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(225000, 0)
    OP_6E(305, 0)
    SetChrPos(0x0101, 5990, -1800, 23310, 90)
    OP_22(0x0131, 0x01, 0x46)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_022F')
    def lambda_022F():
        OP_6D(4910, -1800, 22110, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_022F)

    @scena.Lambda('lambda_0247')
    def lambda_0247():
        OP_67(0, 3270, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0247)

    @scena.Lambda('lambda_025F')
    def lambda_025F():
        OP_6B(4420, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_025F)

    @scena.Lambda('lambda_026F')
    def lambda_026F():
        OP_6C(213000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_026F)

    @scena.Lambda('lambda_027F')
    def lambda_027F():
        OP_6E(1434, 12000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_027F)

    Sleep(10000)

    FadeOut(2000, 0, -1)
    OP_24(0x0131, 0x46)
    Sleep(300)

    OP_24(0x0131, 0x3C)
    Sleep(300)

    OP_24(0x0131, 0x32)
    Sleep(300)

    OP_24(0x0131, 0x28)
    Sleep(300)

    OP_24(0x0131, 0x1E)
    Sleep(300)

    OP_24(0x0131, 0x14)
    Sleep(300)

    OP_23(0x0131)
    OP_0D()
    OP_26(451)
    OP_26(305)
    OP_26(876)
    OP_26(877)
    OP_26(878)
    OP_C4(0x00, 0x00000010)
    Yield()
    FadeIn(1, 0)
    PlayMovie(0x00, 'ED6_DT40.dat', 0x0000, 0x0001)
    def _loc_304(): pass

    label('loc_304')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_31E',
    )

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_31B',
    )

    Jump('loc_31E')

    def _loc_31B(): pass

    label('loc_31B')

    Jump('loc_304')

    def _loc_31E(): pass

    label('loc_31E')

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    Sleep(2000)

    OP_C4(0x01, 0x00000010)
    OP_DC()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x349
@scena.Code('func_03_349')
def func_03_349():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_11(0xFF, 0xFF, 0xFF, 0x0000F424, 0x000493E0, 0x00000000)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 5990, -1800, 24620, 90)
    SetChrPos(0x0101, 5990, -1800, 23310, 90)
    OP_6D(5990, -1800, 23310, 0)
    OP_67(0, 3220, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(251000, 0)
    OP_6E(1188, 0)
    OP_22(0x0131, 0x01, 0x46)
    OP_A1(0x0009, 0x0002)
    OP_A1(0x000A, 0x0003)
    OP_A1(0x000B, 0x0004)
    OP_A1(0x000C, 0x0005)
    OP_A1(0x000D, 0x0006)
    OP_71(0x0002, 0x0002)
    OP_71(0x0002, 0x0020)
    OP_72(0x0002, 0x0004)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 0x00000384)
    OP_71(0x0003, 0x0002)
    OP_71(0x0003, 0x0020)
    OP_72(0x0003, 0x0004)
    OP_6F(0x0003, 800)
    OP_70(0x0003, 0x00000384)
    OP_71(0x0004, 0x0002)
    OP_71(0x0004, 0x0020)
    OP_72(0x0004, 0x0004)
    OP_6F(0x0004, 800)
    OP_70(0x0004, 0x00000384)
    OP_71(0x0005, 0x0002)
    OP_71(0x0005, 0x0020)
    OP_72(0x0005, 0x0004)
    OP_6F(0x0005, 800)
    OP_70(0x0005, 0x00000384)
    OP_71(0x0006, 0x0002)
    OP_71(0x0006, 0x0020)
    OP_72(0x0006, 0x0004)
    OP_6F(0x0006, 800)
    OP_70(0x0006, 0x00000384)
    SetChrPos(0x0009, 26000, 3000, 280000, 0)
    SetChrPos(0x000A, 48000, 2000, 280000, 0)
    SetChrPos(0x000B, 68000, 4000, 280000, 0)
    SetChrPos(0x000C, 88000, 2000, 280000, 0)
    SetChrPos(0x000D, 108000, 4000, 280000, 0)
    OP_D1(9, 0, 180000, 0, 0)
    OP_D1(10, 0, 180000, 0, 0)
    OP_D1(11, 0, 180000, 0, 0)
    OP_D1(12, 0, 180000, 0, 0)
    OP_D1(13, 0, 180000, 0, 0)
    FadeOut(0, 0, -1)
    CreateThread(0x0009, 0x00, 0x00, 0x0004)
    CreateThread(0x000A, 0x00, 0x00, 0x0005)
    CreateThread(0x000B, 0x00, 0x00, 0x0006)
    CreateThread(0x000C, 0x00, 0x00, 0x0007)
    CreateThread(0x000D, 0x00, 0x00, 0x0008)
    Sleep(2000)

    OP_22(0x0079, 0x01, 0x3C)
    Sleep(1000)

    OP_22(0x0079, 0x01, 0x46)
    Sleep(1000)

    FadeIn(2000, 0)
    OP_22(0x0079, 0x01, 0x50)
    Sleep(1000)

    OP_22(0x0079, 0x01, 0x5A)
    Sleep(1000)

    @scena.Lambda('lambda_0596')
    def lambda_0596():
        OP_6D(59460, -1800, 5100, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0596)

    @scena.Lambda('lambda_05AE')
    def lambda_05AE():
        OP_6C(228000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_05AE)

    WaitForThreadExit(0x0000, 0x0000)
    Sleep(4000)

    FadeOut(2000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F3)
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x5E0
@scena.Code('func_04_5E0')
def func_04_5E0():
    @scena.Lambda('lambda_05E6')
    def lambda_05E6():
        OP_D1(254, 0, 180000, 25000, 8000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_05E6)

    OP_8F(0x00FE, 26000, 3000, -20000, 40000, 0x00)
    OP_8F(0x00FE, 60000, 6000, -300000, 40000, 0x00)

    Return()

# id: 0x0005 offset: 0x623
@scena.Code('func_05_623')
def func_05_623():
    Sleep(1000)

    @scena.Lambda('lambda_062E')
    def lambda_062E():
        OP_D1(254, 0, 175000, 30000, 8000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_062E)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, 0x00007530, 0x00000BB8, 0xFFFFB1E0)
    OP_98(0x01, 0x00015F90, 0xFFFFF060, 0xFFFB6C20)

    @scena.Lambda('lambda_0668')
    def lambda_0668():
        OP_98(0x02, 0x00FE, 0x00009C40, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0668)

    Sleep(2000)

    @scena.Lambda('lambda_067D')
    def lambda_067D():
        OP_D1(254, 0, 175000, 30000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_067D)

    WaitForThreadExit(0x00FE, 0x0003)

    @scena.Lambda('lambda_069C')
    def lambda_069C():
        OP_D1(254, 0, 175000, 15000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_069C)

    Return()

# id: 0x0006 offset: 0x6B1
@scena.Code('func_06_6B1')
def func_06_6B1():
    Sleep(2000)

    @scena.Lambda('lambda_06BC')
    def lambda_06BC():
        OP_D1(254, 0, 180000, 35000, 8000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_06BC)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, 0x00007530, 0x000003E8, 0xFFFFB1E0)
    OP_98(0x01, 0x0001D4C0, 0xFFFFC950, 0xFFFB6C20)

    @scena.Lambda('lambda_06F6')
    def lambda_06F6():
        OP_98(0x02, 0x00FE, 0x00009C40, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_06F6)

    Sleep(2000)

    @scena.Lambda('lambda_070B')
    def lambda_070B():
        OP_D1(254, 0, 170000, 35000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_070B)

    WaitForThreadExit(0x00FE, 0x0003)

    @scena.Lambda('lambda_072A')
    def lambda_072A():
        OP_D1(254, 0, 170000, 15000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_072A)

    Return()

# id: 0x0007 offset: 0x73F
@scena.Code('func_07_73F')
def func_07_73F():
    Sleep(3000)

    @scena.Lambda('lambda_074A')
    def lambda_074A():
        OP_D1(254, 0, 180000, 40000, 8000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_074A)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, 0x00007530, 0xFFFFFC18, 0xFFFFB1E0)
    OP_98(0x01, 0x000249F0, 0xFFFFA240, 0xFFFB6C20)

    @scena.Lambda('lambda_0784')
    def lambda_0784():
        OP_98(0x02, 0x00FE, 0x00009C40, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0784)

    Sleep(2000)

    @scena.Lambda('lambda_0799')
    def lambda_0799():
        OP_D1(254, 0, 165000, 40000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0799)

    WaitForThreadExit(0x00FE, 0x0003)

    @scena.Lambda('lambda_07B8')
    def lambda_07B8():
        OP_D1(254, 0, 165000, 15000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_07B8)

    Return()

# id: 0x0008 offset: 0x7CD
@scena.Code('func_08_7CD')
def func_08_7CD():
    Sleep(4000)

    @scena.Lambda('lambda_07D8')
    def lambda_07D8():
        OP_D1(254, 0, 180000, 45000, 8000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_07D8)

    OP_98(0x00, 0x00FE)
    OP_98(0x01, 0x00007530, 0xFFFFF448, 0xFFFFB1E0)
    OP_98(0x01, 0x0002BF20, 0xFFFF7B30, 0xFFFB6C20)

    @scena.Lambda('lambda_0812')
    def lambda_0812():
        OP_98(0x02, 0x00FE, 0x00009C40, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0812)

    Sleep(2000)

    @scena.Lambda('lambda_0827')
    def lambda_0827():
        OP_D1(254, 0, 160000, 45000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0827)

    WaitForThreadExit(0x00FE, 0x0003)

    @scena.Lambda('lambda_0846')
    def lambda_0846():
        OP_D1(254, 0, 160000, 15000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0846)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
