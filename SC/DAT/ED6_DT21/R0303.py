import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R0303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0303   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雷震狂鱼'),
    TXT(0x02, '士兵海恩茨'),
    TXT(0x03, '矿工兰古'),
    TXT(0x04, '阿加特'),
    TXT(0x05, '目标用照相机'),
    TXT(0x06, '玛鲁加山道方向'),
    TXT(0x07, '玛鲁加山道方向'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0303.x'
    header.mapIndex       = 21
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x25AD
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT09/CH10900._CH', 'ED6_DT09/CH10900P._CP'),
        ('ED6_DT09/CH10901._CH', 'ED6_DT09/CH10901P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -420,
            z                   = -20,
            y                   = -34790,
            direction           = 180,
            word_0E             = 3,
            dword_10            = 196608,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
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
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -166100,
            z                   = 100,
            y                   = 127500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -166100,
            z                   = 100,
            y                   = 127500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -167010,
            z                   = -70,
            y                   = 78790,
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
            x                   = -2070,
            z                   = -120,
            y                   = -72730,
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

# id: 0x10003 offset: 0x1B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -4700,
            y           = -2000,
            z           = -62600,
            range       = 1200,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFF1668,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = -15720,
            y           = -2000,
            z           = -24750,
            range       = 13360,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFFB08C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -2500,
            y           = -6100,
            z           = -8670,
            range       = 2500,
            dword_10    = 0x00002710,
            dword_14    = 0xFFFFF254,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
        ScenaEventData(
            x           = -168250,
            y           = -1000,
            z           = 128800,
            range       = -164500,
            dword_10    = 0x000007D0,
            dword_14    = 0x0001F2E8,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = -420,
            y           = -1000,
            z           = -34790,
            range       = 2000,
            dword_10    = 0x00000FA0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x252
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -13840,
            triggerZ            = -130,
            triggerY            = -13720,
            triggerRange        = 1000,
            actorX              = -13620,
            actorZ              = -140,
            actorY              = -12960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x276
@scena.Code('PreInit')
def PreInit():
    OP_A3(0x1970)
    OP_A3(0x1971)
    OP_A3(0x1972)
    OP_A3(0x1973)
    OP_A3(0x1974)
    OP_A3(0x1975)
    OP_A3(0x1976)
    OP_A3(0x1977)
    OP_A3(0x1978)
    OP_A3(0x1979)
    OP_A3(0x197A)
    OP_A3(0x197B)
    OP_A3(0x197C)
    OP_A3(0x1FC0)
    OP_A3(0x1FC1)
    OP_A3(0x1FC2)
    OP_A3(0x1FC3)
    OP_A3(0x1FC4)
    OP_A3(0x1FC5)
    OP_A3(0x1FC6)
    OP_A3(0x1FC7)
    OP_A3(0x1FC8)
    OP_A3(0x1FC9)
    OP_A3(0x1FCA)
    OP_A3(0x1FCB)
    OP_A3(0x1FCC)
    OP_A3(0x1FCD)
    OP_A3(0x1FCE)
    OP_A3(0x1FCF)
    OP_A3(0x1FD0)
    OP_A3(0x1FD1)
    OP_A3(0x1FD2)
    OP_A3(0x1FD3)
    OP_A3(0x1FD4)
    OP_A3(0x1FD5)
    OP_A3(0x1FD6)
    OP_A3(0x1FD7)
    OP_A3(0x1FD8)
    OP_A3(0x1FD9)
    OP_A3(0x1FDA)
    OP_A3(0x1FDB)
    OP_A3(0x1FDC)
    OP_A3(0x1FDD)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 3, 0x1E03)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 4, 0x1E04)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_319',
    )

    SetChrPos(0x0009, -2440, 30, -23500, 180)
    ClearChrFlags(0x0009, 0x0080)

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_349',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_330',
    )

    SetChrFlags(0x000A, 0x0080)

    Jump('loc_346')

    def _loc_330(): pass

    label('loc_330')

    SetChrPos(0x000A, -168160, -10, 126410, 90)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_346(): pass

    label('loc_346')

    Jump('loc_389')

    def _loc_349(): pass

    label('loc_349')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_353',
    )

    Jump('loc_389')

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_362',
    )

    SetChrFlags(0x000A, 0x0080)

    Jump('loc_389')

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Return,
        ),
        'loc_382',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000A, -163860, 40, 125420, 315)

    Jump('loc_389')

    def _loc_382(): pass

    label('loc_382')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_389',
    )

    def _loc_389(): pass

    label('loc_389')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_39F',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0009)

    Jump('loc_3C5')

    def _loc_39F(): pass

    label('loc_39F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_3B5',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 0x000B)

    Jump('loc_3C5')

    def _loc_3B5(): pass

    label('loc_3B5')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C5',
    )

    Event(0, 0x0015)

    def _loc_3C5(): pass

    label('loc_3C5')

    Return()

