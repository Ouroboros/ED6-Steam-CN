import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0400.x'
    header.mapIndex       = 13
    header.bgm            = 15
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
            dword_00        = 0x00005E24,
            dword_04        = 0x00000000,
            dword_08        = 0x0000DAC0,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 13,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00005E24,
            dword_04        = 0x00000000,
            dword_08        = 0x0000DAC0,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 13,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01710._CH', 'ED6_DT07/CH01710P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
    ]

# id: 0x10001 offset: 0x126
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '缇欧',
            x                   = 40470,
            z                   = 0,
            y                   = 16320,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '维鲁',
            x                   = 21900,
            z                   = 0,
            y                   = 25300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '查儿',
            x                   = 25100,
            z                   = 0,
            y                   = 23000,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '弗兰兹',
            x                   = 28100,
            z                   = 0,
            y                   = 24800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '汉娜',
            x                   = 32800,
            z                   = 200,
            y                   = 40000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '牛',
            x                   = 39010,
            z                   = 600,
            y                   = 22850,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '牛',
            x                   = 48160,
            z                   = 460,
            y                   = 18800,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 0,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 38780,
            z                   = 0,
            y                   = 19310,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 51470,
            z                   = 0,
            y                   = 20950,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 51470,
            z                   = 0,
            y                   = 20950,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '米尔西街道方向',
            x                   = 23910,
            z                   = 30,
            y                   = 66820,
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

# id: 0x10002 offset: 0x2C6
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2C6
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2C6
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2C6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_314',
    )

    ChrSetPos(0x000B, 38770, -300, 38410, 90)
    ChrSetPos(0x0008, 29400, 0, 12700, 180)
    ChrSetPos(0x000C, 29740, -300, 39260, 90)
    ChrSetPos(0x000A, 36000, 0, 41000, 0)

    Jump('loc_390')

    def _loc_314(): pass

    label('loc_314')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_354',
    )

    ChrSetPos(0x000B, 35500, 100, 36000, 90)
    ChrSetPos(0x0008, 29400, 0, 12700, 180)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    Jump('loc_390')

    def _loc_354(): pass

    label('loc_354')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_37C',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    Jump('loc_390')

    def _loc_37C(): pass

    label('loc_37C')

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    def _loc_390(): pass

    label('loc_390')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_3A0'),
        (0x00000001, 'loc_3F2'),
        (-1, 'loc_431'),
    )

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 5, 0x22D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EF',
    )

    SetScenaFlags(ScenaFlag(0x0045, 5, 0x22D))
    MapSetFlags(0x00400000)
    CameraMove(24000, 0, 51000, 0)
    OP_6C(36000, 0)
    CameraSetDistance(3000, 0)
    ChrSetPos(0x0102, 23000, 0, 55000, 0)
    ChrSetDirection(0x0102, 180, 0)
    Event(0, func_10_1F13)

    def _loc_3EF(): pass

    label('loc_3EF')

    Jump('loc_431')

    def _loc_3F2(): pass

    label('loc_3F2')

    MapClearFlags(0x00000001)
    CameraMove(17500, 0, 22800, 0)
    ChrSetPos(0x0102, 17000, 600, 23600, 90)
    ChrSetPos(0x0101, 17500, 600, 22800, 90)
    Event(0, func_12_2165)

    Jump('loc_431')

    def _loc_431(): pass

    label('loc_431')

    Return()

# id: 0x0001 offset: 0x432
@scena.Code('func_01_432')
def func_01_432():
    OP_16(0x02, 4000, -96000, -96000, 196612)

    Return()

# id: 0x0002 offset: 0x445
@scena.Code('func_02_445')
def func_02_445():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_45A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_445')

    def _loc_45A(): pass

    label('loc_45A')

    Return()

# id: 0x0003 offset: 0x45B
@scena.Code('func_03_45B')
def func_03_45B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_47E',
    )

    OP_8D(0x00FE, 19800, 21600, 24000, 30300, 3000)

    Jump('func_03_45B')

    def _loc_47E(): pass

    label('loc_47E')

    Return()

