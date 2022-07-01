import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2400   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特蕾莎院长'),
    TXT(0x02, '达尼艾尔'),
    TXT(0x03, '玛丽'),
    TXT(0x04, '克拉姆'),
    TXT(0x05, '吉克'),
    TXT(0x06, '目标用照相机'),
    TXT(0x07, '鸡'),
    TXT(0x08, '鸡'),
    TXT(0x09, '鸡'),
    TXT(0x0A, '梅威海道方向'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2400.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x465
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
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 33500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 6000,
            z                   = 200,
            y                   = 22200,
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
            x                   = 5800,
            z                   = 0,
            y                   = 23600,
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
            x                   = 4300,
            z                   = 200,
            y                   = 22900,
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
            x                   = 800,
            z                   = 6000,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
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
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 1060,
            z                   = 0,
            y                   = -23220,
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

# id: 0x10003 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x232
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x233
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0C00, 0xFFFE5A20, 0x00230067)

    Return()

# id: 0x0002 offset: 0x246
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_25B',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_25B(): pass

    label('loc_25B')

    Return()

# id: 0x0003 offset: 0x25C
@scena.Code('func_03_25C')
def func_03_25C():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, -8760, 13210, 8700, 24630, 0)

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

    def _loc_28A(): pass

    label('loc_28A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3AE',
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
        'loc_373',
    )

    If(
        (
            (Expr.PushLong, 0x2238),
            Expr.Neg,
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Lss,
            (Expr.PushLong, 0x339A),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushLong, 0x21FC),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.PushLong, 0x6036),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_348',
    )

    SetChrFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ClearChrFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_0335')
    def lambda_0335():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0335)

    Jump('loc_36B')

    def _loc_348(): pass

    label('loc_348')

    @scena.Lambda('lambda_034E')
    def lambda_034E():
        OP_8D(0x00FE, -8760, 13210, 8700, 24630, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_034E)

    Sleep(200)

    def _loc_36B(): pass

    label('loc_36B')

    Sleep(30)

    Jump('loc_3AB')

    def _loc_373(): pass

    label('loc_373')

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
        'loc_3AB',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_0393')
    def lambda_0393():
        OP_8D(0x00FE, -8760, 13210, 8700, 24630, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0393)

    def _loc_3AB(): pass

    label('loc_3AB')

    Jump('loc_28A')

    def _loc_3AE(): pass

    label('loc_3AE')

    Return()

# id: 0x0004 offset: 0x3AF
@scena.Code('func_04_3AF')
def func_04_3AF():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_432',
    )

    CreateThread(0x00FE, 0x02, 0x00, 0x0005)
    OP_22(0x0191, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_432',
    )

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['新鲜鸡蛋'], 1)"),
            Expr.Return,
        ),
        'loc_432',
    )

    TalkBegin(0x00FE)
    OP_A2(0x0000)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['新鲜鸡蛋']),
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

    def _loc_432(): pass

    label('loc_432')

    Return()

# id: 0x0005 offset: 0x433
@scena.Code('func_05_433')
def func_05_433():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_44E',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_05_433')

    def _loc_44E(): pass

    label('loc_44E')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
