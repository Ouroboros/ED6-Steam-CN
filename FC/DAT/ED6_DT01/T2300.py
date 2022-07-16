import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '穿制服的少女'),
    TXT(0x02, '基库'),
    TXT(0x03, '戴帽子的男孩'),
    TXT(0x04, '克拉姆'),
    TXT(0x05, '萨蒂'),
    TXT(0x06, '玛丽'),
    TXT(0x07, '阿梅莉娅'),
    TXT(0x08, '照相机'),
    TXT(0x09, '奥维德'),
    TXT(0x0A, '卢希娅'),
    TXT(0x0B, '达尼艾尔'),
    TXT(0x0C, '波利'),
    TXT(0x0D, '卡露娜'),
    TXT(0x0E, '特蕾莎院长'),
    TXT(0x0F, '玛诺利亚间道方向'),
    TXT(0x10, '梅威海道方向'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2300.x'
    header.mapIndex       = 86
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2300._SN', 'ED6_DT01/T2300_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6D7E
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00002328,
            dword_04        = 0x00001770,
            dword_08        = 0xFFFFF448,
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
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 86,
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
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH00004._CH', 'ED6_DT07/CH00004P._CP'),
        ('ED6_DT07/CH00044._CH', 'ED6_DT07/CH00044P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00005._CH', 'ED6_DT07/CH00005P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT06/CH20085._CH', 'ED6_DT06/CH20085P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 18100,
            z                   = 0,
            y                   = 16400,
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
            z                   = 6130,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
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
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 45300,
            z                   = 0,
            y                   = 23500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 37310,
            z                   = 1700,
            y                   = -33090,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -4100,
            z                   = 8000,
            y                   = 45100,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            x                   = 53000,
            z                   = 0,
            y                   = 33500,
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
            x                   = 53000,
            z                   = 0,
            y                   = 33500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2800,
            z                   = 4000,
            y                   = 29000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 6000,
            z                   = 200,
            y                   = 22200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 32500,
            z                   = 0,
            y                   = -34400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 5560,
            z                   = 6000,
            y                   = -2680,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 3860,
            z                   = 4030,
            y                   = 16990,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -2940,
            z                   = 7990,
            y                   = 68620,
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
            x                   = 75410,
            z                   = -40,
            y                   = 20810,
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

# id: 0x10003 offset: 0x34A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x34A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 16870,
            y           = 7000,
            z           = -7690,
            range       = -9400,
            dword_10    = 0x00001388,
            dword_14    = 0xFFFFF998,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = 8200,
            y           = 4000,
            z           = 9300,
            range       = 1460,
            dword_10    = 0x0000178E,
            dword_14    = 0x0000198C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000014,
        ),
        ScenaEventData(
            x           = 65500,
            y           = -1000,
            z           = 23100,
            range       = 68250,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00004736,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = -760,
            y           = 5000,
            z           = 59750,
            range       = -5380,
            dword_10    = 0x00002670,
            dword_14    = 0x0000F4D8,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001B,
        ),
        ScenaEventData(
            x           = 27540,
            y           = 0,
            z           = 18980,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = 53410,
            y           = 0,
            z           = 22710,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 6000,
            y           = 4000,
            z           = 20210,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001F,
        ),
    )

# id: 0x10005 offset: 0x42A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x42A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_4D2',
    )

    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 5000, 4000, 17180, 180)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 5160, 4000, 15170, 180)
    SetChrFlags(0x000B, 0x0010)
    CreateThread(0x000B, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 7040, 4030, 12860, 270)
    SetChrFlags(0x0012, 0x0010)
    CreateThread(0x0012, 0x00, 0x00, 0x0005)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 5130, 4030, 10940, 0)
    SetChrFlags(0x0013, 0x0010)
    CreateThread(0x0013, 0x00, 0x00, 0x0006)
    SetChrPos(0x0011, 3030, 4030, 13020, 90)
    SetChrFlags(0x0011, 0x0010)
    CreateThread(0x0011, 0x00, 0x00, 0x0007)

    Jump('loc_5E9')

    def _loc_4D2(): pass

    label('loc_4D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_4E1',
    )

    ClearChrFlags(0x0014, 0x0080)

    Jump('loc_5E9')

    def _loc_4E1(): pass

    label('loc_4E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_4F5',
    )

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0008)

    Jump('loc_5E9')

    def _loc_4F5(): pass

    label('loc_4F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_598',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 5000, 4000, 17180, 180)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 5160, 4000, 15170, 180)
    SetChrFlags(0x000B, 0x0010)
    CreateThread(0x000B, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 7040, 4030, 12860, 270)
    SetChrFlags(0x0012, 0x0010)
    CreateThread(0x0012, 0x00, 0x00, 0x0005)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 5130, 4030, 10940, 0)
    SetChrFlags(0x0013, 0x0010)
    CreateThread(0x0013, 0x00, 0x00, 0x0006)
    SetChrPos(0x0011, 3030, 4030, 13020, 90)
    SetChrFlags(0x0011, 0x0010)
    CreateThread(0x0011, 0x00, 0x00, 0x0007)

    Jump('loc_5E9')

    def _loc_598(): pass

    label('loc_598')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_5BA',
    )

    SetChrPos(0x0011, 63480, -20, 23290, 180)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)

    Jump('loc_5E9')

    def _loc_5BA(): pass

    label('loc_5BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_5C4',
    )

    Jump('loc_5E9')

    def _loc_5C4(): pass

    label('loc_5C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_5CE',
    )

    Jump('loc_5E9')

    def _loc_5CE(): pass

    label('loc_5CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_5D8',
    )

    Jump('loc_5E9')

    def _loc_5D8(): pass

    label('loc_5D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_5E2',
    )

    Jump('loc_5E9')

    def _loc_5E2(): pass

    label('loc_5E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_5E9',
    )

    def _loc_5E9(): pass

    label('loc_5E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_611',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001F, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_611',
    )

    ClearChrFlags(0x000E, 0x0080)

    def _loc_611(): pass

    label('loc_611')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_61F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0016)

    def _loc_61F(): pass

    label('loc_61F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_63B',
    )

    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0017)

    def _loc_63B(): pass

    label('loc_63B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_649',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0018)

    def _loc_649(): pass

    label('loc_649')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_659'),
        (0x00000069, 'loc_695'),
        (-1, 'loc_6A8'),
    )

    def _loc_659(): pass

    label('loc_659')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 1, 0x409)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66B',
    )

    SetScenaFlags(ScenaFlag(0x0081, 1, 0x409))
    Event(0, 0x0010)

    Jump('loc_692')

    def _loc_66B(): pass

    label('loc_66B')

    If(
        (
            (Expr.Eval, "OP_42(0x0036)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_692',
    )

    OP_28(0x001F, 0x04, 0x10)
    OP_28(0x001F, 0x01, 0x0080)
    FormationDelMember(0x36, 0xFF)
    Event(1, 0x0001)

    def _loc_692(): pass

    label('loc_692')

    Jump('loc_6A8')

    def _loc_695(): pass

    label('loc_695')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 2, 0x40A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A5',
    )

    Event(0, 0x0011)

    def _loc_6A5(): pass

    label('loc_6A5')

    Jump('loc_6A8')

    def _loc_6A8(): pass

    label('loc_6A8')

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x6BA
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -108000, -126000, 196683)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6E4',
    )

    OP_B1('t2300_y')

    Jump('loc_6ED')

    def _loc_6E4(): pass

    label('loc_6E4')

    OP_B1('t2300_n')

    def _loc_6ED(): pass

    label('loc_6ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_705',
    )

    OP_6F(0x0002, 0)
    OP_72(0x0002, 0x0010)

    def _loc_705(): pass

    label('loc_705')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_71A',
    )

    OP_77(0x41, 0x64, 0x82, 0x00, 0x00000000)

    def _loc_71A(): pass

    label('loc_71A')

    PlaySE(453, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x720
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_735',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_735(): pass

    label('loc_735')

    Return()

# id: 0x0003 offset: 0x736
@scena.Code('func_03_736')
def func_03_736():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_759',
    )

    OP_8D(0x00FE, -6100, 32000, 300, 25200, 3000)

    Jump('func_03_736')

    def _loc_759(): pass

    label('loc_759')

    Return()

