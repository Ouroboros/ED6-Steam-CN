import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0810_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0810   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0810.x'
    header.mapIndex       = 1
    header.bgm            = 1
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/E0810._SN', 'ED6_DT21/E0810_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT27/CH04550._CH', 'ED6_DT27/CH04550P._CP'),
        ('ED6_DT27/CH04558._CH', 'ED6_DT27/CH04558P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT27/CH04510._CH', 'ED6_DT27/CH04510P._CP'),
        ('ED6_DT26/CH20363._CH', 'ED6_DT26/CH20363P._CP'),
        ('ED6_DT27/CH03550._CH', 'ED6_DT27/CH03550P._CP'),
        ('ED6_DT26/CH20341._CH', 'ED6_DT26/CH20341P._CP'),
        (None, 'ED6_DT26/CH20341P._CP'),
    ]

# id: 0x10001 offset: 0x10E
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
            name                = '尤莉亚上尉',
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
            name                = '奈尔',
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
            name                = '朵洛希',
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
            name                = '飞船',
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
            name                = '飞船',
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
            name                = '飞船',
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
            name                = '飞船',
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
            name                = '飞船',
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
            name                = '飞船',
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
            name                = '目标用照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0084,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
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
            name                = '目标',
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
            name                = '目标',
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
            name                = '目标',
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
            name                = '目标',
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
            name                = '怀斯曼教授',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458759,
            chipIndex           = 7,
            npcIndex            = 0x01E2,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '歼灭天使玲',
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
            name                = '帕蒂尔·玛蒂尔',
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
            name                = '幻想乐曲·德尔基昂',
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
            name                = '艾丝蒂尔',
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
            name                = '约修亚',
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
            name                = '卡西乌斯',
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
            name                = '基库',
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
            name                = '穆拉',
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
            name                = '拉赛尔博士',
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
            name                = '多伦',
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
            name                = '吉尔',
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
            name                = '阿加特',
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
            name                = '雪拉扎德',
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
            name                = '奥利维尔',
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
            name                = '科洛丝',
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
            name                = '提妲',
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
            name                = '金',
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
            name                = '凯文',
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
            name                = '乔丝特',
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
    )

# id: 0x10002 offset: 0x5EE
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x5EE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x5EE
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x5EE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 5, 0x10FD)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_60F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_18_30DF)

    Jump('loc_A39')

    def _loc_60F(): pass

    label('loc_60F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 6, 0x10FE)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_630',
    )

    ClearScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(1, 0x0000)

    Jump('loc_A39')

    def _loc_630(): pass

    label('loc_630')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_651',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_1C_3B9D)

    Jump('loc_A39')

    def _loc_651(): pass

    label('loc_651')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_672',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_1D_3DB9)

    Jump('loc_A39')

    def _loc_672(): pass

    label('loc_672')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_693',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    Event(0, func_1E_3FCF)

    Jump('loc_A39')

    def _loc_693(): pass

    label('loc_693')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6B4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    Event(0, func_1F_400D)

    Jump('loc_A39')

    def _loc_6B4(): pass

    label('loc_6B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D5',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    Event(0, func_23_4BC0)

    Jump('loc_A39')

    def _loc_6D5(): pass

    label('loc_6D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6F6',
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_28_558F)

    Jump('loc_A39')

    def _loc_6F6(): pass

    label('loc_6F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_717',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x77),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    Event(0, func_2E_5F41)

    Jump('loc_A39')

    def _loc_717(): pass

    label('loc_717')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 7, 0x10F7)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_738',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    Event(0, func_40_898B)

    Jump('loc_A39')

    def _loc_738(): pass

    label('loc_738')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 0, 0x10F8)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_759',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    Event(0, func_2B_5A12)

    Jump('loc_A39')

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 1, 0x10F9)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_77A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    Event(0, func_2C_5BCC)

    Jump('loc_A39')

    def _loc_77A(): pass

    label('loc_77A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 2, 0x10FA)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_79B',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x76),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    Event(0, func_46_96F3)

    Jump('loc_A39')

    def _loc_79B(): pass

    label('loc_79B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 3, 0x10FB)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7BC',
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_2D_5D86)

    Jump('loc_A39')

    def _loc_7BC(): pass

    label('loc_7BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 7, 0x10FF)),
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 4, 0x10FC)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7DD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    ClearScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    Event(0, func_48_9A7B)

    Jump('loc_A39')

    def _loc_7DD(): pass

    label('loc_7DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_7FC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(1, 0x0002)

    Jump('loc_A39')

    def _loc_7FC(): pass

    label('loc_7FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_81B',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(1, 0x0003)

    Jump('loc_A39')

    def _loc_81B(): pass

    label('loc_81B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_83A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(1, 0x0004)

    Jump('loc_A39')

    def _loc_83A(): pass

    label('loc_83A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_859',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(1, 0x000F)

    Jump('loc_A39')

    def _loc_859(): pass

    label('loc_859')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_878',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(1, 0x0014)

    Jump('loc_A39')

    def _loc_878(): pass

    label('loc_878')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_897',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(1, 0x0016)

    Jump('loc_A39')

    def _loc_897(): pass

    label('loc_897')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Return,
        ),
        'loc_8FB',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    OP_76(0x00FF, 0x00000000, 0x0001, 0, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, 0, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, 0, 0, 0, 0x00, 0x00)
    Event(1, 0x0019)

    Jump('loc_A39')

    def _loc_8FB(): pass

    label('loc_8FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 7, 0x10F7)),
            Expr.Return,
        ),
        'loc_911',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    MapSetFlags(0x10000000)
    Event(1, 0x001E)

    Jump('loc_A39')

    def _loc_911(): pass

    label('loc_911')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 0, 0x10F8)),
            Expr.Return,
        ),
        'loc_930',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    MapSetFlags(0x10000000)
    Event(0, func_1B_344B)

    Jump('loc_A39')

    def _loc_930(): pass

    label('loc_930')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 1, 0x10F9)),
            Expr.Return,
        ),
        'loc_94A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    Event(0, func_02_B65)

    Jump('loc_A39')

    def _loc_94A(): pass

    label('loc_94A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 2, 0x10FA)),
            Expr.Return,
        ),
        'loc_964',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    Event(0, func_11_2298)

    Jump('loc_A39')

    def _loc_964(): pass

    label('loc_964')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 3, 0x10FB)),
            Expr.Return,
        ),
        'loc_97E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    Event(0, func_13_2B25)

    Jump('loc_A39')

    def _loc_97E(): pass

    label('loc_97E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 4, 0x10FC)),
            Expr.Return,
        ),
        'loc_9DD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    OP_76(0x00FF, 0x00000000, 0x0001, -1, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -2, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -5, -2, 0, 0x00, 0x00)
    Event(0, func_19_327C)

    Jump('loc_A39')

    def _loc_9DD(): pass

    label('loc_9DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021F, 5, 0x10FD)),
            Expr.Return,
        ),
        'loc_A39',
    )

    ClearScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    OP_76(0x00FF, 0x00000000, 0x0001, -1, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -1, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -2, -1, 0, 0x00, 0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_2A_58DF)

    def _loc_A39(): pass

    label('loc_A39')

    Return()

# id: 0x0001 offset: 0xA3A
@scena.Code('func_01_A3A')
def func_01_A3A():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Return,
        ),
        'loc_A59',
    )

    OP_B1('E0800_7')

    Jump('loc_A88')

    def _loc_A59(): pass

    label('loc_A59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 1, 0x2239)),
            Expr.Return,
        ),
        'loc_A6C',
    )

    OP_B1('E0800_4')

    Jump('loc_A88')

    def _loc_A6C(): pass

    label('loc_A6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 0, 0x2200)),
            Expr.Return,
        ),
        'loc_A7F',
    )

    OP_B1('E0800_6')

    Jump('loc_A88')

    def _loc_A7F(): pass

    label('loc_A7F')

    OP_B1('E0800_5')

    def _loc_A88(): pass

    label('loc_A88')

    Jump('loc_B64')

    def _loc_A8B(): pass

    label('loc_A8B')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 6, 0x203E)),
            Expr.Return,
        ),
        'loc_AAA',
    )

    OP_B1('E0800_1')

    Jump('loc_ACE')

    def _loc_AAA(): pass

    label('loc_AAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 2, 0x2002)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 4, 0x2004)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 6, 0x2006)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_AC5',
    )

    OP_B1('E0800_2')

    Jump('loc_ACE')

    def _loc_AC5(): pass

    label('loc_AC5')

    OP_B1('E0800_2')

    def _loc_ACE(): pass

    label('loc_ACE')

    Jump('loc_B64')

    def _loc_AD1(): pass

    label('loc_AD1')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B28',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_AF0',
    )

    OP_B1('E0800_4')

    Jump('loc_B25')

    def _loc_AF0(): pass

    label('loc_AF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 1, 0x1E19)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 5, 0x1E1D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B08',
    )

    OP_B1('E0800_3')

    Jump('loc_B25')

    def _loc_B08(): pass

    label('loc_B08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 0, 0x1E00)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B1C',
    )

    OP_B1('E0800_2')

    Jump('loc_B25')

    def _loc_B1C(): pass

    label('loc_B1C')

    OP_B1('E0800_1')

    def _loc_B25(): pass

    label('loc_B25')

    Jump('loc_B64')

    def _loc_B28(): pass

    label('loc_B28')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 5, 0x1CA5)),
            Expr.Return,
        ),
        'loc_B48',
    )

    OP_B1('E0800_2y')

    Jump('loc_B58')

    def _loc_B48(): pass

    label('loc_B48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 5, 0x1C1D)),
            Expr.Return,
        ),
        'loc_B58',
    )

    OP_B1('E0800_2')

    def _loc_B58(): pass

    label('loc_B58')

    Jump('loc_B64')

    def _loc_B5B(): pass

    label('loc_B5B')

    OP_B1('E0800_1')
    def _loc_B64(): pass

    label('loc_B64')

    Return()

# id: 0x0002 offset: 0xB65
@scena.Code('func_02_B65')
def func_02_B65():
    EventBegin(0x00)
    OP_DB()
    OP_76(0x00FF, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -10, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -30, -5, 0, 0x00, 0x00)
    LoadEffect(0x00, 'monster\\\\msc0331.eff')
    LoadEffect(0x01, 'map\\\\mp077_00.eff')
    LoadEffect(0x02, 'map\\\\mp078_01.eff')
    CameraMove(-1460, 0, -1110, 0)
    OP_67(0, 6600, -10000, 0)
    CameraSetDistance(4050, 0)
    OP_6C(315000, 0)
    OP_6E(416, 0)
    OP_D0(360000, 0)
    PlaySE(451, 0x00, 0x64)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    OP_71(0x0001, 0x0004)
    OP_A1(0x000E, 0x0000)
    OP_A1(0x0010, 0x0002)
    OP_A1(0x0011, 0x0003)
    OP_A1(0x0012, 0x0004)
    ChrSetPos(0x000E, 0, -5000, 0, 270)
    ChrSetPos(0x0010, 136000, -5000, -50000, 270)
    ChrSetPos(0x0011, 136000, -5000, -50000, 270)
    ChrSetPos(0x0012, 136000, -5000, -50000, 270)
    ChrClearFlags(0x000E, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    ChrClearFlags(0x0012, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 30000, 0)
    OP_D1(0x0011, 0, 270000, 30000, 0)
    OP_D1(0x0012, 0, 270000, 30000, 0)
    PlaySE(121, 0x01, 0x64)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x64)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 900)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 800)
    OP_70(0x0003, 900)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 800)
    OP_70(0x0004, 900)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0D62')
    def lambda_0D62():
        CameraMove(-520, 0, -2050, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D62)

    @scena.Lambda('lambda_0D7A')
    def lambda_0D7A():
        OP_67(0, 2770, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D7A)

    WaitForThreadExit(0x0101, 0x0000)
    CreateThread(0x000E, 0x00, 0x00, func_06_1A07)

    @scena.Lambda('lambda_0D9E')
    def lambda_0D9E():
        CameraMove(-1790, 0, -9260, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D9E)

    @scena.Lambda('lambda_0DB6')
    def lambda_0DB6():
        OP_67(0, 2060, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DB6)

    @scena.Lambda('lambda_0DCE')
    def lambda_0DCE():
        OP_6C(280000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DCE)

    @scena.Lambda('lambda_0DDE')
    def lambda_0DDE():
        OP_D0(365000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DDE)

    Sleep(4000)

    @scena.Lambda('lambda_0DF3')
    def lambda_0DF3():
        OP_67(0, 6060, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0DF3)

    @scena.Lambda('lambda_0E0B')
    def lambda_0E0B():
        OP_6C(75000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E0B)

    @scena.Lambda('lambda_0E1B')
    def lambda_0E1B():
        OP_D0(350000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0E1B)

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_0E30')
    def lambda_0E30():
        OP_67(0, 2060, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0E30)

    WaitForThreadExit(0x0101, 0x0000)
    OP_E8(0x88, 0x13, 0x00, 0x00)
    PlayEffect(0x02, 0x00, 0x0010, 100, 1000, -11000, 184, 0, -26, 950, 950, 950, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x01, 0x0011, 100, 1000, -11000, 184, 0, -26, 950, 950, 950, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x02, 0x0012, 0, 1000, -11500, 183, 0, -26, 900, 900, 900, 0x00FF, 0, 0, 0, 0)
    OP_98(0x00, 0x0010)
    OP_98(0x01, 50000, -5000, 0)
    OP_98(0x01, -50000, -5000, 5000)
    CreateThread(0x0000, 0x00, 0x00, func_20_49D4)

    @scena.Lambda('lambda_0F18')
    def lambda_0F18():
        OP_98(0x02, 0x00FE, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0F18)

    Sleep(1000)

    @scena.Lambda('lambda_0F2D')
    def lambda_0F2D():
        OP_D1(0x00FE, 0, 270000, 0, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_0F2D)

    Sleep(1000)

    OP_98(0x00, 0x0011)
    OP_98(0x01, 50000, -5000, 5000)
    OP_98(0x01, -50000, -5000, 10000)

    @scena.Lambda('lambda_0F6C')
    def lambda_0F6C():
        OP_98(0x02, 0x00FE, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0F6C)

    Sleep(1000)

    @scena.Lambda('lambda_0F81')
    def lambda_0F81():
        OP_D1(0x00FE, 0, 270000, 0, 3000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_0F81)

    Sleep(1000)

    OP_98(0x00, 0x0012)
    OP_98(0x01, 50000, -5000, -5000)
    OP_98(0x01, -50000, -5000, 0)

    @scena.Lambda('lambda_0FC0')
    def lambda_0FC0():
        OP_98(0x02, 0x00FE, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0FC0)

    Sleep(500)

    @scena.Lambda('lambda_0FD5')
    def lambda_0FD5():
        OP_D1(0x00FE, 0, 270000, -30000, 6000)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_0FD5)

    Sleep(2500)

    FadeOut(500, 0, -1)
    OP_0D()
    OP_24(0x0235, 0x00)
    TerminateThread(0x0000, 0x00)
    OP_23(0x0235)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0010, 0x03)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0011, 0x03)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0012, 0x03)
    ChrSetPos(0x000E, -25000, 0, 0, 270)
    ChrSetPos(0x0010, 125000, -6000, 0, 270)
    ChrSetPos(0x0011, 135000, -2000, 15000, 270)
    ChrSetPos(0x0012, 135000, -8000, -15000, 270)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 10000, 0)
    OP_D1(0x0012, 0, 270000, -10000, 0)
    OP_B0(0x0000, 0x3C)
    OP_76(0x00FF, 0x00000000, 0x0001, -20, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -20, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -40, -5, 0, 0x00, 0x00)
    CameraMove(88140, -3850, 0, 0)
    OP_67(0, 2000, -10000, 0)
    CameraSetDistance(4050, 0)
    OP_6C(282000, 0)
    OP_6E(1045, 0)
    OP_D0(365000, 0)
    PlayEffect(0x02, 0x00, 0x0010, -800, 1500, -12000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x01, 0x0011, 500, 500, -11000, 180, 2, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x02, 0x0012, 700, 400, -12000, 182, 3, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    FadeIn(500, 0)

    @scena.Lambda('lambda_11EE')
    def lambda_11EE():
        ChrMoveTo(0x00FE, 0, 0, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_11EE)

    @scena.Lambda('lambda_1209')
    def lambda_1209():
        ChrMoveTo(0x00FE, 50000, -6000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1209)

    @scena.Lambda('lambda_1224')
    def lambda_1224():
        ChrMoveTo(0x00FE, 55000, -2000, 15000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1224)

    @scena.Lambda('lambda_123F')
    def lambda_123F():
        ChrMoveTo(0x00FE, 55000, -8000, -15000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_123F)

    CreateThread(0x0000, 0x00, 0x00, func_20_49D4)
    Sleep(6000)

    @scena.Lambda('lambda_1266')
    def lambda_1266():
        OP_6C(306000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1266)

    StopEffect(0x02, 0x00)
    StopEffect(0x05, 0x00)
    CreateThread(0x0012, 0x00, 0x00, func_03_1745)
    Sleep(1500)

    PlayEffect(0x01, 0xFF, 0x00FF, 95000, -5000, -15000, 270, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0101, 0x0000)
    StopEffect(0x00, 0x00)
    StopEffect(0x03, 0x00)
    StopEffect(0x01, 0x00)
    StopEffect(0x04, 0x00)
    TerminateThread(0x0000, 0x00)
    OP_23(0x0235)
    CreateThread(0x0010, 0x00, 0x00, func_0B_1EC7)
    Sleep(1000)

    Fade(500)
    CameraMove(430, -3850, 8540, 0)
    OP_6C(29000, 0)
    OP_D0(360000, 0)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0011, 0x01)
    ChrSetPos(0x0010, 100000, -8000, 0, 270)
    ChrSetPos(0x0011, 105000, -6000, 15000, 270)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)

    @scena.Lambda('lambda_1359')
    def lambda_1359():
        OP_D1(0x00FE, 0, 245000, 20000, 10000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_1359)

    OP_98(0x00, 0x0010)
    OP_98(0x01, 35540, 0, 26780)
    OP_98(0x01, -30540, 0, 780)

    @scena.Lambda('lambda_1393')
    def lambda_1393():
        OP_98(0x02, 0x00FE, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1393)

    @scena.Lambda('lambda_13A3')
    def lambda_13A3():
        OP_D1(0x00FE, 0, 235000, 20000, 8000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_13A3)

    OP_98(0x00, 0x0011)
    OP_98(0x01, 40540, 0, 46780)
    OP_98(0x01, -20540, 0, 15780)

    @scena.Lambda('lambda_13DD')
    def lambda_13DD():
        OP_98(0x02, 0x00FE, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_13DD)

    @scena.Lambda('lambda_13ED')
    def lambda_13ED():
        CameraMove(6320, -2850, 15060, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13ED)

    @scena.Lambda('lambda_1405')
    def lambda_1405():
        OP_6C(54000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1405)

    @scena.Lambda('lambda_1415')
    def lambda_1415():
        OP_D0(380000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1415)

    @scena.Lambda('lambda_1425')
    def lambda_1425():
        OP_67(0, 3150, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1425)

    ChrSetPos(0x000E, 0, 0, 0, 270)

    @scena.Lambda('lambda_144E')
    def lambda_144E():
        OP_D1(0x00FE, 0, 290000, 35000, 100)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_144E)

    CreateThread(0x000E, 0x00, 0x00, func_07_1AFD)
    WaitForThreadExit(0x000E, 0x0003)

    @scena.Lambda('lambda_1474')
    def lambda_1474():
        OP_D1(0x00FE, 0, 270000, 0, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_1474)

    Sleep(1000)

    @scena.Lambda('lambda_1493')
    def lambda_1493():
        OP_D1(0x00FE, 0, 250000, -35000, 1400)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_1493)

    CreateThread(0x000E, 0x00, 0x00, func_08_1B79)
    WaitForThreadExit(0x000E, 0x0003)

    @scena.Lambda('lambda_14B9')
    def lambda_14B9():
        OP_D1(0x00FE, 0, 270000, 0, 6000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_14B9)

    Sleep(2000)

    Sleep(1000)

    CreateThread(0x0000, 0x00, 0x00, func_20_49D4)
    PlayEffect(0x02, 0x00, 0x0010, 0, 1000, -12000, 160, 3, -30, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    PlayEffect(0x02, 0x01, 0x0011, 1300, 1200, -12000, 152, 0, -30, 900, 900, 900, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    @scena.Lambda('lambda_1558')
    def lambda_1558():
        CameraMove(-27950, -3850, -25800, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1558)

    @scena.Lambda('lambda_1570')
    def lambda_1570():
        OP_6C(125000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1570)

    @scena.Lambda('lambda_1580')
    def lambda_1580():
        OP_67(0, 3800, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1580)

    @scena.Lambda('lambda_1598')
    def lambda_1598():
        OP_D0(340000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1598)

    @scena.Lambda('lambda_15A8')
    def lambda_15A8():
        OP_D1(0x00FE, 0, 270000, 20000, 5000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_15A8)

    CreateThread(0x000E, 0x00, 0x00, func_0A_1DAB)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0010, 0x03)
    OP_72(0x0002, 0x0004)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0011, 0x03)
    OP_72(0x0003, 0x0004)
    PlayEffect(0x02, 0x00, 0x0010, 500, 1000, -12000, 150, 0, -30, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlayEffect(0x02, 0x01, 0x0011, 500, 1000, -12000, 130, 0, -30, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    TerminateThread(0x0012, 0x00)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0012, 0x03)
    ChrSetPos(0x0012, 8000, -4000, -56000, 270)
    OP_71(0x0004, 0x0004)
    OP_D1(0x0012, -5000, 300000, -30000, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -17000, -5000, -41000, 280, 0, 0, 2500, 2500, 2500, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_72(0x0004, 0x0004)
    PlayEffect(0x02, 0x03, 0x0012, 500, 1000, -9000, 210, 0, 20, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    CreateThread(0x0012, 0x00, 0x00, func_05_18B1)
    Sleep(2000)

    CreateThread(0x000E, 0x00, 0x00, func_09_1CB5)
    Sleep(1000)

    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    NewScene('ED6_DT21/E0610._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1745
@scena.Code('func_03_1745')
def func_03_1745():
    @scena.Lambda('lambda_174B')
    def lambda_174B():
        OP_D1(0x00FE, 0, 270000, 30000, 4000)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_174B)

    @scena.Lambda('lambda_1765')
    def lambda_1765():
        ChrMoveTo(0x00FE, 55000, -30000, -15000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1765)

    Sleep(700)

    @scena.Lambda('lambda_1785')
    def lambda_1785():
        ChrMoveTo(0x00FE, 55000, -30000, -15000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1785)

    Sleep(600)

    @scena.Lambda('lambda_17A5')
    def lambda_17A5():
        ChrMoveTo(0x00FE, 55000, -30000, -15000, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_17A5)

    Sleep(500)

    @scena.Lambda('lambda_17C5')
    def lambda_17C5():
        ChrMoveTo(0x00FE, 55000, -30000, -15000, 17000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_17C5)

    Sleep(400)

    @scena.Lambda('lambda_17E5')
    def lambda_17E5():
        ChrMoveTo(0x00FE, 55000, -30000, -15000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_17E5)

    Sleep(300)

    @scena.Lambda('lambda_1805')
    def lambda_1805():
        ChrMoveTo(0x00FE, 55000, -30000, -15000, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1805)

    Sleep(200)

    @scena.Lambda('lambda_1825')
    def lambda_1825():
        ChrMoveTo(0x00FE, 55000, -30000, -15000, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1825)

    Sleep(100)

    @scena.Lambda('lambda_1845')
    def lambda_1845():
        ChrMoveTo(0x00FE, 55000, -30000, -15000, 34000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1845)

    Return()

# id: 0x0004 offset: 0x185B
@scena.Code('func_04_185B')
def func_04_185B():
    @scena.Lambda('lambda_1861')
    def lambda_1861():
        OP_D1(0x00FE, 0, 300000, -20000, 1500)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_1861)

    @scena.Lambda('lambda_187B')
    def lambda_187B():
        ChrMoveTo(0x00FE, 25000, -2000, -20000, 80000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_187B)

    Sleep(1500)

    @scena.Lambda('lambda_189B')
    def lambda_189B():
        ChrMoveTo(0x00FE, -100000, -4000, 70000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_189B)

    Return()

# id: 0x0005 offset: 0x18B1
@scena.Code('func_05_18B1')
def func_05_18B1():
    @scena.Lambda('lambda_18B7')
    def lambda_18B7():
        ChrMoveTo(0x00FE, 3000, -2000, -51000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_18B7)

    Sleep(2500)

    @scena.Lambda('lambda_18D7')
    def lambda_18D7():
        OP_D1(0x00FE, -10000, 300000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_18D7)

    @scena.Lambda('lambda_18F1')
    def lambda_18F1():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_18F1)

    Sleep(200)

    @scena.Lambda('lambda_1911')
    def lambda_1911():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1911)

    Sleep(200)

    @scena.Lambda('lambda_1931')
    def lambda_1931():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1931)

    Sleep(200)

    @scena.Lambda('lambda_1951')
    def lambda_1951():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1951)

    Sleep(200)

    @scena.Lambda('lambda_1971')
    def lambda_1971():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1971)

    Sleep(200)

    @scena.Lambda('lambda_1991')
    def lambda_1991():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1991)

    Sleep(200)

    @scena.Lambda('lambda_19B1')
    def lambda_19B1():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_19B1)

    Sleep(200)

    @scena.Lambda('lambda_19D1')
    def lambda_19D1():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_19D1)

    Sleep(200)

    @scena.Lambda('lambda_19F1')
    def lambda_19F1():
        ChrMoveTo(0x00FE, -150000, -4000, 70000, 36000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_19F1)

    Return()