# id: 0x0004 offset: 0x47F
@scena.Code('func_04_47F')
def func_04_47F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_4BF',
    )

    def _loc_486(): pass

    label('loc_486')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4BC',
    )

    OP_92(0x00FE, 0x000C, 1000, 3000, 0x00)
    Sleep(1000)

    OP_8D(0x00FE, 36200, 39800, 32400, 43600, 3000)

    Jump('loc_486')

    def _loc_4BC(): pass

    label('loc_4BC')

    Jump('loc_4E2')

    def _loc_4BF(): pass

    label('loc_4BF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4E2',
    )

    OP_8D(0x00FE, 19800, 21600, 28200, 24800, 3000)

    Jump('loc_4BF')

    def _loc_4E2(): pass

    label('loc_4E2')

    Return()

# id: 0x0005 offset: 0x4E3
@scena.Code('func_05_4E3')
def func_05_4E3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_506',
    )

    OP_8D(0x00FE, 28150, 34670, 34240, 44760, 3000)

    Jump('func_05_4E3')

    def _loc_506(): pass

    label('loc_506')

    Return()

# id: 0x0006 offset: 0x507
@scena.Code('func_06_507')
def func_06_507():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_527',
    )

    def _loc_50F(): pass

    label('loc_50F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_524',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_50F')

    def _loc_524(): pass

    label('loc_524')

    Jump('loc_54A')

    def _loc_527(): pass

    label('loc_527')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_54A',
    )

    OP_8D(0x00FE, 37390, 35010, 40920, 43630, 3000)

    Jump('loc_527')

    def _loc_54A(): pass

    label('loc_54A')

    Return()

# id: 0x0007 offset: 0x54B
@scena.Code('func_07_54B')
def func_07_54B():
    ChrSetFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, 28710, 33610, 41830, 44000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_697',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_65C',
    )

    If(
        (
            (Expr.PushLong, 0x7026),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Lss,
            (Expr.PushLong, 0x834A),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushLong, 0xA366),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.PushLong, 0xABE0),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_631',
    )

    ChrSetFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ChrClearFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_061E')
    def lambda_061E():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_061E)

    Jump('loc_654')

    def _loc_631(): pass

    label('loc_631')

    @scena.Lambda('lambda_0637')
    def lambda_0637():
        OP_8D(0x00FE, 28710, 33610, 41830, 44000, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0637)

    Sleep(200)

    def _loc_654(): pass

    label('loc_654')

    Sleep(30)

    Jump('loc_694')

    def _loc_65C(): pass

    label('loc_65C')

    Sleep(50)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x28),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_694',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_067C')
    def lambda_067C():
        OP_8D(0x00FE, 28710, 33610, 41830, 44000, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_067C)

    def _loc_694(): pass

    label('loc_694')

    Jump('loc_574')

    def _loc_697(): pass

    label('loc_697')

    Return()

# id: 0x0008 offset: 0x698
@scena.Code('func_08_698')
def func_08_698():
    PlaySE(400, 0x00, 0x64)

    Return()

# id: 0x0009 offset: 0x69E
@scena.Code('func_09_69E')
def func_09_69E():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_728',
    )

    CreateThread(0x00FE, 0x02, 0x00, func_0A_729)
    PlaySE(401, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_728',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x038B, 1)"),
            Expr.Return,
        ),
        'loc_728',
    )

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '新鲜鸡蛋',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FE)

    def _loc_728(): pass

    label('loc_728')

    Return()

# id: 0x000A offset: 0x729
@scena.Code('func_0A_729')
def func_0A_729():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_744',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_0A_729')

    def _loc_744(): pass

    label('loc_744')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000B offset: 0x74F