# id: 0x0001 offset: 0x3C6
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3E6'),
        (0x00000065, 'loc_3E6'),
        (0x00000069, 'loc_3E6'),
        (0x00000066, 'loc_412'),
        (0x00000067, 'loc_412'),
        (0x00000068, 'loc_412'),
        (-1, 'loc_43E'),
    )

    def _loc_3E6(): pass

    label('loc_3E6')

    OP_16(0x02, 0x00000FA0, 0xFFFE0C00, 0xFFFD7790, 0x00230011)
    ClearChrFlags(0x000D, 0x0004)

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x2F8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0xB4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_43E')

    def _loc_412(): pass

    label('loc_412')

    OP_16(0x02, 0x00000FA0, 0xFFFB8390, 0xFFFFBD98, 0x0023006A)
    ClearChrFlags(0x000E, 0x0004)

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x31A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x81),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_43E')

    def _loc_43E(): pass

    label('loc_43E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_458',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_458(): pass

    label('loc_458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Return,
        ),
        'loc_468',
    )

    OP_10(0x03, 0x00)
    OP_10(0x04, 0x01)

    Jump('loc_46E')

    def _loc_468(): pass

    label('loc_468')

    OP_10(0x03, 0x01)
    OP_10(0x04, 0x00)

    def _loc_46E(): pass

    label('loc_46E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_48C',
    )

    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x04, 0x0080)

    Jump('loc_49E')

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x031F, 6, 0x18FE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49E',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x04, 0x0080)

    def _loc_49E(): pass

    label('loc_49E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0326, 3, 0x1933)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B0',
    )

    OP_6F(0x0000, 0)

    Jump('loc_4B7')

    def _loc_4B0(): pass

    label('loc_4B0')

    OP_6F(0x0000, 60)

    def _loc_4B7(): pass

    label('loc_4B7')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_512',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_4E8',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)
    OP_C4(0x00, 0x00000004)

    Jump('loc_512')

    def _loc_4E8(): pass

    label('loc_4E8')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_512',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x00013880, 0x00000000)

    def _loc_512(): pass

    label('loc_512')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_521',
    )

    Jump('loc_571')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_571',
    )

    LoadEffect(0x00, 'map\\\\mp086_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 0, 6000, -8130, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_571(): pass

    label('loc_571')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_57D',
    )

    OP_B2(0x00, 0x03, 0x0080)

    def _loc_57D(): pass

    label('loc_57D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_596',
    )

    OP_10(0x01, 0x00)
    OP_10(0x05, 0x01)

    Jump('loc_59C')

    def _loc_596(): pass

    label('loc_596')

    OP_10(0x01, 0x01)
    OP_10(0x05, 0x00)

    def _loc_59C(): pass

    label('loc_59C')

    Return()

# id: 0x0002 offset: 0x59D
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5B2',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_5B2(): pass

    label('loc_5B2')

    Return()

# id: 0x0003 offset: 0x5B3
@scena.Code('func_03_5B3')
def func_03_5B3():
    TalkBegin(0x000A)
    Call(0, 0x0004)
    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0x5BE