# id: 0x0006 offset: 0x1A07
@scena.Code('func_06_1A07')
def func_06_1A07():
    @scena.Lambda('lambda_1A0D')
    def lambda_1A0D():
        OP_D1(0x00FE, 0, 270000, 30000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1A0D)

    @scena.Lambda('lambda_1A27')
    def lambda_1A27():
        ChrMoveTo(0x00FE, -300000, -5000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1A27)

    Sleep(200)

    @scena.Lambda('lambda_1A47')
    def lambda_1A47():
        ChrMoveTo(0x00FE, -300000, -5000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1A47)

    Sleep(200)

    @scena.Lambda('lambda_1A67')
    def lambda_1A67():
        ChrMoveTo(0x00FE, -300000, -5000, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1A67)

    Sleep(200)

    @scena.Lambda('lambda_1A87')
    def lambda_1A87():
        ChrMoveTo(0x00FE, -300000, -5000, 0, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1A87)

    Sleep(200)

    @scena.Lambda('lambda_1AA7')
    def lambda_1AA7():
        ChrMoveTo(0x00FE, -300000, -5000, 0, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1AA7)

    Sleep(200)

    @scena.Lambda('lambda_1AC7')
    def lambda_1AC7():
        ChrMoveTo(0x00FE, -300000, -5000, 0, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1AC7)

    Sleep(200)

    @scena.Lambda('lambda_1AE7')
    def lambda_1AE7():
        ChrMoveTo(0x00FE, -300000, -5000, 0, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1AE7)

    Return()

# id: 0x0007 offset: 0x1AFD
@scena.Code('func_07_1AFD')
def func_07_1AFD():
    @scena.Lambda('lambda_1B03')
    def lambda_1B03():
        ChrMoveTo(0x00FE, 0, -4000, -8000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B03)

    Sleep(300)

    @scena.Lambda('lambda_1B23')
    def lambda_1B23():
        ChrMoveTo(0x00FE, 0, -4000, -8000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B23)

    Sleep(100)

    @scena.Lambda('lambda_1B43')
    def lambda_1B43():
        ChrMoveTo(0x00FE, 0, -4000, -8000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B43)

    Sleep(100)

    @scena.Lambda('lambda_1B63')
    def lambda_1B63():
        ChrMoveTo(0x00FE, 0, -4000, -8000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B63)

    Return()

# id: 0x0008 offset: 0x1B79
@scena.Code('func_08_1B79')
def func_08_1B79():
    @scena.Lambda('lambda_1B7F')
    def lambda_1B7F():
        ChrMoveTo(0x00FE, -3000, -4000, 9000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B7F)

    Sleep(100)

    @scena.Lambda('lambda_1B9F')
    def lambda_1B9F():
        ChrMoveTo(0x00FE, -3000, -4000, 9000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B9F)

    Sleep(100)

    @scena.Lambda('lambda_1BBF')
    def lambda_1BBF():
        ChrMoveTo(0x00FE, -3000, -4000, 9000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1BBF)

    Sleep(100)

    @scena.Lambda('lambda_1BDF')
    def lambda_1BDF():
        ChrMoveTo(0x00FE, -3000, -4000, 9000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1BDF)

    Sleep(100)

    @scena.Lambda('lambda_1BFF')
    def lambda_1BFF():
        ChrMoveTo(0x00FE, -3000, -4000, 9000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1BFF)

    Sleep(600)

    @scena.Lambda('lambda_1C1F')
    def lambda_1C1F():
        ChrMoveTo(0x00FE, -3000, -4000, 6000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1C1F)

    Sleep(100)

    @scena.Lambda('lambda_1C3F')
    def lambda_1C3F():
        ChrMoveTo(0x00FE, -3000, -4000, 6000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1C3F)

    Sleep(100)

    @scena.Lambda('lambda_1C5F')
    def lambda_1C5F():
        ChrMoveTo(0x00FE, -3000, -4000, 6000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1C5F)

    Sleep(100)

    @scena.Lambda('lambda_1C7F')
    def lambda_1C7F():
        ChrMoveTo(0x00FE, -3000, -4000, 6000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1C7F)

    Sleep(100)

    @scena.Lambda('lambda_1C9F')
    def lambda_1C9F():
        ChrMoveTo(0x00FE, -3000, -4000, 6000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1C9F)

    Return()

# id: 0x0009 offset: 0x1CB5
@scena.Code('func_09_1CB5')
def func_09_1CB5():
    @scena.Lambda('lambda_1CBB')
    def lambda_1CBB():
        OP_D1(0x00FE, 0, 250000, -40000, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_1CBB)

    @scena.Lambda('lambda_1CD5')
    def lambda_1CD5():
        ChrMoveTo(0x00FE, -100000, -4000, 60000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1CD5)

    Sleep(200)

    @scena.Lambda('lambda_1CF5')
    def lambda_1CF5():
        ChrMoveTo(0x00FE, -100000, -4000, 60000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1CF5)

    Sleep(200)

    @scena.Lambda('lambda_1D15')
    def lambda_1D15():
        ChrMoveTo(0x00FE, -100000, -4000, 60000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D15)

    Sleep(200)

    @scena.Lambda('lambda_1D35')
    def lambda_1D35():
        ChrMoveTo(0x00FE, -100000, -4000, 60000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D35)

    Sleep(200)

    @scena.Lambda('lambda_1D55')
    def lambda_1D55():
        ChrMoveTo(0x00FE, -100000, -4000, 60000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D55)

    Sleep(200)

    @scena.Lambda('lambda_1D75')
    def lambda_1D75():
        ChrMoveTo(0x00FE, -100000, -4000, 60000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D75)

    Sleep(200)

    @scena.Lambda('lambda_1D95')
    def lambda_1D95():
        ChrMoveTo(0x00FE, -100000, -4000, 60000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D95)

    Return()

# id: 0x000A offset: 0x1DAB
@scena.Code('func_0A_1DAB')
def func_0A_1DAB():
    @scena.Lambda('lambda_1DB1')
    def lambda_1DB1():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DB1)

    Sleep(200)

    @scena.Lambda('lambda_1DD1')
    def lambda_1DD1():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DD1)

    Sleep(200)

    @scena.Lambda('lambda_1DF1')
    def lambda_1DF1():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DF1)

    Sleep(200)

    @scena.Lambda('lambda_1E11')
    def lambda_1E11():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E11)

    Sleep(3600)

    @scena.Lambda('lambda_1E31')
    def lambda_1E31():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E31)

    Sleep(200)

    @scena.Lambda('lambda_1E51')
    def lambda_1E51():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E51)

    Sleep(200)

    @scena.Lambda('lambda_1E71')
    def lambda_1E71():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E71)

    Sleep(200)

    @scena.Lambda('lambda_1E91')
    def lambda_1E91():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1E91)

    Sleep(200)

    @scena.Lambda('lambda_1EB1')
    def lambda_1EB1():
        ChrMoveTo(0x00FE, -35000, -4000, -15000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1EB1)

    Return()

# id: 0x000B offset: 0x1EC7
@scena.Code('func_0B_1EC7')
def func_0B_1EC7():
    PlayEffect(0x00, 0x00, 0x0010, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -2000, -5000, 0)
    Sleep(400)

    PlayEffect(0x00, 0x01, 0x0010, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -4000, 5000, 0)
    Sleep(200)

    PlayEffect(0x00, 0x02, 0x0011, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, 0, 10000, 0)
    Sleep(300)

    PlayEffect(0x00, 0x03, 0x0011, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -6000, 10000, 0)
    Sleep(500)

    PlayEffect(0x00, 0x04, 0x0010, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -14000, -4000, 0)
    Sleep(400)

    PlayEffect(0x00, 0x05, 0x0010, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -12000, -6000, 0)
    Sleep(200)

    PlayEffect(0x00, 0x06, 0x0011, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -14000, -12000, 0)
    Sleep(400)

    PlayEffect(0x00, 0x07, 0x0011, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -16000, -20000, 0)

    Return()

# id: 0x000C offset: 0x2093
@scena.Code('func_0C_2093')
def func_0C_2093():
    PlayEffect(0x00, 0x00, 0x0010, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -2000, 0, 0)
    Sleep(400)

    PlayEffect(0x00, 0x01, 0x0010, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -4000, 5000, 0)

    Return()

# id: 0x000D offset: 0x2103
@scena.Code('func_0D_2103')
def func_0D_2103():
    Sleep(600)

    PlayEffect(0x00, 0x02, 0x0011, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x00, 0x03, 0x0011, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -6000, 10000, 0)

    Return()

# id: 0x000E offset: 0x2178
@scena.Code('func_0E_2178')
def func_0E_2178():
    PlayEffect(0x00, 0x04, 0x0010, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -4000, -4000, 0)
    Sleep(400)

    PlayEffect(0x00, 0x05, 0x0010, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -2000, -6000, 0)

    Return()

# id: 0x000F offset: 0x21E8
@scena.Code('func_0F_21E8')
def func_0F_21E8():
    Sleep(600)

    PlayEffect(0x00, 0x06, 0x0011, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -4000, -8000, 0)
    Sleep(400)

    PlayEffect(0x00, 0x07, 0x0011, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -6000, -10000, 0)

    Return()

# id: 0x0010 offset: 0x225D
@scena.Code('func_10_225D')
def func_10_225D():
    Sleep(1400)

    PlayEffect(0x00, 0x05, 0x0012, 0, 2000, 0, 0, 0, 0, 3000, 3000, 3000, 0x000E, -50000, -2000, -6000, 0)

    Return()

# id: 0x0011 offset: 0x2298
@scena.Code('func_11_2298')
def func_11_2298():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x00, 'battle\\\\btbomb00.eff')
    LoadEffect(0x01, 'map\\\\mpsmk0.eff')
    LoadEffect(0x02, 'map\\\\mp077_00.eff')
    CameraMove(81300, -9500, 23840, 0)
    OP_67(0, 4140, -10000, 0)
    CameraSetDistance(5040, 0)
    OP_6C(71000, 0)
    OP_6E(869, 0)
    OP_D0(360000, 0)
    PlaySE(451, 0x00, 0x64)
    OP_76(0x00FF, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -20, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -40, -5, 0, 0x00, 0x00)
    OP_A1(0x000E, 0x0000)
    OP_A1(0x000F, 0x0001)
    OP_A1(0x0010, 0x0002)
    OP_A1(0x0011, 0x0003)
    OP_A1(0x0012, 0x0004)
    ChrSetPos(0x000F, 250000, 10000, 15000, 270)
    ChrSetPos(0x000E, 0, 0, 0, 270)
    ChrSetPos(0x0010, 50000, 0, 0, 270)
    ChrSetPos(0x0011, 60000, 0, 15000, 270)
    ChrSetPos(0x0012, 60000, 0, -15000, 270)
    ChrClearFlags(0x000E, 0x0100)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    ChrClearFlags(0x0012, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)
    OP_D1(0x0012, 0, 270000, 0, 0)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 900)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 360)
    OP_70(0x0001, 460)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 800)
    OP_70(0x0003, 900)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 800)
    OP_70(0x0004, 900)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0004, 0x0004)
    PlaySE(121, 0x01, 0x5A)
    FadeIn(1000, 0)
    OP_0D()
    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0011, 0x00, 0x00, func_12_27CC)
    Sleep(3700)

    PlayEffect(0x02, 0xFF, 0x00FF, 45000, -5000, 15000, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)
    WaitForThreadExit(0x0011, 0x0000)
    WaitForThreadExit(0x0011, 0x0001)
    OP_72(0x0001, 0x0004)
    MapSetFlags(0x00000010)

    @scena.Lambda('lambda_253D')
    def lambda_253D():
        CameraMove(50100, -8000, 13150, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_253D)

    @scena.Lambda('lambda_2555')
    def lambda_2555():
        OP_67(0, 2880, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2555)

    @scena.Lambda('lambda_256D')
    def lambda_256D():
        OP_D0(355000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_256D)

    @scena.Lambda('lambda_257D')
    def lambda_257D():
        OP_D1(0x00FE, 0, 270000, -30000, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_257D)

    OP_98(0x00, 0x000F)
    OP_98(0x01, 150000, -8000, 15000)
    OP_98(0x01, 50000, -8000, 15000)
    OP_98(0x01, -50000, -8000, 15000)

    @scena.Lambda('lambda_25C5')
    def lambda_25C5():
        OP_98(0x02, 0x00FE, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_25C5)

    Sleep(4800)

    TerminateThread(0x000F, 0x01)
    Fade(1000)
    CameraMove(30780, -300, 10150, 0)
    CameraSetDistance(2410, 0)
    OP_6C(50000, 0)
    OP_6E(869, 0)
    ChrSetPos(0x000E, 10000, 0, 0, 270)
    OP_D1(0x000E, 0, 270000, -10000, 0)
    ChrSetPos(0x000F, 100000, -4000, 30000, 270)
    OP_D1(0x000F, 0, 270000, 0, 0)

    @scena.Lambda('lambda_2657')
    def lambda_2657():
        CameraMove(-9720, 3450, 2950, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2657)

    @scena.Lambda('lambda_266F')
    def lambda_266F():
        OP_6C(47000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_266F)

    @scena.Lambda('lambda_267F')
    def lambda_267F():
        ChrMoveTo(0x00FE, -100000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_267F)

    @scena.Lambda('lambda_269A')
    def lambda_269A():
        OP_D1(0x00FE, 0, 270000, 20000, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_269A)

    @scena.Lambda('lambda_26B4')
    def lambda_26B4():
        ChrMoveTo(0x00FE, 0, -4000, 30000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_26B4)

    Sleep(1500)

    @scena.Lambda('lambda_26D4')
    def lambda_26D4():
        ChrMoveTo(0x00FE, 0, -4000, 30000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_26D4)

    Sleep(400)

    @scena.Lambda('lambda_26F4')
    def lambda_26F4():
        ChrMoveTo(0x00FE, 0, -4000, 30000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_26F4)

    Sleep(400)

    @scena.Lambda('lambda_2714')
    def lambda_2714():
        ChrMoveTo(0x00FE, 0, -4000, 30000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2714)

    Sleep(400)

    @scena.Lambda('lambda_2734')
    def lambda_2734():
        ChrMoveTo(0x00FE, 0, -4000, 30000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2734)

    Sleep(400)

    @scena.Lambda('lambda_2754')
    def lambda_2754():
        ChrMoveTo(0x00FE, 0, -4000, 30000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2754)

    Sleep(400)

    @scena.Lambda('lambda_2774')
    def lambda_2774():
        ChrMoveTo(0x00FE, 0, -4000, 30000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2774)

    Sleep(400)

    @scena.Lambda('lambda_2794')
    def lambda_2794():
        ChrMoveTo(0x00FE, -100000, -4000, 30000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2794)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    NewScene('ED6_DT21/E0610._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x27CC
@scena.Code('func_12_27CC')
def func_12_27CC():
    PlayEffect(0x01, 0x00, 0x0011, 0, -5000, -3000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1000, -3000, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_283C')
    def lambda_283C():
        ChrMoveToRelativeAsync(0x00FE, 2000, -1000, 2000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_283C)

    OP_D1(0x00FE, 5000, 274000, 5000, 200)
    OP_D1(0x00FE, 5000, 270000, 0, 300)
    OP_D1(0x00FE, 5000, 272000, 3000, 300)
    PlayEffect(0x01, 0x01, 0x0011, 0, -5000, 3000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 3000, 4000, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_28FA')
    def lambda_28FA():
        ChrMoveToRelativeAsync(0x00FE, -1000, -1000, -2000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_28FA)

    OP_D1(0x00FE, 8000, 262000, -8000, 200)
    OP_D1(0x00FE, 2000, 268000, 0, 300)
    OP_D1(0x00FE, 6000, 264000, -6000, 300)
    PlayEffect(0x01, 0x02, 0x0011, -6000, -2000, 1000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0011, 2000, -2000, -1000, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_29B8')
    def lambda_29B8():
        ChrMoveToRelativeAsync(0x00FE, 1000, -4000, 1000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_29B8)

    OP_D1(0x00FE, 8000, 284000, 10000, 200)
    OP_D1(0x00FE, 5000, 270000, -4000, 200)
    OP_D1(0x00FE, 7000, 280000, 6000, 200)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_2A15')
    def lambda_2A15():
        CameraMove(50100, -10000, 13150, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2A15)

    @scena.Lambda('lambda_2A2D')
    def lambda_2A2D():
        OP_67(0, 8029, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A2D)

    @scena.Lambda('lambda_2A45')
    def lambda_2A45():
        CameraSetDistance(2350, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A45)

    @scena.Lambda('lambda_2A55')
    def lambda_2A55():
        OP_D1(0x00FE, 7000, 280000, -30000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2A55)

    @scena.Lambda('lambda_2A6F')
    def lambda_2A6F():
        ChrMoveTo(0x00FE, 60000, -30000, 15000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2A6F)

    Sleep(500)

    @scena.Lambda('lambda_2A8F')
    def lambda_2A8F():
        ChrMoveTo(0x00FE, 60000, -30000, 15000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2A8F)

    Sleep(400)

    @scena.Lambda('lambda_2AAF')
    def lambda_2AAF():
        ChrMoveTo(0x00FE, 60000, -30000, 15000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2AAF)

    Sleep(300)

    @scena.Lambda('lambda_2ACF')
    def lambda_2ACF():
        ChrMoveTo(0x00FE, 60000, -30000, 15000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2ACF)

    Sleep(200)

    @scena.Lambda('lambda_2AEF')
    def lambda_2AEF():
        ChrMoveTo(0x00FE, 60000, -30000, 15000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2AEF)

    Sleep(100)

    @scena.Lambda('lambda_2B0F')
    def lambda_2B0F():
        ChrMoveTo(0x00FE, 60000, -30000, 15000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2B0F)

    Return()

# id: 0x0013 offset: 0x2B25
@scena.Code('func_13_2B25')
def func_13_2B25():
    EventBegin(0x00)
    OP_DB()
    OP_A1(0x000E, 0x0000)
    OP_A1(0x000F, 0x0001)
    OP_A1(0x0010, 0x0002)
    OP_A1(0x0011, 0x0003)
    ChrSetPos(0x000F, 150000, -2000, 8000, 270)
    ChrSetPos(0x000E, 150000, 0, -8000, 270)
    ChrSetPos(0x0010, 300000, 0, -9300, 270)
    ChrSetPos(0x0011, 300000, 0, 6700, 270)
    ChrClearFlags(0x000E, 0x0100)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 800)
    OP_70(0x0000, 900)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 360)
    OP_70(0x0001, 460)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 800)
    OP_70(0x0003, 900)
    OP_71(0x0004, 0x0004)
    PlaySE(121, 0x01, 0x5A)
    CameraMove(-68280, 2400, -1300, 0)
    OP_67(0, 2170, -10000, 0)
    CameraSetDistance(2390, 0)
    OP_6C(90000, 0)
    OP_6E(869, 0)
    PlaySE(451, 0x00, 0x64)
    OP_76(0x00FF, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -6, -3, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -15, -6, 0, 0x00, 0x00)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_2CCC')
    def lambda_2CCC():
        OP_67(0, -2830, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2CCC)

    CreateThread(0x000E, 0x00, 0x00, func_14_2EE7)
    CreateThread(0x000F, 0x00, 0x00, func_15_2F65)
    CreateThread(0x0010, 0x00, 0x00, func_16_2FE3)
    CreateThread(0x0011, 0x00, 0x00, func_17_3061)
    Sleep(6000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(3000)

    OP_20(0x00000BB8)
    OP_21()
    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    PlayBGM(1)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x000E, 0, 0, 0, 270)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 700)
    OP_70(0x0000, 780)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_24(0x0079, 0x46)
    OP_24(0x01C3, 0x5A)
    OP_76(0x00FF, 0x00000000, 0x0001, -2, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -3, -1, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -8, -3, 0, 0x00, 0x00)
    CameraMove(-13440, -10000, -2430, 0)
    OP_67(0, 11980, -10000, 0)
    CameraSetDistance(10090, 0)
    OP_6C(250000, 0)
    OP_6E(473, 0)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 455000, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_2E29')
    def lambda_2E29():
        OP_67(0, 12960, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E29)

    @scena.Lambda('lambda_2E41')
    def lambda_2E41():
        CameraSetDistance(5620, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E41)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetPos(0x000E, 40000, 0, 0, 270)

    @scena.Lambda('lambda_2E67')
    def lambda_2E67():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_2E67)

    Fade(1000)
    CameraMove(24340, -10000, -15770, 0)
    OP_67(0, 3640, -10000, 0)
    CameraSetDistance(8039, 0)
    OP_6C(118000, 0)
    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    NewScene('ED6_DT21/E0610._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x2EE7
@scena.Code('func_14_2EE7')
def func_14_2EE7():
    @scena.Lambda('lambda_2EED')
    def lambda_2EED():
        OP_D1(0x00FE, 0, 260000, 30000, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2EED)

    @scena.Lambda('lambda_2F07')
    def lambda_2F07():
        ChrMoveTo(0x00FE, -50000, 0, -8000, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2F07)

    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_2F27')
    def lambda_2F27():
        OP_D1(0x00FE, 0, 250000, 40000, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F27)

    OP_97(0x00FE, -50000, -40000, -90000, 42000, 0x0000)
    ChrMoveTo(0x00FE, -100000, 0, -100000, 50000, 0x00)

    Return()

# id: 0x0015 offset: 0x2F65
@scena.Code('func_15_2F65')
def func_15_2F65():
    @scena.Lambda('lambda_2F6B')
    def lambda_2F6B():
        OP_D1(0x00FE, 0, 280000, -30000, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F6B)

    @scena.Lambda('lambda_2F85')
    def lambda_2F85():
        ChrMoveTo(0x00FE, -50000, -2000, 8000, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2F85)

    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_2FA5')
    def lambda_2FA5():
        OP_D1(0x00FE, 0, 290000, -40000, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FA5)

    OP_97(0x00FE, -50000, 40000, 90000, 42000, 0x0000)
    ChrMoveTo(0x00FE, -100000, -2000, 100000, 50000, 0x00)

    Return()

# id: 0x0016 offset: 0x2FE3
@scena.Code('func_16_2FE3')
def func_16_2FE3():
    @scena.Lambda('lambda_2FE9')
    def lambda_2FE9():
        OP_D1(0x00FE, 0, 260000, 30000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FE9)

    @scena.Lambda('lambda_3003')
    def lambda_3003():
        ChrMoveTo(0x00FE, -50000, 0, -9300, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3003)

    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_3023')
    def lambda_3023():
        OP_D1(0x00FE, 0, 250000, 40000, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3023)

    OP_97(0x00FE, -50000, -41300, -90000, 42000, 0x0000)
    ChrMoveTo(0x00FE, -100000, 0, -100000, 50000, 0x00)

    Return()

# id: 0x0017 offset: 0x3061
@scena.Code('func_17_3061')
def func_17_3061():
    @scena.Lambda('lambda_3067')
    def lambda_3067():
        OP_D1(0x00FE, 0, 280000, -30000, 10000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3067)

    @scena.Lambda('lambda_3081')
    def lambda_3081():
        ChrMoveTo(0x00FE, -50000, 0, 6700, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3081)

    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_30A1')
    def lambda_30A1():
        OP_D1(0x00FE, 0, 290000, -40000, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_30A1)

    OP_97(0x00FE, -50000, 38700, 90000, 42000, 0x0000)
    ChrMoveTo(0x00FE, -100000, 0, 100000, 50000, 0x00)

    Return()

# id: 0x0018 offset: 0x30DF
@scena.Code('func_18_30DF')
def func_18_30DF():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_12(0x00004E20, 0x000C3500, 0x00000000)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    CameraMove(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    CameraSetDistance(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_B0(0x0001, 0x0A)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 400)
    OP_70(0x0001, 460)
    PlaySE(121, 0x01, 0x46)
    OP_A1(0x000F, 0x0001)
    ChrSetPos(0x000F, 10000, 20000, 0, 270)

    @scena.Lambda('lambda_318C')
    def lambda_318C():
        CameraSetDistance(3130, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_318C)

    @scena.Lambda('lambda_319C')
    def lambda_319C():
        OP_6E(282, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_319C)

    FadeIn(2000, 0)

    @scena.Lambda('lambda_31B5')
    def lambda_31B5():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_31B5)

    Sleep(500)

    @scena.Lambda('lambda_31D5')
    def lambda_31D5():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_31D5)

    Sleep(500)

    @scena.Lambda('lambda_31F5')
    def lambda_31F5():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_31F5)

    Sleep(500)

    @scena.Lambda('lambda_3215')
    def lambda_3215():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3215)

    Sleep(500)

    @scena.Lambda('lambda_3235')
    def lambda_3235():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3235)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/R2201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x327C
