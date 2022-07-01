import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T5200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T5200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔丝特'),
    TXT(0x02, '吉尔'),
    TXT(0x03, '多伦'),
    TXT(0x04, '照相机控制用'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'T5200.x'
    header.mapIndex       = 1
    header.bgm            = 117
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x75E
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
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT27/CH03770._CH', 'ED6_DT27/CH03770P._CP'),
        ('ED6_DT27/CH03760._CH', 'ED6_DT27/CH03760P._CP'),
    ]

# id: 0x10002 offset: 0xC2
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01CC,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x142
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x142
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x142
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x142
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_153',
    )

    OP_A3(0x10F0)
    Event(0, 0x0005)

    Jump('loc_160')

    def _loc_153(): pass

    label('loc_153')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x72),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0002)

    def _loc_160(): pass

    label('loc_160')

    Return()

# id: 0x0001 offset: 0x161
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x162
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    ClearMapFlags(0x02000000)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x010A, 0x0080)
    OP_22(0x01C3, 0x00, 0x64)
    OP_6D(2080, 0, -12200, 0)
    OP_67(0, 12390, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0008, 7740, 3130, 48960, 90)
    SetChrPos(0x0009, 2670, 0, 21830, 0)
    SetChrPos(0x000A, -8320, 0, 15250, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_0208')
    def lambda_0208():
        OP_6D(-2040, 0, 18280, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0208)

    @scena.Lambda('lambda_0220')
    def lambda_0220():
        OP_6B(6500, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0220)

    Sleep(500)

    FadeIn(2000, 0)
    Sleep(2000)

    CreateThread(0x010A, 0x01, 0x00, 0x0003)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Fade(500)
    OP_6D(5010, 0, 25180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3440, 0)
    OP_0D()
    Sleep(500)

    OP_8C(0x0009, 90, 400)
    Sleep(500)

    OP_8C(0x0009, 0, 400)
    Sleep(1000)

    OP_8C(0x0009, 270, 400)

    @scena.Lambda('lambda_02A9')
    def lambda_02A9():
        OP_8E(0x00FE, -2540, 0, 18810, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_02A9)

    Sleep(1000)

    Fade(500)
    OP_6D(-13540, 10, 15940, 0)
    OP_6C(315000, 0)
    OP_0D()
    Sleep(500)

    OP_8C(0x000A, 225, 400)
    Sleep(500)

    OP_8C(0x000A, 315, 400)
    Sleep(1000)

    OP_8C(0x000A, 90, 400)
    SetChrPos(0x0009, -2500, 0, 17010, 254)

    @scena.Lambda('lambda_031E')
    def lambda_031E():
        OP_8E(0x00FE, -4380, 0, 16610, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_031E)

    @scena.Lambda('lambda_0339')
    def lambda_0339():
        OP_6D(-3510, 0, 16860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0339)

    @scena.Lambda('lambda_0351')
    def lambda_0351():
        OP_6B(4440, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0351)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    @scena.Lambda('lambda_0370')
    def lambda_0370():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0370)

    Sleep(500)

    @scena.Lambda('lambda_0383')
    def lambda_0383():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0383)

    Sleep(500)

    @scena.Lambda('lambda_0396')
    def lambda_0396():
        OP_8E(0x00FE, -4540, 1000, 35510, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0396)

    Sleep(400)

    @scena.Lambda('lambda_03B6')
    def lambda_03B6():
        OP_8E(0x00FE, -6050, 1000, 35660, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_03B6)

    Sleep(1000)

    Fade(500)
    OP_6D(-2940, 2000, 57100, 0)
    OP_6B(5240, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0407')
    def lambda_0407():
        OP_6D(11400, 2000, 42760, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0407)

    CreateThread(0x0008, 0x00, 0x00, 0x0004)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    SetChrPos(0x0009, -2540, 1000, 40650, 90)
    SetChrPos(0x000A, -3500, 1000, 42410, 90)

    @scena.Lambda('lambda_0450')
    def lambda_0450():
        OP_8E(0x00FE, 11250, 2000, 41650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0450)

    Sleep(500)

    @scena.Lambda('lambda_0470')
    def lambda_0470():
        OP_8E(0x00FE, 10480, 2000, 43410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0470)

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_0495')
    def lambda_0495():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0495)

    WaitForThreadExit(0x000A, 0x0000)

    @scena.Lambda('lambda_04A8')
    def lambda_04A8():
        OP_8C(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_04A8)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0008, 90, 400)

    @scena.Lambda('lambda_04E3')
    def lambda_04E3():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_04E3)

    Sleep(150)

    @scena.Lambda('lambda_04F6')
    def lambda_04F6():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_04F6)

    Sleep(1500)

    @scena.Lambda('lambda_0509')
    def lambda_0509():
        OP_6D(51590, -1000, 43830, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0509)

    @scena.Lambda('lambda_0521')
    def lambda_0521():
        OP_67(0, 10550, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0521)

    @scena.Lambda('lambda_0539')
    def lambda_0539():
        OP_8E(0x00FE, 22000, 1900, 42830, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0539)

    Sleep(400)

    @scena.Lambda('lambda_0559')
    def lambda_0559():
        OP_8E(0x00FE, 22000, 2000, 41670, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0559)

    Sleep(400)

    @scena.Lambda('lambda_0579')
    def lambda_0579():
        OP_8E(0x00FE, 22000, 2000, 43420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0579)

    Sleep(3200)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T5201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x5B1
@scena.Code('func_03_5B1')
def func_03_5B1():
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#50A同一时刻。\n',
            '埃雷波尼亚帝国，最南部──',
            TxtCtl.Enter,
        ),
    )

    Sleep(3000)

    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#50A距和利贝尔的国境\n',
            '１２０塞尔矩的地点──',
            TxtCtl.Enter,
        ),
    )

    Sleep(3000)

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    Return()

# id: 0x0004 offset: 0x630
@scena.Code('func_04_630')
def func_04_630():
    OP_8E(0x0008, 10770, 2000, 48960, 2000, 0x00)
    OP_8E(0x0008, 12770, 2000, 46350, 2000, 0x00)
    OP_8E(0x0008, 12770, 2000, 42880, 2000, 0x00)
    OP_8C(0x0008, 270, 400)

    Return()

# id: 0x0005 offset: 0x674
@scena.Code('func_05_674')
def func_05_674():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(1050, 50, 6880, 0)
    OP_67(0, 10400, -10000, 0)
    OP_6B(5830, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x01C2, 0x00, 0x64)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_06E6')
    def lambda_06E6():
        OP_6D(-2970, 870, 30980, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_06E6)

    @scena.Lambda('lambda_06FE')
    def lambda_06FE():
        OP_67(0, 15430, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_06FE)

    OP_C8(0x0200, 0x0046, 'C_PLAC28._CH', 0x01, 0x07D0)
    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T5201._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
