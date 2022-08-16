import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4205_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4205   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4205.x'
    header.mapIndex       = 1
    header.bgm            = 31
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
        ('ED6_DT09/CH10490._CH', 'ED6_DT09/CH10490P._CP'),
        ('ED6_DT09/CH10491._CH', 'ED6_DT09/CH10491P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
        ('ED6_DT09/CH10510._CH', 'ED6_DT09/CH10510P._CP'),
        ('ED6_DT09/CH10511._CH', 'ED6_DT09/CH10511P._CP'),
        ('ED6_DT09/CH11110._CH', 'ED6_DT09/CH11110P._CP'),
        ('ED6_DT09/CH11111._CH', 'ED6_DT09/CH11111P._CP'),
        ('ED6_DT09/CH11120._CH', 'ED6_DT09/CH11120P._CP'),
        ('ED6_DT09/CH11121._CH', 'ED6_DT09/CH11121P._CP'),
        ('ED6_DT09/CH11130._CH', 'ED6_DT09/CH11130P._CP'),
        ('ED6_DT09/CH11131._CH', 'ED6_DT09/CH11131P._CP'),
        ('ED6_DT09/CH11140._CH', 'ED6_DT09/CH11140P._CP'),
        ('ED6_DT09/CH11141._CH', 'ED6_DT09/CH11141P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT29/CH12070._CH', 'ED6_DT29/CH12070P._CP'),
        ('ED6_DT29/CH12071._CH', 'ED6_DT29/CH12071P._CP'),
    ]

# id: 0x10001 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 58000,
            z                   = 1500,
            y                   = 52910,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '漆黑猿羊',
            x                   = 54070,
            z                   = 450,
            y                   = 101970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '漆黑猿羊',
            x                   = 54070,
            z                   = 450,
            y                   = 101970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '漆黑猿羊',
            x                   = 54070,
            z                   = 450,
            y                   = 101970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '漆黑猿羊',
            x                   = 54070,
            z                   = 450,
            y                   = 101970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '漆黑猿羊',
            x                   = 54070,
            z                   = 450,
            y                   = 101970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '漆黑猿羊',
            x                   = 54070,
            z                   = 450,
            y                   = 101970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '漆黑猿羊',
            x                   = 54070,
            z                   = 450,
            y                   = 101970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '粉红猿羊',
            x                   = 54070,
            z                   = 450,
            y                   = 101970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x29A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -5110,
            z           = 0,
            y           = 48870,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0274,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 32880,
            z           = 0,
            y           = 53420,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x026D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -29030,
            z           = 0,
            y           = 93770,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0275,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -11760,
            z           = 0,
            y           = 93750,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0271,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -20280,
            z           = 0,
            y           = 93650,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -31370,
            z           = 1000,
            y           = 112540,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x026D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x342
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 49300,
            y           = 0,
            z           = 103300,
            range       = 52050,
            dword_10    = 0x000009C4,
            dword_14    = 0x000187D6,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x362
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 57390,
            triggerZ            = 0,
            triggerY            = 52780,
            triggerRange        = 1000,
            actorX              = 58000,
            actorZ              = 1500,
            actorY              = 52910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30130,
            triggerZ            = 0,
            triggerY            = 114540,
            triggerRange        = 1000,
            actorX              = -29940,
            actorZ              = 0,
            actorY              = 115160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3AA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 7, 0x16FF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C8',
    )

    ChrSetPos(0x0009, 76660, 0, 102000, 270)
    ChrClearFlags(0x0009, 0x0080)

    def _loc_3C8(): pass

    label('loc_3C8')

    Return()