@scena.Code('func_19_327C')
def func_19_327C():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_12(0x00004E20, 0x000C3500, 0x00000000)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_B0(0x0001, 0x0A)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 400)
    OP_70(0x0001, 460)
    PlaySE(121, 0x01, 0x64)
    OP_A1(0x000F, 0x0001)
    ChrSetPos(0x000F, -79470, -30000, -91440, 270)
    CameraMove(-98020, -10000, -92900, 0)
    OP_67(0, -6950, -10000, 0)
    CameraSetDistance(3100, 0)
    OP_6C(232000, 0)
    OP_6E(854, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_3346')
    def lambda_3346():
        CameraMove(-101640, -10000, -90970, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3346)

    @scena.Lambda('lambda_335E')
    def lambda_335E():
        OP_67(0, -8000, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_335E)

    @scena.Lambda('lambda_3376')
    def lambda_3376():
        CameraSetDistance(7000, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3376)

    CreateThread(0x000F, 0x00, 0x00, func_1A_33AA)
    Sleep(4000)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/R2201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x33AA
@scena.Code('func_1A_33AA')
def func_1A_33AA():
    @scena.Lambda('lambda_33B0')
    def lambda_33B0():
        ChrMoveTo(0x00FE, -203180, 100000, -91510, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_33B0)

    Sleep(500)

    @scena.Lambda('lambda_33D0')
    def lambda_33D0():
        ChrMoveTo(0x00FE, -200180, 100000, -91510, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_33D0)

    Sleep(500)

    @scena.Lambda('lambda_33F0')
    def lambda_33F0():
        ChrMoveTo(0x00FE, -203180, 100000, -91510, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_33F0)

    Sleep(500)

    @scena.Lambda('lambda_3410')
    def lambda_3410():
        ChrMoveTo(0x00FE, -203180, 100000, -91510, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3410)

    Sleep(500)

    @scena.Lambda('lambda_3430')
    def lambda_3430():
        ChrMoveTo(0x00FE, -203180, 100000, -91510, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3430)

    WaitForThreadExit(0x000F, 0x0001)

    Return()

# id: 0x001B offset: 0x344B
@scena.Code('func_1B_344B')
def func_1B_344B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_A1(0x000E, 0x0002)
    OP_A1(0x001B, 0x0007)
    ChrSetPos(0x000E, 0, 0, 0, 270)
    OP_72(0x0007, 0x0004)
    OP_72(0x0007, 0x0004)
    Yield()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-32090, 3430, -1640, 0)
    OP_67(0, 8860, -10000, 0)
    CameraSetDistance(2930, 0)
    OP_6C(311000, 0)
    OP_6E(515, 0)
    PlaySE(451, 0x00, 0x64)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetBattleFlags(0x001A, 0x0020)
    ChrSetBattleFlags(0x001B, 0x0020)
    OP_89(0x001A, 3260, 3600, -510, 0)
    OP_89(0x001B, 3310, 3600, 1000, 0)
    ChrSetChipByIndex(0x001A, 10)
    ChrSetSubChip(0x001A, 0)
    ChrSetFlags(0x001A, 0x0800)
    ChrClearFlags(0x001A, 0x0001)
    PlaySE(121, 0x01, 0x3C)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x0A)
    OP_6F(0x0002, 700)
    OP_70(0x0002, 780)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    LoadEffect(0x01, 'map\\\\mp085_00.eff')
    LoadEffect(0x02, 'battle\\\\mgaria0.eff')
    LoadEffect(0x03, 'map\\\\mp085_01.eff')

    @scena.Lambda('lambda_35A6')
    def lambda_35A6():
        CameraMove(3000, 3450, -220, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_35A6)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    CameraMove(2780, 3510, 470, 0)
    OP_67(0, 6020, -10000, 0)
    CameraSetDistance(3270, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_DC()
    Sleep(500)

    ChrTalk(
        0x001A,
        (
            '#0150340009V#1154F#6P──时机已经成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150340010V#1150F从现在起，『福音计划』\n',
            '正式进入第三阶段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x001A, 11)
    ChrSetSubChip(0x001A, 0)

    @scena.Lambda('lambda_368A')
    def lambda_368A():
        OP_99(0x001A, 0x00, 0x03, 1500)

        ExitThread()

    DispatchAsync(0x001A, 0x0000, lambda_368A)

    PlayEffect(0x02, 0x00, 0x001A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    PlaySE(213, 0x00, 0x64)

    @scena.Lambda('lambda_36D9')
    def lambda_36D9():
        OP_99(0x001A, 0x03, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x001A, 0x0000, lambda_36D9)

    Sleep(1000)

    StopEffect(0x00, 0x02)
    Sleep(1000)

    @scena.Lambda('lambda_36F6')
    def lambda_36F6():
        OP_99(0x001A, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x001A, 0x0000, lambda_36F6)

    Sleep(1000)

    Fade(500)
    CameraMove(2450, 3520, -870, 0)
    OP_67(0, 7140, -10000, 0)
    CameraSetDistance(1700, 0)
    OP_6C(191000, 0)
    OP_6E(499, 0)
    OP_0D()
    Sleep(500)

    ChrSetSubChip(0x001A, 0)
    ChrSetChipByIndex(0x001A, 6)

    @scena.Lambda('lambda_375D')
    def lambda_375D():
        OP_99(0x001A, 0x00, 0x09, 2000)

        ExitThread()

    DispatchAsync(0x001A, 0x0000, lambda_375D)

    Sleep(300)

    PlaySE(216, 0x00, 0x64)
    WaitForThreadExit(0x001A, 0x0000)
    Sleep(500)

    ChrTalk(
        0x001A,
        (
            '#0150340011V#1151F#5P被封印在七耀之力无法到达\n',
            '的黑暗夹缝中的『环』啊──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150340012V望汝通过『福音』，\n',
            '再度重现于世间吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    OP_E8(0xB8, 0x0B, 0x00, 0x00)
    Sleep(200)

    PlaySE(144, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x001B, 0, 500, 200, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_20(0x000007D0)
    Sleep(100)

    OP_24(0x01C3, 0x5A)
    Sleep(100)

    OP_24(0x01C3, 0x50)
    Sleep(100)

    OP_24(0x01C3, 0x46)
    Sleep(100)

    OP_24(0x01C3, 0x3C)
    Sleep(100)

    OP_24(0x01C3, 0x32)
    Sleep(100)

    OP_24(0x01C3, 0x28)
    Sleep(100)

    OP_24(0x01C3, 0x1E)
    Sleep(100)

    OP_23(0x01C3)
    OP_21()
    PlayBGM(112)
    Sleep(500)

    Fade(500)
    MapClearFlags(0x00000010)
    CameraMove(2420, 6690, 3310, 0)
    OP_67(0, 1830, -10000, 0)
    CameraSetDistance(2840, 0)
    OP_6C(338000, 0)
    OP_6E(806, 0)
    ChrClearFlags(0x001A, 0x0800)
    OP_0D()

    @scena.Lambda('lambda_38E8')
    def lambda_38E8():
        OP_67(0, 700, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38E8)

    @scena.Lambda('lambda_3900')
    def lambda_3900():
        CameraMove(2420, 8690, 3310, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3900)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0101, 0x0001)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x01, 0x01, 0x00FF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    PlaySE(311, 0x00, 0x64)
    Sleep(2000)

    Sleep(2000)

    Fade(500)
    CameraMove(2450, 3520, -870, 0)
    OP_67(0, 7140, -10000, 0)
    CameraSetDistance(1700, 0)
    OP_6C(191000, 0)
    OP_6E(499, 0)
    StopEffect(0x01, 0x00)
    ChrSetFlags(0x001A, 0x0800)
    OP_0D()
    OP_99(0x001A, 0x09, 0x00, 2000)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x001A,
        (
            '#0150340013V#1155F#5P看吧！\n',
            '耸立在四方的『桩』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150340014V它们便是将你封锁在\n',
            '黑暗深处的最后束缚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150340015V如今它已在人类的伪装下\n',
            '以虚假的形态留存于世，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150340016V就用你那支配万物的神圣之手，\n',
            '将一切真相揭露出来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    PlayEffect(0x01, 0x01, 0x00FF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    Fade(1500)
    CameraMove(2420, 8690, 3310, 0)
    OP_67(0, 700, -10000, 0)
    CameraSetDistance(2840, 0)
    OP_6C(338000, 0)
    OP_6E(806, 0)
    ChrClearFlags(0x001A, 0x0800)
    OP_0D()
    PlayEffect(0x03, 0x02, 0x00FF, -2500, 13000, 15000, 0, 0, 0, 6000, 6000, 6000, 0x00FF, 0, 0, 0, 0)
    PlaySE(311, 0x00, 0x64)
    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001C offset: 0x3B9D
@scena.Code('func_1C_3B9D')
def func_1C_3B9D():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_0D()
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS240._CH')
    OP_C5(0x01, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS241._CH')
    OP_C5(0x02, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS240._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_C6(0x02, 0x03, -1, 0, 0)
    Sleep(2000)

    OP_C6(0x01, 0x00, -36000, -110000, 0)
    OP_C6(0x01, 0x01, 1300, 1300, 0)
    OP_C6(0x02, 0x00, -36000, -110000, 0)
    OP_C6(0x02, 0x01, 1300, 1300, 0)
    OP_C6(0x00, 0x00, -36000, -110000, 1000)
    OP_C6(0x00, 0x01, 1300, 1300, 1000)
    OP_C6(0x00, 0x03, 16777215, 1000, 0)
    OP_C7(0x00, 0x00, 0x00)
    OP_C7(0x00, 0x00, 0x01)
    Sleep(1500)

    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x00, -160000, 0, 1000)
    OP_C6(0x02, 0x00, -160000, 0, 1000)
    Sleep(400)

    OP_C6(0x01, 0x03, -1, 1000, 0)
    OP_C7(0x00, 0x01, 0x00)
    OP_C7(0x00, 0x01, 0x03)
    Sleep(2000)

    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 1000, 0)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    Call(0, 0x0024)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x001D offset: 0x3DB9
@scena.Code('func_1D_3DB9')
def func_1D_3DB9():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS242._CH')
    OP_C5(0x01, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS243._CH')
    OP_C5(0x02, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS242._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_C6(0x02, 0x03, -1, 0, 0)
    Sleep(2000)

    OP_C6(0x01, 0x00, -125000, 0, 0)
    OP_C6(0x01, 0x01, 1300, 1300, 0)
    OP_C6(0x02, 0x00, -125000, 0, 0)
    OP_C6(0x02, 0x01, 1300, 1300, 0)
    OP_C6(0x00, 0x00, -125000, 0, 1000)
    OP_C6(0x00, 0x01, 1300, 1300, 1000)
    OP_C6(0x00, 0x03, 16777215, 1000, 0)
    OP_C7(0x00, 0x00, 0x00)
    OP_C7(0x00, 0x00, 0x01)
    Sleep(1500)

    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x00, -90000, -110000, 1000)
    OP_C6(0x02, 0x00, -90000, -110000, 1000)
    Sleep(400)

    OP_C6(0x01, 0x03, -1, 1000, 0)
    OP_C7(0x00, 0x01, 0x00)
    OP_C7(0x00, 0x01, 0x03)
    Sleep(2000)

    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 1000, 0)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    Call(0, 0x0025)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021F, 3, 0x10FB))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x001E offset: 0x3FCF
@scena.Code('func_1E_3FCF')
def func_1E_3FCF():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    FadeOut(0, 0, -1)
    Call(0, 0x0026)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0x400D
@scena.Code('func_1F_400D')
def func_1F_400D():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x00, 'map\\\\mp078_00.eff')
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-37160, -10000, -21180, 0)
    OP_67(0, -10620, -10000, 0)
    CameraSetDistance(5110, 0)
    OP_6C(31000, 0)
    OP_6E(619, 0)
    OP_A1(0x000E, 0x0001)
    ChrSetPos(0x000E, 38760, -10000, -14790, 270)
    OP_A1(0x000F, 0x0002)
    ChrSetPos(0x000F, 50390, -10000, 4970, 90)
    OP_A1(0x0010, 0x0003)
    ChrSetPos(0x0010, 70850, -10000, -32060, 90)
    ChrClearFlags(0x000E, 0x0100)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x000F, 0, 90000, 10000, 0)
    OP_D1(0x0010, 0, 90000, -10000, 0)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 700)
    OP_70(0x0001, 780)

    @scena.Lambda('lambda_4127')
    def lambda_4127():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4127)

    Sleep(2000)

    OP_B0(0x0002, 0x2D)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 470)
    OP_70(0x0002, 570)
    Sleep(100)

    OP_B0(0x0003, 0x2D)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 470)
    OP_70(0x0003, 570)

    @scena.Lambda('lambda_417A')
    def lambda_417A():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_417A)

    Sleep(200)

    @scena.Lambda('lambda_419A')
    def lambda_419A():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_419A)

    Sleep(3000)

    Fade(500)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x01)
    ChrSetPos(0x000E, -8760, 0, -14790, 270)
    ChrSetPos(0x000F, 40390, 0, 4970, 90)
    ChrSetPos(0x0010, 55850, 0, -26060, 90)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x000F, 0, 80000, 10000, 0)
    OP_D1(0x0010, 0, 95000, -10000, 0)
    OP_6F(0x0002, 941)
    OP_70(0x0002, 1000)
    OP_6F(0x0003, 941)
    OP_70(0x0003, 1000)
    CameraMove(-1430, 11270, -30440, 0)
    OP_67(0, 5280, -10000, 0)
    CameraSetDistance(6040, 0)
    OP_6C(46000, 0)
    OP_6E(619, 0)
    ChrSetPos(0x0000, -8340, 11270, -29600, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -10, -5, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -25, -10, 0, 0x00, 0x00)
    OP_0D()

    @scena.Lambda('lambda_42E7')
    def lambda_42E7():
        CameraMove(-9890, 11270, -27200, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_42E7)

    @scena.Lambda('lambda_42FF')
    def lambda_42FF():
        OP_6C(63000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_42FF)

    @scena.Lambda('lambda_430F')
    def lambda_430F():
        CameraSetDistance(7790, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_430F)

    Sleep(2000)

    PlayEffect(0x00, 0x00, 0x0010, 300, 3300, -8000, 95, 0, 350, 900, 900, 900, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0000, 0x00, 0x00, func_20_49D4)

    @scena.Lambda('lambda_4360')
    def lambda_4360():
        OP_D1(0x00FE, 0, 280000, -35000, 300)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_4360)

    CreateThread(0x000E, 0x00, 0x00, func_21_4A08)
    WaitForThreadExit(0x000E, 0x0003)

    @scena.Lambda('lambda_4386')
    def lambda_4386():
        OP_D1(0x00FE, 0, 270000, 0, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_4386)

    @scena.Lambda('lambda_43A0')
    def lambda_43A0():
        OP_D1(0x00FE, 0, 90000, 10000, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_43A0)

    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    Sleep(500)

    StopEffect(0x00, 0x00)
    OP_24(0x0235, 0x00)
    OP_23(0x0235)
    CreateThread(0x0000, 0x00, 0x00, func_20_49D4)
    PlayEffect(0x00, 0x00, 0x000F, 1000, 3300, -8300, 90, 0, 10, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_440F')
    def lambda_440F():
        OP_D1(0x00FE, 0, 260000, 35000, 300)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_440F)

    CreateThread(0x000E, 0x00, 0x00, func_22_4AE4)
    WaitForThreadExit(0x000E, 0x0003)

    @scena.Lambda('lambda_4435')
    def lambda_4435():
        OP_D1(0x00FE, 0, 270000, 0, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_4435)

    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    Sleep(500)

    StopEffect(0x00, 0x00)
    TerminateThread(0x0000, 0x00)
    OP_24(0x0235, 0x00)
    OP_23(0x0235)

    @scena.Lambda('lambda_446C')
    def lambda_446C():
        OP_D1(0x00FE, 0, 270000, 30000, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_446C)

    @scena.Lambda('lambda_4486')
    def lambda_4486():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -100000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4486)

    Sleep(200)

    @scena.Lambda('lambda_44A6')
    def lambda_44A6():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -100000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_44A6)

    Sleep(200)

    @scena.Lambda('lambda_44C6')
    def lambda_44C6():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -100000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_44C6)

    Sleep(200)

    @scena.Lambda('lambda_44E6')
    def lambda_44E6():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -100000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_44E6)

    Sleep(200)

    @scena.Lambda('lambda_4506')
    def lambda_4506():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -100000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4506)

    Sleep(200)

    @scena.Lambda('lambda_4526')
    def lambda_4526():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -100000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4526)

    Sleep(200)

    @scena.Lambda('lambda_4546')
    def lambda_4546():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -100000, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4546)

    Sleep(200)

    @scena.Lambda('lambda_4566')
    def lambda_4566():
        ChrMoveToRelativeAsync(0x00FE, -100000, 0, -100000, 34000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4566)

    Sleep(800)

    @scena.Lambda('lambda_4586')
    def lambda_4586():
        OP_D1(0x00FE, 0, 90000, -30000, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_4586)

    @scena.Lambda('lambda_45A0')
    def lambda_45A0():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_45A0)

    Sleep(200)

    @scena.Lambda('lambda_45C0')
    def lambda_45C0():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_45C0)

    Sleep(200)

    @scena.Lambda('lambda_45E0')
    def lambda_45E0():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_45E0)

    Sleep(200)

    @scena.Lambda('lambda_4600')
    def lambda_4600():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4600)

    Sleep(200)

    @scena.Lambda('lambda_4620')
    def lambda_4620():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4620)

    Sleep(200)

    @scena.Lambda('lambda_4640')
    def lambda_4640():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4640)

    @scena.Lambda('lambda_465B')
    def lambda_465B():
        OP_D1(0x00FE, 0, 90000, -30000, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_465B)

    @scena.Lambda('lambda_4675')
    def lambda_4675():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4675)

    Sleep(200)

    @scena.Lambda('lambda_4695')
    def lambda_4695():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_4695)

    @scena.Lambda('lambda_46B0')
    def lambda_46B0():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_46B0)

    Sleep(200)

    @scena.Lambda('lambda_46D0')
    def lambda_46D0():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 34000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_46D0)

    @scena.Lambda('lambda_46EB')
    def lambda_46EB():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_46EB)

    Sleep(200)

    @scena.Lambda('lambda_470B')
    def lambda_470B():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_470B)

    Sleep(200)

    @scena.Lambda('lambda_472B')
    def lambda_472B():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_472B)

    Sleep(200)

    @scena.Lambda('lambda_474B')
    def lambda_474B():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_474B)

    Sleep(200)

    @scena.Lambda('lambda_476B')
    def lambda_476B():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_476B)

    Sleep(200)

    @scena.Lambda('lambda_478B')
    def lambda_478B():
        ChrMoveToRelativeAsync(0x00FE, -200000, 0, -100000, 34000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_478B)

    Sleep(2500)

    Fade(500)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x000E, 0x03)
    TerminateThread(0x000F, 0x03)
    TerminateThread(0x0010, 0x03)
    CameraMove(54490, 3940, -20960, 0)
    OP_67(0, 2960, -10000, 0)
    CameraSetDistance(5110, 0)
    OP_6C(294000, 0)
    OP_6E(619, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -20, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -10, -5, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -25, -10, 0, 0x00, 0x00)
    ChrSetPos(0x000E, -38760, 0, -14790, 270)
    ChrSetPos(0x000F, 40390, 0, 4970, 90)
    ChrSetPos(0x0010, 60850, 0, -32060, 90)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x000F, 0, 84000, -10000, 0)
    OP_D1(0x0010, 0, 96000, 10000, 0)
    OP_6F(0x0002, 470)
    OP_70(0x0002, 570)
    OP_6F(0x0003, 470)
    OP_70(0x0003, 570)
    OP_0D()
    OP_DC()
    SetMessageWindowPos(100, 300, -1, -1)
    TalkSetChrName('摩尔根将军')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0600341407V#163F哼……真是阴魂不散。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600341408V别以为速度快一些\n',
            '就能够逃出这个包围网。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600341409V#160F继续追赶，将它拿下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    SetMessageWindowPos(300, 100, -1, -1)
    TalkSetChrName('士兵们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#2440341410V#5S是，长官！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x03C3, 5, 0x1E1D))
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/R4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x49D4
@scena.Code('func_20_49D4')
def func_20_49D4():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A07',
    )

    PlaySE(565, 0x00, 0x64)
    Sleep(1500)

    OP_23(0x0235)
    PlaySE(565, 0x00, 0x64)
    Sleep(1500)

    OP_23(0x0235)
    PlaySE(565, 0x00, 0x64)
    Sleep(1500)

    OP_23(0x0235)

    Jump('func_20_49D4')

    def _loc_4A07(): pass

    label('loc_4A07')

    Return()

# id: 0x0021 offset: 0x4A08
@scena.Code('func_21_4A08')
def func_21_4A08():
    @scena.Lambda('lambda_4A0E')
    def lambda_4A0E():
        ChrMoveTo(0x00FE, -8760, 0, -790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4A0E)

    Sleep(100)

    @scena.Lambda('lambda_4A2E')
    def lambda_4A2E():
        ChrMoveTo(0x00FE, -8760, 0, -790, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4A2E)

    Sleep(100)

    @scena.Lambda('lambda_4A4E')
    def lambda_4A4E():
        ChrMoveTo(0x00FE, -8760, 0, -790, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4A4E)

    Sleep(200)

    @scena.Lambda('lambda_4A6E')
    def lambda_4A6E():
        ChrMoveTo(0x00FE, -8760, 0, -790, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4A6E)

    Sleep(200)

    @scena.Lambda('lambda_4A8E')
    def lambda_4A8E():
        ChrMoveTo(0x00FE, -8760, 0, -790, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4A8E)

    Sleep(200)

    @scena.Lambda('lambda_4AAE')
    def lambda_4AAE():
        ChrMoveTo(0x00FE, -8760, 0, -790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4AAE)

    Sleep(200)

    @scena.Lambda('lambda_4ACE')
    def lambda_4ACE():
        ChrMoveTo(0x00FE, -8760, 0, -790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4ACE)

    Return()

# id: 0x0022 offset: 0x4AE4
@scena.Code('func_22_4AE4')
def func_22_4AE4():
    @scena.Lambda('lambda_4AEA')
    def lambda_4AEA():
        ChrMoveTo(0x00FE, -8760, 0, -14790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4AEA)

    Sleep(100)

    @scena.Lambda('lambda_4B0A')
    def lambda_4B0A():
        ChrMoveTo(0x00FE, -8760, 0, -14790, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4B0A)

    Sleep(100)

    @scena.Lambda('lambda_4B2A')
    def lambda_4B2A():
        ChrMoveTo(0x00FE, -8760, 0, -14790, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4B2A)

    Sleep(200)

    @scena.Lambda('lambda_4B4A')
    def lambda_4B4A():
        ChrMoveTo(0x00FE, -8760, 0, -14790, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4B4A)

    Sleep(200)

    @scena.Lambda('lambda_4B6A')
    def lambda_4B6A():
        ChrMoveTo(0x00FE, -8760, 0, -14790, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4B6A)

    Sleep(200)

    @scena.Lambda('lambda_4B8A')
    def lambda_4B8A():
        ChrMoveTo(0x00FE, -8760, 0, -14790, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4B8A)

    Sleep(200)

    @scena.Lambda('lambda_4BAA')
    def lambda_4BAA():
        ChrMoveTo(0x00FE, -8760, 0, -14790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4BAA)

    Return()