@scena.Code('func_04_5BE')
def func_04_5BE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_68C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_648',
    )

    ChrTalk(
        0x000A,
        (
            '哦！是小姐你们。\n',
            '事故的时候真是多谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '其他矿工们\n',
            '也已经在里面开始工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不介意的话\n',
            '去见见他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_689')

    def _loc_648(): pass

    label('loc_648')

    ChrTalk(
        0x000A,
        (
            '事故的时候真是多谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不介意的话\n',
            '也去见见其他矿工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_689(): pass

    label('loc_689')

    Jump('loc_A13')

    def _loc_68C(): pass

    label('loc_68C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_887',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_753',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6DA',
    )

    ChrTalk(
        0x000A,
        (
            '抱歉，里面不能进去。\n',
            '因为今天开始重新开工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_750')

    def _loc_6DA(): pass

    label('loc_6DA')

    ChrTalk(
        0x000A,
        (
            '哟，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '加通老大\n',
            '终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们也终于\n',
            '重新开工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因此，这里又要禁止\n',
            '无关人士入内了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_750(): pass

    label('loc_750')

    Jump('loc_884')

    def _loc_753(): pass

    label('loc_753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7A9',
    )

    ChrTalk(
        0x000A,
        (
            '今天开始我们也\n',
            '打算重新开工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不好意思，这里禁止\n',
            '无关人士入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_884')

    def _loc_7A9(): pass

    label('loc_7A9')

    ChrTalk(
        0x000A,
        (
            '哟，游击士们啊\n',
            '先前承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们今天也打算来\n',
            '重新开工的……\n',
            '不巧老大还没来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '矿工们只好做些准备工作，\n',
            '现在正在待命中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好像是老大家里\n',
            '出了麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然不太清楚状况\n',
            '但希望他早点来矿山啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_884(): pass

    label('loc_884')

    Jump('loc_A13')

    def _loc_887(): pass

    label('loc_887')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Return,
        ),
        'loc_966',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8F2',
    )

    ChrTalk(
        0x000A,
        (
            '现在你们的游击士同伴\n',
            '正在里面进行避难引导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是帮大忙了。\n',
            '这下就可以回城里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_963')

    def _loc_8F2(): pass

    label('loc_8F2')

    ChrTalk(
        0x000A,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '现在你们的游击士同伴\n',
            '正在里面进行避难引导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是帮大忙了。\n',
            '这下就可以回城里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_963(): pass

    label('loc_963')

    Jump('loc_A13')

    def _loc_966(): pass

    label('loc_966')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_A13',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9AC',
    )

    ChrTalk(
        0x000A,
        (
            '如你们所知，这里是禁止进入的。\n',
            '无关人士请回吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A13')

    def _loc_9AC(): pass

    label('loc_9AC')

    ChrTalk(
        0x000A,
        (
            '哟，你们是\n',
            '那次的游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如你们所知，矿山是\n',
            '禁止无关人士入内的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不好意思请回吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_A13(): pass

    label('loc_A13')

    Return()

# id: 0x0005 offset: 0xA14
@scena.Code('func_05_A14')
def func_05_A14():
    TalkBegin(0x000B)
    Call(0, 0x0006)
    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0xA1F
@scena.Code('func_06_A1F')
def func_06_A1F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Return,
        ),
        'loc_B94',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A89',
    )

    ChrTalk(
        0x000B,
        (
            '#0050290565V#050F现在奥利维尔和金\n',
            '去叫矿工了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290566V你们就\n',
            '赶紧前往农场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B94')

    def _loc_A89(): pass

    label('loc_A89')

    ChrTalk(
        0x000B,
        (
            '#0050290559V#052F喂喂，你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290560V怎么到这边来了。\n',
            '不是要去农场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290561V#1008F啊，不……\n',
            '我们现在正要去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0050290562V#057F……你们以为\n',
            '为什么要兵分两路啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290563V赶快去农场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290564V#1007F明，明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_B94(): pass

    label('loc_B94')

    Return()

# id: 0x0007 offset: 0xB95
@scena.Code('func_07_B95')
def func_07_B95():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x031F, 6, 0x18FE)),
            Expr.Return,
        ),
        'loc_B9D',
    )

    Return()

    def _loc_B9D(): pass

    label('loc_B9D')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_C82'),
        (-1, 'loc_CA5'),
    )

    def _loc_C82(): pass

    label('loc_C82')

    Fade(500)
    OP_89(0x0000, -580, -40, -40880, 357)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_CA5(): pass

    label('loc_CA5')

    Battle(0x00000EEC, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -580, -40, -40880, 357)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_CDE'),
        (0x00000001, 'loc_CE1'),
        (-1, 'loc_CE4'),
    )

    def _loc_CDE(): pass

    label('loc_CDE')

    EventEnd(0x00)

    Return()

    def _loc_CE1(): pass

    label('loc_CE1')

    OP_B4(0x00)

    Return()

    def _loc_CE4(): pass

    label('loc_CE4')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x04, 0x0080)
    OP_0D()
    Sleep(400)

    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A2(0x18FE)
    OP_28(0x00B0, 0x04, 0x10)
    OP_28(0x00B0, 0x04, 0x02)
    OP_28(0x00B0, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0xD50
@scena.Code('func_08_D50')
def func_08_D50():
    UnlockAchievement(0x02, 0xCA, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0326, 3, 0x1933)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E2D',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_DC4',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1933)

    Jump('loc_E2A')

    def _loc_DC4(): pass

    label('loc_DC4')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_E2A(): pass

    label('loc_E2A')

    Jump('loc_E5E')

    def _loc_E2D(): pass

    label('loc_E2D')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xE6C
@scena.Code('func_09_E6C')
def func_09_E6C():
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
        'loc_E83',
    )

    Call(0, 0x000E)
    Call(0, 0x000F)

    def _loc_E83(): pass

    label('loc_E83')

    OP_6D(-1710, -30, -25410, 0)
    OP_67(0, 10030, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(315000, 0)
    OP_6E(393, 0)
    SetChrPos(0x0101, 1330, -30, -53480, 0)
    SetChrPos(0x0102, 140, -20, -53920, 0)
    SetChrPos(0x00F8, 1340, -40, -55460, 0)
    SetChrPos(0x00F9, -110, -30, -55920, 0)

    @scena.Lambda('lambda_0F0A')
    def lambda_0F0A():
        OP_8E(0x00FE, 1330, -30, -43780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F0A)

    @scena.Lambda('lambda_0F25')
    def lambda_0F25():
        OP_8E(0x00FE, 140, -20, -43720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0F25)

    @scena.Lambda('lambda_0F40')
    def lambda_0F40():
        OP_8E(0x00FE, 1340, -40, -45060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0F40)

    @scena.Lambda('lambda_0F5B')
    def lambda_0F5B():
        OP_8E(0x00FE, -110, -30, -45020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0F5B)

    @scena.Lambda('lambda_0F76')
    def lambda_0F76():
        OP_6D(120, -40, -43020, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0F76)

    OP_C8(0x0200, 0x0046, 'C_PLAC19._CH', 0x01, 0x03E8)
    ShowPlaceName('翡翠之塔')
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    OP_6D(250, -20, -43960, 0)
    OP_67(0, 9530, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010340680V#1002F#6P好了……\n',
            '终于要开始调查了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340681V总之必须赶快\n',
            '到塔顶上去才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340682V#1043F#6P嗯……\n',
            '不过情况很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340683V#1004F#6P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, 850, -30, -32460, 180)
    ClearChrFlags(0x0009, 0x0080)
    OP_4A(0x0009, 255)

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '#3840340684V#3P你，你们是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_114A',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_117E')

    def _loc_114A(): pass

    label('loc_114A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_116C',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_117E')

    def _loc_116C(): pass

    label('loc_116C')

    OP_62(0x00F8, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_117E(): pass

    label('loc_117E')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11A5',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_11D9')

    def _loc_11A5(): pass

    label('loc_11A5')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11C7',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_11D9')

    def _loc_11C7(): pass

    label('loc_11C7')

    OP_62(0x00F9, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_11D9(): pass

    label('loc_11D9')

    Sleep(1000)

    @scena.Lambda('lambda_11E4')
    def lambda_11E4():
        OP_6D(120, -40, -42500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11E4)

    @scena.Lambda('lambda_11FC')
    def lambda_11FC():
        OP_67(0, 9040, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11FC)

    OP_8E(0x0009, 500, -60, -41710, 4000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0009,
        (
            '#3840340685V#2P难，难道是\n',
            '联络中提到的游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340686V#1006F#6P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340687V#1042F#6P你是侦察部队的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3840340688V#2P啊，啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3840340689V#2P为了向你们说明\n',
            '塔的状况才留下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1354',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340690V#555F#6P记得你们是被\n',
            '戴面具的家伙袭击了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1486')

    def _loc_1354(): pass

    label('loc_1354')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13A2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340691V#022F#6P记得你们是被\n',
            '戴面具的男子袭击了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1486')

    def _loc_13A2(): pass

    label('loc_13A2')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13EE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340692V#072F#6P听说有个有\n',
            '戴面具的男子出现了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1486')

    def _loc_13EE(): pass

    label('loc_13EE')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_143D',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340693V#1063F#6P听说你们是被\n',
            '戴面具的男子袭击了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1486')

    def _loc_143D(): pass

    label('loc_143D')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1486',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340694V#043F#6P听说有个有\n',
            '戴面具的男子出现了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1486(): pass

    label('loc_1486')

    ChrTalk(
        0x0009,
        (
            '#3840340695V#2P是，是没错\n',
            '但不仅仅是这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3840340696V#2P怎么说呢……\n',
            '实在是很奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340697V#1015F#6P奇怪……什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3840340698V#2P看，看了就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3840340699V#2P总之先到入口来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 0, 500)
    OP_90(0x0009, 0, 0, 15000, 4000, 0x00)
    SetChrPos(0x0009, -2440, 30, -23500, 180)
    OP_4B(0x0009, 255)
    OP_A2(0x1E03)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x000A offset: 0x159A
@scena.Code('func_0A_159A')
def func_0A_159A():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 3, 0x1E03)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_15AC',
    )

    Return()

    def _loc_15AC(): pass

    label('loc_15AC')

    EventBegin(0x01)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要回『埃尔赛尤』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
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
            TXT(0x00, '【回船上】\n'),
            TXT(0x01, '【不回去】\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1648',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_1668')

    def _loc_1648(): pass

    label('loc_1648')

    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_1668(): pass

    label('loc_1668')

    Return()

# id: 0x000B offset: 0x1669
@scena.Code('func_0B_1669')
def func_0B_1669():
    EventBegin(0x00)
    OP_6D(-1900, -90, -56520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1900, -90, -56520, 0)
    SetChrPos(0x0102, -1900, -90, -56520, 0)
    SetChrPos(0x00F8, -1900, -90, -56520, 0)
    SetChrPos(0x00F9, -1900, -90, -56520, 0)
    Yield()
    FadeIn(1000, 0)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x000C offset: 0x16FE
@scena.Code('func_0C_16FE')
def func_0C_16FE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 3, 0x1E03)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 4, 0x1E04)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_170B',
    )

    Return()

    def _loc_170B(): pass

    label('loc_170B')

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
        'loc_1730',
    )

    Call(0, 0x000E)
    Call(0, 0x000F)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_1730(): pass

    label('loc_1730')

    Fade(1000)
    OP_6D(-540, 100, -23090, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 800, 40, -22800, 0)
    SetChrPos(0x0102, -400, 90, -22800, 0)
    SetChrPos(0x00F8, 800, 70, -24200, 0)
    SetChrPos(0x00F9, -400, 10, -24200, 0)
    OP_8C(0x0009, 0, 0)
    OP_4A(0x0009, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010340700V#1004F#6P哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17F2')
    def lambda_17F2():
        OP_6D(-930, 2000, -16490, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_17F2)

    @scena.Lambda('lambda_180A')
    def lambda_180A():
        OP_67(0, 3110, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_180A)

    @scena.Lambda('lambda_1822')
    def lambda_1822():
        OP_6B(2730, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1822)

    @scena.Lambda('lambda_1832')
    def lambda_1832():
        OP_6C(349000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1832)

    @scena.Lambda('lambda_1842')
    def lambda_1842():
        OP_6E(567, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1842)

    WaitForThreadExit(0x0101, 0x0003)
    Fade(1000)
    OP_6D(0, 4890, -15580, 0)
    OP_67(0, 1310, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(0, 0)
    OP_6E(412, 0)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010340701V#1020F那，那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1922',
    )

    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName('提妲')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0070340702V#065F#5P能，能量障壁……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1A62')

    def _loc_1922(): pass

    label('loc_1922')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1974',
    )

    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName('科洛丝')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0060340703V#042F#5P是什么结界吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1A62')

    def _loc_1974(): pass

    label('loc_1974')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19C9',
    )

    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName('凯文神父')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0180340704V#1069F#5P难道是……结界吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1A62')

    def _loc_19C9(): pass

    label('loc_19C9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A11',
    )

    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName('金')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0080340705V#072F#5P唔……结界吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_1A62')

    def _loc_1A11(): pass

    label('loc_1A11')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A62',
    )

    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0030340706V#022F#5P是什么结界呢……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1A62(): pass

    label('loc_1A62')

    Sleep(100)

    Fade(1000)
    ChrTurnDirection(0x0009, 0x0102, 0)
    OP_6D(-1450, 90, -22590, 0)
    OP_67(0, 7770, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(283, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#3840340707V#5P我们到达的时候\n',
            '已经是这样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1AF0')
    def lambda_1AF0():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1AF0')

    DispatchAsync2(0x0101, 0x0001, lambda_1AF0)

    Sleep(50)

    @scena.Lambda('lambda_1B06')
    def lambda_1B06():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1B06')

    DispatchAsync2(0x0102, 0x0001, lambda_1B06)

    Sleep(50)

    @scena.Lambda('lambda_1B1C')
    def lambda_1B1C():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1B1C')

    DispatchAsync2(0x00F8, 0x0001, lambda_1B1C)

    Sleep(50)

    @scena.Lambda('lambda_1B32')
    def lambda_1B32():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1B32')

    DispatchAsync2(0x00F9, 0x0001, lambda_1B32)

    ChrTalk(
        0x0009,
        (
            '#3840340708V#5P然后，正要调查的时候\n',
            '那个戴面具的男子就出现了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340709V#1043F#6P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340710V#1042F没有办法\n',
            '进去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3840340711V#5P戴面具的男子\n',
            '就这样直接进去了，\n',
            '我想应该没问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3840340712V#5P我们当时也想追上去，\n',
            '但是同伴都被打倒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340713V#1007F#4P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340714V#1002F这里就交给我们\n',
            '你先返回部队吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3840340715V#5P明，明白了……\n',
            '愿女神保佑各位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 180, 500)

    @scena.Lambda('lambda_1CF5')
    def lambda_1CF5():
        OP_6D(-690, 20, -27800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1CF5)

    OP_8E(0x0009, -190, -10, -40120, 5000, 0x00)
    SetChrFlags(0x0009, 0x0080)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_1D2B')
    def lambda_1D2B():
        OP_6D(-1450, 90, -22590, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1D2B)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_A2(0x1E04)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x000D offset: 0x1D5D
@scena.Code('func_0D_1D5D')
def func_0D_1D5D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D6A',
    )

    Return()

    def _loc_1D6A(): pass

    label('loc_1D6A')

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DEF',
    )

    ChrTurnDirection(0x000B, 0x0000, 400)
    ChrTurnDirection(0x0000, 0x000B, 0)
    ChrTurnDirection(0x0001, 0x000B, 0)
    ChrTurnDirection(0x0002, 0x000B, 0)
    ChrTurnDirection(0x0003, 0x000B, 0)
    OP_4A(0x000B, 255)
    SetChrFlags(0x000B, 0x0040)
    Call(0, 0x0006)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.PushLong, 0x1EC30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_92(0x0000, 0x000C, 0x00000000, 0x00000BB8, 0x00)
    OP_8C(0x000B, 0, 0)
    Sleep(50)

    EventEnd(0x04)
    OP_4B(0x000B, 255)
    ClearChrFlags(0x000B, 0x0040)

    Jump('loc_1E47')

    def _loc_1DEF(): pass

    label('loc_1DEF')

    ChrTurnDirection(0x000A, 0x0000, 400)
    OP_4A(0x000A, 255)
    SetChrFlags(0x000A, 0x0040)
    Call(0, 0x0004)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.PushLong, 0x1EC30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_92(0x0000, 0x000C, 0x00000000, 0x00000BB8, 0x00)
    OP_8C(0x000A, 180, 0)
    Sleep(50)

    EventEnd(0x04)
    OP_4B(0x000A, 255)
    ClearChrFlags(0x000A, 0x0040)

    def _loc_1E47(): pass

    label('loc_1E47')

    Return()

# id: 0x000E offset: 0x1E48
@scena.Code('func_0E_1E48')
def func_0E_1E48():
    FadeOut(0, 0, -1)
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
        (0x00000000, 'loc_1EC2'),
        (0x00000001, 'loc_1EC8'),
        (-1, 'loc_1ECE'),
    )

    def _loc_1EC2(): pass

    label('loc_1EC2')

    OP_A2(0x1200)

    Jump('loc_1ECE')

    def _loc_1EC8(): pass

    label('loc_1EC8')

    OP_A2(0x1201)

    Jump('loc_1ECE')

    def _loc_1ECE(): pass

    label('loc_1ECE')

    Return()