@scena.Code('func_0B_74F')
def func_0B_74F():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_923',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0056, 7, 0x2B7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C4',
    )

    SetScenaFlags(ScenaFlag(0x0056, 7, 0x2B7))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '这不是艾丝蒂尔和约修亚嘛。\n',
            '你们为什么会背着旅行包啊？ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯～是这样的，\n',
            '我们要去柏斯那里办些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯吗……\n',
            '我听说定期船已经停航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说你们\n',
            '打算走路过去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F没事没事。\n',
            '我听说走路去柏斯又不是很远。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，就算有事非去不可，\n',
            '这段路对于游击士来说也不轻松呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们路上要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_920')

    def _loc_8C4(): pass

    label('loc_8C4')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '唔，就算有事非去不可，\n',
            '这段路对于游击士来说也不轻松呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们路上要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_920(): pass

    label('loc_920')

    Jump('loc_FC8')

    def _loc_923(): pass

    label('loc_923')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_A36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9C8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哎，是你们俩啊。\n',
            '最近怎么样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，我想找天搞个聚会，\n',
            '把以前在主日学校读书的同学都叫到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也好久没有见过伊莉莎她了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A33')

    def _loc_9C8(): pass

    label('loc_9C8')

    ChrTalk(
        0x00FE,
        (
            '对了，我想找天搞个聚会，\n',
            '把以前在主日学校读书的同学都叫到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也好久没有见过伊莉莎她了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A33(): pass

    label('loc_A33')

    Jump('loc_FC8')

    def _loc_A36(): pass

    label('loc_A36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_B35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B00',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔、约修亚，\n',
            '之前真是多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那之后我家\n',
            '可是安静了很多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以恢复供应蔬菜，\n',
            '大家又再度忙碌起来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '查儿和维鲁\n',
            '大概还不能这么早\n',
            '帮家里干活吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B32')

    def _loc_B00(): pass

    label('loc_B00')

    ChrTalk(
        0x00FE,
        (
            '查儿和维鲁\n',
            '大概还不能这么早\n',
            '帮家里干活吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B32(): pass

    label('loc_B32')

    Jump('loc_FC8')

    def _loc_B35(): pass

    label('loc_B35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_C19',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BC6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔、约修亚，\n',
            '真是谢谢你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次完成工作之后\n',
            '记得一定来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '查儿和维鲁\n',
            '一直吵着要你们\n',
            '下次再来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C16')

    def _loc_BC6(): pass

    label('loc_BC6')

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔、约修亚，\n',
            '真是谢谢你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次完成工作之后\n',
            '记得一定来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C16(): pass

    label('loc_C16')

    Jump('loc_FC8')

    def _loc_C19(): pass

    label('loc_C19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 6, 0x22E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F8F',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0045, 6, 0x22E))
    OP_28(0x0002, 0x01, 0x0004)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0013,
        0x01,
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x02,
        (
            (Expr.GetChrWork, 0xFE, 0x2),
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x03,
        (
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0013, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010001353V#001F呀嗬～缇欧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001354V#010F嗨，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0890001355V艾丝蒂尔？\n',
            '还有约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0890001356V你们是来找我玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001357V#000F不是啦，我们是来执行任务的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001358V#000F这里不是有魔兽出现吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '两人向缇欧说明了\n',
            '代替卡西乌斯执行任务的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#0890001359V研修结束了啊……\n',
            '恭喜你们了，真不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0890001360V嗯，如果是你们的话，\n',
            '说不定有办法对付它们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001361V#004F真的有魔兽出现吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0890001362V嗯，这几天一直在捣乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0890001363V拜它们所赐，\n',
            '害得我睡眠不足……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001364V#010F也就是说……\n',
            '那些魔兽是在夜晚出没的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0890001365V说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0890001366V对了，\n',
            '你们还是去向我爸妈询问详细的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0890001367V他们刚才出去送货，\n',
            '我想这个时候应该已经回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_FC8')

    def _loc_F8F(): pass

    label('loc_F8F')

    ChrTalk(
        0x00FE,
        (
            '我爸妈他们\n',
            '刚才出去送货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想差不多该回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FC8(): pass

    label('loc_FC8')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

# id: 0x000C offset: 0xFCE
@scena.Code('func_0C_FCE')
def func_0C_FCE():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1094',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_104D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '连查儿姐姐也\n',
            '开始帮农场干活了，\n',
            '我自己一个人玩也觉得有点闷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也想帮忙呢……\n',
            '帮农场干活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1091')

    def _loc_104D(): pass

    label('loc_104D')

    ChrTalk(
        0x00FE,
        (
            '连查儿姐姐也\n',
            '开始帮农场干活了，\n',
            '我自己一个人玩也觉得有点闷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1091(): pass

    label('loc_1091')

    Jump('loc_14B1')

    def _loc_1094(): pass

    label('loc_1094')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1167',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1121',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '啊，约修亚和艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说，你们已经成为\n',
            '守护正义的游击士了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '厉害啊，好酷哦……\n',
            '我也可以做游击士吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1164')

    def _loc_1121(): pass

    label('loc_1121')

    ChrTalk(
        0x00FE,
        (
            '你们已经成为\n',
            '守护正义的游击士了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也可以做游击士吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1164(): pass

    label('loc_1164')

    Jump('loc_14B1')

    def _loc_1167(): pass

    label('loc_1167')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1237',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1203',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '啊啊，要是我也有\n',
            '像约修亚那样的哥哥就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '缇欧姐姐因为要帮忙做事，\n',
            '所以经常不能陪我玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '查儿姐姐也\n',
            '只会玩过家家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1234')

    def _loc_1203(): pass

    label('loc_1203')

    ChrTalk(
        0x00FE,
        (
            '啊啊，要是我也有\n',
            '像约修亚那样的哥哥就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1234(): pass

    label('loc_1234')

    Jump('loc_14B1')

    def _loc_1237(): pass

    label('loc_1237')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1272',
    )

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '约修亚哥哥，再来玩呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14B1')

    def _loc_1272(): pass

    label('loc_1272')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_14B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 6, 0x22E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 3, 0x283)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1367',
    )

    SetScenaFlags(ScenaFlag(0x0050, 3, 0x283))
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，是约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了！\n',
            '一起来玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F啊，对不起。\n',
            '今天我是来工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作？\n',
            '我一个人玩很无聊的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#011F呵呵，有时间再一起玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约修亚还是那么\n',
            '受这里的孩子们欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13A1')

    def _loc_1367(): pass

    label('loc_1367')

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '约修亚哥哥，\n',
            '有空就要陪我玩呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13A1(): pass

    label('loc_13A1')

    Jump('loc_14B1')

    def _loc_13A4(): pass

    label('loc_13A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 3, 0x283)),
            Expr.Return,
        ),
        'loc_13D4',
    )

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '约修亚哥哥～\n',
            '赶快来玩吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14B1')

    def _loc_13D4(): pass

    label('loc_13D4')

    SetScenaFlags(ScenaFlag(0x0050, 3, 0x283))
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，是约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了！\n',
            '一起来玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F啊，对不起。\n',
            '今天我是来工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作？\n',
            '我一个人玩很无聊的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#011F呵呵，有时间再一起玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约修亚还是那么\n',
            '受这里的孩子们欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14B1(): pass

    label('loc_14B1')

    TalkEnd(0x0009)

    Return()

# id: 0x000D offset: 0x14B5
@scena.Code('func_0D_14B5')
def func_0D_14B5():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_163D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0056, 6, 0x2B6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15F5',
    )

    SetScenaFlags(ScenaFlag(0x0056, 6, 0x2B6))
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，约修亚……\n',
            '你要到哪儿去啊？ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，有点事情要办，\n',
            '打算去柏斯地区那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很快就回来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F唔……\n',
            '我想恐怕不太可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个那个……\n',
            '查儿会等你回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以呢，\n',
            '你回来之后要来这里和我玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F嗯，说定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_163A')

    def _loc_15F5(): pass

    label('loc_15F5')

    ChrTalk(
        0x00FE,
        (
            '那个那个……\n',
            '查儿会等你回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以呢，你要再来这里玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_163A(): pass

    label('loc_163A')

    Jump('loc_193F')

    def _loc_163D(): pass

    label('loc_163D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1739',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1713',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '那、那个，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后查儿也会\n',
            '帮农场干活的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，这不是很好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚轻轻地抚摸了一下查儿的头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '嗯！\n',
            '呵呵，加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1736')

    def _loc_1713(): pass

    label('loc_1713')

    ChrTalk(
        0x00FE,
        (
            '以后查儿也会\n',
            '帮农场干活的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1736(): pass

    label('loc_1736')

    Jump('loc_193F')

    def _loc_1739(): pass

    label('loc_1739')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_193F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 6, 0x22E)),
            Expr.Return,
        ),
        'loc_1846',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 2, 0x282)),
            Expr.Return,
        ),
        'loc_17A2',
    )

    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，约修亚……\n',
            '那个，我爸爸妈妈已经回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '现在就在家里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1843')

    def _loc_17A2(): pass

    label('loc_17A2')

    SetScenaFlags(ScenaFlag(0x0050, 2, 0x282))

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呀嗬～查儿，\n',
            '最近还好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x0102,
        (
            '#010F小查儿，\n',
            '你爸爸妈妈回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊……嗯，回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在就在家里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1843(): pass

    label('loc_1843')

    Jump('loc_193F')

    def _loc_1846(): pass

    label('loc_1846')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 2, 0x282)),
            Expr.Return,
        ),
        'loc_188E',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '现在爸爸妈妈都不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐的话，\n',
            '倒是在那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_193F')

    def _loc_188E(): pass

    label('loc_188E')

    SetScenaFlags(ScenaFlag(0x0050, 2, 0x282))

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呀嗬～查儿，\n',
            '最近还好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F小查儿，\n',
            '你爸爸妈妈在哪儿？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '现在爸爸妈妈都不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐的话，\n',
            '倒是在那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_193F(): pass

    label('loc_193F')

    TalkEnd(0x000A)

    Return()