# id: 0x0023 offset: 0x4BC0
@scena.Code('func_23_4BC0')
def func_23_4BC0():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    FadeOut(0, 0, -1)
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS246._CH')
    OP_C5(0x01, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS247._CH')
    OP_C5(0x02, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS246._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_C6(0x02, 0x03, -1, 0, 0)
    Sleep(2000)

    OP_C6(0x01, 0x00, 0, -144000, 0)
    OP_C6(0x01, 0x01, 1300, 1300, 0)
    OP_C6(0x02, 0x00, 0, -144000, 0)
    OP_C6(0x02, 0x01, 1300, 1300, 0)
    OP_C6(0x00, 0x00, 0, -144000, 1000)
    OP_C6(0x00, 0x01, 1300, 1300, 1000)
    OP_C6(0x00, 0x03, 16777215, 1000, 0)
    OP_C7(0x00, 0x00, 0x00)
    OP_C7(0x00, 0x00, 0x01)
    Sleep(1500)

    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x00, -94000, -16000, 1000)
    OP_C6(0x02, 0x00, -94000, -16000, 1000)
    Sleep(400)

    OP_C6(0x01, 0x03, -1, 1000, 0)
    OP_C7(0x00, 0x01, 0x00)
    OP_C7(0x00, 0x01, 0x03)
    Sleep(2000)

    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 1000, 0)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    Call(0, 0x0027)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x03C3, 6, 0x1E1E))
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0024 offset: 0x4DD9
@scena.Code('func_24_4DD9')
def func_24_4DD9():
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    CameraMove(-24410, 4960, -25560, 0)
    OP_67(0, -5640, -10000, 0)
    CameraSetDistance(5030, 0)
    OP_6C(44000, 0)
    OP_6E(561, 0)
    PlaySE(451, 0x00, 0x64)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    LoadEffect(0x00, 'map\\\\mp077_00.eff')
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, 30000, 20000, 0, 270)
    PlaySE(293, 0x01, 0x46)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 100)
    OP_70(0x0005, 150)

    @scena.Lambda('lambda_4E9E')
    def lambda_4E9E():
        ChrMoveToRelative(0x00FE, -20000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_4E9E)

    FadeIn(1000, 0)
    WaitForThreadExit(0x000E, 0x0002)
    OP_72(0x0005, 0x0020)
    OP_73(0x0005)

    @scena.Lambda('lambda_4ECF')
    def lambda_4ECF():
        ChrMoveToRelative(0x00FE, -50000, -60000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_4ECF)

    @scena.Lambda('lambda_4EEA')
    def lambda_4EEA():
        CameraMove(-42500, 30000, -12940, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4EEA)

    @scena.Lambda('lambda_4F02')
    def lambda_4F02():
        OP_67(0, 15420, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4F02)

    @scena.Lambda('lambda_4F1A')
    def lambda_4F1A():
        CameraSetDistance(5030, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4F1A)

    @scena.Lambda('lambda_4F2A')
    def lambda_4F2A():
        OP_6E(464, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4F2A)

    @scena.Lambda('lambda_4F3A')
    def lambda_4F3A():
        OP_6C(57000, 7000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_4F3A)

    OP_6F(0x0005, 150)
    OP_70(0x0005, 330)
    Sleep(3450)

    PlaySE(221, 0x00, 0x64)
    Sleep(400)

    PlaySE(221, 0x00, 0x64)
    Sleep(400)

    PlaySE(221, 0x00, 0x64)
    OP_73(0x0005)
    PlayEffect(0x00, 0xFF, 0x00FF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    WaitForThreadExit(0x0101, 0x0000)

    Return()

# id: 0x0025 offset: 0x4FC1
@scena.Code('func_25_4FC1')
def func_25_4FC1():
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    CameraMove(-4680, 30000, 7570, 0)
    OP_67(0, 9030, -10000, 0)
    CameraSetDistance(5750, 0)
    OP_6C(140000, 0)
    OP_6E(500, 0)
    PlaySE(451, 0x00, 0x64)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    LoadEffect(0x00, 'map\\\\mp077_00.eff')
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, 30000, 20000, 0, 270)
    PlaySE(293, 0x01, 0x46)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 100)
    OP_70(0x0005, 150)

    @scena.Lambda('lambda_5086')
    def lambda_5086():
        ChrMoveToRelative(0x00FE, -20000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_5086)

    FadeIn(1000, 0)
    WaitForThreadExit(0x000E, 0x0002)
    OP_72(0x0005, 0x0020)
    OP_73(0x0005)

    @scena.Lambda('lambda_50B7')
    def lambda_50B7():
        ChrMoveToRelative(0x00FE, -50000, -60000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_50B7)

    @scena.Lambda('lambda_50D2')
    def lambda_50D2():
        CameraMove(-21610, -2850, 5220, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_50D2)

    @scena.Lambda('lambda_50EA')
    def lambda_50EA():
        OP_67(0, 14310, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_50EA)

    @scena.Lambda('lambda_5102')
    def lambda_5102():
        CameraSetDistance(4500, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5102)

    @scena.Lambda('lambda_5112')
    def lambda_5112():
        OP_6C(224000, 7000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_5112)

    OP_6F(0x0005, 150)
    OP_70(0x0005, 330)
    Sleep(3450)

    PlaySE(221, 0x00, 0x64)
    Sleep(400)

    PlaySE(221, 0x00, 0x64)
    Sleep(400)

    PlaySE(221, 0x00, 0x64)
    OP_73(0x0005)
    PlayEffect(0x00, 0xFF, 0x00FF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    WaitForThreadExit(0x0101, 0x0001)

    Return()

# id: 0x0026 offset: 0x5199
@scena.Code('func_26_5199')
def func_26_5199():
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    LoadEffect(0x00, 'map\\\\mp077_00.eff')
    CameraMove(-15370, 30000, 3100, 0)
    OP_67(0, 9030, -10000, 0)
    CameraSetDistance(5750, 0)
    OP_6C(236000, 0)
    OP_6E(500, 0)
    PlaySE(451, 0x00, 0x64)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, 30000, 20000, 0, 270)
    PlaySE(293, 0x01, 0x46)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 100)
    OP_70(0x0005, 150)

    @scena.Lambda('lambda_5272')
    def lambda_5272():
        CameraMove(13380, 30000, 4450, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5272)

    @scena.Lambda('lambda_528A')
    def lambda_528A():
        ChrMoveToRelative(0x00FE, -20000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_528A)

    FadeIn(1000, 0)
    WaitForThreadExit(0x000E, 0x0002)
    WaitForThreadExit(0x0101, 0x0000)
    OP_72(0x0005, 0x0020)
    OP_73(0x0005)

    @scena.Lambda('lambda_52C0')
    def lambda_52C0():
        ChrMoveToRelative(0x00FE, -50000, -60000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_52C0)

    @scena.Lambda('lambda_52DB')
    def lambda_52DB():
        CameraMove(-15600, -10000, 380, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_52DB)

    @scena.Lambda('lambda_52F3')
    def lambda_52F3():
        OP_67(0, 6870, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_52F3)

    @scena.Lambda('lambda_530B')
    def lambda_530B():
        CameraSetDistance(6430, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_530B)

    @scena.Lambda('lambda_531B')
    def lambda_531B():
        OP_6E(613, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_531B)

    @scena.Lambda('lambda_532B')
    def lambda_532B():
        OP_6C(270000, 7000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_532B)

    OP_6F(0x0005, 150)
    OP_70(0x0005, 330)
    Sleep(3450)

    PlaySE(221, 0x00, 0x64)
    Sleep(400)

    PlaySE(221, 0x00, 0x64)
    Sleep(400)

    PlaySE(221, 0x00, 0x64)
    OP_73(0x0005)
    PlayEffect(0x00, 0xFF, 0x00FF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    WaitForThreadExit(0x0101, 0x0001)

    Return()

# id: 0x0027 offset: 0x53B2
@scena.Code('func_27_53B2')
def func_27_53B2():
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    LoadEffect(0x00, 'map\\\\mp077_00.eff')
    CameraMove(5220, 28870, 190, 0)
    OP_67(0, -8260, -10000, 0)
    CameraSetDistance(5500, 0)
    OP_6C(103000, 0)
    OP_6E(646, 0)
    PlaySE(451, 0x00, 0x64)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, 30000, 20000, 0, 270)
    PlaySE(293, 0x01, 0x46)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 100)
    OP_70(0x0005, 150)

    @scena.Lambda('lambda_5477')
    def lambda_5477():
        CameraSetDistance(7000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5477)

    @scena.Lambda('lambda_5487')
    def lambda_5487():
        ChrMoveToRelative(0x00FE, -20000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_5487)

    FadeIn(1000, 0)
    WaitForThreadExit(0x000E, 0x0002)
    WaitForThreadExit(0x0101, 0x0000)
    OP_72(0x0005, 0x0020)
    OP_73(0x0005)

    @scena.Lambda('lambda_54BD')
    def lambda_54BD():
        ChrMoveToRelative(0x00FE, -50000, -60000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_54BD)

    @scena.Lambda('lambda_54D8')
    def lambda_54D8():
        CameraMove(-28550, -10000, -240, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_54D8)

    @scena.Lambda('lambda_54F0')
    def lambda_54F0():
        OP_67(0, 15830, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_54F0)

    @scena.Lambda('lambda_5508')
    def lambda_5508():
        CameraSetDistance(5900, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5508)

    OP_6F(0x0005, 150)
    OP_70(0x0005, 330)
    Sleep(3450)

    PlaySE(221, 0x00, 0x64)
    Sleep(400)

    PlaySE(221, 0x00, 0x64)
    Sleep(400)

    PlaySE(221, 0x00, 0x64)
    OP_73(0x0005)
    PlayEffect(0x00, 0xFF, 0x00FF, -40000, -10000, 0, 270, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)
    WaitForThreadExit(0x0101, 0x0001)

    Return()

# id: 0x0028 offset: 0x558F
@scena.Code('func_28_558F')
def func_28_558F():
    EventBegin(0x00)
    OP_DB()
    MapClearFlags(0x00100000)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    CameraMove(-150870, 26810, -13480, 0)
    OP_67(0, -3250, -10000, 0)
    CameraSetDistance(1830, 0)
    OP_6C(262000, 0)
    OP_6E(742, 0)
    OP_A1(0x001D, 0x0001)
    ChrSetPos(0x001D, -100380, -10000, -13480, 270)
    PlaySE(275, 0x00, 0x64)
    ChrSetPos(0x001C, 0, 0, 0, 135)
    ChrClearFlags(0x001C, 0x0080)
    OP_CF(0x001C, 0x01, 'Frame85__ren')

    ExecExpressionWithValue(
        0x001C,
        0x24,
        (
            (Expr.PushLong, 0xA5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0001, 0x0020)
    OP_B0(0x0001, 0x0F)
    OP_6F(0x0001, 281)
    OP_70(0x0001, 300)
    LoadEffect(0x02, 'map\\\\mp064_01.eff')
    LoadEffect(0x03, 'map\\\\mp065_01.eff')
    PlayEffect(0x02, 0x01, 0x001D, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x02, 0x001D, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x03, 0x001D, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x001D, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x05, 0x001D, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x06, 0x001D, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_57C2')
    def lambda_57C2():
        OP_67(0, -5540, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_57C2)

    @scena.Lambda('lambda_57DA')
    def lambda_57DA():
        CameraSetDistance(2400, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_57DA)

    @scena.Lambda('lambda_57EA')
    def lambda_57EA():
        OP_6C(270000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_57EA)

    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_5804')
    def lambda_5804():
        ChrMoveToRelative(0x00FE, -400000, 250000, 0, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_5804)

    CreateThread(0x001D, 0x03, 0x00, func_29_584E)
    Sleep(3000)

    FadeOut(1500, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    Sleep(1000)

    OP_DC()
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0029 offset: 0x584E
@scena.Code('func_29_584E')
def func_29_584E():
    Sleep(500)

    OP_24(0x0113, 0x5F)
    Sleep(500)

    OP_24(0x0113, 0x5A)
    Sleep(500)

    OP_24(0x0113, 0x55)
    Sleep(500)

    OP_24(0x0113, 0x50)
    Sleep(500)

    OP_24(0x0113, 0x4B)
    Sleep(500)

    OP_24(0x0113, 0x46)
    Sleep(500)

    OP_24(0x0113, 0x41)
    Sleep(500)

    OP_24(0x0113, 0x3C)
    Sleep(500)

    OP_24(0x0113, 0x37)
    Sleep(500)

    OP_24(0x0113, 0x32)
    Sleep(500)

    OP_24(0x0113, 0x2D)
    Sleep(500)

    OP_24(0x0113, 0x28)
    Sleep(500)

    OP_24(0x0113, 0x23)
    Sleep(500)

    OP_24(0x0113, 0x1E)
    Sleep(500)

    OP_24(0x0113, 0x19)
    Sleep(500)

    OP_24(0x0113, 0x14)

    Return()

# id: 0x002A offset: 0x58DF
@scena.Code('func_2A_58DF')
def func_2A_58DF():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_71(0x0000, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_A1(0x000F, 0x0001)
    ChrSetDirection(0x000F, 270, 0)
    OP_71(0x0001, 0x0020)
    OP_B0(0x0001, 0x14)
    OP_6F(0x0001, 360)
    OP_70(0x0001, 460)
    PlaySE(121, 0x01, 0x64)
    CameraMove(92340, 13360, 25280, 0)
    OP_67(0, 5320, -10000, 0)
    CameraSetDistance(4550, 0)
    OP_6C(247000, 0)
    OP_6E(437, 0)
    PlaySE(451, 0x00, 0x64)

    @scena.Lambda('lambda_597A')
    def lambda_597A():
        CameraMove(22320, 13360, 9400, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_597A)

    @scena.Lambda('lambda_5992')
    def lambda_5992():
        OP_67(0, 3320, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5992)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0000, 0x0000)
    Sleep(1000)

    @scena.Lambda('lambda_59BD')
    def lambda_59BD():
        CameraMove(-45160, 13360, -800, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_59BD)

    @scena.Lambda('lambda_59D5')
    def lambda_59D5():
        OP_6C(270000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_59D5)

    @scena.Lambda('lambda_59E5')
    def lambda_59E5():
        OP_6E(352, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_59E5)

    Sleep(4000)

    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/E0110._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x002B offset: 0x5A12
@scena.Code('func_2B_5A12')
def func_2B_5A12():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-35180, -10000, -17880, 0)
    OP_67(0, -5970, -10000, 0)
    CameraSetDistance(4660, 0)
    OP_6C(28000, 0)
    OP_6E(497, 0)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_A1(0x000E, 0x0002)
    OP_A1(0x000F, 0x0003)
    OP_A1(0x0010, 0x0004)
    ChrSetPos(0x000E, 38760, -5000, -10000, 270)
    ChrSetPos(0x000F, 48390, -5000, -3000, 270)
    ChrSetPos(0x0010, 58850, -5000, -17000, 270)
    ChrClearFlags(0x000E, 0x0100)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_B0(0x0002, 0x2D)
    OP_B0(0x0003, 0x2D)
    OP_B0(0x0004, 0x2D)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 700)
    OP_70(0x0002, 780)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 700)
    OP_70(0x0003, 780)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 700)
    OP_70(0x0004, 780)
    FadeIn(500, 0)
    OP_0D()

    @scena.Lambda('lambda_5B54')
    def lambda_5B54():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5B54)

    Sleep(1000)

    @scena.Lambda('lambda_5B74')
    def lambda_5B74():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5B74)

    Sleep(1000)

    @scena.Lambda('lambda_5B94')
    def lambda_5B94():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5B94)

    Sleep(2000)

    FadeOut(500, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002C offset: 0x5BCC
@scena.Code('func_2C_5BCC')
def func_2C_5BCC():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-35180, -10000, -17880, 0)
    OP_67(0, -5970, -10000, 0)
    CameraSetDistance(4660, 0)
    OP_6C(28000, 0)
    OP_6E(497, 0)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_A1(0x000E, 0x0002)
    OP_A1(0x000F, 0x0003)
    OP_A1(0x0010, 0x0004)
    ChrSetPos(0x000E, 38760, -5000, -10000, 270)
    ChrSetPos(0x000F, 48390, -5000, -3000, 270)
    ChrSetPos(0x0010, 58850, -5000, -17000, 270)
    ChrClearFlags(0x000E, 0x0100)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_B0(0x0002, 0x2D)
    OP_B0(0x0003, 0x2D)
    OP_B0(0x0004, 0x2D)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 700)
    OP_70(0x0002, 780)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 700)
    OP_70(0x0003, 780)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 700)
    OP_70(0x0004, 780)
    FadeIn(500, 0)
    OP_0D()

    @scena.Lambda('lambda_5D0E')
    def lambda_5D0E():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5D0E)

    Sleep(1000)

    @scena.Lambda('lambda_5D2E')
    def lambda_5D2E():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5D2E)

    Sleep(1000)

    @scena.Lambda('lambda_5D4E')
    def lambda_5D4E():
        ChrMoveToRelativeAsync(0x00FE, -400000, 10000, 0, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5D4E)

    Sleep(2000)

    FadeOut(500, 0, -1)
    OP_0D()
    OP_DC()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R4102._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002D offset: 0x5D86
@scena.Code('func_2D_5D86')
def func_2D_5D86():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x0000, -9020, 0, -61470, 0)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    CameraMove(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    CameraSetDistance(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 700000, 0)
    OP_A1(0x000E, 0x0005)
    ChrSetPos(0x000E, 10000, 20000, 0, 270)
    PlaySE(293, 0x01, 0x50)
    OP_B0(0x0005, 0x1E)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 330)
    OP_70(0x0005, 430)

    @scena.Lambda('lambda_5E4C')
    def lambda_5E4C():
        CameraSetDistance(3130, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5E4C)

    @scena.Lambda('lambda_5E5C')
    def lambda_5E5C():
        OP_6E(282, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5E5C)

    FadeIn(2000, 0)

    @scena.Lambda('lambda_5E75')
    def lambda_5E75():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5E75)

    Sleep(500)

    @scena.Lambda('lambda_5E95')
    def lambda_5E95():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5E95)

    Sleep(500)

    @scena.Lambda('lambda_5EB5')
    def lambda_5EB5():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5EB5)

    Sleep(500)

    @scena.Lambda('lambda_5ED5')
    def lambda_5ED5():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5ED5)

    Sleep(500)

    @scena.Lambda('lambda_5EF5')
    def lambda_5EF5():
        ChrMoveToRelative(0x00FE, 0, -130000, 20000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5EF5)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    MapSetFlags(0x00100000)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1402._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002E offset: 0x5F41
