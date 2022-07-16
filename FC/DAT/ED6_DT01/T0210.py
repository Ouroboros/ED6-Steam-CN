import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0210   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '克劳斯市长'),
    TXT(0x02, '米蕾奴夫人'),
    TXT(0x03, '玲达'),
    TXT(0x04, '乔丝特'),
    TXT(0x05, '雪拉扎德'),
    TXT(0x06, '目标用摄像机'),
    TXT(0x07, '树叶'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0210.x'
    header.mapIndex       = 12
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x618B
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00001770,
            dword_04        = 0x00000000,
            dword_08        = 0x0002CEC0,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 12,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00001770,
            dword_04        = 0x00000000,
            dword_08        = 0x0002CEC0,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 45,
            word_34         = 45,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 12,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02330._CH', 'ED6_DT07/CH02330P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH02353._CH', 'ED6_DT07/CH02353P._CP'),
        ('ED6_DT06/CH20034._CH', 'ED6_DT06/CH20034P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10002 offset: 0x12E
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 82247,
            z                   = 0,
            y                   = 2548,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 7138,
            z                   = 0,
            y                   = 64539,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 506,
            z                   = 0,
            y                   = -1811,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 81266,
            z                   = 0,
            y                   = 53214,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 138350,
            z                   = 50,
            y                   = -52070,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 851975,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x20E
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x20E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -6321,
            y           = 0,
            z           = -3741,
            range       = -3987,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE60E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
    )

# id: 0x10005 offset: 0x22E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 75880,
            triggerZ            = 0,
            triggerY            = 56920,
            triggerRange        = 500,
            actorX              = 75880,
            actorZ              = 700,
            actorY              = 56920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 138350,
            triggerZ            = 0,
            triggerY            = -52070,
            triggerRange        = 500,
            actorX              = 138350,
            actorZ              = 0,
            actorY              = -52070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 78710,
            triggerZ            = 0,
            triggerY            = 52510,
            triggerRange        = 1800,
            actorX              = 78710,
            actorZ              = 1000,
            actorY              = 52510,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 77520,
            triggerZ            = 0,
            triggerY            = 50360,
            triggerRange        = 500,
            actorX              = 77520,
            actorZ              = 900,
            actorY              = 50360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 82150,
            triggerZ            = 0,
            triggerY            = 50830,
            triggerRange        = 500,
            actorX              = 82150,
            actorZ              = 1200,
            actorY              = 50830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 82490,
            triggerZ            = 310,
            triggerY            = 57230,
            triggerRange        = 500,
            actorX              = 82490,
            actorZ              = 1200,
            actorY              = 57230,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 78330,
            triggerZ            = 0,
            triggerY            = 57050,
            triggerRange        = 500,
            actorX              = 78330,
            actorZ              = 500,
            actorY              = 57050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 84700,
            triggerZ            = 0,
            triggerY            = 55320,
            triggerRange        = 500,
            actorX              = 84700,
            actorZ              = 500,
            actorY              = 55320,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x34E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_37F',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 200010, 0, 44420, 270)
    SetChrPos(0x000A, 201860, 0, 1360, 90)

    Jump('loc_42E')

    def _loc_37F(): pass

    label('loc_37F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_3B0',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 200010, 0, 44420, 270)
    SetChrPos(0x000A, 201860, 0, 1360, 90)

    Jump('loc_42E')

    def _loc_3B0(): pass

    label('loc_3B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_3C9',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)

    Jump('loc_42E')

    def _loc_3C9(): pass

    label('loc_3C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_3D8',
    )

    ClearChrFlags(0x0009, 0x0080)

    Jump('loc_42E')

    def _loc_3D8(): pass

    label('loc_3D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_409',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 201700, 0, 43930, 90)
    SetChrPos(0x000A, 7130, 0, 64540, 0)

    Jump('loc_42E')

    def _loc_409(): pass

    label('loc_409')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_422',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0008)

    Jump('loc_42E')

    def _loc_422(): pass

    label('loc_422')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_42E',
    )

    ClearChrFlags(0x0009, 0x0080)

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_486',
    )

    TerminateThread(0x0008, 0xFF)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x0008, 7150, 200, -3320, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_486',
    )

    SetChrPos(0x000C, 5410, 0, -3320, 90)
    ClearChrFlags(0x000C, 0x0080)

    def _loc_486(): pass

    label('loc_486')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000070, 'loc_49E'),
        (0x00000073, 'loc_4F0'),
        (0x00000064, 'loc_517'),
        (0x00000001, 'loc_55F'),
        (-1, 'loc_5DB'),
    )

    def _loc_49E(): pass

    label('loc_49E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C9',
    )

    SetScenaFlags(ScenaFlag(0x0049, 7, 0x24F))
    OP_28(0x0003, 0x01, 0x0200)
    OP_28(0x0003, 0x04, 0x10)
    OP_28(0x0004, 0x04, 0x40)
    OP_28(0x0006, 0x04, 0x40)
    Event(0, 0x0012)

    Jump('loc_4ED')

    def _loc_4C9(): pass

    label('loc_4C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4ED',
    )

    SetChrPos(0x0000, 84098, 0, 52559, 270)
    OP_69(0x0000, 0)

    def _loc_4ED(): pass

    label('loc_4ED')

    Jump('loc_5DB')

    def _loc_4F0(): pass

    label('loc_4F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_514',
    )

    SetChrPos(0x0000, 75765, 0, 54963, 90)
    OP_69(0x0000, 0)

    def _loc_514(): pass

    label('loc_514')

    Jump('loc_5DB')

    def _loc_517(): pass

    label('loc_517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 2, 0x23A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 3, 0x23B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_55C',
    )

    EventBegin(0x00)
    SetChrPos(0x0101, -5800, 0, -3300, 0)
    SetChrPos(0x0102, -4800, 0, -3300, 0)
    SetChrPos(0x0008, -1180, 1750, 3000, 0)
    Event(0, 0x0016)

    def _loc_55C(): pass

    label('loc_55C')

    Jump('loc_5DB')

    def _loc_55F(): pass

    label('loc_55F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5D8',
    )

    SetChrPos(0x0101, 81771, 0, 55487, 0)
    SetChrPos(0x0102, 81444, 0, 54476, 0)
    SetChrPos(0x0008, 83000, 0, 53344, 0)
    SetChrPos(0x000C, 81266, 0, 53214, 0)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x004B, 2, 0x25A))
    OP_28(0x001A, 0x04, 0x04)
    OP_28(0x001A, 0x01, 0x0001)
    OP_28(0x001A, 0x01, 0x0002)
    ClearChrFlags(0x000C, 0x0080)
    OP_69(0x0101, 0)
    Event(0, 0x0010)

    def _loc_5D8(): pass

    label('loc_5D8')

    Jump('loc_5DB')

    def _loc_5DB(): pass

    label('loc_5DB')

    Return()

