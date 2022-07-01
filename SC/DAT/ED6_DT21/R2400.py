import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2400   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卢安方向'),
    TXT(0x02, '艾尔·雷登关所方向'),
    TXT(0x03, '绀碧之塔方向'),
    TXT(0x04, '野马'),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2400.x'
    header.mapIndex       = 103
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5A9
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
        ('ED6_DT09/CH10520._CH', 'ED6_DT09/CH10520P._CP'),
        ('ED6_DT09/CH10521._CH', 'ED6_DT09/CH10521P._CP'),
        ('ED6_DT29/CH12040._CH', 'ED6_DT29/CH12040P._CP'),
        ('ED6_DT29/CH12041._CH', 'ED6_DT29/CH12041P._CP'),
        ('ED6_DT09/CH10340._CH', 'ED6_DT09/CH10340P._CP'),
        ('ED6_DT09/CH10341._CH', 'ED6_DT09/CH10341P._CP'),
        ('ED6_DT09/CH11040._CH', 'ED6_DT09/CH11040P._CP'),
        ('ED6_DT09/CH11041._CH', 'ED6_DT09/CH11041P._CP'),
        ('ED6_DT09/CH11070._CH', 'ED6_DT09/CH11070P._CP'),
        ('ED6_DT09/CH11071._CH', 'ED6_DT09/CH11071P._CP'),
        ('ED6_DT09/CH11080._CH', 'ED6_DT09/CH11080P._CP'),
        ('ED6_DT09/CH11081._CH', 'ED6_DT09/CH11081P._CP'),
        ('ED6_DT09/CH11020._CH', 'ED6_DT09/CH11020P._CP'),
        ('ED6_DT09/CH11021._CH', 'ED6_DT09/CH11021P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -23690,
            z                   = 0,
            y                   = 116780,
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
            x                   = 15400,
            z                   = 0,
            y                   = 4440,
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
            x                   = -104100,
            z                   = 10,
            y                   = 74970,
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
            x                   = -8500,
            z                   = 710,
            y                   = 63340,
            direction           = 264,
            word_0E             = 12,
            dword_10            = 786432,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -14830,
            z           = -70,
            y           = 77800,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01AA,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28100,
            z           = 190,
            y           = 43720,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01A5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -15760,
            z           = -60,
            y           = 37690,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01A7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28480,
            z           = 130,
            y           = 9940,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01A9,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -14420,
            z           = 200,
            y           = 18840,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01AA,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -40650,
            z           = 450,
            y           = 58610,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01A5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -66830,
            z           = 20,
            y           = 39070,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01AA,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x25E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -8500,
            y           = -1000,
            z           = 63340,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x27E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -31880,
            triggerZ            = 0,
            triggerY            = 74800,
            triggerRange        = 1500,
            actorX              = -31880,
            actorZ              = 1400,
            actorY              = 74800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -28300,
            triggerZ            = 0,
            triggerY            = 68920,
            triggerRange        = 1500,
            actorX              = -28300,
            actorZ              = 1500,
            actorY              = 68920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2C6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x2C7
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFD73A8, 0xFFFECF50, 0x00230023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2F7',
    )

    SetChrFlags(0x000B, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_309')

    def _loc_2F7(): pass

    label('loc_2F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 5, 0x12FD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_309',
    )

    ClearChrFlags(0x000B, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_309(): pass

    label('loc_309')

    Return()

# id: 0x0002 offset: 0x30A
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_31F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_31F(): pass

    label('loc_31F')

    Return()

# id: 0x0003 offset: 0x320
@scena.Code('func_03_320')
def func_03_320():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 5, 0x12FD)),
            Expr.Return,
        ),
        'loc_328',
    )

    Return()

    def _loc_328(): pass

    label('loc_328')

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
        (0x00000001, 'loc_40D'),
        (-1, 'loc_430'),
    )

    def _loc_40D(): pass

    label('loc_40D')

    Fade(500)
    OP_89(0x0000, -15310, 0, 63620, 90)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_430(): pass

    label('loc_430')

    Battle(0x00000EE0, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -15310, 0, 63620, 90)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_469'),
        (0x00000001, 'loc_46C'),
        (-1, 'loc_46F'),
    )

    def _loc_469(): pass

    label('loc_469')

    EventEnd(0x00)

    Return()

    def _loc_46C(): pass

    label('loc_46C')

    OP_B4(0x00)

    Return()

    def _loc_46F(): pass

    label('loc_46F')

    EventBegin(0x01)
    SetChrFlags(0x000B, 0x0080)
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
    OP_A2(0x12FD)
    OP_28(0x00A4, 0x04, 0x10)
    OP_28(0x00A4, 0x04, 0x02)
    OP_28(0x00A4, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x4DB
@scena.Code('func_04_4DB')
def func_04_4DB():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　绀碧之塔\n',
            '※魔兽很多，危险！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0005 offset: 0x52D
@scena.Code('func_05_52D')
def func_05_52D():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　卢安市　　　　１０５塞尔矩\n',
            '南　艾尔·雷登　　　７０塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