@scena.Code('func_2E_5F41')
def func_2E_5F41():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x00, 'monster\\\\msc0331.eff')
    LoadEffect(0x01, 'battle\\\\btbomb00.eff')
    LoadEffect(0x02, 'map\\\\mp077_00.eff')
    LoadEffect(0x03, 'map\\\\mpsmk0.eff')
    LoadEffect(0x04, 'map\\\\mp094_00.eff')
    LoadEffect(0x05, 'map\\\\mp078_01.eff')
    OP_E8(0x88, 0x13, 0x00, 0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_A1(0x000E, 0x0001)
    ChrSetPos(0x000E, 0, 0, 0, 270)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    OP_6F(0x0001, 200)
    OP_70(0x0001, 600)
    OP_A1(0x000F, 0x0002)
    OP_A1(0x0010, 0x0003)
    OP_A1(0x0011, 0x0004)
    OP_A1(0x0012, 0x0005)
    OP_A1(0x0013, 0x0006)
    ChrSetPos(0x000F, 56000, 0, -30000, 270)
    ChrSetPos(0x0010, 78000, 6000, -16000, 270)
    ChrSetPos(0x0011, 50000, 3000, 0, 270)
    ChrSetPos(0x0012, 78000, 6000, 16000, 270)
    ChrSetPos(0x0013, 56000, 0, 30000, 270)
    ChrClearFlags(0x000F, 0x0100)
    ChrClearFlags(0x0010, 0x0100)
    ChrClearFlags(0x0011, 0x0100)
    ChrClearFlags(0x0012, 0x0100)
    ChrClearFlags(0x0013, 0x0100)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)
    OP_D1(0x0012, 0, 270000, 0, 0)
    OP_D1(0x0013, 0, 270000, 0, 0)
    OP_B0(0x0002, 0x2D)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 680)
    OP_70(0x0002, 780)
    OP_B0(0x0003, 0x2D)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 680)
    OP_70(0x0003, 780)
    OP_B0(0x0004, 0x2D)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 680)
    OP_70(0x0004, 780)
    OP_B0(0x0005, 0x2D)
    OP_71(0x0005, 0x0020)
    OP_6F(0x0005, 680)
    OP_70(0x0005, 780)
    OP_B0(0x0006, 0x2D)
    OP_71(0x0006, 0x0020)
    OP_6F(0x0006, 680)
    OP_70(0x0006, 780)
    OP_76(0x00FF, 0x00000000, 0x0001, -5, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -10, -2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -25, -5, 0, 0x00, 0x00)
    OP_71(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    CameraMove(8660, -10000, -10260, 0)
    OP_67(0, 13390, -10000, 0)
    CameraSetDistance(6420, 0)
    OP_6C(134000, 0)
    OP_6E(626, 0)
    PlaySE(299, 0x00, 0x64)
    PlaySE(121, 0x01, 0x64)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_6241')
    def lambda_6241():
        CameraMove(8520, -3850, -19480, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6241)

    @scena.Lambda('lambda_6259')
    def lambda_6259():
        OP_67(0, 3330, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6259)

    @scena.Lambda('lambda_6271')
    def lambda_6271():
        OP_6C(147000, 12000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6271)

    CreateThread(0x000F, 0x00, 0x00, func_35_7962)
    CreateThread(0x0010, 0x00, 0x00, func_36_7AF8)
    CreateThread(0x0011, 0x00, 0x00, func_37_7C8E)
    CreateThread(0x0012, 0x00, 0x00, func_38_7E24)
    CreateThread(0x0013, 0x00, 0x00, func_39_7FBA)
    Sleep(19000)

    Fade(500)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000F, 0x03)
    TerminateThread(0x0010, 0x00)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0010, 0x03)
    TerminateThread(0x0011, 0x00)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0011, 0x03)
    TerminateThread(0x0012, 0x00)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0012, 0x03)
    TerminateThread(0x0013, 0x00)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0013, 0x03)
    ChrSetPos(0x000F, 250000, -6000, 0, 270)
    ChrSetPos(0x0010, 350000, -6000, 10000, 270)
    ChrSetPos(0x0011, 450000, -6000, -10000, 270)
    ChrSetPos(0x0012, 550000, -6000, 14000, 270)
    ChrSetPos(0x0013, 650000, -6000, -14000, 270)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)
    OP_D1(0x0012, 0, 270000, 0, 0)
    OP_D1(0x0013, 0, 270000, 0, 0)
    OP_6F(0x0002, 800)
    OP_70(0x0002, 900)
    OP_6F(0x0003, 800)
    OP_70(0x0003, 900)
    OP_6F(0x0004, 800)
    OP_70(0x0004, 900)
    OP_6F(0x0005, 800)
    OP_70(0x0005, 900)
    OP_6F(0x0006, 800)
    OP_70(0x0006, 900)
    OP_76(0x00FF, 0x00000000, 0x0001, -20, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -20, -2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -50, -5, 0, 0x00, 0x00)
    CameraMove(30440, -6550, 0, 0)
    OP_67(0, 1450, -10000, 0)
    CameraSetDistance(5720, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_D0(375000, 0)

    @scena.Lambda('lambda_646F')
    def lambda_646F():
        OP_D1(0x00FE, 0, 270000, -20000, 3000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_646F)

    @scena.Lambda('lambda_6489')
    def lambda_6489():
        OP_D1(0x00FE, 0, 270000, 20000, 3000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_6489)

    @scena.Lambda('lambda_64A3')
    def lambda_64A3():
        OP_D1(0x00FE, 0, 270000, -35000, 5000)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_64A3)

    @scena.Lambda('lambda_64BD')
    def lambda_64BD():
        OP_D1(0x00FE, 0, 270000, 35000, 5000)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_64BD)

    @scena.Lambda('lambda_64D7')
    def lambda_64D7():
        ChrMoveTo(0x00FE, -100000, -8000, 0, 120000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_64D7)

    @scena.Lambda('lambda_64F2')
    def lambda_64F2():
        ChrMoveTo(0x00FE, -100000, -8000, -10000, 120000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_64F2)

    @scena.Lambda('lambda_650D')
    def lambda_650D():
        ChrMoveTo(0x00FE, -100000, -8000, 10000, 120000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_650D)

    @scena.Lambda('lambda_6528')
    def lambda_6528():
        ChrMoveTo(0x00FE, -100000, -6000, -14000, 120000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6528)

    @scena.Lambda('lambda_6543')
    def lambda_6543():
        ChrMoveTo(0x00FE, -100000, -6000, 14000, 120000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_6543)

    Sleep(6000)

    FadeOut(1000, 0, -1)
    OP_0D()
    CreateThread(0x0015, 0x03, 0x00, func_2F_75E6)
    CameraMove(-2080, -10000, 0, 0)
    OP_67(0, 14540, -10000, 0)
    CameraSetDistance(8420, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_D0(360000, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -5, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -10, -2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -25, -5, 0, 0x00, 0x00)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 555000, 0)
    OP_72(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    Sleep(1000)

    OP_6F(0x0001, 200)
    OP_70(0x0001, 600)
    CreateThread(0x0015, 0x03, 0x00, func_30_7632)
    FadeIn(2000, 0)
    OP_0D()

    @scena.Lambda('lambda_6652')
    def lambda_6652():
        CameraMove(20000, -10000, 0, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6652)

    @scena.Lambda('lambda_666A')
    def lambda_666A():
        OP_67(0, 1800, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_666A)

    @scena.Lambda('lambda_6682')
    def lambda_6682():
        CameraSetDistance(6160, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6682)

    WaitForThreadExit(0x0000, 0x0000)
    OP_72(0x0001, 0x0020)
    OP_73(0x0001)

    @scena.Lambda('lambda_669F')
    def lambda_669F():
        CameraMove(4740, -8700, 19700, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_669F)

    @scena.Lambda('lambda_66B7')
    def lambda_66B7():
        OP_6C(54000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_66B7)

    @scena.Lambda('lambda_66C7')
    def lambda_66C7():
        CameraSetDistance(5780, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_66C7)

    PlaySE(118, 0x00, 0x64)
    OP_6F(0x0001, 601)
    OP_70(0x0001, 900)
    Sleep(1500)

    PlaySE(273, 0x00, 0x64)
    OP_73(0x0001)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 901)
    OP_70(0x0001, 1500)
    Sleep(1000)

    @scena.Lambda('lambda_670F')
    def lambda_670F():
        ChrMoveTo(0x00FE, -100000, 1000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_670F)

    Sleep(100)

    @scena.Lambda('lambda_672F')
    def lambda_672F():
        ChrMoveTo(0x00FE, -100000, 1000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_672F)

    Sleep(100)

    @scena.Lambda('lambda_674F')
    def lambda_674F():
        ChrMoveTo(0x00FE, -100000, 1000, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_674F)

    Sleep(100)

    @scena.Lambda('lambda_676F')
    def lambda_676F():
        ChrMoveTo(0x00FE, -100000, 1000, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_676F)

    Sleep(100)

    @scena.Lambda('lambda_678F')
    def lambda_678F():
        ChrMoveTo(0x00FE, -100000, 1000, 0, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_678F)

    Sleep(100)

    @scena.Lambda('lambda_67AF')
    def lambda_67AF():
        ChrMoveTo(0x00FE, -100000, 1000, 0, 36000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_67AF)

    Sleep(100)

    @scena.Lambda('lambda_67CF')
    def lambda_67CF():
        ChrMoveTo(0x00FE, -100000, 1000, 0, 56000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_67CF)

    Sleep(1000)

    Fade(1000)
    TerminateThread(0x000E, 0x01)
    CameraMove(20000, -10000, 0, 0)
    OP_67(0, 1800, -10000, 0)
    CameraSetDistance(6160, 0)
    OP_6C(90000, 0)
    OP_6E(536, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    ChrSetPos(0x000E, 150000, 0, 0, 270)

    @scena.Lambda('lambda_685D')
    def lambda_685D():
        ChrMoveTo(0x00FE, -100000, 1000, 0, 84000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_685D)

    Sleep(800)

    @scena.Lambda('lambda_687D')
    def lambda_687D():
        CameraMove(-20000, 11800, 0, 2600)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_687D)

    @scena.Lambda('lambda_6895')
    def lambda_6895():
        OP_67(0, -4600, -10000, 2600)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6895)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_72(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000F, 0x03)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0010, 0x03)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0011, 0x03)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0012, 0x03)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0013, 0x03)
    ChrSetPos(0x0016, -300000, 0, 0, 90)
    ChrSetPos(0x000E, -500000, 0, 0, 90)
    ChrSetPos(0x000F, 10000, -8000, 0, 270)
    ChrSetPos(0x0010, 25000, -8000, 25000, 270)
    ChrSetPos(0x0011, 25000, -8000, -27000, 270)
    ChrSetPos(0x0012, 50000, -2000, 15000, 270)
    ChrSetPos(0x0013, 50000, -2000, -17000, 270)
    OP_D1(0x000E, 0, 90000, 0, 0)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 266000, -5000, 0)
    OP_D1(0x0011, 0, 274000, 5000, 0)
    OP_D1(0x0012, 0, 270000, 0, 0)
    OP_D1(0x0013, 0, 270000, 0, 0)
    CameraMove(-60920, -6600, 8860, 0)
    OP_67(0, 1880, -10000, 0)
    CameraSetDistance(7840, 0)
    OP_6C(106000, 0)
    OP_6E(536, 0)
    OP_D0(375000, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -20, -2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -50, -5, 0, 0x00, 0x00)
    Sleep(1000)

    CreateThread(0x0015, 0x03, 0x00, func_31_7680)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_6A8C')
    def lambda_6A8C():
        ChrMoveTo(0x00FE, -100000, -8000, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_6A8C)

    @scena.Lambda('lambda_6AA7')
    def lambda_6AA7():
        ChrMoveTo(0x00FE, -100000, -8000, 15000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6AA7)

    @scena.Lambda('lambda_6AC2')
    def lambda_6AC2():
        ChrMoveTo(0x00FE, -100000, -8000, -17000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6AC2)

    @scena.Lambda('lambda_6ADD')
    def lambda_6ADD():
        ChrMoveTo(0x00FE, -100000, -8000, 30000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6ADD)

    @scena.Lambda('lambda_6AF8')
    def lambda_6AF8():
        ChrMoveTo(0x00FE, -100000, -8000, -34000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_6AF8)

    @scena.Lambda('lambda_6B13')
    def lambda_6B13():
        ChrMoveTo(0x00FE, -100000, -2000, 10000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6B13)

    @scena.Lambda('lambda_6B2E')
    def lambda_6B2E():
        ChrMoveTo(0x00FE, -100000, -2000, -7000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_6B2E)

    def _loc_6B43(): pass

    label('loc_6B43')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_6B59',
    )

    Sleep(15)

    Jump('loc_6B43')

    def _loc_6B59(): pass

    label('loc_6B59')

    CreateThread(0x0016, 0x00, 0x00, func_3A_8150)
    Sleep(500)

    OP_12(0x00004E20, 0x000B8538, 0x000007D0)

    @scena.Lambda('lambda_6B78')
    def lambda_6B78():
        ChrMoveTo(0x00FE, -300000, 0, 0, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_6B78)

    @scena.Lambda('lambda_6B93')
    def lambda_6B93():
        CameraMove(-161860, -6600, 14140, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_6B93)

    @scena.Lambda('lambda_6BAB')
    def lambda_6BAB():
        OP_67(0, 4460, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6BAB)

    @scena.Lambda('lambda_6BC3')
    def lambda_6BC3():
        CameraSetDistance(7650, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6BC3)

    @scena.Lambda('lambda_6BD3')
    def lambda_6BD3():
        OP_6C(250000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6BD3)

    @scena.Lambda('lambda_6BE3')
    def lambda_6BE3():
        OP_D0(345000, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_6BE3)

    WaitForThreadExit(0x0000, 0x0001)

    @scena.Lambda('lambda_6BF8')
    def lambda_6BF8():
        OP_67(0, 2640, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6BF8)

    Sleep(1000)

    Fade(500)
    OP_24(0x0079, 0x28)
    OP_24(0x0125, 0x64)
    OP_11(0xB8, 0xD8, 0xFF, 20000, 555000, 0)
    StopEffect(0x00, 0x00)
    StopEffect(0x01, 0x00)
    StopEffect(0x02, 0x00)
    StopEffect(0x03, 0x00)
    StopEffect(0x04, 0x00)
    OP_72(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0013, 0x01)
    ChrSetPos(0x0016, 150000, 0, 0, 90)
    ChrSetPos(0x000E, 0, 0, 0, 90)
    OP_D1(0x000E, 0, 90000, 0, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, 15, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, 20, 2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, 50, 5, 0, 0x00, 0x00)
    CameraMove(45680, -8500, -5700, 0)
    OP_67(0, 1840, -10000, 0)
    CameraSetDistance(9750, 0)
    OP_6C(252000, 0)
    OP_6E(536, 0)
    CreateThread(0x0016, 0x00, 0x00, func_3B_826E)
    CreateThread(0x000E, 0x00, 0x00, func_33_77A4)
    WaitForThreadExit(0x000E, 0x0000)
    WaitForThreadExit(0x000E, 0x0001)
    PlayEffect(0x04, 0x00, 0x000E, 7000, -2000, 24000, 0, 0, 0, 3000, 3000, 3000, 0x0016, 0, 0, 0, 0)
    PlaySE(698, 0x00, 0x64)
    OP_7C(400, 0, 3000, 600)
    WaitEffect(0x00, 0x00)
    Sleep(400)

    PlayEffect(0x04, 0x00, 0x000E, 7000, -2000, 24000, 0, 0, 0, 3000, 3000, 3000, 0x0016, 0, 0, 0, 0)
    PlaySE(698, 0x00, 0x64)
    OP_7C(400, 0, 3000, 600)
    WaitEffect(0x00, 0x02)
    Fade(500)
    OP_24(0x0079, 0x64)
    OP_24(0x0125, 0x3C)
    MapClearFlags(0x00000010)
    TerminateThread(0x000E, 0x03)
    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    ChrSetPos(0x000E, -300000, -4000, -20000, 90)
    ChrSetPos(0x000F, 0, -4000, 0, 270)
    ChrSetPos(0x0010, 0, -4000, 20000, 270)
    ChrSetPos(0x0011, 50000, -4000, 20000, 270)
    ChrSetPos(0x0012, 50000, -4000, 20000, 270)
    ChrSetPos(0x0013, 50000, -4000, 20000, 270)
    OP_D1(0x000E, 0, 86000, 0, 0)
    OP_D1(0x000F, 0, 270000, -5000, 0)
    OP_D1(0x0010, 0, 270000, 5000, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)
    OP_D1(0x0012, 0, 270000, 0, 0)
    OP_D1(0x0013, 0, 270000, 0, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -20, -2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -50, -5, 0, 0x00, 0x00)
    CameraMove(-54120, -10000, -5500, 0)
    OP_67(0, 1480, -10000, 0)
    CameraSetDistance(9750, 0)
    OP_6C(252000, 0)
    OP_6E(536, 0)
    CreateThread(0x0010, 0x02, 0x00, func_3F_8943)
    Sleep(600)

    CreateThread(0x000F, 0x02, 0x00, func_3D_86C0)
    Sleep(2000)

    OP_11(0xB8, 0xD8, 0xFF, 20000, 2555000, 0)
    MapSetFlags(0x00000010)
    OP_12(0x00004E20, 0x000B8538, 0x00000BB8)
    Sleep(1000)

    CreateThread(0x0000, 0x03, 0x00, func_20_49D4)
    PlayEffect(0x05, 0x00, 0x0011, 0, 1000, -12000, 176, 0, -26, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_6FEB')
    def lambda_6FEB():
        ChrMoveTo(0x00FE, -200000, -4000, -5000, 70000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6FEB)

    Sleep(500)

    @scena.Lambda('lambda_700B')
    def lambda_700B():
        OP_D1(0x00FE, 0, 266000, 20000, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_700B)

    Sleep(1000)

    Fade(500)
    OP_24(0x0079, 0x64)
    OP_24(0x0125, 0x64)
    TerminateThread(0x0011, 0x01)
    TerminateThread(0x0011, 0x03)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0012, 0x03)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0013, 0x03)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    ChrSetPos(0x000E, 0, 2000, 0, 90)
    ChrSetPos(0x000F, 150000, 0, -10000, 270)
    ChrSetPos(0x0010, 150000, 0, 40000, 270)
    ChrSetPos(0x0011, 150000, 5000, 20000, 270)
    OP_D1(0x000E, 0, 90000, 0, 0)
    OP_D1(0x000F, 0, 270000, 0, 0)
    OP_D1(0x0010, 0, 270000, 0, 0)
    OP_D1(0x0011, 0, 270000, 0, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, 15, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, 20, 2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, 50, 5, 0, 0x00, 0x00)
    CameraMove(79930, -8400, -24930, 0)
    OP_67(0, 1480, -10000, 0)
    CameraSetDistance(12090, 0)
    OP_6C(120000, 0)
    OP_6E(536, 0)
    OP_D0(350000, 0)

    @scena.Lambda('lambda_717E')
    def lambda_717E():
        CameraMove(13700, -4100, -18370, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_717E)

    @scena.Lambda('lambda_7196')
    def lambda_7196():
        OP_6C(192000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_7196)

    PlayEffect(0x05, 0x00, 0x000F, -500, 1000, -12000, 180, 0, 10, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_71DB')
    def lambda_71DB():
        OP_D1(0x00FE, 0, 270000, -20000, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_71DB)

    @scena.Lambda('lambda_71F5')
    def lambda_71F5():
        ChrMoveTo(0x00FE, -200000, 10000, -20000, 100000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_71F5)

    @scena.Lambda('lambda_7210')
    def lambda_7210():
        OP_D1(0x00FE, 0, 90000, 25000, 1000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_7210)

    @scena.Lambda('lambda_722A')
    def lambda_722A():
        ChrMoveTo(0x00FE, 0, 2000, 20000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_722A)

    WaitForThreadExit(0x0000, 0x0000)
    OP_72(0x0003, 0x0004)
    OP_72(0x0004, 0x0004)
    StopEffect(0x00, 0x02)
    CreateThread(0x000E, 0x00, 0x00, func_34_784C)
    Sleep(1000)

    PlayEffect(0x05, 0x00, 0x0010, 500, 1000, -12000, 180, 0, -40, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_7298')
    def lambda_7298():
        OP_D1(0x00FE, 0, 270000, 40000, 2500)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_7298)

    @scena.Lambda('lambda_72B2')
    def lambda_72B2():
        ChrMoveTo(0x00FE, -200000, 0, 45000, 80000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_72B2)

    WaitForThreadExit(0x000E, 0x0003)

    @scena.Lambda('lambda_72D2')
    def lambda_72D2():
        OP_D1(0x00FE, 0, 90000, 0, 10000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_72D2)

    PlayEffect(0x04, 0x01, 0x000E, 2000, -2000, 28000, 0, 0, 0, 3000, 3000, 3000, 0x0011, 0, 0, 0, 0)
    PlaySE(698, 0x00, 0x64)
    OP_7C(400, 0, 3000, 600)
    WaitEffect(0x01, 0x02)
    StopEffect(0x00, 0x02)
    OP_23(0x0235)
    TerminateThread(0x0000, 0x03)
    PlayEffect(0x01, 0xFF, 0x0011, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_7379')
    def lambda_7379():
        OP_D1(0x00FE, 20000, 270000, -60000, 4000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_7379)

    @scena.Lambda('lambda_7393')
    def lambda_7393():
        ChrMoveTo(0x00FE, -150000, -30000, 20000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7393)

    Sleep(2500)

    CreateThread(0x0015, 0x03, 0x00, func_2F_75E6)
    PlayEffect(0x02, 0xFF, 0x00FF, 20000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0xFF, 0x00FF, 5000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x02, 0xFF, 0x00FF, -10000, -10000, 30000, 270, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)

    @scena.Lambda('lambda_746D')
    def lambda_746D():
        CameraMove(23830, -4100, -19830, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_746D)

    @scena.Lambda('lambda_7485')
    def lambda_7485():
        OP_67(0, 1580, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_7485)

    @scena.Lambda('lambda_749D')
    def lambda_749D():
        OP_6C(243000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_749D)

    @scena.Lambda('lambda_74AD')
    def lambda_74AD():
        OP_D1(0x00FE, 0, 90000, 20000, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_74AD)

    @scena.Lambda('lambda_74C7')
    def lambda_74C7():
        ChrMoveTo(0x00FE, 200000, 2000, 20000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_74C7)

    Sleep(600)

    @scena.Lambda('lambda_74E7')
    def lambda_74E7():
        ChrMoveTo(0x00FE, 200000, 2000, 20000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_74E7)

    Sleep(500)

    @scena.Lambda('lambda_7507')
    def lambda_7507():
        ChrMoveTo(0x00FE, 200000, 2000, 20000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_7507)

    Sleep(400)

    @scena.Lambda('lambda_7527')
    def lambda_7527():
        ChrMoveTo(0x00FE, 200000, 2000, 20000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_7527)

    Sleep(300)

    @scena.Lambda('lambda_7547')
    def lambda_7547():
        ChrMoveTo(0x00FE, 200000, 2000, 20000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_7547)

    Sleep(200)

    @scena.Lambda('lambda_7567')
    def lambda_7567():
        ChrMoveTo(0x00FE, 200000, 2000, 20000, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_7567)

    Sleep(100)

    @scena.Lambda('lambda_7587')
    def lambda_7587():
        ChrMoveTo(0x00FE, 200000, 2000, 20000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_7587)

    Sleep(100)

    @scena.Lambda('lambda_75A7')
    def lambda_75A7():
        ChrMoveTo(0x00FE, 200000, 2000, 20000, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_75A7)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    OP_DC()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x0440, 0, 0x2200))
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x002F offset: 0x75E6
@scena.Code('func_2F_75E6')
def func_2F_75E6():
    OP_24(0x0079, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x46)
    Sleep(100)

    OP_24(0x0079, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x32)
    Sleep(100)

    OP_24(0x0079, 0x28)
    Sleep(100)

    OP_24(0x0079, 0x1E)
    Sleep(100)

    OP_24(0x0079, 0x14)
    Sleep(100)

    OP_23(0x0079)

    Return()

# id: 0x0030 offset: 0x7632
@scena.Code('func_30_7632')
def func_30_7632():
    PlaySE(293, 0x01, 0x14)
    Sleep(100)

    OP_24(0x0125, 0x1E)
    Sleep(100)

    OP_24(0x0125, 0x28)
    Sleep(100)

    OP_24(0x0125, 0x32)
    Sleep(100)

    OP_24(0x0125, 0x3C)
    Sleep(100)

    OP_24(0x0125, 0x46)
    Sleep(100)

    OP_24(0x0125, 0x50)
    Sleep(100)

    OP_24(0x0125, 0x5A)
    Sleep(100)

    OP_24(0x0125, 0x64)

    Return()

# id: 0x0031 offset: 0x7680
@scena.Code('func_31_7680')
def func_31_7680():
    OP_24(0x0125, 0x5A)
    PlaySE(121, 0x01, 0x14)
    Sleep(100)

    OP_24(0x0125, 0x50)
    OP_24(0x0079, 0x1E)
    Sleep(100)

    OP_24(0x0125, 0x46)
    OP_24(0x0079, 0x28)
    Sleep(100)

    OP_24(0x0125, 0x3C)
    OP_24(0x0079, 0x32)
    Sleep(100)

    OP_24(0x0125, 0x32)
    OP_24(0x0079, 0x3C)
    Sleep(100)

    OP_24(0x0125, 0x28)
    OP_24(0x0079, 0x46)
    Sleep(100)

    OP_24(0x0079, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x64)

    Return()

# id: 0x0032 offset: 0x76E6
@scena.Code('func_32_76E6')
def func_32_76E6():
    Sleep(1000)

    @scena.Lambda('lambda_76F1')
    def lambda_76F1():
        ChrMoveTo(0x00FE, -200000, -4000, -5000, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_76F1)

    Sleep(500)

    @scena.Lambda('lambda_7711')
    def lambda_7711():
        OP_D1(0x00FE, 0, 266000, 20000, 1500)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_7711)

    Sleep(1000)

    @scena.Lambda('lambda_7730')
    def lambda_7730():
        ChrMoveTo(0x00FE, -200000, -4000, -5000, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7730)

    Sleep(500)

    @scena.Lambda('lambda_7750')
    def lambda_7750():
        OP_D1(0x00FE, 0, 266000, 20000, 1500)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_7750)

    Sleep(1000)

    @scena.Lambda('lambda_776F')
    def lambda_776F():
        ChrMoveTo(0x00FE, -200000, -4000, -5000, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_776F)

    Sleep(500)

    @scena.Lambda('lambda_778F')
    def lambda_778F():
        OP_D1(0x00FE, 0, 266000, 20000, 1500)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_778F)

    Return()

# id: 0x0033 offset: 0x77A4
@scena.Code('func_33_77A4')
def func_33_77A4():
    OP_98(0x00, 0x000E)
    OP_98(0x01, 40000, 0, -20000)
    OP_98(0x01, 70000, 0, 20000)
    OP_98(0x01, 70001, 0, 20001)

    @scena.Lambda('lambda_77D8')
    def lambda_77D8():
        OP_98(0x02, 0x00FE, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_77D8)

    @scena.Lambda('lambda_77E8')
    def lambda_77E8():
        OP_D1(0x00FE, 0, 90000, -20000, 1200)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_77E8)

    WaitForThreadExit(0x000E, 0x0003)

    @scena.Lambda('lambda_7807')
    def lambda_7807():
        OP_D1(0x00FE, 0, 98000, 20000, 2400)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_7807)

    @scena.Lambda('lambda_7821')
    def lambda_7821():
        CameraMove(45680, -10500, -5700, 2400)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_7821)

    @scena.Lambda('lambda_7839')
    def lambda_7839():
        OP_67(0, 1480, -10000, 2400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_7839)

    Return()

# id: 0x0034 offset: 0x784C
@scena.Code('func_34_784C')
def func_34_784C():
    @scena.Lambda('lambda_7852')
    def lambda_7852():
        OP_D1(0x00FE, 0, 90000, -20000, 2400)

        ExitThread()

    DispatchAsync(0x000E, 0x0003, lambda_7852)

    @scena.Lambda('lambda_786C')
    def lambda_786C():
        ChrMoveTo(0x00FE, 5000, 8000, -5000, 2800, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_786C)

    Sleep(300)

    @scena.Lambda('lambda_788C')
    def lambda_788C():
        ChrMoveTo(0x00FE, 5000, 8000, -5000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_788C)

    Sleep(300)

    @scena.Lambda('lambda_78AC')
    def lambda_78AC():
        ChrMoveTo(0x00FE, 5000, 8000, -5000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_78AC)

    Sleep(300)

    @scena.Lambda('lambda_78CC')
    def lambda_78CC():
        ChrMoveTo(0x00FE, 5000, 8000, -5000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_78CC)

    Sleep(300)

    @scena.Lambda('lambda_78EC')
    def lambda_78EC():
        ChrMoveTo(0x00FE, 5000, 8000, -5000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_78EC)

    Sleep(800)

    @scena.Lambda('lambda_790C')
    def lambda_790C():
        ChrMoveTo(0x00FE, 5000, 8000, -5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_790C)

    Sleep(300)

    @scena.Lambda('lambda_792C')
    def lambda_792C():
        ChrMoveTo(0x00FE, 5000, 8000, -5000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_792C)

    Sleep(300)

    @scena.Lambda('lambda_794C')
    def lambda_794C():
        ChrMoveTo(0x00FE, 5000, 8000, -5000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_794C)

    Return()

# id: 0x0035 offset: 0x7962
@scena.Code('func_35_7962')
def func_35_7962():
    @scena.Lambda('lambda_7968')
    def lambda_7968():
        ChrMoveTo(0x00FE, -2000, 4000, -27000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7968)

    Sleep(13000)

    @scena.Lambda('lambda_7988')
    def lambda_7988():
        ChrMoveTo(0x00FE, -2000, 4000, -27000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7988)

    Sleep(400)

    @scena.Lambda('lambda_79A8')
    def lambda_79A8():
        ChrMoveTo(0x00FE, -2000, 4000, -27000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_79A8)

    Sleep(1500)

    @scena.Lambda('lambda_79C8')
    def lambda_79C8():
        OP_D1(0x00FE, 0, 270000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_79C8)

    @scena.Lambda('lambda_79E2')
    def lambda_79E2():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_79E2)

    Sleep(100)

    @scena.Lambda('lambda_7A02')
    def lambda_7A02():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7A02)

    Sleep(100)

    @scena.Lambda('lambda_7A22')
    def lambda_7A22():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7A22)

    Sleep(100)

    @scena.Lambda('lambda_7A42')
    def lambda_7A42():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7A42)

    Sleep(100)

    @scena.Lambda('lambda_7A62')
    def lambda_7A62():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7A62)

    Sleep(100)

    @scena.Lambda('lambda_7A82')
    def lambda_7A82():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7A82)

    Sleep(100)

    @scena.Lambda('lambda_7AA2')
    def lambda_7AA2():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7AA2)

    Sleep(100)

    @scena.Lambda('lambda_7AC2')
    def lambda_7AC2():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7AC2)

    Sleep(100)

    @scena.Lambda('lambda_7AE2')
    def lambda_7AE2():
        ChrMoveTo(0x00FE, -102000, 4000, 0, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7AE2)

    Return()

# id: 0x0036 offset: 0x7AF8
@scena.Code('func_36_7AF8')
def func_36_7AF8():
    @scena.Lambda('lambda_7AFE')
    def lambda_7AFE():
        ChrMoveTo(0x00FE, 29000, 6000, -19000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7AFE)

    Sleep(12000)

    @scena.Lambda('lambda_7B1E')
    def lambda_7B1E():
        ChrMoveTo(0x00FE, 29000, 6000, -19000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7B1E)

    Sleep(400)

    @scena.Lambda('lambda_7B3E')
    def lambda_7B3E():
        ChrMoveTo(0x00FE, 29000, 6000, -19000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7B3E)

    Sleep(3500)

    @scena.Lambda('lambda_7B5E')
    def lambda_7B5E():
        OP_D1(0x00FE, 0, 270000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_7B5E)

    @scena.Lambda('lambda_7B78')
    def lambda_7B78():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7B78)

    Sleep(100)

    @scena.Lambda('lambda_7B98')
    def lambda_7B98():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7B98)

    Sleep(100)

    @scena.Lambda('lambda_7BB8')
    def lambda_7BB8():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7BB8)

    Sleep(100)

    @scena.Lambda('lambda_7BD8')
    def lambda_7BD8():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7BD8)

    Sleep(100)

    @scena.Lambda('lambda_7BF8')
    def lambda_7BF8():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7BF8)

    Sleep(100)

    @scena.Lambda('lambda_7C18')
    def lambda_7C18():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7C18)

    Sleep(100)

    @scena.Lambda('lambda_7C38')
    def lambda_7C38():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7C38)

    Sleep(100)

    @scena.Lambda('lambda_7C58')
    def lambda_7C58():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7C58)

    Sleep(100)

    @scena.Lambda('lambda_7C78')
    def lambda_7C78():
        ChrMoveTo(0x00FE, -71000, 2000, -4000, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7C78)

    Return()

# id: 0x0037 offset: 0x7C8E
@scena.Code('func_37_7C8E')
def func_37_7C8E():
    @scena.Lambda('lambda_7C94')
    def lambda_7C94():
        ChrMoveTo(0x00FE, 0, 3000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7C94)

    Sleep(12000)

    @scena.Lambda('lambda_7CB4')
    def lambda_7CB4():
        ChrMoveTo(0x00FE, 0, 3000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7CB4)

    Sleep(400)

    @scena.Lambda('lambda_7CD4')
    def lambda_7CD4():
        ChrMoveTo(0x00FE, 0, 3000, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7CD4)

    Sleep(2000)

    @scena.Lambda('lambda_7CF4')
    def lambda_7CF4():
        OP_D1(0x00FE, 0, 270000, 20000, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_7CF4)

    @scena.Lambda('lambda_7D0E')
    def lambda_7D0E():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7D0E)

    Sleep(100)

    @scena.Lambda('lambda_7D2E')
    def lambda_7D2E():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7D2E)

    Sleep(100)

    @scena.Lambda('lambda_7D4E')
    def lambda_7D4E():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7D4E)

    Sleep(100)

    @scena.Lambda('lambda_7D6E')
    def lambda_7D6E():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7D6E)

    Sleep(100)

    @scena.Lambda('lambda_7D8E')
    def lambda_7D8E():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7D8E)

    Sleep(100)

    @scena.Lambda('lambda_7DAE')
    def lambda_7DAE():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7DAE)

    Sleep(100)

    @scena.Lambda('lambda_7DCE')
    def lambda_7DCE():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7DCE)

    Sleep(100)

    @scena.Lambda('lambda_7DEE')
    def lambda_7DEE():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7DEE)

    Sleep(100)

    @scena.Lambda('lambda_7E0E')
    def lambda_7E0E():
        ChrMoveTo(0x00FE, -100000, 3000, 0, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7E0E)

    Return()