# id: 0x0001 offset: 0x5DC
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F4',
    )

    OP_B1('t0210_y')

    Jump('loc_5FD')

    def _loc_5F4(): pass

    label('loc_5F4')

    OP_B1('t0210_n')

    def _loc_5FD(): pass

    label('loc_5FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_614',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)

    Jump('loc_62C')

    def _loc_614(): pass

    label('loc_614')

    ClearChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 6, 0x25E)),
            Expr.Return,
        ),
        'loc_627',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_62C')

    def _loc_627(): pass

    label('loc_627')

    ClearChrFlags(0x000E, 0x0080)

    def _loc_62C(): pass

    label('loc_62C')

    If(
        (
            (Expr.PushValueByIndex, 0x1),
            (Expr.PushLong, 0x51),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_64A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_64A(): pass

    label('loc_64A')

    Return()

# id: 0x0002 offset: 0x64B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_660',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_660(): pass

    label('loc_660')

    Return()

# id: 0x0003 offset: 0x661
@scena.Code('func_03_661')
def func_03_661():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_9FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_988',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0340020112V#600F喔，是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340020113V#600F这次真的是给你们添了很多麻烦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020114V#014F不，请别这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020115V#015F而且我们最后还是让犯人逃走了，\n',
            '真是感到抱歉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0340020116V#601F没事没事，\n',
            '你们能够平安无事，结晶又能拿回来，\n',
            '对我来说这样已经足够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340020117V#600F我听说柏斯地区\n',
            '最近好像有一群空贼在四处作案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020118V#009F嗯嗯，好像是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020119V而且那些犯人居然会开飞艇，\n',
            '让他们逃走了我真是不甘心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0340020120V#601F哈哈，竟然还有飞艇，\n',
            '这样你们行动的时候要更加小心才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340020121V#602F不过，说起来柏斯\n',
            '最近发生了一宗定期船失踪事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340020122V详细的情况我也不是很清楚，\n',
            '不过，现在王国军应该在调查吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020123V#003F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0340020124V#603F继续任由空贼作乱下去也不是办法啊。\n',
            '是不是该和柏斯的市长联系一下呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9FA')

    def _loc_988(): pass

    label('loc_988')

    ChrTalk(
        0x00FE,
        (
            '#0340020125V#602F我也在担心定期船失踪这件事。\n',
            '这样继续任由空贼作乱也不行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340020126V试试和柏斯的市长联系一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9FA(): pass

    label('loc_9FA')

    Jump('loc_1220')

    def _loc_9FD(): pass

    label('loc_9FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_AF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A9B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0340011128V#600F想不到我不在期间居然发生了这种事……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340011129V调查事宜我已经委托给协会了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340011130V麻烦你们了，\n',
            '这件事都靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF4')

    def _loc_A9B(): pass

    label('loc_A9B')

    ChrTalk(
        0x00FE,
        (
            '#0340011131V#600F调查事宜我已经委托给协会了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340011132V麻烦你们了，\n',
            '这件事都靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF4(): pass

    label('loc_AF4')

    Jump('loc_1220')

    def _loc_AF7(): pass

    label('loc_AF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Return,
        ),
        'loc_B66',
    )

    ChrTalk(
        0x00FE,
        (
            '#0340011045V#600F我回来的时候\n',
            '就看到家里已经变成这个样子了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340011046V连犯人的影子我也没有看见。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1220')

    def _loc_B66(): pass

    label('loc_B66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_C48',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C0A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0340010387V#600F你们俩都做得很好，\n',
            '把结晶平安送来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010388V听说你们最近也相当活跃啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010389V希望你们今后也在协会的工作中大展身手。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C45')

    def _loc_C0A(): pass

    label('loc_C0A')

    ChrTalk(
        0x00FE,
        (
            '#0340010390V#600F希望你们今后也在协会的工作中大展身手。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C45(): pass

    label('loc_C45')

    Jump('loc_1220')

    def _loc_C48(): pass

    label('loc_C48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 3, 0x23B)),
            Expr.Return,
        ),
        'loc_D06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CB1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0340010063V#600F矿山就在洛连特北部，\n',
            '玛鲁加山道的尽头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010064V离这儿也不是太远。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D03')

    def _loc_CB1(): pass

    label('loc_CB1')

    ChrTalk(
        0x00FE,
        (
            '#0340010065V#600F只要你们出示介绍信，\n',
            '应该就能够进入矿山了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010066V拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D03(): pass

    label('loc_D03')

    Jump('loc_1220')

    def _loc_D06(): pass

    label('loc_D06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_D7B',
    )

    ChrTalk(
        0x0008,
        (
            '#0340001635V#600F玛鲁加的新矿脉中\n',
            '似乎发现了了不起的东西呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340001636V我已经委托游击士协会负责运送了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1220')

    def _loc_D7B(): pass

    label('loc_D7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_DF0',
    )

    ChrTalk(
        0x00FE,
        (
            '#0340001311V#600F听说北边的玛鲁加矿山\n',
            '发现了新矿脉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340001312V听说是条很有潜力的矿脉，\n',
            '真是令人振奋的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1220')

    def _loc_DF0(): pass

    label('loc_DF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_EEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EAD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0340001058V#600F百日战役之后，\n',
            '利贝尔王国复兴的速度非常之惊人。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340001059V和帝国的邦交正常化\n',
            '促进了导力技术和贸易的发展……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340001060V艾莉茜雅女王执政方针非常正确。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EEB')

    def _loc_EAD(): pass

    label('loc_EAD')

    ChrTalk(
        0x0008,
        (
            '#0340001061V#600F呵呵……\n',
            '艾莉茜雅女王执政方针非常正确啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EEB(): pass

    label('loc_EEB')

    Jump('loc_1220')

    def _loc_EEE(): pass

    label('loc_EEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1029',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FC9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0340000384V#600F洛连特和其他的都市相比较而言\n',
            '的确是个相当平凡的乡间小镇。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340000385V但是我个人却很喜欢这里。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340000386V洛连特的人们非常纯朴善良。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340000387V我认为这种朴实的民风非常的珍贵呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1026')

    def _loc_FC9(): pass

    label('loc_FC9')

    ChrTalk(
        0x0008,
        (
            '#0340000388V#600F洛连特的人们非常纯朴善良。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340000389V我认为这种朴实的民风非常的珍贵呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1026(): pass

    label('loc_1026')

    Jump('loc_1220')

    def _loc_1029(): pass

    label('loc_1029')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11A5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0340000222V#600F哦，早上好啊。\n',
            '是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000223V#000F早上好啊，市长爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000224V#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340000225V#600F我听到了关于你们俩的传闻了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340000226V马上就要接受游击士研修训练了吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340000227V#601F你们这样的年轻人能够以成为游击士为志向，\n',
            '保护大家的安全，真是非常好啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340000228V我很期待你们的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000229V#000F嗯，我们会加油的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1220')

    def _loc_11A5(): pass

    label('loc_11A5')

    ChrTalk(
        0x0008,
        (
            '#0340000230V#601F你们这样的年轻人能够以成为游击士为志向，\n',
            '保护大家的安全，真是非常好啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340000231V我很期待你们的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1220(): pass

    label('loc_1220')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x1224
@scena.Code('func_04_1224')
def func_04_1224():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_12D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12AB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '家里遭到了打劫，\n',
            '但幸好谁也没有受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当时一想到那些人\n',
            '会不会对老伴和玲达做些什么，\n',
            '我就非常担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D6')

    def _loc_12AB(): pass

    label('loc_12AB')

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔、约修亚，\n',
            '真的十分感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D6(): pass

    label('loc_12D6')

    Jump('loc_1AF1')

    def _loc_12D9(): pass

    label('loc_12D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_133C',
    )

    ChrTalk(
        0x00FE,
        (
            '#1020011063V那些人走的时候\n',
            '好像还拿了好几包吃的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020011064V难道他们当时也很饿了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF1')

    def _loc_133C(): pass

    label('loc_133C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Return,
        ),
        'loc_155D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 4, 0x25C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1501',
    )

    EventBegin(0x00)
    OP_69(0x0009, 1000)
    SetScenaFlags(ScenaFlag(0x004B, 4, 0x25C))
    OP_28(0x001A, 0x01, 0x0020)

    ChrTalk(
        0x0101,
        (
            '#0010011056V#002F米蕾奴婶婶，您没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1020011057V嗯，不用担心。\n',
            '我没有受到粗暴对待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011058V#012F请问市长夫人，关于那些犯人，\n',
            '您有没有注意到什么特别的事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1020011059V因为那些人都蒙着面，\n',
            '所以没办法分辨他们的面部特征……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1020011060V而且我记得很清楚，\n',
            '家里大门明明锁得好好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1020011061V老伴去了教会，家里只留下两个女人，\n',
            '锁上大门也是为了保险起见嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1020011062V那些人到底是从\n',
            '什么地方进来的呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_155A')

    def _loc_1501(): pass

    label('loc_1501')

    ChrTalk(
        0x0009,
        (
            '#1020011063V那些人走的时候\n',
            '好像还拿了好几包吃的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1020011064V难道他们当时也很饿了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_155A(): pass

    label('loc_155A')

    Jump('loc_1AF1')

    def _loc_155D(): pass

    label('loc_155D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1660',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_160F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '听说你们受我丈夫之托，\n',
            '要去办一件事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们俩这么年轻就这么能干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说卡西乌斯出差了，\n',
            '不过有你们俩在这里的话，\n',
            '洛连特的市民也安心很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_165D')

    def _loc_160F(): pass

    label('loc_160F')

    ChrTalk(
        0x00FE,
        (
            '虽说卡西乌斯出差了，\n',
            '不过有你们俩在这里的话，\n',
            '洛连特的市民也安心很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_165D(): pass

    label('loc_165D')

    Jump('loc_1AF1')

    def _loc_1660(): pass

    label('loc_1660')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1733',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16E6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '玲达说，\n',
            '帕赛尔农场\n',
            '最近不能运送蔬菜过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的蔬菜真的很新鲜，\n',
            '好吃极了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1730')

    def _loc_16E6(): pass

    label('loc_16E6')

    ChrTalk(
        0x00FE,
        (
            '玲达说，\n',
            '帕赛尔农场\n',
            '最近不能运送蔬菜过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1730(): pass

    label('loc_1730')

    Jump('loc_1AF1')

    def _loc_1733(): pass

    label('loc_1733')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_182C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17C8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我们儿子\n',
            '在卢安附近的\n',
            '杰尼丝王立学院那里教书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从儿子走了以后\n',
            '总觉得家里空荡荡的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '真是有些寂寞呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1829')

    def _loc_17C8(): pass

    label('loc_17C8')

    ChrTalk(
        0x00FE,
        (
            '我们儿子\n',
            '在卢安附近的\n',
            '杰尼丝王立学院那里教书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从儿子走了以后\n',
            '总觉得家里空荡荡的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1829(): pass

    label('loc_1829')

    Jump('loc_1AF1')

    def _loc_182C(): pass

    label('loc_182C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1915',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18C4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '对了，是不是该叫玲达过来\n',
            '和我一起准备晚餐了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我想，\n',
            '今天就给老伴儿做\n',
            '他喜欢的罗宋汤吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我先去和玲达商量一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1912')

    def _loc_18C4(): pass

    label('loc_18C4')

    ChrTalk(
        0x0009,
        (
            '我想，\n',
            '今天就给老伴儿做\n',
            '他喜欢的罗宋汤吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我先去和玲达商量一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1912(): pass

    label('loc_1912')

    Jump('loc_1AF1')

    def _loc_1915(): pass

    label('loc_1915')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1A37',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19E4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '玲达把所有的家务活\n',
            '都包揽了下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像不干点什么\n',
            '就镇静不下来一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '肯定是因为她来我们家之前\n',
            '就天天习惯于干家务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果让她休息一会儿的话，\n',
            '她反而会不知所措吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A34')

    def _loc_19E4(): pass

    label('loc_19E4')

    ChrTalk(
        0x0009,
        (
            '玲达把所有的家务活\n',
            '都包揽了下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像不干点什么\n',
            '就镇静不下来一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A34(): pass

    label('loc_1A34')

    Jump('loc_1AF1')

    def _loc_1A37(): pass

    label('loc_1A37')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AC8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0101,
        (
            '#000F米蕾奴婶婶，\n',
            '早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哎呀，早上好。\n',
            '艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们一大早就出门了？\n',
            '真是辛苦了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF1')

    def _loc_1AC8(): pass

    label('loc_1AC8')

    ChrTalk(
        0x0009,
        (
            '你们一大早就出门了？\n',
            '真是辛苦了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF1(): pass

    label('loc_1AF1')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0x1AF5
@scena.Code('func_05_1AF5')
def func_05_1AF5():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1BC2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B77',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '终于把乱糟糟的书房\n',
            '给打扫干净了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可是每天都把这里弄得干干净净的，\n',
            '不能饶恕那些家伙，哼哼哼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BBF')

    def _loc_1B77(): pass

    label('loc_1B77')

    ChrTalk(
        0x00FE,
        (
            '要是我看到那些犯人，\n',
            '一定要用抹布抽他们的脸，\n',
            '用扫帚打他们一顿～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BBF(): pass

    label('loc_1BBF')

    Jump('loc_2179')

    def _loc_1BC2(): pass

    label('loc_1BC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Return,
        ),
        'loc_1DAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 3, 0x25B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D2C',
    )

    EventBegin(0x00)
    OP_69(0x000A, 1000)
    SetScenaFlags(ScenaFlag(0x004B, 3, 0x25B))
    OP_28(0x001A, 0x01, 0x0010)

    ChrTalk(
        0x000A,
        (
            '#1010011047V真是的！吓死我了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1010011048V当时我在阁楼打扫卫生，\n',
            '突然有一群蒙面的男人\n',
            '闯了进来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011049V#002F一群蒙面的男人……\n',
            '也就是说，犯人不止一个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011050V#012F是几个人的团伙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1010011051V让我想想……\n',
            '大概有三、四个人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1010011052V啊，说起来，\n',
            '其中有一个人的个子比较矮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1010011053V说不定是女的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_1DAC')

    def _loc_1D2C(): pass

    label('loc_1D2C')

    ChrTalk(
        0x000A,
        (
            '#1010011054V前几天好不容易把书房打扫干净，\n',
            '现在又搞得乱糟糟的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1010011055V要是你们抓到那些犯人，\n',
            '一定要给我好好教训他们才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DAC(): pass

    label('loc_1DAC')

    Jump('loc_2179')

    def _loc_1DAF(): pass

    label('loc_1DAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1EBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E5A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '接下来得打扫阁楼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的房间暗暗的，\n',
            '还时不时有老鼠蹿出来，\n',
            '有点紧张呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鬼我倒是不怕，\n',
            '但老鼠实在是很讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EB7')

    def _loc_1E5A(): pass

    label('loc_1E5A')

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '接下来得打扫阁楼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的房间暗暗的，\n',
            '还时不时有老鼠蹿出来，\n',
            '有点紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EB7(): pass

    label('loc_1EB7')

    Jump('loc_2179')

    def _loc_1EBA(): pass

    label('loc_1EBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Return,
        ),
        'loc_1F12',
    )

    ChrTalk(
        0x00FE,
        (
            '现在书房里\n',
            '有一位客人来访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果找市长有事的话，\n',
            '就请轻轻地进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2179')

    def _loc_1F12(): pass

    label('loc_1F12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1F7E',
    )

    ChrTalk(
        0x00FE,
        (
            '帕赛尔农场\n',
            '终于又开始供应蔬菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过今年的\n',
            '气候也并不坏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是发生什么事了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2179')

    def _loc_1F7E(): pass

    label('loc_1F7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1F88',
    )

    Jump('loc_2179')

    def _loc_1F88(): pass

    label('loc_1F88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1FD1',
    )

    ChrTalk(
        0x000A,
        (
            '啊……\n',
            '今天要准备哪些菜式呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我得去和夫人商量一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2179')

    def _loc_1FD1(): pass

    label('loc_1FD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_20B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2071',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000A,
        (
            '夫人还来帮助我，\n',
            '和我一起工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就像对待自己\n',
            '家里的亲人一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '之前还无论如何\n',
            '也要我和他们一起用餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我真是太感动了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20B2')

    def _loc_2071(): pass

    label('loc_2071')

    ChrTalk(
        0x000A,
        (
            '夫人对我就像对待\n',
            '自己家里的亲人一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我真是太感动了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20B2(): pass

    label('loc_20B2')

    Jump('loc_2179')

    def _loc_20B5(): pass

    label('loc_20B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2146',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '呼呼，忙死了忙死了。\n',
            '这个屋子实在是太大了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '要做的杂务有扫除和洗涤，\n',
            '早晨真是女佣最忙的时间啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2179')

    def _loc_2146(): pass

    label('loc_2146')

    ChrTalk(
        0x000A,
        (
            '目标～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '在夫人从教会\n',
            '回来之前完成扫除！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2179(): pass

    label('loc_2179')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x217D
@scena.Code('func_06_217D')
def func_06_217D():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 5, 0x25D)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 4, 0x25C)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 3, 0x25B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 0, 0x260)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 6, 0x25E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 7, 0x25F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F84',
    )

    EventBegin(0x00)

    ChrTalk(
        0x000C,
        (
            '#0030011085V#020F刚才我已经向市长\n',
            '了解整件案件的详细经过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011086V#020F你们那边有什么收获吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '『还要再仔细调查一下才行』\n'),
            TXT(0x01, '『嗯，已经找到很多的线索』\n'),
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
        (0x00000001, 'loc_228A'),
        (0x00000000, 'loc_2F37'),
        (-1, 'loc_2F81'),
    )

    def _loc_228A(): pass

    label('loc_228A')

    ClearMapFlags(0x00000001)
    Fade(1000)
    SetChrPos(0x0101, 4720, 0, -2800, 90)
    SetChrPos(0x0102, 5720, 0, -3920, 0)
    SetChrPos(0x000C, 6370, 0, -2250, 225)
    CameraMove(6020, 0, -2610, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0030011088V#020F那么……\n',
            '我们就一项一项来确认吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011089V#020F首先，犯人的目的是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【可以换成米拉的东西】\n'),
            TXT(0x01, '【保险箱里的七耀石】\n'),
            TXT(0x02, '【厨房里的食物】\n'),
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
        (0x00000000, 'loc_23CA'),
        (0x00000001, 'loc_23DB'),
        (0x00000002, 'loc_23EC'),
        (-1, 'loc_23FD'),
    )

    def _loc_23CA(): pass

    label('loc_23CA')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_23FD')

    def _loc_23DB(): pass

    label('loc_23DB')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_23FD')

    def _loc_23EC(): pass

    label('loc_23EC')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_23FD')

    def _loc_23FD(): pass

    label('loc_23FD')

    ChrTalk(
        0x000C,
        (
            '#0030011090V#020F犯人的规模是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【男女二人组】\n'),
            TXT(0x01, '【３～４人的团伙】\n'),
            TXT(0x02, '【女性的独犯】\n'),
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
        (0x00000000, 'loc_24A3'),
        (0x00000001, 'loc_24B4'),
        (0x00000002, 'loc_24C5'),
        (-1, 'loc_24D6'),
    )

    def _loc_24A3(): pass

    label('loc_24A3')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_24D6')

    def _loc_24B4(): pass

    label('loc_24B4')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_24D6')

    def _loc_24C5(): pass

    label('loc_24C5')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_24D6')

    def _loc_24D6(): pass

    label('loc_24D6')

    ChrTalk(
        0x000C,
        (
            '#0030011091V#020F犯人是怎么进来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【从一楼的窗户跳进来】\n'),
            TXT(0x01, '【撬开大门的锁冲进来】\n'),
            TXT(0x02, '【从二楼的阳台爬进来】\n'),
            TXT(0x03, '【从屋顶的阁楼闯进来】\n'),
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
        (0x00000000, 'loc_25AF'),
        (0x00000001, 'loc_25C0'),
        (0x00000002, 'loc_25C3'),
        (0x00000003, 'loc_25D4'),
        (-1, 'loc_25D7'),
    )

    def _loc_25AF(): pass

    label('loc_25AF')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_25D7')

    def _loc_25C0(): pass

    label('loc_25C0')

    Jump('loc_25D7')

    def _loc_25C3(): pass

    label('loc_25C3')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_25D7')

    def _loc_25D4(): pass

    label('loc_25D4')

    Jump('loc_25D7')

    def _loc_25D7(): pass

    label('loc_25D7')

    ChrTalk(
        0x000C,
        (
            '#0030011092V#020F那么，你觉得和这次案件\n',
            '有嫌疑的应该是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【平时进出的市民】\n'),
            TXT(0x01, '【克劳斯市长的家人】\n'),
            TXT(0x02, '【玛鲁加矿山的见习矿工】\n'),
            TXT(0x03, '【最近来访的旅行者】\n'),
            TXT(0x04, '【以上所列的人都不是】\n'),
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
        (0x00000000, 'loc_26E0'),
        (0x00000001, 'loc_26F1'),
        (0x00000002, 'loc_2702'),
        (0x00000003, 'loc_2713'),
        (0x00000004, 'loc_2724'),
        (-1, 'loc_2727'),
    )

    def _loc_26E0(): pass

    label('loc_26E0')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2727')

    def _loc_26F1(): pass

    label('loc_26F1')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2727')

    def _loc_2702(): pass

    label('loc_2702')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2727')

    def _loc_2713(): pass

    label('loc_2713')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2727')

    def _loc_2724(): pass

    label('loc_2724')

    Jump('loc_2727')

    def _loc_2727(): pass

    label('loc_2727')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2787',
    )

    OP_2B(0x001A, 0x0004)
    OP_28(0x001A, 0x01, 0x8000)

    ChrTalk(
        0x000C,
        (
            '#0030011093V#021F呵呵～调查得相当不错。\n',
            '这样就可以确定犯人的身份了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2847')

    def _loc_2787(): pass

    label('loc_2787')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Leq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27F5',
    )

    OP_2B(0x001A, 0x0002)
    OP_28(0x001A, 0x01, 0x4000)

    ChrTalk(
        0x000C,
        (
            '#0030011094V#020F嗯，这些线索也有参考价值。\n',
            '这样就可以确定犯人的身份了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2847')

    def _loc_27F5(): pass

    label('loc_27F5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2847',
    )

    OP_28(0x001A, 0x01, 0x2000)

    ChrTalk(
        0x000C,
        (
            '#0030011095V#025F这些线索都互不相关，\n',
            '不太好确定犯人的身份呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2847(): pass

    label('loc_2847')

    ChrTurnDirection(0x000C, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x000C,
        (
            '#0030011096V#022F……市长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011097V#022F请您回忆一下最近几天，\n',
            '有没有刚认识的人到过书房？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340011098V#604F让我想想。\n',
            '有好几个人呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340011099V杂志社的两位记者也来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011100V#000F怎么，\n',
            '他们两个也来拜访过市长先生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011101V#012F案发当时，\n',
            '那两位记者和我们一起去了『翡翠之塔』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011102V#012F我想应该可以排除在嫌疑犯之外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030011103V#020F原来如此……\n',
            '市长，除此之外还有其他人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340011104V#600F除此之外……\n',
            '就只有乔丝特了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340011105V#601F哈哈哈，不过不可能吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011106V#001F啊哈哈，那也是。\n',
            '那孩子不可能是犯人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011107V#001F怎么说也是王立学院的学生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000C, 225, 400)

    ChrTalk(
        0x000C,
        (
            '#0030011108V#022F并不是所有犯人都会\n',
            '让人一眼就看出来的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011109V#022F校服什么的，\n',
            '这种东西要做出复制品来也不是什么难事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011110V#000F可是，她真的是很乖的孩子呢，\n',
            '又讲礼貌又像大小姐的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011111V#001F对吧，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0102)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020011112V#015F很不巧，我的看法正好相反。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011113V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011114V#012F那时——\n',
            '市长正在把七耀石放进保险箱的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011115V#012F那孩子的眼神就像\n',
            '猎人盯着猎物一样锐利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011116V#012F当时没有确实的证据，\n',
            '而且也没办法当面去问她……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011117V#012F不过，至少在我看来，\n',
            '她并不是什么单纯的女学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011118V#003F不、不会吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340011119V#602F真是难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030011120V#022F无论如何，\n',
            '看来有必要找那女孩问话才行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011121V#022F你们知道那女孩现在在哪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 0)
    Sleep(300)

    ChrTurnDirection(0x0102, 0x000C, 0)

    ChrTalk(
        0x0101,
        (
            '#0010011122V#002F这个嘛～\n',
            '应该是住在旅馆的吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011123V#002F不过她说过\n',
            '今天就要离开洛连特了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030011124V#026F嗯，看来要赶快才行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011125V#024F艾丝蒂尔、约修亚。\n',
            '我们马上去旅馆看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011126V#002F嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011127V#012F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E97')
    def lambda_2E97():
        OP_92(0x00FE, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_2E97)

    SetChrFlags(0x000C, 0x0040)
    OP_92(0x000C, 0x0000, 0, 3000, 0x00)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0008)
    SetScenaFlags(ScenaFlag(0x004C, 1, 0x261))
    OP_28(0x001A, 0x01, 0x0200)
    OP_28(0x001B, 0x04, 0x04)
    OP_28(0x001B, 0x01, 0x0001)
    OP_28(0x001B, 0x01, 0x0002)
    OP_20(0x000005DC)
    EventEnd(0x00)
    SetChrStatus(0x0002, 0x00, 12)
    OP_B5(0x0002, 0x00)
    OP_B5(0x0002, 0x01)
    OP_B5(0x0002, 0x05)
    OP_B5(0x0002, 0x04)
    EquipCmd(0x02, 0x003D)
    EquipCmd(0x02, 0x00F2)
    EquipCmd(0x02, 0x0110)
    EquipCmd(0x02, 0x026D, 0x00)
    EquipCmd(0x02, 0x026A, 0x01)
    EquipCmd(0x02, 0x025E, 0x05)
    EquipCmd(0x02, 0x0267, 0x04)
    AddCraft(0x0002, 0x00AA)
    AddSCraft(0x0002, 0x00F0)
    FormationAddMember(0x02, 0xFF)
    ClearMapFlags(0x00000800)
    OP_21()

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1E()

    Jump('loc_2F81')

    def _loc_2F37(): pass

    label('loc_2F37')

    ChrTalk(
        0x000C,
        (
            '#0030011087V#020F我就说要你们去调查嘛。\n',
            '不过，你们动作要快点才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_2F81')

    def _loc_2F81(): pass

    label('loc_2F81')

    Jump('loc_2FFE')

    def _loc_2F84(): pass

    label('loc_2F84')

    ChrTalk(
        0x000C,
        (
            '#0030011083V#020F哎呀，这么快就调查完了？\n',
            '好像太早了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011084V#020F再认真调查一下吧。\n',
            '说不定有些地方你们还没有调查哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2FFE(): pass

    label('loc_2FFE')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0x3002
@scena.Code('func_07_3002')
def func_07_3002():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 5, 0x25D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36F3',
    )

    Fade(1000)
    SetChrPos(0x0101, 75500, 0, 55990, 0)
    SetChrPos(0x0102, 76250, 0, 55794, 315)
    CameraMove(76000, 0, 56380, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010010996V#007F#3P啊～给女王的礼物就这样……\n',
            '那可是我们辛苦送回来的东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010997V#005F那些可恶的犯人～绝对不能饶恕！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010998V#012F#4P这里看起来……\n',
            '箱门并没有被破坏的痕迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010999V#012F难道是解开密码后打开的，\n',
            '还是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011000V#004F#3P解开密码？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020011001V#012F#4P嗯，这并不是不可能。\n',
            '但是没有专业技术的话很难办到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011002V#012F我想犯人应该是\n',
            '通过更简单的方法得知密码的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011003V#002F#3P更简单的方法……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011004V#013F#4P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011005V#012F比如说，\n',
            '将一种特殊的粉末洒在保险箱的每个按钮上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011006V#012F那种粉末有极强的吸附性，\n',
            '而且颗粒很小肉眼看不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011007V#012F不过，用蓝色的光照射就会发光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011008V#002F#3P嗯嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011009V#015F#4P犯人先洒上那种粉末，\n',
            '然后趁机让市长去输入密码。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011010V#015F被按到的按钮上的粉末\n',
            '就自然会被手指沾掉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011011V#015F这样就不难得知\n',
            '市长按了哪几个按钮了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011012V#004F#3P等一下。\n',
            '这样不就不能知道顺序吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011013V#012F#4P不，这也不一定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011014V#012F手指上沾到的粉末越多，\n',
            '从按钮上沾掉的粉末就会变少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011015V#012F也就是说，\n',
            '从发光量少的按钮开始按就对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011016V#012F如果数字有重复的话会比较麻烦，\n',
            '不过还是可以推断出大致的数字来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011017V#501F#3P哦……我明白了。\n',
            '约修亚，你真是个天才啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011018V#015F#4P这些都只是基础常识啊。\n',
            '总之，先调查一下按钮吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_353B')
    def lambda_353B():
        CameraMove(77550, 0, 56660, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_353B)

    ChrWalkTo(0x0102, 77450, 0, 56040, 2000, 0x00)
    ChrWalkTo(0x0102, 77260, 0, 56973, 2000, 0x00)
    SetChrDirection(0x0102, 225, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrWalkTo(0x0101, 77030, 0, 55790, 2000, 0x00)
    ChrWalkTo(0x0101, 77720, 0, 56410, 2000, 0x00)
    SetChrDirection(0x0101, 270, 400)
    Sleep(2000)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020011019V#012F#3P……果然是那种粉末。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011020V#012F犯人肯定是用我刚才说的方法\n',
            '打开保险箱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011021V#006F#4P是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011022V#006F那现在的问题是，\n',
            '究竟是谁把粉末洒上去的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011023V#006F我想至少应该是\n',
            '进过这间屋子的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011024V#012F#3P是啊……那才是破案的关键。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x004B, 5, 0x25D))
    OP_28(0x001A, 0x01, 0x0004)
    OP_28(0x001A, 0x01, 0x0008)
    EventEnd(0x00)

    Jump('loc_3748')

    def _loc_36F3(): pass

    label('loc_36F3')

    ChrTalk(
        0x0102,
        (
            '#0020011025V#010F既然知道犯人是如何打开保险箱的了，\n',
            '那我们再到其他地方调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    def _loc_3748(): pass

    label('loc_3748')

    Return()

# id: 0x0008 offset: 0x3749
@scena.Code('func_08_3749')
def func_08_3749():
    SetMapFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_375D',
    )

    Jump('loc_3948')

    def _loc_375D(): pass

    label('loc_375D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 4, 0x25C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37BE',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0102,
        (
            '#0020011077V#012F艾丝蒂尔。\n',
            '我们还是先在屋里调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_3948')

    def _loc_37BE(): pass

    label('loc_37BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 7, 0x25F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38CE',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -5150, 0, -3680, 180)
    SetChrPos(0x0102, -5810, 0, -2850, 180)
    CameraMove(-5150, 0, -2820, 1000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010011078V#002F案发当时，\n',
            '大门的确是锁着的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010011079V#002F可是门锁并没有被弄坏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011080V#012F也就是说……\n',
            '犯人是从别的地方进来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x004B, 7, 0x25F))
    OP_28(0x001A, 0x01, 0x0040)
    ChrMoveToRelative(0x0000, 0, 0, 1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_3948')

    def _loc_38CE(): pass

    label('loc_38CE')

    EventBegin(0x01)

    ChrTalk(
        0x0102,
        (
            '#0020011081V#012F看起来犯人当时\n',
            '并不是从大门进来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011082V#012F我们到其他地方调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3948(): pass

    label('loc_3948')

    ClearMapFlags(0x00000080)

    Return()

# id: 0x0009 offset: 0x394E
@scena.Code('func_09_394E')
def func_09_394E():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x004B, 6, 0x25E))
    OP_28(0x001A, 0x01, 0x0100)

    ChrTalk(
        0x0101,
        (
            '#0010011065V#004F啊，这个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrFlags(0x000E, 0x0080)
    FadeOut(300, 0, 100)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '塞尔贝树叶',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x032A, 1)
    ClearMapFlags(0x00000001)

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000D, 800)

    ChrTalk(
        0x0101,
        (
            '#0010011066V#505F这种地方竟然会有树叶，\n',
            '是不是有些奇怪呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011067V而且，\n',
            '这好像不是附近的树上长的叶子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011068V#010F真细心啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011069V#010F这个阁楼是当时\n',
            '市长夫人她们被囚禁的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011070V#010F这树叶有可能是\n',
            '从犯人身上掉下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011071V#006F这么说，是重要的物证呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x01, 0x0001)
    EventEnd(0x01)

    Return()

# id: 0x000A offset: 0x3B44
@scena.Code('func_0A_3B44')
def func_0A_3B44():
    EventBegin(0x00)
    CameraMove(78710, 0, 52510, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010011026V#002F哎呀呀～\n',
            '桌子被翻得乱七八糟的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011027V要是被玲达姐姐看见了\n',
            '她肯定会晕倒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011028V#012F而且书架上的书\n',
            '好像也被犯人弄散了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011029V犯人这样做究竟是为什么呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x000B offset: 0x3C16
@scena.Code('func_0B_3C16')
def func_0B_3C16():
    EventBegin(0x00)
    CameraMove(77520, 0, 50360, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010011039V#000F啊～\n',
            '抽屉里面有好几本书呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011040V不过并没有被翻过的痕迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011041V#012F嗯，好像都是些\n',
            '和洛连特的行政有关的文件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011042V这些东西没事，\n',
            '就说明犯人行事不是出于政治上的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x000C offset: 0x3CF1
@scena.Code('func_0C_3CF1')
def func_0C_3CF1():
    EventBegin(0x00)
    CameraMove(82150, 0, 50830, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010011030V#008F不愧是市长爷爷啊。\n',
            '竟然有这么多这么难懂的书～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011031V#012F好像也有好几本\n',
            '价值不菲的珍藏版呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011032V是犯人不知道它的价值呢，\n',
            '还是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x000D offset: 0x3DA5
@scena.Code('func_0D_3DA5')
def func_0D_3DA5():
    EventBegin(0x00)
    CameraMove(82490, 310, 57230, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010011033V#008F不愧是市长爷爷啊。\n',
            '竟然有这么多这么难懂的书～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011034V#012F好像也有好几本\n',
            '价值不菲的珍藏版呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011035V是犯人不知道它的价值呢，\n',
            '还是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x000E offset: 0x3E59
@scena.Code('func_0E_3E59')
def func_0E_3E59():
    EventBegin(0x00)
    CameraMove(78330, 0, 57050, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010011043V#000F这个罐子倒了……\n',
            '里面什么东西也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011044V#010F嗯……\n',
            '看起来只是被撞倒了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x000F offset: 0x3ED7
@scena.Code('func_0F_3ED7')
def func_0F_3ED7():
    EventBegin(0x00)
    CameraMove(84700, 0, 55320, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010011036V#002F这个是杂物箱吧……\n',
            '不过里面是空的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011037V#012F箱子盖上的锁像是\n',
            '被熔化了一样断开了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011038V说不定……\n',
            '是用导力枪打断的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x0010 offset: 0x3F81
@scena.Code('func_10_3F81')
def func_10_3F81():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000C, 0xFF)
    FadeIn(2000, 0)
    CameraSetDistance(2600, 0)
    CameraMove(82702, 0, 54610, 0)
    SetChrDirection(0x0101, 315, 0)
    SetChrDirection(0x0102, 270, 0)
    SetChrDirection(0x0008, 270, 0)
    SetChrDirection(0x000C, 225, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010010970V#004F哇～乱七八糟的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030010971V#023F搞成这个样子……\n',
            '犯人还真不是一般的粗暴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)
    SetChrDirection(0x000C, 270, 0)
    CameraMove(79224, 0, 54590, 1000)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrWalkTo(0x0101, 80262, 0, 55520, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010010972V#004F啊啊，保险箱……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010973V#603F……那块要送给女王的七耀石也被偷走了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010974V之前还特地让你们送过来，\n',
            '我真是太对不起大家了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 0)
    OP_69(0x0102, 800)

    ChrTalk(
        0x0102,
        (
            '#0020010975V#012F市长您没必要道歉啊。\n',
            '而且这根本不是您的错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010976V#012F对了……\n',
            '其他的房间情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010977V#602F其他的房间几乎没有被翻乱的痕迹。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010978V最多就是囚禁内人她们的\n',
            '阁楼房间稍稍有点乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030010979V#026F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010980V#026F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0102, 400)

    ChrTalk(
        0x000C,
        (
            '#0030010981V#022F艾丝蒂尔、约修亚。\n',
            '我想让你们两人办点事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 180, 400)
    ChrTurnDirection(0x0102, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010982V#002F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030010983V#022F我要向市长\n',
            '了解一下这案件的详细情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030010984V#022F在这段时间里，\n',
            '你们就在屋里调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010985V#004F啊，那就是……\n',
            '所谓的现场勘查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010986V#014F交给我们可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030010987V#020F正好人手足够，\n',
            '分头行动的话效率不是更高吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010988V#006F明白了。\n',
            '我们会努力去做的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030010989V#020F要慎重细致地调查才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0008, 400)

    ChrTalk(
        0x000C,
        (
            '#0030010990V#020F那么市长，\n',
            '我们去客厅谈吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000C, 400)

    ChrTalk(
        0x0008,
        (
            '#0340010991V#602F嗯，该从何说起呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 90, 400)
    CreateThread(0x0008, 0x01, 0x00, 0x0011)
    Sleep(500)

    ChrWalkTo(0x000C, 84500, 0, 53030, 2000, 0x00)
    SetChrFlags(0x000C, 0x0004)
    ChrWalkTo(0x000C, 87230, 0, 53030, 2000, 0x00)
    OP_72(0x0003, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0003, 9)
    OP_70(0x0003, 0)
    OP_73(0x0003)
    OP_71(0x0003, 0x0800)
    SetChrFlags(0x000C, 0x0080)
    SetChrPos(0x0008, 4994, 0, -8380, 315)
    SetChrPos(0x000C, 3173, 0, -5730, 135)

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000D, 800)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010992V#006F现场勘查啊……\n',
            '不禁感到有点紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010993V#012F我们就从这个房间开始调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010994V#012F而且还要向屋里的人\n',
            '听取案件发生时的证言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010995V#006F嗯，ＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    EventEnd(0x00)
    OP_21()
    SetMapFlags(0x00000800)
    PlayBGM(87)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0011 offset: 0x4608
@scena.Code('func_11_4608')
def func_11_4608():
    Sleep(100)

    ChrWalkTo(0x0008, 84500, 0, 53030, 2000, 0x00)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 9)
    OP_73(0x0003)
    SetChrFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, 87230, 0, 53030, 2000, 0x00)
    SetChrFlags(0x0008, 0x0080)

    Return()

# id: 0x0012 offset: 0x4651
@scena.Code('func_12_4651')
def func_12_4651():
    ClearChrFlags(0x000B, 0x0080)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000B, 0xFF)
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    SetMapFlags(0x00400000)
    CameraMove(80120, 0, 270, 0)
    CameraSetDistance(3000, 0)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x0008, 78100, 200, -950, 90)
    SetChrPos(0x000B, 80250, 0, -950, 270)
    SetChrPos(0x0101, 84060, 0, -150, 270)
    SetChrPos(0x0102, 84240, 0, -950, 270)
    FadeIn(2000, 0)
    OP_0D()

    NpcTalk(
        0x000B,
        '穿制服的少女',
        (
            '#0090010282V#217F原来如此……\n',
            '那个钟楼有这样一段逸事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010283V真是太让人感动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010284V#603F用语言来描述战争的悲惨会另有一番意义……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010285V更重要的是可以让人体会到\n',
            '化悲痛为力量、重建和平的那种坚强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0340010286V#604F…………哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0102, 0x01, 0x00, 0x0014)
    ChrWalkTo(0x0101, 81820, 0, 866, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010287V#000F#1P我们把那东西送回来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010288V#000F嗯，打扰你们了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010289V#601F哦，是艾丝蒂尔你们啊。\n',
            '怎么会打扰呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010290V#601F来得正好，我来介绍一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010291V#601F这位是乔丝特，\n',
            '杰尼丝王立学院的学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010292V#000F#1P杰尼丝王立学院……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000B, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010293V#010F我听说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010294V#010F是卢安地区的那所寄宿制高等院校吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090010295V#218F嗯，你说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010296V初次见面，\n',
            '我叫乔丝特·哈尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010297V#001F#1P我叫艾丝蒂尔。\n',
            '请多指教哦，乔丝特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010298V#010F我叫约修亚，请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010299V#600F其实他们俩是游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010300V因为我有点私人的事情，\n',
            '刚才拜托他们帮我处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0090010301V#217F游击士！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010302V就是传说中不屈服于任何权势，\n',
            '以爱好和平为荣耀的自由骑士吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010303V#218F啊啊，我太感动了！\n',
            '没想到能见到真正的游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010304V#008F#1P你、你这么感动，\n',
            '连我们都不好意思了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010305V#008F对了……\n',
            '啊，能叫你小乔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090010306V#218F嗯，没问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010307V#000F#1P小乔你为什么会来这里呢？\n',
            '和市长爷爷认识吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090010308V#217F不是的，\n',
            '其实今天是第一次见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010309V作为自主学习的一部分，\n',
            '我正在调查各地的重要文化遗产。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010310V明知市长身处百忙之中，\n',
            '还麻烦他抽出时间和我谈话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010311V#000F#1P嗯～真是刻苦学习啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010312V#000F那……我们有没有打扰你？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090010313V#217F没有呢，\n',
            '反正我要调查的东西都已经请教过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010314V#217F话说回来……\n',
            '我还呆在这里是不是不方便呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000B, 400)

    ChrTalk(
        0x0008,
        (
            '#0340010315V#600F不不，没这回事啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010316V#600F艾丝蒂尔，机会难得，\n',
            '让她也见识一下那东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010317V#006F#1P啊，好。\n',
            '不过先等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x0015)
    Sleep(500)

    ChrWalkTo(0x0102, 79910, 0, 380, 3000, 0x00)
    SetChrSubChip(0x0008, 1)
    SetChrDirection(0x0102, 225, 400)
    Sleep(1000)

    PlaySE(128, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 6)
    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0x00, 0x0101, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0090010318V#217F啊……！\n',
            '那个就是七耀石吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010319V#217F真是美丽的光芒啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010320V#601F嗯，大小正合适。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010321V很适合作为表达\n',
            '洛连特市民感激之情的礼物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010322V#004F#1P礼物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010323V#010F#2P表达感激之情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010324V#019F原来如此，是女王诞辰庆典的礼物吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010325V#601F真聪明啊，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010326V我打算用这个做成导力器工艺品，\n',
            '赠送给艾莉茜雅女王陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010327V向六十大寿的陛下\n',
            '表达我们洛连特市民的谢意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010328V#004F#1P啊啊，是送给女王的礼物！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090010329V#218F啊，真是太美妙了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010330V#600F我们利贝尔的国民，\n',
            '一直以来受到女王陛下许多恩惠。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010331V今天能够如此方便地乘坐\n',
            '定期飞船也是由于王家的资助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010332V#010F#2P听说利贝尔国内的游击士协会\n',
            '也同样得到了王家许多方面的援助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010333V#010F确实……\n',
            '在各个方面都受到了恩惠啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010334V#004F#1P哇～！\n',
            '真是太厉害了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010335V#001F#1P喂喂，约修亚，怎么办呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010336V#001F我们可是亲手\n',
            '运送过给女王的礼物呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010337V#011F#2P而且你还，\n',
            '拿着它晃来晃去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010338V#008F#1P讨厌，不要说出来嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090010339V#218F嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010340V#601F哈哈，艾丝蒂尔你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010341V#007F#1P真、真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x000B, 0x0008, 400)
    CreateThread(0x0008, 0x01, 0x00, 0x0013)

    ChrTalk(
        0x0101,
        (
            '#0010010342V#000F#1P市长爷爷。\n',
            '那我把这个完好无损地交给您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    StopEffect(0x00, 0x02)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '把',
            (TxtCtl.SetColor, 0x2),
            '七耀石的结晶',
            (TxtCtl.SetColor, 0x0),
            '交给了市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0323, 1)
    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0x00, 0x0008, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrChipByIndex(0x0101, 65535)

    ChrTalk(
        0x0008,
        (
            '#0340010343V#602F嗯，确实就是这东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010344V那么为了保险起见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ClearChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0010)
    SetChrPos(0x0008, 77740, 0, -250, 0)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    ChrWalkTo(0x0008, 75570, 0, 1890, 2000, 0x00)
    SetChrDirection(0x0008, 0, 400)
    TerminateThread(0x0008, 0xFF)
    Sleep(1000)

    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 104)
    OP_73(0x0004)
    Sleep(500)

    SetChrFlags(0x0008, 0x0004)
    ChrMoveTo(0x0008, 75970, 0, 2510, 2000, 0x00)
    StopEffect(0x00, 0x02)
    Sleep(200)

    PlayEffect(0x00, 0x01, 0x00FF, 75970, 500, 3330, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    ChrMoveTo(0x0008, 75570, 0, 1890, 2000, 0x00)
    PlaySE(230, 0x00, 0x64)
    OP_6F(0x0004, 104)
    OP_70(0x0004, 0)
    Sleep(500)

    StopEffect(0x01, 0x02)
    OP_73(0x0004)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0340010345V#603F……这就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x01, 0x00, 0x0013)
    ChrWalkTo(0x0008, 77740, 0, -250, 2000, 0x00)
    Fade(1000)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x0008, 78100, 200, -950, 90)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0340010346V#601F之后只要请梅尔达斯工房\n',
            '把它做成导力器工艺品就行了。\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010347V真是期待早日见到成品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010348V#000F#1P啊，市长爷爷你真狡猾！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010349V#000F做好的话，能让我们看看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090010350V#217F哎呀，真是遗憾……\n',
            '我可是没办法亲眼看到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010351V#218F不过今天不仅增长了很多见闻，\n',
            '还见到了那么美丽的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010352V我都不知道该说些什么感激的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010353V#600F没事没事，\n',
            '这也算是市长的义务嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090010354V#217F真是太感谢您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010355V那么……\n',
            '我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010356V#000F#1P等一下，\n',
            '我们也一起回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 1)

    ChrTalk(
        0x0102,
        (
            '#0020010357V#010F#2P是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010358V#010F市长，我们这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010359V#601F嗯，辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    NewScene('ED6_DT01/T0200._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x5889
@scena.Code('func_13_5889')
def func_13_5889():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_58AB',
    )

    ChrTurnDirection(0x0000, 0x00FE, 0)
    ChrTurnDirection(0x0001, 0x00FE, 0)
    ChrTurnDirection(0x000B, 0x00FE, 0)
    Yield()

    Jump('func_13_5889')

    def _loc_58AB(): pass

    label('loc_58AB')

    Return()

# id: 0x0014 offset: 0x58AC
@scena.Code('func_14_58AC')
def func_14_58AC():
    Sleep(500)

    ChrWalkTo(0x0102, 82320, 0, -20, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x0008, 0)

    Return()

# id: 0x0015 offset: 0x58CD
@scena.Code('func_15_58CD')
def func_15_58CD():
    ChrWalkTo(0x0101, 78840, 0, 400, 3000, 0x00)
    SetChrDirection(0x0101, 180, 400)
    ChrTurnDirection(0x000B, 0x0101, 400)

    Return()

# id: 0x0016 offset: 0x58F0
@scena.Code('func_16_58F0')
def func_16_58F0():
    EventBegin(0x00)
    FadeIn(2000, 0)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ClearMapFlags(0x00000001)
    CameraMove(-5266, 0, -1110, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0047, 3, 0x23B))
    OP_28(0x0003, 0x01, 0x0002)
    OP_28(0x0003, 0x01, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010010030V#006F那么……\n',
            '不知道市长爷爷在不在呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010031V#010F像市长这么忙的人，\n',
            '这种时间外出了也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010032V#6P哦哦……\n',
            '是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 0)
    CameraMove(-2250, 1750, 3170, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010010033V#001F#5P啊，市长爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x01, 0x00, 0x0019)
    CreateThread(0x0101, 0x01, 0x00, 0x0017)
    CreateThread(0x0102, 0x01, 0x00, 0x0018)
    CameraMove(-4620, 0, 1950, 1500)
    Sleep(1500)

    ChrTalk(
        0x0102,
        (
            '#0020010034V#010F打扰了。\n',
            '我们是游击士协会派来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010035V#600F嗯，我已经听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010036V你们是代替卡西乌斯\n',
            '来我这里接受委托的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010037V#007F嗯，的确是这样没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010038V#505F对不起，市长爷爷。\n',
            '本来应该由老爸来接这个任务的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010039V#603F没事没事，\n',
            '我知道他有重要的任务去做，\n',
            '忙得抽不开身也是理所当然的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010040V#600F对了……\n',
            '站在这里说话不太方便。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010041V详细情况就到书房去谈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(2000)
    CameraMove(79750, 0, 190, 0)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x0008, 78100, 200, -950, 90)
    SetChrPos(0x0101, 80520, 0, -840, 270)
    SetChrPos(0x0102, 80370, 0, 180, 225)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0340010042V#600F……虽说是委托，\n',
            '其实也不是什么难事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010043V要协会帮忙做这件事，\n',
            '我还觉得有点不好意思呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010044V只是我手头的工作一直放不开，\n',
            '所以才想到向协会提出请求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010045V#010F听说是运送物品的工作，\n',
            '到底是些什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010046V#600F嗯，我希望你们能代我\n',
            '去一趟北边的玛鲁加矿山，\n',
            '然后把七耀石的结晶送回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010047V#505F说起七耀石……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010048V和我们平时得到的\n',
            '『耀晶片』都是同一种东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010049V#010F严格来说，\n',
            '比宝石小的七耀石碎片才称作耀晶片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010050V耀晶片经过精制和加工之后，\n',
            '就可以做成安装在导力器里的结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010051V#006F原来是这样啊……\n',
            '我大概明白是什么意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010052V#603F在玛鲁加矿山，\n',
            '一直都可以开采到\n',
            '七耀石之一的翠耀石……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010053V最近矿山采集到一块较大的结晶，\n',
            '目前交由矿长暂时保管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010054V#010F从矿长那里取得那块结晶，\n',
            '然后送回来就可以了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010055V#600F没错。\n',
            '怎么样，愿意帮我这个忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010056V#505F运送宝石啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010057V#505F虽然和打倒魔兽不一样\n',
            '不过还是有一种特别的紧张感……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010058V#001F好吧，这件事就交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0340010059V#601F谢谢你们俩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010060V啊，对了，\n',
            '你们把这个带上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '市长的介绍信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0321, 1)

    ChrTalk(
        0x0008,
        (
            '#0340010061V#600F把这封信交给门卫，\n',
            '就可以进入矿山了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010062V#600F那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    ClearMapFlags(0x00400000)

    Return()

# id: 0x0017 offset: 0x60FE
@scena.Code('func_17_60FE')
def func_17_60FE():
    ChrWalkTo(0x0101, -6500, 0, 1260, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 0)

    Return()

# id: 0x0018 offset: 0x611A
@scena.Code('func_18_611A')
def func_18_611A():
    Sleep(500)

    ChrWalkTo(0x0102, -5130, 0, 1000, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0008, 0)

    Return()

# id: 0x0019 offset: 0x613B
@scena.Code('func_19_613B')
def func_19_613B():
    ChrWalkTo(0x0008, -4610, 0, 2940, 2000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
