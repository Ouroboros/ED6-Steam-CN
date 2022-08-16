import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1103_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1103   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1103.x'
    header.mapIndex       = 49
    header.bgm            = 30
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
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT27/CH04540._CH', 'ED6_DT27/CH04540P._CP'),
        ('ED6_DT27/CH04542._CH', 'ED6_DT27/CH04542P._CP'),
        ('ED6_DT27/CH04548._CH', 'ED6_DT27/CH04548P._CP'),
        ('ED6_DT27/CH04546._CH', 'ED6_DT27/CH04546P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00153._CH', 'ED6_DT07/CH00153P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT06/CH20137._CH', 'ED6_DT06/CH20137P._CP'),
        ('ED6_DT26/CH20343._CH', 'ED6_DT26/CH20343P._CP'),
        ('ED6_DT26/CH20345._CH', 'ED6_DT26/CH20345P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT26/CH20346._CH', 'ED6_DT26/CH20346P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT07/CH00326._CH', 'ED6_DT07/CH00326P._CP'),
        ('ED6_DT26/CH20362._CH', 'ED6_DT26/CH20362P._CP'),
        ('ED6_DT26/CH20340._CH', 'ED6_DT26/CH20340P._CP'),
        ('ED6_DT07/CH00158._CH', 'ED6_DT07/CH00158P._CP'),
        ('ED6_DT07/CH00159._CH', 'ED6_DT07/CH00159P._CP'),
        ('ED6_DT26/CH20207._CH', 'ED6_DT26/CH20207P._CP'),
        ('ED6_DT26/CH20364._CH', 'ED6_DT26/CH20364P._CP'),
        ('ED6_DT26/CH20363._CH', 'ED6_DT26/CH20363P._CP'),
        ('ED6_DT26/CH20243._CH', 'ED6_DT26/CH20243P._CP'),
        ('ED6_DT26/CH20347._CH', 'ED6_DT26/CH20347P._CP'),
        ('ED6_DT26/CH20348._CH', 'ED6_DT26/CH20348P._CP'),
        ('ED6_DT27/CH04541._CH', 'ED6_DT27/CH04541P._CP'),
        ('ED6_DT27/CH04547._CH', 'ED6_DT27/CH04547P._CP'),
        ('ED6_DT27/CH04545._CH', 'ED6_DT27/CH04545P._CP'),
        ('ED6_DT06/CH20138._CH', 'ED6_DT06/CH20138P._CP'),
    ]

# id: 0x10001 offset: 0x1C2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '剑帝莱维',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '摩尔根将军',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '折断的刀锋',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古代龙',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '龙',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '警备艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
            name                = ' ',
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
    )

# id: 0x10002 offset: 0x602
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x602
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x602
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x602
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_621',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_29_6EC4)

    Jump('loc_66B')

    def _loc_621(): pass

    label('loc_621')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 1, 0x1A19)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_651',
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006B, 'loc_639'),
        (-1, 'loc_64E'),
    )

    def _loc_639(): pass

    label('loc_639')

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0D_304B)

    Jump('loc_64E')

    def _loc_64E(): pass

    label('loc_64E')

    Jump('loc_66B')

    def _loc_651(): pass

    label('loc_651')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 7, 0x1A17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66B',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_08_161D)

    def _loc_66B(): pass

    label('loc_66B')

    Return()

# id: 0x0001 offset: 0x66C
@scena.Code('func_01_66C')
def func_01_66C():
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_10(0x00, 0x00)

    Return()

# id: 0x0002 offset: 0x67A
@scena.Code('func_02_67A')
def func_02_67A():
    @scena.Lambda('lambda_0680')
    def lambda_0680():
        CameraMove(-2940, 0, 5940, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0680)

    @scena.Lambda('lambda_0698')
    def lambda_0698():
        OP_6C(315000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0698)

    @scena.Lambda('lambda_06A8')
    def lambda_06A8():
        CameraSetDistance(3500, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06A8)

    @scena.Lambda('lambda_06B8')
    def lambda_06B8():
        OP_6E(262, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_06B8)

    ChrSetFlags(0x0009, 0x1000)
    ChrSetChipByIndex(0x0009, 10)

    @scena.Lambda('lambda_06D2')
    def lambda_06D2():
        ChrWalkTo(0x00FE, -7290, 0, 8250, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_06D2)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 11)

    @scena.Lambda('lambda_06FC')
    def lambda_06FC():
        OP_99(0x00FE, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_06FC)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_0711')
    def lambda_0711():
        ChrJumpTo(0x00FE, -2590, 0, 5280, 1400, 12000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0711)

    Sleep(300)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_073E')
    def lambda_073E():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_073E)

    Sleep(100)

    OP_7C(0, 200, 3000, 100)
    PlayEffect(0x03, 0x01, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_07A3')
    def lambda_07A3():
        OP_99(0x00FE, 0x04, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_07A3)

    ChrJumpTo(0x0009, -3480, 0, 5580, 200, 5000)
    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_07D4')
    def lambda_07D4():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_07D4)

    @scena.Lambda('lambda_07E4')
    def lambda_07E4():
        ChrJumpTo(0x00FE, -1810, 0, 5090, 500, 8000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_07E4)

    Sleep(100)

    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_080F')
    def lambda_080F():
        ChrJumpTo(0x0008, 1270, 0, 4170, 200, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_080F)

    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 2)
    Sleep(200)

    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0009, 0x0002)
    ChrSetSubChip(0x0009, 0)
    WaitForThreadExit(0x0008, 0x0000)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 5)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_0876')
    def lambda_0876():
        OP_99(0x0008, 0x00, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0876)

    @scena.Lambda('lambda_0886')
    def lambda_0886():
        ChrJumpTo(0x0008, -90, 0, 4470, 200, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0886)

    Sleep(100)

    OP_7C(0, 200, 3000, 100)
    PlayEffect(0x03, 0x01, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_08F4')
    def lambda_08F4():
        OP_9E(0x00FE, 20, 0, 300, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_08F4)

    WaitForThreadExit(0x0008, 0x0000)
    ChrSetSubChip(0x0008, 7)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 24)

    @scena.Lambda('lambda_0927')
    def lambda_0927():
        OP_99(0x00FE, 0x00, 0x0E, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0927)

    Sleep(400)

    PlaySE(505, 0x00, 0x64)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_0949')
    def lambda_0949():
        ChrJumpTo(0x0008, 110, 0, 5710, 200, 9000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0949)

    @scena.Lambda('lambda_0967')
    def lambda_0967():
        ChrSetDirection(0x0008, 225, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0967)

    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)
    Sleep(200)

    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)

    @scena.Lambda('lambda_099B')
    def lambda_099B():
        OP_9E(0x00FE, 20, 0, 300, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_099B)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 6)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_09C4')
    def lambda_09C4():
        OP_99(0x0008, 0x00, 0x0A, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_09C4)

    Sleep(200)

    OP_7C(0, 200, 3000, 100)
    PlayEffect(0x03, 0x01, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)

    @scena.Lambda('lambda_0A24')
    def lambda_0A24():
        OP_9E(0x00FE, 20, 0, 300, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_0A24)

    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 4)
    WaitForThreadExit(0x0008, 0x0000)
    ChrSetSubChip(0x0008, 7)
    ChrClearFlags(0x0009, 0x0002)

    @scena.Lambda('lambda_0A5C')
    def lambda_0A5C():
        ChrSetDirection(0x0009, 45, 0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A5C)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 11)
    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_0A7E')
    def lambda_0A7E():
        OP_99(0x00FE, 0x00, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A7E)

    @scena.Lambda('lambda_0A8E')
    def lambda_0A8E():
        ChrJumpTo(0x0009, -680, 0, 5320, 200, 8000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A8E)

    Sleep(200)

    PlaySE(163, 0x00, 0x64)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_0AC8')
    def lambda_0AC8():
        ChrJumpTo(0x0008, 5050, 0, 3990, 600, 9000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0AC8)

    Sleep(200)

    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_0AF5')
    def lambda_0AF5():
        CameraMove(4240, 0, 3920, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AF5)

    @scena.Lambda('lambda_0B0D')
    def lambda_0B0D():
        OP_6C(332000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B0D)

    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x0009, 3930, 0, 1240, 500, 6000)
    ChrSetDirection(0x0009, 0, 0)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    ChrTurnDirection(0x0008, 0x0009, 0)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 3)
    Sleep(300)

    ChrSetFlags(0x0009, 0x0020)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0008, 0x1000)
    ChrSetFlags(0x0009, 0x1000)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0009, 10)

    @scena.Lambda('lambda_0B90')
    def lambda_0B90():
        ChrJumpTo(0x00FE, 4500, 0, 2110, 300, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B90)

    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_0BB6')
    def lambda_0BB6():
        ChrJumpTo(0x00FE, 4790, 0, 3020, 300, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BB6)

    Sleep(200)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 8)
    WaitForThreadExit(0x0008, 0x0001)
    ChrClearFlags(0x0008, 0x1000)
    ChrClearFlags(0x0009, 0x1000)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetChipByIndex(0x0009, 14)

    @scena.Lambda('lambda_0C01')
    def lambda_0C01():
        OP_9E(0x00FE, 20, 0, 4000, 2500)
        Yield()

        Jump('lambda_0C01')

    DispatchAsync2(0x0009, 0x0003, lambda_0C01)

    Sleep(100)

    @scena.Lambda('lambda_0C23')
    def lambda_0C23():
        OP_9E(0x00FE, 20, 0, 4000, 2500)
        Yield()

        Jump('lambda_0C23')

    DispatchAsync2(0x0008, 0x0003, lambda_0C23)

    Sleep(500)

    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    Return()

# id: 0x0003 offset: 0xC56
@scena.Code('func_03_C56')
def func_03_C56():
    ChrSetChipByIndex(0x0008, 33)
    ChrSetSubChip(0x0008, 1)

    @scena.Lambda('lambda_0C66')
    def lambda_0C66():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0C66)

    @scena.Lambda('lambda_0C80')
    def lambda_0C80():
        ChrJumpTo(0x00FE, 1140, 0, 260, 500, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C80)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_0CB2')
    def lambda_0CB2():
        ChrJumpTo(0x00FE, 3880, 0, -940, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CB2)

    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 6)

    Return()

# id: 0x0004 offset: 0xCDF
@scena.Code('func_04_CDF')
def func_04_CDF():
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetSubChip(0x0008, 0)

    Return()

# id: 0x0005 offset: 0xCF4
@scena.Code('func_05_CF4')
def func_05_CF4():
    WaitForThreadExit(0x0009, 0x0001)
    Sleep(400)

    ChrSetChipByIndex(0x0009, 10)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_0D0E')
    def lambda_0D0E():
        ChrSetDirection(0x00FE, 110, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_0D0E)

    Return()