# id: 0x0038 offset: 0x7E24
@scena.Code('func_38_7E24')
def func_38_7E24():
    @scena.Lambda('lambda_7E2A')
    def lambda_7E2A():
        ChrMoveTo(0x00FE, 27000, 6000, 2000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7E2A)

    Sleep(12000)

    @scena.Lambda('lambda_7E4A')
    def lambda_7E4A():
        ChrMoveTo(0x00FE, 27000, 6000, 2000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7E4A)

    Sleep(400)

    @scena.Lambda('lambda_7E6A')
    def lambda_7E6A():
        ChrMoveTo(0x00FE, 27000, 6000, 2000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7E6A)

    Sleep(4200)

    @scena.Lambda('lambda_7E8A')
    def lambda_7E8A():
        OP_D1(0x00FE, 0, 270000, 20000, 2000)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_7E8A)

    @scena.Lambda('lambda_7EA4')
    def lambda_7EA4():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7EA4)

    Sleep(100)

    @scena.Lambda('lambda_7EC4')
    def lambda_7EC4():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7EC4)

    Sleep(100)

    @scena.Lambda('lambda_7EE4')
    def lambda_7EE4():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7EE4)

    Sleep(100)

    @scena.Lambda('lambda_7F04')
    def lambda_7F04():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7F04)

    Sleep(100)

    @scena.Lambda('lambda_7F24')
    def lambda_7F24():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7F24)

    Sleep(100)

    @scena.Lambda('lambda_7F44')
    def lambda_7F44():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7F44)

    Sleep(100)

    @scena.Lambda('lambda_7F64')
    def lambda_7F64():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7F64)

    Sleep(100)

    @scena.Lambda('lambda_7F84')
    def lambda_7F84():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7F84)

    Sleep(100)

    @scena.Lambda('lambda_7FA4')
    def lambda_7FA4():
        ChrMoveTo(0x00FE, -73000, 6000, 12000, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7FA4)

    Return()

# id: 0x0039 offset: 0x7FBA
@scena.Code('func_39_7FBA')
def func_39_7FBA():
    @scena.Lambda('lambda_7FC0')
    def lambda_7FC0():
        ChrMoveTo(0x00FE, 6000, -3000, 14000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_7FC0)

    Sleep(12000)

    @scena.Lambda('lambda_7FE0')
    def lambda_7FE0():
        ChrMoveTo(0x00FE, 6000, -3000, 14000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_7FE0)

    Sleep(400)

    @scena.Lambda('lambda_8000')
    def lambda_8000():
        ChrMoveTo(0x00FE, 6000, -3000, 14000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_8000)

    Sleep(3000)

    @scena.Lambda('lambda_8020')
    def lambda_8020():
        OP_D1(0x00FE, 0, 270000, 20000, 2000)

        ExitThread()

    DispatchAsync(0x0013, 0x0003, lambda_8020)

    @scena.Lambda('lambda_803A')
    def lambda_803A():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_803A)

    Sleep(100)

    @scena.Lambda('lambda_805A')
    def lambda_805A():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_805A)

    Sleep(100)

    @scena.Lambda('lambda_807A')
    def lambda_807A():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_807A)

    Sleep(100)

    @scena.Lambda('lambda_809A')
    def lambda_809A():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_809A)

    Sleep(100)

    @scena.Lambda('lambda_80BA')
    def lambda_80BA():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_80BA)

    Sleep(100)

    @scena.Lambda('lambda_80DA')
    def lambda_80DA():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_80DA)

    Sleep(100)

    @scena.Lambda('lambda_80FA')
    def lambda_80FA():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_80FA)

    Sleep(100)

    @scena.Lambda('lambda_811A')
    def lambda_811A():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_811A)

    Sleep(100)

    @scena.Lambda('lambda_813A')
    def lambda_813A():
        ChrMoveTo(0x00FE, -94000, 3000, -10000, 55000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_813A)

    Return()

# id: 0x003A offset: 0x8150
@scena.Code('func_3A_8150')
def func_3A_8150():
    PlayEffect(0x00, 0x00, 0x000F, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x0016, 0, 0, 10000, 0)
    Sleep(300)

    PlayEffect(0x00, 0x01, 0x0010, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x0016, 0, 0, -5000, 0)
    Sleep(100)

    PlayEffect(0x00, 0x02, 0x0011, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x0016, 0, 0, 5000, 0)
    Sleep(400)

    PlayEffect(0x00, 0x03, 0x0012, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x0016, 0, 0, -5000, 0)
    Sleep(200)

    PlayEffect(0x00, 0x04, 0x0013, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0x0016, 0, 0, 0, 0)

    Return()

# id: 0x003B offset: 0x826E
@scena.Code('func_3B_826E')
def func_3B_826E():
    PlayEffect(0x00, 0xFF, 0x0016, 0, -8000, 15000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -100000, 0, 10000, 0)
    Sleep(200)

    PlayEffect(0x00, 0xFF, 0x0016, 0, -10000, 25000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -100000, 0, 20000, 0)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x0016, 0, -8000, 20000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -100000, 0, 30000, 0)
    Sleep(400)

    PlayEffect(0x00, 0xFF, 0x0016, 0, -10000, 50000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -100000, 0, 35000, 0)
    Sleep(200)

    PlayEffect(0x00, 0xFF, 0x0016, 0, -8000, 30000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -100000, 0, 40000, 0)
    Sleep(1200)

    ChrSetPos(0x0016, 160000, 0, 0, 90)
    PlayEffect(0x00, 0xFF, 0x0016, 0, -10000, -5000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -90000, 0, -45000, 0)
    Sleep(200)

    PlayEffect(0x00, 0xFF, 0x0016, 0, -8000, -25000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -90000, 0, -35000, 0)
    Sleep(300)

    PlayEffect(0x00, 0xFF, 0x0016, 0, -10000, -10000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -90000, 0, -40000, 0)
    Sleep(200)

    PlayEffect(0x00, 0xFF, 0x0016, 0, -6000, -20000, 0, 0, 0, 3000, 3000, 3000, 0x000E, -90000, 0, -25000, 0)

    Return()

# id: 0x003C offset: 0x8485
@scena.Code('func_3C_8485')
def func_3C_8485():
    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x03, 0x07, 0x00FE, 1000, -1000, 1000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x06, 0x00FE, 3000, 0, -3000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FE, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_8533')
    def lambda_8533():
        ChrMoveToRelativeAsync(0x00FE, 4000, -3000, -2000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_8533)

    OP_D1(0x00FE, 5000, 274000, -15000, 200)
    OP_D1(0x00FE, 0, 270000, 0, 300)
    OP_D1(0x00FE, 5000, 272000, -10000, 300)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_8590')
    def lambda_8590():
        OP_D1(0x00FE, 10000, 272000, -30000, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_8590)

    @scena.Lambda('lambda_85AA')
    def lambda_85AA():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_85AA)

    Sleep(200)

    @scena.Lambda('lambda_85CA')
    def lambda_85CA():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_85CA)

    Sleep(200)

    @scena.Lambda('lambda_85EA')
    def lambda_85EA():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_85EA)

    Sleep(200)

    @scena.Lambda('lambda_860A')
    def lambda_860A():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_860A)

    Sleep(200)

    @scena.Lambda('lambda_862A')
    def lambda_862A():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_862A)

    Sleep(200)

    @scena.Lambda('lambda_864A')
    def lambda_864A():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_864A)

    Sleep(200)

    @scena.Lambda('lambda_866A')
    def lambda_866A():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_866A)

    Sleep(200)

    @scena.Lambda('lambda_868A')
    def lambda_868A():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_868A)

    Sleep(200)

    @scena.Lambda('lambda_86AA')
    def lambda_86AA():
        ChrMoveTo(0x00FE, 20000, -20000, -2000, 52000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_86AA)

    Return()

# id: 0x003D offset: 0x86C0
@scena.Code('func_3D_86C0')
def func_3D_86C0():
    CreateThread(0x000F, 0x00, 0x00, func_3C_8485)
    Sleep(1400)

    PlayEffect(0x02, 0xFF, 0x00FF, 0, -10000, 0, 270, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x06, 0x00)
    StopEffect(0x07, 0x00)

    Return()

# id: 0x003E offset: 0x8708
@scena.Code('func_3E_8708')
def func_3E_8708():
    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayEffect(0x03, 0x05, 0x00FE, 0, -1000, 0, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x00FE, 3000, 0, -3000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FE, 0, 1000, 0, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_87B6')
    def lambda_87B6():
        ChrMoveToRelativeAsync(0x00FE, 3000, -2000, 2000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_87B6)

    OP_D1(0x00FE, -10000, 266000, 10000, 200)
    OP_D1(0x00FE, 5000, 270000, 0, 300)
    OP_D1(0x00FE, 0, 268000, 10000, 300)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_8813')
    def lambda_8813():
        OP_D1(0x00FE, 15000, 268000, 30000, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_8813)

    @scena.Lambda('lambda_882D')
    def lambda_882D():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_882D)

    Sleep(200)

    @scena.Lambda('lambda_884D')
    def lambda_884D():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_884D)

    Sleep(200)

    @scena.Lambda('lambda_886D')
    def lambda_886D():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_886D)

    Sleep(200)

    @scena.Lambda('lambda_888D')
    def lambda_888D():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_888D)

    Sleep(200)

    @scena.Lambda('lambda_88AD')
    def lambda_88AD():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_88AD)

    Sleep(200)

    @scena.Lambda('lambda_88CD')
    def lambda_88CD():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_88CD)

    Sleep(200)

    @scena.Lambda('lambda_88ED')
    def lambda_88ED():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_88ED)

    Sleep(200)

    @scena.Lambda('lambda_890D')
    def lambda_890D():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 40000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_890D)

    Sleep(200)

    @scena.Lambda('lambda_892D')
    def lambda_892D():
        ChrMoveTo(0x00FE, 20000, -20000, 22000, 52000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_892D)

    Return()

# id: 0x003F offset: 0x8943
@scena.Code('func_3F_8943')
def func_3F_8943():
    CreateThread(0x0010, 0x00, 0x00, func_3E_8708)
    Sleep(1400)

    PlayEffect(0x02, 0xFF, 0x00FF, 0, -10000, 20000, 260, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x04, 0x00)
    StopEffect(0x05, 0x00)

    Return()

# id: 0x0040 offset: 0x898B
@scena.Code('func_40_898B')
def func_40_898B():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x00, 'map\\\\mp009_00.eff')
    LoadEffect(0x01, 'battle\\\\btbomb00.eff')
    LoadEffect(0x02, 'map\\\\mpsmk0.eff')
    LoadEffect(0x03, 'map\\\\mp095_00.eff')
    LoadEffect(0x04, 'monster\\\\ms30800c.eff')
    LoadEffect(0x05, 'map\\\\mp106_00.eff')
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrClearFlags(0x0008, 0x0001)
    CameraMove(-84460, 1980, 25700, 0)
    OP_67(0, -2400, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(106000, 0)
    OP_6E(576, 0)
    PlaySE(451, 0x00, 0x64)
    OP_A1(0x000E, 0x0001)
    ChrSetPos(0x000E, -40000, 0, 0, 90)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000E, 0, 90000, 20000, 0)
    PlaySE(293, 0x01, 0x46)
    PlaySE(344, 0x01, 0x64)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 100)
    OP_70(0x0001, 150)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 3)
    ChrSetPos(0x0008, 0, 0, 0, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    OP_CF(0x0008, 0x02, 'Frame134_on_head')
    OP_A1(0x001E, 0x0002)
    ChrSetPos(0x001E, 200000, 80000, 80000, 270)
    ChrClearFlags(0x001E, 0x0100)
    OP_D1(0x001E, 0, 270000, 0, 0)
    OP_B0(0x0002, 0x14)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 320)
    OP_70(0x0002, 340)
    CameraMove(63620, -10000, 7720, 0)
    OP_67(0, 3450, -10000, 0)
    CameraSetDistance(10700, 0)
    OP_6C(200000, 0)
    OP_6E(1448, 0)
    OP_D0(360000, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, 10, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, 10, 2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, 25, 5, 0, 0x00, 0x00)
    OP_12(0x00004E20, 0x001E8480, 0x00000BB8)

    @scena.Lambda('lambda_8BCE')
    def lambda_8BCE():
        ChrMoveTo(0x00FE, 0, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_8BCE)

    OP_D1(0x001E, 0, 225000, 0, 0)
    ChrSetPos(0x001E, 100000, 20000, 100000, 270)
    FadeIn(1000, 0)
    Sleep(2700)

    PlaySE(345, 0x00, 0x64)
    Sleep(300)

    MapClearFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_8C33')
    def lambda_8C33():
        OP_D1(0x00FE, 10000, 225000, 40000, 1500)

        ExitThread()

    DispatchAsync(0x001E, 0x0003, lambda_8C33)

    @scena.Lambda('lambda_8C4D')
    def lambda_8C4D():
        OP_D0(355000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_8C4D)

    @scena.Lambda('lambda_8C5D')
    def lambda_8C5D():
        ChrMoveTo(0x00FE, 0, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_8C5D)

    Sleep(100)

    @scena.Lambda('lambda_8C7D')
    def lambda_8C7D():
        ChrMoveTo(0x00FE, 0, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_8C7D)

    Sleep(100)

    @scena.Lambda('lambda_8C9D')
    def lambda_8C9D():
        ChrMoveTo(0x00FE, 0, 0, 0, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_8C9D)

    Sleep(100)

    @scena.Lambda('lambda_8CBD')
    def lambda_8CBD():
        ChrMoveTo(0x00FE, 0, 0, 0, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_8CBD)

    Sleep(100)

    @scena.Lambda('lambda_8CDD')
    def lambda_8CDD():
        ChrMoveTo(0x00FE, 0, 0, 0, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_8CDD)

    Sleep(100)

    @scena.Lambda('lambda_8CFD')
    def lambda_8CFD():
        ChrMoveTo(0x00FE, 0, 0, 0, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_8CFD)

    Sleep(100)

    @scena.Lambda('lambda_8D1D')
    def lambda_8D1D():
        ChrMoveTo(0x00FE, 0, 0, 0, 50000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_8D1D)

    Sleep(900)

    Fade(500)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x0000, 0x00)
    TerminateThread(0x001E, 0x03)
    OP_71(0x0001, 0x0004)
    CameraMove(-84460, 1980, 25700, 0)
    OP_67(0, -2400, -10000, 0)
    CameraSetDistance(4050, 0)
    OP_6C(106000, 0)
    OP_6E(576, 0)
    OP_D0(340000, 0)
    ChrSetPos(0x001E, 150000, 80000, 80000, 270)
    OP_D1(0x001E, 0, 270000, 0, 0)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 5)
    ChrSetFlags(0x0008, 0x0008)

    @scena.Lambda('lambda_8DCC')
    def lambda_8DCC():
        OP_D0(360000, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_8DCC)

    OP_98(0x00, 0x001E)
    OP_98(0x01, 70000, 40000, -40000)
    OP_98(0x01, 0, 10000, 35000)
    OP_98(0x01, -120000, -10000, 25000)

    @scena.Lambda('lambda_8E0A')
    def lambda_8E0A():
        OP_98(0x02, 0x00FE, 60000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_8E0A)

    CreateThread(0x001E, 0x00, 0x00, func_45_9668)
    Sleep(5000)

    WaitForThreadExit(0x001E, 0x0001)
    Sleep(500)

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_76(0x00FF, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -10, -2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -25, -5, 0, 0x00, 0x00)
    ChrClearFlags(0x0008, 0x0008)
    CameraMove(-1030, 3860, -600, 0)
    OP_67(0, 8810, -10000, 0)
    CameraSetDistance(2090, 0)
    OP_6C(137000, 0)
    OP_6E(362, 0)
    ChrSetPos(0x001E, 0, 0, 0, 270)
    OP_D1(0x001E, 0, 270000, 0, 0)
    OP_0D()
    ChrSetPos(0x0000, 1310, 3860, -1340, 0)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#0140390113V#124F#5P──来，让我看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140390114V#123F当希望之翼折断时……\n',
            '你们能如何应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_DB()
    PlayBGM(132)
    Sleep(500)

    Play3DEffect(0x03, 0x00, 0x02, 'Frame34_Bone__33_', 0x00000000, 0x00000000, 0x00000000, 0x010E, 0x0000, 0x0000, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Play3DEffect(0x03, 0x01, 0x02, 'Frame26_Bone__25_', 0x00000000, 0x00000000, 0x00000000, 0x010E, 0x0000, 0x0000, 0x000003E8, 0x000003E8, 0x000003E8, 0x00000000)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(345, 0x00, 0x64)

    @scena.Lambda('lambda_8FF3')
    def lambda_8FF3():
        OP_D1(0x00FE, 0, 270000, 20000, 2000)

        ExitThread()

    DispatchAsync(0x001E, 0x0003, lambda_8FF3)

    @scena.Lambda('lambda_900D')
    def lambda_900D():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_900D)

    Sleep(100)

    @scena.Lambda('lambda_9028')
    def lambda_9028():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_9028)

    Sleep(100)

    @scena.Lambda('lambda_9043')
    def lambda_9043():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_9043)

    Sleep(100)

    @scena.Lambda('lambda_905E')
    def lambda_905E():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x000036B0, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_905E)

    Sleep(100)

    @scena.Lambda('lambda_9079')
    def lambda_9079():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x000055F0, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_9079)

    Sleep(100)

    @scena.Lambda('lambda_9094')
    def lambda_9094():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x00009470, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_9094)

    Sleep(100)

    @scena.Lambda('lambda_90AF')
    def lambda_90AF():
        OP_94(0x01, 0x00FE, 0x0000, 0x000186A0, 0x0000EA60, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_90AF)

    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x001E, 0x01)
    TerminateThread(0x001E, 0x03)
    OP_72(0x0001, 0x0004)
    OP_76(0x00FF, 0x00000000, 0x0001, -15, 0, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000001, 0x0001, -15, -2, 0, 0x00, 0x00)
    OP_76(0x00FF, 0x00000002, 0x0001, -40, -5, 0, 0x00, 0x00)
    ChrSetPos(0x001E, -120000, 0, -20000, 90)
    OP_D1(0x001E, 0, 90000, 0, 0)
    ChrSetPos(0x000E, 0, 6000, 0, 270)
    OP_D1(0x000E, 0, 270000, 0, 0)
    CameraMove(-12820, 5000, -13570, 0)
    OP_67(0, 1270, -10000, 0)
    CameraSetDistance(7550, 0)
    OP_6C(294000, 0)
    OP_6E(548, 0)
    CreateThread(0x001E, 0x00, 0x00, func_42_930D)
    OP_0D()

    @scena.Lambda('lambda_91C0')
    def lambda_91C0():
        CameraMove(520, 3000, 12000, 1900)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_91C0)

    @scena.Lambda('lambda_91D8')
    def lambda_91D8():
        OP_6C(354000, 1900)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_91D8)

    Sleep(5000)

    FadeOut(1000, 0, -1)
    OP_0D()
    StopEffect(0x00, 0x00)
    StopEffect(0x01, 0x00)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    OP_23(0x0125)
    OP_23(0x0158)
    OP_23(0x01C3)
    Sleep(1000)

    OP_C4(0x00, 0x00000010)
    FadeIn(1, 0)
    PlayMovie(0x00, 'ED6_DT45.dat', 0x0000, 0x0001)
    def _loc_9236(): pass

    label('loc_9236')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9250',
    )

    Sleep(100)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_924D',
    )

    Jump('loc_9250')

    def _loc_924D(): pass

    label('loc_924D')

    Jump('loc_9236')

    def _loc_9250(): pass

    label('loc_9250')

    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    Sleep(2000)

    OP_C4(0x01, 0x00000010)
    OP_AD('ED6_DT24/C_VIS149._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_20(0x00000BB8)
    OP_21()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x0455, 7, 0x22AF))
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0041 offset: 0x92AA
@scena.Code('func_41_92AA')
def func_41_92AA():
    ChrMoveTo(0x00FE, 0, 0, -10000, 58000, 0x00)
    PlayEffect(0x00, 0xFF, 0x00FF, 0, 0, 0, 270, 0, 0, 10000, 10000, 10000, 0x00FF, 0, 0, 0, 0)
    PlaySE(155, 0x00, 0x64)
    ChrMoveTo(0x00FE, 100000, 0, -10000, 58000, 0x00)

    Return()

# id: 0x0042 offset: 0x930D
@scena.Code('func_42_930D')
def func_42_930D():
    OP_72(0x0002, 0x0020)
    OP_B0(0x0002, 0x02)
    OP_6F(0x0002, 412)
    OP_70(0x0002, 416)

    @scena.Lambda('lambda_932A')
    def lambda_932A():
        OP_D1(0x00FE, 0, 90000, -20000, 2000)

        ExitThread()

    DispatchAsync(0x001E, 0x0003, lambda_932A)

    ChrMoveTo(0x00FE, -2000, 0, -14000, 58000, 0x00)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_7C(600, 0, 5000, 1000)
    CreateThread(0x00FE, 0x02, 0x00, func_43_9430)
    ChrMoveTo(0x00FE, 8000, 0, -14000, 20000, 0x00)
    PlaySE(155, 0x00, 0x64)
    OP_B0(0x0002, 0x0F)
    OP_6F(0x0002, 416)
    OP_70(0x0002, 427)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(6520, 3000, -5000, 0)
    OP_6C(72000, 0)

    @scena.Lambda('lambda_93CC')
    def lambda_93CC():
        OP_D1(0x00FE, 0, 90000, 30000, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_93CC)

    OP_98(0x00, 0x001E)
    OP_98(0x01, 150000, 4000, -5000)
    OP_98(0x01, 300000, 8000, 30000)

    @scena.Lambda('lambda_9406')
    def lambda_9406():
        OP_98(0x02, 0x00FE, 58000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_9406)

    OP_73(0x0002)
    PlaySE(346, 0x00, 0x64)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x14)
    OP_6F(0x0002, 320)
    OP_70(0x0002, 340)

    Return()