# id: 0x000F offset: 0x1ECF
@scena.Code('func_0F_1ECF')
def func_0F_1ECF():
    FadeOut(0, 0, -1)
    OP_6D(55450, 4000, 13070, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0010 offset: 0x1F5E
@scena.Code('func_10_1F5E')
def func_10_1F5E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2040',
    )

    EventBegin(0x00)
    Fade(500)
    ClearMapFlags(0x00000001)
    OP_6D(-40, 4000, -8710, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x0101, 850, 4000, -10070, 0)
    SetChrPos(0x0102, -360, 4000, -10110, 0)
    SetChrPos(0x00F8, 820, 3600, -11500, 0)
    SetChrPos(0x00F9, -450, 3600, -11500, 0)
    CreateThread(0x0101, 0x00, 0x00, 0x0011)
    Sleep(300)

    CreateThread(0x0102, 0x00, 0x00, 0x0012)
    Sleep(300)

    CreateThread(0x00F8, 0x00, 0x00, 0x0013)
    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, 0x0014)
    WaitForThreadExit(0x0003, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x02000000)
    NewScene('ED6_DT21/C0700._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2040(): pass

    label('loc_2040')

    Return()

# id: 0x0011 offset: 0x2041
@scena.Code('func_11_2041')
def func_11_2041():
    OP_91(0x00FE, 0, 0, 1800, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_2086')
    def lambda_2086():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2086)

    @scena.Lambda('lambda_20A0')
    def lambda_20A0():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_20A0)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0012 offset: 0x20C6
