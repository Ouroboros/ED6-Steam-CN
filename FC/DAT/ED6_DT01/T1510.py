import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1510_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1510   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1510.x'
    header.mapIndex       = 1
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
            word_30         = 225,
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
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01623._CH', 'ED6_DT07/CH01623P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20049._CH', 'ED6_DT06/CH20049P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雷纳德',
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '索菲娜',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '罗伊德',
            x                   = 13000,
            z                   = 0,
            y                   = 7500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '艾露凯',
            x                   = 13700,
            z                   = 150,
            y                   = 6400,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '阿妮特',
            x                   = 15930,
            z                   = 250,
            y                   = 6290,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '斯丁克',
            x                   = 23980,
            z                   = 300,
            y                   = 9640,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 17080,
            z                   = 0,
            y                   = 13470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 16100,
            z                   = 200,
            y                   = 6240,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 13450,
            z                   = 200,
            y                   = 6320,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 15250,
            z                   = 700,
            y                   = 6400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327690,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 14160,
            z                   = 700,
            y                   = 6050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327690,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 14790,
            z                   = 800,
            y                   = 6500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835017,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 14450,
            z                   = 800,
            y                   = 6650,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835017,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 15000,
            z                   = 0,
            y                   = 5500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835017,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 14600,
            z                   = 0,
            y                   = 5500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835017,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 14200,
            z                   = 0,
            y                   = 5500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835017,
            chipIndex           = 9,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x31A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x31A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x31A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 23100,
            triggerZ            = 0,
            triggerY            = 6000,
            triggerRange        = 700,
            actorX              = 24500,
            actorZ              = 1500,
            actorY              = 6100,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 80610,
            triggerZ            = 0,
            triggerY            = 9100,
            triggerRange        = 1400,
            actorX              = 80610,
            actorZ              = 1500,
            actorY              = 9100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x362
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_380',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    Jump('loc_4B4')

    def _loc_380(): pass

    label('loc_380')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_38A',
    )

    Jump('loc_4B4')

    def _loc_38A(): pass

    label('loc_38A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_3E2',
    )

    ChrSetChipByIndex(0x000B, 12)
    ChrSetChipByIndex(0x000C, 13)
    ChrClearFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0010)
    ChrClearFlags(0x000B, 0x0040)
    ChrClearFlags(0x000C, 0x0040)
    ChrSetPos(0x000B, 54800, 0, 3410, 180)
    ChrSetPos(0x000C, 51130, 0, 5960, 270)
    CreateThread(0x000B, 0x00, 0x00, func_02_5AF)
    CreateThread(0x000C, 0x00, 0x00, func_04_5C6)

    Jump('loc_4B4')

    def _loc_3E2(): pass

    label('loc_3E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 6, 0x33E)),
            Expr.Return,
        ),
        'loc_43A',
    )

    ChrSetChipByIndex(0x000B, 12)
    ChrSetChipByIndex(0x000C, 13)
    ChrClearFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0010)
    ChrClearFlags(0x000B, 0x0040)
    ChrClearFlags(0x000C, 0x0040)
    ChrSetPos(0x000B, 54800, 0, 3410, 180)
    ChrSetPos(0x000C, 51130, 0, 5960, 270)
    CreateThread(0x000B, 0x00, 0x00, func_02_5AF)
    CreateThread(0x000C, 0x00, 0x00, func_04_5C6)

    Jump('loc_4B4')

    def _loc_43A(): pass

    label('loc_43A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 5, 0x33D)),
            Expr.Return,
        ),
        'loc_444',
    )

    Jump('loc_4B4')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_44E',
    )

    Jump('loc_4B4')

    def _loc_44E(): pass

    label('loc_44E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_46C',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0010)

    Jump('loc_4B4')

    def _loc_46C(): pass

    label('loc_46C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_476',
    )

    Jump('loc_4B4')

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_494',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    Jump('loc_4B4')

    def _loc_494(): pass

    label('loc_494')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_4B4',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0008)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrClearFlags(0x000E, 0x0080)

    def _loc_4B4(): pass

    label('loc_4B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 7, 0x33F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_567',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            Expr.Return,
        ),
        'loc_517',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0010, 13450, 200, 6240, 0)
    ChrSetFlags(0x0010, 0x0002)
    ChrSetChipByIndex(0x0010, 11)
    ChrSetSubChip(0x0012, 1)

    Jump('loc_567')

    def _loc_517(): pass

    label('loc_517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 2, 0x34A)),
            Expr.Return,
        ),
        'loc_535',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)

    Jump('loc_567')

    def _loc_535(): pass

    label('loc_535')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_558',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetSubChip(0x0012, 1)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)

    Jump('loc_567')

    def _loc_558(): pass

    label('loc_558')

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    def _loc_567(): pass

    label('loc_567')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_575',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0F_4373)

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_58C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x46),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_10_58EA)

    def _loc_58C(): pass

    label('loc_58C')

    Return()

# id: 0x0001 offset: 0x58D
@scena.Code('func_01_58D')
def func_01_58D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A5',
    )

    OP_B1('t1510_y')

    Jump('loc_5AE')

    def _loc_5A5(): pass

    label('loc_5A5')

    OP_B1('t1510_n')

    def _loc_5AE(): pass

    label('loc_5AE')

    Return()

# id: 0x0002 offset: 0x5AF
@scena.Code('func_02_5AF')
def func_02_5AF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C4',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_5AF')

    def _loc_5C4(): pass

    label('loc_5C4')

    Return()

# id: 0x0003 offset: 0x5C5
@scena.Code('func_03_5C5')
def func_03_5C5():
    Return()

# id: 0x0004 offset: 0x5C6
@scena.Code('func_04_5C6')
def func_04_5C6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5E9',
    )

    OP_8D(0x00FE, 50200, 5000, 54800, 6300, 2000)

    Jump('func_04_5C6')

    def _loc_5E9(): pass

    label('loc_5E9')

    Return()