# id: 0x0043 offset: 0x9430
@scena.Code('func_43_9430')
def func_43_9430():
    PlayEffect(0x04, 0xFF, 0x00FF, -2000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0xFF, 0x00FF, 0, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0xFF, 0x00FF, 2000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0xFF, 0x00FF, 4000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0xFF, 0x00FF, 6000, 2000, -8000, 270, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0044 offset: 0x953A
@scena.Code('func_44_953A')
def func_44_953A():
    PlayEffect(0x02, 0x07, 0x000E, 3000, 0, 1000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x06, 0x000E, -3000, 0, 3000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x000E, 0, 0, 1000, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_95DF')
    def lambda_95DF():
        ChrMoveTo(0x00FE, 0, 4000, 10000, 80000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_95DF)

    OP_D1(0x00FE, 5000, 270000, -25000, 200)
    OP_D1(0x00FE, 0, 270000, -15000, 400)
    OP_D1(0x00FE, 5000, 270000, -20000, 600)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_9638')
    def lambda_9638():
        OP_D1(0x00FE, 10000, 270000, -25000, 8000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_9638)

    @scena.Lambda('lambda_9652')
    def lambda_9652():
        ChrMoveTo(0x00FE, -10000, -20000, 15000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_9652)

    Return()

# id: 0x0045 offset: 0x9668
@scena.Code('func_45_9668')
def func_45_9668():
    OP_D1(0x001E, 10000, 270000, 40000, 2000)

    @scena.Lambda('lambda_9681')
    def lambda_9681():
        OP_D1(0x00FE, 10000, 270000, -40000, 2000)

        ExitThread()

    DispatchAsync(0x001E, 0x0003, lambda_9681)

    OP_72(0x0002, 0x0020)
    OP_B0(0x0002, 0x0A)
    OP_6F(0x0002, 350)
    OP_70(0x0002, 370)
    OP_73(0x0002)
    OP_B0(0x0002, 0x05)
    OP_6F(0x0002, 370)
    OP_70(0x0002, 375)
    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_B0(0x0002, 0x14)
    OP_6F(0x0002, 320)
    OP_70(0x0002, 340)
    TerminateThread(0x001E, 0x03)
    OP_D1(0x001E, 0, 270000, 0, 1000)

    Return()

# id: 0x0046 offset: 0x96F3
@scena.Code('func_46_96F3')
def func_46_96F3():
    EventBegin(0x00)
    OP_DB()
    OP_E8(0x88, 0x13, 0x00, 0x00)
    LoadChip('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP', 10)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(-183060, 30000, 22680, 0)
    OP_67(0, -5630, -10000, 0)
    CameraSetDistance(6120, 0)
    OP_6C(325000, 0)
    OP_6E(343, 0)
    OP_71(0x0000, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_A1(0x0008, 0x0000)
    ChrSetPos(0x0008, -183080, -50000, -10000, 270)
    OP_A1(0x001D, 0x0001)
    ChrSetPos(0x001D, -183080, 15000, -10000, 270)
    PlaySE(275, 0x01, 0x5F)
    LoadEffect(0x02, 'map\\\\mp064_01.eff')
    LoadEffect(0x03, 'map\\\\mp065_01.eff')
    PlayEffect(0x02, 0x00, 0x001D, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x01, 0x001D, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x02, 0x001D, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x03, 0x001D, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x001D, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x05, 0x001D, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_B0(0x0001, 0x0A)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 281)
    OP_70(0x0001, 300)
    ChrSetPos(0x001C, 0, 0, 0, 315)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetChipByIndex(0x001C, 10)
    ChrSetSubChip(0x001C, 0)
    OP_CF(0x001C, 0x01, 'Frame85__ren')
    ChrSetDirection(0x001C, 315, 0)

    ExecExpressionWithValue(
        0x001C,
        0x24,
        (
            (Expr.PushLong, 0xA5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-183060, 30000, 22680, 0)
    OP_67(0, -5630, -10000, 0)
    CameraSetDistance(6120, 0)
    OP_6C(315000, 0)
    OP_6E(343, 0)

    @scena.Lambda('lambda_9999')
    def lambda_9999():
        OP_67(0, -2500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9999)

    @scena.Lambda('lambda_99B1')
    def lambda_99B1():
        OP_6C(0, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_99B1)

    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_99CB')
    def lambda_99CB():
        ChrMoveToRelative(0x00FE, 0, 45000, 150000, 32000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_99CB)

    CreateThread(0x001D, 0x03, 0x00, func_47_9A14)
    Sleep(3000)

    FadeOut(2000, 0, -1)
    OP_0D()
    WaitForThreadExit(0x001D, 0x0003)
    Sleep(1000)

    OP_E8(0xE8, 0x03, 0x00, 0x00)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5311._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0047 offset: 0x9A14
@scena.Code('func_47_9A14')
def func_47_9A14():
    OP_24(0x0113, 0x5A)
    Sleep(500)

    OP_24(0x0113, 0x55)
    Sleep(500)

    OP_24(0x0113, 0x50)
    Sleep(500)

    OP_24(0x0113, 0x4B)
    Sleep(500)

    OP_24(0x0113, 0x46)
    Sleep(500)

    OP_24(0x0113, 0x41)
    Sleep(500)

    OP_24(0x0113, 0x3C)
    Sleep(500)

    OP_24(0x0113, 0x37)
    Sleep(500)

    OP_24(0x0113, 0x32)
    Sleep(500)

    OP_24(0x0113, 0x28)
    Sleep(500)

    OP_24(0x0113, 0x1E)
    Sleep(500)

    OP_23(0x0113)

    Return()

# id: 0x0048 offset: 0x9A7B
@scena.Code('func_48_9A7B')
def func_48_9A7B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    LoadEffect(0x00, 'map\\mp077_00.eff')
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    LoadChip('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP', 10)
    LoadChip('ED6_DT27/CH03211._CH', 'ED6_DT27/CH03211P._CP', 11)
    LoadChip('ED6_DT26/CH20459._CH', 'ED6_DT26/CH20459P._CP', 12)
    LoadChip('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP', 13)
    LoadChip('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP', 14)
    LoadChip('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP', 15)
    LoadChip('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP', 16)
    LoadChip('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP', 17)
    LoadChip('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP', 18)
    LoadChip('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP', 19)
    LoadChip('ED6_DT27/CH03210._CH', 'ED6_DT27/CH03210P._CP', 20)
    LoadChip('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP', 21)
    LoadChip('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP', 22)
    LoadChip('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP', 23)
    LoadChip('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP', 24)
    LoadChip('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP', 25)
    LoadChip('ED6_DT26/CH20457._CH', 'ED6_DT26/CH20457P._CP', 26)
    LoadChip('ED6_DT26/CH20458._CH', 'ED6_DT26/CH20458P._CP', 27)
    LoadChip('ED6_DT26/CH20413._CH', 'ED6_DT26/CH20413P._CP', 28)
    LoadChip('ED6_DT26/CH20414._CH', 'ED6_DT26/CH20414P._CP', 29)
    ChrSetChipByIndex(0x001F, 26)
    ChrSetChipByIndex(0x0020, 27)
    ChrSetChipByIndex(0x0021, 12)
    ChrSetChipByIndex(0x0022, 13)
    ChrSetChipByIndex(0x0023, 14)
    ChrSetChipByIndex(0x0024, 15)
    ChrSetChipByIndex(0x0025, 16)
    ChrSetChipByIndex(0x0026, 17)
    ChrSetChipByIndex(0x0028, 18)
    ChrSetChipByIndex(0x0029, 19)
    ChrSetChipByIndex(0x002A, 20)
    ChrSetChipByIndex(0x0027, 21)
    ChrSetChipByIndex(0x002B, 22)
    ChrSetChipByIndex(0x002C, 23)
    ChrSetChipByIndex(0x002D, 24)
    ChrSetChipByIndex(0x002E, 25)
    CameraMove(190000, 32299, -15160, 0)
    OP_67(0, -520, -10000, 0)
    CameraSetDistance(1300, 0)
    OP_6C(360000, 0)
    OP_6E(750, 0)
    OP_D0(360000, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, -10, 0, 0, 0x00, 0x00)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetPos(0x0022, 200000, 32299, -15160, 270)
    ChrSetPos(0x0014, 197920, 33120, -15080, 0)
    PlaySE(451, 0x01, 0x64)
    OP_A1(0x000E, 0x0001)
    ChrClearFlags(0x000E, 0x0100)
    OP_D1(0x000E, 0, 270000, 0, 0)
    ChrSetPos(0x000E, 200000, 0, 0, 270)
    OP_71(0x0001, 0x0020)
    OP_6F(0x0001, 360)
    OP_70(0x0001, 460)
    OP_A1(0x000F, 0x0002)
    ChrClearFlags(0x000F, 0x0100)
    OP_D1(0x000F, 4000, 270000, 0, 0)
    ChrSetPos(0x000F, 200000, 30000, 0, 270)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 330)
    OP_70(0x0002, 430)
    OP_A1(0x000D, 0x0000)
    ChrClearFlags(0x000D, 0x0100)
    ChrSetPos(0x001F, 0, 0, 0, 0)
    ChrSetPos(0x0020, 0, 0, 0, 0)
    ChrSetPos(0x0021, 0, 0, 0, 0)
    OP_CF(0x001F, 0x00, 'Frame144_back_Null2')
    OP_CF(0x0020, 0x00, 'Frame145_back_Null3')
    OP_CF(0x0021, 0x00, 'Frame143_back_Null1')
    OP_71(0x0000, 0x0020)
    OP_71(0x0000, 0x0008)
    OP_6F(0x0000, 30)

    ExecExpressionWithValue(
        0x0021,
        0x24,
        (
            (Expr.PushLong, 0x9B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x24,
        (
            (Expr.PushLong, 0xA0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0020,
        0x24,
        (
            (Expr.PushLong, 0xA0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x0000000D, 0x07)
    OP_71(0x0001, 0x0004)
    OP_71(0x0000, 0x0004)
    PlaySE(293, 0x01, 0x46)
    FadeIn(2000, 0)
    OP_6A(0x0014)

    @scena.Lambda('lambda_9DAC')
    def lambda_9DAC():
        ChrMoveTo(0x00FE, -300000, 32299, -15160, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_9DAC)

    CreateThread(0x0014, 0x00, 0x00, func_5F_BD0E)
    CreateThread(0x0014, 0x03, 0x00, func_60_BED4)
    PlaySE(341, 0x01, 0x64)
    Sleep(5000)

    CreateThread(0x0021, 0x03, 0x00, func_63_BFF3)
    Sleep(13500)

    CreateThread(0x0022, 0x03, 0x00, func_62_BFA6)
    Sleep(1500)

    OP_6A(0x00FF)

    @scena.Lambda('lambda_9DFA')
    def lambda_9DFA():
        CameraMove(-202480, -120, -15440, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9DFA)

    @scena.Lambda('lambda_9E12')
    def lambda_9E12():
        OP_67(0, 2280, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9E12)

    @scena.Lambda('lambda_9E2A')
    def lambda_9E2A():
        CameraSetDistance(1900, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9E2A)

    @scena.Lambda('lambda_9E3A')
    def lambda_9E3A():
        OP_6C(702000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_9E3A)

    @scena.Lambda('lambda_9E4A')
    def lambda_9E4A():
        OP_D0(360000, 2000)

        ExitThread()

    DispatchAsync(0x0021, 0x0000, lambda_9E4A)

    WaitForThreadExit(0x0101, 0x0000)
    OP_72(0x0000, 0x0004)
    OP_71(0x0000, 0x0020)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 30)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0001)
    ChrClearFlags(0x001F, 0x0001)
    ChrClearFlags(0x0020, 0x0001)
    OP_23(0x0155)
    OP_23(0x0125)
    ChrSetPos(0x000D, -270000, -30000, -5080, 90)
    OP_D1(0x000D, -5000, 90000, 0, 0)

    @scena.Lambda('lambda_9EBF')
    def lambda_9EBF():
        ChrMoveTo(0x00FE, -90000, 30000, -5080, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_9EBF)

    Sleep(300)

    PlayBGM(118)
    Sleep(500)

    PlayEffect(0x00, 0xFF, 0x00FF, -200000, -5000, -15080, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -200000, -5000, -5080, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, -200000, -5000, -25080, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0102, 0x03, 0x00, func_64_C025)

    @scena.Lambda('lambda_9F8C')
    def lambda_9F8C():
        CameraMove(-200300, -5320, -13480, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9F8C)

    @scena.Lambda('lambda_9FA4')
    def lambda_9FA4():
        OP_67(0, -4420, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9FA4)

    @scena.Lambda('lambda_9FBC')
    def lambda_9FBC():
        OP_6C(785000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9FBC)

    Sleep(4000)

    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x0022, 0x01)
    ChrSetFlags(0x0022, 0x0080)
    CameraMove(21490, 30000, 11030, 0)
    OP_67(0, 4220, -10000, 0)
    CameraSetDistance(4480, 0)
    OP_6C(230000, 0)
    OP_6E(262, 0)

    ExecExpressionWithValue(
        0x0021,
        0x24,
        (
            (Expr.PushLong, 0xAF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x24,
        (
            (Expr.PushLong, 0xAF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0020,
        0x24,
        (
            (Expr.PushLong, 0xAF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_11(0xB8, 0xD8, 0xFF, 20000, 455000, 0)
    OP_76(0x00FF, 0x00000000, 0x0001, 2, 0, 0, 0x00, 0x00)
    ChrSetPos(0x000D, 0, 15000, 0, 90)
    OP_71(0x0000, 0x0020)
    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 30)
    Sleep(1000)

    FadeIn(2000, 0)

    @scena.Lambda('lambda_A0B0')
    def lambda_A0B0():
        CameraSetDistance(4000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A0B0)

    OP_6C(237000, 8000)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    CameraMove(-1420, 30000, 5980, 0)
    OP_67(0, 7720, -10000, 0)
    CameraSetDistance(2830, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x001F,
        (
            '#0010421170V#1004F#4P等、等等雷格纳特！\n',
            '你怎么会在这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421171V#1019F而且怎么\n',
            '连老爸也在这里啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0021, 0x0010)
    ChrSetFlags(0x0021, 0x0002)
    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 1)
    Sleep(300)

    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 8)
    Sleep(100)

    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 9)
    Sleep(500)

    ChrTalk(
        0x0021,
        (
            '#0160421172V#080F#5P这什么话，毕竟整个王国的\n',
            '导力都完全恢复了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160421173V#081F我就把剩下的事都推给了摩尔根将军，\n',
            '然后就让它搭我过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0010421174V#1007F#4P搭、搭你过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0020421175V#1054F#6P真是惊人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421176V#1053F……初次见面，雷格纳特。\n',
            '我从艾丝蒂尔那里听说了你的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020421177V#1040F危难之时得你相救，\n',
            '真是非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490421178V呵呵，不必向我道谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490421179V新时代的清风已经吹来……\n',
            '我只是出来活动活动翅膀而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x001F,
        (
            '#0010421180V#1016F#4P嘿嘿……\n',
            '不过还真是死里逃生啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421181V#1004F对了，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421182V#1015F我记得你只能\n',
            '在暗中观察人类吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010421183V这样帮助我们没问题么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490421184V那是你们在『辉之环』面前\n',
            '做出答复之前的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490421185V而现在答案既已出现，\n',
            '古代盟约也就随之解除，禁忌也消失了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490421186V所以我才应『剑圣』的请求，\n',
            '前来迎接你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0020,
        (
            '#0020421187V#1044F#6P古代的盟约……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0010421188V#1019F#4P真是越听越糊涂啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0021, 0x09, 0x0B, 2000)
    Sleep(100)

    CreateThread(0x0021, 0x00, 0x00, func_4A_B211)
    WaitForThreadExit(0x0021, 0x0000)

    ChrTalk(
        0x0021,
        (
            '#0160421189V#083F#5P不用看我，我也不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0021, 0x0000)
    OP_99(0x0021, 0x0D, 0x09, 1000)
    Fade(100)
    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 8)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0021,
        (
            '#0160421190V#080F#5P因为这个老顽固\n',
            '口风很紧，每次一提到关键问题\n',
            '时就开始遮遮掩掩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)
    TalkSetChrName('古龙雷格纳特')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3490421191V呵呵，别见怪。\n',
            '龙也有龙自己的规矩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490421192V不过有句话可以告诉你们……\n',
            '命运的齿轮，现在才\n',
            '刚刚开始转动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490421193V而且，齿轮一旦开始转动，\n',
            '不到最后绝不会停止……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3490421194V你们要牢记这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0021,
        (
            '#0160421195V#082F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0010421196V#1020F#4P等、等一等……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0020421197V#1042F#6P就是说利贝尔还会\n',
            '发生同样的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(100)
    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 9)
    OP_0D()
    OP_99(0x0021, 0x09, 0x0B, 1000)
    Sleep(500)

    ChrTalk(
        0x0021,
        (
            '#0160421198V#085F#5P不，这命运应该会\n',
            '降临到其他的地方，\n',
            '由其他的人来承担吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0021, 0x0B, 0x09, 1000)
    Sleep(500)

    ChrTalk(
        0x0021,
        (
            '#0160421199V#080F#5P──总之这次\n',
            '你们干得很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160421200V现在什么也不用想，\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160421201V和你们那些患难与共的好伙伴一起！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0010421202V#1008F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    CreateThread(0x0020, 0x03, 0x00, func_49_B1BC)
    OP_20(0x000003E8)
    OP_21()
    PlayBGM(8)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_72(0x0002, 0x0004)
    OP_D1(0x000F, 0, 270000, 0, 0)
    ChrSetPos(0x000F, 120000, 10000, 0, 270)
    Yield()
    ChrClearFlags(0x002B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x002A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0027, 0x0080)
    ChrClearFlags(0x0028, 0x0080)
    ChrClearFlags(0x0029, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x002D, 0x0080)
    ChrClearFlags(0x002C, 0x0080)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x002B, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrClearFlags(0x002A, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x0027, 0x0001)
    ChrClearFlags(0x0028, 0x0001)
    ChrClearFlags(0x0029, 0x0001)
    ChrClearFlags(0x0023, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x002D, 0x0001)
    ChrClearFlags(0x002C, 0x0001)
    ChrClearFlags(0x0024, 0x0001)
    ChrSetBattleFlags(0x002B, 0x0020)
    ChrSetBattleFlags(0x000C, 0x0020)
    ChrSetBattleFlags(0x002A, 0x0020)
    ChrSetBattleFlags(0x000B, 0x0020)
    ChrSetBattleFlags(0x0027, 0x0020)
    ChrSetBattleFlags(0x0028, 0x0020)
    ChrSetBattleFlags(0x0029, 0x0020)
    ChrSetBattleFlags(0x0023, 0x0020)
    ChrSetBattleFlags(0x0009, 0x0020)
    ChrSetBattleFlags(0x002D, 0x0020)
    ChrSetBattleFlags(0x002C, 0x0020)
    ChrSetBattleFlags(0x0024, 0x0020)
    ChrSetFlags(0x002B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x002A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0027, 0x0040)
    ChrSetFlags(0x0028, 0x0040)
    ChrSetFlags(0x0029, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x002D, 0x0040)
    ChrSetFlags(0x002C, 0x0040)
    ChrSetFlags(0x0023, 0x0040)
    ChrSetFlags(0x0024, 0x0040)
    OP_89(0x002B, 104080, 11860, 60, 270)
    OP_89(0x000C, 104670, 11950, 840, 270)
    OP_89(0x002A, 104430, 12360, -900, 270)
    OP_89(0x000B, 105220, 12330, 930, 270)
    OP_89(0x0027, 104890, 12270, -480, 270)
    OP_89(0x0028, 105150, 12350, -1520, 270)
    OP_89(0x0029, 106610, 11480, 1420, 270)
    OP_89(0x0009, 106600, 11650, 150, 270)
    OP_89(0x002D, 106770, 12050, -1460, 270)
    OP_89(0x002C, 107810, 11410, -220, 270)
    OP_89(0x0023, 107450, 11320, 910, 270)
    OP_89(0x0024, 107670, 12010, -1810, 270)
    ChrSetChipByIndex(0x002B, 10)
    ChrSetSubChip(0x002B, 0)
    ChrSetChipByIndex(0x002A, 11)
    ChrSetSubChip(0x002A, 0)
    ChrSetPos(0x000F, 220000, 10000, -30000, 270)
    OP_D1(0x000F, 0, 270000, 0, 0)

    @scena.Lambda('lambda_AB4D')
    def lambda_AB4D():
        ChrMoveTo(0x00FE, 0, 10000, -20000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_AB4D)

    PlaySE(293, 0x01, 0x14)

    @scena.Lambda('lambda_AB6D')
    def lambda_AB6D():
        CameraMove(51560, 15660, -17500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_AB6D)

    @scena.Lambda('lambda_AB85')
    def lambda_AB85():
        OP_67(0, 8200, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_AB85)

    @scena.Lambda('lambda_AB9D')
    def lambda_AB9D():
        OP_6C(102000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_AB9D)

    @scena.Lambda('lambda_ABAD')
    def lambda_ABAD():
        OP_6E(792, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_ABAD)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_ABC2')
    def lambda_ABC2():
        OP_67(0, 2200, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_ABC2)

    WaitForThreadExit(0x0101, 0x0001)
    OP_24(0x0125, 0x1E)
    Sleep(1000)

    OP_24(0x0125, 0x28)
    Sleep(1000)

    OP_24(0x0125, 0x32)
    Sleep(1000)

    TerminateThread(0x000F, 0x01)
    ChrSetPos(0x000F, -90000, 10000, -25000, 90)
    OP_D1(0x000F, 0, 90000, 0, 0)
    LoadEffect(0x01, 'map\\\\mp032_00.eff')
    Fade(1000)
    OP_71(0x0000, 0x0004)
    CameraMove(-74360, 12520, -24750, 0)
    OP_67(0, 6440, -10000, 0)
    CameraSetDistance(1870, 0)
    OP_6C(246000, 0)
    OP_6E(528, 0)
    ChrSetDirection(0x002B, 90, 0)
    ChrSetDirection(0x000C, 90, 0)
    ChrSetDirection(0x002A, 90, 0)
    ChrSetDirection(0x000B, 90, 0)
    ChrSetDirection(0x0027, 90, 0)
    ChrSetDirection(0x0028, 90, 0)
    ChrSetDirection(0x0029, 90, 0)
    ChrSetDirection(0x0023, 90, 0)
    ChrSetDirection(0x0009, 90, 0)
    ChrSetDirection(0x002D, 90, 0)
    ChrSetDirection(0x002C, 90, 0)
    ChrSetDirection(0x0024, 90, 0)
    CreateThread(0x002C, 0x00, 0x00, func_4D_B2B9)
    CreateThread(0x0009, 0x00, 0x00, func_4E_B365)
    CreateThread(0x0027, 0x00, 0x00, func_4F_B39E)
    CreateThread(0x0028, 0x00, 0x00, func_50_B404)
    CreateThread(0x000B, 0x00, 0x00, func_51_B474)
    CreateThread(0x0029, 0x00, 0x00, func_52_B58E)
    CreateThread(0x002A, 0x00, 0x00, func_53_B630)
    CreateThread(0x002B, 0x00, 0x00, func_54_B68C)
    CreateThread(0x002D, 0x00, 0x00, func_55_B838)
    CreateThread(0x000C, 0x00, 0x00, func_56_B880)
    CreateThread(0x0023, 0x00, 0x00, func_57_B9F6)
    CreateThread(0x0024, 0x00, 0x00, func_58_BA20)
    OP_24(0x0125, 0x3C)
    OP_0D()
    Sleep(1000)

    OP_24(0x0125, 0x46)

    @scena.Lambda('lambda_AD33')
    def lambda_AD33():
        CameraMove(-70360, 16370, -24750, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_AD33)

    @scena.Lambda('lambda_AD4B')
    def lambda_AD4B():
        OP_67(0, 3800, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_AD4B)

    @scena.Lambda('lambda_AD63')
    def lambda_AD63():
        OP_6C(206000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_AD63)

    OP_72(0x0001, 0x0004)
    OP_D1(0x000E, 0, 90000, 10000, 0)
    ChrSetPos(0x000E, -120000, 5000, -50000, 90)
    ChrSetBattleFlags(0x002E, 0x0020)
    ChrSetBattleFlags(0x0025, 0x0020)
    ChrSetBattleFlags(0x0026, 0x0020)
    Yield()
    ChrClearFlags(0x002E, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrClearFlags(0x002E, 0x0001)
    ChrClearFlags(0x0025, 0x0001)
    ChrClearFlags(0x0026, 0x0001)
    OP_89(0x002E, -119350, 11040, -46600, 75)
    OP_89(0x0025, -120480, 11010, -46460, 75)
    OP_89(0x0026, -116240, 15200, -48160, 75)
    OP_E5(0x2E, 0x00, 0x00)
    OP_E5(0x25, 0x00, 0x00)
    OP_E5(0x26, 0x00, 0x00)
    ChrSetFlags(0x002E, 0x0002)
    ChrSetFlags(0x0025, 0x0002)
    ChrSetChipByIndex(0x002E, 29)
    ChrSetSubChip(0x002E, 24)
    ChrSetChipByIndex(0x0025, 29)
    ChrSetSubChip(0x0025, 48)
    CreateThread(0x002E, 0x00, 0x00, func_59_BA3B)
    CreateThread(0x0025, 0x00, 0x00, func_5A_BB3D)
    ChrSetRGBAMask(0x0026, 255, 255, 255, 0, 0)
    PlaySE(121, 0x01, 0x32)

    @scena.Lambda('lambda_AE45')
    def lambda_AE45():
        ChrMoveTo(0x00FE, -80000, 5000, -50000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_AE45)

    Sleep(4200)

    @scena.Lambda('lambda_AE65')
    def lambda_AE65():
        ChrMoveTo(0x00FE, -80000, 5000, -50000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_AE65)

    Sleep(200)

    @scena.Lambda('lambda_AE85')
    def lambda_AE85():
        ChrMoveTo(0x00FE, -80000, 5000, -50000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_AE85)

    Sleep(200)

    @scena.Lambda('lambda_AEA5')
    def lambda_AEA5():
        ChrMoveTo(0x00FE, -80000, 5000, -50000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_AEA5)

    Sleep(200)

    @scena.Lambda('lambda_AEC5')
    def lambda_AEC5():
        ChrMoveTo(0x00FE, -80000, 5000, -50000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_AEC5)

    Sleep(200)

    @scena.Lambda('lambda_AEE5')
    def lambda_AEE5():
        ChrMoveTo(0x00FE, -80000, 5000, -50000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_AEE5)

    Sleep(200)

    @scena.Lambda('lambda_AF05')
    def lambda_AF05():
        ChrMoveTo(0x00FE, -80000, 5000, -50000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_AF05)

    Sleep(200)

    @scena.Lambda('lambda_AF25')
    def lambda_AF25():
        ChrMoveTo(0x00FE, -80000, 5000, -50000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_AF25)

    OP_72(0x0001, 0x0020)
    CreateThread(0x0026, 0x00, 0x00, func_61_BF87)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0026, 0x0000)
    Sleep(2000)

    Fade(500)
    TerminateThread(0x002B, 0x00)
    TerminateThread(0x000C, 0x00)
    TerminateThread(0x002E, 0x00)
    ChrSetPos(0x000E, 100000, 0, 0, 90)
    ChrSetPos(0x000F, 100000, 0, -20000, 90)
    OP_72(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    ChrSetFlags(0x001F, 0x0010)
    ChrSetFlags(0x001F, 0x0002)
    ChrSetChipByIndex(0x001F, 26)
    ChrSetSubChip(0x001F, 5)
    ChrSetFlags(0x0020, 0x0010)
    ChrSetFlags(0x0020, 0x0002)
    ChrSetChipByIndex(0x0020, 27)
    ChrSetSubChip(0x0020, 5)
    ChrClearFlags(0x0021, 0x0002)
    ChrSetSubChip(0x0021, 0)
    ChrSetDirection(0x0021, 0, 0)
    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 30)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    CreateThread(0x0102, 0x03, 0x00, func_65_C09B)
    CameraMove(6010, 29000, -1560, 0)
    OP_67(0, 7440, -10000, 0)
    CameraSetDistance(650, 0)
    OP_6C(297000, 0)
    OP_6E(750, 0)
    OP_24(0x0125, 0x14)
    OP_24(0x0079, 0x14)
    OP_0D()
    Sleep(600)

    ChrSetChipByIndex(0x001F, 26)
    ChrSetSubChip(0x001F, 8)
    Sleep(100)

    ChrSetChipByIndex(0x001F, 26)
    ChrSetSubChip(0x001F, 9)
    Sleep(200)

    ChrSetChipByIndex(0x0020, 27)
    ChrSetSubChip(0x0020, 8)
    Sleep(100)

    ChrSetChipByIndex(0x0020, 27)
    ChrSetSubChip(0x0020, 9)
    Sleep(600)

    ChrSetChipByIndex(0x001F, 26)
    ChrSetSubChip(0x001F, 10)
    ChrSetChipByIndex(0x0020, 27)
    ChrSetSubChip(0x0020, 10)
    Sleep(150)

    ChrSetChipByIndex(0x001F, 26)
    ChrSetSubChip(0x001F, 11)
    ChrSetChipByIndex(0x0020, 27)
    ChrSetSubChip(0x0020, 11)
    Sleep(150)

    ChrSetChipByIndex(0x001F, 26)
    ChrSetSubChip(0x001F, 10)
    ChrSetChipByIndex(0x0020, 27)
    ChrSetSubChip(0x0020, 10)
    Sleep(150)

    ChrSetChipByIndex(0x001F, 26)
    ChrSetSubChip(0x001F, 9)
    ChrSetChipByIndex(0x0020, 27)
    ChrSetSubChip(0x0020, 9)
    Sleep(1000)

    Fade(100)
    CreateThread(0x001F, 0x00, 0x00, func_4B_B26C)
    Sleep(50)

    CreateThread(0x0020, 0x00, 0x00, func_4C_B2A3)
    OP_0D()

    @scena.Lambda('lambda_B0F6')
    def lambda_B0F6():
        OP_6E(600, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B0F6)

    Sleep(4500)

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_24(0x01C3, 0x5A)
    Sleep(200)

    OP_24(0x01C3, 0x50)
    Sleep(200)

    OP_24(0x01C3, 0x46)
    Sleep(200)

    OP_24(0x01C3, 0x3C)
    Sleep(200)

    OP_24(0x01C3, 0x32)
    Sleep(200)

    OP_24(0x01C3, 0x28)
    Sleep(200)

    OP_24(0x01C3, 0x1E)
    Sleep(200)

    OP_24(0x01C3, 0x14)
    Sleep(200)

    OP_24(0x01C3, 0x0A)
    Sleep(200)

    OP_23(0x01C3)
    OP_23(0x0125)
    OP_23(0x0079)
    OP_C4(0x00, 0x00000010)
    Yield()
    FadeIn(1, 0)
    UnlockAchievement(0x16, 0x0000, 0x00)
    PlayMovie(0x00, 'ED6_DT47.dat', 0x0008, 0x0000)
    OP_21()
    FadeOut(1000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    OP_C4(0x01, 0x00000010)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T5200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0049 offset: 0xB1BC
@scena.Code('func_49_B1BC')
def func_49_B1BC():
    OP_24(0x01C3, 0x5A)
    Sleep(300)

    OP_24(0x01C3, 0x50)
    Sleep(300)

    OP_24(0x01C3, 0x46)
    Sleep(300)

    OP_24(0x01C3, 0x3C)
    Sleep(300)

    OP_24(0x01C3, 0x32)
    Sleep(300)

    OP_24(0x01C3, 0x28)
    Sleep(300)

    OP_24(0x01C3, 0x1E)
    Sleep(300)

    OP_24(0x01C3, 0x14)
    Sleep(300)

    OP_24(0x01C3, 0x0A)
    Sleep(300)

    OP_23(0x01C3)

    Return()

# id: 0x004A offset: 0xB211
@scena.Code('func_4A_B211')
def func_4A_B211():
    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 12)
    Sleep(200)

    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 13)
    Sleep(200)

    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 14)
    Sleep(300)

    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 13)
    Sleep(80)

    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 15)
    Sleep(300)

    ChrSetChipByIndex(0x0021, 12)
    ChrSetSubChip(0x0021, 13)
    Sleep(200)

    Return()

# id: 0x004B offset: 0xB26C
@scena.Code('func_4B_B26C')
def func_4B_B26C():
    OP_99(0x00FE, 0x10, 0x11, 1500)
    OP_99(0x00FE, 0x0D, 0x0F, 1500)
    Sleep(50)

    ChrSetSubChip(0x00FE, 21)
    Sleep(50)

    def _loc_B28D(): pass

    label('loc_B28D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B2A2',
    )

    OP_99(0x00FE, 0x10, 0x15, 1500)

    Jump('loc_B28D')

    def _loc_B2A2(): pass

    label('loc_B2A2')

    Return()

# id: 0x004C offset: 0xB2A3
@scena.Code('func_4C_B2A3')
def func_4C_B2A3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B2B8',
    )

    OP_99(0x00FE, 0x10, 0x15, 1500)

    Jump('func_4C_B2A3')

    def _loc_B2B8(): pass

    label('loc_B2B8')

    Return()

# id: 0x004D offset: 0xB2B9
@scena.Code('func_4D_B2B9')
def func_4D_B2B9():
    Yield()
    Sleep(400)

    ChrMoveToRelativeAsync(0x00FE, 2100, 0, 0, 450, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 56)
    Sleep(2000)

    ChrSetSubChip(0x00FE, 56)
    Sleep(100)

    ChrSetSubChip(0x00FE, 57)
    Sleep(100)

    ChrSetSubChip(0x00FE, 58)
    Sleep(150)

    ChrSetSubChip(0x00FE, 59)
    Sleep(150)

    ChrSetSubChip(0x00FE, 60)
    Sleep(200)

    ChrSetSubChip(0x00FE, 59)
    Sleep(150)

    ChrSetSubChip(0x00FE, 58)
    Sleep(150)

    ChrSetSubChip(0x00FE, 59)
    Sleep(150)

    ChrSetSubChip(0x00FE, 60)
    Sleep(200)

    ChrSetSubChip(0x00FE, 59)
    Sleep(150)

    ChrSetSubChip(0x00FE, 58)
    Sleep(100)

    ChrSetSubChip(0x00FE, 57)
    Sleep(100)

    ChrSetSubChip(0x00FE, 56)

    Return()

# id: 0x004E offset: 0xB365
@scena.Code('func_4E_B365')
def func_4E_B365():
    Yield()
    Sleep(250)

    ChrMoveToRelativeAsync(0x00FE, 2300, 0, 0, 700, 0x00)
    Sleep(1500)

    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 32)
    Sleep(100)

    ChrSetSubChip(0x00FE, 33)

    Return()

# id: 0x004F offset: 0xB39E
@scena.Code('func_4F_B39E')
def func_4F_B39E():
    Yield()
    Sleep(350)

    ChrMoveToRelativeAsync(0x00FE, 2600, 0, 0, 600, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 8)
    Sleep(1000)

    ChrSetSubChip(0x00FE, 9)
    Sleep(100)

    ChrSetSubChip(0x00FE, 10)
    Sleep(1000)

    ChrSetSubChip(0x00FE, 9)
    Sleep(100)

    ChrSetSubChip(0x00FE, 8)
    Sleep(1000)

    ChrSetSubChip(0x00FE, 11)
    Sleep(200)

    ChrSetSubChip(0x00FE, 12)

    Return()

# id: 0x0050 offset: 0xB404
@scena.Code('func_50_B404')
def func_50_B404():
    Yield()
    Sleep(300)

    ChrMoveToRelativeAsync(0x00FE, 2600, 0, 0, 650, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 6)
    Sleep(500)

    ChrSetSubChip(0x00FE, 6)
    Sleep(150)

    ChrSetSubChip(0x00FE, 5)
    Sleep(150)

    ChrSetSubChip(0x00FE, 4)
    Sleep(150)

    ChrSetSubChip(0x00FE, 3)
    Sleep(150)

    ChrSetSubChip(0x00FE, 2)
    Sleep(150)

    ChrSetSubChip(0x00FE, 1)
    Sleep(150)

    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0051 offset: 0xB474
@scena.Code('func_51_B474')
def func_51_B474():
    Yield()
    Sleep(200)

    ChrMoveToRelativeAsync(0x00FE, 2500, 0, 0, 750, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 13)
    Sleep(1000)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 15)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 13)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 15)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 13)
    Sleep(1000)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 15)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 13)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 15)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 13)
    Sleep(1000)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 15)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 13)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 15)
    Sleep(150)

    ChrSetSubChip(0x00FE, 14)
    Sleep(150)

    ChrSetSubChip(0x00FE, 13)

    Return()

# id: 0x0052 offset: 0xB58E
@scena.Code('func_52_B58E')
def func_52_B58E():
    Yield()
    Sleep(300)

    ChrMoveToRelativeAsync(0x00FE, 2300, 0, 0, 500, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 16)
    Sleep(1000)

    ChrSetSubChip(0x00FE, 17)
    Sleep(200)

    ChrSetSubChip(0x00FE, 18)
    Sleep(200)

    ChrSetSubChip(0x00FE, 19)
    Sleep(200)

    ChrSetSubChip(0x00FE, 20)
    Sleep(200)

    ChrSetSubChip(0x00FE, 21)
    Sleep(200)

    ChrSetSubChip(0x00FE, 22)
    Sleep(1500)

    ChrSetSubChip(0x00FE, 21)
    Sleep(200)

    ChrSetSubChip(0x00FE, 20)
    Sleep(200)

    ChrSetSubChip(0x00FE, 19)
    Sleep(200)

    ChrSetSubChip(0x00FE, 18)
    Sleep(200)

    ChrSetSubChip(0x00FE, 17)
    Sleep(200)

    ChrSetSubChip(0x00FE, 16)

    Return()

# id: 0x0053 offset: 0xB630
@scena.Code('func_53_B630')
def func_53_B630():
    Yield()
    Sleep(200)

    ChrMoveToRelativeAsync(0x00FE, 3000, 0, 0, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetSubChip(0x00FE, 37)
    ChrSetChipByIndex(0x00FE, 29)
    Sleep(2000)

    ChrSetSubChip(0x00FE, 37)
    Sleep(100)

    ChrSetSubChip(0x00FE, 38)
    Sleep(100)

    ChrSetSubChip(0x00FE, 39)
    Sleep(2000)

    ChrSetSubChip(0x00FE, 38)
    Sleep(100)

    ChrSetSubChip(0x00FE, 37)

    Return()

# id: 0x0054 offset: 0xB68C
@scena.Code('func_54_B68C')
def func_54_B68C():
    Yield()
    ChrMoveToRelativeAsync(0x00FE, 3000, 0, 0, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 28)
    ChrSetSubChip(0x00FE, 0)
    Sleep(150)

    ChrSetSubChip(0x00FE, 1)
    Sleep(150)

    ChrSetSubChip(0x00FE, 2)
    Sleep(150)

    ChrSetSubChip(0x00FE, 3)
    Sleep(150)

    ChrSetSubChip(0x00FE, 4)
    Sleep(150)

    ChrSetSubChip(0x00FE, 5)
    Sleep(150)

    ChrSetSubChip(0x00FE, 0)
    Sleep(150)

    ChrSetSubChip(0x00FE, 1)
    Sleep(150)

    ChrSetSubChip(0x00FE, 2)
    Sleep(150)

    ChrSetSubChip(0x00FE, 3)
    Sleep(150)

    ChrSetSubChip(0x00FE, 4)
    Sleep(150)

    ChrSetSubChip(0x00FE, 5)
    Sleep(150)

    ChrSetSubChip(0x00FE, 0)
    Sleep(150)

    ChrSetSubChip(0x00FE, 1)
    Sleep(150)

    ChrSetSubChip(0x00FE, 2)
    Sleep(150)

    ChrSetSubChip(0x00FE, 3)
    Sleep(150)

    ChrSetSubChip(0x00FE, 4)
    Sleep(150)

    ChrSetSubChip(0x00FE, 5)
    Sleep(150)

    ChrSetSubChip(0x00FE, 0)
    Sleep(150)

    ChrSetSubChip(0x00FE, 1)
    Sleep(150)

    ChrSetSubChip(0x00FE, 2)
    Sleep(150)

    ChrSetSubChip(0x00FE, 3)
    Sleep(150)

    ChrSetSubChip(0x00FE, 4)
    Sleep(150)

    ChrSetSubChip(0x00FE, 5)
    Sleep(150)

    ChrSetSubChip(0x00FE, 8)
    Sleep(200)

    ChrSetSubChip(0x00FE, 9)
    Sleep(300)

    ChrSetSubChip(0x00FE, 6)
    Sleep(400)

    ChrSetSubChip(0x00FE, 7)
    Sleep(500)

    OP_9E(0x00FE, 8, 0, 500, 3000)
    Sleep(500)

    ChrSetSubChip(0x00FE, 15)
    Sleep(300)

    ChrSetSubChip(0x00FE, 13)
    Sleep(150)

    def _loc_B7EF(): pass

    label('loc_B7EF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B837',
    )

    ChrSetSubChip(0x00FE, 8)
    Sleep(150)

    ChrSetSubChip(0x00FE, 9)
    Sleep(150)

    ChrSetSubChip(0x00FE, 10)
    Sleep(150)

    ChrSetSubChip(0x00FE, 11)
    Sleep(150)

    ChrSetSubChip(0x00FE, 12)
    Sleep(150)

    ChrSetSubChip(0x00FE, 13)
    Sleep(150)

    Jump('loc_B7EF')

    def _loc_B837(): pass

    label('loc_B837')

    Return()

# id: 0x0055 offset: 0xB838
@scena.Code('func_55_B838')
def func_55_B838():
    Yield()
    Sleep(350)

    ChrMoveToRelativeAsync(0x00FE, 2300, 0, 0, 550, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 30)
    Sleep(500)

    ChrSetSubChip(0x00FE, 30)
    Sleep(150)

    ChrSetSubChip(0x00FE, 31)
    Sleep(150)

    ChrSetSubChip(0x00FE, 23)

    Return()

# id: 0x0056 offset: 0xB880
@scena.Code('func_56_B880')
def func_56_B880():
    Yield()
    Sleep(250)

    ChrMoveToRelativeAsync(0x00FE, 3000, 0, 0, 1100, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 46)
    Sleep(500)

    def _loc_B8AE(): pass

    label('loc_B8AE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B9F5',
    )

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x000C, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x000C, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x000C, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x000C, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x000C, 0, 1400, 600, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    Jump('loc_B8AE')

    def _loc_B9F5(): pass

    label('loc_B9F5')

    Return()

# id: 0x0057 offset: 0xB9F6
@scena.Code('func_57_B9F6')
def func_57_B9F6():
    Yield()
    Sleep(450)

    ChrMoveToRelativeAsync(0x00FE, 2100, 0, 0, 400, 0x00)
    ChrSetFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 29)
    ChrSetSubChip(0x00FE, 7)

    Return()

# id: 0x0058 offset: 0xBA20
@scena.Code('func_58_BA20')
def func_58_BA20():
    Yield()
    Sleep(450)

    ChrMoveToRelativeAsync(0x00FE, 2100, 0, 0, 400, 0x00)

    Return()

# id: 0x0059 offset: 0xBA3B
@scena.Code('func_59_BA3B')
def func_59_BA3B():
    Sleep(2500)

    ChrSetSubChip(0x00FE, 24)
    Sleep(150)

    ChrSetSubChip(0x00FE, 25)
    Sleep(150)

    ChrSetSubChip(0x00FE, 26)
    Sleep(150)

    ChrSetSubChip(0x00FE, 27)
    Sleep(150)

    ChrSetSubChip(0x00FE, 28)
    Sleep(150)

    ChrSetSubChip(0x00FE, 29)
    Sleep(150)

    ChrSetSubChip(0x00FE, 24)
    Sleep(150)

    ChrSetSubChip(0x00FE, 25)
    Sleep(150)

    ChrSetSubChip(0x00FE, 26)
    Sleep(150)

    ChrSetSubChip(0x00FE, 27)
    Sleep(150)

    ChrSetSubChip(0x00FE, 28)
    Sleep(150)

    ChrSetSubChip(0x00FE, 29)
    Sleep(150)

    ChrSetSubChip(0x00FE, 24)
    Sleep(150)

    ChrSetSubChip(0x00FE, 25)
    Sleep(150)

    ChrSetSubChip(0x00FE, 34)
    Sleep(150)

    ChrSetSubChip(0x00FE, 35)
    Sleep(150)

    ChrSetSubChip(0x00FE, 36)
    Sleep(150)

    ChrSetSubChip(0x00FE, 29)
    Sleep(150)

    def _loc_BAF4(): pass

    label('loc_BAF4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BB3C',
    )

    ChrSetSubChip(0x00FE, 24)
    Sleep(150)

    ChrSetSubChip(0x00FE, 25)
    Sleep(150)

    ChrSetSubChip(0x00FE, 26)
    Sleep(150)

    ChrSetSubChip(0x00FE, 27)
    Sleep(150)

    ChrSetSubChip(0x00FE, 28)
    Sleep(150)

    ChrSetSubChip(0x00FE, 29)
    Sleep(150)

    Jump('loc_BAF4')

    def _loc_BB3C(): pass

    label('loc_BB3C')

    Return()

# id: 0x005A offset: 0xBB3D
@scena.Code('func_5A_BB3D')
def func_5A_BB3D():
    Sleep(2500)

    ChrSetSubChip(0x00FE, 44)
    Sleep(150)

    ChrSetSubChip(0x00FE, 42)
    Sleep(150)

    ChrSetSubChip(0x00FE, 43)
    Sleep(150)

    ChrSetSubChip(0x00FE, 42)
    Sleep(150)

    ChrSetSubChip(0x00FE, 44)
    Sleep(150)

    ChrSetSubChip(0x00FE, 41)
    Sleep(150)

    ChrSetSubChip(0x00FE, 40)
    Sleep(150)

    ChrSetSubChip(0x00FE, 41)
    Sleep(150)

    ChrSetSubChip(0x00FE, 44)
    Sleep(150)

    ChrSetSubChip(0x00FE, 42)
    Sleep(150)

    ChrSetSubChip(0x00FE, 43)
    Sleep(150)

    ChrSetSubChip(0x00FE, 42)
    Sleep(150)

    ChrSetSubChip(0x00FE, 44)
    Sleep(150)

    ChrSetSubChip(0x00FE, 45)
    Sleep(150)

    ChrSetSubChip(0x00FE, 48)

    Return()

# id: 0x005B offset: 0xBBD4
@scena.Code('func_5B_BBD4')
def func_5B_BBD4():
    ChrMoveTo(0x00FE, 47150, 30000, -7190, 8000, 0x00)
    ChrMoveTo(0x00FE, -6420, 16219, -23160, 12000, 0x00)
    ChrMoveTo(0x00FE, -80000, 3000, 0, 4000, 0x00)

    Return()

# id: 0x005C offset: 0xBC11
@scena.Code('func_5C_BC11')
def func_5C_BC11():
    @scena.Lambda('lambda_BC17')
    def lambda_BC17():
        ChrSetDirection(0x00FE, 90, 200)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_BC17)

    ChrMoveTo(0x00FE, 160000, 150000, 0, 8000, 0x00)

    Return()

# id: 0x005D offset: 0xBC34
@scena.Code('func_5D_BC34')
def func_5D_BC34():
    OP_98(0x00, 0x0022)
    OP_98(0x01, -40000, 34000, -15160)
    OP_98(0x01, -60000, 38000, 20000)
    OP_98(0x01, -120000, 20000, 20000)

    @scena.Lambda('lambda_BC68')
    def lambda_BC68():
        OP_98(0x02, 0x00FE, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_BC68)

    Return()

# id: 0x005E offset: 0xBC73
@scena.Code('func_5E_BC73')
def func_5E_BC73():
    @scena.Lambda('lambda_BC79')
    def lambda_BC79():
        CameraMove(-28420, 33660, -15760, 3400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_BC79)

    @scena.Lambda('lambda_BC91')
    def lambda_BC91():
        OP_67(0, -2320, -10000, 3400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BC91)

    @scena.Lambda('lambda_BCA9')
    def lambda_BCA9():
        OP_6C(312000, 3400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_BCA9)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_BCBE')
    def lambda_BCBE():
        CameraMove(-16840, 34860, 10260, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_BCBE)

    @scena.Lambda('lambda_BCD6')
    def lambda_BCD6():
        OP_67(0, 1060, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BCD6)

    @scena.Lambda('lambda_BCEE')
    def lambda_BCEE():
        OP_6C(270000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_BCEE)

    @scena.Lambda('lambda_BCFE')
    def lambda_BCFE():
        OP_D0(10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_BCFE)

    WaitForThreadExit(0x0101, 0x0001)

    Return()

# id: 0x005F offset: 0xBD0E
@scena.Code('func_5F_BD0E')
def func_5F_BD0E():
    @scena.Lambda('lambda_BD14')
    def lambda_BD14():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BD14)

    Sleep(1000)

    Sleep(1000)

    OP_24(0x0079, 0x5A)
    Sleep(1000)

    Sleep(1000)

    OP_24(0x0079, 0x50)
    Sleep(1000)

    Sleep(1000)

    OP_24(0x0079, 0x46)
    Sleep(1000)

    Sleep(1000)

    OP_24(0x0079, 0x3C)
    Sleep(1000)

    Sleep(1000)

    OP_24(0x0079, 0x32)
    Sleep(1000)

    Sleep(1000)

    OP_24(0x0079, 0x28)
    Sleep(1000)

    Sleep(1000)

    OP_24(0x0079, 0x1E)
    Sleep(1000)

    @scena.Lambda('lambda_BD96')
    def lambda_BD96():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 19800, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BD96)

    Sleep(400)

    @scena.Lambda('lambda_BDB6')
    def lambda_BDB6():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 19400, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BDB6)

    Sleep(400)

    OP_24(0x0079, 0x14)

    @scena.Lambda('lambda_BDDA')
    def lambda_BDDA():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 19000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BDDA)

    Sleep(400)

    @scena.Lambda('lambda_BDFA')
    def lambda_BDFA():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 18600, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BDFA)

    Sleep(400)

    @scena.Lambda('lambda_BE1A')
    def lambda_BE1A():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 18200, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BE1A)

    Sleep(400)

    @scena.Lambda('lambda_BE3A')
    def lambda_BE3A():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 17600, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BE3A)

    Sleep(400)

    OP_24(0x0079, 0x0A)

    @scena.Lambda('lambda_BE5E')
    def lambda_BE5E():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 17000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BE5E)

    Sleep(400)

    @scena.Lambda('lambda_BE7E')
    def lambda_BE7E():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 16200, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BE7E)

    Sleep(400)

    @scena.Lambda('lambda_BE9E')
    def lambda_BE9E():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 15600, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BE9E)

    Sleep(400)

    @scena.Lambda('lambda_BEBE')
    def lambda_BEBE():
        ChrMoveTo(0x00FE, -200000, 33120, -15080, 14600, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_BEBE)

    Return()

