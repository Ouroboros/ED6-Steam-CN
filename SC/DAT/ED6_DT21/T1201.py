import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '莱森村长'),
    TXT(0x02, '罗亚'),
    TXT(0x03, '菲戈'),
    TXT(0x04, '贝斯卡'),
    TXT(0x05, '库赖老人'),
    TXT(0x06, '巴德斯'),
    TXT(0x07, '拉文努山道方向'),
    TXT(0x08, '拉文努废坑方向'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1201.x'
    header.mapIndex       = 1
    header.bgm            = 26
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x36A1
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
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 24310,
            z                   = -4000,
            y                   = 16670,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 26100,
            z                   = -4000,
            y                   = 12970,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 20640,
            z                   = -4000,
            y                   = 19180,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 19590,
            z                   = -4000,
            y                   = 16200,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 17380,
            z                   = -4000,
            y                   = 9850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 22560,
            z                   = -530,
            y                   = 26920,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
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

# id: 0x10003 offset: 0x1E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -3900,
            y           = -1000,
            z           = 6200,
            range       = -100,
            dword_10    = 0x000007D0,
            dword_14    = 0x00001FA4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = 5000,
            y           = 0,
            z           = 34240,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 5150,
            y           = 4550,
            z           = 41780,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 5310,
            y           = 0,
            z           = 23020,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = 6000,
            y           = 4400,
            z           = 54640,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 3260,
            y           = 7000,
            z           = 66870,
            range       = 9230,
            dword_10    = 0x00002710,
            dword_14    = 0x00010C52,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = -3900,
            y           = -100,
            z           = 7250,
            range       = -100,
            dword_10    = 0x0000076C,
            dword_14    = 0x0000203A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001B,
        ),
        ScenaEventData(
            x           = 5100,
            y           = 8000,
            z           = 67350,
            range       = 9000,
            dword_10    = 0x00002710,
            dword_14    = 0x00010AFE,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001B,
        ),
    )

# id: 0x10005 offset: 0x2E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -7280,
            triggerZ            = 4460,
            triggerY            = 54000,
            triggerRange        = 800,
            actorX              = -7280,
            actorZ              = 5460,
            actorY              = 54000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33020,
            triggerZ            = 8000,
            triggerY            = 35080,
            triggerRange        = 1000,
            actorX              = 33020,
            actorZ              = 9200,
            actorY              = 35080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x32A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_33E',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000D, 0x0080)

    Jump('loc_34A')

    def _loc_33E(): pass

    label('loc_33E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_34A',
    )

    SetChrFlags(0x000D, 0x0010)

    def _loc_34A(): pass

    label('loc_34A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_360',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0011)

    Jump('loc_380')

    def _loc_360(): pass

    label('loc_360')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_36C'),
        (-1, 'loc_380'),
    )

    def _loc_36C(): pass

    label('loc_36C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 4, 0x1A14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37D',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000F)

    def _loc_37D(): pass

    label('loc_37D')

    Jump('loc_380')

    def _loc_380(): pass

    label('loc_380')

    Return()

# id: 0x0001 offset: 0x381
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE5638, 0xFFFE98A0, 0x00230043)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_3A6',
    )

    OP_B1('t1201_n')

    Jump('loc_560')

    def _loc_3A6(): pass

    label('loc_3A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 3, 0x1A83)),
            Expr.Return,
        ),
        'loc_3CE',
    )

    OP_B1('t1201_y')
    OP_10(0x08, 0x00)
    OP_82(0x86, 0x00)
    OP_82(0x87, 0x00)
    OP_82(0x88, 0x00)
    OP_82(0x89, 0x00)
    OP_82(0x8A, 0x00)
    OP_82(0x8B, 0x00)

    Jump('loc_560')

    def _loc_3CE(): pass

    label('loc_3CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_560',
    )

    OP_B1('t1201_n')
    LoadEffect(0x00, 'map\\mpsmk0.eff')
    LoadEffect(0x01, 'map\\mpsmk1.eff')
    LoadEffect(0x02, 'map\\mpsmk2.eff')
    LoadEffect(0x03, 'map\\mpsmk3.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 17810, -3200, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 28240, -4000, 6260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x00FF, 17940, -3500, 24500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0xFF, 0x00FF, 14180, -3300, 7940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 16920, -3300, 16420, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x00FF, 21000, -4000, 7530, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_560(): pass

    label('loc_560')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_570',
    )

    OP_72(0x0006, 0x0010)

    Jump('loc_574')

    def _loc_570(): pass

    label('loc_570')

    OP_64(0x00, 0x0001)

    def _loc_574(): pass

    label('loc_574')

    SetMapFlags(0x02000000)
    OP_82(0x8C, 0x02)

    Return()