# id: 0x0005 offset: 0x5EA
@scena.Code('func_05_5EA')
def func_05_5EA():
    TalkBegin(0x0008)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_648',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x15)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_648(): pass

    label('loc_648')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_662',
    )

    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

    def _loc_662(): pass

    label('loc_662')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_6B8',
    )

    ChrTalk(
        0x0008,
        (
            '噢，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '客人又来钓鱼吗？\n',
            '请在这里好好放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1007')

    def _loc_6B8(): pass

    label('loc_6B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            Expr.Return,
        ),
        'loc_71A',
    )

    ChrTalk(
        0x0008,
        (
            '那边的两个人，\n',
            '喝得真是不少啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我必须要去拉文努村\n',
            '多订购一些果实酒才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1007')

    def _loc_71A(): pass

    label('loc_71A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_775',
    )

    ChrTalk(
        0x0008,
        (
            '哟，鱼钓得怎么样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果钓到什么好东西的话，\n',
            '不妨让我们帮你做成菜哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1007')

    def _loc_775(): pass

    label('loc_775')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 6, 0x33E)),
            Expr.Return,
        ),
        'loc_7BE',
    )

    ChrTalk(
        0x0008,
        (
            '唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今天又进了很新鲜的鱼。\n',
            '敬请期待我们的料理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1007')

    def _loc_7BE(): pass

    label('loc_7BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 5, 0x33D)),
            Expr.Return,
        ),
        'loc_842',
    )

    ChrTalk(
        0x0008,
        (
            '来找罗伊德大叔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果你们不介意的话，\n',
            '一定要留在这里住一晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '刚才正好有一个房间\n',
            '因为取消预定空出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1007')

    def _loc_842(): pass

    label('loc_842')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_CE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 4, 0x33C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C8F',
    )

    SetScenaFlags(ScenaFlag(0x0067, 4, 0x33C))
    OP_28(0x0038, 0x01, 0x0002)
    EventBegin(0x00)
    OP_69(0x0008, 1000)
    ChrSetSubChip(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#1220030640V欢迎来到川蝉亭。\n',
            '请问几位客人是来留宿的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030641V#501F嗯……也算是吧。\n',
            '其实我们不单是来留宿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030642V#010F我们还要找一个人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030643V请问在这里留宿的客人当中，\n',
            '有没有钓鱼爱好者呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030644V嗯，说到钓鱼，\n',
            '这里的大部分客人都非常喜欢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030645V#020F听说昨天来留宿的老伯\n',
            '认识这里的一位钓友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030646V不知道你是否认识那位钓友呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030647V啊啊，你说罗伊德大叔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030648V你们一说钓友，\n',
            '我就知道是罗伊德大叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030649V#505F罗伊德？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030650V嗯，一位从王都来的客人，\n',
            '自称是专业的前卫钓鱼者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030651V听说他也是王都的\n',
            '『钓公师团』的成员之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 1, 0x369)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BBA',
    )

    ChrTalk(
        0x0101,
        (
            '#0010030652V#506F听、听起来好像很厉害啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030653V#000F那么他现在在哪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030654V哈哈，这个时间他应该\n',
            '正在悠然自得地垂钓吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030655V到里面的栈桥就可以找到他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C8A')

    def _loc_BBA(): pass

    label('loc_BBA')

    ChrTalk(
        0x0101,
        (
            '#0010030656V#506F听、听起来好像很厉害啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030657V#000F想问一下他是不是\n',
            '在外面钓鱼的那个大叔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030658V啊啊，我想就是他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1220030659V你们大声叫他就行了，\n',
            '如果太小声的话他可能听不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C8A(): pass

    label('loc_C8A')

    EventEnd(0x01)

    Jump('loc_CE0')

    def _loc_C8F(): pass

    label('loc_C8F')

    ChrTalk(
        0x0008,
        (
            '罗依德先生现在应该\n',
            '正在悠然自得地垂钓吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '到里面的栈桥就可以找到他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_CE0(): pass

    label('loc_CE0')

    Jump('loc_1007')

    def _loc_CE3(): pass

    label('loc_CE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_DEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D93',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0008,
        (
            '说起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '王国军也曾经到这里\n',
            '打听失踪的定期船的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，\n',
            '这里平时可是平静得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '别说可疑的人物，\n',
            '就连定期船也不会在这里出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DEB')

    def _loc_D93(): pass

    label('loc_D93')

    ChrTalk(
        0x0008,
        (
            '王国军也曾经到这里\n',
            '打听失踪的定期船的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，\n',
            '这里平时可是平静得不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DEB(): pass

    label('loc_DEB')

    Jump('loc_1007')

    def _loc_DEE(): pass

    label('loc_DEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_F12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E9C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0008,
        (
            '说起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从这里向西北方向望去，\n',
            '能看到一座很古老的塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个建筑物好像\n',
            '被称为『琥珀之塔』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那座塔究竟是\n',
            '为了什么而建造出来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F0F')

    def _loc_E9C(): pass

    label('loc_E9C')

    ChrTalk(
        0x0008,
        (
            '从这里向西北方向望去，\n',
            '能看到一座被称为\n',
            '『琥珀之塔』的很古老的塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那座塔究竟是\n',
            '为了什么而建造出来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F0F(): pass

    label('loc_F0F')

    Jump('loc_1007')

    def _loc_F12(): pass

    label('loc_F12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1007',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FA1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0008,
        (
            '噢，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里是我们兄妹俩经营的\n',
            '瓦雷利亚湖北岸旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，如果没什么急事，\n',
            '请在这里好好放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1007')

    def _loc_FA1(): pass

    label('loc_FA1')

    ChrTalk(
        0x0008,
        (
            '这里是我们兄妹俩经营的\n',
            '瓦雷利亚湖北岸旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，如果没什么急事，\n',
            '请在这里好好放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1007(): pass

    label('loc_1007')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x100B
@scena.Code('func_06_100B')
def func_06_100B():
    Call(0, 0x0007)

    Return()

# id: 0x0007 offset: 0x1010
@scena.Code('func_07_1010')
def func_07_1010():
    TalkBegin(0x0009)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_106C',
    )

    OP_0D()
    OP_A9(0x14)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_106C(): pass

    label('loc_106C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_107D',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_107D(): pass

    label('loc_107D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_10C0',
    )

    ChrTalk(
        0x0009,
        (
            '今天真是好天气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呵呵，\n',
            '被子都应该晒干了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F6D')

    def _loc_10C0(): pass

    label('loc_10C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            Expr.Return,
        ),
        'loc_111E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '这绝对不是我在自夸，\n',
            '我哥烧的鱼可是非常好吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请你们一定要尝一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F6D')

    def _loc_111E(): pass

    label('loc_111E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_11EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11A0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '本店的料理\n',
            '都是用从渔夫那里\n',
            '直接购进的鲜鱼制成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '所以说呢，来本店的客人\n',
            '都能品尝到最新鲜的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11E7')

    def _loc_11A0(): pass

    label('loc_11A0')

    ChrTalk(
        0x0009,
        (
            '你在找同伴的那个男孩子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不好意思，\n',
            '他好像没有到这边来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11E7(): pass

    label('loc_11E7')

    Jump('loc_1F6D')

    def _loc_11EA(): pass

    label('loc_11EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 6, 0x33E)),
            Expr.Return,
        ),
        'loc_1558',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 6, 0x346)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1256',
    )

    ChrTalk(
        0x0009,
        (
            '各位，\n',
            '来到这里可不要错过钓鱼的乐趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们也准备了租借用的钓竿，\n',
            '请随意使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1555')

    def _loc_1256(): pass

    label('loc_1256')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 4, 0x344)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_141C',
    )

    EventBegin(0x00)
    OP_69(0x0009, 1000)
    SetScenaFlags(ScenaFlag(0x0068, 4, 0x344))

    ChrTalk(
        0x0101,
        (
            '#0010030961V#000F那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030962V请问你们这里有钓鱼竿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030963V嗯，有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030964V您是想钓鱼吧。\n',
            '来留宿的客人不用付租金。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030965V#001F啊，真的吗？\n',
            '太幸运了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0332, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '钓鱼竿',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010030966V#501F嗯，虽说是租借用的钓鱼竿，\n',
            '不过质量还挺不错的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030967V那我就不客气地拿去用了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030968V呵呵……\n',
            '请好好享受钓鱼的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_1555')

    def _loc_141C(): pass

    label('loc_141C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14FB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0101,
        (
            '#501F想问问，\n',
            '你们这里有什么好的钓鱼场所呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '让我想想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '说到好的钓鱼场所，\n',
            '肯定是湖上的小岛上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过我觉得还是\n',
            '栈桥周围的环境最好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '水底的地形比较复杂，\n',
            '所以那里的鱼也会有比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1555')

    def _loc_14FB(): pass

    label('loc_14FB')

    ChrTalk(
        0x0009,
        (
            '我觉得还是\n',
            '栈桥周围的环境最好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '水底的地形比较复杂，\n',
            '所以那里的鱼也会有比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1555(): pass

    label('loc_1555')

    Jump('loc_1F6D')

    def _loc_1558(): pass

    label('loc_1558')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 5, 0x33D)),
            Expr.Return,
        ),
        'loc_1BE7',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 22480, 0, 5710, 90)
    ChrSetPos(0x0102, 22370, 0, 6610, 90)
    ChrSetPos(0x0103, 21380, 0, 5470, 90)
    ChrSetPos(0x0104, 22060, 0, 4510, 45)
    ChrTurnDirection(0x0009, 0x0101, 0)
    OP_69(0x0009, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16FB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '#1240030855V哎呀，客人是要留宿的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030856V#501F嗯，有这个打算……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020030857V#010F艾丝蒂尔，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030858V如果有什么事情还没做的话，\n',
            '还是趁这个时间去完成比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030859V要是我们租了房间，\n',
            '那就不能再回柏斯了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030860V#000F嗯，的确是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    Jump('loc_1721')

    def _loc_16FB(): pass

    label('loc_16FB')

    ChrTalk(
        0x0009,
        (
            '#1240030863V啊，你们要租房间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1721(): pass

    label('loc_1721')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
        10,
        0,
        (
            TXT(0x00, '【暂时不租】\n'),
            TXT(0x01, '【租房间】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_178A'),
        (0x00000001, 'loc_17E2'),
        (-1, 'loc_1BE4'),
    )

    def _loc_178A(): pass

    label('loc_178A')

    ChrTalk(
        0x0009,
        (
            '#1240030861V我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030862V你们可以先预约，\n',
            '等办完事情再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_4B(0x0009, 255)

    Jump('loc_1BE4')

    def _loc_17E2(): pass

    label('loc_17E2')

    ChrTalk(
        0x0009,
        (
            '#1240030864V我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030865V各位请这边走。\n',
            '我带你们到房间去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapClearFlags(0x00000001)
    SetScenaFlags(ScenaFlag(0x0067, 6, 0x33E))
    OP_28(0x0038, 0x01, 0x0040)
    OP_28(0x0016, 0x04, 0x40)
    OP_28(0x0018, 0x04, 0x40)
    FadeOut(1500, 0, -1)
    OP_0D()
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0103, 0x0004)
    ChrSetPos(0x0009, 104400, 0, 13140, 180)
    ChrSetPos(0x0101, 106160, 0, 11480, 180)
    ChrSetPos(0x0102, 105150, 0, 10900, 180)
    ChrSetPos(0x0104, 104580, 0, 11870, 180)
    ChrSetPos(0x0103, 105850, 0, 12550, 180)
    CameraMove(107290, 0, 4690, 0)
    CameraSetDistance(2800, 0)
    Sleep(1000)

    FadeIn(1500, 0)
    CameraMove(107690, 0, 12420, 3000)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#1240030866V这里就是客人你们的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030867V那么，在享用晚饭之前，\n',
            '大家就先在这里好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0004)
    ChrSetDirection(0x0009, 225, 300)
    ChrWalkTo(0x0009, 103940, 0, 12930, 2000, 0x00)

    @scena.Lambda('lambda_1984')
    def lambda_1984():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1984)

    ChrWalkTo(0x0009, 102270, 0, 12930, 2000, 0x00)
    ChrSetFlags(0x0009, 0x0080)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020030868V#010F的确是一间好房子啊。\n',
            '和城市的酒店相比，真的别有一番风味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030869V#006F#2P嗯，感觉真好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030870V而且租金又不是很贵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 225, 400)

    ChrTalk(
        0x0103,
        (
            '#0030030871V#020F#1P呵呵，好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030872V在今夜行动之前，\n',
            '我们就先好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 90, 400)

    ChrTalk(
        0x0104,
        (
            '#0040030873V#031F呵呵，不错的提议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030874V#004F#2P啊，虽然放松一下也不错……\n',
            '可是这么悠然自得地休息可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030875V#021F#1P休息的时候就该好好休息。\n',
            '这也是游击士的工作啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030876V吃零食也好，到外面散步也好，\n',
            '总之现在可以自由活动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1500._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1BE4(): pass

    label('loc_1BE4')

    Jump('loc_1F6D')

    def _loc_1BE7(): pass

    label('loc_1BE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1C41',
    )

    ChrTalk(
        0x0009,
        (
            '各位客人您好。\n',
            '欢迎来到川蝉亭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果想留宿的话，\n',
            '请先到我这里来登记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F6D')

    def _loc_1C41(): pass

    label('loc_1C41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1CB4',
    )

    ChrTalk(
        0x0009,
        (
            '王国军好像到\n',
            '琥珀之塔周边进行了调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '而且他们好像\n',
            '发现了一个可疑人物。\n',
            '听说还是一位考古学者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F6D')

    def _loc_1CB4(): pass

    label('loc_1CB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1DA5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D4A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '这里是原本是\n',
            '雷纳德哥哥经营的旅馆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我来这里玩的时候\n',
            '被这里的气氛所深深吸引。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '所以我就干脆\n',
            '来帮哥哥打理这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DA2')

    def _loc_1D4A(): pass

    label('loc_1D4A')

    ChrTalk(
        0x0009,
        (
            '我来这里玩的时候\n',
            '被这里的气氛所深深吸引……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '所以我就干脆\n',
            '来帮哥哥打理这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DA2(): pass

    label('loc_1DA2')

    Jump('loc_1F6D')

    def _loc_1DA5(): pass

    label('loc_1DA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1F6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ED5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '欢迎来到川蝉亭。\n',
            '请问客人是来留宿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030877V#501F嗯……这个嘛，\n',
            '其实不是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030878V哦，真是遗憾呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030879V这里湖边景色十分漂亮，\n',
            '而且全天都吹着清爽自然的风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030880V在这里休闲度假是最适合不过了。\n',
            '以后有机会一定要来这里休息一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F6D')

    def _loc_1ED5(): pass

    label('loc_1ED5')

    ChrTalk(
        0x0009,
        (
            '#1240030881V这里湖边景色十分漂亮，\n',
            '而且全天都吹着清爽自然的风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1240030882V在这里休闲度假是最适合不过了。\n',
            '以后有机会一定要来这里休息一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F6D(): pass

    label('loc_1F6D')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x1F71
@scena.Code('func_08_1F71')
def func_08_1F71():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '今天又让那家伙\n',
            '逃过了我一次的追捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来要选择一个更好的位置才行，\n',
            '再努力一下试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1FDA
@scena.Code('func_09_1FDA')
def func_09_1FDA():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            Expr.Return,
        ),
        'loc_201F',
    )

    ChrTalk(
        0x00FE,
        (
            '一到傍晚，\n',
            '这附近就被夕阳染成橘黄色，\n',
            '非常漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_238D')

    def _loc_201F(): pass

    label('loc_201F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_213C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20CB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '又这样悠悠闲闲地过了一天啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作累了的话，\n',
            '适当放松一下也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说回去还有很多工作要做，\n',
            '不过休息的时候还是要好好休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2139')

    def _loc_20CB(): pass

    label('loc_20CB')

    ChrTalk(
        0x00FE,
        (
            '工作累了的话，\n',
            '适当放松一下也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说回去还有很多工作要做，\n',
            '不过休息的时候还是要好好休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2139(): pass

    label('loc_2139')

    Jump('loc_238D')

    def _loc_213C(): pass

    label('loc_213C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 6, 0x33E)),
            Expr.Return,
        ),
        'loc_217D',
    )

    ChrTalk(
        0x00FE,
        (
            '啊呀，\n',
            '你们也是来这里投宿的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请多关照哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_238D')

    def _loc_217D(): pass

    label('loc_217D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 5, 0x33D)),
            Expr.Return,
        ),
        'loc_2268',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2213',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '明年我要和老公一起\n',
            '来这里度假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每年他只有看家的份，\n',
            '也真是挺可怜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，和女儿两个人来，\n',
            '这种感觉也蛮不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2265')

    def _loc_2213(): pass

    label('loc_2213')

    ChrTalk(
        0x00FE,
        (
            '明年我要和老公一起\n',
            '来这里度假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每年他只有看家的份，\n',
            '也真是挺可怜的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2265(): pass

    label('loc_2265')

    Jump('loc_238D')

    def _loc_2268(): pass

    label('loc_2268')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_22A8',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯的这间川蝉亭\n',
            '和蔡斯的红叶亭，\n',
            '我都非常喜欢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_238D')

    def _loc_22A8(): pass

    label('loc_22A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2318',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然顺着那些旅游胜地\n',
            '一路游览下来也很不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我还是喜欢像这样\n',
            '悠然自得的旅行生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_238D')

    def _loc_2318(): pass

    label('loc_2318')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_2386',
    )

    ChrTalk(
        0x00FE,
        (
            '今天天气真是好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我决定下午\n',
            '在湖边好好看书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，不过看书之余，\n',
            '也想试试钓鱼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_238D')

    def _loc_2386(): pass

    label('loc_2386')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_238D',
    )

    def _loc_238D(): pass

    label('loc_238D')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x2391
@scena.Code('func_0A_2391')
def func_0A_2391():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            Expr.Return,
        ),
        'loc_23F3',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多到吃饭的时间了。\n',
            '今天的菜会是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的菜还是可以期待一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_273A')

    def _loc_23F3(): pass

    label('loc_23F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_249B',
    )

    ChrTalk(
        0x00FE,
        (
            '本店的大部分客人\n',
            '都是为了钓鱼而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前从柏斯来了一个老爷爷，\n',
            '他为了在这里钓鱼连家也不回，\n',
            '一钓就是一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也想试试\n',
            '钓一天的鱼是什么感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_273A')

    def _loc_249B(): pass

    label('loc_249B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 6, 0x33E)),
            Expr.Return,
        ),
        'loc_24D9',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的晚饭是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在就开始期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_273A')

    def _loc_24D9(): pass

    label('loc_24D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 5, 0x33D)),
            Expr.Return,
        ),
        'loc_258E',
    )

    ChrTalk(
        0x00FE,
        (
            '从王都来的那个叫罗伊德的人\n',
            '好像挺古怪的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他钓鱼的时候，无论你怎么叫他，\n',
            '他也好像完全没有反应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在食堂和他聊天的时候，\n',
            '他给人的感觉却是很随和很健谈的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_273A')

    def _loc_258E(): pass

    label('loc_258E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_26CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_266F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '每年的这个时候，\n',
            '我和母亲\n',
            '都会到这里来旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里呆上几天\n',
            '是我们母女的例行公事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '母亲她每年\n',
            '都很期待这个旅游哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每次都是我和母亲两个人来，\n',
            '而把父亲自己丢在家里。\n',
            '总觉得他有点可怜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26CC')

    def _loc_266F(): pass

    label('loc_266F')

    ChrTalk(
        0x00FE,
        (
            '每年的这个时候，\n',
            '我和母亲\n',
            '都会到这里来旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里呆上几天\n',
            '是我们母女的例行公事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26CC(): pass

    label('loc_26CC')

    Jump('loc_273A')

    def _loc_26CF(): pass

    label('loc_26CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_273A',
    )

    ChrTalk(
        0x00FE,
        (
            '可以品尝美味的料理，\n',
            '又可以悠闲地度假……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这是超级的享受，\n',
            '不过也要注意是否会发胖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_273A(): pass

    label('loc_273A')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x273E
@scena.Code('func_0B_273E')
def func_0B_273E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29E3',
    )

    SetScenaFlags(ScenaFlag(0x006B, 7, 0x35F))
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0101,
        (
            '#006F（咦……\n',
            '　这个人莫非是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，\n',
            '　好像和我们一样都是游击士呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那个……',
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

    ChrTalk(
        0x0101,
        (
            '#002F喂，打扰一下？',
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

    ChrTalk(
        0x0103,
        (
            '#023F蜂蜜苏打水……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#020F好久不见了呢，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '你是……\n',
            '以前的那个见习游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F没错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '托你的福，\n',
            '现在我已经是正游击士啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……看起来的确成熟了不少。\n',
            '在柏斯支部有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，现在就正在工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近发生了很多事情，\n',
            '游击士的人手远远不够呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#002F（是雪拉姐的熟人吧。\n',
            '　感觉有点恐怖的人呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（但是那走路的动作……\n',
            '　看起来应该很厉害吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BEC')

    def _loc_29E3(): pass

    label('loc_29E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BAB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0101,
        (
            '#000F啊，您是……\n',
            '是斯丁克先生吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F您会在这里，\n',
            '难道是发生了什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我是来消灭通缉魔兽的。\n',
            '不是什么大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从卢格兰老爷子那里听说了，\n',
            '你们真的是卡西乌斯先生的孩子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F您认识父亲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊……\n',
            '以前曾经受过他的照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111172V#505F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '老爸在柏斯地区\n',
            '熟人也相当多呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 0)

    Jump('loc_2BEC')

    def _loc_2BAB(): pass

    label('loc_2BAB')

    ChrTurnDirection(0x00FE, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '……如果能早点得知\n',
            '卡西乌斯先生的消息就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 0)

    def _loc_2BEC(): pass

    label('loc_2BEC')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x2BF0
@scena.Code('func_0C_2BF0')
def func_0C_2BF0():
    TalkBegin(0x000E)
    ChrTurnDirection(0x00FE, 0x0103, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EBE',
    )

    SetScenaFlags(ScenaFlag(0x006C, 0, 0x360))

    ChrTalk(
        0x00FE,
        (
            '#0120020457V#814F啊，难道……\n',
            '这不是雪拉扎德前辈吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020458V#850F很久不见了～\n',
            '自从您去修行之后就再没见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020459V#020F啊呀，这不是亚妮拉丝嘛。\n',
            '你在这里做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120020460V#810嗯～\n',
            '协会委托我来这边消灭通缉魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020461V就在刚才，\n',
            '我终于把工作解决掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020462V#020F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020463V对了，\n',
            '你已经找到所谓的剑之道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#0120020464V#819F呵呵，请别问了。\n',
            '我还处在修行阶段呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020465V#810F说起来，\n',
            '前辈您也是在执行协会的任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020466V#020F是啊，不过我和你的任务性质不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120020467V#810F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020468V这个地区最近发生的\n',
            '不寻常的事情还真多啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020469V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F2C')

    def _loc_2EBE(): pass

    label('loc_2EBE')

    ChrTalk(
        0x00FE,
        (
            '#0120020470V#810F雪拉扎德前辈，\n',
            '这个地区最近发生了很多不寻常的事情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020471V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F2C(): pass

    label('loc_2F2C')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x2F30
@scena.Code('func_0D_2F30')
def func_0D_2F30():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F49',
    )

    TalkEnd(0x0010)
    Call(0, 0x0011)

    Jump('loc_3918')

    def _loc_2F49(): pass

    label('loc_2F49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_3482',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 2, 0x34A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_327D',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0069, 2, 0x34A))
    CameraMove(14850, 0, 6330, 1000)

    ChrTalk(
        0x000F,
        (
            '#0030030979V#028F唔～\n',
            '你的酒量也不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030980V哦呵呵……正合我意啊㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030981V好啦好啦，赶快给我喝！\n',
            '（咕噜咕噜咕噜……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(249, 0x00, 0x64)
    Fade(1000)
    ChrSetSubChip(0x0012, 5)
    OP_0D()
    OP_62(0x0010, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0040030982V#037F等、等一下。\n',
            '你喝得有点太猛了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030983V这样的话晚上的工作不就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0030030984V#029F……你说什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_7C(0, 200, 2000, 200)

    ChrTalk(
        0x000F,
        (
            '#0030030985V#029F哼哼，赖皮演奏家！\n',
            '难道你不愿意喝我敬你的酒吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0040030986V#038F哇哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0010, 0x0010)
    ChrTurnDirection(0x0010, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3148',
    )

    ChrSetSubChip(0x0010, 1)

    Jump('loc_3179')

    def _loc_3148(): pass

    label('loc_3148')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_315E',
    )

    ChrSetSubChip(0x0010, 0)

    Jump('loc_3179')

    def _loc_315E(): pass

    label('loc_315E')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3174',
    )

    ChrSetSubChip(0x0010, 2)

    Jump('loc_3179')

    def _loc_3174(): pass

    label('loc_3174')

    ChrSetSubChip(0x0010, 1)

    def _loc_3179(): pass

    label('loc_3179')

    ChrSetDirection(0x0010, 90, 0)
    ChrSetFlags(0x0010, 0x0010)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0040030987V#038F艾丝蒂尔君……\n',
            '你们怎么不帮我说几句啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030988V#007F不好意思啊～\n',
            '变成这样的话我也阻止不住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030989V#006F别担心，\n',
            '雪拉姐就算喝多少瓶都不会醉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0040030990V#037F我是说……你们不担心我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 0)
    EventEnd(0x00)

    Jump('loc_347F')

    def _loc_327D(): pass

    label('loc_327D')

    ChrClearFlags(0x0010, 0x0010)
    ChrTurnDirection(0x0010, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_329F',
    )

    ChrSetSubChip(0x0010, 1)

    Jump('loc_32BA')

    def _loc_329F(): pass

    label('loc_329F')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_32B5',
    )

    ChrSetSubChip(0x0010, 1)

    Jump('loc_32BA')

    def _loc_32B5(): pass

    label('loc_32B5')

    ChrSetSubChip(0x0010, 2)

    def _loc_32BA(): pass

    label('loc_32BA')

    ChrSetDirection(0x0010, 90, 0)
    ChrSetFlags(0x0010, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3402',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0010,
        (
            '#0040030991V#037F她、她真的这么能喝吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030992V#007F雪拉姐不单是一级的游击士，\n',
            '而且还是一级的酒场好手呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030993V就连我家的老爸也喝不过她。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0040030994V#037F这、这么厉害啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030995V这样说我倒是想看看她喝醉的样子。\n',
            '不过我还是有点怕怕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_347A')

    def _loc_3402(): pass

    label('loc_3402')

    ChrTalk(
        0x0010,
        (
            '#0040030996V#037F虽说想看她有什么大胆的表演，\n',
            '不过在那之前我可能已经醉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030997V唔……这是重大的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_347A(): pass

    label('loc_347A')

    ChrSetSubChip(0x0010, 0)
    def _loc_347F(): pass

    label('loc_347F')

    Jump('loc_3918')

    def _loc_3482(): pass

    label('loc_3482')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 3, 0x343)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_376D',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0068, 3, 0x343))
    CameraMove(14850, 0, 6330, 1000)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德和奥利维尔\n',
            '以沁凉的果实酒交杯换盏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrTurnDirection(0x0101, 0x000F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030905V#000F雪拉姐呀……\n',
            '现在还是白天你就喝这么多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030906V就算是再清淡的酒也有个限度啊，\n',
            '喝多了不怕搞坏身体吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0010)
    ChrTurnDirection(0x000F, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_359D',
    )

    ChrSetSubChip(0x000F, 2)

    Jump('loc_35CE')

    def _loc_359D(): pass

    label('loc_359D')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_35B3',
    )

    ChrSetSubChip(0x000F, 1)

    Jump('loc_35CE')

    def _loc_35B3(): pass

    label('loc_35B3')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_35C9',
    )

    ChrSetSubChip(0x000F, 0)

    Jump('loc_35CE')

    def _loc_35C9(): pass

    label('loc_35C9')

    ChrSetSubChip(0x000F, 2)

    def _loc_35CE(): pass

    label('loc_35CE')

    ChrSetDirection(0x000F, 270, 0)
    ChrSetFlags(0x000F, 0x0010)

    ChrTalk(
        0x000F,
        (
            '#0030030907V#021F没问题，没问题。\n',
            '酒这种东西其实和水差不多嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0010, 0x0010)
    ChrTurnDirection(0x0010, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3640',
    )

    ChrSetSubChip(0x0010, 1)

    Jump('loc_3671')

    def _loc_3640(): pass

    label('loc_3640')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3656',
    )

    ChrSetSubChip(0x0010, 0)

    Jump('loc_3671')

    def _loc_3656(): pass

    label('loc_3656')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_366C',
    )

    ChrSetSubChip(0x0010, 2)

    Jump('loc_3671')

    def _loc_366C(): pass

    label('loc_366C')

    ChrSetSubChip(0x0010, 1)

    def _loc_3671(): pass

    label('loc_3671')

    ChrSetDirection(0x0010, 90, 0)
    ChrSetFlags(0x0010, 0x0010)

    ChrTalk(
        0x0010,
        (
            '#0040030908V#035F呵呵，艾丝蒂尔君。\n',
            '有时候也要适当放松一下自己嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030909V我知道怎么服侍雪拉君，\n',
            '你们就放心把她交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030910V#007F不，令人担心的倒不是雪拉姐……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0040030911V#033F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x000F, 0)
    EventEnd(0x00)

    Jump('loc_3918')

    def _loc_376D(): pass

    label('loc_376D')

    ChrClearFlags(0x0010, 0x0010)
    ChrTurnDirection(0x0010, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_378F',
    )

    ChrSetSubChip(0x0010, 1)

    Jump('loc_37AA')

    def _loc_378F(): pass

    label('loc_378F')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_37A5',
    )

    ChrSetSubChip(0x0010, 1)

    Jump('loc_37AA')

    def _loc_37A5(): pass

    label('loc_37A5')

    ChrSetSubChip(0x0010, 2)

    def _loc_37AA(): pass

    label('loc_37AA')

    ChrSetDirection(0x0010, 90, 0)
    ChrSetFlags(0x0010, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3886',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x0010,
        (
            '#0040030912V#035F我只是问她要不要喝一杯，\n',
            '她就很轻易地说ＯＫ没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030913V呵呵，雪拉君也终于开始\n',
            '注意到我无人能敌的魅力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030914V#000F（过分的自信怕是会弄出人命的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3913')

    def _loc_3886(): pass

    label('loc_3886')

    ChrTalk(
        0x0010,
        (
            '#0040030915V#031F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030916V如果她醉倒的话，\n',
            '我会温柔地让她投入我的怀里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030917V#007F（我为你的无知有点担心……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3913(): pass

    label('loc_3913')

    ChrSetSubChip(0x0010, 0)

    def _loc_3918(): pass

    label('loc_3918')

    TalkEnd(0x0010)

    Return()

# id: 0x000E offset: 0x391C
@scena.Code('func_0E_391C')
def func_0E_391C():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3935',
    )

    TalkEnd(0x000F)
    Call(0, 0x0011)

    Jump('loc_436F')

    def _loc_3935(): pass

    label('loc_3935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_3E24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 2, 0x34A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C70',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0069, 2, 0x34A))
    CameraMove(14850, 0, 6330, 1000)

    ChrTalk(
        0x000F,
        (
            '#0030030998V#028F唔～\n',
            '你的酒量也不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030999V哦呵呵……正合我意啊㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031000V好啦好啦，赶快给我喝！\n',
            '（咕噜咕噜咕噜……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(249, 0x00, 0x64)
    Fade(1000)
    ChrSetSubChip(0x0012, 5)
    OP_0D()
    OP_62(0x0010, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0040031001V#037F等、等一下。\n',
            '你喝得有点太猛了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031002V这样的话晚上的工作不就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0030031003V#029F……你说什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_7C(0, 200, 2000, 200)

    ChrTalk(
        0x000F,
        (
            '#0030031004V#029F哼哼，赖皮演奏家！\n',
            '难道你不愿意喝我敬你的酒吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0040031005V#038F哇哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0010, 0x0010)
    ChrTurnDirection(0x0010, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3B34',
    )

    ChrSetSubChip(0x0010, 1)

    Jump('loc_3B65')

    def _loc_3B34(): pass

    label('loc_3B34')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3B4A',
    )

    ChrSetSubChip(0x0010, 0)

    Jump('loc_3B65')

    def _loc_3B4A(): pass

    label('loc_3B4A')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3B60',
    )

    ChrSetSubChip(0x0010, 2)

    Jump('loc_3B65')

    def _loc_3B60(): pass

    label('loc_3B60')

    ChrSetSubChip(0x0010, 1)

    def _loc_3B65(): pass

    label('loc_3B65')

    ChrSetDirection(0x0010, 90, 0)
    ChrSetFlags(0x0010, 0x0010)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0040031006V#038F艾丝蒂尔君……\n',
            '你们怎么不帮我说几句啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031007V#007F不好意思啊～\n',
            '变成这样的话我也阻止不住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031008V#006F别担心，\n',
            '雪拉姐就算喝多少瓶都不会醉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0040031009V#037F我是说……你们不担心我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 0)
    EventEnd(0x00)

    Jump('loc_3E21')

    def _loc_3C70(): pass

    label('loc_3C70')

    ChrClearFlags(0x000F, 0x0010)
    ChrTurnDirection(0x000F, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3C92',
    )

    ChrSetSubChip(0x000F, 2)

    Jump('loc_3CAD')

    def _loc_3C92(): pass

    label('loc_3C92')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3CA8',
    )

    ChrSetSubChip(0x000F, 2)

    Jump('loc_3CAD')

    def _loc_3CA8(): pass

    label('loc_3CA8')

    ChrSetSubChip(0x000F, 1)

    def _loc_3CAD(): pass

    label('loc_3CAD')

    ChrSetDirection(0x000F, 270, 0)
    ChrSetFlags(0x000F, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D78',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000F,
        (
            '#0030031010V#028F唔……好热啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031011V干脆通通脱光算了，\n',
            '穿着衣服喝酒好麻烦啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031012V#004F你、你喝醉啦。\n',
            '这里有很多客人在吃饭啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E1C')

    def _loc_3D78(): pass

    label('loc_3D78')

    OP_62(0x000F, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0030031013V#028F艾丝蒂尔～你这个小丫头\n',
            '真的是越看越可爱呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031014V来，陪姐姐喝一杯好不好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031015V#002F我不喝！ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E1C(): pass

    label('loc_3E1C')

    ChrSetSubChip(0x000F, 0)
    def _loc_3E21(): pass

    label('loc_3E21')

    Jump('loc_436F')

    def _loc_3E24(): pass

    label('loc_3E24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 3, 0x343)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4108',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0068, 3, 0x343))
    CameraMove(14850, 0, 6330, 1000)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德和奥利维尔\n',
            '以沁凉的果实酒交杯换盏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010030918V#000F雪拉姐呀……\n',
            '现在还是白天你就喝这么多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030919V就算是再清淡的酒也有个限度啊，\n',
            '喝多了不怕搞坏身体吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0010)
    ChrTurnDirection(0x000F, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3F38',
    )

    ChrSetSubChip(0x000F, 2)

    Jump('loc_3F69')

    def _loc_3F38(): pass

    label('loc_3F38')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3F4E',
    )

    ChrSetSubChip(0x000F, 1)

    Jump('loc_3F69')

    def _loc_3F4E(): pass

    label('loc_3F4E')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3F64',
    )

    ChrSetSubChip(0x000F, 0)

    Jump('loc_3F69')

    def _loc_3F64(): pass

    label('loc_3F64')

    ChrSetSubChip(0x000F, 2)

    def _loc_3F69(): pass

    label('loc_3F69')

    ChrSetDirection(0x000F, 270, 0)
    ChrSetFlags(0x000F, 0x0010)

    ChrTalk(
        0x000F,
        (
            '#0030030920V#021F没问题，没问题。\n',
            '酒这种东西其实和水差不多嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0010, 0x0010)
    ChrTurnDirection(0x0010, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3FDB',
    )

    ChrSetSubChip(0x0010, 1)

    Jump('loc_400C')

    def _loc_3FDB(): pass

    label('loc_3FDB')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3FF1',
    )

    ChrSetSubChip(0x0010, 0)

    Jump('loc_400C')

    def _loc_3FF1(): pass

    label('loc_3FF1')

    If(
        (
            (Expr.GetChrWork, 0x10, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4007',
    )

    ChrSetSubChip(0x0010, 2)

    Jump('loc_400C')

    def _loc_4007(): pass

    label('loc_4007')

    ChrSetSubChip(0x0010, 1)

    def _loc_400C(): pass

    label('loc_400C')

    ChrSetDirection(0x0010, 90, 0)
    ChrSetFlags(0x0010, 0x0010)

    ChrTalk(
        0x0010,
        (
            '#0040030921V#035F呵呵，艾丝蒂尔君。\n',
            '有时候也要适当放松一下自己嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030922V我知道怎么服侍雪拉君，\n',
            '你们就放心把她交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030923V#007F不，令人担心的倒不是雪拉姐……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0040030924V#033F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000F, 0)
    ChrSetSubChip(0x0010, 0)
    EventEnd(0x00)

    Jump('loc_436F')

    def _loc_4108(): pass

    label('loc_4108')

    ChrClearFlags(0x000F, 0x0010)
    ChrTurnDirection(0x000F, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_412A',
    )

    ChrSetSubChip(0x000F, 2)

    Jump('loc_4145')

    def _loc_412A(): pass

    label('loc_412A')

    If(
        (
            (Expr.GetChrWork, 0xF, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4140',
    )

    ChrSetSubChip(0x000F, 2)

    Jump('loc_4145')

    def _loc_4140(): pass

    label('loc_4140')

    ChrSetSubChip(0x000F, 1)

    def _loc_4145(): pass

    label('loc_4145')

    ChrSetDirection(0x000F, 270, 0)
    ChrSetFlags(0x000F, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_42C8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000F,
        (
            '#0030030925V#020F说起来，艾丝蒂尔。\n',
            '约修亚他干什么去了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030926V难道是你被甩了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030927V#007F嗯……就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0030030928V#023F真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030929V#009F我本来约他去钓鱼，\n',
            '但是他说要读书，就不管我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030930V真是的，难道不觉得态度过于冷淡了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0030030931V#025F什么呀，差点让我误会了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_436A')

    def _loc_42C8(): pass

    label('loc_42C8')

    ChrTalk(
        0x000F,
        (
            '#0030030932V#020F我知道你从小就很喜欢钓鱼。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030933V不过这可是男孩子的兴趣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030934V#001F嘿嘿，没关系啦。\n',
            '本来钓鱼就是非常有趣的事情嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_436A(): pass

    label('loc_436A')

    ChrSetSubChip(0x000F, 0)

    def _loc_436F(): pass

    label('loc_436F')

    TalkEnd(0x000F)

    Return()

# id: 0x000F offset: 0x4373
@scena.Code('func_0F_4373')
def func_0F_4373():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(17490, 0, 11000, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0103, 0x0004)
    ChrSetFlags(0x0104, 0x0004)
    ChrSetPos(0x000A, 17247, 0, 11528, 180)
    ChrSetPos(0x0101, 18088, 0, 10277, 270)
    ChrSetPos(0x0102, 18100, 0, 9000, 270)
    ChrSetPos(0x0103, 15700, 0, 10682, 90)
    ChrSetPos(0x0104, 15500, 0, 9000, 90)

    ChrTalk(
        0x000A,
        (
            '#1230030773V是这样啊……\n',
            '你们是从库瓦诺那儿听说我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030774V啊啊，我的确是看到了。\n',
            '就在前天夜晚，几个奇怪的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030775V#000F果然是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030776V可以把那天看到的事情\n',
            '详细地告诉我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030777V……在此之前我想问一句。\n',
            '你们是不是游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030778V我说的话是不是牵涉到什么案件？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030779V#012F现在还不能断定。\n',
            '不过，相关联的可能性还是有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030780V我知道了……\n',
            '既然是这样，我一定会协助你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030781V前天晚上……\n',
            '也就是我在小艇上夜钓的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030782V因为和努西苦战了一整天，\n',
            '累得不行了所以想回旅馆休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030783V天色也已经晚了，\n',
            '住宿的客人也都休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030784V#022F请等一下。\n',
            '……你说的『努西』是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030785V你可要认真听好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030786V所谓的努西，\n',
            '是生活在这个瓦雷利亚湖的\n',
            '一种十分巨大的鱼精。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030787V十年来，努西一直都是\n',
            '我们这些钓鱼爱好者最热衷的话题，\n',
            '但它同时也是一种让人难以捉摸的鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030030788V#023F（不妙……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030789V#017F（不小心让他兴致高昂起来了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030790V#004F有、有这么厉害的鱼吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030791V对啊，要知道这五年来，\n',
            '我一直在追踪那家伙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030792V不过，那家伙的脾性反复无常，\n',
            '一时游到这来一时游到那去，\n',
            '一时吃这种鱼饵一时吃那种鱼饵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030793V最近，我听说那家伙在这附近出现，\n',
            '就急忙从王都追了过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030794V#035F呵呵，多么狂热的激情啊。\n',
            '对于你的心情我非常地理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030795V若是看到了中意的东西，\n',
            '我也一定会想尽办法得到它。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030796V譬如说『格兰·夏利拿』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030797V#007F那样也叫得到吗？\n',
            '应该是不问自取偷偷喝完才对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030798V#026F咳咳……回到正题吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030799V那么罗伊德先生，\n',
            '你夜钓回来之后又怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030800V啊，好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030801V之后，我就把小艇放好，\n',
            '接着正要走回旅馆睡觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030802V就在那时，我看到了奇怪的二人组合。\n',
            '他们从旅馆出来，走到外面的街道上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030803V#012F走到街道上……\n',
            '而且是在深夜的时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030804V啊啊，我不会看错的。\n',
            '就是走到安塞尔新街那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030805V我本来以为他们\n',
            '是外出游玩晚归的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030806V不过深更半夜才回来也太奇怪了吧。\n',
            '所以第二天，我向旅馆的人打听了一下，\n',
            '不过大家都说不认识这些家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030807V当时我以为自己看到了幽灵，\n',
            '不禁感觉背后发寒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030808V#004F幽、幽灵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030809V会、会出现吗？在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030810V哈哈，我看到的是两人一起，\n',
            '而且还是一男一女的年轻组合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030811V或许那两人是一对得不到\n',
            '身边人的承认而徇情的恋人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030812V#003F啊～～～别、别再说了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030813V#025F哎呀哎呀。\n',
            '你还是怕听到幽灵这类的话题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030814V#010F就是越害怕才越想听嘛，\n',
            '怪谭之类的，还有不可思议的故事之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030815V#031F呵呵，看艾丝蒂尔君\n',
            '害怕得尖叫起来的样子，\n',
            '真是越看越可爱，越看越动人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030816V简直就像在寒风中战栗的小猫㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030817V#009F哼！再说这种话就小心你的门牙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030818V哈哈哈……\n',
            '幽灵什么的只是开玩笑而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030819V当时我还不敢肯定，\n',
            '不过那对男女应该不是情侣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030820V因为我看到那个女子穿着很怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030821V#010F穿着很怪……这怎么说呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030822V我只是看到背影，\n',
            '也不敢肯定有没有看错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030823V不过看样子她穿的就是校服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0104, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030824V#004F校服？难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030825V#014F杰尼丝王立学院的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030826V呵呵，你们知道得很清楚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030827V我的外甥女也在那学校念书，\n',
            '所以我看得出那就是王立学院的校服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030828V#022F原来如此……\n',
            '终于知道所谓的奇怪家伙是谁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030829V#009F怪不得被人叫做奇怪的家伙！\n',
            '肯定是那个嚣张的男人婆！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030830V总算抓到你的尾巴了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030831V怎么了……\n',
            '难道你们认识他们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030832V我觉得那两个人选择在\n',
            '深夜出现可能是出于什么目的吧，\n',
            '这一点你们也最好注意一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030833V对了，我还听他们说过\n',
            '今天半夜会再来这里一次的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030834V#014F啊？真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030835V对对，那个年轻男子亲口说过，\n',
            '两天后还会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030836V他的口气十分认真，让我印象很深。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030837V#020F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030838V这是很重要的线索啊。\n',
            '感谢你的合作，之后就交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030839V我们绝对会好好利用这些线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030840V呼，太好了……\n',
            '你能这么说我很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030841V突然感觉如释重负啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030842V……这下可安心了。\n',
            '我又可以安安稳稳地钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1230030843V这次不会让你逃掉的！\n',
            '各位朋友，我这就先失陪了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000A, 24343, 0, 14247, 15000, 0x00)
    ChrSetFlags(0x000A, 0x0080)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030844V#000F好一个钓鱼迷呢……\n',
            '这样的集中力我们还真是比不上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030845V#010F那个所谓的『钓公师团』，\n',
            '不知道是一个什么样的组织呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030846V#030F听到现在，\n',
            '我连那对男女是什么来头也还没搞清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030847V究竟你们在调查什么事情，\n',
            '可以向我详细地解释一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030848V#020F也对。\n',
            '事情大致是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德向奥利维尔讲解了关于\n',
            '在洛连特出现的空贼团少女乔丝特的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0104,
        (
            '#0040030849V#033F原来如此……还真是\n',
            '踏破铁鞋无觅处，得来全不费功夫。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030850V这么说，今天晚上有好戏看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030851V#020F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030852V为了慎重起见，\n',
            '我们也要租一间房间落脚比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030853V而且必须等到今天半夜才能行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030854V#000F嗯。\n',
            '我们回柜台那里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0102, 0x0004)
    ChrClearFlags(0x0103, 0x0004)
    ChrClearFlags(0x0104, 0x0004)
    Fade(1000)
    ChrSetPos(0x0000, 17154, 0, 12588, 0)
    ChrSetPos(0x0001, 17154, 0, 12588, 0)
    ChrSetPos(0x0002, 17154, 0, 12588, 0)
    ChrSetPos(0x0003, 17154, 0, 12588, 0)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x58EA
@scena.Code('func_10_58EA')
def func_10_58EA():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(23550, 0, 12290, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3030, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetSubChip(0x000F, 2)
    ChrSetSubChip(0x0010, 1)
    OP_4A(0x0009, 255)
    OP_4A(0x0008, 255)
    ChrSetDirection(0x0009, 0, 0)
    CameraMove(17310, 0, 5790, 6000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    MapSetFlags(0x02000000)
    NewScene('ED6_DT01/T1500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x5974
@scena.Code('func_11_5974')
def func_11_5974():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(15740, 0, 7650, 0)
    ChrSetPos(0x0101, 15500, 0, 7820, 225)
    ChrSetPos(0x0102, 16400, 0, 7540, 225)
    OP_0D()

    ChrTalk(
        0x0010,
        (
            '#0040031116V#038F你们……快来救救我啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031117V再、再喝下去会出……人命的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031118V#004F呜哇～好厉害哦。\n',
            '看来要对你另眼相看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031119V#010F确实是啊，陪雪拉姐姐喝酒，\n',
            '能像你这样还有意识的可没几个哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000F, 2)
    Sleep(300)

    OP_62(0x000F, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0030031120V#028F呵呵……\n',
            '你们来得真巧啊⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031121V来来来～陪姐姐一起喝酒㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031122V好不好，好不好，来～嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031123V#009F我、我们现在要去吃晚饭，\n',
            '所以就不陪你们耍酒疯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0030031124V#029F不行不行～\n',
            '通通留下来陪我喝酒～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031125V你们不陪，我可要大发雷霆哦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031126V#007F雪拉姐已经进入疯狂状态了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031127V#019F雪拉姐姐、奥利维尔，\n',
            '看来你们相处得还不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031128V说实话，其实你们俩挺相配的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000F, 0)
    Sleep(300)

    ChrSetDirection(0x0101, 225, 0)

    ChrTalk(
        0x000F,
        (
            '#0030031129V#028F#2P…………………………（盯着看）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031130V#021F什么呀～这家伙还差的远啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0040031131V#036F哎哟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031132V约、约修亚君，\n',
            '你就别这样和人家开玩笑嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031133V#008F好、好可怜的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031134V#010F有这回事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0040031135V#035F不过你们两个小坏蛋也……\n',
            '挺有情趣的……我最喜欢了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031136V…………呼呼………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031137V#007F看来白担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031138V#019F呵呵，说得也是。\n',
            '那我们到去柜台那边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031139V不要破坏他们的二人世界了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031140V#001F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, func_12_6036)
    CreateThread(0x0102, 0x01, 0x00, func_13_6090)
    Sleep(1000)

    CameraMove(14770, 0, 6250, 2000)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0040031141V#036F雪拉君……求求你了……\n',
            '不要再灌我了好不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(249, 0x00, 0x64)
    Fade(1000)
    ChrSetSubChip(0x0012, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0040031142V#038F………啊啊啊啊啊啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x0332, 1)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    OP_20(0x000007D0)
    FadeOut(2000, 0, -1)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1501._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x6036
@scena.Code('func_12_6036')
def func_12_6036():
    Sleep(700)

    ChrSetFlags(0x00FE, 0x0004)
    ChrSetDirection(0x00FE, 90, 400)
    ChrWalkTo(0x00FE, 18440, 0, 7500, 2000, 0x00)
    ChrWalkTo(0x00FE, 19630, 0, 8710, 2000, 0x00)
    ChrWalkTo(0x00FE, 24950, 0, 8780, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0013 offset: 0x6090
@scena.Code('func_13_6090')
def func_13_6090():
    ChrSetDirection(0x00FE, 90, 400)
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 18440, 0, 7500, 2000, 0x00)
    ChrWalkTo(0x00FE, 19630, 0, 8710, 2000, 0x00)
    ChrWalkTo(0x00FE, 24950, 0, 8780, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x0014 offset: 0x60E5
@scena.Code('func_14_60E5')
def func_14_60E5():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼工具并排摆在架子上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