# id: 0x0060 offset: 0xBED4
@scena.Code('func_60_BED4')
def func_60_BED4():
    @scena.Lambda('lambda_BEDA')
    def lambda_BEDA():
        OP_6C(680000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_BEDA)

    @scena.Lambda('lambda_BEEA')
    def lambda_BEEA():
        OP_67(0, 3080, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BEEA)

    @scena.Lambda('lambda_BF02')
    def lambda_BF02():
        CameraSetDistance(720, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_BF02)

    @scena.Lambda('lambda_BF12')
    def lambda_BF12():
        OP_D0(355000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_BF12)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_BF27')
    def lambda_BF27():
        OP_67(0, 5580, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BF27)

    @scena.Lambda('lambda_BF3F')
    def lambda_BF3F():
        CameraSetDistance(1640, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_BF3F)

    @scena.Lambda('lambda_BF4F')
    def lambda_BF4F():
        OP_D0(370000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_BF4F)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_BF64')
    def lambda_BF64():
        OP_67(0, 8820, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BF64)

    @scena.Lambda('lambda_BF7C')
    def lambda_BF7C():
        CameraSetDistance(720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_BF7C)

    Return()

# id: 0x0061 offset: 0xBF87
@scena.Code('func_61_BF87')
def func_61_BF87():
    OP_6F(0x0001, 61)
    OP_70(0x0001, 95)
    Sleep(500)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

    Return()

# id: 0x0062 offset: 0xBFA6
@scena.Code('func_62_BFA6')
def func_62_BFA6():
    OP_24(0x0155, 0x5A)
    Sleep(300)

    OP_24(0x0155, 0x50)
    Sleep(300)

    OP_24(0x0155, 0x46)
    Sleep(300)

    OP_24(0x0155, 0x3C)
    Sleep(300)

    OP_24(0x0155, 0x32)
    Sleep(300)

    OP_24(0x0155, 0x28)
    Sleep(300)

    OP_24(0x0155, 0x1E)
    Sleep(300)

    OP_24(0x0155, 0x14)
    Sleep(300)

    OP_24(0x0155, 0x0A)

    Return()

# id: 0x0063 offset: 0xBFF3
@scena.Code('func_63_BFF3')
def func_63_BFF3():
    OP_24(0x0125, 0x3C)
    Sleep(500)

    OP_24(0x0125, 0x32)
    Sleep(500)

    OP_24(0x0125, 0x28)
    Sleep(500)

    OP_24(0x0125, 0x1E)
    Sleep(500)

    OP_24(0x0125, 0x14)
    Sleep(500)

    OP_24(0x0125, 0x0A)

    Return()

# id: 0x0064 offset: 0xC025
@scena.Code('func_64_C025')
def func_64_C025():
    Sleep(800)

    PlaySE(288, 0x00, 0x50)
    Sleep(1300)

    PlaySE(288, 0x00, 0x5A)
    Sleep(1300)

    PlaySE(288, 0x00, 0x5A)
    Sleep(1300)

    PlaySE(288, 0x00, 0x5A)
    Sleep(2400)

    def _loc_C052(): pass

    label('loc_C052')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C072',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_C065',
    )

    Jump('loc_C072')

    def _loc_C065(): pass

    label('loc_C065')

    PlaySE(288, 0x00, 0x5A)
    Sleep(2000)

    Jump('loc_C052')

    def _loc_C072(): pass

    label('loc_C072')

    PlaySE(288, 0x00, 0x55)
    Sleep(2000)

    PlaySE(288, 0x00, 0x41)
    Sleep(2000)

    PlaySE(288, 0x00, 0x2D)
    Sleep(2000)

    PlaySE(288, 0x00, 0x19)
    Sleep(2000)

    Return()

# id: 0x0065 offset: 0xC09B
@scena.Code('func_65_C09B')
def func_65_C09B():
    Sleep(1100)

    def _loc_C0A0(): pass

    label('loc_C0A0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C0C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_C0B3',
    )

    Jump('loc_C0C0')

    def _loc_C0B3(): pass

    label('loc_C0B3')

    PlaySE(288, 0x00, 0x50)
    Sleep(2000)

    Jump('loc_C0A0')

    def _loc_C0C0(): pass

    label('loc_C0C0')

    PlaySE(288, 0x00, 0x46)
    Sleep(2000)

    PlaySE(288, 0x00, 0x3C)
    Sleep(2000)

    PlaySE(288, 0x00, 0x28)
    Sleep(2000)

    PlaySE(288, 0x00, 0x14)
    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