@scena.Code('func_12_20C6')
def func_12_20C6():
    OP_91(0x00FE, 0, 0, 1800, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_210B')
    def lambda_210B():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_210B)

    @scena.Lambda('lambda_2125')
    def lambda_2125():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2125)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0013 offset: 0x214B
@scena.Code('func_13_214B')
def func_13_214B():
    OP_91(0x00FE, 0, 0, 2800, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_2190')
    def lambda_2190():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2190)

    @scena.Lambda('lambda_21AA')
    def lambda_21AA():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_21AA)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0014 offset: 0x21D0
@scena.Code('func_14_21D0')
def func_14_21D0():
    OP_91(0x00FE, 0, 0, 2800, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0001)
    OP_7D(0x00, 0x00FE, 0x0032, 0x01F4)
    OP_22(0x0099, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0004)
    OP_91(0x00FE, 0, 500, 0, 0, 0x00)

    @scena.Lambda('lambda_2215')
    def lambda_2215():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2215)

    @scena.Lambda('lambda_222F')
    def lambda_222F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000005DC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_222F)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_91(0x00FE, 0, 2500, 0, 5000, 0x00)

    Return()

# id: 0x0015 offset: 0x2255
@scena.Code('func_15_2255')
def func_15_2255():
    EventBegin(0x00)
    OP_6D(-40, 4000, -8710, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x0101, 500, 4400, -7000, 180)
    SetChrPos(0x0102, -500, 4400, -7000, 180)
    SetChrPos(0x00F8, 500, 4400, -7000, 180)
    SetChrPos(0x00F9, -500, 4400, -7000, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x0101, 0x0001)
    ClearChrFlags(0x0102, 0x0001)
    ClearChrFlags(0x00F8, 0x0001)
    ClearChrFlags(0x00F9, 0x0001)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0101, 0x00, 0x00, 0x0016)
    Sleep(800)

    CreateThread(0x0102, 0x00, 0x00, 0x0017)
    Sleep(800)

    CreateThread(0x00F8, 0x00, 0x00, 0x0018)
    Sleep(800)

    CreateThread(0x00F9, 0x00, 0x00, 0x0019)
    WaitForThreadExit(0x00F9, 0x0000)
    Fade(500)
    OP_6D(100, 4000, -10180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 100, 4000, -10180, 180)
    SetChrPos(0x0001, 100, 4000, -10180, 180)
    SetChrPos(0x0002, 100, 4000, -10180, 180)
    SetChrPos(0x0003, 100, 4000, -10180, 180)
    OP_0D()
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0016 offset: 0x23E1
@scena.Code('func_16_23E1')
def func_16_23E1():
    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_23EC')
    def lambda_23EC():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_23EC)

    @scena.Lambda('lambda_2406')
    def lambda_2406():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2406)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_2427')
    def lambda_2427():
        OP_8F(0x00FE, 500, 4000, -11570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2427)

    WaitForThreadExit(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0017 offset: 0x2447
@scena.Code('func_17_2447')
def func_17_2447():
    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_2452')
    def lambda_2452():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2452)

    @scena.Lambda('lambda_246C')
    def lambda_246C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_246C)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_248D')
    def lambda_248D():
        OP_8F(0x00FE, -500, 4000, -11570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_248D)

    WaitForThreadExit(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0018 offset: 0x24AD
@scena.Code('func_18_24AD')
def func_18_24AD():
    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_24B8')
    def lambda_24B8():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_24B8)

    @scena.Lambda('lambda_24D2')
    def lambda_24D2():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_24D2)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_24F3')
    def lambda_24F3():
        OP_8F(0x00FE, 500, 3600, -10600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_24F3)

    WaitForThreadExit(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x0019 offset: 0x2513
@scena.Code('func_19_2513')
def func_19_2513():
    OP_22(0x0099, 0x00, 0x64)

    @scena.Lambda('lambda_251E')
    def lambda_251E():
        OP_9E(0x00FE, 0x00000000, 0x00000064, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_251E)

    @scena.Lambda('lambda_2538')
    def lambda_2538():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_2538)

    WaitForThreadExit(0x00FE, 0x0002)
    SetChrFlags(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0001)

    @scena.Lambda('lambda_2559')
    def lambda_2559():
        OP_8F(0x00FE, -500, 3600, -10600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2559)

    WaitForThreadExit(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