# id: 0x0001 offset: 0x3C9
@scena.Code('func_01_3C9')
def func_01_3C9():
    OP_1B(0x0D, 0x00, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E4, 2, 0x1722)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E0',
    )

    OP_6F(0x0000, 0)

    Jump('loc_3E7')

    def _loc_3E0(): pass

    label('loc_3E0')

    OP_6F(0x0000, 60)

    def _loc_3E7(): pass

    label('loc_3E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E4, 4, 0x1724)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F9',
    )

    OP_6F(0x0001, 0)

    Jump('loc_400')

    def _loc_3F9(): pass

    label('loc_3F9')

    OP_6F(0x0001, 60)

    def _loc_400(): pass

    label('loc_400')

    ExecExpressionWithValue(
        0x0012,
        0x24,
        (
            (Expr.PushLong, 0xE7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0016,
        0x24,
        (
            (Expr.PushLong, 0xE7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x417
@scena.Code('func_02_417')
def func_02_417():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_57E')

    def _loc_43C(): pass

    label('loc_43C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_455',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_57E')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_46E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_57E')

    def _loc_46E(): pass

    label('loc_46E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_487',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_57E')

    def _loc_487(): pass

    label('loc_487')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A0',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_57E')

    def _loc_4A0(): pass

    label('loc_4A0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B9',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_57E')

    def _loc_4B9(): pass

    label('loc_4B9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D2',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_57E')

    def _loc_4D2(): pass

    label('loc_4D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4EB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_57E')

    def _loc_4EB(): pass

    label('loc_4EB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_504',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_57E')

    def _loc_504(): pass

    label('loc_504')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51D',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_57E')

    def _loc_51D(): pass

    label('loc_51D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_536',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_57E')

    def _loc_536(): pass

    label('loc_536')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_54F',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_57E')

    def _loc_54F(): pass

    label('loc_54F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_568',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_57E')

    def _loc_568(): pass

    label('loc_568')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_57E(): pass

    label('loc_57E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_593',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_57E')

    def _loc_593(): pass

    label('loc_593')

    Return()

# id: 0x0003 offset: 0x594
@scena.Code('func_03_594')
def func_03_594():
    EventBegin(0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '隐藏门被完全封锁了，\n',
            '无法通过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrMoveToRelative(0x0000, 1000, 0, 0, 2000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0004 offset: 0x600
@scena.Code('func_04_600')
def func_04_600():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 7, 0x16FF)),
            Expr.Return,
        ),
        'loc_608',
    )

    Return()

    def _loc_608(): pass

    label('loc_608')

    EventBegin(0x00)
    ChrSetDirection(0x0000, 90, 0)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x0009, 76660, 0, 102000, 270)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetChipByIndex(0x0009, 15)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_0653')
    def lambda_0653():
        ChrMoveToRelativeAsync(0x00FE, -24160, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0653)

    ChrSetPos(0x000A, 78660, 0, 102500, 270)
    ChrSetPos(0x000B, 78660, 0, 101500, 270)
    ChrSetPos(0x000C, 80660, 0, 102000, 270)
    ChrSetPos(0x000D, 82660, 0, 102500, 270)
    ChrSetPos(0x000E, 82660, 0, 101500, 270)
    ChrSetPos(0x000F, 84660, 0, 102000, 270)
    ChrSetPos(0x0010, 86660, 0, 102000, 270)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetChipByIndex(0x000A, 15)
    ChrSetSubChip(0x000A, 0)
    ChrSetChipByIndex(0x000B, 15)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000C, 15)
    ChrSetSubChip(0x000C, 0)
    ChrSetChipByIndex(0x000D, 15)
    ChrSetSubChip(0x000D, 0)
    ChrSetChipByIndex(0x000E, 15)
    ChrSetSubChip(0x000E, 0)
    ChrSetChipByIndex(0x000F, 15)
    ChrSetSubChip(0x000F, 0)
    ChrSetChipByIndex(0x0010, 25)
    ChrSetSubChip(0x0010, 0)
    CreateThread(0x0009, 0x00, 0x00, func_02_417)
    CreateThread(0x000A, 0x00, 0x00, func_02_417)
    CreateThread(0x000B, 0x00, 0x00, func_02_417)
    CreateThread(0x000C, 0x00, 0x00, func_02_417)
    CreateThread(0x000D, 0x00, 0x00, func_02_417)
    CreateThread(0x000E, 0x00, 0x00, func_02_417)
    CreateThread(0x000F, 0x00, 0x00, func_02_417)
    CreateThread(0x0010, 0x00, 0x00, func_02_417)

    @scena.Lambda('lambda_078B')
    def lambda_078B():
        ChrMoveToRelativeAsync(0x00FE, -24160, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_078B)

    @scena.Lambda('lambda_07A6')
    def lambda_07A6():
        ChrMoveToRelativeAsync(0x00FE, -24160, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07A6)

    @scena.Lambda('lambda_07C1')
    def lambda_07C1():
        ChrMoveToRelativeAsync(0x00FE, -24160, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_07C1)

    @scena.Lambda('lambda_07DC')
    def lambda_07DC():
        ChrMoveToRelativeAsync(0x00FE, -24160, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_07DC)

    @scena.Lambda('lambda_07F7')
    def lambda_07F7():
        ChrMoveToRelativeAsync(0x00FE, -24160, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_07F7)

    @scena.Lambda('lambda_0812')
    def lambda_0812():
        ChrMoveToRelativeAsync(0x00FE, -24160, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0812)

    @scena.Lambda('lambda_082D')
    def lambda_082D():
        ChrMoveToRelativeAsync(0x00FE, -24160, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_082D)

    @scena.Lambda('lambda_0848')
    def lambda_0848():
        CameraMove(60800, 120, 102000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0848)

    @scena.Lambda('lambda_0860')
    def lambda_0860():
        OP_67(0, 5150, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0860)

    @scena.Lambda('lambda_0878')
    def lambda_0878():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0878)

    @scena.Lambda('lambda_0888')
    def lambda_0888():
        OP_6C(90000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0888)

    WaitForThreadExit(0x0000, 0x0000)
    ChrSetFlags(0x00F7, 0x0040)
    ChrSetFlags(0x00F8, 0x0040)
    ChrSetPos(0x0101, 49500, 450, 102000, 90)
    ChrSetPos(0x00F7, 48200, 300, 102600, 90)
    ChrSetPos(0x00F8, 48200, 300, 101400, 90)
    ChrSetPos(0x00F9, 46950, 0, 102000, 90)
    ChrSetChipByIndex(0x0101, 16)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            Expr.Return,
        ),
        (0x00000001, 'loc_90F'),
        (0x00000002, 'loc_917'),
        (0x00000003, 'loc_91F'),
        (0x00000004, 'loc_927'),
        (0x00000005, 'loc_92F'),
        (0x00000006, 'loc_937'),
        (0x00000007, 'loc_93F'),
        (-1, 'loc_947'),
    )

    def _loc_90F(): pass

    label('loc_90F')

    ChrSetChipByIndex(0x00F7, 17)

    Jump('loc_947')

    def _loc_917(): pass

    label('loc_917')

    ChrSetChipByIndex(0x00F7, 18)

    Jump('loc_947')

    def _loc_91F(): pass

    label('loc_91F')

    ChrSetChipByIndex(0x00F7, 19)

    Jump('loc_947')

    def _loc_927(): pass

    label('loc_927')

    ChrSetChipByIndex(0x00F7, 20)

    Jump('loc_947')

    def _loc_92F(): pass

    label('loc_92F')

    ChrSetChipByIndex(0x00F7, 21)

    Jump('loc_947')

    def _loc_937(): pass

    label('loc_937')

    ChrSetChipByIndex(0x00F7, 22)

    Jump('loc_947')

    def _loc_93F(): pass

    label('loc_93F')

    ChrSetChipByIndex(0x00F7, 23)

    Jump('loc_947')

    def _loc_947(): pass

    label('loc_947')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000001, 'loc_96C'),
        (0x00000002, 'loc_974'),
        (0x00000003, 'loc_97C'),
        (0x00000004, 'loc_984'),
        (0x00000005, 'loc_98C'),
        (0x00000006, 'loc_994'),
        (0x00000007, 'loc_99C'),
        (-1, 'loc_9A4'),
    )

    def _loc_96C(): pass

    label('loc_96C')

    ChrSetChipByIndex(0x00F8, 17)

    Jump('loc_9A4')

    def _loc_974(): pass

    label('loc_974')

    ChrSetChipByIndex(0x00F8, 18)

    Jump('loc_9A4')

    def _loc_97C(): pass

    label('loc_97C')

    ChrSetChipByIndex(0x00F8, 19)

    Jump('loc_9A4')

    def _loc_984(): pass

    label('loc_984')

    ChrSetChipByIndex(0x00F8, 20)

    Jump('loc_9A4')

    def _loc_98C(): pass

    label('loc_98C')

    ChrSetChipByIndex(0x00F8, 21)

    Jump('loc_9A4')

    def _loc_994(): pass

    label('loc_994')

    ChrSetChipByIndex(0x00F8, 22)

    Jump('loc_9A4')

    def _loc_99C(): pass

    label('loc_99C')

    ChrSetChipByIndex(0x00F8, 23)

    Jump('loc_9A4')

    def _loc_9A4(): pass

    label('loc_9A4')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000001, 'loc_9C9'),
        (0x00000002, 'loc_9D1'),
        (0x00000003, 'loc_9D9'),
        (0x00000004, 'loc_9E1'),
        (0x00000005, 'loc_9E9'),
        (0x00000006, 'loc_9F1'),
        (0x00000007, 'loc_9F9'),
        (-1, 'loc_A01'),
    )

    def _loc_9C9(): pass

    label('loc_9C9')

    ChrSetChipByIndex(0x00F9, 17)

    Jump('loc_A01')

    def _loc_9D1(): pass

    label('loc_9D1')

    ChrSetChipByIndex(0x00F9, 18)

    Jump('loc_A01')

    def _loc_9D9(): pass

    label('loc_9D9')

    ChrSetChipByIndex(0x00F9, 19)

    Jump('loc_A01')

    def _loc_9E1(): pass

    label('loc_9E1')

    ChrSetChipByIndex(0x00F9, 20)

    Jump('loc_A01')

    def _loc_9E9(): pass

    label('loc_9E9')

    ChrSetChipByIndex(0x00F9, 21)

    Jump('loc_A01')

    def _loc_9F1(): pass

    label('loc_9F1')

    ChrSetChipByIndex(0x00F9, 22)

    Jump('loc_A01')

    def _loc_9F9(): pass

    label('loc_9F9')

    ChrSetChipByIndex(0x00F9, 23)

    Jump('loc_A01')

    def _loc_A01(): pass

    label('loc_A01')

    Sleep(2000)

    @scena.Lambda('lambda_0A0C')
    def lambda_0A0C():
        CameraMove(51900, 450, 102000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0A0C)

    WaitForThreadExit(0x0009, 0x0001)
    Battle(0x00000277, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrClearFlags(0x00F7, 0x0040)
    ChrClearFlags(0x00F8, 0x0040)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_A4E'),
        (0x00000000, 'loc_A53'),
        (0x00000002, 'loc_A5A'),
        (-1, 'loc_A61'),
    )

    def _loc_A4E(): pass

    label('loc_A4E')

    OP_B4(0x00)

    Jump('loc_A61')

    def _loc_A53(): pass

    label('loc_A53')

    Call(0, 0x0005)

    Jump('loc_A61')

    def _loc_A5A(): pass

    label('loc_A5A')

    Call(0, 0x0006)

    Jump('loc_A61')

    def _loc_A61(): pass

    label('loc_A61')

    Return()