# id: 0x0006 offset: 0xD17
@scena.Code('func_06_D17')
def func_06_D17():
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_0D2C')
    def lambda_0D2C():
        CameraMove(-1800, 0, 6230, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D2C)

    @scena.Lambda('lambda_0D44')
    def lambda_0D44():
        OP_67(0, 4450, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D44)

    @scena.Lambda('lambda_0D5C')
    def lambda_0D5C():
        CameraSetDistance(2029, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D5C)

    ChrSetFlags(0x0009, 0x1000)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_0D7B')
    def lambda_0D7B():
        ChrWalkTo(0x00FE, -6590, 0, 8150, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D7B)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x0009, 3)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0DAF')
    def lambda_0DAF():
        ChrJumpTo(0x00FE, -2050, 0, 5690, 1400, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0DAF)

    Sleep(200)

    @scena.Lambda('lambda_0DD2')
    def lambda_0DD2():
        OP_99(0x00FE, 0x03, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0DD2)

    Sleep(100)

    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 2)
    ChrSetDirection(0x0008, 332, 0)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x00C8)

    @scena.Lambda('lambda_0E00')
    def lambda_0E00():
        ChrJumpTo(0x00FE, -1200, 0, 140, 200, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E00)

    Sleep(150)

    ChrSetFlags(0x0009, 0x0800)
    PlaySE(85, 0x00, 0x5A)
    PlayEffect(0x12, 0xFF, 0x00FF, -380, -1000, 4830, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 600, 3000, 100)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 32)
    ChrSetSubChip(0x0008, 1)
    ChrSetDirection(0x0008, 20, 0)
    Sleep(200)

    @scena.Lambda('lambda_0E93')
    def lambda_0E93():
        CameraMove(370, 0, 2040, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0E93)

    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 4)
    ChrSetDirection(0x0009, 200, 0)

    @scena.Lambda('lambda_0EBC')
    def lambda_0EBC():
        OP_99(0x00FE, 0x04, 0x0E, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0EBC)

    @scena.Lambda('lambda_0ECC')
    def lambda_0ECC():
        ChrJumpTo(0x00FE, -1260, 0, 1440, 200, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0ECC)

    CreateThread(0x0009, 0x00, 0x00, func_05_CF4)
    Sleep(200)

    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_0F00')
    def lambda_0F00():
        ChrSetDirection(0x00FE, 330, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0F00)

    @scena.Lambda('lambda_0F0E')
    def lambda_0F0E():
        ChrJumpTo(0x00FE, 1490, 0, -2360, 500, 3500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F0E)

    Sleep(200)

    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0F40')
    def lambda_0F40():
        ChrSetDirection(0x00FE, 280, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0F40)

    @scena.Lambda('lambda_0F4E')
    def lambda_0F4E():
        ChrJumpTo(0x00FE, 4360, 0, 200, 500, 3500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F4E)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_0F71')
    def lambda_0F71():
        CameraMove(-2540, 0, 3240, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0F71)

    @scena.Lambda('lambda_0F89')
    def lambda_0F89():
        CameraSetDistance(1930, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F89)

    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 3)

    @scena.Lambda('lambda_0FB0')
    def lambda_0FB0():
        ChrJumpTo(0x00FE, 100, 0, 880, 500, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FB0)

    Sleep(150)

    @scena.Lambda('lambda_0FD3')
    def lambda_0FD3():
        OP_99(0x00FE, 0x03, 0x06, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0FD3)

    Sleep(100)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x0009, 1000, 500, -500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x0009, 0x03)
    ChrClearFlags(0x0009, 0x0800)
    ChrSetDirection(0x0009, 110, 0)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_1051')
    def lambda_1051():
        ChrMoveTo(0x00FE, -3200, 0, 2070, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1051)

    @scena.Lambda('lambda_106C')
    def lambda_106C():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_106C)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 0)
    Sleep(100)

    @scena.Lambda('lambda_109A')
    def lambda_109A():
        CameraMove(-4210, 0, 3570, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_109A)

    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 2)

    @scena.Lambda('lambda_10BC')
    def lambda_10BC():
        ChrJumpTo(0x00FE, -4920, 0, 2660, 300, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_10BC)

    @scena.Lambda('lambda_10DA')
    def lambda_10DA():
        ChrMoveTo(0x00FE, -1800, 0, 1640, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_10DA)

    Sleep(100)

    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 1)
    PlaySE(132, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 3)
    Sleep(100)

    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 10)

    @scena.Lambda('lambda_112C')
    def lambda_112C():
        ChrMoveTo(0x00FE, -3690, 0, 2290, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_112C)

    Sleep(100)

    @scena.Lambda('lambda_114C')
    def lambda_114C():
        OP_99(0x00FE, 0x0A, 0x0E, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_114C)

    Sleep(100)

    @scena.Lambda('lambda_1161')
    def lambda_1161():
        CameraMove(-270, 0, 2070, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1161)

    @scena.Lambda('lambda_1179')
    def lambda_1179():
        CameraSetDistance(2029, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1179)

    OP_23(0x00D6)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x0008, -1000, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    CreateThread(0x0008, 0x00, 0x00, func_03_C56)
    Sleep(400)

    ChrClearFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_11F2')
    def lambda_11F2():
        ChrMoveTo(0x00FE, -870, 0, 1130, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11F2)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x0009, 3)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_1226')
    def lambda_1226():
        ChrJumpTo(0x00FE, 3290, 0, -950, 1500, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1226)

    Sleep(200)

    @scena.Lambda('lambda_1249')
    def lambda_1249():
        OP_99(0x00FE, 0x03, 0x06, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1249)

    ChrSetChipByIndex(0x0008, 32)
    ChrSetSubChip(0x0008, 14)

    @scena.Lambda('lambda_1263')
    def lambda_1263():
        ChrMoveTo(0x00FE, 4270, 0, 1100, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1263)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(100)

    ChrSetFlags(0x0009, 0x0800)
    PlaySE(85, 0x00, 0x5A)
    PlayEffect(0x12, 0xFF, 0x00FF, 4830, -1000, -1240, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 600, 3000, 100)
    Sleep(100)

    @scena.Lambda('lambda_12DD')
    def lambda_12DD():
        CameraMove(2850, 0, 920, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_12DD)

    @scena.Lambda('lambda_12F5')
    def lambda_12F5():
        OP_6C(314000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12F5)

    ChrSetSubChip(0x0008, 15)
    Sleep(30)

    ChrSetDirection(0x0008, 200, 0)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_1320')
    def lambda_1320():
        OP_99(0x00FE, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1320)

    @scena.Lambda('lambda_1330')
    def lambda_1330():
        ChrMoveTo(0x00FE, 3980, 0, 60, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1330)

    Sleep(150)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x0009, 1000, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    ChrClearFlags(0x0009, 0x0800)
    ChrSetDirection(0x0009, 60, 0)
    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 9)

    @scena.Lambda('lambda_13B1')
    def lambda_13B1():
        ChrMoveTo(0x00FE, 4290, 0, -4870, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_13B1)

    @scena.Lambda('lambda_13CC')
    def lambda_13CC():
        OP_9E(0x00FE, 40, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_13CC)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0009, 0x0002)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_13FA')
    def lambda_13FA():
        ChrJumpTo(0x00FE, 4730, 0, 2190, 200, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_13FA)

    CreateThread(0x0008, 0x00, 0x00, func_04_CDF)

    @scena.Lambda('lambda_141F')
    def lambda_141F():
        CameraMove(4240, 0, 3920, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_141F)

    @scena.Lambda('lambda_1437')
    def lambda_1437():
        OP_6C(332000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1437)

    @scena.Lambda('lambda_1447')
    def lambda_1447():
        CameraSetDistance(2130, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1447)

    @scena.Lambda('lambda_1457')
    def lambda_1457():
        OP_67(0, 5080, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1457)

    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x0009, 2)
    ChrSetDirection(0x0009, 20, 0)

    @scena.Lambda('lambda_1480')
    def lambda_1480():
        ChrJumpTo(0x00FE, 4500, 0, 2110, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1480)

    @scena.Lambda('lambda_149E')
    def lambda_149E():
        OP_99(0x00FE, 0x02, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_149E)

    Sleep(350)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0xFF, 0x0008, 0, 800, -1000, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    TerminateThread(0x0009, 0x02)
    TerminateThread(0x0008, 0x00)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0009, 34)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_151A')
    def lambda_151A():
        ChrMoveTo(0x00FE, 4890, 0, 3080, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_151A)

    @scena.Lambda('lambda_1535')
    def lambda_1535():
        OP_9E(0x00FE, 60, 0, 500, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1535)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x02)

    @scena.Lambda('lambda_1558')
    def lambda_1558():
        OP_9E(0x00FE, 15, 4294967288, 0, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_1558)

    @scena.Lambda('lambda_1572')
    def lambda_1572():
        OP_9E(0x00FE, 15, 4294967288, 0, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1572)

    CreateThread(0x0008, 0x00, 0x00, func_07_159C)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(2000)

    Return()