# id: 0x0004 offset: 0x75A
@scena.Code('func_04_75A')
def func_04_75A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_82E',
    )

    ChrWalkTo(0x00FE, 7040, 4030, 12860, 3500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    OP_62(0x000B, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 5130, 4030, 10940, 3500, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    OP_62(0x000B, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3030, 4030, 13020, 3500, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    OP_62(0x000B, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 5160, 4000, 15170, 3500, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    OP_62(0x000B, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    Jump('func_04_75A')

    def _loc_82E(): pass

    label('loc_82E')

    Return()

# id: 0x0005 offset: 0x82F
@scena.Code('func_05_82F')
def func_05_82F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_903',
    )

    ChrWalkTo(0x00FE, 5130, 4030, 10940, 3500, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    OP_62(0x0012, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3030, 4030, 13020, 3500, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    OP_62(0x0012, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 5160, 4000, 15170, 3500, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    OP_62(0x0012, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 7040, 4030, 12860, 3500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    OP_62(0x0012, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    Jump('func_05_82F')

    def _loc_903(): pass

    label('loc_903')

    Return()

# id: 0x0006 offset: 0x904
@scena.Code('func_06_904')
def func_06_904():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9D8',
    )

    ChrWalkTo(0x00FE, 3030, 4030, 13020, 3500, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    Sleep(1000)

    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 5160, 4000, 15170, 3500, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1000)

    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 7040, 4030, 12860, 3500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    Sleep(1000)

    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 5130, 4030, 10940, 3500, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(1000)

    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('func_06_904')

    def _loc_9D8(): pass

    label('loc_9D8')

    Return()

# id: 0x0007 offset: 0x9D9
@scena.Code('func_07_9D9')
def func_07_9D9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AAD',
    )

    ChrWalkTo(0x00FE, 5160, 4000, 15170, 3500, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    OP_62(0x0011, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 7040, 4030, 12860, 3500, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    OP_62(0x0011, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 5130, 4030, 10940, 3500, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    OP_62(0x0011, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3030, 4030, 13020, 3500, 0x00)
    SetChrDirection(0x00FE, 90, 400)
    OP_62(0x0011, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    Jump('func_07_9D9')

    def _loc_AAD(): pass

    label('loc_AAD')

    Return()

# id: 0x0008 offset: 0xAAE
@scena.Code('func_08_AAE')
def func_08_AAE():
    TalkBegin(0x0014)

    ChrTalk(
        0x0014,
        (
            '#0320061359V那帮家伙由我看着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061360V你们就赶去卢安，\n',
            '向嘉恩报告昨天的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0014)

    Return()

# id: 0x0009 offset: 0xB06
@scena.Code('func_09_B06')
def func_09_B06():
    TalkBegin(0x000C)
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B64',
    )

    OP_0D()
    OP_A9(0x36)
    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_B64(): pass

    label('loc_B64')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B75',
    )

    TalkEnd(0x000C)

    Return()

    def _loc_B75(): pass

    label('loc_B75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_C54',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C01',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000C,
        (
            '孩子们的脸上\n',
            '总算又展露了笑容……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过犯人竟然是\n',
            '那个戴尔蒙市长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我想总有一天\n',
            '孩子们会知道真相的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C51')

    def _loc_C01(): pass

    label('loc_C01')

    ChrTalk(
        0x000C,
        (
            '不过犯人竟然是\n',
            '那个戴尔蒙市长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我想总有一天\n',
            '孩子们会知道真相的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C51(): pass

    label('loc_C51')

    Jump('loc_1345')

    def _loc_C54(): pass

    label('loc_C54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_D3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CFA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000C,
        (
            '听说那些纵火犯\n',
            '都被抓住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '虽然松了一口气，\n',
            '不过我的心情还是很悲伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '事情虽然解决了，\n',
            '但是孩子们的心灵创伤是不会这么简单痊愈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3B')

    def _loc_CFA(): pass

    label('loc_CFA')

    ChrTalk(
        0x000C,
        (
            '事情虽然解决了，\n',
            '但是孩子们的心灵创伤是不会这么简单痊愈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D3B(): pass

    label('loc_D3B')

    Jump('loc_1345')

    def _loc_D3E(): pass

    label('loc_D3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_E1E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000C,
        (
            '听说特蕾莎老师被袭击，\n',
            '还受了伤啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊啊，爱德丝啊……\n',
            '您究竟想对\n',
            '老师和孩子们做什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '求你们了，游击士。\n',
            '一定要抓住犯人们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E1B')

    def _loc_DE1(): pass

    label('loc_DE1')

    ChrTalk(
        0x000C,
        (
            '啊啊，爱德丝啊……\n',
            '您究竟想对\n',
            '老师和孩子们做什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E1B(): pass

    label('loc_E1B')

    Jump('loc_1345')

    def _loc_E1E(): pass

    label('loc_E1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_E72',
    )

    ChrTalk(
        0x000C,
        (
            '孤儿院的孩子们\n',
            '最近好像有点精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '女孩子们\n',
            '经常到这里来玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1345')

    def _loc_E72(): pass

    label('loc_E72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_ED2',
    )

    ChrTalk(
        0x000C,
        (
            '一个孤儿院的男孩子\n',
            '刚才飞快地奔出去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '发生什么事了吗……\n',
            '我有点担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1345')

    def _loc_ED2(): pass

    label('loc_ED2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_F76',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F36',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000C,
        (
            '听说孤儿院着火了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '刚才孩子们\n',
            '都哭着从这里走过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好可怜啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F73')

    def _loc_F36(): pass

    label('loc_F36')

    ChrTalk(
        0x000C,
        (
            '听说孤儿院着火了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '刚才孩子们\n',
            '都哭着从这里走过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F73(): pass

    label('loc_F73')

    Jump('loc_1345')

    def _loc_F76(): pass

    label('loc_F76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_FD4',
    )

    ChrTalk(
        0x000C,
        (
            '我想给婆婆多少帮点忙，\n',
            '于是就开了一间花店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '各位游击士，\n',
            '来一束花怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1345')

    def _loc_FD4(): pass

    label('loc_FD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_1065',
    )

    ChrTalk(
        0x000C,
        (
            '要去玛西亚孤儿院的话，\n',
            '走东边的梅威海道然后拐入岔道，\n',
            '这样你们就可以找到那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '如果没有看漏路标的话，\n',
            '应该很快就能找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1345')

    def _loc_1065(): pass

    label('loc_1065')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12EA',
    )

    EventBegin(0x00)
    OP_69(0x000C, 1000)

    ChrTalk(
        0x000C,
        (
            '#1470040643V哎呀，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040644V#002F我们有件事想请问您……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040645V您有没有在这附近\n',
            '见到一个戴帽子的男孩呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1470040646V戴帽子的男孩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1470040647V啊啊……\n',
            '他不就是那个王立学院女学生的朋友吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040648V#002F嗯，就是那孩子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040649V#010F请问你知道他是哪家的孩子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1470040650V他不是这村子的孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1470040651V我想他应该是孤儿院的孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040652V#004F孤儿院……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1470040653V嗯，就是『玛西亚孤儿院』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1470040654V由一位叫特蕾莎的女士\n',
            '所开设的慈善设施。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1470040655V走东面的梅威海道就会经过那里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040656V#002F原来那孩子是住在孤儿院的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040657V#010F我们也去孤儿院那边看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0081, 5, 0x40D))
    EventEnd(0x01)

    Jump('loc_1345')

    def _loc_12EA(): pass

    label('loc_12EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1345',
    )

    ChrTalk(
        0x000C,
        (
            '在村子里绽放的是\n',
            '一种名为玛诺利亚的木莲花。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嘿嘿，\n',
            '是不是非常漂亮可爱呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1345(): pass

    label('loc_1345')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x1349
@scena.Code('func_0A_1349')
def func_0A_1349():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_136E',
    )

    OP_4A(0x0011, 0)

    ChrTalk(
        0x00FE,
        (
            '等一下～！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0011, 0)

    Jump('loc_187C')

    def _loc_136E(): pass

    label('loc_136E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Return,
        ),
        'loc_1431',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13EC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '那些大哥哥\n',
            '是不是欺负波利了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐，\n',
            '你们去教训他们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '欺负大家的人，\n',
            '是绝对不能原谅的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_142E')

    def _loc_13EC(): pass

    label('loc_13EC')

    ChrTalk(
        0x00FE,
        (
            '那些大哥哥\n',
            '是不是欺负波利了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐，\n',
            '你们去教训他们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_142E(): pass

    label('loc_142E')

    Jump('loc_187C')

    def _loc_1431(): pass

    label('loc_1431')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_14A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_148E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '孤儿院的大家\n',
            '都一边哭一边回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事？\n',
            '是谁欺负他们了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14A4')

    def _loc_148E(): pass

    label('loc_148E')

    ChrTalk(
        0x00FE,
        (
            '是谁欺负他们了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14A4(): pass

    label('loc_14A4')

    Jump('loc_187C')

    def _loc_14A7(): pass

    label('loc_14A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_14D8',
    )

    OP_4A(0x0011, 0)

    ChrTalk(
        0x00FE,
        (
            '我交了好多朋友，\n',
            '真开心。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0011, 0)

    Jump('loc_187C')

    def _loc_14D8(): pass

    label('loc_14D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1577',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_153D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '克拉姆\n',
            '刚才飞奔出去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是又做了什么坏事，\n',
            '惹特蕾莎老师生气了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1574')

    def _loc_153D(): pass

    label('loc_153D')

    ChrTalk(
        0x00FE,
        (
            '克拉姆是不是又做了什么坏事，\n',
            '惹特蕾莎老师生气了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1574(): pass

    label('loc_1574')

    Jump('loc_187C')

    def _loc_1577(): pass

    label('loc_1577')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_1647',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15EA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '孤儿院的大家\n',
            '都到我家里来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家好像\n',
            '非常痛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '该怎么办呢，我很担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1644')

    def _loc_15EA(): pass

    label('loc_15EA')

    ChrTalk(
        0x00FE,
        (
            '孤儿院的大家\n',
            '都到我家里来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家好像非常痛苦啊……\n',
            '该怎么办呢，我很担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1644(): pass

    label('loc_1644')

    Jump('loc_187C')

    def _loc_1647(): pass

    label('loc_1647')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_16E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16C2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '卢希娅也想去孤儿院玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都像兄妹一样，\n',
            '相处得好开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想和他们一起玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16E5')

    def _loc_16C2(): pass

    label('loc_16C2')

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '卢希娅也想去孤儿院玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16E5(): pass

    label('loc_16E5')

    Jump('loc_187C')

    def _loc_16E8(): pass

    label('loc_16E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_1750',
    )

    ChrTalk(
        0x00FE,
        (
            '孤儿院的孩子们\n',
            '有时候会来玛诺利亚村玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我碰到过他们好几次了。\n',
            '特蕾莎老师非常温柔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_187C')

    def _loc_1750(): pass

    label('loc_1750')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_17E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17B9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '戴帽子的男孩子？\n',
            '难道你们说的是他吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '我好像在花店那里看到过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17E6')

    def _loc_17B9(): pass

    label('loc_17B9')

    ChrTalk(
        0x00FE,
        (
            '那个男孩子，\n',
            '我好像在花店那里看到过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17E6(): pass

    label('loc_17E6')

    Jump('loc_187C')

    def _loc_17E9(): pass

    label('loc_17E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_187C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_184D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '大姐姐，你们是来旅游的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家是酒馆兼旅馆。\n',
            '不介意的话就住我家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_187C')

    def _loc_184D(): pass

    label('loc_184D')

    ChrTalk(
        0x00FE,
        (
            '我家是酒馆兼旅馆。\n',
            '不介意的话就住我家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_187C(): pass

    label('loc_187C')

    TalkEnd(0x0011)

    Return()

# id: 0x000B offset: 0x1880
@scena.Code('func_0B_1880')
def func_0B_1880():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_18D2',
    )

    OP_4A(0x000B, 0)

    ChrTalk(
        0x00FE,
        (
            '#0400070168V#772F#30A如果让波利当鬼的话，\n',
            '游戏就没有意思了。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x000B, 0)

    Jump('loc_1910')

    def _loc_18D2(): pass

    label('loc_18D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1910',
    )

    OP_4A(0x000B, 0)

    ChrTalk(
        0x00FE,
        (
            '#0400070169V#770F#17A大家都已经很有精神了！\n',
            '　',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x000B, 0)

    def _loc_1910(): pass

    label('loc_1910')

    TalkEnd(0x000B)

    Return()

# id: 0x000C offset: 0x1914
@scena.Code('func_0C_1914')
def func_0C_1914():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_19A5',
    )

    ChrTalk(
        0x00FE,
        (
            '#0410070170V有老师在旁边，\n',
            '果然感到很安心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410070171V但我们总有一天\n',
            '必须要自立的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410070172V那时侯大家都要\n',
            '好好报答老师呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F6')

    def _loc_19A5(): pass

    label('loc_19A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_19F6',
    )

    ChrTalk(
        0x00FE,
        (
            '#0410050982V姐姐，\n',
            '谢谢你们救了克拉姆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410050983V那个孩子\n',
            '真的很乱来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19F6(): pass

    label('loc_19F6')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x19FA
@scena.Code('func_0D_19FA')
def func_0D_19FA():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1A30',
    )

    OP_4A(0x0012, 0)

    ChrTalk(
        0x00FE,
        (
            '#0420050984V今天的饭会是什么呢～',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0012, 0)

    Jump('loc_1A8E')

    def _loc_1A30(): pass

    label('loc_1A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1A63',
    )

    OP_4A(0x0012, 0)

    ChrTalk(
        0x00FE,
        (
            '#0420050985V今天的饭会是什么呢～',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0012, 0)

    Jump('loc_1A8E')

    def _loc_1A63(): pass

    label('loc_1A63')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1A8E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0420050546V克拉姆他\n',
            '突然怎么了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A8E(): pass

    label('loc_1A8E')

    TalkEnd(0x0012)

    Return()

# id: 0x000E offset: 0x1A92
@scena.Code('func_0E_1A92')
def func_0E_1A92():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_1AC4',
    )

    OP_4A(0x0013, 0)

    ChrTalk(
        0x00FE,
        (
            '#0430050986V#18A嘿咻嘿咻……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0013, 0)

    Jump('loc_1B32')

    def _loc_1AC4(): pass

    label('loc_1AC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_1AF5',
    )

    OP_4A(0x0013, 0)

    ChrTalk(
        0x00FE,
        (
            '#0430050987V#17A大家正在玩呢～',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_4B(0x0013, 0)

    Jump('loc_1B32')

    def _loc_1AF5(): pass

    label('loc_1AF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_1B32',
    )

    ChrTalk(
        0x00FE,
        (
            '克拉姆他\n',
            '在吃布丁的时候，\n',
            '好像在考虑什么事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B32(): pass

    label('loc_1B32')

    TalkEnd(0x0013)

    Return()

# id: 0x000F offset: 0x1B36
@scena.Code('func_0F_1B36')
def func_0F_1B36():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D38',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0390070152V#753F哎呀，艾丝蒂尔你们这副装束，\n',
            '难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070153V#501F嗯，\n',
            '我们这就准备去蔡斯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0390070154V#753F真是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390070155V#750F各位实在是帮了我们大忙啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390070156V而且没能给你们什么回报，\n',
            '我真的是过意不去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070157V#008F不要紧，您太客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070158V能看到孩子们的笑脸，\n',
            '我觉得我们的努力就有价值了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0390070159V#750F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390070160V……你们到了蔡斯之后\n',
            '也要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070161V#010F谢谢。\n',
            '老师你们也请保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0390070162V#751F嗯，\n',
            '真的是多谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9E')

    def _loc_1D38(): pass

    label('loc_1D38')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0390070163V#751F艾丝蒂尔、约修亚，\n',
            '你们要保重啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390070164V你们到了蔡斯之后\n',
            '也要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D9E(): pass

    label('loc_1D9E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1DA2
@scena.Code('func_10_1DA2')
def func_10_1DA2():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_12(0x00000064, 0x0003D090, 0x00000000)
    SetChrPos(0x0101, -2020, 8000, 57380, 180)
    SetChrPos(0x0102, -3170, 8039, 57530, 180)
    CameraMove(-2500, 6000, -3290, 0)
    OP_6C(310000, 0)
    CameraSetDistance(5900, 0)

    @scena.Lambda('lambda_1E01')
    def lambda_1E01():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E01)

    Sleep(2000)

    @scena.Lambda('lambda_1E16')
    def lambda_1E16():
        CameraMove(-2100, 7980, 57740, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E16)

    OP_12(0x00009470, 0x00014C08, 0x00001F40)
    CameraSetDistance(3000, 8000)

    ChrTalk(
        0x0101,
        (
            '#0010040381V#501F#2P哈～～\n',
            '终于来到有人住的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)
    Sleep(200)

    SetChrDirection(0x0101, 90, 400)
    Sleep(200)

    SetChrDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010040382V#000F#2P哇啊～真漂亮……\n',
            '这里到处开满了白花……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040383V这村子叫什么名字呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040384V#010F玛诺利亚村。\n',
            '一个位于海道沿岸的小村落。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040385V这种白色的花，应该是木莲的一种吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040386V#000F#2P嗯～真的好漂亮啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040387V而且这种花香和海水味混在一起，\n',
            '感觉有种清新自然的甘甜气息～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040388V#001F嗯……\n',
            '不知不觉我都有点饿了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040389V#019F哈哈，\n',
            '闻到花香食欲就被刺激起来了，\n',
            '还真像艾丝蒂尔的习性啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040390V#011F正所谓『好看不如好吃』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040391V#006F#2P因为正是长身体的时候嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040392V已经到中午了吧。\n',
            '我们找个地方休息一下，吃点东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040393V#014F好啊……\n',
            '我们身上好像还有些干粮吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040394V#004F#2P啊，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040395V#000F难得来到这么别致的小村落，\n',
            '不如尝尝当地的料理吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040396V我们可是第一次来到卢安地区呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040397V#010F嗯，也是。\n',
            '那我们到这里的旅馆看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x21D0
@scena.Code('func_11_21D0')
def func_11_21D0():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(27790, 0, 18450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0008, 0x0040)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 35500, -80, 17000, 270)
    SetChrPos(0x0101, 27300, 480, 20630, 0)
    SetChrPos(0x0102, 27300, 480, 21630, 180)
    FadeIn(1000, 0)
    ChrWalkTo(0x0008, 27460, 60, 16830, 3000, 0x00)
    SetChrDirection(0x0008, 0, 400)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0060040454V#042F刚刚已经来这里找过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040455V#042F在杂货店里也没有见到他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22D0')
    def lambda_22D0():
        CameraMove(27520, 60, 16390, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_22D0)

    SetChrDirection(0x0008, 270, 400)
    SetChrDirection(0x0008, 180, 400)
    Sleep(200)

    SetChrDirection(0x0008, 270, 400)
    Sleep(200)

    SetChrDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0060040456V#043F怎么办……\n',
            '那小家伙到底去了哪里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_70(0x0004, 30)
    OP_73(0x0004)
    ChrMoveTo(0x0101, 27280, 500, 19340, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010040457V#001F约修亚，快点啦快点啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040458V#012F等一下，艾丝蒂尔。\n',
            '当心后面的台阶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_23C5')
    def lambda_23C5():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_23C5)

    @scena.Lambda('lambda_23D3')
    def lambda_23D3():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_23D3)

    @scena.Lambda('lambda_23E1')
    def lambda_23E1():
        ChrMoveTo(0x00FE, 27380, 60, 17180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_23E1)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(125, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_240B')
    def lambda_240B():
        ChrJumpTo(0x00FE, 27240, 20, 17780, 500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_240B)

    @scena.Lambda('lambda_2429')
    def lambda_2429():
        ChrJumpTo(0x00FE, 27440, 70, 15630, 500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2429)

    CreateThread(0x0101, 0x02, 0x00, 0x0012)

    ChrTalk(
        0x0008,
        (
            '#044F#4P#12A呀……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010040460V#004F#1P#12A啊……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0101, 0x0001)
    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_248F')
    def lambda_248F():
        ChrWalkTo(0x00FE, 27730, 500, 19280, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_248F)

    WaitForThreadExit(0x0102, 0x0001)
    ClearChrFlags(0x0102, 0x0004)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040461V#007F好疼啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(400)
    SetChrChipByIndex(0x0101, 65535)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ClearChrFlags(0x0101, 0x0004)
    OP_92(0x0101, 0x0008, 1000, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010040462V#004F不、不好意思，你没事吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040463V刚才我没看到门口有人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060040464V#040F啊，我没事，不要在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(400)
    SetChrChipByIndex(0x0008, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0060040465V#045F其实该说对不起的是我才对。\n',
            '都怪我在看其他地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040466V#501F啊，是这样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040467V#001F哈哈，大家没事就好了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0004, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0004, 30)
    OP_70(0x0004, 0)
    ChrWalkTo(0x0102, 28280, -40, 16990, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0008, 400)
    OP_71(0x0004, 0x0800)

    ChrTalk(
        0x0102,
        (
            '#0020040468V#017F真是的……\n',
            '艾丝蒂尔，你在说什么啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040469V#014F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060040470V#040F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040471V#000F怎么了，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040472V#013F没、没什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0102, 0x0008, 1200, 1000, 0x00)

    @scena.Lambda('lambda_2734')
    def lambda_2734():
        ChrTurnDirection(0x00FE, 0x0008, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2734)

    ChrTurnDirection(0x0008, 0x0102, 0)

    ChrTalk(
        0x0102,
        (
            '#0020040473V#010F不好意思。\n',
            '我的同伴给你添麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040474V你没有受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060040475V#045F啊，我没事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040476V我正急着找人……\n',
            '所以刚才没有留意周围。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040477V#501F啊，你找的是什么人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '#0060040478V#040F一个１０岁左右的男孩，\n',
            '戴着一顶帽子的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040479V你们有没有看到过他呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040480V#000F戴帽子的男孩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040481V#000F约修亚，你有没有印象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040482V#010F没有，我印象中并未见过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060040483V#043F这样啊……\n',
            '到底跑到哪里去了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040484V#045F那我先失陪了，\n',
            '刚才给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 90, 400)

    @scena.Lambda('lambda_2947')
    def lambda_2947():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2947')

    DispatchAsync2(0x0101, 0x0001, lambda_2947)

    @scena.Lambda('lambda_2958')
    def lambda_2958():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2958')

    DispatchAsync2(0x0102, 0x0001, lambda_2958)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    @scena.Lambda('lambda_298D')
    def lambda_298D():
        ChrWalkTo(0x00FE, 41150, -20, 18660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_298D)

    CameraMove(30950, -30, 16970, 2000)
    WaitForThreadExit(0x0008, 0x0001)
    SetChrFlags(0x0008, 0x0080)
    OP_63(0x0101)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1200)

    CameraMove(28490, 40, 16850, 1000)
    TerminateThread(0x0101, 0xFF)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040485V#002F约修亚？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040486V#002F喂，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0102)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040487V#014F#2P哦，啊啊……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040488V#007F怎么也没怎么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010040489V#004F啊，难道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040490V#001F原来是这样，我知道啦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040491V#018F#2P……你又在乱想什么啦？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040492V#006F别害羞、别害羞嘛⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040493V知道什么叫一见钟情吗？\n',
            '恋爱之花就是在这个时候绽放的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040494V#017F#2P你·别·误·会·了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040495V我只是觉得她和\n',
            '我以前认识的一个人有点相似而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040496V#010F#2P所以，刚才只是有点惊讶罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040497V#004F啊……真的吗？哇～\n',
            '和你小时候认识的人很像啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040498V#502F这种理由只能得３０分呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0102,
        (
            '#0020040499V#015F#2P我说，艾丝蒂尔。\n',
            '你还记得刚才那女孩的校服吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040500V#004F说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040501V她的衣服好像和乔丝特变装时穿的\n',
            '什么学院的校服一模一样呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040502V#010F#2P是杰尼丝王立学院。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040503V因为王立学院就在卢安地区，\n',
            '所以我们见到这些学生也并不奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040504V#501F嗯～这次总该是货真价实的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040505V#001F我觉得那女孩很有礼貌，\n',
            '而且头脑也好像很聪明的呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040506V气质和那个傲慢的男人婆完全不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040507V#015F#2P你还敢说那件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040508V是谁第一次见到乔丝特的时候\n',
            '被骗得晕头转向的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040509V#009F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040510V#019F#2P而且，当时又是谁\n',
            '像刚才那样拿我开了一顿玩笑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040511V不过，就算被骗，\n',
            '也毕竟都是以前的事情啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040512V#003F唔唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040513V#019F#2P与其花时间嘲笑别人，\n',
            '还不如花点功夫观察身边的人和事，\n',
            '锻炼一下自己的观察力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040514V#007F明白了，我完全明白了啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040515V我以后再也不会随便嘲笑别人啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040516V#010F#2P你明白了就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040517V料理都快凉了，\n',
            '我们去瞭望台那里吃午餐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040518V#007F好～～吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0081, 2, 0x40A))
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x3056
@scena.Code('func_12_3056')
def func_12_3056():
    Sleep(200)

    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0008, 11)

    Return()

# id: 0x0013 offset: 0x3066
@scena.Code('func_13_3066')
def func_13_3066():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 2, 0x40A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F1A',
    )

    EventBegin(0x00)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040519V#004F呜哇～～真是绝妙的景色！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040520V#010F嗯，海边的风景一览无遗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3108')
    def lambda_3108():
        CameraMove(2428, 6000, -13190, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3108)

    @scena.Lambda('lambda_3120')
    def lambda_3120():
        CameraSetDistance(8450, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3120)

    @scena.Lambda('lambda_3130')
    def lambda_3130():
        OP_6C(60000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3130)

    @scena.Lambda('lambda_3140')
    def lambda_3140():
        OP_67(0, 5095, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3140)

    OP_12(0x000186A0, 0x0003D090, 0x00001B58)
    Sleep(7000)

    ChrTalk(
        0x0101,
        (
            '#0010040521V#501F在这里吃午餐……\n',
            '简直就是一种奢侈的享受啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040522V#010F我也有同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040523V我们现在就开始吃吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040524V#501F嗯⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040525V#001F啊～肚子真的好饿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(5420, 6000, -13860, 0)
    CameraSetDistance(2800, 0)
    OP_6C(51000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_12(0x00000000, 0x00000000, 0x00000000)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrChipByIndex(0x0101, 12)
    SetChrChipByIndex(0x0102, 13)
    SetChrPos(0x0101, 5200, 6200, -13860, 180)
    SetChrPos(0x0102, 6100, 6200, -13860, 180)
    SetChrSubChip(0x0101, 1)
    SetChrSubChip(0x0102, 2)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010040526V#501F#3P我的便当是\n',
            '熏火腿三明治。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040527V嗯～～还没吃就闻到一阵香味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040528V#010F而我的是……海鲜焗饭。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040529V漂着淡淡番红花的香味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040530V#001F#3P那么，我不客气了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040531V#015F我也不客气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 0)
    Sleep(100)

    SetChrSubChip(0x0102, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010040532V#501F#3P先吃一口尝尝味道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040533V#502F莫咕莫咕莫咕……咕咚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040534V#004F哇～真的很好吃呢！\n',
            '而且莴苣又香又脆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040535V#010F我的焗饭也很不错，\n',
            '番红花的香气恰倒好处。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040536V白之木莲亭老板的厨艺的确一流。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010040537V#501F#3P约修亚，可以让我尝一口吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040538V我还没吃过海鲜焗饭，\n',
            '很想尝尝是什么味道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0102, 2)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020040539V#010F好啊……\n',
            '那我和你交换吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040540V#000F#3P嗯……\n',
            '不过我两只手都拿着东西，不太方便……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040541V约修亚你喂我吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040542V#014F我喂你……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040543V#001F#3P当然啦，啊～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040544V#018F这样……\n',
            '我觉得有点不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040545V#006F#3P怕什么呀。\n',
            '反正这里又没人看着我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040546V就像小孩子玩过家家那样，\n',
            '有什么不好意思的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040547V#017F……我说的不好意思\n',
            '并不是你那种不好意思啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040548V算了，真拿你没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚舀了一勺饭，\n',
            '轻轻地喂进艾丝蒂尔的嘴里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010040549V#502F#3P呷咕～呷咕～呷咕……咕咚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040550V#501F嗯～太好吃啦㈱\n',
            '这简直是海岸乡村料理的代表作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040551V怎么说呢，\n',
            '这里的花香总能刺激起我的食欲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040552V#010F知道啦知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040553V#009F#3P怎么听起来这么不情愿啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040554V#001F嘿～让你也尝尝我的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔向约修亚的嘴里\n',
            '硬塞了一大团吃剩的三明治。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020040555V#014F啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040556V#015F嚼嚼嚼……嚼嚼嚼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040557V#018F……好吃是好吃……\n',
            '不过也不要突然塞这么多给我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040558V#502F#3P哼哼哼，我偏要⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(5600, 6150, -15410, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(225000, 0)
    OP_6E(261, 0)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrPos(0x0101, 5150, 6150, -14900, 180)
    SetChrPos(0x0102, 6010, 6000, -14900, 180)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010040559V#001F哈～实在是太好吃啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040560V#010F嗯，就连附送的\n',
            '那杯香草茶也十分甘甜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040561V#501F嗯，喝了之后很舒服呢，\n',
            '感觉身体也开始暖和起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040562V#007F海风吹过来也很舒服……\n',
            '总觉得有点想睡觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040563V#010F吃饱了就睡\n',
            '很容易胖得像小猪一样哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040564V不过吃完饭后偶尔午睡一下，\n',
            '倒也不是什么坏事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040565V#501F嗯嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040566V#004F……啊，那是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    PlaySE(140, 0x00, 0x64)
    OP_12(0x00009470, 0x00020F58, 0x00000000)
    OP_6C(0, 0)

    @scena.Lambda('lambda_3B74')
    def lambda_3B74():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_3B74')

    DispatchAsync2(0x0102, 0x0001, lambda_3B74)

    @scena.Lambda('lambda_3B85')
    def lambda_3B85():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_3B85')

    DispatchAsync2(0x0101, 0x0001, lambda_3B85)

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearChrFlags(0x0009, 0x0001)
    SetChrPos(0x0009, -15000, 15680, -15710, 0)
    OP_69(0x0009, 0)
    OP_6A(0x0009)

    @scena.Lambda('lambda_3BC1')
    def lambda_3BC1():
        CameraSetDistance(4000, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3BC1)

    @scena.Lambda('lambda_3BD1')
    def lambda_3BD1():
        OP_6C(300000, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3BD1)

    ClearChrFlags(0x0009, 0x0080)
    ChrWalkTo(0x0009, 19800, 11500, -12310, 13000, 0x00)
    ChrWalkTo(0x0009, 39700, 11500, -110, 13000, 0x00)
    ChrWalkTo(0x0009, 55300, 14700, 6090, 13000, 0x00)
    Fade(1000)
    SetChrFlags(0x0009, 0x0080)
    OP_6A(0x0000)
    ClearMapFlags(0x00000001)
    SetChrPos(0x0101, 9310, 6140, -12420, 90)
    SetChrPos(0x0102, 8940, 6140, -13650, 90)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    CameraMove(8900, 6000, -13650, 0)
    CameraSetDistance(3000, 0)
    OP_6C(51000, 0)
    OP_67(0, 9500, -10000, 0)
    OP_12(0x00009470, 0x00014C08, 0x00000000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010040567V#004F看，刚才那只鸟！\n',
            '就算是海鸥也太大了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040568V#010F#4P是啊。\n',
            '翅膀的形状也不同，嘴也锋利很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040569V应该是鹰吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040570V#000F白色的鹰……\n',
            '还真是少见啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040571V#001F嘿嘿！\n',
            '总觉得一会儿会遇到什么好事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040572V#019F#4P呵呵，如果是就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040573V#010F对了艾丝蒂尔……\n',
            '你已经没有睡意了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040574V#008F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040575V嗯……已经不困了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040576V#010F#4P那么，我们也该出发了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040577V争取今天下午到达卢安，\n',
            '然后办理支部的转属手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040578V#000F说的也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040579V嗯，好吧。\n',
            '虽然有点舍不得，不过还是赶快出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    RemoveItem(0x033C, 1)
    SetScenaFlags(ScenaFlag(0x0081, 3, 0x40B))
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)

    def _loc_3F1A(): pass

    label('loc_3F1A')

    Return()

# id: 0x0014 offset: 0x3F1B
@scena.Code('func_14_3F1B')
def func_14_3F1B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4A68',
    )

    SetScenaFlags(ScenaFlag(0x0081, 4, 0x40C))
    EventBegin(0x00)
    FadeOut(500, 0, -1)
    OP_0D()
    CameraMove(4130, 3990, 10660, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 4590, 5970, 3440, 0)
    SetChrPos(0x0102, 5510, 5980, 2610, 0)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0040)
    SetChrPos(0x000A, 180, 4050, 18030, 152)
    FadeIn(500, 0)

    @scena.Lambda('lambda_3FC0')
    def lambda_3FC0():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_3FC0')

    DispatchAsync2(0x0101, 0x0003, lambda_3FC0)

    @scena.Lambda('lambda_3FD1')
    def lambda_3FD1():
        ChrWalkTo(0x00FE, 4300, 3970, 11420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3FD1)

    Sleep(500)

    @scena.Lambda('lambda_3FF1')
    def lambda_3FF1():
        ChrWalkTo(0x00FE, 5220, 4010, 9680, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3FF1)

    Sleep(1200)

    @scena.Lambda('lambda_4011')
    def lambda_4011():
        ChrWalkTo(0x00FE, 4260, 3980, 11980, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4011)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(125, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    ChrTurnDirection(0x000A, 0x0101, 0)

    @scena.Lambda('lambda_404C')
    def lambda_404C():
        ChrJumpTo(0x00FE, 4390, 3980, 10420, 500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_404C)

    @scena.Lambda('lambda_406A')
    def lambda_406A():
        ChrJumpTo(0x00FE, 4360, 3960, 13150, 500, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_406A)

    CreateThread(0x0101, 0x02, 0x00, 0x0015)
    RemoveItem(0x035C, 1)

    ChrTalk(
        0x000A,
        (
            '#774F#4P#12A哇哇！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010040581V#004F#1P#12A啊……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010040582V#007F呜……\n',
            '怎么今天老是和别人撞个正着呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x000A, 0x0004)
    ChrWalkTo(0x000A, 4430, 3990, 11580, 3000, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0400040583V#771F不好意思啦。\n',
            '我正在找人，没留意周围。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040584V#770F哎，\n',
            '姐姐你们好像不是这里的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(400)
    SetChrChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010040585V#000F说得没错。\n',
            '我们是从别的地方来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040586V#004F啊，你难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0400040587V#772F……怎、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040588V#501F刚才有个穿校服的女生\n',
            '说她在找一个戴帽子的男孩子……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040589V是不是就是你啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0400040590V#770F啊……对对。\n',
            '我刚才也是一直在找她呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040591V你们是在哪儿见到她的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040592V#000F在旅馆附近……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040593V不过这是刚才的事情，\n',
            '她现在在哪我就不清楚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040594V我们也来帮你找那个女生吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0400040595V#774F不、不用了。\n',
            '我等一下自己去找就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrJumpToRelative(0x000A, 0, 0, 0, 800, 6000)

    ChrTalk(
        0x000A,
        (
            '#0400040596V#771F我先走了，拜拜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 90, 400)

    @scena.Lambda('lambda_43DE')
    def lambda_43DE():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_43DE')

    DispatchAsync2(0x0102, 0x0003, lambda_43DE)

    @scena.Lambda('lambda_43EF')
    def lambda_43EF():
        CameraMove(7160, 4030, 12560, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_43EF)

    ChrWalkTo(0x000A, 16840, 1720, 14680, 6000, 0x00)
    SetChrFlags(0x000A, 0x0080)
    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010040597V#501F好活泼的男孩子哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040598V感觉他和洛连特的鲁克\n',
            '在某些方面有点相像呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040599V不知道鲁克那小子现在在干什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    @scena.Lambda('lambda_44BF')
    def lambda_44BF():
        CameraMove(4380, 4019, 9800, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_44BF)

    TerminateThread(0x0101, 0x03)
    SetChrDirection(0x0101, 90, 400)
    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010040600V#004F#2P约修亚，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0102)
    TerminateThread(0x0102, 0x03)
    SetChrDirection(0x0102, 0, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040601V#014F#1P啊……\n',
            '也许是我多心了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040602V艾丝蒂尔，你有没有丢掉什么东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040603V#004F#2P丢掉？什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040604V#012F#1P看看身上有没有什么东西不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040605V钱包或者饰物之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040606V#004F#2P什么呀，又不是遇到了小偷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040607V#006F钱包……在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040608V头饰……也在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040609V#501F游击士的徽章……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040610V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020040611V#015F#1P果然是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040612V#004F#2P啊啊啊啊～～～～？\n',
            '怎么会这样呢！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040613V难道是下山的时候\n',
            '不小心弄丢的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040614V#012F#1P冷静点，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040615V刚才吃午餐的时候，\n',
            '徽章还好好地贴在你左边的胸前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040616V就算是不见了，\n',
            '也应该是在这附近弄丢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrDirection(0x0101, 180, 400)
    Sleep(200)

    SetChrDirection(0x0101, 270, 400)
    Sleep(200)

    SetChrDirection(0x0101, 0, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010040617V#002F#2P可、可是……\n',
            '会是在哪里弄丢的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040618V#004F#2P难、难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040619V#010F#1P嗯，很可能是刚才那个男孩子做的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040620V我觉得他撞到你的时候很不自然，\n',
            '所以才想到会不会是他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040621V#005F#2P你、你说什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040622V为、为什么\n',
            '他要偷我的游击士徽章啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040623V#015F#1P的确……\n',
            '小孩子拿着那东西也没什么用处。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040624V所以恶作剧的可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040625V#009F#2P呜呜呜呜～……\n',
            '这个可恶的调皮蛋，我绝对不放过他！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040626V#005F要是被我抓到的话，\n',
            '一定要好好教训教训他！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040627V#010F#1P呵呵，对小孩子可要手下留情哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040628V总之，\n',
            '我们先在这附近找找那孩子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_4A68(): pass

    label('loc_4A68')

    Return()

# id: 0x0015 offset: 0x4A69
@scena.Code('func_15_4A69')
def func_15_4A69():
    Sleep(200)

    SetChrChipByIndex(0x0101, 14)

    Return()

# id: 0x0016 offset: 0x4A74
@scena.Code('func_16_4A74')
def func_16_4A74():
    EventBegin(0x00)
    CameraMove(26870, 100, 17110, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000D, 39130, -90, 16600, 270)
    SetChrPos(0x0101, 26280, 40, 17460, 180)
    SetChrPos(0x0102, 26250, 70, 16210, 0)
    SetChrPos(0x0136, 27640, 40, 17110, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010050481V#002F话说回来，\n',
            '这件事还真是不好办……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050482V我们要从哪里开始搜查好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050483V#012F#4P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050484V总之先回协会\n',
            '向嘉恩先生报告一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050485V然后再定出搜查方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050486V#006F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050487V#049F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0136, 400)
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050488V#004F哎？你没事吧？\n',
            '怎么发起呆来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050489V#045F啊，对不起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050490V我觉得自己脑子稍微有点乱……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050491V#003F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050492V#501F对了，\n',
            '约瑟夫是特蕾莎院长的丈夫吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050493V#048F是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050494V不过他在几年前已经去世了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050495V我小的时候，\n',
            '他和老师一样也非常疼我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050496V#000F是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050497V#004F咦？那就是说……\n',
            '科洛丝也是在孤儿院长大的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050498V#045F不是呢，并不是这个意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050499V其实在很久以前，\n',
            '因为一些事情受到他们的照顾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050500V当我进了王立学院，\n',
            '也就是我来了卢安之后，\n',
            '就和老师他们越来越亲近了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050501V#501F原来是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050502V#010F所以你就常来玩，\n',
            '也顺便帮忙照顾那些孩子是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050503V#048F是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050504V#047F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050505V#049F和老师还有孩子们比起来，\n',
            '其实我所受到的打击\n',
            '根本就不算什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050506V所以我也要打起精神来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050507V#3P科洛丝姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0136, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_4A(0x000D, 255)
    ClearChrFlags(0x000D, 0x0080)

    @scena.Lambda('lambda_4F97')
    def lambda_4F97():
        CameraMove(28370, 100, 17960, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4F97)

    @scena.Lambda('lambda_4FAF')
    def lambda_4FAF():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_4FAF')

    DispatchAsync2(0x0136, 0x0001, lambda_4FAF)

    @scena.Lambda('lambda_4FC0')
    def lambda_4FC0():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_4FC0')

    DispatchAsync2(0x0101, 0x0001, lambda_4FC0)

    @scena.Lambda('lambda_4FD1')
    def lambda_4FD1():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_4FD1')

    DispatchAsync2(0x0102, 0x0001, lambda_4FD1)

    OP_62(0x000D, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x000D, 29080, -120, 17280, 5000, 0x00)

    ChrTalk(
        0x0136,
        (
            '#0060050508V#044F玛丽。\n',
            '怎么了，慌成这样子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050509V那个、那个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050510V克拉姆那家伙\n',
            '不知跑到哪儿去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050511V#043F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050512V#004F不、不知跑到哪儿去了，\n',
            '难道是跑出玛诺利亚村了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050513V#012F能说得详细点吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050514V啊，好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050515V那两个叔叔来了之后，\n',
            '克拉姆就跑上了二楼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050516V然后一会儿就下来了，脸涨得通红，\n',
            '嘴里说着『饶不了他们！』什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050517V气冲冲地跑了出去呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050518V#002F饶不了他们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050519V这、这难道是指……！',
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
            TXT(0x00, '【放火烧孤儿院的犯人】\n'),
            TXT(0x01, '【戴尔蒙市长和他的秘书】\n'),
            TXT(0x02, '【仓库一带的那帮流氓】\n'),
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
        (0x00000000, 'loc_528C'),
        (0x00000001, 'loc_5326'),
        (0x00000002, 'loc_53BE'),
        (-1, 'loc_5433'),
    )

    def _loc_528C(): pass

    label('loc_528C')

    ChrTalk(
        0x0102,
        (
            '#0020050520V#012F那是肯定的，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050521V在这种情况下，\n',
            '应该是指『渡鸦帮』的那帮家伙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050522V那孩子大概是听见了\n',
            '基尔巴特秘书所说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x003B, 0x0001)

    Jump('loc_5433')

    def _loc_5326(): pass

    label('loc_5326')

    ChrTalk(
        0x0102,
        (
            '#0020050523V#017F你怎么会这么想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050524V#012F在这种情况下，\n',
            '应该是指『渡鸦帮』的那帮家伙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050525V那孩子大概是听见了\n',
            '基尔巴特秘书所说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5433')

    def _loc_53BE(): pass

    label('loc_53BE')

    ChrTalk(
        0x0102,
        (
            '#0020050526V#013F嗯……\n',
            '应该就是指『渡鸦帮』的那帮流氓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050527V那孩子大概是听见了\n',
            '基尔巴特秘书所说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x003B, 0x0002)

    Jump('loc_5433')

    def _loc_5433(): pass

    label('loc_5433')

    ChrTalk(
        0x0101,
        (
            '#0010050528V#004F那、那不就糟了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050529V那孩子该不会是想\n',
            '闯到那帮流氓的地盘去吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0136, 0xFF)
    SetChrDirection(0x0136, 270, 400)

    ChrTalk(
        0x0136,
        (
            '#0060050530V#043F#2P怎、怎么会这样……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050531V#042F不能让他这么做！\n',
            '我要立刻去阻止他才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050532V#012F我们也一起去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050533V如果快一点的话， \n',
            '或许能在他到达卢安之前追上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050534V科洛丝姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_556C')
    def lambda_556C():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_556C')

    DispatchAsync2(0x0136, 0x0001, lambda_556C)

    Sleep(400)

    ChrTalk(
        0x0136,
        (
            '#0060050535V#042F不用担心。\n',
            '我们一定会把克拉姆带回来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050536V玛丽你要照顾好\n',
            '其他的孩子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0410050537V是啊……\n',
            '哥哥姐姐，拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5609')
    def lambda_5609():
        CameraMove(26760, 100, 17100, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5609)

    ChrWalkTo(0x000D, 27490, 500, 19110, 3000, 0x00)
    SetChrDirection(0x000D, 0, 400)
    OP_70(0x0004, 30)
    OP_73(0x0004)
    SetChrFlags(0x000D, 0x0004)
    ChrWalkTo(0x000D, 27900, 500, 21200, 3000, 0x00)
    SetChrFlags(0x000D, 0x0080)
    OP_72(0x0004, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0004, 30)
    OP_70(0x0004, 0)
    OP_71(0x0004, 0x0800)
    OP_73(0x0004)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0136, 0xFF)
    ChrTurnDirection(0x0102, 0x0136, 400)
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050538V#002F那我们赶快回卢安吧！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0136, 270, 400)

    ChrTalk(
        0x0136,
        (
            '#0060050539V#042F好的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x56E7
@scena.Code('func_17_56E7')
def func_17_56E7():
    EventBegin(0x00)
    OP_77(0x41, 0x64, 0x82, 0x00, 0x00000000)
    CameraMove(27410, 20, 17820, 0)
    OP_6C(315000, 0)
    SetChrChipByIndex(0x0106, 16)
    SetChrPos(0x0106, 27180, 500, 20940, 0)
    SetChrPos(0x0101, 27180, 500, 20940, 0)
    SetChrPos(0x0102, 27180, 500, 20940, 0)
    SetChrPos(0x0105, 27180, 500, 20940, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_70(0x0004, 30)
    OP_73(0x0004)

    @scena.Lambda('lambda_576F')
    def lambda_576F():
        ChrWalkTo(0x00FE, 27640, 0, 16800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_576F)

    Sleep(500)

    @scena.Lambda('lambda_578F')
    def lambda_578F():
        ChrWalkTo(0x00FE, 26900, 0, 17590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_578F)

    Sleep(500)

    @scena.Lambda('lambda_57AF')
    def lambda_57AF():
        ChrWalkTo(0x00FE, 28760, 0, 17460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_57AF)

    Sleep(500)

    @scena.Lambda('lambda_57CF')
    def lambda_57CF():
        ChrWalkTo(0x00FE, 27890, 0, 18190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_57CF)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#004F哇，都已经这么晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0106, 0x0001)
    OP_6F(0x0004, 30)
    OP_70(0x0004, 0)

    ChrTalk(
        0x0106,
        (
            '#057F嘁……不好办了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061098V这么暗，\n',
            '能查出些什么来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, 16500, 6000, 10000, 0)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '此时能听到基库的叫声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0106, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_5903')
    def lambda_5903():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5903)

    @scena.Lambda('lambda_5911')
    def lambda_5911():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5911)

    @scena.Lambda('lambda_591F')
    def lambda_591F():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_591F)

    @scena.Lambda('lambda_592D')
    def lambda_592D():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_592D)

    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050061099V#052F那是什么，刚才那声鸟鸣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ClearChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_5976')
    def lambda_5976():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_5976)

    @scena.Lambda('lambda_5986')
    def lambda_5986():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_5986')

    DispatchAsync2(0x0101, 0x0001, lambda_5986)

    @scena.Lambda('lambda_5997')
    def lambda_5997():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_5997')

    DispatchAsync2(0x0102, 0x0001, lambda_5997)

    @scena.Lambda('lambda_59A8')
    def lambda_59A8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_59A8')

    DispatchAsync2(0x0106, 0x0001, lambda_59A8)

    OP_92(0x0009, 0x0136, 5000, 10000, 0x00)
    OP_92(0x0009, 0x0136, 4000, 8000, 0x00)
    OP_92(0x0009, 0x0136, 3000, 6000, 0x00)
    OP_92(0x0009, 0x0136, 2000, 3000, 0x00)
    TerminateThread(0x0106, 0x01)
    SetChrDirection(0x0106, 180, 0)
    ChrWalkTo(0x0009, 29330, 900, 16860, 1500, 0x00)
    TerminateThread(0x0101, 0x01)
    SetChrDirection(0x0101, 45, 0)

    @scena.Lambda('lambda_5A1B')
    def lambda_5A1B():
        SetChrDirection(0x00FE, 270, 200)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_5A1B)

    SetChrChipByIndex(0x0105, 15)
    SetChrSubChip(0x0105, 3)
    SetChrFlags(0x0105, 0x0020)
    SetChrDirection(0x0105, 225, 200)
    ChrMoveTo(0x0009, 29220, 100, 17090, 1000, 0x00)
    WaitForThreadExit(0x0009, 0x0003)
    Sleep(100)

    Fade(250)
    SetChrFlags(0x0009, 0x0080)
    SetChrSubChip(0x0105, 1)
    SetChrFlags(0x0105, 0x0020)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060061100V#044F啊，基库……\n',
            '你跑到哪儿去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061101V#055F这、这家伙是什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061102V#006F#4P是科洛丝的朋友，\n',
            '白隼基库啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061103V#055F哈啊……朋友……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0440061104V#310F啾！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0440061105V啾，啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061106V#047F是吗……我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061107V#042F谢谢呢，基库。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0440061108V#311F啾☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#053F还真是优哉游哉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061110V#051F那么，这位小姑娘。\n',
            '你那位朋友说了些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061111V#042F基库应该能帮我们\n',
            '找到那些袭击老师的犯人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061112V老师他们受到袭击的时候，\n',
            '似乎刚好被它看见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061113V#051F哈哈哈！\n',
            '这玩笑真有趣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061114V#006F#4P好样的！不愧是基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F#3P嗯，立大功了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0440061116V#311F啾～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050061117V#055F喂，等等！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061118V你们该不会\n',
            '连这鸟乱叫的话都信吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F#3P因为我们已经\n',
            '亲眼见识过好几次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061120V#006F#4P你不相信的话，\n',
            '可以不跟我们一起走哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061121V科洛丝、基库，我们走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0440061123V#310F啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x0009, 0x0080)
    SetChrSubChip(0x0105, 3)
    SetChrDirection(0x0105, 270, 0)

    @scena.Lambda('lambda_5E17')
    def lambda_5E17():
        ChrWalkTo(0x00FE, 16500, 6000, 13700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5E17)

    Sleep(100)

    @scena.Lambda('lambda_5E37')
    def lambda_5E37():
        ChrWalkTo(0x00FE, 16500, 6000, 13700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5E37)

    Sleep(100)

    @scena.Lambda('lambda_5E57')
    def lambda_5E57():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_5E57')

    DispatchAsync2(0x0101, 0x0001, lambda_5E57)

    @scena.Lambda('lambda_5E68')
    def lambda_5E68():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_5E68')

    DispatchAsync2(0x0102, 0x0001, lambda_5E68)

    SetChrChipByIndex(0x0105, 65535)
    ClearChrFlags(0x0105, 0x0020)
    SetChrSubChip(0x0105, 0)

    @scena.Lambda('lambda_5E88')
    def lambda_5E88():
        ChrWalkTo(0x00FE, 16500, 6000, 13700, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5E88)

    Sleep(100)

    @scena.Lambda('lambda_5EA8')
    def lambda_5EA8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_5EA8')

    DispatchAsync2(0x0106, 0x0001, lambda_5EA8)

    @scena.Lambda('lambda_5EB9')
    def lambda_5EB9():
        ChrWalkTo(0x00FE, 16500, 6000, 13700, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5EB9)

    Sleep(100)

    @scena.Lambda('lambda_5ED9')
    def lambda_5ED9():
        ChrWalkTo(0x00FE, 16500, 6000, 13700, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5ED9)

    Sleep(500)

    TerminateThread(0x0101, 0xFF)

    @scena.Lambda('lambda_5EFD')
    def lambda_5EFD():
        ChrWalkTo(0x00FE, 11620, 4030, 14980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5EFD)

    Sleep(500)

    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_5F21')
    def lambda_5F21():
        ChrWalkTo(0x00FE, 11620, 4030, 14980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5F21)

    Sleep(100)

    @scena.Lambda('lambda_5F41')
    def lambda_5F41():
        ChrWalkTo(0x00FE, 11620, 4030, 14980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5F41)

    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050061124V#055F………我～说…………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061125V#054F喂、喂，你们这些小鬼，等等！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_62(0x0106, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_5FD3')
    def lambda_5FD3():
        ChrWalkTo(0x00FE, 11620, 4030, 14980, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_5FD3)

    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    SetMapFlags(0x02000000)
    ClearMapFlags(0x10000000)
    NewScene('ED6_DT01/R2101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x6000
@scena.Code('func_18_6000')
def func_18_6000():
    EventBegin(0x00)
    OP_B8(0x05)
    FormationDelMember(0x05, 0xFF)
    SetChrPos(0x0101, 6920, 5980, -1940, 225)
    SetChrPos(0x0102, 6130, 6000, -1360, 180)
    SetChrPos(0x0105, 7280, 5980, -2810, 270)
    SetChrDirection(0x0014, 45, 0)
    OP_4A(0x0014, 255)
    CameraMove(5680, 6000, -2120, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0014,
        (
            '#0320061335V#830F好了……\n',
            '那帮家伙由我看着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061336V你们就赶去卢安，\n',
            '向嘉恩报告昨天的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061337V#004F#4P我们倒是没关系，不过……\n',
            '卡露娜姐姐您已经没事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0320061338V#831F当然啦。只是被人抓住破绽，\n',
            '熏了点催眠药而已嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061339V#835F不过这次事出突然，\n',
            '我已经不记得对方是什么样的人了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061340V还真是丢脸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061341V#010F这也不能怪您。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061342V我们也是四人联手\n',
            '才勉强击退那些犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061343V#040F那些孩子们平安无事，\n',
            '也都多亏了卡露娜小姐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061344V真是太感谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0320061345V#835F哈哈……\n',
            '是啊，总算是不幸中的大幸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061346V#833F我听说阿加特\n',
            '自己一个人去追那帮家伙了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061347V虽然他的身手不容置疑，\n',
            '但说到底还是有点担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061348V#003F#4P嗯、嗯……\n',
            '要是没捉到他们反而受伤的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061349V#015F现在也唯有相信阿加特兄了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061350V从昨天他所说的话判断，\n',
            '他好像一直在追那些犯人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061351V#010F对于他们的做事手法似乎也很了解，\n',
            '我想应该不会那么轻易失手的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061352V#006F#4P嗯……也对呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061353V所以，我们现在也应该\n',
            '尽力做好自己能做的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0320061354V#830F没错，就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061355V在事情了结之前，\n',
            '这些属于特蕾莎院长的捐款\n',
            '就先由我来暂代保管吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320061356V这次我一定会保护好的，\n',
            '所以你们就安心出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061357V#041F好的，拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061358V#006F#4P那么，我们走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    SetChrDirection(0x0014, 90, 400)
    OP_4B(0x0014, 255)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x657E
@scena.Code('func_19_657E')
def func_19_657E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 1, 0x409)),
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_667B',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6636',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040398V#000F我说，已经中午了。\n',
            '我们找个地方休息一下吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040399V吃过午饭再出发怎么样？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040400V#010F好啊。\n',
            '先去找个吃饭的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6674')

    def _loc_6636(): pass

    label('loc_6636')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040401V#000F等会儿再出发，\n',
            '先去找个吃饭的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6674(): pass

    label('loc_6674')

    Call(0, 0x001A)

    Jump('loc_69E1')

    def _loc_667B(): pass

    label('loc_667B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_66EF',
    )

    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040402V#010F这边是通往街道的出口啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040403V瞭望台应该是在\n',
            '村子里风车小屋的方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x001A)

    Jump('loc_69E1')

    def _loc_66EF(): pass

    label('loc_66EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_67C5',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_675E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040404V#012F首先调查一下\n',
            '那个孩子去哪儿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040405V然后再开始追踪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67BE')

    def _loc_675E(): pass

    label('loc_675E')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040406V#012F首先调查一下\n',
            '那个孩子去哪儿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040407V先向村民询问一下会比较稳妥。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_67BE(): pass

    label('loc_67BE')

    Call(0, 0x001A)

    Jump('loc_69E1')

    def _loc_67C5(): pass

    label('loc_67C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6927',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6862',
    )

    ChrTalk(
        0x0106,
        (
            '#0050040408V#050F已经没有时间回卢安去了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040409V嘁，没办法了。\n',
            '虽然觉得像被捉弄了一样，\n',
            '不过现在也只有赌在那个基库上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6920')

    def _loc_6862(): pass

    label('loc_6862')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050040410V#050F等等，你们要去哪儿呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040411V已经没有时间再回卢安去了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_68BD')
    def lambda_68BD():
        ChrTurnDirection(0x0105, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_68BD)

    @scena.Lambda('lambda_68CB')
    def lambda_68CB():
        ChrTurnDirection(0x0101, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_68CB)

    ChrTurnDirection(0x0102, 0x0106, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040412V#012F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040413V现在只能相信基库，\n',
            '跟在它后面追踪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6920(): pass

    label('loc_6920')

    Call(0, 0x001A)

    Jump('loc_69E1')

    def _loc_6927(): pass

    label('loc_6927')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_69E1',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6999',
    )

    ChrTalk(
        0x0106,
        (
            '#0050040414V#050F已经没有绕远路的时间了啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040415V赶快回灯塔去\n',
            '把这件事搞定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69DD')

    def _loc_6999(): pass

    label('loc_6999')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050040416V#050F喂，你们去哪儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040417V还是快点到灯塔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_69DD(): pass

    label('loc_69DD')

    Call(0, 0x001A)

    def _loc_69E1(): pass

    label('loc_69E1')

    Return()

# id: 0x001A offset: 0x69E2
@scena.Code('func_1A_69E2')
def func_1A_69E2():
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x001B offset: 0x69FE
@scena.Code('func_1B_69FE')
def func_1B_69FE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A72',
    )

    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040629V#010F这边是通往街道的出口啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040630V瞭望台应该是在\n',
            '村子里风车小屋的方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x001C)

    Jump('loc_6D15')

    def _loc_6A72(): pass

    label('loc_6A72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6B48',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6AE1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040631V#012F首先调查一下\n',
            '那个孩子去哪儿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040632V然后再开始追踪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B41')

    def _loc_6AE1(): pass

    label('loc_6AE1')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040633V#012F首先调查一下\n',
            '那个孩子去哪儿了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040634V先向村民询问一下会比较稳妥。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B41(): pass

    label('loc_6B41')

    Call(0, 0x001C)

    Jump('loc_6D15')

    def _loc_6B48(): pass

    label('loc_6B48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6C8C',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6BC2',
    )

    ChrTalk(
        0x0101,
        (
            '#0010040635V#002F啊……\n',
            '这边是古罗尼连峰的方向啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040636V要回卢安的话\n',
            '必须走东面那条海道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C85')

    def _loc_6BC2(): pass

    label('loc_6BC2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C2B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020040637V#012F这边是玛诺利亚间道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040638V要回卢安的话，\n',
            '必须走东面的那条梅威海道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C85')

    def _loc_6C2B(): pass

    label('loc_6C2B')

    ChrTalk(
        0x0105,
        (
            '#0060040639V#042F这边是玛诺利亚间道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040640V要去卢安的话，\n',
            '必须走东面出口的梅威海道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C85(): pass

    label('loc_6C85')

    Call(0, 0x001C)

    Jump('loc_6D15')

    def _loc_6C8C(): pass

    label('loc_6C8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D15',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CB0',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_6CB7')

    def _loc_6CB0(): pass

    label('loc_6CB0')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_6CB7(): pass

    label('loc_6CB7')

    ChrTalk(
        0x0102,
        (
            '#0020040641V#012F这边是间道的出口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040642V先去找特蕾莎老师吧，\n',
            '她一定在玛诺利亚村里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x001C)

    def _loc_6D15(): pass

    label('loc_6D15')

    Return()

# id: 0x001C offset: 0x6D16
@scena.Code('func_1C_6D16')
def func_1C_6D16():
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x001D offset: 0x6D32
@scena.Code('func_1D_6D32')
def func_1D_6D32():
    OP_13(0x0058)

    Return()

# id: 0x001E offset: 0x6D36
@scena.Code('func_1E_6D36')
def func_1E_6D36():
    OP_13(0x0057)

    Return()

# id: 0x001F offset: 0x6D3A
@scena.Code('func_1F_6D3A')
def func_1F_6D3A():
    OP_13(0x0059)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