# id: 0x0005 offset: 0xA62
@scena.Code('func_05_A62')
def func_05_A62():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x01)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    CameraMove(50000, 450, 101960, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 50000, 450, 101960, 90)
    ChrSetPos(0x0001, 50000, 450, 101960, 90)
    ChrSetPos(0x0002, 50000, 450, 101960, 90)
    ChrSetPos(0x0003, 50000, 450, 101960, 90)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetSubChip(0x00F7, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    SetScenaFlags(ScenaFlag(0x02DF, 7, 0x16FF))
    OP_B2(0x00, 0x00, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xB78
@scena.Code('func_06_B78')
def func_06_B78():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x01)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetPos(0x0009, 76660, 0, 102000, 270)
    ChrClearFlags(0x0009, 0x0080)
    CameraMove(45980, 0, 101860, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 45980, 0, 101860, 270)
    ChrSetPos(0x0001, 45980, 0, 101860, 270)
    ChrSetPos(0x0002, 45980, 0, 101860, 270)
    ChrSetPos(0x0003, 45980, 0, 101860, 270)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x00F7, 65535)
    ChrSetSubChip(0x00F7, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xC97
@scena.Code('func_07_C97')
def func_07_C97():
    UnlockAchievement(0x02, 0x0109, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E4, 2, 0x1722)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E2F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E4, 3, 0x1723)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D7B',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0CEE')
    def lambda_0CEE():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CEE)

    @scena.Lambda('lambda_0D09')
    def lambda_0D09():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0D09)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000276, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_D56'),
        (0x00000002, 'loc_D68'),
        (0x00000001, 'loc_D78'),
        (-1, 'loc_D7B'),
    )

    def _loc_D56(): pass

    label('loc_D56')

    SetScenaFlags(ScenaFlag(0x02E4, 3, 0x1723))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_D7B')

    def _loc_D68(): pass

    label('loc_D68')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_D78(): pass

    label('loc_D78')

    OP_B4(0x00)

    Return()

    def _loc_D7B(): pass

    label('loc_D7B')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['神圣修女服'], 1)"),
            Expr.Return,
        ),
        'loc_DCA',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['神圣修女服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x02E4, 2, 0x1722))

    Jump('loc_E2C')

    def _loc_DCA(): pass

    label('loc_DCA')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['神圣修女服']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['神圣修女服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_E2C(): pass

    label('loc_E2C')

    Jump('loc_E5E')

    def _loc_E2F(): pass

    label('loc_E2F')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_E5E(): pass

    label('loc_E5E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xE6C
@scena.Code('func_08_E6C')
def func_08_E6C():
    UnlockAchievement(0x02, 0x010A, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E4, 4, 0x1724)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F8A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 30)
    OP_73(0x0001)
    OP_6F(0x0001, 30)
    AddSepith(0x00, 25)
    AddSepith(0x01, 25)
    AddSepith(0x02, 25)
    AddSepith(0x03, 25)
    AddSepith(0x04, 25)
    AddSepith(0x05, 25)
    AddSepith(0x06, 25)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×２５\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×２５\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×２５\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×２５\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×２５\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×２５\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×２５\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x02E4, 4, 0x1724))

    Jump('loc_FA4')

    def _loc_F8A(): pass

    label('loc_F8A')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_FA4(): pass

    label('loc_FA4')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