# id: 0x000E offset: 0x1943
@scena.Code('func_0E_1943')
def func_0E_1943():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1A6E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19FC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '自从飞艇发明以来，\n',
            '我们农场就不断接到\n',
            '来自各个地方的采购单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '我们也不能满足所有顾客的定购啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时候蔬菜供不应求，\n',
            '真不知该高兴还是烦恼。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A6B')

    def _loc_19FC(): pass

    label('loc_19FC')

    ChrTalk(
        0x00FE,
        (
            '自从飞艇发明以来，\n',
            '我们农场就不断接到\n',
            '来自各个地方的采购单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '我们也不能满足所有顾客的定购啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A6B(): pass

    label('loc_1A6B')

    Jump('loc_1D9A')

    def _loc_1A6E(): pass

    label('loc_1A6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1B8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B29',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '哦哦，你们两个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我到城镇的时候\n',
            '听到了你们的传闻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在你们可是\n',
            '赫赫有名的游击士啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们为我们\n',
            '保卫农田的这件事\n',
            '已经成为我引以为豪的话题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B88')

    def _loc_1B29(): pass

    label('loc_1B29')

    ChrTalk(
        0x00FE,
        (
            '我到城镇的时候\n',
            '现在你们可是',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们为我们\n',
            '保卫农田的这件事\n',
            '已经成为我引以为豪的话题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B88(): pass

    label('loc_1B88')

    Jump('loc_1D9A')

    def _loc_1B8B(): pass

    label('loc_1B8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1CC6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C54',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '哦哦，你们两个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从你们来了之后，\n',
            '那些魔兽再也没有来捣乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔬菜也像往常那样\n',
            '可以对外供应了。\n',
            '一家人总算安心下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全靠你们的功劳啊。\n',
            '真的十分感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC3')

    def _loc_1C54(): pass

    label('loc_1C54')

    ChrTalk(
        0x00FE,
        (
            '全靠你们的功劳，\n',
            '那些魔兽再也没有来捣乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔬菜也像往常那样\n',
            '可以对外供应了。\n',
            '一家人总算安心下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CC3(): pass

    label('loc_1CC3')

    Jump('loc_1D9A')

    def _loc_1CC6(): pass

    label('loc_1CC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1D9A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D4B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '这次你们真是帮了大忙。\n',
            '这下就能恢复蔬菜的输出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有很多人等着\n',
            '我们农场的蔬菜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须加把劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9A')

    def _loc_1D4B(): pass

    label('loc_1D4B')

    ChrTalk(
        0x00FE,
        (
            '这次你们真是帮了大忙，\n',
            '这下就能恢复蔬菜的输出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的十分感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D9A(): pass

    label('loc_1D9A')

    TalkEnd(0x000B)

    Return()

# id: 0x000F offset: 0x1D9E
@scena.Code('func_0F_1D9E')
def func_0F_1D9E():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1E9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E44',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '这不是艾丝蒂尔和约修亚嘛。\n',
            '是来这里办事的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士这份工作\n',
            '也不是那么轻松的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '千万不要蛮干，\n',
            '要循序渐进慢慢努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E98')

    def _loc_1E44(): pass

    label('loc_1E44')

    ChrTalk(
        0x00FE,
        (
            '游击士这份工作\n',
            '也不是那么轻松的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '千万不要蛮干，\n',
            '要循序渐进慢慢努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E98(): pass

    label('loc_1E98')

    Jump('loc_1F0F')

    def _loc_1E9B(): pass

    label('loc_1E9B')

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔、约修亚。\n',
            '最近你们两个还不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有时间的话，再过来这里玩哦。\n',
            '那些孩子们都很想见你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1F0F(): pass

    label('loc_1F0F')

    TalkEnd(0x000C)

    Return()

# id: 0x0010 offset: 0x1F13
@scena.Code('func_10_1F13')
def func_10_1F13():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetPos(0x0101, 23380, 0, 61450, 0)
    ChrSetPos(0x0102, 24610, 0, 61450, 0)
    CameraMove(44190, 0, 16580, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3830, 0)
    OP_6C(269000, 0)
    OP_6E(261, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1F88')
    def lambda_1F88():
        OP_6C(0, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F88)

    CameraMove(22290, 0, 23280, 6000)

    @scena.Lambda('lambda_1FA9')
    def lambda_1FA9():
        CameraMove(24020, 0, 51850, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FA9)

    Sleep(3000)

    @scena.Lambda('lambda_1FC6')
    def lambda_1FC6():
        ChrWalkTo(0x00FE, 23800, 60, 50730, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1FC6)

    Sleep(500)

    @scena.Lambda('lambda_1FE6')
    def lambda_1FE6():
        ChrWalkTo(0x00FE, 24760, 160, 51410, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1FE6)

    Sleep(3600)

    Fade(1000)
    CameraMove(24140, 30, 50930, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001348V#501F哈啊～\n',
            '每次来这里都感到这么悠闲宁静。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001349V#501F有魔兽来捣乱这种事，\n',
            '还真是让人不敢相信呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001350V#010F现在确实感觉不到魔兽的气息……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001351V#010F总之先了解一下情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001352V#000F缇欧会在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0000, 0xFF)
    EventEnd(0x00)
    MapClearFlags(0x00400000)

    Return()

# id: 0x0011 offset: 0x2155
@scena.Code('func_11_2155')
def func_11_2155():
    OP_A6(0x0000)
    CameraSetDistance(4370, 6000)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0012 offset: 0x2165
@scena.Code('func_12_2165')
def func_12_2165():
    EventBegin(0x00)
    MapSetFlags(0x00400000)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000B, 0x0008)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000C, 0x0008)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000A, 0x0008)
    ChrSetPos(0x000B, 23950, 20, 50260, 0)
    ChrSetPos(0x000C, 25400, 310, 50280, 0)
    ChrSetPos(0x0008, 23110, 280, 51210, 45)
    ChrSetPos(0x0009, 24740, 150, 51220, 0)
    ChrSetPos(0x000A, 25710, 360, 51250, 0)
    ChrSetPos(0x0101, 23600, 130, 52840, 180)
    ChrSetPos(0x0102, 24780, 160, 53490, 180)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    CameraMove(23970, 130, 51650, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeOut(0, 0, -1)
    OP_20(0x00000000)
    PlaySE(13, 0x00, 0x64)
    Sleep(5000)

    OP_1E()
    FadeIn(2000, 0)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0910001614V谢谢啊。\n',
            '这次你们真是帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0910001615V不过最后却害你们没能完成任务。\n',
            '实在是有点过意不去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001616V#010F请不要介意。\n',
            '我们从这次任务中学到了很多东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001617V#010F如果以后再有需要帮助的地方，\n',
            '尽管联络游击士协会就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0910001618V一定会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0890001619V艾丝蒂尔、约修亚。\n',
            '记得有空多来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0900001620V工作不忙的话要经常来这里住哦。\n',
            '到时候煮些更好吃的菜给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001621V#001F谢谢啦，缇欧，还有阿姨。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001622V#019F我们一定会再来拜访的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    FadeOut(1000, 0, -1)
    OP_0D()
    NewScene('ED6_DT01/R0201._SN', 0, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x24BA
@scena.Code('func_13_24BA')
def func_13_24BA():
    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, 23890, 0, 62090, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0008)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0014 offset: 0x24E0
@scena.Code('func_14_24E0')
def func_14_24E0():
    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, 23890, 0, 62090, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0008)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