# id: 0x0002 offset: 0x57D
@scena.Code('ReInit')
def ReInit():
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
        'loc_5A2',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_6E4')

    def _loc_5A2(): pass

    label('loc_5A2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BB',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_6E4')

    def _loc_5BB(): pass

    label('loc_5BB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D4',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_6E4')

    def _loc_5D4(): pass

    label('loc_5D4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5ED',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_6E4')

    def _loc_5ED(): pass

    label('loc_5ED')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_606',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_6E4')

    def _loc_606(): pass

    label('loc_606')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61F',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_6E4')

    def _loc_61F(): pass

    label('loc_61F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_638',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_6E4')

    def _loc_638(): pass

    label('loc_638')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_651',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_6E4')

    def _loc_651(): pass

    label('loc_651')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66A',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_6E4')

    def _loc_66A(): pass

    label('loc_66A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_683',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_6E4')

    def _loc_683(): pass

    label('loc_683')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_69C',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_6E4')

    def _loc_69C(): pass

    label('loc_69C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B5',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_6E4')

    def _loc_6B5(): pass

    label('loc_6B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CE',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_6E4')

    def _loc_6CE(): pass

    label('loc_6CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E4',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_6E4(): pass

    label('loc_6E4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6F9',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_6E4')

    def _loc_6F9(): pass

    label('loc_6F9')

    Return()

# id: 0x0003 offset: 0x6FA
@scena.Code('func_03_6FA')
def func_03_6FA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_71E',
    )

    OP_8C(0x00FE, 180, 400)
    Sleep(2000)

    OP_8C(0x00FE, 270, 400)
    Sleep(2000)

    Jump('func_03_6FA')

    def _loc_71E(): pass

    label('loc_71E')

    Return()

# id: 0x0004 offset: 0x71F
@scena.Code('func_04_71F')
def func_04_71F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_77E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_742',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_742(): pass

    label('loc_742')

    OP_8E(0x00FE, 21540, -4000, 9200, 2000, 0x00)
    Sleep(1000)

    OP_8E(0x00FE, 20390, -4000, 14160, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    Sleep(2000)

    Jump('func_04_71F')

    def _loc_77E(): pass

    label('loc_77E')

    Return()

# id: 0x0005 offset: 0x77F
@scena.Code('func_05_77F')
def func_05_77F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A2',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_7A2(): pass

    label('loc_7A2')

    OP_8E(0x00FE, 27130, -4000, 12130, 1000, 0x00)
    OP_8C(0x00FE, 225, 400)
    Sleep(2000)

    OP_8E(0x00FE, 26100, -4000, 12970, 1000, 0x00)
    OP_8C(0x00FE, 225, 400)
    Sleep(2000)

    Jump('func_05_77F')

    def _loc_7E5(): pass

    label('loc_7E5')

    Return()

# id: 0x0006 offset: 0x7E6
@scena.Code('func_06_7E6')
def func_06_7E6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_824',
    )

    OP_8C(0x00FE, 0, 400)
    Sleep(2000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_815',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_815(): pass

    label('loc_815')

    OP_8C(0x00FE, 315, 400)
    Sleep(2000)

    Jump('func_06_7E6')

    def _loc_824(): pass

    label('loc_824')

    Return()

# id: 0x0007 offset: 0x825
@scena.Code('func_07_825')
def func_07_825():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_88B',
    )

    OP_8E(0x00FE, 19590, -4000, 16200, 1000, 0x00)
    OP_8C(0x00FE, 225, 400)
    Sleep(2000)

    OP_8E(0x00FE, 20790, -4000, 14260, 1000, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_87C',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_87C(): pass

    label('loc_87C')

    OP_8C(0x00FE, 270, 400)
    Sleep(2000)

    Jump('func_07_825')

    def _loc_88B(): pass

    label('loc_88B')

    Return()

# id: 0x0008 offset: 0x88C
@scena.Code('func_08_88C')
def func_08_88C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8EB',
    )

    OP_8E(0x00FE, 15550, -4000, 9030, 1000, 0x00)
    Sleep(2000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C8',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_8C8(): pass

    label('loc_8C8')

    OP_8E(0x00FE, 17380, -4000, 9850, 1000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(2000)

    Jump('func_08_88C')

    def _loc_8EB(): pass

    label('loc_8EB')

    Return()

# id: 0x0009 offset: 0x8EC
@scena.Code('func_09_8EC')
def func_09_8EC():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 5, 0x1A15)),
            Expr.Return,
        ),
        'loc_93D',
    )

    ChrTalk(
        0x00FE,
        (
            '这里没事的，\n',
            '阿加特就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他好像一脸\n',
            '很沉重的表情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94C')

    def _loc_93D(): pass

    label('loc_93D')

    Call(0, 0x0010)
    OP_8C(0x0008, 180, 0)
    OP_4B(0x0008, 255)

    def _loc_94C(): pass

    label('loc_94C')

    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0x950
@scena.Code('func_0A_950')
def func_0A_950():
    TalkBegin(0x000C)
    OP_63(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_960',
    )

    Jump('loc_AED')

    def _loc_960(): pass

    label('loc_960')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_A4E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_9C1',
    )

    ChrTalk(
        0x00FE,
        (
            '必须要和年轻人一起\n',
            '好好考虑将来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要重建果树园\n',
            '需要所有人的团结啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4B')

    def _loc_9C1(): pass

    label('loc_9C1')

    ChrTalk(
        0x00FE,
        (
            '唉……真难受啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，光是叹息\n',
            '什么也无法开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '支撑村子的\n',
            '果树园不行了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须要和年轻人一起\n',
            '好好考虑将来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_A4B(): pass

    label('loc_A4B')

    Jump('loc_AED')

    def _loc_A4E(): pass

    label('loc_A4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_AED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_A91',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，真残酷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AED')

    def _loc_A91(): pass

    label('loc_A91')

    ChrTalk(
        0x00FE,
        (
            '呼，真残酷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至今一直倾注了心血\n',
            '培育出来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_AED(): pass

    label('loc_AED')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0xAF1
@scena.Code('func_0B_AF1')
def func_0B_AF1():
    TalkBegin(0x000B)
    OP_63(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_B01',
    )

    Jump('loc_CD1')

    def _loc_B01(): pass

    label('loc_B01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_BF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_B6A',
    )

    ChrTalk(
        0x00FE,
        (
            '我也有保护自己\n',
            '家人生活的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那果树园该怎么办，\n',
            '首先要和村里的人谈谈才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF0')

    def _loc_B6A(): pass

    label('loc_B6A')

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然难过……\n',
            '但现在不是消沉的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了家人\n',
            '必须考虑将来的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果树园该怎么办，\n',
            '需要和村里人好好谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_BF0(): pass

    label('loc_BF0')

    Jump('loc_CD1')

    def _loc_BF3(): pass

    label('loc_BF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_CD1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_C3B',
    )

    ChrTalk(
        0x00FE,
        (
            '现在应该\n',
            '考虑将来的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……首先是收拾善后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD1')

    def _loc_C3B(): pass

    label('loc_C3B')

    ChrTalk(
        0x00FE,
        (
            '好、好不容易引进的\n',
            '导力式拖拉机……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……总、总之现在\n',
            '要先收拾善后才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '考虑将来的事\n',
            '等做完这个再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_CD1(): pass

    label('loc_CD1')

    TalkEnd(0x000B)

    Return()

# id: 0x000C offset: 0xCD5
@scena.Code('func_0C_CD5')
def func_0C_CD5():
    TalkBegin(0x0009)
    OP_63(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_D96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D2D',
    )

    ChrTalk(
        0x00FE,
        (
            '我妻子和孩子都在柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里收拾完了\n',
            '我打算马上去那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D96')

    def _loc_D2D(): pass

    label('loc_D2D')

    ChrTalk(
        0x00FE,
        (
            '柏斯那边\n',
            '似乎也遭到了龙的破坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我妻子和孩子都在柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里收拾完了\n',
            '我打算马上去那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_D96(): pass

    label('loc_D96')

    TalkEnd(0x0009)

    Return()

# id: 0x000D offset: 0xD9A
@scena.Code('func_0D_D9A')
def func_0D_D9A():
    TalkBegin(0x000A)
    OP_63(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_DAA',
    )

    Jump('loc_F84')

    def _loc_DAA(): pass

    label('loc_DAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_E8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E09',
    )

    ChrTalk(
        0x00FE,
        (
            '鲁伊他们是战后\n',
            '才出生的一代嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能的话真不想\n',
            '让他们有这种遭遇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E87')

    def _loc_E09(): pass

    label('loc_E09')

    ChrTalk(
        0x00FE,
        (
            '托付给酒馆的\n',
            '鲁伊真令人担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他好像看到了龙的样子，\n',
            '变得非常胆怯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不想让那孩子\n',
            '留下这么可怕的回忆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_E87(): pass

    label('loc_E87')

    Jump('loc_F84')

    def _loc_E8A(): pass

    label('loc_E8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_F84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EE1',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏了阿加特\n',
            '才防止了火势扩大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到他竟然\n',
            '用剑砍倒大树。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F84')

    def _loc_EE1(): pass

    label('loc_EE1')

    ChrTalk(
        0x00FE,
        (
            '正在果园进行灭火的时候\n',
            '阿加特突然赶来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用那巨大的剑\n',
            '砍倒了大树。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏有他，\n',
            '火势没有再扩大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不、不过实在是太可怕了，\n',
            '都被吓的腿软了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_F84(): pass

    label('loc_F84')

    TalkEnd(0x000A)

    Return()

# id: 0x000E offset: 0xF88
@scena.Code('func_0E_F88')
def func_0E_F88():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_F95',
    )

    Jump('loc_104D')

    def _loc_F95(): pass

    label('loc_F95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_F9F',
    )

    Jump('loc_104D')

    def _loc_F9F(): pass

    label('loc_F9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_104D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_FDE',
    )

    ChrTalk(
        0x00FE,
        (
            '好过分……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果树园被弄得乱七八糟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104D')

    def _loc_FDE(): pass

    label('loc_FDE')

    ChrTalk(
        0x00FE,
        (
            '好过分……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果树园被弄得乱七八糟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连贝斯卡的\n',
            '拖拉机都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶的龙……\n',
            '绝对饶不了你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_104D(): pass

    label('loc_104D')

    TalkEnd(0x000D)

    Return()

# id: 0x000F offset: 0x1051
@scena.Code('func_0F_1051')
def func_0F_1051():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_106E',
    )

    Call(0, 0x0015)

    def _loc_106E(): pass

    label('loc_106E')

    OP_6D(-1780, 0, 9660, 0)
    OP_67(0, 7460, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(171000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1220, 0, 7010, 0)
    SetChrPos(0x0107, -2340, 0, 6850, 0)
    SetChrPos(0x00F8, -1430, 0, 5450, 0)
    SetChrPos(0x00F9, -2520, 0, 5280, 0)

    @scena.Lambda('lambda_10F5')
    def lambda_10F5():
        OP_8E(0x00FE, -1220, 0, 11010, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_10F5)

    Sleep(100)

    @scena.Lambda('lambda_1115')
    def lambda_1115():
        OP_8E(0x00FE, -2340, 0, 10850, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_1115)

    Sleep(100)

    @scena.Lambda('lambda_1135')
    def lambda_1135():
        OP_8E(0x00FE, -1430, 0, 9450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_1135)

    Sleep(100)

    @scena.Lambda('lambda_1155')
    def lambda_1155():
        OP_8E(0x00FE, -2520, 0, 9280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_1155)

    OP_C8(0x0200, 0x0046, 'C_PLAC15._CH', 0x01, 0x07D0)
    ShowPlaceName('拉文努村')
    FadeIn(2000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0101, 45, 400)

    ChrTalk(
        0x0101,
        (
            '#0010301003V#1020F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11E1')
    def lambda_11E1():
        OP_6D(20180, 0, 8950, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11E1)

    @scena.Lambda('lambda_11F9')
    def lambda_11F9():
        OP_67(0, 11500, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11F9)

    @scena.Lambda('lambda_1211')
    def lambda_1211():
        OP_6B(2200, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1211)

    @scena.Lambda('lambda_1221')
    def lambda_1221():
        OP_6C(30000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1221)

    @scena.Lambda('lambda_1231')
    def lambda_1231():
        OP_6E(412, 10000)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_1231)

    OP_8C(0x0101, 90, 400)

    @scena.Lambda('lambda_1248')
    def lambda_1248():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1248)

    Sleep(100)

    @scena.Lambda('lambda_125B')
    def lambda_125B():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_125B)

    Sleep(100)

    @scena.Lambda('lambda_126E')
    def lambda_126E():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_126E)

    WaitForThreadExit(0x0101, 0x0002)
    Sleep(2000)

    SetChrPos(0x0101, 8930, 0, 9620, 90)
    SetChrPos(0x0107, 8540, 0, 10360, 90)
    SetChrPos(0x00F8, 9090, 0, 8720, 90)
    SetChrPos(0x00F9, 8170, 0, 11260, 90)
    Fade(500)
    OP_6D(9120, 0, 10270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010301004V#1026F#6P这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301005V#065F#6P好、好过分……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13D6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301006V#022F#6P……总之，先找到\n',
            '给我们联络的村长吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030301007V他应该知道龙和\n',
            '阿加特的去向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C5')

    def _loc_13D6(): pass

    label('loc_13D6')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1451',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301008V#043F#6P……总之，先找到\n',
            '给我们联络的村长吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060301009V他应该知道龙和\n',
            '阿加特的去向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C5')

    def _loc_1451(): pass

    label('loc_1451')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14C5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301010V#032F#6P总之先找到\n',
            '给我们联络的村长吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040301011V他应该知道龙和\n',
            '阿加特的去向吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14C5(): pass

    label('loc_14C5')

    ChrTalk(
        0x0101,
        (
            '#0010301012V#1003F#6P嗯……对呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A14)
    OP_28(0x0094, 0x01, 0x0002)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0010 offset: 0x14FD
@scena.Code('func_10_14FD')
def func_10_14FD():
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
        'loc_151E',
    )

    Call(0, 0x0015)
    FadeIn(0, 0)
    Sleep(200)

    def _loc_151E(): pass

    label('loc_151E')

    Fade(1000)
    OP_6D(25120, -4000, 16950, 0)
    OP_67(0, 6370, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 26060, -4000, 17030, 270)
    SetChrPos(0x0107, 26140, -4000, 15780, 270)
    SetChrPos(0x00F8, 27550, -4000, 16800, 270)
    SetChrPos(0x00F9, 27620, -4000, 15500, 270)
    OP_8C(0x0008, 270, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010301013V#1002F#4P村长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    OP_63(0x0008)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#1180301014V#5P噢……你们是那时的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301015V#5P从柏斯市的协会\n',
            '特地来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16BF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301016V#020F#4P嗯嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301017V#1004F#4P我们的事，\n',
            '您还记得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_170F')

    def _loc_16BF(): pass

    label('loc_16BF')

    ChrTalk(
        0x0101,
        (
            '#0010301018V#1004F#4P嗯，是这样的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301019V我们的事，\n',
            '您还记得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_170F(): pass

    label('loc_170F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17C1',
    )

    FadeOut(300, 0, 100)

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
            TXT(0x00, '【◇前篇完成了山道的魔兽剿灭】\n'),
            TXT(0x01, '【◇前篇没完成山道的魔兽剿灭】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_17A8'),
        (0x00000001, 'loc_17B0'),
        (-1, 'loc_17B8'),
    )

    def _loc_17A8(): pass

    label('loc_17A8')

    OP_28(0x000E, 0x04, 0x10)

    Jump('loc_17B8')

    def _loc_17B0(): pass

    label('loc_17B0')

    OP_28(0x000E, 0x03, 0x10)

    Jump('loc_17B8')

    def _loc_17B8(): pass

    label('loc_17B8')

    FadeIn(300, 0)

    def _loc_17C1(): pass

    label('loc_17C1')

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_183B',
    )

    ChrTalk(
        0x0008,
        (
            '#1180301020V#5P啊啊、你们帮忙剿灭魔兽和解决了\n',
            '那次的空贼事件嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301021V#5P怎么可能会忘记呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_189C')

    def _loc_183B(): pass

    label('loc_183B')

    ChrTalk(
        0x0008,
        (
            '#1180301022V#5P啊啊、空贼事件的时候\n',
            '连军队都来了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301021V#5P怎么可能会忘记呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_189C(): pass

    label('loc_189C')

    ChrTalk(
        0x0101,
        (
            '#0010280504V#1025F#4P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301025V#1020F先、先不说这个了！\n',
            '龙跑到哪儿去了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301026V#063F#6P还、还有阿加特哥哥\n',
            '去哪里了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301027V#5P唔，唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301028V#5P烧毁了果树园之后\n',
            '龙就飞到北方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301029V#5P就在那之后、阿加特突然出现\n',
            '帮忙灭火……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301030V#5P可是火灭了之后，不知何时\n',
            '他就不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301031V#065F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301032V#1015F#4P会不会是\n',
            '去她妹妹那里了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301033V她住在村子里吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301034V#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301035V#5P是吗……\n',
            '阿加特是这么说的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301036V#1026F#4P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301037V#065F#6P那个那个……\n',
            '是怎么回事～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301038V#5P之前我确认过了，阿加特\n',
            '不在米夏身边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301039V#5P当然，他也没回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 1, 0x1A81)),
            Expr.Return,
        ),
        'loc_1D3B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010301040V#1015F#4P这、这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301041V#1007F那果然\n',
            '是去追龙了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010301042V#1020F#4P（等、等一下……！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301043V（米夏……\n',
            '　记得是刚刚看到的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070301044V#064F#6P怎么了，姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x0107, 600)

    ChrTalk(
        0x0101,
        (
            '#0010301045V#1016F#2P不、不，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301046V#1003F（总、总之，\n',
            '　应该先找到阿加特……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)
    OP_8C(0x0107, 270, 400)

    Jump('loc_1D8F')

    def _loc_1D3B(): pass

    label('loc_1D3B')

    ChrTalk(
        0x0101,
        (
            '#0010301040V#1015F#4P这、这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301048V#1007F那果然\n',
            '是去追龙了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D8F(): pass

    label('loc_1D8F')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1DEE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301049V#022F#4P这边往北……\n',
            '是空贼们藏着定期船的废坑方向吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E33')

    def _loc_1DEE(): pass

    label('loc_1DEE')

    ChrTalk(
        0x0103,
        (
            '#0030301050V#022F#4P这边往北……\n',
            '是特务兵作为基地的废坑方向吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E33(): pass

    label('loc_1E33')

    Jump('loc_1ED7')

    def _loc_1E36(): pass

    label('loc_1E36')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E86',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301051V#032F#4P根据王国地图，北边\n',
            '好像有连续的山道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ED7')

    def _loc_1E86(): pass

    label('loc_1E86')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ED7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301052V#042F#4P这边往北……\n',
            '是曾经有七耀石矿山的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ED7(): pass

    label('loc_1ED7')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F25',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301053V#070F#4P喔……老人家。\n',
            '有什么可以帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FBE')

    def _loc_1F25(): pass

    label('loc_1F25')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F71',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301054V#043F#4P那个……现在\n',
            '有什么可以帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FBE')

    def _loc_1F71(): pass

    label('loc_1F71')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FBE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301055V#030F#4P呼……老人家。\n',
            '还有地方需要人手的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FBE(): pass

    label('loc_1FBE')

    ChrTalk(
        0x0008,
        (
            '#1180301056V#5P啊啊，不必费心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301057V#5P火总算是扑灭了，\n',
            '现在就剩收拾善后了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301058V#5P比起这个……\n',
            '阿加特更重要，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1180301059V#5P他的表情看起来相当沉重，\n',
            '不知道会做出什么乱来的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301060V#1002F#4P明、明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 135, 500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010301061V#1005F#5P大家，赶快\n',
            '去北边山道找找吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 500)

    ChrTalk(
        0x0107,
        (
            '#0070301062V#062F#3P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A15)
    OP_28(0x0094, 0x01, 0x0004)
    OP_28(0x0094, 0x01, 0x0008)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0011 offset: 0x214E
@scena.Code('func_11_214E')
def func_11_214E():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    OP_6D(18470, -4000, 12420, 0)
    OP_67(0, 13920, -10000, 0)
    OP_6B(4470, 0)
    OP_6C(317000, 0)
    OP_6E(255, 0)
    OP_12(0x00007D00, 0x0003D090, 0x00000000)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_21DC')
    def lambda_21DC():
        OP_6D(-16410, -4000, 57810, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_21DC)

    OP_6C(298000, 12000)

    @scena.Lambda('lambda_21FD')
    def lambda_21FD():
        OP_6E(230, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21FD)

    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1210._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x2225
@scena.Code('func_12_2225')
def func_12_2225():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 3, 0x1A1B)),
            Expr.Return,
        ),
        'loc_254A',
    )

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
        'loc_224D',
    )

    Call(0, 0x0016)
    FadeIn(0, 0)
    Sleep(200)

    def _loc_224D(): pass

    label('loc_224D')

    ChrTalk(
        0x0101,
        (
            '#0010301502V#1015F（嗯，姑且算是给提妲\n',
            '　传了话，不过……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301503V（还有什么事没做吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

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
            TXT(0x00, '【回柏斯市】\n'),
            TXT(0x01, '【还不能回去】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2334',
    )

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Jump('loc_2547')

    def _loc_2334(): pass

    label('loc_2334')

    Fade(1000)
    OP_6D(-2410, 0, 7020, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -2130, 0, 7650, 180)
    SetChrPos(0x00F7, -1120, 0, 6000, 0)
    SetChrPos(0x00F8, -2480, 0, 5960, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2401',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301504V#020F#6P好了、太阳也下山了，\n',
            '差不多该回柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24A6')

    def _loc_2401(): pass

    label('loc_2401')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2455',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301505V#070F#6P好了、太阳也下山了，\n',
            '差不多该回柏斯了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24A6')

    def _loc_2455(): pass

    label('loc_2455')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24A6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301506V#030F#6P好了、太阳也下山了，\n',
            '差不多该回柏斯了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24A6(): pass

    label('loc_24A6')

    ChrTalk(
        0x0101,
        (
            '#0010301507V#1006F#2P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301508V晚上会收到将军的联络，\n',
            '要赶快返回柏斯才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1104._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2547(): pass

    label('loc_2547')

    Jump('loc_27CD')

    def _loc_254A(): pass

    label('loc_254A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_27CD',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Ez,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2688',
    )

    ChrTurnDirection(0x0101, 0x0000, 400)

    ChrTalk(
        0x0101,
        (
            '#0010301509V#1004F啊，回柏斯之前\n',
            '要跟提妲说一声才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x0101, 400)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000002, 'loc_25C1'),
        (0x00000007, 'loc_25F2'),
        (0x00000003, 'loc_2623'),
        (0x00000004, 'loc_2654'),
        (-1, 'loc_2685'),
    )

    def _loc_25C1(): pass

    label('loc_25C1')

    ChrTalk(
        0x0103,
        (
            '#0030301510V#023F西北有间\n',
            '小小的民房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2685')

    def _loc_25F2(): pass

    label('loc_25F2')

    ChrTalk(
        0x0108,
        (
            '#0080301511V#073F西北有间\n',
            '小小的民房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2685')

    def _loc_2623(): pass

    label('loc_2623')

    ChrTalk(
        0x0104,
        (
            '#0040301512V#033F西北有间\n',
            '小小的民房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2685')

    def _loc_2654(): pass

    label('loc_2654')

    ChrTalk(
        0x0105,
        (
            '#0060301513V#044F西北有间\n',
            '小小的民房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2685')

    def _loc_2685(): pass

    label('loc_2685')

    Jump('loc_27AD')

    def _loc_2688(): pass

    label('loc_2688')

    ChrTurnDirection(0x0101, 0x0001, 400)

    ChrTalk(
        0x0101,
        (
            '#0010301509V#1004F啊，回柏斯之前\n',
            '要跟提妲说一声才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0001, 0x0101, 400)

    Switch(
        (
            (Expr.PushValueByIndex, 0xB),
            Expr.Return,
        ),
        (0x00000002, 'loc_26E9'),
        (0x00000007, 'loc_271A'),
        (0x00000003, 'loc_274B'),
        (0x00000004, 'loc_277C'),
        (-1, 'loc_27AD'),
    )

    def _loc_26E9(): pass

    label('loc_26E9')

    ChrTalk(
        0x0103,
        (
            '#0030301515V#020F西北有间\n',
            '小小的民房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27AD')

    def _loc_271A(): pass

    label('loc_271A')

    ChrTalk(
        0x0108,
        (
            '#0080301516V#070F西北有间\n',
            '小小的民房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27AD')

    def _loc_274B(): pass

    label('loc_274B')

    ChrTalk(
        0x0104,
        (
            '#0040301517V#030F西北有间\n',
            '小小的民房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27AD')

    def _loc_277C(): pass

    label('loc_277C')

    ChrTalk(
        0x0105,
        (
            '#0060301518V#040F西北有间\n',
            '小小的民房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27AD')

    def _loc_27AD(): pass

    label('loc_27AD')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_27CD(): pass

    label('loc_27CD')

    Return()

# id: 0x0013 offset: 0x27CE
@scena.Code('func_13_27CE')
def func_13_27CE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CD9',
    )

    EventBegin(0x00)
    Fade(500)
    SetChrPos(0x0101, 33350, 8000, 36400, 180)
    SetChrPos(0x0107, 33770, 8000, 37410, 180)
    SetChrPos(0x00F8, 32590, 8000, 37110, 180)
    SetChrPos(0x00F9, 33210, 8000, 38210, 180)
    OP_6D(33180, 8000, 36770, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 5, 0x1A15)),
            Expr.Return,
        ),
        'loc_2B92',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 1, 0x1A81)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A84',
    )

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９２年\n',
            '由于战火而失去的\n',
            '６个善良的灵魂，长眠与此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雷夫、阿贝尔、尼高尔、\n',
            '维姆、依蕾娜、米夏。\n',
            '愿你们在女神的怀抱中得到安宁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010301065V#1020F#4P（等、等一下……！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301066V（米夏……\n',
            '　刚才村长说过的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070301067V#064F#6P怎么了，姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x0107, 600)

    ChrTalk(
        0x0101,
        (
            '#0010301068V#1016F#5P不，不，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301069V#1003F（虽、虽然在意……\n',
            '　但现在要先追上阿加特才行……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A81)

    Jump('loc_2B8F')

    def _loc_2A84(): pass

    label('loc_2A84')

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９２年\n',
            '由于战火而失去的\n',
            '６个善良的灵魂，长眠与此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雷夫、阿贝尔、尼高尔、\n',
            '维姆、依蕾娜、米夏。\n',
            '愿你们在女神的怀抱中得到安宁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010301070V#1003F#4P（虽、虽然在意……\n',
            '　但现在要先追上阿加特才行……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B8F(): pass

    label('loc_2B8F')

    Jump('loc_2CCF')

    def _loc_2B92(): pass

    label('loc_2B92')

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９２年\n',
            '由于战火而失去的\n',
            '６个善良的灵魂，长眠与此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雷夫、阿贝尔、尼高尔、\n',
            '维姆、依蕾娜、米夏。\n',
            '愿你们在女神的怀抱中得到安宁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010301063V#1015F#6P（咦，米夏\n',
            '　好像在哪儿听说过……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301064V#1002F（……唔，不好！\n',
            '　要赶快找村长问话才行！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A81)
    def _loc_2CCF(): pass

    label('loc_2CCF')

    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Jump('loc_2DA4')

    def _loc_2CD9(): pass

    label('loc_2CD9')

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９２年\n',
            '由于战火而失去的\n',
            '６个善良的灵魂，长眠与此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雷夫、阿贝尔、尼高尔、\n',
            '维姆、依蕾娜、米夏。\n',
            '愿你们在女神的怀抱中得到安宁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)
    def _loc_2DA4(): pass

    label('loc_2DA4')

    Return()

# id: 0x0014 offset: 0x2DA5
@scena.Code('func_14_2DA5')
def func_14_2DA5():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0015 offset: 0x2DEB
@scena.Code('func_15_2DEB')
def func_15_2DEB():
    FadeOut(0, 0, -1)
    OP_6D(-32830, 0, 10760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0x00000000, 'loc_2EA2'),
        (0x00000001, 'loc_2EA8'),
        (-1, 'loc_2EAE'),
    )

    def _loc_2EA2(): pass

    label('loc_2EA2')

    OP_A2(0x1200)

    Jump('loc_2EAE')

    def _loc_2EA8(): pass

    label('loc_2EA8')

    OP_A2(0x1201)

    Jump('loc_2EAE')

    def _loc_2EAE(): pass

    label('loc_2EAE')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0006,
            0x00FF,
            0x00FF,
        ),
        (
            0x0002,
            0x0003,
            0x0004,
            0x0007,
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0016 offset: 0x2EE8
@scena.Code('func_16_2EE8')
def func_16_2EE8():
    FadeOut(0, 0, -1)
    OP_6D(-32830, 0, 10760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0x00000000, 'loc_2F9F'),
        (0x00000001, 'loc_2FA5'),
        (-1, 'loc_2FAB'),
    )

    def _loc_2F9F(): pass

    label('loc_2F9F')

    OP_A2(0x1200)

    Jump('loc_2FAB')

    def _loc_2FA5(): pass

    label('loc_2FA5')

    OP_A2(0x1201)

    Jump('loc_2FAB')

    def _loc_2FAB(): pass

    label('loc_2FAB')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x00FF,
            0x00FF,
        ),
        (
            0x0002,
            0x0003,
            0x0004,
            0x0007,
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0017 offset: 0x2FE3
@scena.Code('func_17_2FE3')
def func_17_2FE3():
    SetPlaceName(0x002E)

    Return()

# id: 0x0018 offset: 0x2FE7
@scena.Code('func_18_2FE7')
def func_18_2FE7():
    SetPlaceName(0x002D)

    Return()

# id: 0x0019 offset: 0x2FEB
@scena.Code('func_19_2FEB')
def func_19_2FEB():
    SetPlaceName(0x002F)

    Return()

# id: 0x001A offset: 0x2FEF
@scena.Code('func_1A_2FEF')
def func_1A_2FEF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 3, 0x1A1B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_31AC',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_304D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010301519V#1015F这边已经没事了。\n',
            '得赶快去阿加特家里才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318C')

    def _loc_304D(): pass

    label('loc_304D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_309C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301520V#020F去废坑那边也无济于事。\n',
            '赶快去阿加特家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318C')

    def _loc_309C(): pass

    label('loc_309C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30E9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301521V#040F废坑方向已经没事了。\n',
            '赶快去阿加特家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318C')

    def _loc_30E9(): pass

    label('loc_30E9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_313A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301522V#030F这边已经没事了。\n',
            '赶快去看看阿加特的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_318C')

    def _loc_313A(): pass

    label('loc_313A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_318C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301523V#070F废坑这边已经没事了。\n',
            '赶快去看看阿加特的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_318C(): pass

    label('loc_318C')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_31AC(): pass

    label('loc_31AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 3, 0x1A1B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3365',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3208',
    )

    ChrTalk(
        0x0101,
        (
            '#0010301524V#1016F这边是废坑方向吧。\n',
            '回柏斯得去南门才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3345')

    def _loc_3208(): pass

    label('loc_3208')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_325B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301525V#020F这边的出口是废坑那边。\n',
            '回柏斯的话要去南门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3345')

    def _loc_325B(): pass

    label('loc_325B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32A8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301526V#040F这边是废坑方向吧。\n',
            '回柏斯得去南门才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3345')

    def _loc_32A8(): pass

    label('loc_32A8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32F9',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301527V#030F这边是废坑方向。\n',
            '回柏斯得从南门出去才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3345')

    def _loc_32F9(): pass

    label('loc_32F9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3345',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301528V#070F这边是废坑那边吧。\n',
            '回柏斯的话要去南门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3345(): pass

    label('loc_3345')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_3365(): pass

    label('loc_3365')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 4, 0x1A14)),
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 5, 0x1A15)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3569',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33C9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010301529V#1002F没时间四处闲逛了吧。\n',
            '先得去找村长了解情况才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3549')

    def _loc_33C9(): pass

    label('loc_33C9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_341E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301530V#022F没时间四处闲逛了。\n',
            '先得去找村长了解情况才行哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3549')

    def _loc_341E(): pass

    label('loc_341E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3465',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301531V#042F没时间绕道了吧。\n',
            '赶快去找村长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3549')

    def _loc_3465(): pass

    label('loc_3465')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34B0',
    )

    ChrTalk(
        0x0104,
        (
            '#0040301532V#032F没时间四处闲逛了吧。\n',
            '赶快去找村长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3549')

    def _loc_34B0(): pass

    label('loc_34B0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34FF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070301533V#063F四处闲逛可不行哦。\n',
            '……先要找到村长才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3549')

    def _loc_34FF(): pass

    label('loc_34FF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3549',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301534V#072F没时间四处闲逛了吧。\n',
            '先得去找村长问话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3549(): pass

    label('loc_3549')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_3569(): pass

    label('loc_3569')

    Return()

# id: 0x001B offset: 0x356A
@scena.Code('func_1B_356A')
def func_1B_356A():
    ClearMapFlags(0x02000000)

    Return()

# id: 0x001C offset: 0x3570
@scena.Code('func_1C_3570')
def func_1C_3570():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_35A8')
    def lambda_35A8():
        OP_6D(35190, -3850, 5430, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_35A8)

    @scena.Lambda('lambda_35C0')
    def lambda_35C0():
        OP_6B(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_35C0)

    @scena.Lambda('lambda_35D0')
    def lambda_35D0():
        OP_6C(225000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_35D0)

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
        'loc_3657',
    )

    OP_C0(0x0E, 0x0000000A, 0x000088F4, 0xFFFFF0F6, 0x00002044, 0x000000B4, 0x000088C2, 0xFFFFEF98, 0x00001446)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_3666')

    def _loc_3657(): pass

    label('loc_3657')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3666',
    )

    EventEnd(0x01)

    def _loc_3666(): pass

    label('loc_3666')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
