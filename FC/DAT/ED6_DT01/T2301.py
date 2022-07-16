import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2301   ._SN')

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
    TXT(0x0D, '玛诺利亚间道方向'),
    TXT(0x0E, '梅威海道方向'),
    TXT(0x0F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2301.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2301._SN', 'ED6_DT01/T2300_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x553B
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
    ]

# id: 0x10002 offset: 0x13A
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
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 46980,
            z                   = 0,
            y                   = 22480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            talkScenaIndex      = 0x0007,
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
            talkScenaIndex      = 0x0005,
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
            talkScenaIndex      = 0x0008,
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
            talkScenaIndex      = 0x0009,
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

# id: 0x10003 offset: 0x2FA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2FA
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
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 8200,
            y           = 4000,
            z           = 9300,
            range       = 1460,
            dword_10    = 0x0000178E,
            dword_14    = 0x0000198C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = 65500,
            y           = -1000,
            z           = 23100,
            range       = 68250,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00004736,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000012,
        ),
        ScenaEventData(
            x           = -760,
            y           = 5000,
            z           = 59750,
            range       = -5380,
            dword_10    = 0x00002670,
            dword_14    = 0x0000F4D8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000014,
        ),
        ScenaEventData(
            x           = 27540,
            y           = 0,
            z           = 18980,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 53410,
            y           = 0,
            z           = 22710,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 6000,
            y           = 4000,
            z           = 20210,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000018,
        ),
    )

# id: 0x10005 offset: 0x3DA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x3DA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3E4',
    )

    Jump('loc_4AF')

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_3F8',
    )

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0011, 0x0008)

    Jump('loc_4AF')

    def _loc_3F8(): pass

    label('loc_3F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_476',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -2050, 3970, 31120, 0)
    CreateThread(0x000B, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -5690, 4160, 30210, 0)
    CreateThread(0x000D, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, -3290, 3990, 27420, 0)
    CreateThread(0x0012, 0x00, 0x00, 0x0003)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, -5420, 4000, 27290, 0)
    CreateThread(0x0013, 0x00, 0x00, 0x0003)

    Jump('loc_4AF')

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_480',
    )

    Jump('loc_4AF')

    def _loc_480(): pass

    label('loc_480')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_48A',
    )

    Jump('loc_4AF')

    def _loc_48A(): pass

    label('loc_48A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_494',
    )

    Jump('loc_4AF')

    def _loc_494(): pass

    label('loc_494')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_49E',
    )

    Jump('loc_4AF')

    def _loc_49E(): pass

    label('loc_49E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_4A8',
    )

    Jump('loc_4AF')

    def _loc_4A8(): pass

    label('loc_4A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_4AF',
    )

    def _loc_4AF(): pass

    label('loc_4AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4D7',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x04)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x001F, 0x01, 0x0002)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4D7',
    )

    ClearChrFlags(0x000E, 0x0080)

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_4E5',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0010)

    def _loc_4E5(): pass

    label('loc_4E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_501',
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
    Event(0, 0x0011)

    def _loc_501(): pass

    label('loc_501')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_511'),
        (0x00000069, 'loc_54D'),
        (-1, 'loc_560'),
    )

    def _loc_511(): pass

    label('loc_511')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 1, 0x409)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_523',
    )

    SetScenaFlags(ScenaFlag(0x0081, 1, 0x409))
    Event(0, 0x000A)

    Jump('loc_54A')

    def _loc_523(): pass

    label('loc_523')

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
        'loc_54A',
    )

    OP_28(0x001F, 0x04, 0x10)
    OP_28(0x001F, 0x01, 0x0008)
    FormationDelMember(0x36, 0xFF)
    Event(1, 0x0001)

    def _loc_54A(): pass

    label('loc_54A')

    Jump('loc_560')

    def _loc_54D(): pass

    label('loc_54D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 2, 0x40A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_55D',
    )

    Event(0, 0x000B)

    def _loc_55D(): pass

    label('loc_55D')

    Jump('loc_560')

    def _loc_560(): pass

    label('loc_560')

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

