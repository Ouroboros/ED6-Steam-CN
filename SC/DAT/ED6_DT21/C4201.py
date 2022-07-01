import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '恶魔流体'),
    TXT(0x02, '命运编造者'),
    TXT(0x03, '泥泞食人树'),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4201.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xF9A
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
        ('ED6_DT29/CH13040._CH', 'ED6_DT29/CH13040P._CP'),
        ('ED6_DT29/CH13041._CH', 'ED6_DT29/CH13041P._CP'),
        ('ED6_DT09/CH10990._CH', 'ED6_DT09/CH10990P._CP'),
        ('ED6_DT09/CH10991._CH', 'ED6_DT09/CH10991P._CP'),
        ('ED6_DT09/CH10250._CH', 'ED6_DT09/CH10250P._CP'),
        ('ED6_DT09/CH10251._CH', 'ED6_DT09/CH10251P._CP'),
    ]

# id: 0x10002 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 132640,
            z                   = 0,
            y                   = -146070,
            direction           = 90,
            word_0E             = 16,
            dword_10            = 1048576,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 131960,
            z                   = 0,
            y                   = 21060,
            direction           = 90,
            word_0E             = 18,
            dword_10            = 1179648,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 119240,
            z                   = 0,
            y                   = 5950,
            direction           = 270,
            word_0E             = 20,
            dword_10            = 1310720,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 139310,
            z           = 0,
            y           = 6070,
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
            x           = 104120,
            z           = 0,
            y           = 13980,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0273,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1F2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 129800,
            y           = -1000,
            z           = -148400,
            range       = 136100,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFDCF74,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 135300,
            y           = -1000,
            z           = 23750,
            range       = 137100,
            dword_10    = 0x000007D0,
            dword_14    = 0x00004A1A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = 114460,
            y           = -1000,
            z           = 2260,
            range       = 116360,
            dword_10    = 0x000007D0,
            dword_14    = 0x000022F6,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10005 offset: 0x252
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 118070,
            triggerZ            = 0,
            triggerY            = 19130,
            triggerRange        = 1000,
            actorX              = 118680,
            actorZ              = 1500,
            actorY              = 19250,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 123780,
            triggerZ            = 0,
            triggerY            = 19220,
            triggerRange        = 1000,
            actorX              = 122910,
            actorZ              = 1500,
            actorY              = 19200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 103870,
            triggerZ            = 0,
            triggerY            = 24400,
            triggerRange        = 1000,
            actorX              = 103830,
            actorZ              = 1500,
            actorY              = 24960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 136410,
            triggerZ            = 0,
            triggerY            = -112150,
            triggerRange        = 1000,
            actorX              = 137180,
            actorZ              = 1500,
            actorY              = -112180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 128250,
            triggerZ            = 0,
            triggerY            = -152730,
            triggerRange        = 1000,
            actorX              = 127270,
            actorZ              = 1500,
            actorY              = -152920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x306
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x307
@scena.Code('Init')
def Init():
    OP_6F(0x0000, 0)
    OP_6F(0x0003, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 4, 0x1714)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_327',
    )

    OP_6F(0x0001, 0)

    Jump('loc_32E')

    def _loc_327(): pass

    label('loc_327')

    OP_6F(0x0001, 60)

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 6, 0x1716)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_340',
    )

    OP_6F(0x0002, 0)

    Jump('loc_347')

    def _loc_340(): pass

    label('loc_340')

    OP_6F(0x0002, 60)

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 0, 0x1718)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_359',
    )

    OP_6F(0x0004, 0)

    Jump('loc_360')

    def _loc_359(): pass

    label('loc_359')

    OP_6F(0x0004, 60)

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 1, 0x1719)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_372',
    )

    OP_6F(0x0005, 0)

    Jump('loc_379')

    def _loc_372(): pass

    label('loc_372')

    OP_6F(0x0005, 60)

    def _loc_379(): pass

    label('loc_379')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_397',
    )

    SetChrFlags(0x0009, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)

    Jump('loc_3A9')

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 5, 0x16FD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A9',
    )

    ClearChrFlags(0x0009, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)

    def _loc_3A9(): pass

    label('loc_3A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3C7',
    )

    SetChrFlags(0x000A, 0x0080)
    OP_B2(0x00, 0x02, 0x0080)

    Jump('loc_3D9')

    def _loc_3C7(): pass

    label('loc_3C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 6, 0x16FE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D9',
    )

    ClearChrFlags(0x000A, 0x0080)
    OP_B2(0x01, 0x02, 0x0080)

    def _loc_3D9(): pass

    label('loc_3D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_408',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x70),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F3',
    )

    OP_8C(0x0008, 270, 0)

    def _loc_3F3(): pass

    label('loc_3F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 6, 0x20FE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_405',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_405(): pass

    label('loc_405')

    Jump('loc_412')

    def _loc_408(): pass

    label('loc_408')

    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    def _loc_412(): pass

    label('loc_412')

    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x418
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_42D',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_42D(): pass

    label('loc_42D')

    Return()

# id: 0x0003 offset: 0x42E
@scena.Code('func_03_42E')
def func_03_42E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 5, 0x16FD)),
            Expr.Return,
        ),
        'loc_436',
    )

    Return()

    def _loc_436(): pass

    label('loc_436')

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
        (0x00000001, 'loc_51B'),
        (-1, 'loc_53E'),
    )

    def _loc_51B(): pass

    label('loc_51B')

    Fade(500)
    OP_89(0x0000, 140060, 0, 20720, 270)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_53E(): pass

    label('loc_53E')

    Battle(0x00000EE7, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 140060, 0, 20720, 270)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_577'),
        (0x00000001, 'loc_57A'),
        (-1, 'loc_57D'),
    )

    def _loc_577(): pass

    label('loc_577')

    EventEnd(0x00)

    Return()

    def _loc_57A(): pass

    label('loc_57A')

    OP_B4(0x00)

    Return()

    def _loc_57D(): pass

    label('loc_57D')

    EventBegin(0x01)
    SetChrFlags(0x0009, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
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
    OP_A2(0x16FD)
    OP_28(0x00AB, 0x04, 0x10)
    OP_28(0x00AB, 0x04, 0x02)
    OP_28(0x00AB, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x5E9
@scena.Code('func_04_5E9')
def func_04_5E9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 6, 0x16FE)),
            Expr.Return,
        ),
        'loc_5F1',
    )

    Return()

    def _loc_5F1(): pass

    label('loc_5F1')

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
        (0x00000001, 'loc_6D6'),
        (-1, 'loc_6F9'),
    )

    def _loc_6D6(): pass

    label('loc_6D6')

    Fade(500)
    OP_89(0x0000, 111820, 0, 6100, 90)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_6F9(): pass

    label('loc_6F9')

    Battle(0x00000EE8, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 111820, 0, 6100, 90)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_732'),
        (0x00000001, 'loc_735'),
        (-1, 'loc_738'),
    )

    def _loc_732(): pass

    label('loc_732')

    EventEnd(0x00)

    Return()

    def _loc_735(): pass

    label('loc_735')

    OP_B4(0x00)

    Return()

    def _loc_738(): pass

    label('loc_738')

    EventBegin(0x01)
    SetChrFlags(0x000A, 0x0080)
    OP_B2(0x00, 0x02, 0x0080)
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
    OP_A2(0x16FE)
    OP_28(0x00AC, 0x04, 0x10)
    OP_28(0x00AC, 0x04, 0x02)
    OP_28(0x00AC, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x7A4
@scena.Code('func_05_7A4')
def func_05_7A4():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000070, 'loc_7B4'),
        (0x00000072, 'loc_906'),
        (-1, 'loc_A58'),
    )

    def _loc_7B4(): pass

    label('loc_7B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 6, 0x20FE)),
            Expr.Return,
        ),
        'loc_7BC',
    )

    Return()

    def _loc_7BC(): pass

    label('loc_7BC')

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
        (0x00000001, 'loc_8A1'),
        (-1, 'loc_8C4'),
    )

    def _loc_8A1(): pass

    label('loc_8A1')

    Fade(500)
    OP_89(0x0000, 127130, 0, -146140, 90)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_8C4(): pass

    label('loc_8C4')

    Battle(0x00000EFC, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 127130, 0, -146140, 90)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_8FD'),
        (0x00000001, 'loc_900'),
        (-1, 'loc_903'),
    )

    def _loc_8FD(): pass

    label('loc_8FD')

    EventEnd(0x00)

    Return()

    def _loc_900(): pass

    label('loc_900')

    OP_B4(0x00)

    Return()

    def _loc_903(): pass

    label('loc_903')

    Jump('loc_A58')

    def _loc_906(): pass

    label('loc_906')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 6, 0x20FE)),
            Expr.Return,
        ),
        'loc_90E',
    )

    Return()

    def _loc_90E(): pass

    label('loc_90E')

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
        (0x00000001, 'loc_9F3'),
        (-1, 'loc_A16'),
    )

    def _loc_9F3(): pass

    label('loc_9F3')

    Fade(500)
    OP_89(0x0000, 138840, 0, -146140, 270)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_A16(): pass

    label('loc_A16')

    Battle(0x00000EF5, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 138840, 0, -146140, 270)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_A4F'),
        (0x00000001, 'loc_A52'),
        (-1, 'loc_A55'),
    )

    def _loc_A4F(): pass

    label('loc_A4F')

    EventEnd(0x00)

    Return()

    def _loc_A52(): pass

    label('loc_A52')

    OP_B4(0x00)

    Return()

    def _loc_A55(): pass

    label('loc_A55')

    Jump('loc_A58')

    def _loc_A58(): pass

    label('loc_A58')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
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
    OP_A2(0x20FE)
    OP_28(0x00BD, 0x04, 0x10)
    OP_28(0x00BD, 0x04, 0x02)
    OP_28(0x00BD, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xAC4
@scena.Code('func_06_AC4')
def func_06_AC4():
    UnlockAchievement(0x02, 0x00, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 4, 0x1714)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BA1',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['火绒草长靴'], 1)"),
            Expr.Return,
        ),
        'loc_B38',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['火绒草长靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1714)

    Jump('loc_B9E')

    def _loc_B38(): pass

    label('loc_B38')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['火绒草长靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['火绒草长靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_B9E(): pass

    label('loc_B9E')

    Jump('loc_BD2')

    def _loc_BA1(): pass

    label('loc_BA1')

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
    def _loc_BD2(): pass

    label('loc_BD2')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xBE0
@scena.Code('func_07_BE0')
def func_07_BE0():
    UnlockAchievement(0x02, 0x01, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E2, 6, 0x1716)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CBD',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['诡异之星'], 1)"),
            Expr.Return,
        ),
        'loc_C54',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['诡异之星']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1716)

    Jump('loc_CBA')

    def _loc_C54(): pass

    label('loc_C54')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['诡异之星']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['诡异之星']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_CBA(): pass

    label('loc_CBA')

    Jump('loc_CEE')

    def _loc_CBD(): pass

    label('loc_CBD')

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
    def _loc_CEE(): pass

    label('loc_CEE')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xCFC
@scena.Code('func_08_CFC')
def func_08_CFC():
    UnlockAchievement(0x02, 0x02, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 0, 0x1718)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DD9',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['还魂胶囊'], 1)"),
            Expr.Return,
        ),
        'loc_D70',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1718)

    Jump('loc_DD6')

    def _loc_D70(): pass

    label('loc_D70')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)

    def _loc_DD6(): pass

    label('loc_DD6')

    Jump('loc_E0A')

    def _loc_DD9(): pass

    label('loc_DD9')

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
    def _loc_E0A(): pass

    label('loc_E0A')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xE18
@scena.Code('func_09_E18')
def func_09_E18():
    UnlockAchievement(0x02, 0x03, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E3, 1, 0x1719)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EF5',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_E8C',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1719)

    Jump('loc_EF2')

    def _loc_E8C(): pass

    label('loc_E8C')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)

    def _loc_EF2(): pass

    label('loc_EF2')

    Jump('loc_F26')

    def _loc_EF5(): pass

    label('loc_EF5')

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
    def _loc_F26(): pass

    label('loc_F26')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xF34
@scena.Code('func_0A_F34')
def func_0A_F34():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉杆很紧，扳不动。',
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