# id: 0x0007 offset: 0x159C
@scena.Code('func_07_159C')
def func_07_159C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_161C',
    )

    PlayEffect(0x03, 0xFF, 0x00FF, 4760, 1100, 2720, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    PlayEffect(0x03, 0xFF, 0x00FF, 4700, 1200, 2700, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    Jump('func_07_159C')

    def _loc_161C(): pass

    label('loc_161C')

    Return()

# id: 0x0008 offset: 0x161D
@scena.Code('func_08_161D')
def func_08_161D():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-17960, 0, -9210, 0)
    OP_67(0, 8360, -10000, 0)
    CameraSetDistance(2740, 0)
    OP_6C(59000, 0)
    OP_6E(602, 0)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0008, -460, 0, 4800, 21)
    ChrClearFlags(0x0008, 0x0080)
    OP_72(0x0000, 0x0004)
    OP_CF(0x0019, 0x00, 'Frame127_FireEmitter')
    OP_A1(0x0018, 0x0000)
    ChrSetPos(0x0018, 12660, 0, 13410, 232)
    ChrSetFlags(0x0018, 0x0001)
    ChrClearFlags(0x0018, 0x0080)

    ExecExpressionWithValue(
        0x0018,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x07,
        (
            (Expr.PushLong, 0x1964),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x34,
        (
            (Expr.PushLong, 0x249F0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    LoadEffect(0x00, 'map\\\\mp015_00.eff')

    @scena.Lambda('lambda_1721')
    def lambda_1721():
        CameraMove(6450, 0, 10810, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1721)

    @scena.Lambda('lambda_1739')
    def lambda_1739():
        OP_67(0, 7880, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1739)

    FadeIn(2000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_6F(0x0000, 80)
    OP_70(0x0000, 120)
    Fade(500)
    CameraMove(990, 3620, 6360, 0)
    OP_67(0, 5670, -10000, 0)
    CameraSetDistance(2000, 0)
    OP_6C(356000, 0)
    OP_6E(580, 0)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    PlaySE(287, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 5)
    OP_70(0x0000, 55)
    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0140301085V#121F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 22)
    ChrSetSubChip(0x0008, 0)
    OP_99(0x0008, 0x00, 0x04, 1500)
    Sleep(500)

    PlaySE(145, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x0008, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_B0(0x0000, 0x1E)
    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_B0(0x0000, 0x0F)
    Fade(500)
    OP_6F(0x0000, 290)
    OP_70(0x0000, 300)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 300)
    OP_70(0x0000, 350)
    PlaySE(290, 0x00, 0x64)
    Sleep(1000)

    OP_72(0x0000, 0x0020)
    OP_B0(0x0000, 0x1E)
    OP_73(0x0000)
    OP_B0(0x0000, 0x0F)

    @scena.Lambda('lambda_18EA')
    def lambda_18EA():
        CameraMove(2140, 0, 8390, 3500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_18EA)

    @scena.Lambda('lambda_1902')
    def lambda_1902():
        OP_67(0, 5940, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1902)

    @scena.Lambda('lambda_191A')
    def lambda_191A():
        CameraSetDistance(2290, 3500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_191A)

    Fade(500)
    OP_23(0x0193)
    OP_6F(0x0000, 350)
    OP_70(0x0000, 435)
    OP_73(0x0000)
    CreateThread(0x0019, 0x00, 0x00, func_09_27BA)
    WaitForThreadExit(0x0008, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0008,
        (
            '#0140301086V#124F好……这样就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x04, 0x00, 1500)
    PlaySE(216, 0x00, 0x64)
    Sleep(750)

    ChrTalk(
        0x0008,
        (
            '#0140301087V#121F嗯、收集资料\n',
            '还需要一些时间吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301088V真是的，把这么麻烦的工作\n',
            '推给我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, -15470, 0, 11980, 90)
    ChrClearFlags(0x0009, 0x0080)

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0050301089V#4P……你说什么麻烦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_1A61')
    def lambda_1A61():
        CameraMove(-6950, 0, 9120, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1A61)

    @scena.Lambda('lambda_1A79')
    def lambda_1A79():
        OP_67(0, 5080, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1A79)

    @scena.Lambda('lambda_1A91')
    def lambda_1A91():
        CameraSetDistance(3020, 2500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1A91)

    @scena.Lambda('lambda_1AA1')
    def lambda_1AA1():
        OP_6C(332000, 2500)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1AA1)

    @scena.Lambda('lambda_1AB1')
    def lambda_1AB1():
        OP_6E(385, 2500)

        ExitThread()

    DispatchAsync(0x0018, 0x0002, lambda_1AB1)

    Sleep(500)

    ChrSetChipByIndex(0x0008, 5)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_1AD0')
    def lambda_1AD0():
        ChrTurnDirection(0x0008, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1AD0)

    ChrWalkTo(0x0009, -11870, 0, 10820, 2000, 0x00)
    WaitForThreadExit(0x0008, 0x0001)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301090V#120F#2P你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301091V#051F#5P那把金色的剑……\n',
            '果真是那时的红头盔队长吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301092V真好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140301093V#124F#2P等级为Ｃ，『重剑』\n',
            '阿加特·科洛斯纳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301094V#123F不，政变事件之后，\n',
            '据说升级为B了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301095V#053F#5P哼……\n',
            '不愧是原情报部的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301096V#555F那个时候只会像老鼠一样\n',
            '偷偷摸摸地行动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301097V这次倒是搞得\n',
            '相当华丽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(505, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 14)
    OP_0D()
    Sleep(750)

    ChrTalk(
        0x0009,
        (
            '#0050301098V#057F#5P……这次我就不说逮捕\n',
            '之类的场面话了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301099V我要把你那张假正经的脸\n',
            '打个稀巴烂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140301100V#124F#2P好有气势啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301101V#123F不过，那种程度的损害，\n',
            '还不算华丽吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301102V和10年前……\n',
            '你所看到的光景相比较来说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0140301103V#123F#2P这个国家的游击士的经历\n',
            '我都调查了一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301104V呵呵，你果然\n',
            '和我有点相似嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)

    ChrTalk(
        0x0009,
        (
            '#0050301105V#057F#5P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301106V#053F呵呵……相似？',
            TxtCtl.Enter,
        ),
    )

    OP_21()
    CloseMessageWindow()
    Sleep(200)

    PlayBGM(43)
    Sleep(500)

    Fade(250)
    PlaySE(505, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetSubChip(0x0009, 3)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0050301107V#550F#5P#3S你这一无所知的混帐\n',
            '还敢大放厥词！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    LoadEffect(0x03, 'map\\\\mp009_00.eff')

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0018, 0x00, 0x00, func_06_D17)
    WaitForThreadExit(0x0018, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0140301108V#124F#2P……实力的差距\n',
            '在上次交手时你就应该明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301109V更何况这次还有龙的威胁。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301110V#120F你明知没有胜算，为何还要一个人追来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301111V#057F#6P我才不管什么胜算不胜算……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301112V#054F我只是看你不爽……\n',
            '就这么简单！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140301113V#121F#2P哎呀呀……只有这种程度吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301114V这样的话，龙也派不上用场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301115V#057F#6P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0x03)
    TerminateThread(0x0008, 0x03)
    TerminateThread(0x0008, 0x00)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x0009, 6)
    PlaySE(163, 0x00, 0x64)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)
    ChrJumpTo(0x0008, 5580, 0, 5800, 500, 7000)
    PlaySE(164, 0x00, 0x64)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_212F')
    def lambda_212F():
        ChrJumpTo(0x00FE, 5050, 0, 3990, 200, 15000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_212F)

    @scena.Lambda('lambda_214D')
    def lambda_214D():
        OP_99(0x00FE, 0x00, 0x05, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_214D)

    Sleep(100)

    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 0)
    PlayEffect(0x03, 0x01, 0x0009, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 100)
    PlaySE(214, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_21BC')
    def lambda_21BC():
        OP_9E(0x00FE, 20, 0, 300, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_21BC)

    @scena.Lambda('lambda_21D6')
    def lambda_21D6():
        ChrMoveTo(0x00FE, 4360, 0, 1800, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_21D6)

    WaitForThreadExit(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 6)

    @scena.Lambda('lambda_2205')
    def lambda_2205():
        OP_99(0x00FE, 0x00, 0x05, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2205)

    Sleep(100)

    PlayEffect(0x03, 0x02, 0x0009, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    OP_7C(0, 400, 3000, 100)

    @scena.Lambda('lambda_2265')
    def lambda_2265():
        ChrMoveTo(0x00FE, 4690, 0, 3110, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2265)

    @scena.Lambda('lambda_2280')
    def lambda_2280():
        OP_9E(0x00FE, 20, 0, 300, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2280)

    @scena.Lambda('lambda_229A')
    def lambda_229A():
        ChrMoveTo(0x00FE, 4110, 0, 1120, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_229A)

    WaitForThreadExit(0x0008, 0x0002)
    PlaySE(550, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_22C9')
    def lambda_22C9():
        OP_99(0x00FE, 0x00, 0x04, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_22C9)

    Sleep(100)

    PlayEffect(0x03, 0x03, 0x0009, 0, 500, 500, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlaySE(214, 0x00, 0x64)
    OP_7C(0, 600, 3000, 100)

    @scena.Lambda('lambda_2329')
    def lambda_2329():
        ChrMoveTo(0x00FE, 4500, 0, 2110, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2329)

    Sleep(100)

    @scena.Lambda('lambda_2349')
    def lambda_2349():
        CameraMove(3100, 0, 170, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2349)

    @scena.Lambda('lambda_2361')
    def lambda_2361():
        OP_9E(0x00FE, 30, 0, 1200, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2361)

    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 12)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_238A')
    def lambda_238A():
        ChrJumpTo(0x0009, 3210, 0, -2870, 500, 18000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_238A)

    Sleep(100)

    ChrSetChipByIndex(0x0009, 13)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_23B7')
    def lambda_23B7():
        ChrJumpTo(0x0009, 2920, 0, -3840, 200, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_23B7)

    ChrTalk(
        0x0009,
        (
            '#0050301116V#056F#10A呜喔……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    @scena.Lambda('lambda_23FD')
    def lambda_23FD():
        OP_99(0x00FE, 0x04, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_23FD)

    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_241B')
    def lambda_241B():
        CameraSetDistance(2540, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_241B)

    Sleep(500)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 26)
    ChrSetSubChip(0x0008, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301117V#121F虽然有相似的地方……\n',
            '但我和你有决定性的不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301118V那就是挥剑的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301119V#057F什、什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140301120V#124F我之所以挥剑\n',
            '是为了抛弃人道而成为修罗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301121V#120F而你，只是为了填补\n',
            '自我的空虚而挥剑罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301122V#052F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140301123V#124F挥舞沉重的铁块\n',
            '让悲哀的空虚充满激情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301124V当愤怒震慑心灵之际，\n',
            '便可以从悲伤之中逃离出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301125V#121F但是，这只不过是自欺欺人罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2631')
    def lambda_2631():
        OP_9E(0x00FE, 20, 0, 300, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2631)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301126V#056F…………住口………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140301127V#123F而自欺欺人者\n',
            '是不可能向前迈进的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301128V莫说是领悟『理』之境界，\n',
            '就连堕入『修罗』之道也是妄想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301129V这样子下去……\n',
            '你永远都只是个半吊子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0003)

    @scena.Lambda('lambda_2734')
    def lambda_2734():
        OP_9E(0x00FE, 50, 0, 300, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2734)

    Sleep(500)

    Fade(250)
    PlaySE(505, 0x00, 0x64)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301130V#550F#3S给我闭嘴！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0342, 7, 0x1A17))
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C1102._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x27BA
@scena.Code('func_09_27BA')
def func_09_27BA():
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 385)
    OP_70(0x0000, 435)

    Return()

# id: 0x000A offset: 0x27CE
@scena.Code('func_0A_27CE')
def func_0A_27CE():
    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0009, 0x1000)
    ChrClearFlags(0x0009, 0x0800)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_27F6')
    def lambda_27F6():
        ChrMoveTo(0x0009, 3340, 0, -2180, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_27F6)

    @scena.Lambda('lambda_2811')
    def lambda_2811():
        CameraMove(4450, 0, 1950, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2811)

    Sleep(200)

    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 11)

    @scena.Lambda('lambda_2856')
    def lambda_2856():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2856)

    @scena.Lambda('lambda_2866')
    def lambda_2866():
        ChrJumpTo(0x0009, 4130, 0, 740, 500, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2866)

    PlaySE(505, 0x00, 0x64)
    Sleep(200)

    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_2896')
    def lambda_2896():
        ChrJumpTo(0x0008, 4920, 0, 2900, 200, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2896)

    ChrTurnDirection(0x0008, 0x0009, 0)
    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0008, 400)
    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_28CC')
    def lambda_28CC():
        OP_99(0x00FE, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_28CC)

    @scena.Lambda('lambda_28DC')
    def lambda_28DC():
        ChrJumpTo(0x0009, 4440, 0, 2100, 200, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_28DC)

    Sleep(250)

    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    OP_7C(0, 200, 3000, 100)
    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0x01, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_295C')
    def lambda_295C():
        OP_99(0x00FE, 0x00, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_295C)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_2971')
    def lambda_2971():
        OP_99(0x00FE, 0x04, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2971)

    @scena.Lambda('lambda_2981')
    def lambda_2981():
        ChrTurnDirection(0x0009, 0x0008, 0)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2981)

    @scena.Lambda('lambda_298F')
    def lambda_298F():
        ChrJumpTo(0x0009, 5180, 0, -610, 200, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_298F)

    WaitForThreadExit(0x0009, 0x0001)
    Sleep(100)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 24)

    @scena.Lambda('lambda_29C6')
    def lambda_29C6():
        OP_99(0x00FE, 0x00, 0x0E, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_29C6)

    Sleep(400)

    @scena.Lambda('lambda_29DB')
    def lambda_29DB():
        ChrJumpTo(0x0009, 5220, 0, 370, 200, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_29DB)

    PlaySE(505, 0x00, 0x64)
    Sleep(300)

    PlaySE(163, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_2A1A')
    def lambda_2A1A():
        ChrJumpTo(0x0008, 1960, 0, -5040, 2000, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2A1A)

    @scena.Lambda('lambda_2A38')
    def lambda_2A38():
        CameraMove(1870, 0, -5050, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A38)

    Sleep(200)

    @scena.Lambda('lambda_2A55')
    def lambda_2A55():
        ChrSetDirection(0x0008, 0, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2A55)

    WaitForThreadExit(0x0009, 0x0001)
    WaitForThreadExit(0x0008, 0x0000)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    PlaySE(164, 0x00, 0x64)
    ChrTurnDirection(0x0009, 0x0008, 500)
    Sleep(100)

    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 23)
    ChrSetSubChip(0x0009, 19)

    @scena.Lambda('lambda_2A9F')
    def lambda_2A9F():
        OP_99(0x00FE, 0x14, 0x17, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2A9F)

    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_2AB9')
    def lambda_2AB9():
        CameraMove(1990, 2310, -4890, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2AB9)

    @scena.Lambda('lambda_2AD1')
    def lambda_2AD1():
        ChrJumpTo(0x0009, 2170, 0, -4000, 2000, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2AD1)

    Sleep(600)

    @scena.Lambda('lambda_2AF4')
    def lambda_2AF4():
        CameraMove(1870, 0, -5050, 100)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AF4)

    @scena.Lambda('lambda_2B0C')
    def lambda_2B0C():
        CameraSetDistance(3360, 100)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2B0C)

    ChrSetFlags(0x0009, 0x0800)
    PlaySE(85, 0x00, 0x5A)

    @scena.Lambda('lambda_2B26')
    def lambda_2B26():
        OP_99(0x00FE, 0x18, 0x1A, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2B26)

    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2B48')
    def lambda_2B48():
        ChrJumpTo(0x0008, 680, 0, -9000, 200, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2B48)

    PlayEffect(0x12, 0xFF, 0x00FF, 1960, 0, -5040, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 500, 2000, 100)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000B offset: 0x2BC7
@scena.Code('func_0B_2BC7')
def func_0B_2BC7():
    Sleep(200)

    @scena.Lambda('lambda_2BD2')
    def lambda_2BD2():
        ChrSetDirection(0x0008, 0, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2BD2)

    WaitForThreadExit(0x0008, 0x0000)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    PlaySE(164, 0x00, 0x64)

    Return()

# id: 0x000C offset: 0x2BF7
@scena.Code('func_0C_2BF7')
def func_0C_2BF7():
    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0009, 0x1000)
    ChrClearFlags(0x0009, 0x0800)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_2C1F')
    def lambda_2C1F():
        ChrMoveTo(0x0009, 3340, 0, -2180, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2C1F)

    @scena.Lambda('lambda_2C3A')
    def lambda_2C3A():
        CameraMove(4450, 0, 1950, 600)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2C3A)

    @scena.Lambda('lambda_2C52')
    def lambda_2C52():
        CameraSetDistance(2870, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2C52)

    Sleep(200)

    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x0009, 3)

    @scena.Lambda('lambda_2C8F')
    def lambda_2C8F():
        ChrJumpTo(0x0009, 4130, 0, 740, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2C8F)

    Sleep(200)

    @scena.Lambda('lambda_2CB2')
    def lambda_2CB2():
        OP_99(0x00FE, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2CB2)

    PlaySE(505, 0x00, 0x64)
    ChrSetAfterImage(0x00, 0x0008, 0x0014, 0x012C)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 2)

    @scena.Lambda('lambda_2CD9')
    def lambda_2CD9():
        ChrJumpTo(0x0008, 4920, 0, 2900, 200, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2CD9)

    ChrTurnDirection(0x0008, 0x0009, 0)
    WaitForThreadExit(0x0009, 0x0000)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetSubChip(0x0008, 0)
    Sleep(300)

    ChrTurnDirection(0x0009, 0x0008, 400)
    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_2D26')
    def lambda_2D26():
        OP_99(0x00FE, 0x00, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2D26)

    @scena.Lambda('lambda_2D36')
    def lambda_2D36():
        ChrJumpTo(0x0009, 4440, 0, 2100, 200, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2D36)

    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 1)

    @scena.Lambda('lambda_2D5E')
    def lambda_2D5E():
        OP_99(0x00FE, 0x01, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2D5E)

    Sleep(250)

    PlaySE(214, 0x00, 0x64)
    PlayEffect(0x03, 0x01, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 400, 3000, 200)
    TerminateThread(0x0009, 0x01)

    @scena.Lambda('lambda_2DC2')
    def lambda_2DC2():
        OP_99(0x00FE, 0x04, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2DC2)

    @scena.Lambda('lambda_2DD2')
    def lambda_2DD2():
        ChrTurnDirection(0x0009, 0x0008, 0)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2DD2)

    @scena.Lambda('lambda_2DE0')
    def lambda_2DE0():
        ChrJumpTo(0x0009, 5180, 0, -610, 200, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2DE0)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_2E0D')
    def lambda_2E0D():
        OP_99(0x00FE, 0x00, 0x0E, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2E0D)

    Sleep(400)

    @scena.Lambda('lambda_2E22')
    def lambda_2E22():
        ChrJumpTo(0x0009, 5220, 0, 370, 500, 7000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2E22)

    Sleep(200)

    PlaySE(505, 0x00, 0x64)
    PlaySE(163, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)
    ChrSetAfterImage(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_2E61')
    def lambda_2E61():
        ChrJumpTo(0x0008, 1960, 0, -5040, 2000, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2E61)

    @scena.Lambda('lambda_2E7F')
    def lambda_2E7F():
        CameraMove(2800, 0, -1440, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E7F)

    @scena.Lambda('lambda_2E97')
    def lambda_2E97():
        CameraSetDistance(3370, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E97)

    CreateThread(0x0008, 0x00, 0x00, func_0B_2BC7)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetSubChip(0x0009, 0)
    ChrSetFlags(0x0009, 0x0020)
    ChrTurnDirection(0x0009, 0x0008, 1000)
    ChrClearFlags(0x0009, 0x0020)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 23)
    ChrSetSubChip(0x0009, 19)

    @scena.Lambda('lambda_2EDD')
    def lambda_2EDD():
        OP_99(0x00FE, 0x13, 0x15, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2EDD)

    WaitForThreadExit(0x0009, 0x0001)
    Sleep(100)

    @scena.Lambda('lambda_2EF7')
    def lambda_2EF7():
        OP_99(0x00FE, 0x15, 0x17, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2EF7)

    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_2F11')
    def lambda_2F11():
        CameraMove(1990, 2310, -4890, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F11)

    @scena.Lambda('lambda_2F29')
    def lambda_2F29():
        ChrJumpTo(0x0009, 2170, 0, -4000, 2000, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2F29)

    Sleep(200)

    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 24)
    ChrSetSubChip(0x0009, 10)
    Sleep(200)

    ChrSetAfterImage(0x00, 0x0008, 0x001E, 0x012C)
    ChrSetChipByIndex(0x0008, 31)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2F72')
    def lambda_2F72():
        ChrJumpTo(0x0008, 680, 0, -9000, 500, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2F72)

    Sleep(200)

    @scena.Lambda('lambda_2F95')
    def lambda_2F95():
        CameraMove(1870, 0, -5050, 100)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F95)

    @scena.Lambda('lambda_2FAD')
    def lambda_2FAD():
        CameraSetDistance(3360, 100)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2FAD)

    TerminateThread(0x0009, 0x02)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x0009, 0x0800)
    ChrSetChipByIndex(0x0009, 23)
    ChrSetSubChip(0x0009, 24)

    @scena.Lambda('lambda_2FD5')
    def lambda_2FD5():
        OP_99(0x00FE, 0x18, 0x1A, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2FD5)

    PlaySE(85, 0x00, 0x5A)
    PlayEffect(0x12, 0xFF, 0x00FF, 1960, -1000, -5040, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 600, 3000, 200)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    ChrSetAfterImage(0x01, 0x0008, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000D offset: 0x304B
@scena.Code('func_0D_304B')
def func_0D_304B():
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
        'loc_305E',
    )

    Call(0, 0x0034)

    def _loc_305E(): pass

    label('loc_305E')

    CameraMove(3100, 0, 170, 0)
    OP_67(0, 5150, -10000, 0)
    CameraSetDistance(3670, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0008, 4500, 0, 2110, 180)
    ChrSetPos(0x0009, 2950, 0, -4500, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 26)
    ChrSetSubChip(0x0008, 7)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 3)
    OP_72(0x0000, 0x0004)
    ChrSetPos(0x0018, 12660, 0, 13410, 225)
    OP_A1(0x0018, 0x0000)
    ChrSetPos(0x0018, 12660, 0, 13410, 232)
    ChrSetPos(0x0019, 0, 0, 0, 225)
    OP_CF(0x0019, 0x00, 'Frame127_FireEmitter')
    ChrSetFlags(0x0018, 0x0001)
    ChrClearFlags(0x0018, 0x0080)

    ExecExpressionWithValue(
        0x0018,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            (Expr.PushLong, 0x8),
            Expr.Or,
            (Expr.PushLong, 0x40),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x07,
        (
            (Expr.PushLong, 0x1964),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x34,
        (
            (Expr.PushLong, 0x249F0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 385)
    OP_70(0x0000, 435)
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')
    LoadEffect(0x01, 'monster\\ms30703.eff')
    LoadEffect(0x02, 'battle\\\\btbomb00.eff')
    LoadEffect(0x03, 'map\\\\mp009_00.eff')
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301166V#550F#3S啊啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    CreateThread(0x0018, 0x00, 0x00, func_0C_2BF7)
    WaitForThreadExit(0x0018, 0x0000)
    Sleep(1000)

    @scena.Lambda('lambda_3248')
    def lambda_3248():
        CameraMove(1300, 0, -5900, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3248)

    @scena.Lambda('lambda_3260')
    def lambda_3260():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3260)

    @scena.Lambda('lambda_3278')
    def lambda_3278():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3278)

    @scena.Lambda('lambda_3288')
    def lambda_3288():
        OP_6C(332000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3288)

    @scena.Lambda('lambda_3298')
    def lambda_3298():
        OP_6E(262, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3298)

    OP_99(0x0009, 0x1A, 0x1E, 1000)
    WaitForThreadExit(0x0101, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0009, 0x0800)

    ChrTalk(
        0x0009,
        (
            '#0050301167V#550F可、可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140301168V#124F真难看啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301169V#120F我的同情心可是有限度的。\n',
            '差不多该结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 8)
    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0140301170V#126F喝啊啊啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301171V#550F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_33D8')
    def lambda_33D8():
        CameraMove(1910, 0, -4550, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_33D8)

    @scena.Lambda('lambda_33F0')
    def lambda_33F0():
        ChrJumpTo(0x00FE, 3050, 0, -2600, 200, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_33F0)

    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 14)
    ChrSetSubChip(0x0009, 7)
    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    LoadEffect(0x03, 'map\\\\mp009_00.eff')

    ChrTalk(
        0x0008,
        (
            '#0140301172V#127F#5P──喝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0016, 1380, 0, -6560, 0)
    ChrClearFlags(0x0016, 0x0080)

    @scena.Lambda('lambda_3485')
    def lambda_3485():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1500)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_3485)

    StopEffect(0x00, 0x00)

    @scena.Lambda('lambda_349A')
    def lambda_349A():
        ChrJumpTo(0x00FE, 4930, 0, 2240, 200, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_349A)

    PlaySE(155, 0x00, 0x64)
    OP_20(0x00000000)
    PlayEffect(0x03, 0x01, 0x0009, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0017, 0x00, 0x00, func_28_6E55)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 16)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_350D')
    def lambda_350D():
        CameraMove(3620, 0, 240, 200)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_350D)

    ChrSetChipByIndex(0x0008, 7)
    ChrSetSubChip(0x0008, 5)
    WaitForThreadExit(0x0016, 0x0001)
    ChrSetFlags(0x0016, 0x0080)
    Sleep(1000)

    @scena.Lambda('lambda_353E')
    def lambda_353E():
        OP_9E(0x00FE, 20, 0, 5000, 2000)
        Yield()

        Jump('lambda_353E')

    DispatchAsync2(0x0009, 0x0003, lambda_353E)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301173V#056F#6P……呜啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0x03)
    OP_99(0x0009, 0x01, 0x04, 1000)
    PlaySE(524, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    OP_99(0x0008, 0x05, 0x07, 1600)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetSubChip(0x0008, 0)
    Sleep(500)

    @scena.Lambda('lambda_35C0')
    def lambda_35C0():
        ChrTurnDirection(0x00FE, 0x0009, 300)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_35C0)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0140301174V#121F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    OP_0D()
    Sleep(500)

    ChrSetDirection(0x0008, 0, 400)

    @scena.Lambda('lambda_3621')
    def lambda_3621():
        CameraMove(4340, 0, 9850, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3621)

    @scena.Lambda('lambda_3639')
    def lambda_3639():
        OP_67(0, 4770, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3639)

    @scena.Lambda('lambda_3651')
    def lambda_3651():
        CameraSetDistance(4410, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3651)

    @scena.Lambda('lambda_3661')
    def lambda_3661():
        OP_6C(359000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3661)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0140301175V#124F#2P好了……\n',
            '差不多到时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301176V#120F趁现在把『福音』的\n',
            '控制程式也调整一下吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301177V#5P#40W……慢、慢着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0009, 400)
    Fade(500)
    CameraMove(3620, 0, 240, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)
    OP_0D()
    PlayBGM(83)

    @scena.Lambda('lambda_3778')
    def lambda_3778():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_3778')

    DispatchAsync2(0x0009, 0x0003, lambda_3778)

    Sleep(500)

    OP_99(0x0009, 0x04, 0x01, 500)
    TerminateThread(0x0009, 0x03)
    Sleep(500)

    @scena.Lambda('lambda_37AC')
    def lambda_37AC():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_37AC')

    DispatchAsync2(0x0009, 0x0003, lambda_37AC)

    ChrSetFlags(0x0009, 0x0020)
    ChrSetDirection(0x0009, 0, 200)
    TerminateThread(0x0009, 0x03)
    ChrClearFlags(0x0009, 0x0020)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301178V#550F#40W还……还没完……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301179V还没结束……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(-26270, 0, 18840, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -26050, 0, 19690, 90)
    ChrSetPos(0x0107, -26220, 0, 18290, 90)
    ChrSetPos(0x00F8, -27300, 0, 19840, 90)
    ChrSetPos(0x00F9, -27540, 0, 18220, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010301180V#1020F#5P那是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301181V#065F#6P阿、阿加特哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3908')
    def lambda_3908():
        ChrWalkTo(0x00FE, -14380, 0, 15030, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3908)

    Sleep(300)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010301182V#1005F#5P提妲！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_71(0x0000, 0x0004)
    Fade(500)
    CameraMove(3800, 0, -260, 0)
    OP_67(0, 8070, -10000, 0)
    CameraSetDistance(1780, 0)
    OP_6C(237000, 0)
    OP_6E(428, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301183V#124F……到这时候\n',
            '还想把破碎的铁块粘起来吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0008, 26)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301184V#123F好吧。\n',
            '就让你带着遗憾离开这个世界吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0107, -8990, 0, 1190, 135)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 17)

    NpcTalk(
        0x0107,
        '少女的声音',
        (
            '#0070301185V#3S不行～！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(250)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetFlags(0x0107, 0x1000)

    @scena.Lambda('lambda_3AEA')
    def lambda_3AEA():
        CameraSetDistance(2000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3AEA)

    @scena.Lambda('lambda_3AFA')
    def lambda_3AFA():
        OP_67(0, 7000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3AFA)

    ChrWalkTo(0x0107, 3800, 0, -1120, 6000, 0x00)
    ChrTurnDirection(0x0107, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301186V#550F臭小鬼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301187V……为什么……\n',
            '会在这种地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301188V#065F#6P那个那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301189V因为担心阿加特哥哥… \n',
            '所以就和姐姐一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301190V#3S提妲！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    LoadEffect(0x00, 'map\\\\mp015_00.eff')
    ChrTurnDirection(0x0008, 0x0101, 400)
    Fade(250)
    ChrSetChipByIndex(0x0008, 22)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    PlaySE(216, 0x00, 0x64)
    OP_99(0x0008, 0x00, 0x04, 1500)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0140301191V#121F#6P……停下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(145, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x0008, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    Fade(500)
    OP_72(0x0000, 0x0004)
    ChrSetPos(0x0018, 15390, 0, 12100, 255)
    CameraMove(11070, 0, 18710, 0)
    OP_67(0, 7880, -10000, 0)
    CameraSetDistance(3710, 0)
    OP_6C(21000, 0)
    OP_6E(426, 0)
    OP_0D()
    Sleep(500)

    PlaySE(290, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3D09')
    def lambda_3D09():
        CameraMove(4220, 3290, 14610, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3D09)

    @scena.Lambda('lambda_3D21')
    def lambda_3D21():
        OP_67(0, 2730, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3D21)

    @scena.Lambda('lambda_3D39')
    def lambda_3D39():
        CameraSetDistance(2760, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3D39)

    @scena.Lambda('lambda_3D49')
    def lambda_3D49():
        OP_6C(56000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_3D49)

    @scena.Lambda('lambda_3D59')
    def lambda_3D59():
        OP_6E(426, 3000)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_3D59)

    OP_72(0x0000, 0x0020)
    Fade(500)
    OP_B0(0x0000, 0x1E)
    OP_6F(0x0000, 460)
    OP_70(0x0000, 365)

    @scena.Lambda('lambda_3D85')
    def lambda_3D85():
        ChrWalkTo(0x00FE, -5130, 0, 5370, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3D85)

    @scena.Lambda('lambda_3DA0')
    def lambda_3DA0():
        ChrWalkTo(0x00FE, -5230, 0, 6650, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3DA0)

    @scena.Lambda('lambda_3DBB')
    def lambda_3DBB():
        ChrWalkTo(0x00FE, -6920, 0, 4720, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3DBB)

    OP_73(0x0000)
    OP_B0(0x0000, 0x14)
    OP_6F(0x0000, 80)
    OP_70(0x0000, 120)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x01, 0x00, 0x0019, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlaySE(289, 0x00, 0x64)
    Sleep(200)

    Fade(500)
    CameraMove(3920, 0, 15460, 0)
    OP_67(0, 2610, -10000, 0)
    CameraSetDistance(3260, 0)
    OP_6C(45000, 0)
    OP_6E(532, 0)
    Sleep(300)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EA7',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x00)

    Jump('loc_3EDB')

    def _loc_3EA7(): pass

    label('loc_3EA7')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EC9',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x00)

    Jump('loc_3EDB')

    def _loc_3EC9(): pass

    label('loc_3EC9')

    OP_62(0x00F9, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)

    def _loc_3EDB(): pass

    label('loc_3EDB')

    CreateThread(0x00F9, 0x00, 0x00, func_13_59E7)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F09',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x00)

    Jump('loc_3F3D')

    def _loc_3F09(): pass

    label('loc_3F09')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F2B',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x00)

    Jump('loc_3F3D')

    def _loc_3F2B(): pass

    label('loc_3F2B')

    OP_62(0x00F8, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)

    def _loc_3F3D(): pass

    label('loc_3F3D')

    CreateThread(0x00F8, 0x00, 0x00, func_12_59B9)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    CreateThread(0x0101, 0x00, 0x00, func_11_598B)
    OP_73(0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 5)
    OP_70(0x0000, 55)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F8, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    OP_63(0x00F8)
    OP_63(0x00F9)
    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010301192V#1021F#5P唔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 465)
    OP_70(0x0000, 487)
    Sleep(500)

    PlaySE(290, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)

    @scena.Lambda('lambda_402D')
    def lambda_402D():
        ChrJumpTo(0x00FE, -14940, 0, 9580, 500, 5000)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_402D)

    Sleep(100)

    @scena.Lambda('lambda_4050')
    def lambda_4050():
        ChrJumpTo(0x00FE, -12750, 0, 10970, 500, 5000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4050)

    Sleep(100)

    @scena.Lambda('lambda_4073')
    def lambda_4073():
        ChrJumpTo(0x00FE, -11950, 0, 9670, 500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4073)

    OP_73(0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 487)
    OP_70(0x0000, 517)
    Fade(500)
    CameraMove(-5710, 0, 10880, 0)
    OP_67(0, 4380, -10000, 0)
    CameraSetDistance(2220, 0)
    OP_6C(78000, 0)
    OP_6E(599, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4130',
    )

    ChrTalk(
        0x0108,
        (
            '#0080301193V#077F#5P喔、真麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_419F')

    def _loc_4130(): pass

    label('loc_4130')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4169',
    )

    ChrTalk(
        0x0103,
        (
            '#0030301194V#523F#5P唔、不妙呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_419F')

    def _loc_4169(): pass

    label('loc_4169')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_419F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301195V#043F#5P怎、怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_419F(): pass

    label('loc_419F')

    Sleep(500)

    Fade(500)
    OP_71(0x0000, 0x0004)
    CameraMove(3800, 0, -260, 0)
    OP_67(0, 8070, -10000, 0)
    CameraSetDistance(1800, 0)
    OP_6C(237000, 0)
    OP_6E(428, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301085V#121F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x04, 0x00, 1500)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 25)
    Sleep(250)

    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(500)

    CreateThread(0x0008, 0x00, 0x00, func_10_5967)

    @scena.Lambda('lambda_4254')
    def lambda_4254():
        CameraMove(3300, 0, -900, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4254)

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070301197V#065F#5P啊、啊呜……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrClearFlags(0x0107, 0x0002)
    ChrSetChipByIndex(0x0107, 17)
    ChrMoveTo(0x0107, 3530, 0, -1700, 1000, 0x00)
    OP_56(0x00)
    OP_59()
    OP_63(0x0107)
    ChrSetFlags(0x0107, 0x0002)
    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 18)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070301198V#068F#5P别、别过来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301199V#550F白、白痴……\n',
            '那种东西管用吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301200V别管我了……\n',
            '赶快逃跑……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0140301201V#121F拉赛尔博士的孙女，\n',
            '提妲·拉赛尔吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301202V听说是位天才少女，\n',
            '但行为也太莽撞了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301203V#124F虽然我没有兴趣\n',
            '对付小女孩──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 26)
    ChrSetSubChip(0x0008, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301204V#120F──但如有必要，一样杀无赦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301205V你还是乖乖地让开比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301206V#550F你、你这混帐……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301207V#062F#5P我、我不会让开的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_99(0x0107, 0x00, 0x04, 1200)

    @scena.Lambda('lambda_451D')
    def lambda_451D():
        CameraSetDistance(1700, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_451D)

    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070301208V#063F#5P我……总是给阿加特哥哥\n',
            '添麻烦，一直受他的照顾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301209V只有现在…我才能\n',
            '偿还这些恩情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0107, 4)
    Sleep(50)

    ChrSetSubChip(0x0107, 5)
    Sleep(50)

    ChrSetSubChip(0x0107, 6)
    Sleep(50)

    ChrSetSubChip(0x0107, 5)
    Sleep(50)

    ChrSetSubChip(0x0107, 4)
    Sleep(50)

    ChrSetSubChip(0x0107, 7)
    Sleep(50)

    ChrSetSubChip(0x0107, 8)
    Sleep(50)

    ChrSetSubChip(0x0107, 7)
    Sleep(50)

    ChrSetSubChip(0x0107, 4)
    Sleep(50)

    ChrSetSubChip(0x0107, 5)
    Sleep(50)

    ChrSetSubChip(0x0107, 6)
    Sleep(50)

    ChrSetSubChip(0x0107, 5)
    Sleep(50)

    ChrSetSubChip(0x0107, 4)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070301210V#561F#5P不……不对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070301211V#066F#5P虽然阿加特哥哥对我……\n',
            '总是一副不耐烦的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301212V一直都叫我小鬼小鬼的，\n',
            '把我当小孩子对待……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301213V但其实他真的很温柔……\n',
            '总是默默地保护着我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x04, 0x00, 1500)
    Sleep(300)

    ChrTalk(
        0x0107,
        (
            '#0070301214V#062F#5P是我最喜欢……最重要的人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0107, 0x00, 0x04, 2000)

    @scena.Lambda('lambda_4763')
    def lambda_4763():
        OP_99(0x0107, 0x09, 0x17, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_4763)

    Sleep(400)

    PlaySE(216, 0x00, 0x50)
    PlaySE(130, 0x00, 0x50)
    WaitForThreadExit(0x0107, 0x0002)
    Sleep(300)

    OP_99(0x0107, 0x18, 0x1B, 2000)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070301215V#068F#5P#3S所以我……\n',
            '绝对不会让开的！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 500, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301216V#052F……啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0140301217V#124F哼，真是勇敢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301218V#121F这种半吊子真的\n',
            '值得你这么倾慕吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetPos(0x001A, -11240, 30000, -11760, 227)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrClearFlags(0x0008, 0x0800)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 0)
    ChrTurnDirection(0x0008, 0x0107, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301219V#123F算了，既然有人插手，\n',
            '这次我就暂且退下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301220V#064F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_20(0x000003E8)
    Fade(500)
    OP_72(0x0000, 0x0004)
    ChrSetPos(0x0018, 12660, 0, 13410, 225)
    CameraMove(780, 0, 12430, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(332000, 0)
    OP_6E(552, 0)
    OP_0D()
    ChrClearFlags(0x0107, 0x0002)
    ChrSetChipByIndex(0x0107, 65535)
    ChrSetSubChip(0x0107, 0)
    OP_CF(0x001B, 0x00, 'Frame143_back_Null1')
    ChrSetPos(0x001C, 9190, 0, 5540, 0)
    ChrSetPos(0x001D, -230, 0, 4170, 0)
    PlayEffect(0x02, 0xFF, 0x001C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlayEffect(0x02, 0xFF, 0x001D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_72(0x0000, 0x0020)
    PlayEffect(0x02, 0xFF, 0x001B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0000, 517)
    OP_70(0x0000, 540)
    OP_73(0x0000)
    OP_6F(0x0000, 125)
    OP_70(0x0000, 180)
    Sleep(1500)

    PlaySE(287, 0x00, 0x64)
    OP_7C(300, 300, 5000, 500)
    OP_73(0x0000)

    @scena.Lambda('lambda_4AA2')
    def lambda_4AA2():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4AA2)

    @scena.Lambda('lambda_4AB0')
    def lambda_4AB0():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4AB0)

    @scena.Lambda('lambda_4ABE')
    def lambda_4ABE():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4ABE)

    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 5)
    OP_70(0x0000, 55)
    Sleep(500)

    PlayBGM(116)
    Sleep(500)

    OP_DB()
    Fade(500)
    OP_72(0x0001, 0x0004)
    OP_A1(0x001A, 0x0001)
    ChrSetPos(0x001A, -11240, 30000, -11760, 227)
    LoadEffect(0x04, 'map\\\\mp021_00.eff')
    CameraMove(-1010, 0, -1490, 0)
    OP_67(0, 22530, -10000, 0)
    CameraSetDistance(2870, 0)
    OP_6C(30000, 0)
    OP_6E(523, 0)
    PlaySE(121, 0x00, 0x64)
    CreateThread(0x001A, 0x01, 0x00, func_15_5ACC)

    @scena.Lambda('lambda_4B69')
    def lambda_4B69():
        CameraMove(-8560, 0, -7500, 13000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4B69)

    @scena.Lambda('lambda_4B81')
    def lambda_4B81():
        OP_6C(315000, 13000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4B81)

    @scena.Lambda('lambda_4B91')
    def lambda_4B91():
        CameraSetDistance(1890, 13000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4B91)

    Sleep(2000)

    SetMessageWindowPos(100, 75, -1, -1)
    TalkSetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600301221V#163F#60A主炮和右舷副炮，\n',
            '锁定瞄准龙！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(6000)

    TalkSetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600301222V#160F#57A着陆同时，\n',
            '全体人员，迅速展开！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(5700)

    OP_56(0x00)
    Sleep(500)

    SetMessageWindowPos(300, 250, -1, -1)
    TalkSetChrName('士兵们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#2440301223V#5S#30A Yes·Sir！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 500, 3000, 100)
    Sleep(2000)

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    @scena.Lambda('lambda_4CA0')
    def lambda_4CA0():
        ChrSetDirection(0x00FE, 125, 10)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4CA0)

    Sleep(100)

    @scena.Lambda('lambda_4CB3')
    def lambda_4CB3():
        ChrSetDirection(0x00FE, 125, 16)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4CB3)

    Sleep(100)

    @scena.Lambda('lambda_4CC6')
    def lambda_4CC6():
        ChrSetDirection(0x00FE, 125, 20)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4CC6)

    Sleep(100)

    @scena.Lambda('lambda_4CD9')
    def lambda_4CD9():
        ChrSetDirection(0x00FE, 125, 26)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4CD9)

    Sleep(100)

    @scena.Lambda('lambda_4CEC')
    def lambda_4CEC():
        ChrSetDirection(0x00FE, 125, 30)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4CEC)

    Sleep(100)

    @scena.Lambda('lambda_4CFF')
    def lambda_4CFF():
        ChrSetDirection(0x00FE, 125, 39)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4CFF)

    Sleep(85)

    @scena.Lambda('lambda_4D12')
    def lambda_4D12():
        ChrSetDirection(0x00FE, 125, 40)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4D12)

    Sleep(85)

    @scena.Lambda('lambda_4D25')
    def lambda_4D25():
        ChrSetDirection(0x00FE, 125, 46)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4D25)

    Sleep(85)

    @scena.Lambda('lambda_4D38')
    def lambda_4D38():
        ChrSetDirection(0x00FE, 125, 50)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4D38)

    Sleep(85)

    @scena.Lambda('lambda_4D4B')
    def lambda_4D4B():
        ChrSetDirection(0x00FE, 125, 59)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4D4B)

    Sleep(85)

    @scena.Lambda('lambda_4D5E')
    def lambda_4D5E():
        ChrSetDirection(0x00FE, 125, 60)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4D5E)

    Sleep(85)

    @scena.Lambda('lambda_4D71')
    def lambda_4D71():
        ChrSetDirection(0x00FE, 125, 66)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4D71)

    Sleep(85)

    @scena.Lambda('lambda_4D84')
    def lambda_4D84():
        ChrSetDirection(0x00FE, 125, 50)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4D84)

    Sleep(85)

    OP_6F(0x0001, 1001)
    OP_70(0x0001, 1020)

    @scena.Lambda('lambda_4DA5')
    def lambda_4DA5():
        ChrSetDirection(0x00FE, 125, 30)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4DA5)

    Sleep(85)

    @scena.Lambda('lambda_4DB8')
    def lambda_4DB8():
        ChrSetDirection(0x00FE, 125, 20)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4DB8)

    Sleep(85)

    @scena.Lambda('lambda_4DCB')
    def lambda_4DCB():
        ChrSetDirection(0x00FE, 125, 14)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_4DCB)

    WaitForThreadExit(0x001A, 0x0003)
    Sleep(2000)

    Fade(500)
    StopEffect(0x01, 0x00)
    OP_23(0x0079)
    OP_23(0x00CC)
    CameraMove(4250, 0, 1420, 0)
    OP_67(0, 5560, -10000, 0)
    CameraSetDistance(3050, 0)
    OP_6C(332000, 0)
    OP_6E(321, 0)
    CameraMove(3320, 0, 260, 0)
    OP_67(0, 6400, -10000, 0)
    CameraSetDistance(2530, 0)
    OP_6C(321000, 0)
    OP_6E(374, 0)
    OP_0D()
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 200, 3000, 300)
    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0140301224V#124F#2P呼……\n',
            '总算登场了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301225V#123F这样最后的实验\n',
            '也可以开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x00, 0x00, func_14_5A15)
    Sleep(600)

    Fade(500)
    OP_B0(0x0000, 0x0A)
    CameraMove(8460, 2890, 13560, 0)
    OP_67(0, 6400, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(42000, 0)
    OP_6E(374, 0)
    OP_0D()
    WaitForThreadExit(0x0008, 0x0000)

    ChrTalk(
        0x0107,
        (
            '#0070301226V#065F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301227V#550F#5P慢、慢着……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 315, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301228V#121F#6P别忘了。\n',
            '阿加特·科洛斯纳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301229V只要你还在自欺欺人，\n',
            '就永远成不了任何气候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301230V也保护不了你想要保护的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301231V#550F#5P………咕…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301232V#2P给、给我等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -8130, 0, 9590, 90)
    ChrSetPos(0x00F8, -9490, 0, 10350, 90)
    ChrSetPos(0x00F9, -9580, 0, 8320, 90)
    ChrSetSubChip(0x0009, 4)
    Sleep(100)

    Fade(500)
    CameraMove(-3200, 0, 9770, 0)
    OP_67(0, 9230, -10000, 0)
    CameraSetDistance(2170, 0)
    OP_6C(260000, 0)
    OP_6E(594, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010301233V#1005F#6P默不吭声地听你说话，\n',
            '你竟然就开始得意忘形，乱说一通！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301234V这次绝对不会让你逃跑！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140301235V#124F#5P艾丝蒂尔·布莱特。\n',
            '你用心记住吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301236V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140301237V#121F#5P这次实验结束后，\n',
            '计划就会转移到下一阶段。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301238V到时要是不留神的话，\n',
            '就一定会后悔的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0008, 22)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    PlaySE(216, 0x00, 0x64)
    OP_99(0x0008, 0x00, 0x04, 1500)
    Sleep(300)

    LoadEffect(0x03, 'map\\\\mp015_00.eff')
    PlaySE(145, 0x00, 0x64)
    PlayEffect(0x03, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    Fade(500)
    CameraMove(19800, 0, 12010, 0)
    OP_67(0, 8200, -10000, 0)
    CameraSetDistance(4290, 0)
    OP_6C(80000, 0)
    OP_6E(431, 0)
    ChrSetDirection(0x0008, 0, 0)
    ChrSetChipByIndex(0x0008, 27)
    ChrSetSubChip(0x0008, 1)
    ChrSetDirection(0x0101, 90, 0)
    ChrSetDirection(0x00F8, 90, 0)
    ChrSetDirection(0x00F9, 90, 0)
    OP_0D()
    OP_72(0x0000, 0x0020)
    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 185)
    OP_70(0x0000, 225)
    Sleep(1000)

    PlaySE(405, 0x00, 0x64)
    PlaySE(287, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    OP_73(0x0000)
    LoadEffect(0x00, 'monster\\ms30704.eff')
    Fade(500)
    OP_6F(0x0000, 225)
    OP_70(0x0000, 248)
    OP_B0(0x0000, 0x0A)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 235)
    OP_70(0x0000, 248)
    CreateThread(0x0018, 0x03, 0x00, func_0E_5909)
    Sleep(500)

    CreateThread(0x0018, 0x02, 0x00, func_0F_5920)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010301239V#1020F#5P慢、慢着！\n',
            '那到底是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000A, 0x01, 0x00, func_19_5BD6)
    Sleep(400)

    LoadEffect(0x04, 'monster\\ms30602b.eff')
    LoadEffect(0x05, 'monster\\ms30602a.eff')
    LoadEffect(0x06, 'map\\\\mp003_00.eff')
    LoadEffect(0x07, 'scraft\\sc003_12.eff')
    Fade(500)
    CameraMove(-370, 0, 3680, 0)
    OP_67(0, 4380, -10000, 0)
    CameraSetDistance(3560, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    Sleep(200)

    CreateThread(0x0011, 0x01, 0x00, func_1B_5C58)
    Sleep(100)

    CreateThread(0x000D, 0x01, 0x00, func_1C_5CA3)
    Sleep(400)

    CreateThread(0x0012, 0x01, 0x00, func_1D_5CEE)
    Sleep(100)

    CreateThread(0x000E, 0x01, 0x00, func_1E_5D39)
    Sleep(300)

    CreateThread(0x0013, 0x01, 0x00, func_1F_5D84)
    Sleep(100)

    CreateThread(0x000F, 0x01, 0x00, func_20_5DCF)
    Sleep(400)

    CreateThread(0x0014, 0x01, 0x00, func_21_5E1A)
    Sleep(100)

    CreateThread(0x0010, 0x01, 0x00, func_22_5E65)
    Sleep(400)

    CreateThread(0x000C, 0x01, 0x00, func_23_5EB0)
    Sleep(100)

    CreateThread(0x0015, 0x01, 0x00, func_1A_5C0D)
    WaitForThreadExit(0x0011, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0600301240V#162F#2P可恶的龙！\n',
            '别想逃跑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301241V全体人员，射击开始！\n',
            '射击射击，尽量给我打！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000F, 0x0001)
    WaitForThreadExit(0x0014, 0x0001)
    WaitForThreadExit(0x0015, 0x0001)
    Sleep(200)

    Fade(500)
    CameraMove(10720, 30000, 32460, 0)
    OP_67(0, 9320, -10000, 0)
    CameraSetDistance(2420, 0)
    OP_6C(180000, 0)
    OP_6E(306, 0)
    CreateThread(0x001A, 0x00, 0x00, func_26_635A)
    CreateThread(0x000C, 0x01, 0x00, func_25_5FAB)
    CreateThread(0x001A, 0x01, 0x00, func_27_6706)
    CreateThread(0x0011, 0x01, 0x00, func_24_5EFB)
    Sleep(100)

    CreateThread(0x000D, 0x01, 0x00, func_24_5EFB)
    CreateThread(0x0012, 0x01, 0x00, func_24_5EFB)
    Sleep(100)

    CreateThread(0x000E, 0x01, 0x00, func_25_5FAB)
    CreateThread(0x0014, 0x01, 0x00, func_24_5EFB)
    Sleep(100)

    CreateThread(0x000F, 0x01, 0x00, func_24_5EFB)
    CreateThread(0x0013, 0x01, 0x00, func_24_5EFB)
    Sleep(100)

    CreateThread(0x0010, 0x01, 0x00, func_25_5FAB)
    CreateThread(0x0015, 0x01, 0x00, func_24_5EFB)
    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#0140301242V#123F#6P哼，对传说中的古代龙\n',
            '那种攻击怎么可能有效。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140301243V#124F走吧──『古龙雷格纳特』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_DB()

    @scena.Lambda('lambda_56CB')
    def lambda_56CB():
        CameraMove(14000, 17250, 12870, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_56CB)

    @scena.Lambda('lambda_56E3')
    def lambda_56E3():
        OP_67(0, 8180, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_56E3)

    @scena.Lambda('lambda_56FB')
    def lambda_56FB():
        CameraSetDistance(4220, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_56FB)

    @scena.Lambda('lambda_570B')
    def lambda_570B():
        OP_6C(200000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_570B)

    @scena.Lambda('lambda_571B')
    def lambda_571B():
        OP_6E(426, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_571B)

    OP_72(0x0000, 0x0020)
    OP_73(0x0000)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 200)
    OP_70(0x0000, 275)
    TerminateThread(0x0018, 0x03)
    OP_23(0x01F7)
    PlaySE(405, 0x00, 0x64)
    PlaySE(287, 0x00, 0x64)
    OP_7C(500, 500, 5000, 500)
    OP_7C(300, 300, 5000, 500)
    OP_73(0x0000)
    CreateThread(0x0018, 0x03, 0x00, func_0E_5909)

    @scena.Lambda('lambda_5782')
    def lambda_5782():
        CameraSetDistance(4800, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_5782)

    @scena.Lambda('lambda_5792')
    def lambda_5792():
        ChrMoveTo(0x00FE, 1200, 55000, 2410, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_5792)

    OP_6F(0x0000, 545)
    OP_70(0x0000, 564)
    PlayEffect(0x00, 0xFF, 0x0018, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 565)
    OP_70(0x0000, 585)
    CreateThread(0x0018, 0x02, 0x00, func_0F_5920)

    @scena.Lambda('lambda_580D')
    def lambda_580D():
        ChrMoveTo(0x00FE, 1200, 55000, 2410, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_580D)

    Sleep(300)

    TerminateThread(0x0018, 0x02)

    @scena.Lambda('lambda_5831')
    def lambda_5831():
        ChrMoveTo(0x00FE, 1200, 55000, 2410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_5831)

    Sleep(100)

    @scena.Lambda('lambda_5851')
    def lambda_5851():
        ChrMoveTo(0x00FE, 1200, 55000, 2410, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_5851)

    Sleep(100)

    @scena.Lambda('lambda_5871')
    def lambda_5871():
        ChrMoveTo(0x00FE, 1200, 55000, 2410, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_5871)

    Sleep(100)

    @scena.Lambda('lambda_5891')
    def lambda_5891():
        ChrMoveTo(0x00FE, 1200, 55000, 2410, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_5891)

    Sleep(100)

    @scena.Lambda('lambda_58B1')
    def lambda_58B1():
        ChrMoveTo(0x00FE, 1200, 55000, 2410, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_58B1)

    Sleep(100)

    @scena.Lambda('lambda_58D1')
    def lambda_58D1():
        ChrMoveTo(0x00FE, 1200, 55000, 2410, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_58D1)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x5909
@scena.Code('func_0E_5909')
def func_0E_5909():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_591F',
    )

    PlaySE(288, 0x00, 0x64)
    Sleep(1300)

    Jump('func_0E_5909')

    def _loc_591F(): pass

    label('loc_591F')

    Return()

# id: 0x000F offset: 0x5920
@scena.Code('func_0F_5920')
def func_0F_5920():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5966',
    )

    PlayEffect(0x00, 0xFF, 0x0018, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(1300)

    Jump('func_0F_5920')

    def _loc_5966(): pass

    label('loc_5966')

    Return()

# id: 0x0010 offset: 0x5967
@scena.Code('func_10_5967')
def func_10_5967():
    ChrSetChipByIndex(0x00FE, 25)
    ChrMoveTo(0x00FE, 4360, 0, 710, 700, 0x00)
    ChrSetChipByIndex(0x00FE, 5)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0011 offset: 0x598B
@scena.Code('func_11_598B')
def func_11_598B():
    ChrSetChipByIndex(0x00FE, 65535)
    ChrJumpTo(0x00FE, -9160, 0, 8400, 500, 5000)
    ChrSetChipByIndex(0x00FE, 65535)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0012 offset: 0x59B9
@scena.Code('func_12_59B9')
def func_12_59B9():
    ChrSetChipByIndex(0x00FE, 65535)
    ChrJumpTo(0x00FE, -9110, 0, 9760, 500, 5000)
    ChrSetChipByIndex(0x00FE, 65535)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0013 offset: 0x59E7
@scena.Code('func_13_59E7')
def func_13_59E7():
    ChrSetChipByIndex(0x00FE, 65535)
    ChrJumpTo(0x00FE, -11000, 0, 8760, 500, 5000)
    ChrSetChipByIndex(0x00FE, 65535)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0014 offset: 0x5A15
@scena.Code('func_14_5A15')
def func_14_5A15():
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 0)
    ChrSetDirection(0x00FE, 0, 500)
    ChrSetChipByIndex(0x00FE, 28)
    ChrSetSubChip(0x00FE, 1)
    Sleep(100)

    ChrSetSubChip(0x00FE, 2)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetAfterImage(0x00, 0x00FE, 0x0032, 0x01F4)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_5A52')
    def lambda_5A52():
        ChrJumpTo(0x00FE, 8160, 8300, 13670, 9000, 7000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_5A52)

    WaitForThreadExit(0x0008, 0x0003)
    ChrClearFlags(0x0008, 0x0001)
    ChrSetDirection(0x00FE, 90, 0)
    PlaySE(164, 0x00, 0x64)
    OP_CF(0x0008, 0x00, 'Frame143_back_Null1')

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x00FE, 0x0004)
    ChrSetAfterImage(0x01, 0x00FE, 0x0000, 0x0000)
    ChrSetSubChip(0x00FE, 1)
    Sleep(500)

    ChrSetChipByIndex(0x00FE, 0)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0015 offset: 0x5ACC
@scena.Code('func_15_5ACC')
def func_15_5ACC():
    @scena.Lambda('lambda_5AD2')
    def lambda_5AD2():
        ChrMoveTo(0x00FE, -11240, 0, -11760, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_5AD2)

    Sleep(6000)

    @scena.Lambda('lambda_5AF2')
    def lambda_5AF2():
        ChrMoveTo(0x00FE, -11240, 0, -11760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_5AF2)

    Sleep(3000)

    @scena.Lambda('lambda_5B12')
    def lambda_5B12():
        ChrMoveTo(0x00FE, -11240, 0, -11760, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_5B12)

    Sleep(2000)

    @scena.Lambda('lambda_5B32')
    def lambda_5B32():
        ChrMoveTo(0x00FE, -11240, 0, -11760, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_5B32)

    PlayEffect(0x04, 0x01, 0x001A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x01, 0x64)

    Return()

# id: 0x0016 offset: 0x5B82
@scena.Code('func_16_5B82')
def func_16_5B82():
    ChrWalkTo(0x00FE, -6570, 0, 11490, 6000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0017 offset: 0x5B9E
@scena.Code('func_17_5B9E')
def func_17_5B9E():
    ChrWalkTo(0x00FE, -8280, 0, 11760, 6000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0018 offset: 0x5BBA
@scena.Code('func_18_5BBA')
def func_18_5BBA():
    ChrWalkTo(0x00FE, -7330, 0, 9910, 6000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0019 offset: 0x5BD6
@scena.Code('func_19_5BD6')
def func_19_5BD6():
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -2350, 0, 2640, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x001A offset: 0x5C0D
@scena.Code('func_1A_5C0D')
def func_1A_5C0D():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -5330, 0, -290, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001B offset: 0x5C58
@scena.Code('func_1B_5C58')
def func_1B_5C58():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -5320, 0, 4540, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001C offset: 0x5CA3
@scena.Code('func_1C_5CA3')
def func_1C_5CA3():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -630, 0, -1460, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001D offset: 0x5CEE
@scena.Code('func_1D_5CEE')
def func_1D_5CEE():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -880, 0, 890, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001E offset: 0x5D39
@scena.Code('func_1E_5D39')
def func_1E_5D39():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -7870, 0, 5020, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x001F offset: 0x5D84
@scena.Code('func_1F_5D84')
def func_1F_5D84():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -3260, 0, 310, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0020 offset: 0x5DCF
@scena.Code('func_20_5DCF')
def func_20_5DCF():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -5670, 0, 2720, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0021 offset: 0x5E1A
@scena.Code('func_21_5E1A')
def func_21_5E1A():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -3600, 0, -1920, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0022 offset: 0x5E65
@scena.Code('func_22_5E65')
def func_22_5E65():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -8600, 0, 2800, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0023 offset: 0x5EB0
@scena.Code('func_23_5EB0')
def func_23_5EB0():
    ChrSetChipByIndex(0x00FE, 19)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, -8940, 0, -7810, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -6980, 0, 1360, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    ChrSetChipByIndex(0x00FE, 20)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0024 offset: 0x5EFB
@scena.Code('func_24_5EFB')
def func_24_5EFB():
    ChrSetChipByIndex(0x00FE, 20)
    def _loc_5F00(): pass

    label('loc_5F00')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5FAA',
    )

    OP_99(0x00FE, 0x00, 0x04, 2600)
    Sleep(500)

    OP_99(0x00FE, 0x04, 0x00, 2600)

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x6),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F41',
    )

    Sleep(500)

    Jump('loc_5FA7')

    def _loc_5F41(): pass

    label('loc_5F41')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F56',
    )

    Sleep(600)

    Jump('loc_5FA7')

    def _loc_5F56(): pass

    label('loc_5F56')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F6B',
    )

    Sleep(700)

    Jump('loc_5FA7')

    def _loc_5F6B(): pass

    label('loc_5F6B')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F80',
    )

    Sleep(800)

    Jump('loc_5FA7')

    def _loc_5F80(): pass

    label('loc_5F80')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F95',
    )

    Sleep(900)

    Jump('loc_5FA7')

    def _loc_5F95(): pass

    label('loc_5F95')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5FA7',
    )

    Sleep(1000)

    def _loc_5FA7(): pass

    label('loc_5FA7')

    Jump('loc_5F00')

    def _loc_5FAA(): pass

    label('loc_5FAA')

    Return()