# id: 0x0001 offset: 0x572
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -108000, -126000, 196683)
    PlaySE(453, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x58A
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_59F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_59F(): pass

    label('loc_59F')

    Return()

# id: 0x0003 offset: 0x5A0
@scena.Code('func_03_5A0')
def func_03_5A0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C3',
    )

    OP_8D(0x00FE, -6100, 32000, 300, 25200, 3000)

    Jump('func_03_5A0')

    def _loc_5C3(): pass

    label('loc_5C3')

    Return()

# id: 0x0004 offset: 0x5C4
@scena.Code('func_04_5C4')
def func_04_5C4():
    TalkBegin(0x000C)

    ChrTalk(
        0x000C,
        (
            '等忙完了店的事情\n',
            '我也要去看看孩子们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x0005 offset: 0x5F6
@scena.Code('func_05_5F6')
def func_05_5F6():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_69F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '那些看起来很凶的叔叔\n',
            '到底是什么人啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '欺负波利他们的\n',
            '难道就是那些人？',
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

    Jump('loc_69C')

    def _loc_67D(): pass

    label('loc_67D')

    ChrTalk(
        0x00FE,
        (
            '欺负大家的人，\n',
            '不能原谅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_69C(): pass

    label('loc_69C')

    Jump('loc_B56')

    def _loc_69F(): pass

    label('loc_69F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_715',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6FC',
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

    Jump('loc_712')

    def _loc_6FC(): pass

    label('loc_6FC')

    ChrTalk(
        0x00FE,
        (
            '是谁欺负他们了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_712(): pass

    label('loc_712')

    Jump('loc_B56')

    def _loc_715(): pass

    label('loc_715')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_79C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_77A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '和波利他们在一起，\n',
            '卢希娅每天玩得都很愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我交了好多朋友，\n',
            '真开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_799')

    def _loc_77A(): pass

    label('loc_77A')

    ChrTalk(
        0x00FE,
        (
            '我交了好多朋友，\n',
            '真开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_799(): pass

    label('loc_799')

    Jump('loc_B56')

    def _loc_79C(): pass

    label('loc_79C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_83B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_801',
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

    Jump('loc_838')

    def _loc_801(): pass

    label('loc_801')

    ChrTalk(
        0x00FE,
        (
            '克拉姆是不是又做了什么坏事，\n',
            '惹特蕾莎老师生气了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_838(): pass

    label('loc_838')

    Jump('loc_B56')

    def _loc_83B(): pass

    label('loc_83B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_90B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8AE',
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

    Jump('loc_908')

    def _loc_8AE(): pass

    label('loc_8AE')

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

    def _loc_908(): pass

    label('loc_908')

    Jump('loc_B56')

    def _loc_90B(): pass

    label('loc_90B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_9BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_98C',
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
            '卢希娅也想和他们交朋友啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9BB')

    def _loc_98C(): pass

    label('loc_98C')

    ChrTalk(
        0x00FE,
        (
            '卢希娅也想和\n',
            '孤儿院的孩子们成为好朋友啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9BB(): pass

    label('loc_9BB')

    Jump('loc_B56')

    def _loc_9BE(): pass

    label('loc_9BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_A26',
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

    Jump('loc_B56')

    def _loc_A26(): pass

    label('loc_A26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Return,
        ),
        'loc_ABF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A8F',
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

    Jump('loc_ABC')

    def _loc_A8F(): pass

    label('loc_A8F')

    ChrTalk(
        0x00FE,
        (
            '那个男孩子，\n',
            '我好像在花店那里看到过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ABC(): pass

    label('loc_ABC')

    Jump('loc_B56')

    def _loc_ABF(): pass

    label('loc_ABF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_B56',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B27',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '大姐姐，你们是来住宿的客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家是酒馆兼旅馆。\n',
            '不介意的话就住我家吧★',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B56')

    def _loc_B27(): pass

    label('loc_B27')

    ChrTalk(
        0x00FE,
        (
            '我家是酒馆兼旅馆。\n',
            '不介意的话就住我家吧★',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B56(): pass

    label('loc_B56')

    TalkEnd(0x0011)

    Return()

# id: 0x0006 offset: 0xB5A
@scena.Code('func_06_B5A')
def func_06_B5A():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_BB6',
    )

    ChrTalk(
        0x00FE,
        (
            '#0400960001V#770F啊，是姐姐你们！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400960002V最近大家都很精神哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400960003V请放心吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BB6(): pass

    label('loc_BB6')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0xBBA
@scena.Code('func_07_BBA')
def func_07_BBA():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_C0E',
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

    def _loc_C0E(): pass

    label('loc_C0E')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0xC12
@scena.Code('func_08_C12')
def func_08_C12():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_C39',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的饭会是什么呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C64')

    def _loc_C39(): pass

    label('loc_C39')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_C64',
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

    def _loc_C64(): pass

    label('loc_C64')

    TalkEnd(0x0012)

    Return()

# id: 0x0009 offset: 0xC68
@scena.Code('func_09_C68')
def func_09_C68():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_C89',
    )

    ChrTalk(
        0x00FE,
        (
            '大家正在玩呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CC6')

    def _loc_C89(): pass

    label('loc_C89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_CC6',
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

    def _loc_CC6(): pass

    label('loc_CC6')

    TalkEnd(0x0013)

    Return()

# id: 0x000A offset: 0xCCA
@scena.Code('func_0A_CCA')
def func_0A_CCA():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrPos(0x0101, -2020, 8000, 57380, 180)
    SetChrPos(0x0102, -3170, 8039, 57530, 180)
    CameraMove(-2500, 6000, -3290, 0)
    OP_6C(310000, 0)
    CameraSetDistance(5900, 0)

    @scena.Lambda('lambda_0D1C')
    def lambda_0D1C():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D1C)

    Sleep(2000)

    @scena.Lambda('lambda_0D31')
    def lambda_0D31():
        CameraMove(-2100, 7980, 57740, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D31)

    CameraSetDistance(3000, 8000)

    ChrTalk(
        0x0101,
        (
            '#501F#2P哈～～\n',
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
            '#000F#2P哇啊～真漂亮……\n',
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
            '#000F#2P嗯～真的好漂亮啊～',
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
            '#006F#2P因为正是长身体的时候嘛。',
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
            '#004F#2P啊，等一下。',
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

# id: 0x000B offset: 0x10BB
@scena.Code('func_0B_10BB')
def func_0B_10BB():
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

    @scena.Lambda('lambda_11BB')
    def lambda_11BB():
        CameraMove(27520, 60, 16390, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_11BB)

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

    @scena.Lambda('lambda_12B0')
    def lambda_12B0():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12B0)

    @scena.Lambda('lambda_12BE')
    def lambda_12BE():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_12BE)

    @scena.Lambda('lambda_12CC')
    def lambda_12CC():
        ChrMoveTo(0x00FE, 27380, 60, 17180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12CC)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(18, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_12F6')
    def lambda_12F6():
        ChrJumpTo(0x00FE, 27240, 20, 17780, 500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12F6)

    @scena.Lambda('lambda_1314')
    def lambda_1314():
        ChrJumpTo(0x00FE, 27440, 70, 15630, 500, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1314)

    CreateThread(0x0101, 0x02, 0x00, 0x000C)

    ChrTalk(
        0x0008,
        (
            '#0060040459V#044F#4P#12A呀……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#004F#1P#12A啊……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0101, 0x0001)
    SetChrFlags(0x0102, 0x0004)

    @scena.Lambda('lambda_137A')
    def lambda_137A():
        ChrWalkTo(0x00FE, 27730, 500, 19280, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_137A)

    WaitForThreadExit(0x0102, 0x0001)
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
    OP_6F(0x0004, 30)
    OP_70(0x0004, 0)
    ChrWalkTo(0x0102, 28280, -40, 16990, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0008, 400)

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

    @scena.Lambda('lambda_160B')
    def lambda_160B():
        ChrTurnDirection(0x00FE, 0x0008, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_160B)

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

    @scena.Lambda('lambda_181E')
    def lambda_181E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_181E')

    DispatchAsync2(0x0101, 0x0001, lambda_181E)

    @scena.Lambda('lambda_182F')
    def lambda_182F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_182F')

    DispatchAsync2(0x0102, 0x0001, lambda_182F)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    @scena.Lambda('lambda_1864')
    def lambda_1864():
        ChrWalkTo(0x00FE, 41150, -20, 18660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1864)

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
            '#014F#2P哦，啊啊……怎么了？',
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
            '#0010040489V#004F啊，难道说……',
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
            '#018F#2P……你又在乱想什么啦？\n',
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
            '#017F#2P你·别·误·会·了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040495V我只是觉得她和\n',
            '我以前认识的一个人有点相似而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F#2P所以，刚才只是有点惊讶罢了。',
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
            '#015F#2P我说，艾丝蒂尔。\n',
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
            '#010F#2P是杰尼丝王立学院。',
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
            '#015F#2P你还敢说那件事。',
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
            '#019F#2P而且，当时又是谁\n',
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
            '#019F#2P与其花时间嘲笑别人，\n',
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
            '#010F#2P你明白了就好。',
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

# id: 0x000C offset: 0x1EE9
@scena.Code('func_0C_1EE9')
def func_0C_1EE9():
    Sleep(200)

    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0008, 11)

    Return()

# id: 0x000D offset: 0x1EF9
@scena.Code('func_0D_1EF9')
def func_0D_1EF9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 2, 0x40A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D2E',
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

    @scena.Lambda('lambda_1F9B')
    def lambda_1F9B():
        CameraMove(2428, 6000, -13190, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F9B)

    @scena.Lambda('lambda_1FB3')
    def lambda_1FB3():
        CameraSetDistance(8450, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FB3)

    @scena.Lambda('lambda_1FC3')
    def lambda_1FC3():
        OP_6C(60000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1FC3)

    @scena.Lambda('lambda_1FD3')
    def lambda_1FD3():
        OP_67(0, 5095, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1FD3)

    OP_12(0x00009470, 0x0003D090, 0x00001B58)
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
    OP_12(0x00009470, 0x00014C08, 0x00000000)
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
            '#010F而我的是……海鲜焗饭。\n',
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
            '#015F我也不客气了。',
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
            '#010F好啊……\n',
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
            '#014F我喂你……？',
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
            '#018F这样……\n',
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
            '#017F……我说的不好意思\n',
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
            '#010F知道啦知道啦。',
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
            '#014F啊。',
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
            '#010F嗯，就连附送的\n',
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
            '#010F吃饱了就睡\n',
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
    OP_12(0x00009470, 0x00020F58, 0x00000000)
    OP_6C(0, 0)

    @scena.Lambda('lambda_29BC')
    def lambda_29BC():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_29BC')

    DispatchAsync2(0x0102, 0x0001, lambda_29BC)

    @scena.Lambda('lambda_29CD')
    def lambda_29CD():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_29CD')

    DispatchAsync2(0x0101, 0x0001, lambda_29CD)

    @scena.Lambda('lambda_29DE')
    def lambda_29DE():
        OP_69(0x0009, 0)
        Yield()

        Jump('lambda_29DE')

    DispatchAsync2(0x0009, 0x0003, lambda_29DE)

    @scena.Lambda('lambda_29EF')
    def lambda_29EF():
        OP_69(0x0009, 0)
        Yield()

        Jump('lambda_29EF')

    DispatchAsync2(0x0009, 0x0001, lambda_29EF)

    @scena.Lambda('lambda_2A00')
    def lambda_2A00():
        CameraSetDistance(4000, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2A00)

    @scena.Lambda('lambda_2A10')
    def lambda_2A10():
        OP_6C(300000, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2A10)

    SetChrPos(0x0009, -15000, 15680, -15710, 0)
    ClearChrFlags(0x0009, 0x0080)
    ChrWalkTo(0x0009, 19800, 11500, -12310, 13000, 0x00)
    ChrWalkTo(0x0009, 39700, 11500, -110, 13000, 0x00)
    ChrWalkTo(0x0009, 55300, 14700, 6090, 13000, 0x00)
    Fade(1000)
    SetChrFlags(0x0009, 0x0080)
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
            '#010F#4P是啊。\n',
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
    SetScenaFlags(ScenaFlag(0x0081, 3, 0x40B))
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)

    def _loc_2D2E(): pass

    label('loc_2D2E')

    Return()

# id: 0x000E offset: 0x2D2F
@scena.Code('func_0E_2D2F')
def func_0E_2D2F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 4, 0x40C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_37E4',
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

    @scena.Lambda('lambda_2DD4')
    def lambda_2DD4():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2DD4')

    DispatchAsync2(0x0101, 0x0003, lambda_2DD4)

    @scena.Lambda('lambda_2DE5')
    def lambda_2DE5():
        ChrWalkTo(0x00FE, 4300, 3970, 11420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DE5)

    Sleep(500)

    @scena.Lambda('lambda_2E05')
    def lambda_2E05():
        ChrWalkTo(0x00FE, 5220, 4010, 9680, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2E05)

    Sleep(1200)

    @scena.Lambda('lambda_2E25')
    def lambda_2E25():
        ChrWalkTo(0x00FE, 4260, 3980, 11980, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2E25)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(18, 0x00, 0x64)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    ChrTurnDirection(0x000A, 0x0101, 0)

    @scena.Lambda('lambda_2E60')
    def lambda_2E60():
        ChrJumpTo(0x00FE, 4390, 3980, 10420, 500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E60)

    @scena.Lambda('lambda_2E7E')
    def lambda_2E7E():
        ChrJumpTo(0x00FE, 4360, 3960, 13150, 500, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2E7E)

    CreateThread(0x0101, 0x02, 0x00, 0x000F)

    ChrTalk(
        0x000A,
        (
            '#0400040580V#774F#4P#12A哇哇！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#004F#1P#12A啊……',
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
            '#771F不好意思啦。\n',
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
            '#772F……怎、怎么了？',
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
            '#770F啊……对对。\n',
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
            '#774F不、不用了。\n',
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
            '#771F我先走了，拜拜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 90, 400)

    @scena.Lambda('lambda_31CA')
    def lambda_31CA():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_31CA')

    DispatchAsync2(0x0102, 0x0003, lambda_31CA)

    @scena.Lambda('lambda_31DB')
    def lambda_31DB():
        CameraMove(7160, 4030, 12560, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_31DB)

    ChrWalkTo(0x000A, 16840, 1720, 14680, 6000, 0x00)
    SetChrFlags(0x000A, 0x0080)
    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#501F好活泼的男孩子哦～',
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

    @scena.Lambda('lambda_32A4')
    def lambda_32A4():
        CameraMove(4380, 4019, 9800, 1200)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_32A4)

    TerminateThread(0x0101, 0x03)
    SetChrDirection(0x0101, 90, 400)
    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#004F#2P约修亚，怎么了？',
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
            '#014F#1P啊……\n',
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
            '#004F#2P丢掉？什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F#1P看看身上有没有什么东西不见了。',
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
            '#004F#2P什么呀，又不是遇到了小偷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040607V#006F钱包……在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040608V头饰……也在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040609V#501F游击士的纹章……',
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
            '#015F#1P果然是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F#2P啊啊啊啊～～～～？\n',
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
            '#012F#1P冷静点，艾丝蒂尔。',
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
            '#002F#2P可、可是……\n',
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
            '#004F#2P难、难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F#1P嗯，很可能是刚才那个男孩子做的。',
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
            '#005F#2P你、你说什么～！？',
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
            '#015F#1P的确……\n',
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
            '#009F#2P呜呜呜呜～……\n',
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
            '#010F#1P呵呵，对小孩子可要手下留情哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040628V总之，\n',
            '我们先在这附近找找那孩子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_37E4(): pass

    label('loc_37E4')

    Return()

# id: 0x000F offset: 0x37E5
@scena.Code('func_0F_37E5')
def func_0F_37E5():
    Sleep(200)

    SetChrChipByIndex(0x0101, 14)

    Return()

# id: 0x0010 offset: 0x37F0
@scena.Code('func_10_37F0')
def func_10_37F0():
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

    @scena.Lambda('lambda_3D13')
    def lambda_3D13():
        CameraMove(28370, 100, 17960, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3D13)

    @scena.Lambda('lambda_3D2B')
    def lambda_3D2B():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_3D2B')

    DispatchAsync2(0x0136, 0x0001, lambda_3D2B)

    @scena.Lambda('lambda_3D3C')
    def lambda_3D3C():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_3D3C')

    DispatchAsync2(0x0101, 0x0001, lambda_3D3C)

    @scena.Lambda('lambda_3D4D')
    def lambda_3D4D():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_3D4D')

    DispatchAsync2(0x0102, 0x0001, lambda_3D4D)

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
            '那个、那个！',
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
            '啊，好的……',
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
        (0x00000000, 'loc_3FFA'),
        (0x00000001, 'loc_408F'),
        (0x00000002, 'loc_4127'),
        (-1, 'loc_4197'),
    )

    def _loc_3FFA(): pass

    label('loc_3FFA')

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

    Jump('loc_4197')

    def _loc_408F(): pass

    label('loc_408F')

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

    Jump('loc_4197')

    def _loc_4127(): pass

    label('loc_4127')

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

    Jump('loc_4197')

    def _loc_4197(): pass

    label('loc_4197')

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
            '科洛丝姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_42C9')
    def lambda_42C9():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_42C9')

    DispatchAsync2(0x0136, 0x0001, lambda_42C9)

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
            '是啊……\n',
            '哥哥姐姐，拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_435F')
    def lambda_435F():
        CameraMove(26760, 100, 17100, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_435F)

    ChrWalkTo(0x000D, 27490, 500, 19110, 3000, 0x00)
    SetChrDirection(0x000D, 0, 400)
    OP_70(0x0004, 30)
    OP_73(0x0004)
    SetChrFlags(0x000D, 0x0004)
    ChrWalkTo(0x000D, 27900, 500, 21200, 3000, 0x00)
    SetChrFlags(0x000D, 0x0080)
    OP_6F(0x0004, 30)
    OP_70(0x0004, 0)
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

# id: 0x0011 offset: 0x442E
@scena.Code('func_11_442E')
def func_11_442E():
    EventBegin(0x00)
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

    @scena.Lambda('lambda_44AD')
    def lambda_44AD():
        ChrWalkTo(0x00FE, 27640, 0, 16800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44AD)

    Sleep(500)

    @scena.Lambda('lambda_44CD')
    def lambda_44CD():
        ChrWalkTo(0x00FE, 26900, 0, 17590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_44CD)

    Sleep(500)

    @scena.Lambda('lambda_44ED')
    def lambda_44ED():
        ChrWalkTo(0x00FE, 28760, 0, 17460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_44ED)

    Sleep(500)

    @scena.Lambda('lambda_450D')
    def lambda_450D():
        ChrWalkTo(0x00FE, 27890, 0, 18190, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_450D)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010061096V#580F哇，都已经这么晚了。',
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
            '#0050061097V#552F嘁……不好办了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061098V这么暗，\n',
            '能查出些什么来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, 16500, 6000, 10000, 0)
    PlaySE(407, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0106, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_4614')
    def lambda_4614():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4614)

    @scena.Lambda('lambda_4622')
    def lambda_4622():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4622)

    @scena.Lambda('lambda_4630')
    def lambda_4630():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4630)

    @scena.Lambda('lambda_463E')
    def lambda_463E():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_463E)

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

    @scena.Lambda('lambda_4687')
    def lambda_4687():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_4687)

    @scena.Lambda('lambda_4697')
    def lambda_4697():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4697')

    DispatchAsync2(0x0101, 0x0001, lambda_4697)

    @scena.Lambda('lambda_46A8')
    def lambda_46A8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_46A8')

    DispatchAsync2(0x0102, 0x0001, lambda_46A8)

    @scena.Lambda('lambda_46B9')
    def lambda_46B9():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_46B9')

    DispatchAsync2(0x0106, 0x0001, lambda_46B9)

    PlaySE(140, 0x00, 0x64)
    OP_92(0x0009, 0x0105, 5000, 8000, 0x00)
    OP_92(0x0009, 0x0105, 4000, 6000, 0x00)
    OP_92(0x0009, 0x0105, 3000, 4000, 0x00)
    OP_92(0x0009, 0x0105, 2000, 2000, 0x00)
    TerminateThread(0x0106, 0x01)
    SetChrDirection(0x0106, 180, 0)
    ChrWalkTo(0x0009, 29330, 900, 16860, 1500, 0x00)
    TerminateThread(0x0101, 0x01)
    SetChrDirection(0x0101, 45, 0)

    @scena.Lambda('lambda_4731')
    def lambda_4731():
        SetChrDirection(0x00FE, 270, 200)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_4731)

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
            '#0050061109V#551F还真是优哉游哉啊。',
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
            '#0020061115V#010F#6P嗯，立大功了呢。',
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
            '#0020061119V#015F#6P因为我们已经\n',
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
            '#0060061122V#042F好！',
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
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_4B4E')
    def lambda_4B4E():
        ChrWalkTo(0x00FE, 9500, 6000, 13700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4B4E)

    Sleep(100)

    @scena.Lambda('lambda_4B6E')
    def lambda_4B6E():
        ChrWalkTo(0x00FE, 9500, 6000, 13700, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4B6E)

    Sleep(100)

    @scena.Lambda('lambda_4B8E')
    def lambda_4B8E():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4B8E')

    DispatchAsync2(0x0101, 0x0001, lambda_4B8E)

    @scena.Lambda('lambda_4B9F')
    def lambda_4B9F():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4B9F')

    DispatchAsync2(0x0102, 0x0001, lambda_4B9F)

    SetChrChipByIndex(0x0105, 65535)
    ClearChrFlags(0x0105, 0x0020)
    SetChrSubChip(0x0105, 0)

    @scena.Lambda('lambda_4BBF')
    def lambda_4BBF():
        ChrWalkTo(0x00FE, 9500, 6000, 13700, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4BBF)

    Sleep(100)

    @scena.Lambda('lambda_4BDF')
    def lambda_4BDF():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4BDF')

    DispatchAsync2(0x0106, 0x0001, lambda_4BDF)

    @scena.Lambda('lambda_4BF0')
    def lambda_4BF0():
        ChrWalkTo(0x00FE, 9500, 6000, 13700, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4BF0)

    Sleep(100)

    @scena.Lambda('lambda_4C10')
    def lambda_4C10():
        ChrWalkTo(0x00FE, 9500, 6000, 13700, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4C10)

    Sleep(500)

    TerminateThread(0x0101, 0xFF)

    @scena.Lambda('lambda_4C34')
    def lambda_4C34():
        ChrWalkTo(0x00FE, 11620, 4030, 14980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C34)

    Sleep(500)

    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_4C58')
    def lambda_4C58():
        ChrWalkTo(0x00FE, 11620, 4030, 14980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4C58)

    Sleep(100)

    @scena.Lambda('lambda_4C78')
    def lambda_4C78():
        ChrWalkTo(0x00FE, 11620, 4030, 14980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4C78)

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

    @scena.Lambda('lambda_4D0A')
    def lambda_4D0A():
        ChrWalkTo(0x00FE, 11620, 4030, 14980, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_4D0A)

    OP_0D()
    OP_28(0x003E, 0x01, 0x0002)
    OP_28(0x003E, 0x01, 0x0004)
    OP_28(0x003E, 0x01, 0x0008)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    SetMapFlags(0x02000000)
    ClearMapFlags(0x10000000)
    NewScene('ED6_DT01/R2111._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x4D49
@scena.Code('func_12_4D49')
def func_12_4D49():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 1, 0x409)),
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E46',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E01',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
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

    Jump('loc_4E3F')

    def _loc_4E01(): pass

    label('loc_4E01')

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

    def _loc_4E3F(): pass

    label('loc_4E3F')

    Call(0, 0x0013)

    Jump('loc_51AC')

    def _loc_4E46(): pass

    label('loc_4E46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4EBA',
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
    Call(0, 0x0013)

    Jump('loc_51AC')

    def _loc_4EBA(): pass

    label('loc_4EBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4F90',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F29',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
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

    Jump('loc_4F89')

    def _loc_4F29(): pass

    label('loc_4F29')

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

    def _loc_4F89(): pass

    label('loc_4F89')

    Call(0, 0x0013)

    Jump('loc_51AC')

    def _loc_4F90(): pass

    label('loc_4F90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_50F2',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_502D',
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

    Jump('loc_50EB')

    def _loc_502D(): pass

    label('loc_502D')

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

    @scena.Lambda('lambda_5088')
    def lambda_5088():
        ChrTurnDirection(0x0105, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5088)

    @scena.Lambda('lambda_5096')
    def lambda_5096():
        ChrTurnDirection(0x0101, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5096)

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

    def _loc_50EB(): pass

    label('loc_50EB')

    Call(0, 0x0013)

    Jump('loc_51AC')

    def _loc_50F2(): pass

    label('loc_50F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_51AC',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5164',
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

    Jump('loc_51A8')

    def _loc_5164(): pass

    label('loc_5164')

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

    def _loc_51A8(): pass

    label('loc_51A8')

    Call(0, 0x0013)

    def _loc_51AC(): pass

    label('loc_51AC')

    Return()

# id: 0x0013 offset: 0x51AD
@scena.Code('func_13_51AD')
def func_13_51AD():
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0014 offset: 0x51C9
@scena.Code('func_14_51C9')
def func_14_51C9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 3, 0x413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_523D',
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
    Call(0, 0x0013)

    Jump('loc_54E0')

    def _loc_523D(): pass

    label('loc_523D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 3, 0x40B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5313',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52AC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
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

    Jump('loc_530C')

    def _loc_52AC(): pass

    label('loc_52AC')

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

    def _loc_530C(): pass

    label('loc_530C')

    Call(0, 0x0015)

    Jump('loc_54E0')

    def _loc_5313(): pass

    label('loc_5313')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5457',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_538D',
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

    Jump('loc_5450')

    def _loc_538D(): pass

    label('loc_538D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53F6',
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

    Jump('loc_5450')

    def _loc_53F6(): pass

    label('loc_53F6')

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

    def _loc_5450(): pass

    label('loc_5450')

    Call(0, 0x0015)

    Jump('loc_54E0')

    def _loc_5457(): pass

    label('loc_5457')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54E0',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_547B',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_5482')

    def _loc_547B(): pass

    label('loc_547B')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_5482(): pass

    label('loc_5482')

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
    Call(0, 0x0015)

    def _loc_54E0(): pass

    label('loc_54E0')

    Return()

# id: 0x0015 offset: 0x54E1
@scena.Code('func_15_54E1')
def func_15_54E1():
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0016 offset: 0x54FD
@scena.Code('func_16_54FD')
def func_16_54FD():
    OP_13(0x0058)

    Return()

# id: 0x0017 offset: 0x5501
@scena.Code('func_17_5501')
def func_17_5501():
    OP_13(0x0057)

    Return()

# id: 0x0018 offset: 0x5505
@scena.Code('func_18_5505')
def func_18_5505():
    OP_13(0x0059)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