# id: 0x0025 offset: 0x5FAB
@scena.Code('func_25_5FAB')
def func_25_5FAB():
    ChrSetChipByIndex(0x00FE, 20)
    def _loc_5FB0(): pass

    label('loc_5FB0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6359',
    )

    OP_99(0x00FE, 0x00, 0x04, 2600)
    PlaySE(503, 0x00, 0x64)
    Sleep(500)

    OP_99(0x00FE, 0x04, 0x00, 2600)

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x6),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_602B',
    )

    PlayEffect(0x06, 0xFF, 0x001C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    Jump('loc_6356')

    def _loc_602B(): pass

    label('loc_602B')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6075',
    )

    PlayEffect(0x06, 0xFF, 0x001D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    Jump('loc_6356')

    def _loc_6075(): pass

    label('loc_6075')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60BF',
    )

    PlayEffect(0x06, 0xFF, 0x001E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(700)

    Jump('loc_6356')

    def _loc_60BF(): pass

    label('loc_60BF')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6109',
    )

    PlayEffect(0x06, 0xFF, 0x001F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    Jump('loc_6356')

    def _loc_6109(): pass

    label('loc_6109')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6153',
    )

    PlayEffect(0x06, 0xFF, 0x0020, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(900)

    Jump('loc_6356')

    def _loc_6153(): pass

    label('loc_6153')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_619D',
    )

    PlayEffect(0x06, 0xFF, 0x0021, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Jump('loc_6356')

    def _loc_619D(): pass

    label('loc_619D')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61E7',
    )

    PlayEffect(0x06, 0xFF, 0x0022, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    Jump('loc_6356')

    def _loc_61E7(): pass

    label('loc_61E7')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6231',
    )

    PlayEffect(0x06, 0xFF, 0x0023, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(700)

    Jump('loc_6356')

    def _loc_6231(): pass

    label('loc_6231')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_627B',
    )

    PlayEffect(0x06, 0xFF, 0x0024, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    Jump('loc_6356')

    def _loc_627B(): pass

    label('loc_627B')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_62C5',
    )

    PlayEffect(0x06, 0xFF, 0x0025, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(900)

    Jump('loc_6356')

    def _loc_62C5(): pass

    label('loc_62C5')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_630F',
    )

    PlayEffect(0x06, 0xFF, 0x0026, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Jump('loc_6356')

    def _loc_630F(): pass

    label('loc_630F')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6356',
    )

    PlayEffect(0x06, 0xFF, 0x0027, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(700)

    def _loc_6356(): pass

    label('loc_6356')

    Jump('loc_5FB0')

    def _loc_6359(): pass

    label('loc_6359')

    Return()

# id: 0x0026 offset: 0x635A
@scena.Code('func_26_635A')
def func_26_635A():
    ChrSetPos(0x0028, -2890, 4570, -13910, 45)
    def _loc_636B(): pass

    label('loc_636B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6705',
    )

    Sleep(500)

    PlayEffect(0x05, 0xFF, 0x0028, 0, 0, 0, -21, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlaySE(992, 0x00, 0x64)

    ExecExpressionWithReg(
        0x0003,
        (
            Expr.Rand,
            (Expr.PushLong, 0x5),
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
        'loc_6409',
    )

    PlayEffect(0x04, 0xFF, 0x001C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_6409(): pass

    label('loc_6409')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_644E',
    )

    PlayEffect(0x04, 0xFF, 0x001D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_644E(): pass

    label('loc_644E')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6493',
    )

    PlayEffect(0x04, 0xFF, 0x001E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_6493(): pass

    label('loc_6493')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_64D8',
    )

    PlayEffect(0x04, 0xFF, 0x001F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_64D8(): pass

    label('loc_64D8')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_651D',
    )

    PlayEffect(0x04, 0xFF, 0x0020, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_651D(): pass

    label('loc_651D')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6562',
    )

    PlayEffect(0x04, 0xFF, 0x0021, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_6562(): pass

    label('loc_6562')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_65A7',
    )

    PlayEffect(0x04, 0xFF, 0x0022, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_65A7(): pass

    label('loc_65A7')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_65EC',
    )

    PlayEffect(0x04, 0xFF, 0x0023, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_65EC(): pass

    label('loc_65EC')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6631',
    )

    PlayEffect(0x04, 0xFF, 0x0024, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_6631(): pass

    label('loc_6631')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6676',
    )

    PlayEffect(0x04, 0xFF, 0x0025, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_6676(): pass

    label('loc_6676')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66BB',
    )

    PlayEffect(0x04, 0xFF, 0x0026, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_66FD')

    def _loc_66BB(): pass

    label('loc_66BB')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66FD',
    )

    PlayEffect(0x04, 0xFF, 0x0027, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_66FD(): pass

    label('loc_66FD')

    Sleep(10000)

    Jump('loc_636B')

    def _loc_6705(): pass

    label('loc_6705')

    Return()

# id: 0x0027 offset: 0x6706
@scena.Code('func_27_6706')
def func_27_6706():
    ChrSetPos(0x001C, -1050, 0, 10880, 0)
    ChrSetPos(0x001D, 610, 0, 13410, 0)
    ChrSetPos(0x001E, 230, 0, 7550, 0)
    ChrSetPos(0x001F, 7300, 0, 7640, 0)
    ChrSetPos(0x0020, 9270, 0, 5590, 0)
    ChrSetPos(0x0021, 11970, 0, 7410, 0)
    ChrSetPos(0x0022, 9780, 0, 8530, 0)
    ChrSetPos(0x0023, -1300, 0, 16110, 0)
    ChrSetPos(0x0024, 8280, 0, 5580, 0)
    ChrSetPos(0x0025, 11320, 0, 4310, 0)
    ChrSetPos(0x0026, 13890, 0, 5860, 0)
    ChrSetPos(0x0027, 6890, 0, 9970, 0)
    def _loc_67D2(): pass

    label('loc_67D2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6E54',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xC),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x07, 0x01, 0x00FF, -8950, 6000, -6300, 45, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x07, 0x02, 0x00FF, -8950, 6000, -6300, 45, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_68DA',
    )

    PlayEffect(0x02, 0xFF, 0x001C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x001F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_68DA(): pass

    label('loc_68DA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6959',
    )

    PlayEffect(0x02, 0xFF, 0x001D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x0021, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6959(): pass

    label('loc_6959')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_69D8',
    )

    PlayEffect(0x02, 0xFF, 0x001E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x0023, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_69D8(): pass

    label('loc_69D8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A57',
    )

    PlayEffect(0x02, 0xFF, 0x001F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x0025, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6A57(): pass

    label('loc_6A57')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6AD6',
    )

    PlayEffect(0x02, 0xFF, 0x0020, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x0027, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6AD6(): pass

    label('loc_6AD6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B55',
    )

    PlayEffect(0x02, 0xFF, 0x0021, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x001C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6B55(): pass

    label('loc_6B55')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6BD4',
    )

    PlayEffect(0x02, 0xFF, 0x0022, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x001E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6BD4(): pass

    label('loc_6BD4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C53',
    )

    PlayEffect(0x02, 0xFF, 0x0023, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x0020, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6C53(): pass

    label('loc_6C53')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CD2',
    )

    PlayEffect(0x02, 0xFF, 0x0024, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x0022, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6CD2(): pass

    label('loc_6CD2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D51',
    )

    PlayEffect(0x02, 0xFF, 0x0025, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x0024, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6D51(): pass

    label('loc_6D51')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DD0',
    )

    PlayEffect(0x02, 0xFF, 0x0026, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x001D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_6E4C')

    def _loc_6DD0(): pass

    label('loc_6DD0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E4C',
    )

    PlayEffect(0x02, 0xFF, 0x0027, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x02, 0xFF, 0x0026, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_6E4C(): pass

    label('loc_6E4C')

    Sleep(2000)

    Jump('loc_67D2')

    def _loc_6E54(): pass

    label('loc_6E54')

    Return()

# id: 0x0028 offset: 0x6E55
@scena.Code('func_28_6E55')
def func_28_6E55():
    ChrSetPos(0x00FE, 3990, 800, -760, 180)
    ChrSetChipByIndex(0x00FE, 15)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_6E85')
    def lambda_6E85():
        ChrJumpTo(0x00FE, 5460, -500, -1800, 4000, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_6E85)

    @scena.Lambda('lambda_6EA3')
    def lambda_6EA3():
        OP_99(0x00FE, 0x00, 0x07, 3500)
        Yield()

        Jump('lambda_6EA3')

    DispatchAsync2(0x00FE, 0x0002, lambda_6EA3)

    WaitForThreadExit(0x00FE, 0x0001)
    TerminateThread(0x00FE, 0x02)
    PlaySE(292, 0x00, 0x50)
    ChrSetSubChip(0x00FE, 5)

    Return()

# id: 0x0029 offset: 0x6EC4
@scena.Code('func_29_6EC4')
def func_29_6EC4():
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
        'loc_6ED7',
    )

    Call(0, 0x0034)

    def _loc_6ED7(): pass

    label('loc_6ED7')

    CameraMove(-20380, 0, 2110, 0)
    OP_67(0, 5350, -10000, 0)
    CameraSetDistance(3020, 0)
    OP_6C(257000, 0)
    OP_6E(660, 0)
    ChrSetFlags(0x0107, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x00F8, 0x0080)
    ChrClearFlags(0x00F9, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x00F8, -3000, 0, -4670, 225)
    ChrSetPos(0x0101, -4070, 0, -3070, 225)
    ChrSetPos(0x00F9, -2360, 0, -2940, 225)
    ChrSetPos(0x000A, -5010, 0, -5490, 45)
    ChrSetPos(0x000B, -5010, 0, -7780, 45)
    OP_72(0x0001, 0x0004)
    OP_6F(0x0001, 200)

    @scena.Lambda('lambda_6F99')
    def lambda_6F99():
        CameraMove(-10260, 0, -7880, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6F99)

    @scena.Lambda('lambda_6FB1')
    def lambda_6FB1():
        OP_67(0, 5350, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6FB1)

    @scena.Lambda('lambda_6FC9')
    def lambda_6FC9():
        OP_6C(257000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6FC9)

    ExecExpressionWithValue(
        0x0018,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A1(0x001A, 0x0001)
    ChrSetPos(0x001A, -11240, 0, -11760, 127)
    ChrSetFlags(0x001A, 0x0001)
    ChrClearFlags(0x001A, 0x0080)

    ExecExpressionWithValue(
        0x001A,
        0x28,
        (
            (Expr.PushLong, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x07,
        (
            (Expr.PushLong, 0x1770),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x34,
        (
            (Expr.PushLong, 0x13880),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1500, 0)
    CreateThread(0x000C, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    CreateThread(0x000D, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    FadeIn(2000, 0)
    CreateThread(0x000A, 0x03, 0x00, func_2A_8366)
    Sleep(500)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010301244V#1020F#6P──等、等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    CameraMove(-3640, 0, -5570, 0)
    OP_67(0, 4390, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(176000, 0)
    OP_6E(310, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010301245V#1005F#6P让我们收手是什么意思！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301246V将军难道还把我们游击士\n',
            '当作眼中钉吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600301247V#160F话不是这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301248V但是，那是连警备艇的导力炮\n',
            '也难以伤之分毫的魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301249V你们究竟能做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280769V#1026F#6P这，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7313',
    )

    ChrTalk(
        0x0105,
        (
            '#0060301251V#043F#6P将军……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600301252V#163F……即使是公主殿下\n',
            '我还是不能相让。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301253V#160F勇气和匹夫之勇是不同的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301254V公主殿下也看过柏斯和拉文努村\n',
            '所受到的损害了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301255V即使说这是一场战争\n',
            '也不为过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060301256V#049F#6P嗯嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_73DC')

    def _loc_7313(): pass

    label('loc_7313')

    ChrTalk(
        0x000A,
        (
            '#0600301257V#163F勇气和匹夫之勇是不同的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301258V#160F你们也目睹了柏斯和拉文努村\n',
            '所受到的损害了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301259V即使说这是一场战争\n',
            '也不为过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301260V#1003F#6P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_73DC(): pass

    label('loc_73DC')

    ChrTalk(
        0x000A,
        (
            '#0600301261V#163F常言道：术业有专攻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301262V既然是战争，\n',
            '还是交给我们专业人士为好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301263V#161F至于你们，对了……\n',
            '如能集中精力搜索『噬身之蛇』的据点\n',
            '就帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301264V#1005F#6P但、但是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, -10540, 0, -390, 135)
    ChrClearFlags(0x0009, 0x0080)

    NpcTalk(
        0x0009,
        '青年的声音',
        (
            '#0050301265V#1P……开什么玩笑………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_755E',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_759C')

    def _loc_755E(): pass

    label('loc_755E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7585',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_759C')

    def _loc_7585(): pass

    label('loc_7585')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_759C(): pass

    label('loc_759C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_75C3',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_7601')

    def _loc_75C3(): pass

    label('loc_75C3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_75EA',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_7601')

    def _loc_75EA(): pass

    label('loc_75EA')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_7601(): pass

    label('loc_7601')

    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_7628')
    def lambda_7628():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7628)

    @scena.Lambda('lambda_7636')
    def lambda_7636():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_7636)

    Sleep(50)

    @scena.Lambda('lambda_7649')
    def lambda_7649():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_7649)

    @scena.Lambda('lambda_7657')
    def lambda_7657():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_7657)

    Sleep(50)

    @scena.Lambda('lambda_766A')
    def lambda_766A():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_766A)

    @scena.Lambda('lambda_7678')
    def lambda_7678():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_7678')

    DispatchAsync2(0x0101, 0x0002, lambda_7678)

    @scena.Lambda('lambda_7689')
    def lambda_7689():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_7689')

    DispatchAsync2(0x00F8, 0x0002, lambda_7689)

    @scena.Lambda('lambda_769A')
    def lambda_769A():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_769A')

    DispatchAsync2(0x00F9, 0x0002, lambda_769A)

    @scena.Lambda('lambda_76AB')
    def lambda_76AB():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_76AB')

    DispatchAsync2(0x000A, 0x0002, lambda_76AB)

    @scena.Lambda('lambda_76BC')
    def lambda_76BC():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_76BC')

    DispatchAsync2(0x000B, 0x0002, lambda_76BC)

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetSubChip(0x000A, 0)
    ChrSetSubChip(0x000B, 0)
    ChrSetFlags(0x0009, 0x0020)
    CreateThread(0x0009, 0x00, 0x00, func_30_8483)
    CameraMove(-4720, 0, -5400, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010301266V#1004F#5P阿加特……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0000)
    ChrSetPos(0x0107, -11980, 0, 4770, 135)
    ChrClearFlags(0x0107, 0x0080)

    ChrTalk(
        0x0107,
        (
            '#0070301267V#1P阿、阿加特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0107, -5820, 0, -3840, 5000, 0x00)
    ChrTurnDirection(0x0107, 0x0009, 400)

    @scena.Lambda('lambda_779A')
    def lambda_779A():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_779A')

    DispatchAsync2(0x0107, 0x0002, lambda_779A)

    ChrTalk(
        0x0107,
        (
            '#0070301268V#065F#6P才刚刚做了急救，\n',
            '不可以逞强哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301269V#1286F#4P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000B, 0x02)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0107, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)
    TerminateThread(0x000A, 0x02)
    TerminateThread(0x000B, 0x02)

    ChrTalk(
        0x000A,
        (
            '#0600301270V#160F#5P……你是……\n',
            '『重剑』阿加特吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301271V听卡西乌斯说过\n',
            '你是个很有朝气的青年游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301272V#1282F#4P大叔的事先不说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301273V#1293F我说……将军阁下啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301274V你说术业有专攻……\n',
            '战争就交给专业人士……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301275V这句话……是认真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600301276V#163F#5P……当然是认真的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301277V#160F和保护人民的游击士不同，\n',
            '我们必须得保护国家才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301278V在这种情况下，所谓的国家\n',
            '指的是人民和国土两者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301279V能做到这件事的只有军队而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0050301280V#1291F#4P呵呵……保护人民和国土吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_7A73')
    def lambda_7A73():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_7A73')

    DispatchAsync2(0x0107, 0x0001, lambda_7A73)

    @scena.Lambda('lambda_7A84')
    def lambda_7A84():
        CameraMove(-4580, 0, -6170, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7A84)

    @scena.Lambda('lambda_7A9C')
    def lambda_7A9C():
        OP_99(0x00FE, 0x08, 0x0F, 1600)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7A9C)

    OP_92(0x0009, 0x000A, 600, 1500, 0x00)
    TerminateThread(0x0009, 0x01)
    Fade(250)
    CameraSetDistance(3000, 0)

    @scena.Lambda('lambda_7ACC')
    def lambda_7ACC():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_7ACC')

    DispatchAsync2(0x000B, 0x0002, lambda_7ACC)

    ChrSetFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 30)
    ChrSetSubChip(0x000A, 6)
    ChrSetChipByIndex(0x0009, 30)
    ChrSetSubChip(0x0009, 30)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301281V#1287F#4P#4S别惹人发笑了！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000A,
        (
            '#0600301282V#163F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301283V#1020F#6P等、等等！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301284V#065F#6P阿、阿加特哥哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x00, 0x00, func_33_8605)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0050301285V#1287F#4P每次、每次都是一样！！\n',
            '你们这些混账永远都不能及时赶到！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301286V只会说一些统一安排行动之类的废话！\n',
            '研究什么无聊战术，错过大好时机！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301287V没有命令就什么也做不到！\n',
            '能保护的东西都保护不了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301288V这次也是！\n',
            '１０年前的战争也是一样！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0600301289V#161F#5P！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301290V难不成，你是那时候的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x00, 0x00, func_33_8605)

    ChrTalk(
        0x0009,
        (
            '#0050301291V#1287F#4P可恶……谁会放心\n',
            '托付给你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301292V#1285F这次……只有这次……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301293V我……要亲手……\n',
            '守护米夏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0x00)
    Sleep(500)

    @scena.Lambda('lambda_7DEE')
    def lambda_7DEE():
        CameraMove(-4820, 0, -5480, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7DEE)

    @scena.Lambda('lambda_7E06')
    def lambda_7E06():
        OP_67(0, 6660, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7E06)

    @scena.Lambda('lambda_7E1E')
    def lambda_7E1E():
        CameraSetDistance(3010, 1500)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_7E1E)

    @scena.Lambda('lambda_7E2E')
    def lambda_7E2E():
        OP_6E(280, 1500)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_7E2E)

    ChrSetFlags(0x0009, 0x0800)

    @scena.Lambda('lambda_7E43')
    def lambda_7E43():
        OP_94(0x01, 0x00FE, 0x0000, 0xFFFFFF38, 0x000003E8, 0x01)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_7E43)

    @scena.Lambda('lambda_7E59')
    def lambda_7E59():
        OP_99(0x00FE, 0x0A, 0x0F, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_7E59)

    @scena.Lambda('lambda_7E69')
    def lambda_7E69():
        OP_94(0x01, 0x00FE, 0x0000, 0xFFFFFF38, 0x000003E8, 0x01)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7E69)

    @scena.Lambda('lambda_7E7F')
    def lambda_7E7F():
        OP_99(0x00FE, 0x22, 0x27, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_7E7F)

    Sleep(500)

    PlaySE(524, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070301294V#065F#6P阿加特哥哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300882V#1020F#6P等、等等！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x000A)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0600301296V#163F#5P……唔、伤口\n',
            '似乎没有裂开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301297V只是精神和体力耗尽\n',
            '昏过去了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301298V#063F#6P……阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301299V#1007F#6P真、真是的，\n',
            '吓死人了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000A, 0x0F, 0x11, 1000)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0600301300V#160F#5P总之，最好找个\n',
            '舒适的床铺让他睡一觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301301V他在村里有间房子，\n',
            '我就送他去拉文努村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301302V#1015F#6P啊，嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301303V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010301304V#1004F为、为什么您会知道\n',
            '阿加特的家在拉文努村呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0600301305V#160F#5P……我原来曾经\n',
            '见过这家伙一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600301306V那时候的少年……\n',
            '已经长得这么大了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301307V#1026F#6P那时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000A, 0x11, 0x13, 1000)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0600301308V#163F#5P『百日战役』结束以后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000A, 0x14, 0x17, 1000)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0600301309V#166F#5P建造这家伙的妹妹和村人们\n',
            '的墓碑时候的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070301310V#065F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 1, 0x1A81)),
            Expr.Return,
        ),
        'loc_8273',
    )

    ChrTalk(
        0x0101,
        (
            '#0010301311V#1020F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8296')

    def _loc_8273(): pass

    label('loc_8273')

    ChrTalk(
        0x0101,
        (
            '#0010301312V#1020F#6P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8296(): pass

    label('loc_8296')

    FadeOut(2000, 0, -1)
    OP_0D()
    FormationDelMember(0x06, 0xFF)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82BB',
    )

    FormationDelMember(0x02, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_82FD')

    def _loc_82BB(): pass

    label('loc_82BB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82D2',
    )

    FormationDelMember(0x03, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF7, 0xFF)

    Jump('loc_82FD')

    def _loc_82D2(): pass

    label('loc_82D2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82E9',
    )

    FormationDelMember(0x04, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF7, 0xFF)

    Jump('loc_82FD')

    def _loc_82E9(): pass

    label('loc_82E9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82FD',
    )

    FormationDelMember(0x07, 0xFF)
    FormationAddMember(ChrTable['金'], 0xF7, 0xFF)

    def _loc_82FD(): pass

    label('loc_82FD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8314',
    )

    FormationDelMember(0x02, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF8, 0xFF)

    Jump('loc_8356')

    def _loc_8314(): pass

    label('loc_8314')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_832B',
    )

    FormationDelMember(0x03, 0xFF)
    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)

    Jump('loc_8356')

    def _loc_832B(): pass

    label('loc_832B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8342',
    )

    FormationDelMember(0x04, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF8, 0xFF)

    Jump('loc_8356')

    def _loc_8342(): pass

    label('loc_8342')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8356',
    )

    FormationDelMember(0x07, 0xFF)
    FormationAddMember(ChrTable['金'], 0xF8, 0xFF)

    def _loc_8356(): pass

    label('loc_8356')

    SetScenaFlags(ScenaFlag(0x0350, 3, 0x1A83))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1201._SN', 108, 0, 0)
    IdleLoop()

    Return()

# id: 0x002A offset: 0x8366
@scena.Code('func_2A_8366')
def func_2A_8366():
    CreateThread(0x000E, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    CreateThread(0x000F, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    CreateThread(0x0010, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    CreateThread(0x0011, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    CreateThread(0x0012, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    CreateThread(0x0013, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    CreateThread(0x0014, 0x01, 0x00, func_2B_83C2)
    Sleep(800)

    CreateThread(0x0015, 0x01, 0x00, func_2B_83C2)

    Return()

# id: 0x002B offset: 0x83C2
@scena.Code('func_2B_83C2')
def func_2B_83C2():
    ChrSetChipByIndex(0x00FE, 4)
    ChrSetSubChip(0x00FE, 0)
    ChrSetPos(0x00FE, 6580, 0, -8930, 180)
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -1910, 0, -19020, 3000, 0x00)
    ChrWalkTo(0x00FE, -8340, 1300, -13680, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x002C offset: 0x841A
@scena.Code('func_2C_841A')
def func_2C_841A():
    ChrMoveTo(0x00FE, -5580, 0, -4230, 4000, 0x00)

    Return()

# id: 0x002D offset: 0x842F
@scena.Code('func_2D_842F')
def func_2D_842F():
    ChrMoveTo(0x00FE, -3500, 0, -4470, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x000A, 400)

    Return()

# id: 0x002E offset: 0x844B
@scena.Code('func_2E_844B')
def func_2E_844B():
    ChrWalkTo(0x00FE, -3680, 0, -2830, 4000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x002F offset: 0x8467
@scena.Code('func_2F_8467')
def func_2F_8467():
    ChrWalkTo(0x00FE, -2430, 0, -3990, 4000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0030 offset: 0x8483
@scena.Code('func_30_8483')
def func_30_8483():
    ChrSetPos(0x00FE, -10540, 0, -390, 135)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 8)

    @scena.Lambda('lambda_84AE')
    def lambda_84AE():
        OP_99(0x00FE, 0x08, 0x0F, 1600)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_84AE)

    OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000005DC, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_84D2')
    def lambda_84D2():
        OP_99(0x00FE, 0x08, 0x0F, 1600)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_84D2)

    OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000005DC, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_84F6')
    def lambda_84F6():
        OP_99(0x00FE, 0x08, 0x0F, 1600)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_84F6)

    OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000005DC, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_851A')
    def lambda_851A():
        OP_99(0x00FE, 0x08, 0x0F, 1600)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_851A)

    OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000005DC, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_853E')
    def lambda_853E():
        OP_99(0x00FE, 0x08, 0x0F, 1600)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_853E)

    OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000005DC, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_8562')
    def lambda_8562():
        OP_99(0x00FE, 0x08, 0x0F, 1600)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_8562)

    OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000005DC, 0x01)

    Return()

# id: 0x0031 offset: 0x857C
@scena.Code('func_31_857C')
def func_31_857C():
    @scena.Lambda('lambda_8582')
    def lambda_8582():
        OP_99(0x00FE, 0x08, 0x0F, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_8582)

    OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x01)
    Sleep(500)

    @scena.Lambda('lambda_85A6')
    def lambda_85A6():
        OP_99(0x00FE, 0x08, 0x0F, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_85A6)

    OP_94(0x00, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x01)

    Return()

# id: 0x0032 offset: 0x85C0
@scena.Code('func_32_85C0')
def func_32_85C0():
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 8)

    @scena.Lambda('lambda_85DA')
    def lambda_85DA():
        OP_99(0x00FE, 0x08, 0x0F, 1000)
        Yield()

        Jump('lambda_85DA')

    DispatchAsync2(0x00FE, 0x0001, lambda_85DA)

    ChrMoveTo(0x0009, -5400, 0, -5220, 1000, 0x00)
    TerminateThread(0x00FE, 0x01)
    ChrSetSubChip(0x00FE, 8)

    Return()

# id: 0x0033 offset: 0x8605
@scena.Code('func_33_8605')
def func_33_8605():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8698',
    )

    ChrSetSubChip(0x000A, 7)
    ChrSetSubChip(0x0009, 31)
    Sleep(100)

    ChrSetSubChip(0x000A, 8)
    ChrSetSubChip(0x0009, 32)
    Sleep(100)

    ChrSetSubChip(0x000A, 9)
    ChrSetSubChip(0x0009, 33)
    Sleep(100)

    ChrSetSubChip(0x000A, 7)
    ChrSetSubChip(0x0009, 31)
    Sleep(100)

    ChrSetSubChip(0x000A, 8)
    ChrSetSubChip(0x0009, 32)
    Sleep(100)

    ChrSetSubChip(0x000A, 9)
    ChrSetSubChip(0x0009, 33)
    Sleep(100)

    ChrSetSubChip(0x000A, 7)
    ChrSetSubChip(0x0009, 31)
    Sleep(100)

    ChrSetSubChip(0x000A, 8)
    ChrSetSubChip(0x0009, 32)
    Sleep(100)

    ChrSetSubChip(0x000A, 9)
    ChrSetSubChip(0x0009, 33)
    Sleep(500)

    Jump('func_33_8605')

    def _loc_8698(): pass

    label('loc_8698')

    Return()

# id: 0x0034 offset: 0x8699
@scena.Code('func_34_8699')
def func_34_8699():
    FadeOut(0, 0, -1)
    CameraMove(-41010, -360, 62470, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_8750'),
        (0x00000001, 'loc_8756'),
        (-1, 'loc_875C'),
    )

    def _loc_8750(): pass

    label('loc_8750')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_875C')

    def _loc_8756(): pass

    label('loc_8756')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_875C')

    def _loc_875C(): pass

    label('loc_875C')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['提妲'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['雪拉扎德'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
